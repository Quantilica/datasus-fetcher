import datetime as dt
import ftplib
import queue
import threading
import time
from functools import lru_cache
from pathlib import Path
from typing import Callable, Iterable

import quantilica_core.metadata as core_meta
from quantilica_core.exceptions import FetchError
from quantilica_core.ftp import FTP_TRANSIENT_ERRORS, ftp_connect
from quantilica_core.manifests import DownloadManifest
from quantilica_core.retry import exponential_delay

from datasus_fetcher.slicer import Slicer

from . import logger, meta
from .remote_names import get_pattern, parse_filename
from .storage import DataPartition, DataRepository, RemoteFile

FTP_HOST = "ftp.datasus.gov.br"
FTP_TIMEOUT = 30.0
MEGA = 1_000_000


class Fetcher(threading.Thread):
    def __init__(
        self,
        q: queue.Queue,
        dest_dir: Path,
        callback: Callable | None = None,
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

    def run(self):
        self.ftp = connect()
        try:
            while not self.dead():
                file: RemoteFile = self.q.get()

                filepath: Path = self.repo.get_data_filepath(file=file)
                if filepath.exists() and filepath.stat().st_size == file.size:
                    self.q.task_done()
                    continue

                try:
                    logger.debug("%s -> %s", file.full_path, filepath)
                    t0 = time.time()
                    fetch_file(self.ftp, file.full_path, filepath)
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

                    file_metadata = {
                        "url": url,
                        "size": file.size,
                        "filepath": filepath,
                        "suffix": file.extension,
                        "dataset": file.dataset,
                        "created_at": file.datetime,
                        "manifest": manifest,
                    }

                    self.callback(file_metadata)

                except ftplib.error_perm:
                    logger.exception(
                        "Permanent FTP error for %s — skipping.",
                        file.full_path,
                    )
                except FTP_TRANSIENT_ERRORS as exc:
                    logger.warning(
                        "Transient error for %s: %s. Reconnecting...",
                        file.full_path,
                        exc,
                    )
                    try:
                        self.ftp.close()
                    except Exception:
                        pass
                    try:
                        self.ftp = connect()
                    except FetchError:
                        logger.exception("Reconnect failed — stopping thread.")
                        self.kill()
                except Exception:
                    logger.exception(
                        "Unexpected error for %s — skipping.", file.full_path
                    )
                finally:
                    self.q.task_done()
        finally:
            self.ftp.close()

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
    try:
        ftp.cwd(directory)
    except ftplib.error_perm:
        logger.exception("Directory not found: %s", directory)
        return []

    files: list[str] = []
    max_retries = retries
    attempt = 0
    while retries > 0:
        attempt += 1
        files.clear()
        try:
            ftp.retrlines("LIST", files.append)
            break
        except FTP_TRANSIENT_ERRORS:
            logger.exception(
                "Transient error listing files (attempt %d/%d).",
                attempt,
                max_retries,
            )
            retries -= 1
            if retries > 0:
                time.sleep(
                    exponential_delay(
                        attempt, base_delay=2.0, max_delay=30.0, jitter=1.0
                    )
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
            logger.warning(
                "Could not parse size for file %s in %s", name, directory
            )
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
):
    """Fetch a file from a remote FTP server.

    :param path: The path to the file.
    :param dest_filepath: The destination file path.
    :param ftp: The FTP connection.
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
                ftp.retrbinary("RETR " + path, f.write)
            return
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
    manifest.write_json(
        filepath.with_suffix(filepath.suffix + ".manifest.json")
    )
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
):
    """Multithreaded download data files"""
    logger.info("Starting download with %s threads", threads)
    if datasets:
        datasets_ = set(datasets) & set(meta.datasets.keys())
    else:
        datasets_ = meta.datasets.keys()
    ftp0 = connect()
    q = queue.Queue()
    for _ in range(threads):
        _w = Fetcher(q, destdir, callback=callback)
        _w.start()
    for dataset in datasets_:
        logger.info("Listing files of %s", dataset)
        for remote_file in list_dataset_files(ftp0, dataset):
            if slicer is not None and not slicer(remote_file):
                continue
            q.put(remote_file)
    ftp0.close()
    logger.info("Joining queue")
    q.join()
    # Fetcher threads close their own FTP connections in run()'s finally block


def _list_support_files(ftp: ftplib.FTP, ftp_dirs: list[str]) -> list[dict]:
    files = []
    for ftp_dir in ftp_dirs:
        ftp.cwd(ftp_dir)
        files.extend(list_files(ftp, directory=ftp_dir))
    return files


def _download_support_files(
    ftp: ftplib.FTP,
    files: list[dict],
    destdir: Path,
):
    for i, file in enumerate(files):
        filename, extension = file["filename"].rsplit(".", 1)
        filename = f"{filename}@{file['datetime']:%Y%m%d}.{extension}"
        filepath = destdir / filename

        if filepath.exists() and filepath.stat().st_size == file["size"]:
            continue

        logger.debug(f"{i: >5} {file['full_path']} -> {filepath}")
        t0 = time.time()
        fetch_file(ftp, file["full_path"], filepath)
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


def list_documentation_files(ftp: ftplib.FTP, dataset: str) -> list[dict]:
    return _list_support_files(ftp, meta.docs[dataset]["dir"])


def download_documentation(
    ftp: ftplib.FTP,
    dataset: str,
    destdir: Path,
):
    files = list_documentation_files(ftp, dataset)
    yield from _download_support_files(ftp, files, destdir / f"{dataset}[doc]")


def list_auxiliary_tables_files(ftp: ftplib.FTP, dataset: str) -> list[dict]:
    return _list_support_files(ftp, meta.auxiliary_tables[dataset]["dir"])


def download_auxiliary_tables(
    ftp: ftplib.FTP,
    dataset: str,
    destdir: Path,
):
    files = list_auxiliary_tables_files(ftp, dataset)
    yield from _download_support_files(ftp, files, destdir / f"{dataset}[aux]")


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
