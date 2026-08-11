import contextlib
import datetime as dt
import ftplib
import threading
import time
from collections.abc import Callable, Iterable
from functools import lru_cache
from pathlib import Path

from quantilica.core.exceptions import FetchError
from quantilica.core.files import is_complete_file
from quantilica.core.ftp import FTP_TRANSIENT_ERRORS, FtpClient, MonitoredFTP
from quantilica.core.manifests import DownloadManifest
from quantilica.core.retry import exponential_delay
from tqdm import tqdm as _tqdm

try:
    from quantilica.cli.ui import (
        ProgressPool,
        get_console,
        graceful_executor,
        make_batch_progress,
        make_download_progress,
    )
    from rich.console import Group
    from rich.live import Live

    _RICH_AVAILABLE = True
except (ModuleNotFoundError, ImportError):  # pragma: no cover
    _RICH_AVAILABLE = False

from datasus_fetcher.slicer import Slicer

from . import logger, meta
from .remote_names import get_pattern, parse_filename
from .storage import (
    DataPartition,
    RemoteFile,
    get_data_filepath,
)

FTP_HOST = "ftp.datasus.gov.br"
FTP_TIMEOUT = 60.0
MEGA = 1_000_000
_IDLE_TIMEOUT = 90.0  # segundos sem bytes recebidos antes de declarar stall

# Erros que justificam reconectar e re-tentar o arquivo no nível do worker.
# fetch_file converte o esgotamento de transitórios em FetchError, então
# precisamos incluí-lo aqui (FetchError não é um FTP_TRANSIENT_ERRORS).
_RETRYABLE_DOWNLOAD_ERRORS: tuple[type[BaseException], ...] = (
    FetchError,
    *FTP_TRANSIENT_ERRORS,
)


class _Aborted(Exception):
    """Raised when an in-flight download is interrupted by the user."""


def log_download(tt: float, size: int, filename: str):
    filesize_mb = size / MEGA
    download_speed_mbps = (size * 8) / tt / MEGA
    log = " ".join(
        [
            f"{filename: <40}",
            f"{filesize_mb: >6.2f} MB",
            f"{tt: >5.2f} s",
            f"{download_speed_mbps: >5.2f} Mb/s",
        ]
    )
    logger.info(log)


def connect(timeout: float = FTP_TIMEOUT, attempts: int = 3) -> MonitoredFTP:
    last_exc: BaseException | None = None
    for attempt in range(1, attempts + 1):
        try:
            ftp = MonitoredFTP(FTP_HOST, timeout=timeout, encoding="latin-1")
            ftp.login()
            return ftp
        except FTP_TRANSIENT_ERRORS as exc:
            last_exc = exc
            if attempt == attempts:
                break
            time.sleep(
                exponential_delay(attempt, base_delay=2.0, max_delay=30.0, jitter=1.0)
            )
    raise FetchError(
        f"Could not connect to {FTP_HOST} after {attempts} attempts"
    ) from last_exc


@lru_cache
def list_files(
    ftp: ftplib.FTP,
    directory: str,
    retries: int = 3,
    max_recursive_depth: int = 3,
) -> list[dict]:
    files: list[str] = []
    max_retries = retries
    attempt = 0
    while retries > 0:
        attempt += 1
        files.clear()
        try:
            ftp.cwd(directory)
            ftp.retrlines("LIST", files.append)
            break
        except ftplib.error_perm:
            logger.exception("Directory not found: %s", directory)
            return []
        except FTP_TRANSIENT_ERRORS:
            logger.exception(
                "Transient error listing files (attempt %d/%d).",
                attempt,
                max_retries,
            )
            retries -= 1
            if retries <= 0:
                raise
            time.sleep(
                exponential_delay(attempt, base_delay=2.0, max_delay=30.0, jitter=1.0)
            )

    # parse files' date, size and name
    def parse_line(line: str) -> dict[str, str | int | dt.datetime | None]:
        date, t, size, name = line.split(maxsplit=3)
        if "." in name:
            extension = name.rsplit(".", maxsplit=1)[1].lower()
        else:
            extension = None
        datetime = dt.datetime.strptime(date + " " + t, "%m-%d-%y %I:%M%p")
        try:
            size = int(size)
        except ValueError:
            logger.warning("Could not parse size for file %s in %s", name, directory)
            size = 0
        return {
            "datetime": datetime,
            "size": size,
            "filename": name,
            "extension": extension,
            "full_path": f"{directory}/{name}",
        }

    dirs = []
    parsed_files = []
    for line in files:
        if "<DIR>" not in line:
            parsed_files.append(parse_line(line))
        else:
            *_, name = line.split(maxsplit=3)
            dirs.append(name)
    for d in dirs:
        if max_recursive_depth > 0:
            parsed_files.extend(
                list_files(
                    ftp,
                    f"{directory}/{d}",
                    retries=retries,
                    max_recursive_depth=max_recursive_depth - 1,
                )
            )

    return parsed_files


