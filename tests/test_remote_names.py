import re
import unittest

from quantilica_core.exceptions import ParseError

from datasus_fetcher import meta
from datasus_fetcher.remote_names import get_pattern, parse_filename


def _match(period: dict, filename: str) -> re.Match | None:
    return get_pattern(period=period).match(filename.lower())


class TestGetPattern(unittest.TestCase):
    def test_returns_compiled_regex(self):
        period = meta.datasets["sih-sp"]["periods"][1]
        self.assertIsInstance(get_pattern(period=period), re.Pattern)

    def test_pattern_matches_valid_filename(self):
        period = meta.datasets["sih-rd"]["periods"][0]
        pattern = get_pattern(period=period)
        self.assertIsNotNone(pattern.match("rdsp2001.dbc"))

    def test_pattern_rejects_invalid_filename(self):
        period = meta.datasets["sih-rd"]["periods"][0]
        pattern = get_pattern(period=period)
        self.assertIsNone(pattern.match("totally_wrong.dbc"))

    def test_pattern_is_case_insensitive_by_lowering(self):
        # get_pattern lowercases the compiled pattern;
        # filenames must also be lowercased before matching (as the code does)
        period = meta.datasets["sih-sp"]["periods"][1]
        pattern = get_pattern(period=period)
        self.assertIsNotNone(pattern.match("spgo1904.dbc"))


class TestParseFilenameUfYear2Month(unittest.TestCase):
    """uf_year2_month_pattern — 2-digit year, UF + year + month."""

    def _period(self):
        return meta.datasets["sih-sp"]["periods"][1]

    def test_basic(self):
        m = _match(self._period(), "SPGO1904.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["uf"], "go")
        self.assertEqual(result["year"], 2019)
        self.assertEqual(result["month"], 4)

    def test_century_inference_70s(self):
        # Year "79" → 1979 (starts with 7)
        m = _match(self._period(), "SPSP7901.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["year"], 1979)

    def test_century_inference_80s(self):
        m = _match(self._period(), "SPSP8512.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["year"], 1985)

    def test_century_inference_90s(self):
        m = _match(self._period(), "SPSP9706.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["year"], 1997)

    def test_century_inference_00s(self):
        # Year "00" → 2000 (starts with 0)
        m = _match(self._period(), "SPSP0001.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["year"], 2000)

    def test_century_inference_60s_maps_to_2060(self):
        # Year "60" → 2060 (starts with 6, not in "789")
        m = _match(self._period(), "SPSP6006.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["year"], 2060)

    def test_month_december(self):
        m = _match(self._period(), "SPSP2312.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["month"], 12)

    def test_month_january(self):
        m = _match(self._period(), "SPSP2301.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["month"], 1)


class TestParseFilenameUfYear(unittest.TestCase):
    """uf_year_pattern — 4-digit year + UF (SINASC-DN periods[1])."""

    def _period(self):
        return meta.datasets["sinasc-dn"]["periods"][1]

    def test_basic(self):
        m = _match(self._period(), "DNSP2015.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["uf"], "sp")
        self.assertEqual(result["year"], 2015)
        self.assertNotIn("month", result)

    def test_different_state(self):
        m = _match(self._period(), "DNBA2020.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["uf"], "ba")
        self.assertEqual(result["year"], 2020)

    def test_national_br_code(self):
        m = _match(self._period(), "DNBR2018.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["uf"], "br")


class TestParseFilenameUfYear2(unittest.TestCase):
    """uf_year2_pattern — 2-digit year + UF (SIM-DO-CID09)."""

    def _period(self):
        return meta.datasets["sim-do-cid09"]["periods"][0]

    def test_1990s(self):
        m = _match(self._period(), "DORSP96.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["uf"], "sp")
        self.assertEqual(result["year"], 1996)

    def test_1970s(self):
        m = _match(self._period(), "DORRJ79.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["uf"], "rj")
        self.assertEqual(result["year"], 1979)


class TestParseFilenameYearOnly(unittest.TestCase):
    """year_pattern — 4-digit year, no UF (SINASC-DNEX)."""

    def _period(self):
        return meta.datasets["sinasc-dnex"]["periods"][0]

    def test_basic(self):
        m = _match(self._period(), "DNEX2015.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["year"], 2015)
        self.assertNotIn("uf", result)
        self.assertNotIn("month", result)

    def test_recent_year(self):
        m = _match(self._period(), "DNEX2023.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["year"], 2023)


class TestParseFilenameUfYear2MonthSiaPa(unittest.TestCase):
    """uf_year2_month_pattern_sia_pa — adds optional version letter."""

    def _period(self):
        # SIA-PA periods[1] uses uf_year2_month_pattern_sia_pa
        return meta.datasets["sia-pa"]["periods"][1]

    def test_no_version(self):
        m = _match(self._period(), "PASP0801.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["uf"], "sp")
        self.assertEqual(result["year"], 2008)
        self.assertEqual(result["month"], 1)
        self.assertEqual(result["version"], "")

    def test_with_version_letter(self):
        m = _match(self._period(), "PASP0801a.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["uf"], "sp")
        self.assertEqual(result["year"], 2008)
        self.assertEqual(result["month"], 1)
        self.assertEqual(result["version"], "a")

    def test_version_b(self):
        m = _match(self._period(), "PARJ1506b.dbc")
        result = parse_filename(m, self._period()["filename_pattern"])
        self.assertEqual(result["version"], "b")


class TestParseFilenameUnknownPatternRaises(unittest.TestCase):
    def test_unknown_pattern_raises_parse_error(self):
        # Build a dummy match object using a simple regex
        m = re.match(r"(sp)(08)(01)", "sp0801")
        with self.assertRaises(ParseError):
            parse_filename(m, "nonexistent_pattern")


if __name__ == "__main__":
    unittest.main()
