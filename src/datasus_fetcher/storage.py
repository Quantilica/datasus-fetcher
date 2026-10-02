import datetime as dt
import json
from collections.abc import Generator
from dataclasses import dataclass, field
from pathlib import Path

from quantilica.core.dates import year_month_partition
from quantilica.core.exceptions import ParseError
from quantilica.core.files import is_complete_file
from quantilica.core.storage import LocalStorage, build_stamped_filename

from . import logger


@dataclass
class File:
    """Data class representing a local file with its metadata."""

    filepath: Path
    dataset: str
    partition: str
    date: dt.date
    extension: str
    size: int
    is_most_recent: bool = False


@dataclass
class DataPartition:
    """Data class representing a partition in DATASUS datasets."""

    uf: str | None = None
    year: int | None = None
    month: int | None = None
    version: str | None = None

    def __str__(self) -> str:
        uf, year, month = self.uf, self.year, self.month
        match (uf, year, month):
            case (None, int(), None):
                partition = f"{year}"
            case (str(), None, None):
                partition = f"{uf}"
            case (str(), int(), None):
                partition = f"{year}-{uf}"
            case (str(), int(), int()):
                partition = f"{year}{month:02}-{uf}"
            case _:
                partition = ""
        if version := self.version:
            partition = f"{partition}-{version}" if partition else version
        return partition.lower()


@dataclass
class RemoteFile:
    """Data class representing a remote file on DATASUS FTP."""

    filename: str
    full_path: str
    datetime: dt.datetime
    extension: str
    size: int
    dataset: str
    preliminary: bool = False
    partition: DataPartition = field(default_factory=DataPartition)


def get_partition_dir(remote_file: RemoteFile) -> str:
    """Returns the partition directory string (``YYYY`` or ``YYYYMM``).

    Args:
        remote_file (RemoteFile): The remote file to get the partition directory for.

    Returns:
        str: The partition directory string.
    """
    year = remote_file.partition.year
    if year is None:
        return ""
    return year_month_partition(year, remote_file.partition.month)


def get_filename(remote_file: RemoteFile) -> str:
    """Returns ``{dataset}[_{partition}]@{YYYYMMDD}.{ext}`` filename.

    Args:
        remote_file (RemoteFile): The remote file to generate the filename for.

    Returns:
        str: The generated filename.
    """
    dataset = remote_file.dataset
    if remote_file.preliminary:
        dataset += "-preliminar"
    partition = str(remote_file.partition)
    return build_stamped_filename(
        dataset,
        partition,
        ext=remote_file.extension,
        timestamp=remote_file.datetime.date(),
    )


def get_data_filepath(data_dir: Path | str, remote_file: RemoteFile) -> Path:
    """Returns the absolute path where ``remote_file`` should be stored.

    Args:
        data_dir (Path | str): The base directory for storing data.
        remote_file (RemoteFile): The remote file to get the storage path for.

    Returns:
        Path: The absolute path for the file.
    """
    dataset = remote_file.dataset
    partition_dir = get_partition_dir(remote_file)
    filename = get_filename(remote_file)
    base = Path(data_dir) / dataset
    if partition_dir:
        return base / partition_dir / filename
    return base / filename


def get_manifest_path(target_path: Path) -> Path:
    """Returns the sidecar manifest path for a downloaded file.

    Matches the convention used by ``DownloadManifest.write_json``: the
    manifest lives next to the file with a ``.manifest.json`` suffix.

    Args:
        target_path (Path): Path of the downloaded data file.

    Returns:
        Path: The corresponding manifest sidecar path.
    """
    return target_path.with_suffix(target_path.suffix + ".manifest.json")


def is_manifest_valid(manifest_path: Path) -> bool:
    """Checks whether a download manifest sidecar exists and is parseable.

    A valid manifest must be a JSON object carrying non-empty ``sha256`` and
    ``size_bytes`` fields, as written by ``DownloadManifest.write_json``.

    Args:
        manifest_path (Path): Path of the manifest sidecar file.

    Returns:
        bool: True if the manifest exists and parses with required fields.
    """
    try:
        if not manifest_path.is_file():
            return False
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    if not isinstance(data, dict):
        return False
    sha256 = data.get("sha256")
    size = data.get("size_bytes")
    if not isinstance(sha256, str) or len(sha256) != 64:
        return False
    return isinstance(size, int) and size >= 0


