"""Regressão (0.14.0): datas tipo ``D`` do SINAN rejeitadas pela conversão estrita.

Os campos de data do SINAN (``DT_SIN_PRI``, ``DT_OBITO``...) são do tipo ``D`` no
.dbf, e o leitor já os entrega como ``pl.Date``. ``wrangle_datasus`` convertia a
coluna para texto (``"2024-03-02"``) e tentava ler ``AAAAMMDD``: tudo virava nulo e a
conversão estrita levantava "Valores fora do formato esperado".

Fixtures reais: ``dbf/DENGBR24_head.dbf`` (recorte de ``DENGBR24`` com o cabeçalho
original) e ``BOTUBR22.dbc`` (arquivo completo do FTP, 38 registros).
"""

import datetime as dt
from pathlib import Path

import pytest

pl = pytest.importorskip("polars")
pytest.importorskip("fastdbf")
pytest.importorskip("dbfread")

from datasus_fetcher import reader  # noqa: E402
from datasus_fetcher.wrangling import convert_file  # noqa: E402

FIXTURES = Path(__file__).parent / "fixtures"
DENG_DBF = FIXTURES / "dbf" / "DENGBR24_head.dbf"
BOTU_DBC = FIXTURES / "BOTUBR22.dbc"


def _date_fields(raw: pl.DataFrame) -> list[str]:
    return [c for c, t in raw.schema.items() if t == pl.Date]


def test_read_dbf_then_wrangle_sinan_dengue():
    raw = reader.read_dbf(DENG_DBF)
    df = reader.wrangle_datasus(raw, dataset="sinan-deng")

    assert df.height == raw.height == 25
    for col in _date_fields(raw):
        assert df.schema[col.lower()] == pl.Date
        assert df[col.lower()].to_list() == raw[col].to_list()
    assert df["dt_sin_pri"].null_count() == 0
    assert df["dt_obito"].drop_nulls().to_list() == [
        dt.date(2024, 1, 20),
        dt.date(2024, 1, 21),
        dt.date(2024, 1, 19),
        dt.date(2024, 1, 29),
        dt.date(2024, 1, 30),
    ]


@pytest.mark.parametrize("chunk_bytes", [None, 2048])
def test_read_dbf_with_wrangle_transform(chunk_bytes):
    """Caminho do ``convert_file``: o wrangling aplicado a cada pedaço."""
    df = reader.read_dbf(
        DENG_DBF,
        chunk_bytes=chunk_bytes,
        transform=lambda f: reader.wrangle_datasus(f, dataset="sinan-deng"),
    )
    assert df.height == 25
    assert df.schema["dt_sin_pri"] == pl.Date
    assert df.schema["dt_obito"] == pl.Date


def test_read_dbc_wrangles_sinan_dates(tmp_path):
    raw = reader.read_dbc(BOTU_DBC, clean=False)
    df = reader.read_dbc(BOTU_DBC, dataset="sinan-botu")

    assert df.height == raw.height == 38
    for col in _date_fields(raw):
        assert df.schema[col.lower()] == pl.Date
        assert df[col.lower()].to_list() == raw[col].to_list()
    assert df["dt_obito"].drop_nulls().to_list() == [
        dt.date(2022, 2, 23),
        dt.date(2022, 6, 1),
        dt.date(2022, 12, 30),
    ]

    out = convert_file(BOTU_DBC, tmp_path / "botu.parquet")
    assert pl.read_parquet(out).schema["dt_sin_pri"] == pl.Date


def test_wrangle_accepts_date_datetime_and_null_columns():
    raw = pl.DataFrame(
        {
            "DT_SIN_PRI": [dt.date(2024, 3, 2), None],
            "DT_OBITO": pl.Series([None, None], dtype=pl.Null),
            "DT_NOTIF": [dt.datetime(2024, 3, 4, 13, 5), None],
            "DT_INTER": ["20240304", ""],
        }
    )
    df = reader.wrangle_datasus(raw)
    assert df.schema == {
        "dt_sin_pri": pl.Date,
        "dt_obito": pl.Date,
        "dt_notif": pl.Date,
        "dt_inter": pl.Date,
    }
    assert df["dt_sin_pri"].to_list() == [dt.date(2024, 3, 2), None]
    assert df["dt_notif"].to_list() == [dt.date(2024, 3, 4), None]
    assert df["dt_inter"].to_list() == [dt.date(2024, 3, 4), None]


@pytest.mark.parametrize("invalid", ["2024-03-02", "02032024", "20240231", "2024"])
def test_wrangle_still_rejects_invalid_date_text(invalid):
    raw = pl.DataFrame({"DT_SIN_PRI": ["20240302", invalid]})
    with pytest.raises(ValueError, match="DT_SIN_PRI: 1 valor"):
        reader.wrangle_datasus(raw, dataset="sinan-deng")
