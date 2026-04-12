import datetime
import unittest

from datasus_fetcher.slicer import Slicer
from datasus_fetcher.storage import DataPartition, RemoteFile


def make_file(uf=None, year=None, month=None) -> RemoteFile:
    return RemoteFile(
        filename="test.dbc",
        full_path="/test/test.dbc",
        datetime=datetime.datetime(2024, 1, 1),
        extension="dbc",
        size=1024,
        dataset="sih-rd",
        partition=DataPartition(uf=uf, year=year, month=month),
    )


class TestSlicerByTime(unittest.TestCase):
    def test_no_filter_passes_all(self):
        slicer = Slicer()
        self.assertTrue(slicer.by_time(make_file(year=2020, month=1)))
        self.assertTrue(slicer.by_time(make_file(year=1995)))

    def test_start_only(self):
        slicer = Slicer(start_time="202001")
        self.assertTrue(slicer.by_time(make_file(year=2020, month=1)))
        self.assertTrue(slicer.by_time(make_file(year=2023, month=6)))
        self.assertFalse(slicer.by_time(make_file(year=2019, month=12)))

    def test_end_only(self):
        slicer = Slicer(end_time="202012")
        self.assertTrue(slicer.by_time(make_file(year=2020, month=12)))
        self.assertTrue(slicer.by_time(make_file(year=2019, month=1)))
        self.assertFalse(slicer.by_time(make_file(year=2021, month=1)))

    def test_start_and_end(self):
        slicer = Slicer(start_time="202001", end_time="202012")
        self.assertTrue(slicer.by_time(make_file(year=2020, month=6)))
        self.assertTrue(slicer.by_time(make_file(year=2020, month=1)))
        self.assertTrue(slicer.by_time(make_file(year=2020, month=12)))
        self.assertFalse(slicer.by_time(make_file(year=2019, month=12)))
        self.assertFalse(slicer.by_time(make_file(year=2021, month=1)))

    def test_year_only_filter(self):
        slicer = Slicer(start_time="2015", end_time="2020")
        self.assertTrue(slicer.by_time(make_file(year=2018)))
        self.assertFalse(slicer.by_time(make_file(year=2014)))
        self.assertFalse(slicer.by_time(make_file(year=2021)))

    def test_boundary_inclusive(self):
        slicer = Slicer(start_time="202001", end_time="202001")
        self.assertTrue(slicer.by_time(make_file(year=2020, month=1)))

    def test_file_without_date_excluded_by_filter(self):
        slicer = Slicer(start_time="202001", end_time="202012")
        # File with no year/month produces empty string "".
        # Empty string is lexicographically less than any period string,
        # so it is excluded when a time filter is active.
        self.assertFalse(slicer.by_time(make_file()))


class TestSlicerByRegions(unittest.TestCase):
    def test_no_regions_passes_all(self):
        slicer = Slicer()
        self.assertTrue(slicer.by_regions(make_file(uf="sp")))
        self.assertTrue(slicer.by_regions(make_file(uf="rj")))
        self.assertTrue(slicer.by_regions(make_file(uf=None)))

    def test_matching_region(self):
        slicer = Slicer(regions=["sp", "rj"])
        self.assertTrue(slicer.by_regions(make_file(uf="sp")))
        self.assertTrue(slicer.by_regions(make_file(uf="rj")))

    def test_non_matching_region(self):
        slicer = Slicer(regions=["sp", "rj"])
        self.assertFalse(slicer.by_regions(make_file(uf="mg")))
        self.assertFalse(slicer.by_regions(make_file(uf="ba")))

    def test_single_region(self):
        slicer = Slicer(regions=["sp"])
        self.assertTrue(slicer.by_regions(make_file(uf="sp")))
        self.assertFalse(slicer.by_regions(make_file(uf="rj")))


class TestSlicerCall(unittest.TestCase):
    def test_both_conditions_must_pass(self):
        slicer = Slicer(start_time="202001", end_time="202012", regions=["sp"])
        # Correct time and region
        self.assertTrue(slicer(make_file(uf="sp", year=2020, month=6)))
        # Correct time, wrong region
        self.assertFalse(slicer(make_file(uf="rj", year=2020, month=6)))
        # Wrong time, correct region
        self.assertFalse(slicer(make_file(uf="sp", year=2021, month=1)))
        # Both wrong
        self.assertFalse(slicer(make_file(uf="rj", year=2021, month=1)))

    def test_empty_slicer_passes_everything(self):
        slicer = Slicer()
        self.assertTrue(slicer(make_file(uf="sp", year=2020, month=1)))
        self.assertTrue(slicer(make_file(uf="am", year=1998)))
        self.assertTrue(slicer(make_file()))


if __name__ == "__main__":
    unittest.main()
