"""Tests for --system/-s CLI resolution (thin CLI delegating to plugin)."""

import unittest

import pytest

from datasus_fetcher.cli import parse_systems, resolve_targets


class TestParseSystems(unittest.TestCase):
    def test_none_when_absent(self):
        self.assertIsNone(parse_systems(None))

    def test_single_system(self):
        result = parse_systems(["sim"])
        self.assertIn("sim-do-cid09", result)
        self.assertIn("sim-domat-cid10", result)
        self.assertEqual(len(result), 10)

    def test_case_insensitive(self):
        self.assertEqual(parse_systems(["SINASC"]), ["sinasc-dn", "sinasc-dnex"])

    def test_comma_separated(self):
        result = parse_systems(["sih,sinasc"])
        self.assertIn("sih-rd", result)
        self.assertIn("sinasc-dn", result)
        self.assertEqual(len(result), 4 + 2)

    def test_multiple_occurrences(self):
        result = parse_systems(["sim", "sih"])
        self.assertIn("sim-do-cid09", result)
        self.assertIn("sih-rd", result)
        self.assertEqual(len(result), 10 + 4)

    def test_mixed_with_dataset_id(self):
        result = resolve_targets(["sia-pa"], parse_systems(["sim"]))
        self.assertIn("sia-pa", result)
        self.assertIn("sim-do-cid10", result)

    def test_unknown_system_exits(self):
        with pytest.raises(SystemExit, match="bogus"):
            parse_systems(["bogus"])

    def test_whitespace_and_empty_fragments(self):
        self.assertIsNone(parse_systems(["", "  "]))
        self.assertIsNone(parse_systems(None))


class TestResolveTargets(unittest.TestCase):
    def test_systems_wins_when_datasets_absent(self):
        self.assertEqual(
            resolve_targets(None, ["sih-rd"]),
            ["sih-rd"],
        )

    def test_datasets_only_passthrough(self):
        self.assertEqual(resolve_targets(["cnes-dc"], None), ["cnes-dc"])

    def test_both_none_return_none(self):
        self.assertIsNone(resolve_targets(None, None))

    def test_datasets_merge_without_duplicates(self):
        result = resolve_targets(["sih-rd"], ["sih-er", "sih-rd", "sih-rj", "sih-sp"])
        self.assertEqual(result.count("sih-rd"), 1)
        self.assertEqual(result, ["sih-er", "sih-rd", "sih-rj", "sih-sp"])

    def test_unknown_positional_dataset_appended(self):
        result = resolve_targets(["sih-rd"], ["sinasc-dn", "sinasc-dnex"])
        self.assertEqual(result, ["sinasc-dn", "sinasc-dnex", "sih-rd"])


class TestMainWiring(unittest.TestCase):
    def test_list_has_system_flag(self):
        result = parse_systems(["cnes"])
        self.assertEqual(result[:1], ["cnes-dc"])

    def test_pipeline_has_system_flag(self):
        self.assertEqual(
            parse_systems(["SIH"]), ["sih-er", "sih-rd", "sih-rj", "sih-sp"]
        )

    def test_positional_datasets_still_supported(self):
        self.assertIsNone(parse_systems(None))
        self.assertEqual(
            resolve_targets(["sih-rd", "cnes-dc"], None), ["sih-rd", "cnes-dc"]
        )


if __name__ == "__main__":
    unittest.main()
