"""Tests for CLI convert, decompress, and pipeline commands."""

from pathlib import Path
from unittest.mock import patch

import pytest

from datasus_fetcher.cli import main

FIXTURE_DBC = Path(__file__).parent / "fixtures" / "DOAC1996.dbc"


def test_cli_decompress(tmp_path: Path):
    """Test CLI 'decompress' command."""
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture não encontrada")

    out_dbf = tmp_path / "saida.dbf"
    main(["decompress", "-i", str(FIXTURE_DBC), "-o", str(out_dbf)])
    assert out_dbf.exists()


def test_cli_convert_parquet(tmp_path: Path):
    """Test CLI 'convert' command producing Parquet."""
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture não encontrada")

    out_parquet = tmp_path / "saida.parquet"
    main(["convert", "-i", str(FIXTURE_DBC), "-o", str(out_parquet)])
    assert out_parquet.exists()


def test_cli_missing_analytics_graceful_exit(tmp_path: Path):
    """Test that missing analytics extra exits gracefully without traceback."""
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture não encontrada")

    out_parquet = tmp_path / "saida.parquet"

    with patch("datasus_fetcher._HAS_ANALYTICS", False):
        with pytest.raises(SystemExit) as excinfo:
            main(["convert", "-i", str(FIXTURE_DBC), "-o", str(out_parquet)])
        assert excinfo.value.code == 1