def is_cached_download(
    target_path: Path,
    expected_size: int,
    manifest_path: Path | None = None,
) -> bool:
    """Returns True if ``target_path`` is already downloaded and consistent.

    The incremental check requires all of:

    - the data file exists locally;
    - its byte size matches the remote ``expected_size``;
    - the sidecar manifest exists and is well-formed (SHA-256 integrity
      provenance is preserved from the original download).

    Downloads performed through ``FtpClient.download_with_manifest`` always
    produce the sidecar manifest, so files without one are freed downloads
    and will be re-fetched for provenance completeness.

    Args:
        target_path (Path): Local path where the file would be stored.
        expected_size (int): Size (bytes) reported by the remote listing.
        manifest_path (Path | None): Manifest sidecar path; defaults to
            ``target_path + '.manifest.json'``.

    Returns:
        bool: True when the download can be skipped (cached and valid).
    """
    if manifest_path is None:
        manifest_path = get_manifest_path(target_path)
    return is_complete_file(target_path, expected_size) and is_manifest_valid(
        manifest_path
    )


class DataRepository:
    """Manages local storage for DATASUS files using LocalStorage."""

    def __init__(self, root: Path | str):
        """Initializes the DataRepository.

        Args:
            root (Path | str): The root directory for local storage.
        """
        self.storage = LocalStorage(root)

    def get_partition_dir(self, remote_file: RemoteFile) -> str:
        """Returns the partition directory string for a remote file.

        Args:
            remote_file (RemoteFile): The remote file.

        Returns:
            str: The partition directory string.
        """
        return get_partition_dir(remote_file)

    def get_filename(self, remote_file: RemoteFile) -> str:
        """Returns the filename for a remote file.

        Args:
            remote_file (RemoteFile): The remote file.

        Returns:
            str: The generated filename.
        """
        return get_filename(remote_file)

    def get_data_filepath(self, file: RemoteFile) -> Path:
        """Returns the absolute path where the file should be stored.

        Args:
            file (RemoteFile): The remote file.

        Returns:
            Path: The absolute path for the file.
        """
        dataset = file.dataset
        partition_dir = get_partition_dir(file)
        filename = get_filename(file)
        key = (
            f"{dataset}/{partition_dir}/{filename}"
            if partition_dir
            else f"{dataset}/{filename}"
        )
        return self.storage.path_for(key)


def get_file_metadata(file: Path) -> File:
    """Parses a ``{dataset}[_{partition}]@{YYYYMMDD}.{ext}`` filename.

    Args:
        file (Path): The file path to parse.

    Returns:
        File: The file metadata.

    Raises:
        ValueError: If the filename is missing the '@' separator.
    """
    stem = file.stem
    base, sep, file_date_str = stem.rpartition("@")
    if not sep:
        raise ValueError(f"Filename missing '@' separator: {file.name}")
    if "_" in base:
        dataset, partition = base.split("_", 1)
    else:
        dataset, partition = base, ""
    extension = file.suffix
    file_date = dt.datetime.strptime(file_date_str, "%Y%m%d").date()
    size = file.stat().st_size
    return File(
        filepath=file,
        size=size,
        dataset=dataset,
        partition=partition,
        date=file_date,
        extension=extension,
    )


def get_files_metadata(dirpath: Path) -> Generator[File, None, None]:
    """Yields metadata for all files in a directory.

    Args:
        dirpath (Path): The directory path to scan.

    Yields:
        Generator[File, None, None]: A generator of File objects.
    """
    files = {}
    for f in dirpath.glob("*.*"):
        try:
            file = get_file_metadata(f)
        except (ValueError, ParseError):
            logger.warning("Skipping file %s", f.name)
            continue
        if file.partition not in files:
            files[file.partition] = []
        files[file.partition].append(file)
    for partition in files:
        partition_files_sorted = sorted(
            files[partition],
            key=lambda f: f.filepath.name,
        )
        n_files_partition_sorted = len(partition_files_sorted)
        for i, file in enumerate(partition_files_sorted, 1):
            file.is_most_recent = i == n_files_partition_sorted
            yield file
