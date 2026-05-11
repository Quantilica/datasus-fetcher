import datetime as dt
from dataclasses import dataclass, field
from pathlib import Path
from typing import Generator, Optional

from quantilica_core.exceptions import ParseError
from quantilica_core.storage import LocalStorage

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
    uf: Optional[str] = None
    year: Optional[int] = None
    month: Optional[int] = None
    version: Optional[str] = None

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


class DataRepository:
    """Manages local storage for DATASUS files using LocalStorage."""

    def __init__(self, root: Path | str):
        self.storage = LocalStorage(root)

    def get_partition_dir(self, remote_file: RemoteFile) -> str:
        partition_dir = ""
        if remote_file.partition.year is not None:
            partition_dir += f"{remote_file.partition.year}"
        if remote_file.partition.month is not None:
            partition_dir += f"{remote_file.partition.month:02d}"
        return partition_dir

    def get_filename(self, remote_file: RemoteFile) -> str:
        """Returns the filename for the given file info and partition."""
        dataset = remote_file.dataset
        if remote_file.preliminary:
            dataset += "-preliminar"
        extension = remote_file.extension
        file_datetime = remote_file.datetime.strftime("%Y%m%d")
        partition = str(remote_file.partition)
        filename = "_".join(
            [s for s in (dataset, partition, file_datetime) if s]
        )
        return f"{filename}.{extension}"

    def get_data_filepath(self, file: RemoteFile) -> Path:
        dataset: str = file.dataset
        partition_dir: str = self.get_partition_dir(file)
        filename: str = self.get_filename(file)
        key = (
            f"{dataset}/{partition_dir}/{filename}"
            if partition_dir
            else f"{dataset}/{filename}"
        )
        return self.storage.path_for(key)


def get_file_metadata(file: Path) -> File:
    """Returns a dict with the parsed filename."""
    dataset, partition, file_date = file.stem.split("_")
    extension = file.suffix
    file_date = dt.datetime.strptime(file_date, "%Y%m%d").date()
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
