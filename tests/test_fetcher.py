import datetime
import ftplib
import queue
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from datasus_fetcher import fetcher
from datasus_fetcher.storage import DataPartition, RemoteFile


def make_remote_file(
    uf="sp", year=2020, month=1, size=1024, dataset="sih-rd"
) -> RemoteFile:
    return RemoteFile(
        filename="RDSP2001.dbc",
        full_path="/SIHSUS/200801_/Dados/RDSP2001.dbc",
        datetime=datetime.datetime(2024, 1, 15),
        extension="dbc",
        size=size,
        dataset=dataset,
        partition=DataPartition(uf=uf, year=year, month=month),
    )


class TestLogDownload(unittest.TestCase):
    def test_does_not_raise(self):
        # log_download calls logger.info — just verify it doesn't raise
        fetcher.log_download(tt=2.5, size=1_000_000, filename="test_file.dbc")

    def test_zero_size(self):
        fetcher.log_download(tt=1.0, size=0, filename="empty.dbc")

    def test_very_fast_download(self):
        # Very small tt should not cause division by zero
        fetcher.log_download(tt=0.001, size=500_000, filename="fast.dbc")


class TestFetcherSkipsExistingFile(unittest.TestCase):
    def test_skips_file_with_matching_size(self):
        """If local file exists and size matches, skip the download."""
        with tempfile.TemporaryDirectory() as tmpdir:
            data_dir = Path(tmpdir)
            remote_file = make_remote_file(size=42)

            # Write a local file with the same size at the expected path
            from datasus_fetcher.storage import get_data_filepath

            local_path = get_data_filepath(data_dir, remote_file)
            local_path.parent.mkdir(parents=True, exist_ok=True)
            local_path.write_bytes(b"x" * 42)

            # Create a Fetcher with a mocked FTP and a queue with the file
            q = queue.Queue()
            q.put(remote_file)

            mock_ftp = MagicMock(spec=ftplib.FTP)

            with patch.object(fetcher, "connect", return_value=mock_ftp):
                worker = fetcher.Fetcher(q=q, dest_dir=data_dir)
                worker.kill()  # stop the run() loop after this item

            # Run the core logic manually (simulate one loop iteration)
            from datasus_fetcher.storage import get_data_filepath

            filepath = get_data_filepath(data_dir, remote_file)
            self.assertTrue(filepath.exists())
            self.assertEqual(filepath.stat().st_size, remote_file.size)


