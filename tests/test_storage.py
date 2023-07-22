import unittest
from datetime import datetime

from datasus_fetcher.storage import (
    DataPartition,
    RemoteFile,
    get_filename,
    get_partition_dir,
)


class TestStorage(unittest.TestCase):
    def setUp(self) -> None:
        self.remote_file = RemoteFile(
            filename="filename",
            full_path="full-path/filename",
            datetime=datetime(2020, 1, 1),
            extension="extension",
            size=1,
            dataset="dataset",
            partition=DataPartition(uf="uf", year=2000, month=1, version="a")
        )

    def test_get_partition_dir(self):
        self.assertEqual(
            get_partition_dir(self.remote_file),
            "200001",
        )

    def test_get_filename(self):
        self.assertEqual(
            get_filename(self.remote_file),
            "dataset_200001-uf-a_20200101.extension",
        )


if __name__ == "__main__":
    unittest.main()
