"""Tests for the metadata-first listing (datasus-metadata snapshot)."""

import datetime as dt
import json
import os
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

from datasus_fetcher import plugin, snapshot

RECORD = {
    "filename": "RDAC2401.dbc",
    "full_path": "/dissemin/publicos/SIHSUS/200801_/Dados/RDAC2401.dbc",
    "datetime": "2024-03-01T10:00:00",
    "extension": "dbc",
    "size": 123,
    "dataset": "sih-rd",
    "partition": {"uf": "ac", "year": 2024, "month": 1, "subpartition": None},
    "preliminary": False,
}
DOC = {
    "filename": "doc.pdf",
    "full_path": "/x/doc.pdf",
    "datetime": "2024-01-02T03:04:00",
    "extension": "pdf",
    "size": 9,
    "dataset": "sih-rd",
}


class SnapshotTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.base = Path(self._tmp.name)

    def write(self, kind: str, dataset: str, payload, age_h: float = 1.0) -> Path:
        path = self.base / kind / f"{dataset}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            payload if isinstance(payload, str) else json.dumps(payload),
            encoding="utf-8",
        )
        mtime = time.time() - age_h * 3600
        os.utime(path, (mtime, mtime))
        return path


class TestSnapshotLoading(SnapshotTestCase):
    def test_fresh_snapshot_returns_remote_files(self):
        self.write("data", "sih-rd", [RECORD])
        files = snapshot.snapshot_data_files("sih-rd", base_dir=self.base)
        self.assertEqual(len(files), 1)
        f = files[0]
        self.assertEqual(f.filename, "RDAC2401.dbc")
        self.assertEqual(f.datetime, dt.datetime(2024, 3, 1, 10, 0))
        self.assertEqual(f.dataset, "sih-rd")
        self.assertEqual(str(f.partition), "202401-ac")

    def test_stale_snapshot_returns_none(self):
        self.write("data", "sih-rd", [RECORD], age_h=40)
        self.assertIsNone(snapshot.snapshot_data_files("sih-rd", base_dir=self.base))

    def test_max_age_is_configurable(self):
        self.write("data", "sih-rd", [RECORD], age_h=40)
        files = snapshot.snapshot_data_files("sih-rd", base_dir=self.base, max_age=48)
        self.assertEqual(len(files), 1)

    def test_missing_file_returns_none(self):
        self.assertIsNone(snapshot.snapshot_data_files("sih-rd", base_dir=self.base))

    def test_invalid_json_returns_none(self):
        self.write("data", "sih-rd", "{not json")
        self.assertIsNone(snapshot.snapshot_data_files("sih-rd", base_dir=self.base))

    def test_malformed_records_return_none(self):
        self.write("data", "sih-rd", [{"filename": "x"}])
        self.assertIsNone(snapshot.snapshot_data_files("sih-rd", base_dir=self.base))

    def test_unconfigured_returns_none(self):
        with mock.patch.dict(os.environ, {}, clear=False):
            os.environ.pop(snapshot.ENV_DIR, None)
            self.assertIsNone(snapshot.snapshot_data_files("sih-rd"))

    def test_env_configuration(self):
        self.write("data", "sih-rd", [RECORD], age_h=40)
        env = {snapshot.ENV_DIR: str(self.base), snapshot.ENV_MAX_AGE: "48"}
        with mock.patch.dict(os.environ, env):
            self.assertEqual(len(snapshot.snapshot_data_files("sih-rd")), 1)

    def test_subpartition_maps_to_version(self):
        rec = {
            **RECORD,
            "partition": {"uf": "ac", "year": 2024, "month": 1, "subpartition": "a"},
        }
        self.write("data", "sih-rd", [rec])
        f = snapshot.snapshot_data_files("sih-rd", base_dir=self.base)[0]
        self.assertEqual(f.partition.version, "a")

    def test_support_files(self):
        self.write("documentation", "sih-rd", [DOC])
        out = snapshot.snapshot_support_files("doc", "sih-rd", base_dir=self.base)
        self.assertEqual(out[0]["datetime"], dt.datetime(2024, 1, 2, 3, 4))


class TestListDatasetsMetadataFirst(SnapshotTestCase):
    def _env(self):
        return mock.patch.dict(os.environ, {snapshot.ENV_DIR: str(self.base)})

    def test_fresh_snapshot_skips_ftp(self):
        self.write("data", "sih-rd", [RECORD])
        with (
            self._env(),
            mock.patch.object(plugin, "_get_ftp") as get_ftp,
            mock.patch.object(plugin.fetcher, "list_dataset_files") as ftp_list,
        ):
            entries = plugin.datasus_list_datasets("sih-rd")
        get_ftp.assert_not_called()
        ftp_list.assert_not_called()
        data = [e for e in entries if e["type"] == "data"]
        self.assertEqual([e["id"] for e in data], ["RDAC2401.dbc"])
        self.assertEqual(data[0]["size"], 123)

    def test_stale_snapshot_falls_back_to_ftp(self):
        self.write("data", "sih-rd", [RECORD], age_h=40)
        with (
            self._env(),
            mock.patch.object(plugin, "_get_ftp", return_value="ftp") as get_ftp,
            mock.patch.object(
                plugin.fetcher, "list_dataset_files", return_value=[]
            ) as ftp_list,
        ):
            plugin.datasus_list_datasets("sih-rd")
        get_ftp.assert_called()
        ftp_list.assert_called_once_with("ftp", "sih-rd")

    def test_unconfigured_uses_ftp(self):
        with (
            mock.patch.dict(os.environ, {}, clear=False),
            mock.patch.object(plugin, "_get_ftp", return_value="ftp"),
            mock.patch.object(
                plugin.fetcher, "list_dataset_files", return_value=[]
            ) as ftp_list,
        ):
            os.environ.pop(snapshot.ENV_DIR, None)
            plugin.datasus_list_datasets("sih-rd")
        ftp_list.assert_called_once()


if __name__ == "__main__":
    unittest.main()
