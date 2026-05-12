import datetime
import tempfile
import unittest
from pathlib import Path

from datasus_fetcher.storage import (
    DataPartition,
    RemoteFile,
    get_data_filepath,
    get_file_metadata,
    get_filename,
    get_files_metadata,
    get_partition_dir,
)


def make_remote_file(
    uf=None,
    year=None,
    month=None,
    version=None,
    preliminary=False,
    dataset="sih-rd",
) -> RemoteFile:
    return RemoteFile(
        filename="source.dbc",
        full_path=f"/SIHSUS/{dataset}/source.dbc",
        datetime=datetime.datetime(2024, 1, 15),
        extension="dbc",
        size=1024,
        dataset=dataset,
        preliminary=preliminary,
        partition=DataPartition(
            uf=uf, year=year, month=month, version=version
        ),
    )


class TestDataPartitionStr(unittest.TestCase):
    def test_year_only(self):
        self.assertEqual(str(DataPartition(year=2020)), "2020")

    def test_uf_only(self):
        self.assertEqual(str(DataPartition(uf="SP")), "sp")

    def test_uf_and_year(self):
        self.assertEqual(str(DataPartition(uf="RJ", year=2020)), "2020-rj")

    def test_uf_year_month(self):
        self.assertEqual(
            str(DataPartition(uf="MG", year=2020, month=6)), "202006-mg"
        )

    def test_uf_year_month_zero_padded(self):
        self.assertEqual(
            str(DataPartition(uf="SP", year=2020, month=1)), "202001-sp"
        )

    def test_with_version(self):
        self.assertEqual(
            str(DataPartition(uf="SP", year=2020, month=1, version="a")),
            "202001-sp-a",
        )

    def test_empty_partition(self):
        # Matches the _ (default) case in DataPartition.__str__
        self.assertEqual(str(DataPartition()), "")

    def test_none_year_none_month_none_uf(self):
        self.assertEqual(
            str(DataPartition(uf=None, year=None, month=None)), ""
        )

    def test_lowercase_conversion(self):
        # All output must be lowercase regardless of input
        self.assertEqual(str(DataPartition(uf="AC", year=2015)), "2015-ac")


class TestGetPartitionDir(unittest.TestCase):
    def test_year_and_month(self):
        f = make_remote_file(year=2020, month=1)
        self.assertEqual(get_partition_dir(f), "202001")

    def test_year_only(self):
        f = make_remote_file(year=2020)
        self.assertEqual(get_partition_dir(f), "2020")

    def test_month_zero_padding(self):
        f = make_remote_file(year=2020, month=3)
        self.assertEqual(get_partition_dir(f), "202003")

    def test_no_date(self):
        f = make_remote_file()
        self.assertEqual(get_partition_dir(f), "")


class TestGetFilename(unittest.TestCase):
    def test_uf_year_month_partition(self):
        f = make_remote_file(uf="sp", year=2020, month=1)
        self.assertEqual(get_filename(f), "sih-rd_202001-sp@20240115.dbc")

    def test_year_only_partition(self):
        f = make_remote_file(year=2023, dataset="sinasc-dn")
        self.assertEqual(get_filename(f), "sinasc-dn_2023@20240115.dbc")

    def test_preliminary_flag_adds_suffix(self):
        f = make_remote_file(uf="sp", year=2024, month=1, preliminary=True)
        self.assertIn("-preliminar", get_filename(f))
        self.assertTrue(get_filename(f).startswith("sih-rd-preliminar_"))

    def test_with_version(self):
        f = make_remote_file(uf="sp", year=2008, month=1, version="a")
        self.assertEqual(get_filename(f), "sih-rd_200801-sp-a@20240115.dbc")

    def test_extension_preserved(self):
        f = make_remote_file(year=2020)
        self.assertTrue(get_filename(f).endswith(".dbc"))

    def test_date_format_yyyymmdd(self):
        f = make_remote_file(year=2020)
        # download date portion must be YYYYMMDD after the '@' separator
        stem = get_filename(f).rsplit(".", 1)[0]
        _, _, date_part = stem.rpartition("@")
        self.assertEqual(date_part, "20240115")


