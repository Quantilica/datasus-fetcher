import contextlib
import datetime as dt
import ftplib
import queue
import threading
import time
from collections.abc import Callable, Iterable
from functools import lru_cache
from pathlib import Path

import quantilica_core.metadata as core_meta
from quantilica_core.exceptions import FetchError
from quantilica_core.files import is_complete_file
from quantilica_core.ftp import FTP_TRANSIENT_ERRORS, ftp_connect
from quantilica_core.manifests import DownloadManifest
from quantilica_core.retry import exponential_delay
from tqdm import tqdm as _tqdm

from datasus_fetcher.slicer import Slicer

from . import logger, meta
from .remote_names import get_pattern, parse_filename
from .storage import (
    DataPartition,
    DataRepository,
    RemoteFile,
    get_data_filepath,
)

FTP_HOST = "ftp.datasus.gov.br"
FTP_TIMEOUT = 60.0
MEGA = 1_000_000

# Erros que justificam reconectar e re-tentar o arquivo no nível do worker.
# fetch_file converte o esgotamento de transitórios em FetchError, então
# precisamos incluí-lo aqui (FetchError não é um FTP_TRANSIENT_ERRORS).
_RETRYABLE_DOWNLOAD_ERRORS: tuple[type[BaseException], ...] = (
    FetchError,
    *FTP_TRANSIENT_ERRORS,
)


class _Aborted(Exception):
    """Raised when an in-flight download is interrupted by the user."""


class Fetcher(threading.Thread):
    def __init__(
        self,
        q: queue.Queue,
        dest_dir: Path,
        callback: Callable | None = None,
        failed_files: list[str] | None = None,
    ):
        super().__init__()
        self.daemon = True
        self.ftp: ftplib.FTP | None = None
        self.q = q
        self.repo = DataRepository(dest_dir)
        if callable(callback):
            self.callback = callback
        else:
            self.callback = lambda _: None
        self._kill_event = threading.Event()
        self._failed_files: list[str] = failed_files if failed_files is not None else []

    def run(self):
        self.ftp = connect()
        try:
            while True:
                try:
                    file: RemoteFile | None = self.q.get(timeout=0.5)
                except queue.Empty:
                    if self.dead():
                        return
                    continue

                if file is None:
                    self.q.task_done()
                    return

                if self.dead():
                    self.q.task_done()
                    continue

                filepath: Path = self.repo.get_data_filepath(file=file)
                if is_complete_file(filepath, file.size):
                    self.q.task_done()
                    continue

                try:
                    self._download_one(file, filepath)
                except _Aborted:
                    logger.info("Aborted download of %s", file.full_path)
                    return
                except ftplib.error_perm:
                    logger.exception(
                        "Permanent FTP error for %s — skipping.",
                        file.full_path,
                    )
                except _RETRYABLE_DOWNLOAD_ERRORS as exc:
                    logger.warning(
                        "Transient error for %s: %s. Reconnecting...",
                        file.full_path,
                        exc,
                    )
                    with contextlib.suppress(Exception):
                        self.ftp.close()
                    try:
                        self.ftp = connect()
                    except FetchError:
                        logger.exception("Reconnect failed — stopping thread.")
                        self._failed_files.append(file.full_path)
                        self.kill()
                    else:
                        if not self.dead():
                            logger.info("Reconnected. Retrying %s...", file.full_path)
                            try:
                                self._download_one(file, filepath)
                            except _Aborted:
                                logger.info("Aborted retry of %s", file.full_path)
                                return
                            except Exception:
                                logger.exception(
                                    "Retry after reconnect failed for %s —"
                                    " recording as failed.",
                                    file.full_path,
                                )
                                self._failed_files.append(file.full_path)
                except Exception:
                    logger.exception(
                        "Unexpected error for %s — skipping.", file.full_path
                    )
                    self._failed_files.append(file.full_path)
                finally:
                    self.q.task_done()
        finally:
            if self.ftp is not None:
                with contextlib.suppress(Exception):
                    self.ftp.close()

    def _download_one(self, file: RemoteFile, filepath: Path) -> None:
        logger.debug("%s -> %s", file.full_path, filepath)
        t0 = time.time()
        fetch_file(
            self.ftp,
            file.full_path,
            filepath,
            retries=5,
            abort_check=self.dead,
        )
        tt = time.time() - t0
        log_download(tt, file.size, filepath.name)

        url = f"ftp://{FTP_HOST}/{file.full_path}"
        manifest = _write_manifest(
            filepath,
            url,
            file.dataset,
            metadata={
                "partition": str(file.partition),
                "preliminary": file.preliminary,
                "remote_datetime": file.datetime.isoformat(),
            },
        )

        self.callback(
            {
                "url": url,
                "size": file.size,
                "filepath": filepath,
                "suffix": file.extension,
                "dataset": file.dataset,
                "created_at": file.datetime,
                "manifest": manifest,
            }
        )

    def kill(self) -> None:
        self._kill_event.set()

    def dead(self) -> bool:
        return self._kill_event.is_set()


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


