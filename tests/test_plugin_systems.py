"""Tests for --system/-s resolution in the Typer plugin CLI."""

import unittest

import typer
from typer.testing import CliRunner

from datasus_fetcher import meta
from datasus_fetcher.plugin import _systems_to_datasets, app, resolve_dataset_targets

runner = CliRunner()


class TestSystemsToDatasets(unittest.TestCase):
    def test_none_passthrough(self):
        self.assertIsNone(_systems_to_datasets(None))
        self.assertIsNone(_systems_to_datasets([]))

    def test_comma_separated(self):
        result = _systems_to_datasets(["sih,sinasc"])
        self.assertIn("sih-rd", result)
        self.assertIn("sinasc-dnex", result)
        self.assertEqual(len(result), 6)

    def test_case_insensitive(self):
        self.assertEqual(
            _systems_to_datasets(["SINASC"]),
            ["sinasc-dn", "sinasc-dnex"],
        )

    def test_unknown_raises_bad_parameter(self):
        with self.assertRaises(typer.BadParameter):
            _systems_to_datasets(["bogus"])


class TestResolveDatasetTargets(unittest.TestCase):
    def test_systems_only(self):
        self.assertEqual(
            resolve_dataset_targets(None, ["sih-rd", "sih-rj"]),
            ["sih-rd", "sih-rj"],
        )

    def test_datasets_only(self):
        self.assertEqual(
            resolve_dataset_targets(["cnes-dc"], None),
            ["cnes-dc"],
        )

    def test_both_none(self):
        self.assertIsNone(resolve_dataset_targets(None, None))

    def test_merge_dedup(self):
        result = resolve_dataset_targets(
            ["sih-rd"], ["sih-er", "sih-rd", "sih-rj", "sih-sp"]
        )
        self.assertEqual(result.count("sih-rd"), 1)


class TestPluginCliWiring(unittest.TestCase):
    def test_sync_rejects_unknown_system(self):
        result = runner.invoke(app, ["sync", "-s", "bogus"])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Unknown system or dataset", result.output)

    def test_mapping_consistency_with_meta(self):
        result = _systems_to_datasets(["sim"])
        self.assertEqual(result, sorted(meta.SYSTEM_DATASETS["sim"]))


if __name__ == "__main__":
    unittest.main()
