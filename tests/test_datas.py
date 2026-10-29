"""Datas do DATASUS em formatos além de AAAAMMDD (todas viram ``pl.Date``).

Fixtures: arquivos reais do FTP do DATASUS — RESP (AM, 2015), SIA-PS (BA, 2012-12)
e SISPRENATAL (AL, 2012-01).
"""

import datetime as dt
from pathlib import Path

import pytest

pl = pytest.importorskip("polars")
dbfread = pytest.importorskip("dbfread")

from datasus_fetcher import reader  # noqa: E402

FIXTURES = Path(__file__).parent / "fixtures"


def _frame(**cols):
    return pl.DataFrame({k: pl.Series(v, dtype=pl.String) for k, v in cols.items()})


def test_competencia_aaaamm_vira_primeiro_dia_do_mes():
    df = reader.read_dbc(FIXTURES / "PSBA1212.dbc", dataset="sia-ps")
    assert df.schema["dt_process"] == pl.Date
    assert set(df["dt_atend"].to_list()) == {dt.date(2012, 11, 1), dt.date(2012, 12, 1)}


def test_sisprenatal_competencia():
    df = reader.read_dbc(FIXTURES / "PNAL1201.dbc", dataset="sisprenatal-pn")
    assert df["dt_atend"].to_list() == [dt.date(2012, 1, 1)] * df.height


def test_resp_ddmmaaaa():
    df = reader.read_dbc(FIXTURES / "RESPAM15.dbc", dataset="resp")
    assert df.schema["dt_nasc"] == pl.Date
    assert dt.date(2018, 5, 2) in df["dt_nasc"].to_list()  # "02052018"


def test_sih_antigo_aammdd():
    df = reader.wrangle_datasus(
        _frame(DT_INTER=["920826", "20120105"], DT_SAIDA=["920901", None]),
        dataset="sih-rd",
    )
    assert df["dt_inter"].to_list() == [dt.date(1992, 8, 26), dt.date(2012, 1, 5)]
    assert df["dt_saida"].to_list() == [dt.date(1992, 9, 1), None]


def test_data_invalida_continua_erro():
    with pytest.raises(ValueError, match="DT_INTER"):
        reader.wrangle_datasus(_frame(DT_INTER=["20121345"]), dataset="sih-rd")


def test_campo_d_so_com_asteriscos_vira_nulo(tmp_path: Path):
    """SINAN: ``********`` num campo D; o fastdbf e o dbfread recusavam o arquivo."""
    header_len = 32 + 2 * 32 + 1
    record_len = 1 + 4 + 8
    head = bytearray(32)
    head[0] = 3
    head[4:8] = (2).to_bytes(4, "little")
    head[8:10] = header_len.to_bytes(2, "little")
    head[10:12] = record_len.to_bytes(2, "little")

    def field(name: bytes, ftype: bytes, length: int) -> bytes:
        desc = bytearray(32)
        desc[: len(name)] = name
        desc[11] = ftype[0]
        desc[16] = length
        return bytes(desc)

    data = (
        bytes(head)
        + field(b"ID", b"C", 4)
        + field(b"DT_DIAG", b"D", 8)
        + b"\r"
        + b" 0001********"
        + b" 000220070115"
        + b"\x1a"
    )
    src = tmp_path / "sinan.dbf"
    src.write_bytes(data)

    df = reader.read_dbf(src)

    assert df["DT_DIAG"].to_list() == [None, dt.date(2007, 1, 15)]


def test_decimal_alem_da_precisao_declarada_alarga_a_precisao():
    """SINAN-SRC: "3415.0" num N(6,3) cabe no campo, mas não em decimal(6,3)."""
    campo = reader.DbfField("PESO", "N", 6, 3)
    df = reader._exact_decimals(  # noqa: SLF001
        pl.DataFrame({"PESO": [3415.0, 1.25]}), [campo]
    )
    assert df.schema["PESO"] == pl.Decimal(38, 3)
    assert [str(v) for v in df["PESO"].to_list()] == ["3415.000", "1.250"]


def test_dd_mm_aaaa_com_barras():
    # DT_NASC do SIA-PO
    out = reader.wrangle_datasus(_frame(DT_NASC=["29/05/1960", None]), dataset="po")
    assert out["dt_nasc"].to_list() == [dt.date(1960, 5, 29), None]


def test_inteiro_so_com_letras_vira_nulo():
    out = reader.wrangle_datasus(
        _frame(ANO=["2000", "EA", "..", "4."]), dataset="sinan-deng"
    )
    assert out["ano"].to_list() == [2000, None, None, 4]


def test_inteiro_em_outro_formato_segue_erro():
    with pytest.raises(ValueError, match="ANO"):
        reader.wrangle_datasus(_frame(ANO=["2000", "20o0"]), dataset="sinan-deng")


def test_campo_d_cortado_vira_nulo_e_numero_com_aspas_e_lido():
    cls = reader._datasus_field_parser(dbfread)
    parser = cls.__new__(cls)  # sem tabela: parseD/parseN não a usam
    assert parser.parseD(None, b"03/03/20") is None
    assert parser.parseD(None, b"12/1/200") is None
    assert parser.parseD(None, b"-0010101") is None
    assert parser.parseD(None, b"42664   ") == dt.date(2016, 10, 21)
    with pytest.raises(ValueError):
        parser.parseD(None, b"2008AB01")
    assert parser.parseN(None, b'"14.35') == 14.35
    assert parser.parseN(None, b"$   6.12") == 6.12
    assert parser.parseN(None, b"\xa0 6.50") == 6.5
    assert parser.parseN(None, b"E") is None
    with pytest.raises(ValueError):
        parser.parseN(None, b"14x35")


def test_zero_em_coluna_de_data_numerica_vira_nulo():
    df = pl.DataFrame({"DT_DIGITA": [0, 20240105]})
    out = reader.wrangle_datasus(df, dataset="sinan-sdta")
    assert out["dt_digita"].to_list() == [None, dt.date(2024, 1, 5)]