def connect(timeout: float = FTP_TIMEOUT, attempts: int = 3) -> ftplib.FTP:
    return ftp_connect(
        FTP_HOST,
        encoding="latin-1",
        timeout=timeout,
        attempts=attempts,
        base_delay=2.0,
        max_delay=30.0,
        jitter=1.0,
    )


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


def fetch_file(
    ftp: ftplib.FTP,
    path: str,
    dest_filepath: Path | str,
    retries: int = 3,
    *,
    abort_check: Callable[[], bool] | None = None,
):
    """Fetch a file from a remote FTP server.

    :param path: The path to the file.
    :param dest_filepath: The destination file path.
    :param ftp: The FTP connection.
    :param abort_check: Optional callable polled per data chunk; if it
        returns truthy, the download is aborted, the partial file is
        removed, and :class:`_Aborted` is raised (no retries).
    """

    if isinstance(dest_filepath, str):
        dest_filepath = Path(dest_filepath.lower())
    dest_filepath.parent.mkdir(parents=True, exist_ok=True)

    max_retries = retries
    attempt = 0
    while retries > 0:
        attempt += 1
        try:
            with open(dest_filepath, "wb") as f:

                def _write(chunk: bytes, _f=f) -> None:
                    if abort_check is not None and abort_check():
                        raise _Aborted
                    _f.write(chunk)

                ftp.retrbinary("RETR " + path, _write)
            return
        except _Aborted:
            dest_filepath.unlink(missing_ok=True)
            raise
        except ftplib.error_perm:
            logger.exception("File %s not found.", path)
            dest_filepath.unlink(missing_ok=True)
            return
        except FTP_TRANSIENT_ERRORS:
            logger.exception(
                "Transient error for %s (attempt %d/%d).",
                path,
                attempt,
                max_retries,
            )
            dest_filepath.unlink(missing_ok=True)
            retries -= 1
            if retries > 0:
                if abort_check is not None and abort_check():
                    raise _Aborted from None
                time.sleep(
                    exponential_delay(
                        attempt, base_delay=2.0, max_delay=60.0, jitter=1.0
                    )
                )

    raise FetchError(f"Download of {path} failed after {max_retries} attempts")