def list_dataset_files(ftp: ftplib.FTP, dataset: str) -> list[RemoteFile]:
    dataset_files = []
    for period in meta.datasets[dataset]["periods"]:
        files = [
            RemoteFile(
                filename=f["filename"],
                datetime=f["datetime"],
                size=f["size"],
                extension=f["extension"],
                full_path=f["full_path"],
                dataset=dataset,
                preliminary=period.get("preliminary", False),
            )
            for f in list_files(ftp, directory=period["dir"], retries=3)
        ]
        if not period["filename_pattern"]:
            dataset_files.extend(files)
            continue
        fn_pattern = period["filename_pattern"]
        pattern = get_pattern(period=period)
        for file in files:
            m = pattern.match(file.filename.lower())
            if m:
                file.partition = DataPartition(**parse_filename(m, fn_pattern))
                dataset_files.append(file)
    return dataset_files


def download_data(
    datasets: Iterable[str],
    destdir: Path,
    threads: int = 2,
    callback: Callable | None = None,
    slicer: Slicer | None = None,
    show_progress: bool = False,
):
    """Multithreaded download data files, dataset by dataset."""
    logger.info("Starting download with %s threads", threads)
    datasets_ = (
        set(datasets) & set(meta.datasets.keys())
        if datasets
        else set(meta.datasets.keys())
    )

    ftp0 = connect()
    failed_files: list[str] = []

    live = None
    batch_progress = None
    file_progress = None
    pool = None

    if show_progress and _RICH_AVAILABLE:
        console = get_console()
        batch_progress = make_batch_progress(console)
        file_progress = make_download_progress(console)
        pool = ProgressPool(workers=threads, file_prog=file_progress)
        live = Live(
            Group(batch_progress, file_progress),
            console=console,
            refresh_per_second=10,
        )
        live.start()

    thread_local = threading.local()

    def get_ftp() -> ftplib.FTP:
        if not hasattr(thread_local, "ftp"):
            thread_local.ftp = connect()
        return thread_local.ftp

    def _worker(file: RemoteFile) -> dict | None:
        filepath: Path = get_data_filepath(destdir, file)
        if is_complete_file(filepath, file.size):
            return None

        ctx = (
            pool.acquire(description=f"[cyan]{filepath.name}[/cyan]")
            if pool
            else contextlib.nullcontext()
        )
        try:
            with ctx as cb:
                downloaded_bytes = 0

                def chunk_cb(n: int) -> None:
                    nonlocal downloaded_bytes
                    downloaded_bytes += n
                    if cb is not None:
                        cb(downloaded_bytes, file.size)

                t0 = time.time()
                client = FtpClient(FTP_HOST, timeout=FTP_TIMEOUT)
                url = f"ftp://{FTP_HOST}/{file.full_path}"
                client.download_with_manifest(
                    url=file.full_path,
                    target_path=filepath,
                    source_id="datasus",
                    dataset_id=file.dataset,
                    producer="datasus-fetcher",
                    metadata={
                        "partition": str(file.partition),
                        "preliminary": file.preliminary,
                        "remote_datetime": file.datetime.isoformat(),
                    },
                    progress=chunk_cb,
                )

                tt = time.time() - t0
                log_download(tt, file.size, filepath.name)

                try:
                    manifest_path = filepath.with_suffix(
                        filepath.suffix + ".manifest.json"
                    )
                    manifest = DownloadManifest.from_file(manifest_path)
                except Exception:
                    manifest = None

                res = {
                    "url": url,
                    "size": file.size,
                    "filepath": filepath,
                    "suffix": file.extension,
                    "dataset": file.dataset,
                    "created_at": file.datetime,
                    "manifest": manifest,
                }
                if callback:
                    callback(res)
                return res
        except Exception as exc:
            logger.error("Worker failed for %s: %s", file.full_path, exc)
            failed_files.append(file.full_path)
            return None

    try:
        import concurrent.futures

        exec_ctx = (
            graceful_executor(max_workers=threads)
            if _RICH_AVAILABLE
            else concurrent.futures.ThreadPoolExecutor(max_workers=threads)
        )

        with exec_ctx as executor:
            for dataset in sorted(datasets_):
                logger.info("Listing files of %s", dataset)

                def _needs_download(f: RemoteFile) -> bool:
                    fp = get_data_filepath(destdir, f)
                    return not is_complete_file(fp, f.size)

                attempts = 3
                while attempts > 0:
                    try:
                        dataset_files = [
                            f
                            for f in list_dataset_files(ftp0, dataset)
                            if (slicer is None or slicer(f)) and _needs_download(f)
                        ]
                        break
                    except FTP_TRANSIENT_ERRORS:
                        attempts -= 1
                        if attempts <= 0:
                            raise
                        logger.warning(
                            "Transient error listing %s. Reconnecting...", dataset
                        )
                        with contextlib.suppress(Exception):
                            ftp0.close()
                        ftp0 = connect()

                if not dataset_files:
                    continue

                batch_task = None
                pbar = None
                if show_progress:
                    if batch_progress is not None:
                        batch_task = batch_progress.add_task(
                            f"[cyan]{dataset}[/cyan]", total=len(dataset_files)
                        )
                    else:
                        total_bytes = sum(f.size for f in dataset_files)
                        pbar = _tqdm(
                            total=total_bytes,
                            desc=dataset,
                            unit="B",
                            unit_scale=True,
                            unit_divisor=1024,
                            leave=True,
                        )

                futures = [executor.submit(_worker, f) for f in dataset_files]
                for future in concurrent.futures.as_completed(futures):
                    res = future.result()
                    if batch_task is not None:
                        batch_progress.update(batch_task, advance=1)
                    if pbar is not None and res is not None:
                        pbar.update(res["size"])

                if pbar is not None:
                    pbar.close()

    except KeyboardInterrupt:
        import sys

        print("\nDownload interrompido pelo usuário.")
        sys.exit(130)
    finally:
        if live is not None:
            with contextlib.suppress(Exception):
                live.stop()
        with contextlib.suppress(Exception):
            ftp0.close()
        if failed_files:
            logger.warning(
                "%d arquivo(s) falharam permanentemente após todas as tentativas:\n%s",
                len(failed_files),
                "\n".join(f"  {p}" for p in sorted(failed_files)),
            )


