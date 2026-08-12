from .storage import RemoteFile


class Slicer:
    """Filters remote files based on time and regions."""

    def __init__(
        self,
        start_time: str = "",
        end_time: str = "",
        regions: list[str] | None = None,
    ) -> None:
        """Initializes the Slicer.

        Args:
            start_time (str, optional): The start time period. Defaults to "".
            end_time (str, optional): The end time period. Defaults to "".
            regions (list[str] | None, optional): A list of region codes. Defaults to None.
        """
        self.start_time = start_time
        self.end_time = end_time
        self.regions = regions or []

    def by_time(self, remote_file: RemoteFile) -> bool:
        """Filters a remote file by time.

        Args:
            remote_file (RemoteFile): The remote file to filter.

        Returns:
            bool: True if the file matches the time criteria, False otherwise.
        """
        # If no start or end time is provided, there is no need to
        # filter, return True
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
        """Filters a remote file by region.

        Args:
            remote_file (RemoteFile): The remote file to filter.

        Returns:
            bool: True if the file matches the region criteria, False otherwise.
        """
        if self.regions:
            return remote_file.partition.uf in self.regions
        return True

    def __call__(self, remote_file: RemoteFile) -> bool:
        """Filters a remote file by time and region.

        Args:
            remote_file (RemoteFile): The remote file to filter.

        Returns:
            bool: True if the file matches both time and region criteria, False otherwise.
        """
        return self.by_regions(remote_file) and self.by_time(remote_file)
