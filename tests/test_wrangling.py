"""Tests for batch conversion routines in datasus_fetcher.wrangling."""

import shutil
from pathlib import Path

import polars as pl
import pytest

from datasus_fetcher.wrangling import (
    convert_directory,
    convert_file,
    parse_filename_metadata,
)

FIXTURE_DBC = Path(__file__).parent / "fixtures" / "DOAC1996.dbc"


def test_parse_filename_metadata():
    """Test extracting dataset, UF, year, and month from various naming patterns."""
    # SIM-DO com ano de 4 dígitos
    m1 = parse_filename_metadata("DOAC1996.dbc")
    assert m1 == {"dataset": "sim-do", "uf": "ac", "ano": 1996}

    # SIH-RD com ano de 2 dígitos e mês
    m2 = parse_filename_metadata("RDSP2401.dbc")
    assert m2 == {"dataset": "sih-rd", "uf": "sp", "ano": 2024, "mes": 1}

    # Stamped filename (formato do quantilica-core)
    m3 = parse_filename_metadata("RDSP2401@20240215.dbc")
    assert m3 == {"dataset": "sih-rd", "uf": "sp", "ano": 2024, "mes": 1}

    # CNES com ano
    m4 = parse_filename_metadata("cnes2022.dbc")
    assert m4 == {"dataset": "cnes", "ano": 2022}

    # Ano de 4 dígitos sem dataset reconhecido
    m5 = parse_filename_metadata("dados2022.dbc")
    assert m5 == {"ano": 2022}


def test_convert_file(tmp_path: Path):
    """Test converting a single file to Parquet and DBF."""
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture não encontrada")

    # 1. Converter para Parquet
    out_parquet = tmp_path / "saida.parquet"
    res_parquet = convert_file(FIXTURE_DBC, out_parquet, target_format="parquet")
    assert res_parquet.exists()
    assert res_parquet == out_parquet

    df = pl.read_parquet(res_parquet)
    assert len(df) > 0
    # Metadados de partição devem ter sido injetados
    assert "uf" in df.columns
    assert "ano" in df.columns
    assert df["uf"][0] == "ac"
    assert df["ano"][0] == 1996

    # 2. Converter para DBF
    out_dbf = tmp_path / "saida.dbf"
    res_dbf = convert_file(FIXTURE_DBC, out_dbf, target_format="dbf")
    assert res_dbf.exists()
    assert res_dbf == out_dbf


def test_convert_directory(tmp_path: Path):
    """Test converting all files in a directory hierarchy in parallel."""
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture não encontrada")

    in_dir = tmp_path / "raw" / "sim-do"
    in_dir.mkdir(parents=True)
    shutil.copy(FIXTURE_DBC, in_dir / "DOAC1996.dbc")
    shutil.copy(FIXTURE_DBC, in_dir / "DOAC1997.dbc")

    out_dir = tmp_path / "parquet"

    converted = convert_directory(
        in_dir,
        out_dir,
        target_format="parquet",
        workers=2,
    )

    assert len(converted) == 2
    for p in converted:
        assert p.exists()
        assert p.suffix == ".parquet"
