"""Tests for CLI convert, decompress, and pipeline commands."""

from pathlib import Path
from unittest.mock import patch

import pytest

pytest.importorskip("typer")

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
    """Test CLI 'convert' command producing Hive Lake Parquet."""
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture não encontrada")
    from datasus_fetcher import _HAS_ANALYTICS

    if not _HAS_ANALYTICS:
        pytest.skip("Requer datasus-fetcher[analysis] (polars + dbfread/fastdbf)")

    lake_dir = tmp_path / "lake"
    main(["convert", "-i", str(FIXTURE_DBC), "-o", str(lake_dir)])
    assert (lake_dir / "datasus" / "sim-do-cid10").exists()


def test_cli_missing_analytics_graceful_exit(tmp_path: Path):
    """Test that missing analytics extra exits gracefully without traceback."""
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture não encontrada")

    lake_dir = tmp_path / "lake"

    err = ImportError("No module named 'quantilica.analytics'")
    with patch("datasus_fetcher.lake.converter.convert", side_effect=err):
        with pytest.raises(SystemExit) as excinfo:
            main(["convert", "-i", str(FIXTURE_DBC), "-o", str(lake_dir)])
        assert excinfo.value.code == 1