def _list_support_files(ftp: ftplib.FTP, ftp_dirs: list[str]) -> list[dict]:
    files = []
    for ftp_dir in ftp_dirs:
        files.extend(list_files(ftp, directory=ftp_dir))
    return files


def _download_support_files(
    ftp: ftplib.FTP,
    files: list[dict],
    destdir: Path,
    *,
    connect_fn: Callable[[], ftplib.FTP] = connect,
):
    for i, file in enumerate(files):
        filename, extension = file["filename"].rsplit(".", 1)
        filename = f"{filename}@{file['datetime']:%Y%m%d}.{extension}"
        filepath = destdir / filename

        if is_complete_file(filepath, file["size"]):
            continue

        logger.debug(f"{i: >5} {file['full_path']} -> {filepath}")
        t0 = time.time()

        client = FtpClient(FTP_HOST, timeout=FTP_TIMEOUT)
        url = f"ftp://{FTP_HOST}/{file['full_path']}"
        client.download_with_manifest(
            url=file["full_path"],
            target_path=filepath,
            source_id="datasus",
            dataset_id=destdir.name,
            producer="datasus-fetcher",
            metadata={"remote_datetime": file["datetime"].isoformat()},
        )

        tt = time.time() - t0
        filesize_kb = f"{file['size'] / 1024:.2f} kB"
        download_speed_kbps = f"{file['size'] / tt / 1024:.2f} kB/s"
        logger.debug(
            f"      {filename} {tt:.2f} s {filesize_kb} {download_speed_kbps}",
        )

        try:
            manifest_path = filepath.with_suffix(filepath.suffix + ".manifest.json")
            manifest = DownloadManifest.from_file(manifest_path)
        except Exception:
            manifest = None

        yield {
            "url": url,
            "size": file["size"],
            "filepath": filepath,
            "created_at": file["datetime"],
            "suffix": extension,
            "manifest": manifest,
        }


def list_documentation_files(ftp: ftplib.FTP, dataset: str) -> list[dict]:
    return _list_support_files(ftp, meta.docs[dataset]["dir"])


def download_documentation(
    ftp: ftplib.FTP,
    dataset: str,
    destdir: Path,
):
    files = list_documentation_files(ftp, dataset)
    yield from _download_support_files(ftp, files, destdir / "_documentacao" / dataset)


def list_auxiliary_tables_files(ftp: ftplib.FTP, dataset: str) -> list[dict]:
    return _list_support_files(ftp, meta.auxiliary_tables[dataset]["dir"])


def download_auxiliary_tables(
    ftp: ftplib.FTP,
    dataset: str,
    destdir: Path,
):
    files = list_auxiliary_tables_files(ftp, dataset)
    yield from _download_support_files(ftp, files, destdir / "_auxiliar" / dataset)
