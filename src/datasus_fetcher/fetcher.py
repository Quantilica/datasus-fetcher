import datetime as dt
import ftplib
import time
from functools import lru_cache

from quantilica.core.exceptions import FetchError
from quantilica.core.ftp import FTP_TRANSIENT_ERRORS, MonitoredFTP
from quantilica.core.retry import exponential_delay

try:
    _RICH_AVAILABLE = True
except (ModuleNotFoundError, ImportError):  # pragma: no cover
    _RICH_AVAILABLE = False


from . import logger, meta
from .remote_names import get_pattern, parse_filename
from .storage import (
    DataPartition,
    RemoteFile,
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
    """Logs the download progress and speed.

    Args:
        tt (float): Time taken for the download in seconds.
        size (int): Size of the downloaded file in bytes.
        filename (str): Name of the downloaded file.
    """
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
    """Connects to the DATASUS FTP server.

    Args:
        timeout (float, optional): Connection timeout in seconds. Defaults to FTP_TIMEOUT.
        attempts (int, optional): Number of connection attempts. Defaults to 3.

    Returns:
        MonitoredFTP: An authenticated and monitored FTP connection object.

    Raises:
        FetchError: If the connection fails after the specified number of attempts.
    """
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
    """Lists files in a given FTP directory.

    Args:
        ftp (ftplib.FTP): The FTP connection object.
        directory (str): The remote directory path to list.
        retries (int, optional): Number of retries on transient errors. Defaults to 3.
        max_recursive_depth (int, optional): Maximum depth for recursive listing. Defaults to 3.

    Returns:
        list[dict]: A list of dictionaries containing file metadata.
    """
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
    """Lists all remote files associated with a specific dataset.

    Args:
        ftp (ftplib.FTP): The FTP connection object.
        dataset (str): The dataset identifier.

    Returns:
        list[RemoteFile]: A list of RemoteFile objects for the dataset.
    """
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


def _list_support_files(ftp: ftplib.FTP, ftp_dirs: list[str]) -> list[dict]:
    files = []
    for ftp_dir in ftp_dirs:
        files.extend(list_files(ftp, directory=ftp_dir))
    return files


def list_documentation_files(ftp: ftplib.FTP, dataset: str) -> list[dict]:
    """Lists documentation files for a specific dataset.

    Args:
        ftp (ftplib.FTP): The FTP connection object.
        dataset (str): The dataset identifier.

    Returns:
        list[dict]: A list of dictionaries containing file metadata.
    """
    return _list_support_files(ftp, meta.docs[dataset]["dir"])


def list_auxiliary_tables_files(ftp: ftplib.FTP, dataset: str) -> list[dict]:
    """Lists auxiliary table files for a specific dataset.

    Args:
        ftp (ftplib.FTP): The FTP connection object.
        dataset (str): The dataset identifier.

    Returns:
        list[dict]: A list of dictionaries containing file metadata.
    """
    return _list_support_files(ftp, meta.auxiliary_tables[dataset]["dir"])
