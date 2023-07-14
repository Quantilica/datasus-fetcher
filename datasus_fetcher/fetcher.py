import datetime as dt
import ftplib
import logging
import queue
import threading
import time
from functools import lru_cache
from pathlib import Path
from typing import Callable, Iterable, Self

from datasus_fetcher.slicer import Slicer

from . import meta
from .remote_names import get_pattern, parse_filename
from .storage import (
    DataPartition,
    RemoteFile,
    calculate_sha256,
    get_filename,
    get_partition_dir,
)

FTP_HOST = "ftp.datasus.gov.br"
MEGA = 1_000_000
logger = logging.getLogger(__name__)


class Fetcher(threading.Thread):
    def __init__(
        self: Self,
        q: queue.Queue,
        dest_dir: Path,
        callback: Callable = None,
    ):
        super().__init__()
        self.daemon = True
        self.ftp = connect()
        self.q = q
        self.dest_dir = dest_dir
        if callable(callback):
            self.callback = callback
        else:
            self.callback = lambda _: None

    def run(self):
        while True:
            file: RemoteFile = self.q.get()
            dataset = file.dataset
            partition_dir = get_partition_dir(file)
            filename = get_filename(file)

            filepath: Path = self.dest_dir / dataset / partition_dir / filename
            if filepath.exists() and filepath.stat().st_size == file.size:
                self.q.task_done()
                continue
            filepath.parent.mkdir(parents=True, exist_ok=True)

            try:
                logger.debug(file.full_path, "->", filepath)
                t0 = time.time()
                fetch_file(self.ftp, file.full_path, filepath)
                tt = time.time() - t0
                sha256 = calculate_sha256(filepath)
                log_download(tt, file.size, filepath.name)

                file_metadata = {
                    "url": f"ftp://{FTP_HOST}/{file.full_path}",
                    "size": file.size,
                    "filepath": filepath,
                    "suffix": file.extension,
                    "sha256": sha256,
                    "dataset": dataset,
                    "created_at": file.datetime,
                }

                self.callback(file_metadata)

            except Exception as e:
                logger.debug(f"Exception {e}")
            finally:
                self.q.task_done()


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


def connect() -> ftplib.FTP:
    """Connects to the FTP server."""
    ftp = ftplib.FTP(FTP_HOST, encoding="latin-1")
    ftp.login()
    return ftp


@lru_cache
def list_files(ftp: ftplib.FTP, directory: str, retries: int = 3) -> list[dict]:
    try:
        ftp.cwd(directory)
    except ftplib.error_perm:
        logger.exception(f"Directory not found. {directory}")

    while retries > 0:
        files = []
        try:
            ftp.retrlines("LIST", files.append)
            break
        # Timeout exception
        except (ftplib.error_temp, TimeoutError):
            logger.exception(f"Timeout exception while listing files.")
            retries -= 1
            time.sleep(5)

    # parse files' date, size and name
    def parse_line(line):
        date, time, size, name = line.split()
        extension = name.rsplit(".", maxsplit=1)[1].lower()
        datetime = dt.datetime.strptime(date + " " + time, "%m-%d-%y %I:%M%p")
        try:
            size = int(size)
        except ValueError:
            size = None
        return {
            "datetime": datetime,
            "size": size,
            "filename": name,
            "extension": extension,
            "full_path": f"{directory}/{name}",
        }

    files = [parse_line(line) for line in files]

    return files


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
    if not dest_filepath.parent.exists():
        dest_filepath.parent.mkdir(parents=True)

    while retries > 0:
        try:
            with open(dest_filepath, "wb") as f:
                ftp.retrbinary("RETR " + path, f.write)
            break
        # File not found exception
        except ftplib.error_perm:
            logger.exception(f"File {path} not found.")
            dest_filepath.unlink(missing_ok=True)
            break
        # Timeout exception
        except (ftplib.error_temp, TimeoutError):
            logger.exception(f"Timeout exception for {path}.")
            dest_filepath.unlink(missing_ok=True)
            retries -= 1
            time.sleep(5)


def list_dataset_files(ftp: ftplib.FTP, dataset: str) -> list[RemoteFile]:
    dataset_files = []
    for period in meta.datasets[dataset]["periods"]:
        files = [
            RemoteFile(**f)
            for f in list_files(ftp, directory=period["dir"], retries=3)
        ]
        fn_pattern = period["filename_pattern"]
        pattern = get_pattern(period=period)
        for file in files:
            m = pattern.match(file.filename.lower())
            if m:
                file.dataset = dataset
                file.partition = DataPartition(**parse_filename(m, fn_pattern))
                dataset_files.append(file)
    return dataset_files


def download_data(
    datasets: Iterable[str],
    destdir: Path,
    threads: int = 2,
    callback: Callable = print,
    slicer: Slicer = None,
):
    """Multithreaded download data files"""
    logger.info(f"Starting download with {threads} threads")
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
        logger.info(f"Getting files of {dataset}")
        for remote_file in list_dataset_files(ftp0, dataset):
            if slicer is not None and not slicer(remote_file):
                continue
            q.put(remote_file)
    ftp0.close()
    logger.info("Joining queue")
    q.join()
    for th in threading.enumerate():
        if th.daemon:
            th.ftp.close()


def download_documentation(
    ftp: ftplib.FTP,
    dataset: str,
    destdir: Path,
):

    destdir = destdir / f"{dataset}[doc]"

    ftp_dir = meta.docs[dataset]["dir"]
    ftp.cwd(ftp_dir)

    files = list_files(ftp)

    for i, file in enumerate(files):
        filename, extension = file["filename"].rsplit(".", 1)
        filename = f"{filename}@{file['datetime']:%Y%m%d}.{extension}"
        filepath = destdir / filename
        logger.debug(f"{i: >5}", file["full_path"], "->", filepath)
        t0 = time.time()
        fetch_file(ftp, file["full_path"], filepath)
        tt = time.time() - t0
        sha256 = calculate_sha256(filepath)
        filesize_kb = f"{file['size'] / 1024:.2f} kB"
        download_speed_kbps = f"{file['size'] / tt / 1024:.2f} kB/s"
        logger.debug(f"      {sha256} {tt:.2f} s {filesize_kb} {download_speed_kbps}")

        file_metadata = {
            "url": f"ftp://{FTP_HOST}/{file['full_path']}",
            "size": file["size"],
            "filepath": filepath,
            "created_at": file["datetime"],
            "sha256": sha256,
            "suffix": extension,
        }

        yield file_metadata
