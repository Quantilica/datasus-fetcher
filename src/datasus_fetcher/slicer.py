from .storage import RemoteFile


class Slicer:
    """
    Slicer is a class that filters remote files based on time and regions.
    """

    def __init__(
        self,
        start_time: str = "",
        end_time: str = "",
        regions: list[str] | None = None,
    ) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.regions = regions or []

    def by_time(self, remote_file: RemoteFile) -> bool:
        """
        Filter a remote file by time.
        """
        # If no start or end time is provided, there is no need to filter, return True
        if self.start_time == "" and self.end_time == "":
            return True

        t = ""
        if remote_file.partition.year is not None:
            t += f"{remote_file.partition.year}"
        if remote_file.partition.month is not None:
            t += f"{remote_file.partition.month:02d}"

        if self.start_time and not self.end_time:
            return t >= self.start_time
        elif not self.start_time and self.end_time:
            return t <= self.end_time

        return t >= self.start_time and t <= self.end_time

    def by_regions(self, remote_file: RemoteFile) -> bool:
        """
        Filter a remote file by region.
        """
        if self.regions:
            return remote_file.partition.uf in self.regions
        return True

    def __call__(self, remote_file: RemoteFile) -> bool:
        """
        Filter a remote file by time and region.
        """
        return self.by_regions(remote_file) and self.by_time(remote_file)