def _write_manifest(
    filepath: Path,
    url: str,
    dataset_id: str,
    metadata: dict,
) -> DownloadManifest:
    manifest = DownloadManifest.from_file(
        source_id="datasus",
        dataset_id=dataset_id,
        url=url,
        file_path=filepath,
        producer="datasus-fetcher",
        metadata=metadata,
    )
    manifest.write_json(filepath.with_suffix(filepath.suffix + ".manifest.json"))
    return manifest


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
    q: queue.Queue = queue.Queue()
    failed_files: list[str] = []

    # Mutable callback reference — swapped per dataset after each q.join()
    _cb_ref: list[Callable | None] = [callback]

    def _shared_cb(file_metadata: dict) -> None:
        if _cb_ref[0]:
            _cb_ref[0](file_metadata)

    workers: list[Fetcher] = []
    for _ in range(threads):
        w = Fetcher(q, destdir, callback=_shared_cb, failed_files=failed_files)
        w.start()
        workers.append(w)

    current_pbar: list[_tqdm | None] = [None]

    try:
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

            if show_progress:
                pbar = _tqdm(
                    total=len(dataset_files),
                    desc=dataset,
                    unit=" arquivo",
                    leave=True,
                )
                current_pbar[0] = pbar

                def _dataset_cb(fm: dict, _pbar: _tqdm = pbar) -> None:
                    _pbar.update(1)
                    if callback:
                        callback(fm)

                _cb_ref[0] = _dataset_cb
            else:
                _cb_ref[0] = callback

            for f in dataset_files:
                q.put(f)
            while q.unfinished_tasks:
                time.sleep(0.05)

            if show_progress:
                pbar.close()
                current_pbar[0] = None

    except KeyboardInterrupt:
        for w in workers:
            w.kill()
        # Drain queued-but-not-started items so q.unfinished_tasks unblocks
        # and surviving workers don't keep pulling from a stale backlog.
        while True:
            try:
                q.get_nowait()
            except queue.Empty:
                break
            q.task_done()
        _tqdm.write("\nDownload interrompido pelo usuário.")
    finally:
        if current_pbar[0] is not None:
            with contextlib.suppress(Exception):
                current_pbar[0].close()
            current_pbar[0] = None
        # Send shutdown sentinels — wakes workers blocked on get(timeout).
        for _ in workers:
            q.put(None)
        for w in workers:
            w.join(timeout=5)
            if w.is_alive():
                logger.warning("Worker %s did not exit within timeout.", w.name)
        with contextlib.suppress(Exception):
            ftp0.close()
        if failed_files:
            logger.warning(
                "%d arquivo(s) falharam permanentemente após todas as tentativas:\n%s",
                len(failed_files),
                "\n".join(f"  {p}" for p in sorted(failed_files)),
            )
    # Fetcher threads close their own FTP connections in run()'s finally block


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
    owns_ftp = False  # o caller é dono do ftp inicial; reconnects são nossos
    try:
        for i, file in enumerate(files):
            filename, extension = file["filename"].rsplit(".", 1)
            filename = f"{filename}@{file['datetime']:%Y%m%d}.{extension}"
            filepath = destdir / filename

            if is_complete_file(filepath, file["size"]):
                continue

            logger.debug(f"{i: >5} {file['full_path']} -> {filepath}")
            t0 = time.time()

            for attempt in range(1, 3):  # até 2 tentativas
                try:
                    fetch_file(ftp, file["full_path"], filepath, retries=5)
                    break
                except FetchError as exc:
                    if attempt >= 2:
                        logger.error(
                            "Support file failed after reconnect: %s",
                            file["full_path"],
                        )
                        raise
                    logger.warning(
                        "Transient error for support file %s: %s. Reconnecting...",
                        file["full_path"],
                        exc,
                    )
                    if owns_ftp:
                        with contextlib.suppress(Exception):
                            ftp.close()
                    ftp = connect_fn()
                    owns_ftp = True

            tt = time.time() - t0
            filesize_kb = f"{file['size'] / 1024:.2f} kB"
            download_speed_kbps = f"{file['size'] / tt / 1024:.2f} kB/s"
            logger.debug(
                f"      {filename} {tt:.2f} s {filesize_kb} {download_speed_kbps}",
            )

            url = f"ftp://{FTP_HOST}/{file['full_path']}"
            manifest = _write_manifest(
                filepath,
                url,
                destdir.name,
                metadata={"remote_datetime": file["datetime"].isoformat()},
            )

            yield {
                "url": url,
                "size": file["size"],
                "filepath": filepath,
                "created_at": file["datetime"],
                "suffix": extension,
                "manifest": manifest,
            }
    finally:
        if owns_ftp:
            with contextlib.suppress(Exception):
                ftp.close()


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


def generate_catalog(
    downloaded_files: list[dict],
) -> core_meta.MetadataCatalog:
    """Generate a validated MetadataCatalog from a list of downloaded files."""
    source_id = "datasus"
    source = core_meta.Source(
        id=source_id,
        name="DATASUS - Departamento de Informática do SUS",
        homepage_url="https://datasus.saude.gov.br",
    )

    datasets_map = {}
    resources = []

    for file in downloaded_files:
        dataset_id = file.get("dataset", "unknown")
        if dataset_id not in datasets_map:
            datasets_map[dataset_id] = core_meta.Dataset(
                id=dataset_id,
                source_id=source_id,
                name=meta.datasets.get(dataset_id, {}).get("nome", dataset_id),
            )

        # Extract filename as resource id/name
        filename = file["filepath"].name
        resource_id = filename.replace(".", "_")

        resources.append(
            core_meta.Resource(
                id=resource_id,
                dataset_id=dataset_id,
                name=filename,
                url=file["url"],
                format=file["suffix"],
                path=str(file["filepath"].absolute()),
                metadata={
                    "created_at": file["created_at"].isoformat()
                    if isinstance(file["created_at"], dt.datetime)
                    else str(file["created_at"]),
                },
            )
        )

    catalog = core_meta.MetadataCatalog(
        sources=[source],
        datasets=list(datasets_map.values()),
        resources=resources,
    )
    catalog.validate_references()
    return catalog
