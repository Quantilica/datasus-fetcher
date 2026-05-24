import datetime as dt
from collections.abc import Generator
from dataclasses import dataclass, field
from pathlib import Path

from quantilica_core.dates import year_month_partition
from quantilica_core.exceptions import ParseError
from quantilica_core.storage import LocalStorage, build_stamped_filename

from . import logger


@dataclass
class File:
    filepath: Path
    dataset: str
    partition: str
    date: dt.date
    extension: str
    size: int
    is_most_recent: bool = False


@dataclass
class DataPartition:
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
            partition += f"-{version}"
        return partition.lower()


@dataclass
class RemoteFile:
    filename: str
    full_path: str
    datetime: dt.datetime
    extension: str
    size: int
    dataset: str
    preliminary: bool = False
    partition: DataPartition = field(default_factory=DataPartition)


def get_partition_dir(remote_file: RemoteFile) -> str:
    """Return the partition directory string (``YYYY`` or ``YYYYMM``)."""
    year = remote_file.partition.year
    if year is None:
        return ""
    return year_month_partition(year, remote_file.partition.month)


def get_filename(remote_file: RemoteFile) -> str:
    """Return ``{dataset}[_{partition}]@{YYYYMMDD}.{ext}`` filename."""
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
    """Return the absolute path where ``remote_file`` should be stored."""
    dataset = remote_file.dataset
    partition_dir = get_partition_dir(remote_file)
    filename = get_filename(remote_file)
    base = Path(data_dir) / dataset
    if partition_dir:
        return base / partition_dir / filename
    return base / filename


class DataRepository:
    """Manages local storage for DATASUS files using LocalStorage."""

    def __init__(self, root: Path | str):
        self.storage = LocalStorage(root)

    def get_partition_dir(self, remote_file: RemoteFile) -> str:
        return get_partition_dir(remote_file)

    def get_filename(self, remote_file: RemoteFile) -> str:
        return get_filename(remote_file)

    def get_data_filepath(self, file: RemoteFile) -> Path:
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
    """Parse a ``{dataset}[_{partition}]@{YYYYMMDD}.{ext}`` filename."""
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
