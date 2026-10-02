"""Tests for system resolution (SYSTEM_DATASETS, --system expansion)."""

import unittest

import pytest

from datasus_fetcher import meta


class TestSystemDatasetsMapping(unittest.TestCase):
    def test_mapping_is_derived_from_dataset_groups(self):
        from collections import defaultdict

        expected = defaultdict(set)
        for dataset, cfg in meta.datasets.items():
            expected[cfg["group"]].add(dataset)
        for system, dataset_ids in meta.SYSTEM_DATASETS.items():
            self.assertEqual(set(dataset_ids), expected[system])

    def test_known_systems_present(self):
        for system in ("sim", "sinasc", "sih", "cnes", "sia", "sinan"):
            self.assertIn(system, meta.SYSTEM_DATASETS)

    def test_sih_datasets(self):
        self.assertEqual(
            meta.SYSTEM_DATASETS["sih"],
            ("sih-er", "sih-rd", "sih-rj", "sih-sp"),
        )

    def test_sinasc_datasets(self):
        self.assertEqual(
            meta.SYSTEM_DATASETS["sinasc"],
            ("sinasc-dn", "sinasc-dnex"),
        )

    def test_sim_includes_all_doc_variants(self):
        sim = meta.SYSTEM_DATASETS["sim"]
        for dataset in ("sim-do-cid09", "sim-do-cid10", "sim-dofet-cid10"):
            self.assertIn(dataset, sim)
        self.assertTrue(all(d.startswith("sim-") for d in sim))

    def test_mapping_covers_every_dataset_exactly_once(self):
        covered = [
            dataset
            for dataset_ids in meta.SYSTEM_DATASETS.values()
            for dataset in dataset_ids
        ]
        self.assertEqual(sorted(covered), sorted(meta.datasets))


class TestGetSystemDatasets(unittest.TestCase):
    def test_case_insensitive(self):
        self.assertEqual(meta.get_system_datasets("SIM"), meta.SYSTEM_DATASETS["sim"])
        self.assertEqual(
            meta.get_system_datasets("SINASC"), meta.SYSTEM_DATASETS["sinasc"]
        )
        self.assertEqual(meta.get_system_datasets("Sih"), meta.SYSTEM_DATASETS["sih"])

    def test_whitespace_is_stripped(self):
        self.assertEqual(
            meta.get_system_datasets("  sim  "), meta.SYSTEM_DATASETS["sim"]
        )

    def test_unknown_system_raises_keyerror(self):
        with pytest.raises(KeyError):
            meta.get_system_datasets("bogus")


class TestExpandSystems(unittest.TestCase):
    def test_single_system(self):
        self.assertEqual(
            meta.expand_systems(["sih"]),
            ["sih-er", "sih-rd", "sih-rj", "sih-sp"],
        )

    def test_case_insensitive_mixed(self):
        self.assertEqual(
            meta.expand_systems(["SIM", "Sinasc"]),
            sorted((*meta.SYSTEM_DATASETS["sim"], *"sinasc-dn sinasc-dnex".split())),
        )

    def test_comma_separated_list(self):
        self.assertEqual(
            meta.expand_systems(["sih", "sia-pa"]),
            ["sia-pa", "sih-er", "sih-rd", "sih-rj", "sih-sp"],
        )

    def test_multiple_occurrences(self):
        result = meta.expand_systems(["sim", "sim"])
        self.assertEqual(result, sorted(meta.SYSTEM_DATASETS["sim"]))

    def test_deduplicates_datasets(self):
        result = meta.expand_systems(["sim", "sim-do-cid10"])
        self.assertEqual(result.count("sim-do-cid10"), 1)

    def test_dataset_id_passes_through(self):
        self.assertEqual(meta.expand_systems(["sih-rd"]), ["sih-rd"])

    def test_empty_and_none(self):
        self.assertEqual(meta.expand_systems(None), [])
        self.assertEqual(meta.expand_systems([]), [])
        self.assertEqual(meta.expand_systems(["", "  "]), [])

    def test_unknown_raises_keyerror(self):
        with pytest.raises(KeyError, match="bogus"):
            meta.expand_systems(["bogus"])

    def test_result_is_sorted(self):
        result = meta.expand_systems(["sia"])
        self.assertEqual(result, sorted(result))


if __name__ == "__main__":
    unittest.main()
