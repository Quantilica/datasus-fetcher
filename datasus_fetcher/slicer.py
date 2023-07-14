from typing import Self

from .storage import RemoteFile


class Slicer:
    def __init__(
        self: Self,
        start_time: str = None,
        end_time: str = None,
        regions: list[str] = None,
    ) -> None:
        if start_time:
            self.start_time = start_time
        else:
            self.start_time = None
        if end_time:
            self.end_time = end_time
        else:
            self.end_time = None
        if regions:
            self.regions = regions
        else:
            self.regions = []

    def by_time(self, remote_file: RemoteFile) -> bool:
        if not any((self.start_time, self.end_time)):
            return True

        t = ""
        if remote_file.partition.year is not None:
            t += f"{remote_file.partition.year}"
        if remote_file.partition.month is not None:
            t += f"{remote_file.partition.month:02d}"
        else:
            t += "00"

        if self.start_time and not self.end_time:
            return t >= self.start_time
        elif not self.start_time and self.end_time:
            return t <= self.end_time
        return t >= self.start_time and t <= self.end_time

    def by_regions(self, remote_file: RemoteFile) -> bool:
        if any(self.regions):
            return remote_file.partition.uf in self.regions
        return True

    def __call__(self, remote_file: RemoteFile) -> bool:
        return self.by_regions(remote_file) and self.by_time(remote_file)