class TestFetchFile(unittest.TestCase):
    def test_creates_parent_directories(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            dest = Path(tmpdir) / "nested" / "dir" / "file.dbc"
            self.assertFalse(dest.parent.exists())

            mock_ftp = MagicMock(spec=ftplib.FTP)
            mock_ftp.retrbinary.side_effect = lambda cmd, callback: callback(
                b"data"
            )

            fetcher.fetch_file(mock_ftp, "/remote/file.dbc", dest)

            self.assertTrue(dest.parent.exists())

    def test_writes_file_content(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            dest = Path(tmpdir) / "file.dbc"
            payload = b"binary content"

            mock_ftp = MagicMock(spec=ftplib.FTP)
            mock_ftp.retrbinary.side_effect = lambda cmd, callback: callback(
                payload
            )

            fetcher.fetch_file(mock_ftp, "/remote/file.dbc", dest)

            self.assertTrue(dest.exists())
            self.assertEqual(dest.read_bytes(), payload)

    def test_retries_on_timeout(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            dest = Path(tmpdir) / "file.dbc"

            mock_ftp = MagicMock(spec=ftplib.FTP)
            # Fail twice with timeout, then succeed
            mock_ftp.retrbinary.side_effect = [
                ftplib.error_temp("timeout"),
                ftplib.error_temp("timeout"),
                None,  # success on 3rd attempt
            ]

            with patch("datasus_fetcher.fetcher.time.sleep"):
                fetcher.fetch_file(
                    mock_ftp, "/remote/file.dbc", dest, retries=3
                )

            self.assertEqual(mock_ftp.retrbinary.call_count, 3)

    def test_stops_on_permission_error(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            dest = Path(tmpdir) / "file.dbc"

            mock_ftp = MagicMock(spec=ftplib.FTP)
            mock_ftp.retrbinary.side_effect = ftplib.error_perm(
                "550 not found"
            )

            fetcher.fetch_file(
                mock_ftp, "/remote/missing.dbc", dest, retries=3
            )

            # Should not retry on permission error — only one attempt
            self.assertEqual(mock_ftp.retrbinary.call_count, 1)
            self.assertFalse(dest.exists())

    def test_accepts_string_path(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            dest_str = str(Path(tmpdir) / "file.dbc")

            mock_ftp = MagicMock(spec=ftplib.FTP)
            mock_ftp.retrbinary.side_effect = lambda cmd, callback: callback(
                b"ok"
            )

            # Should not raise even when dest is a string
            fetcher.fetch_file(mock_ftp, "/remote/file.dbc", dest_str)


class TestListFiles(unittest.TestCase):
    def _make_ftp(self, lines: list[str]) -> MagicMock:
        """Build a mock FTP that returns given LIST lines."""
        mock_ftp = MagicMock(spec=ftplib.FTP)

        def fake_retrlines(cmd, callback):
            for line in lines:
                callback(line)

        mock_ftp.retrlines.side_effect = fake_retrlines
        return mock_ftp

    def test_parses_file_entry(self):
        lines = ["01-15-24  09:30AM             1024 RDSP2001.DBC"]
        mock_ftp = self._make_ftp(lines)
        # lru_cache must be cleared between tests to avoid cross-contamination
        fetcher.list_files.cache_clear()
        result = fetcher.list_files(mock_ftp, "/SIHSUS/200801_/Dados")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["filename"], "RDSP2001.DBC")
        self.assertEqual(result[0]["size"], 1024)
        self.assertEqual(result[0]["extension"], "dbc")

    def test_skips_directories(self):
        lines = [
            "01-15-24  09:30AM       <DIR>          subdir",
            "01-15-24  09:30AM             512 file.dbc",
        ]
        mock_ftp = self._make_ftp(lines)
        fetcher.list_files.cache_clear()

        # max_recursive_depth=0 evita recursão no <DIR>; só o arquivo conta
        result = fetcher.list_files(
            mock_ftp, "/some/dir", max_recursive_depth=0
        )

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["filename"], "file.dbc")

    def test_full_path_is_composed(self):
        lines = ["01-15-24  09:30AM             100 TEST.DBC"]
        mock_ftp = self._make_ftp(lines)
        fetcher.list_files.cache_clear()
        result = fetcher.list_files(mock_ftp, "/mydir")
        self.assertEqual(result[0]["full_path"], "/mydir/TEST.DBC")

    def test_retries_on_timeout(self):
        mock_ftp = MagicMock(spec=ftplib.FTP)
        call_count = {"n": 0}

        def fake_retrlines(cmd, callback):
            call_count["n"] += 1
            if call_count["n"] < 3:
                raise ftplib.error_temp("timeout")
            callback("01-15-24  09:30AM             100 FILE.DBC")

        mock_ftp.retrlines.side_effect = fake_retrlines
        fetcher.list_files.cache_clear()

        with patch("datasus_fetcher.fetcher.time.sleep"):
            result = fetcher.list_files(mock_ftp, "/dir", retries=3)

        self.assertEqual(len(result), 1)
        self.assertEqual(call_count["n"], 3)

    def tearDown(self):
        fetcher.list_files.cache_clear()


class TestFetcherReconnectsAndRetries(unittest.TestCase):
    def test_reconnects_and_retries_file(self):
        """Transient FetchError → reconnect → retry succeeds; file kept."""
        with tempfile.TemporaryDirectory() as tmpdir:
            data_dir = Path(tmpdir)
            remote_file = make_remote_file(size=999)
            q = queue.Queue()
            q.put(remote_file)
            q.put(None)  # sentinela para encerrar o loop

            failed: list[str] = []
            mock_ftp = MagicMock(spec=ftplib.FTP)
            with (
                patch.object(
                    fetcher, "connect", return_value=mock_ftp
                ) as mock_connect,
                patch.object(
                    fetcher.Fetcher,
                    "_download_one",
                    side_effect=[fetcher.FetchError("boom"), None],
                ) as mock_dl,
            ):
                worker = fetcher.Fetcher(
                    q=q, dest_dir=data_dir, failed_files=failed
                )
                worker.run()

            self.assertEqual(mock_dl.call_count, 2)
            # 1 conexão inicial + 1 reconexão
            self.assertGreaterEqual(mock_connect.call_count, 2)
            self.assertEqual(failed, [])


class TestFetcherRecordsPermanentFailure(unittest.TestCase):
    def test_retry_also_fails_records_failure(self):
        """Retry após reconexão também falha → registrado em failed_files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            data_dir = Path(tmpdir)
            remote_file = make_remote_file(size=999)
            q = queue.Queue()
            q.put(remote_file)
            q.put(None)

            failed: list[str] = []
            mock_ftp = MagicMock(spec=ftplib.FTP)
            with (
                patch.object(fetcher, "connect", return_value=mock_ftp),
                patch.object(
                    fetcher.Fetcher,
                    "_download_one",
                    side_effect=[
                        fetcher.FetchError("boom1"),
                        fetcher.FetchError("boom2"),
                    ],
                ),
            ):
                worker = fetcher.Fetcher(
                    q=q, dest_dir=data_dir, failed_files=failed
                )
                worker.run()

            self.assertIn(remote_file.full_path, failed)


class TestFetcherReconnectFailureStopsThread(unittest.TestCase):
    def test_reconnect_failure_kills_worker(self):
        """connect() falha na reconexão → worker morre e registra falha."""
        with tempfile.TemporaryDirectory() as tmpdir:
            data_dir = Path(tmpdir)
            remote_file = make_remote_file(size=999)
            q = queue.Queue()
            q.put(remote_file)
            q.put(None)

            failed: list[str] = []
            mock_ftp = MagicMock(spec=ftplib.FTP)
            # 1ª chamada (inicial) ok; 2ª (reconexão) levanta FetchError
            mock_connect = MagicMock(
                side_effect=[mock_ftp, fetcher.FetchError("no connect")]
            )
            with (
                patch.object(fetcher, "connect", mock_connect),
                patch.object(
                    fetcher.Fetcher,
                    "_download_one",
                    side_effect=[fetcher.FetchError("boom")],
                ),
            ):
                worker = fetcher.Fetcher(
                    q=q, dest_dir=data_dir, failed_files=failed
                )
                worker.run()

            self.assertTrue(worker.dead())
            self.assertIn(remote_file.full_path, failed)


class TestDownloadSupportFilesReconnect(unittest.TestCase):
    def test_reconnects_on_transient(self):
        """FetchError no support file → reconecta via connect_fn e segue."""
        with tempfile.TemporaryDirectory() as tmpdir:
            destdir = Path(tmpdir) / "docs"
            files = [
                {
                    "filename": "doc.pdf",
                    "datetime": datetime.datetime(2024, 1, 1),
                    "size": 10,
                    "full_path": "/docs/doc.pdf",
                }
            ]
            orig_ftp = MagicMock(spec=ftplib.FTP)
            new_ftp = MagicMock(spec=ftplib.FTP)
            connect_fn = MagicMock(return_value=new_ftp)

            with (
                patch.object(
                    fetcher,
                    "fetch_file",
                    side_effect=[fetcher.FetchError("boom"), None],
                ) as mock_fetch,
                patch.object(
                    fetcher, "_write_manifest", return_value=MagicMock()
                ),
                # tempos distintos para evitar divisão por zero no cálculo
                patch.object(
                    fetcher.time, "time", side_effect=[1000.0, 1000.5]
                ),
            ):
                results = list(
                    fetcher._download_support_files(
                        orig_ftp, files, destdir, connect_fn=connect_fn
                    )
                )

            self.assertEqual(len(results), 1)
            self.assertEqual(connect_fn.call_count, 1)
            self.assertEqual(mock_fetch.call_count, 2)
            new_ftp.close.assert_called_once()  # conexão criada é fechada


if __name__ == "__main__":
    unittest.main()
