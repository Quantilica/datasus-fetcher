"""Tests for --system/-s CLI resolution (standalone argparse CLI)."""

import unittest

import pytest

from datasus_fetcher.cli import get_parser, parse_systems, resolve_targets


class TestParseSystems(unittest.TestCase):
    def test_none_when_absent(self):
        parser = get_parser()
        args = parser.parse_args(["sync"])
        self.assertIsNone(parse_systems(args.system))

    def test_single_system(self):
        parser = get_parser()
        args = parser.parse_args(["sync", "-s", "sim"])
        self.assertIn("sim-do-cid09", parse_systems(args.system))
        self.assertIn("sim-domat-cid10", parse_systems(args.system))
        self.assertEqual(len(parse_systems(args.system)), 10)

    def test_case_insensitive(self):
        parser = get_parser()
        args = parser.parse_args(["sync", "--system", "SINASC"])
        self.assertEqual(parse_systems(args.system), ["sinasc-dn", "sinasc-dnex"])

    def test_comma_separated(self):
        parser = get_parser()
        args = parser.parse_args(["sync", "-s", "sih,sinasc"])
        result = parse_systems(args.system)
        self.assertIn("sih-rd", result)
        self.assertIn("sinasc-dn", result)
        self.assertEqual(len(result), 4 + 2)

    def test_multiple_occurrences(self):
        parser = get_parser()
        args = parser.parse_args(["sync", "-s", "sim", "-s", "sih"])
        result = parse_systems(args.system)
        self.assertIn("sim-do-cid09", result)
        self.assertIn("sih-rd", result)
        self.assertEqual(len(result), 10 + 4)

    def test_mixed_with_dataset_id(self):
        parser = get_parser()
        args = parser.parse_args(["sync", "-s", "sim", "sia-pa"])
        result = resolve_targets(args.datasets, parse_systems(args.system))
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


class TestParserWiring(unittest.TestCase):
    def test_list_has_system_flag(self):
        parser = get_parser()
        args = parser.parse_args(["list", "-s", "cnes"])
        self.assertEqual(parse_systems(args.system)[:1], ["cnes-dc"])

    def test_pipeline_has_system_flag(self):
        parser = get_parser()
        args = parser.parse_args(["pipeline", "--system", "SIH"])
        self.assertEqual(
            parse_systems(args.system), ["sih-er", "sih-rd", "sih-rj", "sih-sp"]
        )

    def test_positional_datasets_still_supported(self):
        parser = get_parser()
        args = parser.parse_args(["sync", "sih-rd", "cnes-dc"])
        self.assertEqual(args.datasets, ["sih-rd", "cnes-dc"])
        self.assertIsNone(parse_systems(args.system))


if __name__ == "__main__":
    unittest.main()
