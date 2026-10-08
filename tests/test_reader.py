"""Tests for reader and wrangling logic in datasus_fetcher.reader."""

from pathlib import Path

import polars as pl
import pytest

from datasus_fetcher.reader import (
    decompress_dbc,
    read_dbc,
    read_dbf,
    wrangle_datasus,
    write_parquet,
)

FIXTURE_DBC = Path(__file__).parent / "fixtures" / "DOAC1996.dbc"


def test_decompress_dbc(tmp_path: Path):
    """Test decompress_dbc wrapper."""
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture não encontrada")

    out_dbf = decompress_dbc(FIXTURE_DBC, tmp_path / "custom.dbf")
    assert out_dbf.exists()
    assert out_dbf.name == "custom.dbf"


def test_read_dbf_and_dbc(tmp_path: Path):
    """Test reading DBF and reading DBC with automatic cleanup."""
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture não encontrada")
    from datasus_fetcher import _HAS_ANALYTICS

    if not _HAS_ANALYTICS:
        pytest.skip("Requer datasus-fetcher[analysis] (polars + dbfread/fastdbf)")

    # Ler DBF diretamente
    dbf_path = decompress_dbc(FIXTURE_DBC, tmp_path / "temp.dbf")
    df_dbf = read_dbf(dbf_path)
    assert isinstance(df_dbf, pl.DataFrame)
    assert len(df_dbf) > 0

    # Ler DBC direto (com cleanup de DBF)
    df_dbc = read_dbc(FIXTURE_DBC, keep_dbf=False, clean=True)
    assert isinstance(df_dbc, pl.DataFrame)
    assert len(df_dbc) == len(df_dbf)
    assert "_deleted" not in df_dbc.columns


def test_wrangle_datasus_rules():
    """Test detailed wrangling rules: null sentinels, codes, dates, numbers."""
    df_raw = pl.DataFrame(
        {
            "MUNIC_RES": ["355030 ", " 080001", "999999"],
            "CID10": [" A90 ", "J18.0", ""],
            "DT_INTER": ["20240115", "00000000", "20231231"],
            "VAL_TOT": ["1520,50", " 0.00 ", "NA"],
            "DIAS_PERM": ["5", " 10 ", "None"],
            "OUTRO_TEXTO": [" Exemplo ", "   ", "Valido"],
            "_DELETED": [False, False, True],
        }
    )

    df_clean = wrangle_datasus(df_raw, lowercase=True)

    # 1. Registro com _deleted=True deve ser filtrado e coluna descartada
    assert len(df_clean) == 2
    assert "_deleted" not in df_clean.columns

    # 2. Códigos preservados como strings limpas
    assert df_clean["munic_res"].to_list() == ["355030", "080001"]
    assert df_clean["cid10"].to_list() == ["A90", "J18.0"]

    # 3. Datas convertidas para pl.Date (sentinela 00000000 vira None)
    import datetime as dt

    dates = df_clean["dt_inter"].to_list()
    assert dates[0] == dt.date(2024, 1, 15)
    assert dates[1] is None

    # 4. Valores monetários convertidos para pl.Float64
    vals = df_clean["val_tot"].to_list()
    assert vals[0] == 1520.50
    assert vals[1] == 0.0

    # 5. Inteiros convertidos para pl.Int64
    dias = df_clean["dias_perm"].to_list()
    assert dias[0] == 5
    assert dias[1] == 10

    # 6. Strings limpas e espaços em branco virando None
    textos = df_clean["outro_texto"].to_list()
    assert textos[0] == "Exemplo"
    assert textos[1] is None


def test_write_parquet(tmp_path: Path):
    """Test saving DataFrame to Parquet and reading back."""
    df = pl.DataFrame({"ano": [2024], "uf": ["sp"], "total": [100.5]})
    dest = tmp_path / "subdir" / "data.parquet"

    saved_path = write_parquet(df, dest, compression="zstd")
    assert saved_path.exists()

    df_read = pl.read_parquet(saved_path)
    assert df_read.equals(df)


def test_normalize_frame_struct_series():
    """fastdbf novo devolve StructArray: Series de structs vira DataFrame."""
    from datasus_fetcher.reader import _normalize_frame

    # Reproduz o que pl.from_arrow retorna com fastdbf>=0.6 (ver run
    # 37609604005: Series sem nome, shape (2263,), dtype struct[41]).
    series = pl.Series("", [{"a": 1, "b": "x"}, {"a": 2, "b": "y"}])
    assert series.dtype == pl.Struct

    df = _normalize_frame(series)
    assert isinstance(df, pl.DataFrame)
    assert df.columns == ["a", "b"]
    assert df["a"].to_list() == [1, 2]

    # Passthrough: DataFrame entra, DataFrame sai (mesmo objeto).
    raw = pl.DataFrame({"a": [1]})
    assert _normalize_frame(raw) is raw

    # Series escalar (DBF de coluna única) vira frame de 1 coluna.
    single = pl.Series("col", [1, 2, 3])
    framed = _normalize_frame(single)
    assert isinstance(framed, pl.DataFrame)
    assert framed.columns == ["col"]
