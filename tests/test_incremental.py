"""Tests for incremental download behavior (manifest-aware cached skip)."""

import datetime
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from datasus_fetcher.fetcher import download_data
from datasus_fetcher.storage import (
    DataPartition,
    RemoteFile,
    get_data_filepath,
    get_manifest_path,
    is_cached_download,
    is_manifest_valid,
)


def _write_download_artifacts(target: Path, content: bytes) -> Path:
    """Simulates artifacts produced by FtpClient.download_with_manifest."""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)
    manifest = {
        "source_id": "datasus",
        "dataset_id": "sinasc-dn",
        "url": "ftp://ftp.datasus.gov.br/test.dbc",
        "fetched_at": "2026-01-01T00:00:00+00:00",
        "sha256": hashlib.sha256(content).hexdigest(),
        "size_bytes": len(content),
        "manifest_version": 1,
    }
    manifest_path = get_manifest_path(target)
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    return manifest_path


def make_remote_file(size: int = 4, dataset: str = "sinasc-dn") -> RemoteFile:
    return RemoteFile(
        filename="DNSP2015.dbc",
        full_path="/SINASC/1996_/Dados/DNRES/DNSP2015.dbc",
        datetime=datetime.datetime(2026, 1, 1),
        extension="dbc",
        size=size,
        dataset=dataset,
        partition=DataPartition(uf="sp", year=2015),
    )


class TestIsManifestValid(unittest.TestCase):
    def test_valid_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sinasc-dn" / "2021" / "fake.dbc"
            manifest_path = _write_download_artifacts(target, b"data")
            self.assertTrue(is_manifest_valid(manifest_path))
            self.assertEqual(is_manifest_valid(get_manifest_path(target)), True)

    def test_missing_manifest(self):
        self.assertFalse(is_manifest_valid(Path("/nonexistent/manifest.json")))

    def test_invalid_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            mp = Path(tmp) / "m.manifest.json"
            mp.write_text("not json{", encoding="utf-8")
            self.assertFalse(is_manifest_valid(mp))

    def test_manifest_missing_required_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            mp = Path(tmp) / "m.manifest.json"
            mp.write_text(json.dumps({"sha256": "ab"}), encoding="utf-8")
            self.assertFalse(is_manifest_valid(mp))

    def test_manifest_with_bad_sha256(self):
        with tempfile.TemporaryDirectory() as tmp:
            mp = Path(tmp) / "m.manifest.json"
            mp.write_text(
                json.dumps({"sha256": "zz", "size_bytes": 1}), encoding="utf-8"
            )
            self.assertFalse(is_manifest_valid(mp))

    def test_manifest_json_array_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            mp = Path(tmp) / "m.manifest.json"
            mp.write_text("[]", encoding="utf-8")
            self.assertFalse(is_manifest_valid(mp))


class TestGetManifestPath(unittest.TestCase):
    def test_matches_download_with_manifest_convention(self):
        p = Path("/data/sim/2020/sim-do-cid10_2020-sp@20240101.dbc")
        self.assertEqual(
            get_manifest_path(p),
            Path("/data/sim/2020/sim-do-cid10_2020-sp@20240101.dbc.manifest.json"),
        )


class TestIsCachedDownload(unittest.TestCase):
    def test_cached_skips_when_file_and_manifest_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            rf = make_remote_file()
            target = get_data_filepath(Path(tmp), rf)
            _write_download_artifacts(target, b"data")
            self.assertTrue(is_cached_download(target, rf.size))

    def test_size_mismatch_triggers_redownload(self):
        with tempfile.TemporaryDirectory() as tmp:
            rf = make_remote_file()
            target = get_data_filepath(Path(tmp), rf)
            _write_download_artifacts(target, b"data")
            self.assertFalse(is_cached_download(target, rf.size + 1))

    def test_missing_manifest_triggers_redownload(self):
        with tempfile.TemporaryDirectory() as tmp:
            rf = make_remote_file()
            target = get_data_filepath(Path(tmp), rf)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b"data")
            self.assertFalse(is_cached_download(target, rf.size))

    def test_corrupt_manifest_triggers_redownload(self):
        with tempfile.TemporaryDirectory() as tmp:
            rf = make_remote_file()
            target = get_data_filepath(Path(tmp), rf)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b"data")
            get_manifest_path(target).write_text("{broken", encoding="utf-8")
            self.assertFalse(is_cached_download(target, rf.size))

    def test_missing_file_is_not_cached(self):
        with tempfile.TemporaryDirectory() as tmp:
            rf = make_remote_file()
            target = get_data_filepath(Path(tmp), rf)
            self.assertFalse(is_cached_download(target, rf.size))


class TestDownloadDataIncremental(unittest.TestCase):
    def test_cached_file_is_skipped_without_download(self):
        with tempfile.TemporaryDirectory() as tmp:
            destdir = Path(tmp)
            listed = [make_remote_file()]
            target = get_data_filepath(destdir, listed[0])
            _write_download_artifacts(target, b"data")

            with (
                patch("datasus_fetcher.fetcher.connect") as connect_mock,
                patch("datasus_fetcher.fetcher.FtpClient") as client_cls,
                patch(
                    "datasus_fetcher.fetcher.list_dataset_files",
                    return_value=listed,
                ),
            ):
                connect_mock.return_value = MagicMock()
                download_data(["sinasc-dn"], destdir, threads=1)

            client_cls.assert_not_called()

    def test_new_file_is_downloaded(self):
        with tempfile.TemporaryDirectory() as tmp:
            destdir = Path(tmp)
            listed = [make_remote_file()]

            client = MagicMock()
            with (
                patch("datasus_fetcher.fetcher.connect") as connect_mock,
                patch(
                    "datasus_fetcher.fetcher.FtpClient", return_value=client
                ) as client_cls,
                patch(
                    "datasus_fetcher.fetcher.list_dataset_files",
                    return_value=listed,
                ),
            ):
                connect_mock.return_value = MagicMock()
                download_data(["sinasc-dn"], destdir, threads=1)

            client_cls.assert_called_once()
            client.download_with_manifest.assert_called_once()
            kwargs = client.download_with_manifest.call_args.kwargs
            self.assertEqual(
                kwargs["target_path"], get_data_filepath(destdir, listed[0])
            )


if __name__ == "__main__":
    unittest.main()
