import datetime as dt
import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


@dataclass
class File:
    filepath: Path
    dataset: str
    partition: str
    date: dt.date
    extension: str
    size: int
    # checksum: str = None
    is_most_recent: bool = False


@dataclass
class DataPartition:
    uf: str = None
    year: int = None
    month: int = None
    version: str = None

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
    dataset: str = None
    partition: DataPartition = field(default_factory=DataPartition)


def calculate_sha256(filepath: Path) -> str:
    """Returns the SHA256 hash of a file."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()


def get_partition_dir(remote_file: RemoteFile) -> str:
    partition_dir = ""
    if remote_file.partition.year is not None:
        partition_dir += f"{remote_file.partition.year}"
    if remote_file.partition.month is not None:
        partition_dir += f"{remote_file.partition.month:02d}"
    return partition_dir


def get_filename(remote_file: RemoteFile) -> str:
    """Returns the filename for the given file info and partition."""
    dataset = remote_file.dataset
    extension = remote_file.extension
    file_datetime = remote_file.datetime.strftime("%Y%m%d")
    partition = str(remote_file.partition)
    filename = "_".join([s for s in (dataset, partition, file_datetime) if s])
    return f"{filename}.{extension}"


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
        # checksum=get_sha1_hash(file),
        extension=extension,
    )


def get_files_metadata(dirpath: Path) -> File:
    files = {}
    for f in dirpath.glob("*.*"):
        file = get_file_metadata(f)
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


def get_most_recent(files: Iterable[File]) -> dict[str, File]:
    most_recent_files = [file for file in files if file.is_most_recent]
    return most_recent_files