class TestGetDataFilepath(unittest.TestCase):
    def test_yearmonth_partition(self):
        f = make_remote_file(uf="sp", year=2020, month=1)
        result = get_data_filepath(Path("/data"), f)
        self.assertEqual(
            result, Path("/data/sih-rd/202001/sih-rd_202001-sp@20240115.dbc")
        )

    def test_year_only_partition(self):
        f = make_remote_file(year=2023, dataset="sinasc-dn")
        result = get_data_filepath(Path("/data"), f)
        self.assertEqual(
            result, Path("/data/sinasc-dn/2023/sinasc-dn_2023@20240115.dbc")
        )

    def test_data_dir_is_prefix(self):
        base = Path("/custom/path")
        f = make_remote_file(uf="rj", year=2022, month=6)
        result = get_data_filepath(base, f)
        self.assertTrue(result.is_relative_to(base))

    def test_dataset_directory_matches_dataset_name(self):
        f = make_remote_file(uf="mg", year=2021, month=3, dataset="cnes-st")
        result = get_data_filepath(Path("/data"), f)
        self.assertEqual(result.parts[-3], "cnes-st")


class TestGetFileMetadata(unittest.TestCase):
    def _write_temp_file(
        self, tmpdir: str, name: str, content: bytes = b"x"
    ) -> Path:
        p = Path(tmpdir) / name
        p.write_bytes(content)
        return p

    def test_yearmonth_uf_partition(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            f = self._write_temp_file(
                tmpdir, "sih-rd_202001-sp@20240115.dbc", b"abc"
            )
            result = get_file_metadata(f)
            self.assertEqual(result.dataset, "sih-rd")
            self.assertEqual(result.partition, "202001-sp")
            self.assertEqual(result.date, datetime.date(2024, 1, 15))
            self.assertEqual(result.extension, ".dbc")
            self.assertEqual(result.size, 3)

    def test_year_only_partition(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            f = self._write_temp_file(tmpdir, "sinasc-dn_2023-sp@20240101.dbc")
            result = get_file_metadata(f)
            self.assertEqual(result.dataset, "sinasc-dn")
            self.assertEqual(result.partition, "2023-sp")
            self.assertEqual(result.date, datetime.date(2024, 1, 1))

    def test_invalid_filename_raises_value_error(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            f = self._write_temp_file(tmpdir, "invalid_filename.dbc")
            with self.assertRaises(ValueError):
                get_file_metadata(f)

    def test_filepath_preserved(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            f = self._write_temp_file(tmpdir, "sih-rd_202001-sp@20240115.dbc")
            result = get_file_metadata(f)
            self.assertEqual(result.filepath, f)


class TestGetFilesMetadata(unittest.TestCase):
    def _write(self, dirpath: Path, name: str, content: bytes = b"x") -> Path:
        p = dirpath / name
        p.write_bytes(content)
        return p

    def test_single_file_is_most_recent(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            self._write(d, "sih-rd_202001-sp@20240101.dbc")
            files = list(get_files_metadata(d))
            self.assertEqual(len(files), 1)
            self.assertTrue(files[0].is_most_recent)

    def test_two_versions_marks_latest_as_most_recent(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            self._write(d, "sih-rd_202001-sp@20230101.dbc")
            self._write(d, "sih-rd_202001-sp@20240115.dbc")
            files = list(get_files_metadata(d))
            self.assertEqual(len(files), 2)
            older = next(f for f in files if "20230101" in f.filepath.name)
            newer = next(f for f in files if "20240115" in f.filepath.name)
            self.assertFalse(older.is_most_recent)
            self.assertTrue(newer.is_most_recent)

    def test_different_partitions_are_independent(self):
        # sp and rj are separate partitions; each gets its own most_recent flag
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            self._write(d, "sih-rd_202001-sp@20240101.dbc")
            self._write(d, "sih-rd_202001-rj@20240101.dbc")
            files = list(get_files_metadata(d))
            self.assertEqual(len(files), 2)
            self.assertTrue(all(f.is_most_recent for f in files))

    def test_invalid_filename_is_skipped(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            self._write(d, "sih-rd_202001-sp@20240101.dbc")
            self._write(d, "garbage.dbc")
            files = list(get_files_metadata(d))
            self.assertEqual(len(files), 1)
            self.assertEqual(files[0].dataset, "sih-rd")

    def test_empty_directory_yields_nothing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            files = list(get_files_metadata(Path(tmpdir)))
            self.assertEqual(files, [])

    def test_three_versions_only_last_is_most_recent(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            d = Path(tmpdir)
            self._write(d, "sih-rd_202001-sp@20220101.dbc")
            self._write(d, "sih-rd_202001-sp@20230601.dbc")
            self._write(d, "sih-rd_202001-sp@20240115.dbc")
            files = list(get_files_metadata(d))
            self.assertEqual(len(files), 3)
            most_recent = [f for f in files if f.is_most_recent]
            self.assertEqual(len(most_recent), 1)
            self.assertIn("20240115", most_recent[0].filepath.name)


if __name__ == "__main__":
    unittest.main()
