import re
import unittest

from datasus_fetcher import meta
from datasus_fetcher.remote_names import get_pattern, parse_filename


class TestRemoteNames(unittest.TestCase):
    def test_get_pattern(self):
        period = meta.datasets["sih-sp"]["periods"][1]
        fn_prefix = period["filename_prefix"]
        fn_pattern = period["filename_pattern"]
        fn_ext = period["extension"]
        pattern = re.compile(f"^{fn_prefix}{fn_pattern}\\.{fn_ext}$".lower())
        self.assertEqual(
            get_pattern(period=period),
            pattern,
        )

    def test_parse_filename(self):
        filename = "SPGO1904.dbc"
        period = meta.datasets["sih-sp"]["periods"][1]
        fn_pattern = period["filename_pattern"]
        pattern = get_pattern(period=period)
        m = pattern.match(filename.lower())
        parse_filename(m, fn_pattern)


if __name__ == "__main__":
    unittest.main()
