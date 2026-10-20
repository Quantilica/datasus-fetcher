"""Field offsets, exact decimals and strict conversions in the DBF reader."""

import datetime as dt
import struct
from decimal import Decimal
from pathlib import Path

import polars as pl
import pytest

from datasus_fetcher import _HAS_ANALYTICS
from datasus_fetcher.reader import (
    _dbf_fields,
    _read_dbf_dbfread,
    _with_field_offsets,
    decompress_dbc,
    read_dbf,
    wrangle_datasus,
)
from datasus_fetcher.wrangling import parse_filename_metadata

pytestmark = pytest.mark.skipif(
    not _HAS_ANALYTICS, reason="Requer datasus-fetcher[analysis]"
)

FIXTURE_DBC = Path(__file__).parent / "fixtures" / "DOAC1996.dbc"


def make_dbf(path: Path, fields: list[tuple[str, str, int, int]], rows: list[tuple]):
    """Write a dBASE III file the way DATASUS does: every field offset zeroed."""
    header_len = 32 + 32 * len(fields) + 1
    record_len = 1 + sum(length for _, _, length, _ in fields)
    out = bytearray()
    out += struct.pack("<BBBBIHH", 3, 126, 1, 1, len(rows), header_len, record_len)
    out += b"\0" * 20
    for name, ftype, length, decimals in fields:
        desc = bytearray(32)
        desc[: len(name)] = name.encode("ascii")
        desc[11] = ord(ftype)
        desc[16] = length
        desc[17] = decimals
        out += desc  # bytes 12-15 (deslocamento) ficam zerados
    out += b"\r"
    for row in rows:
        out += b" "
        for (_, ftype, length, _), value in zip(fields, row, strict=True):
            text = str(value)
            out += (text.rjust(length) if ftype == "N" else text.ljust(length)).encode(
                "latin-1"
            )
    out += b"\x1a"
    path.write_bytes(bytes(out))
    return path


FIELDS = [
    ("N_AIH", "C", 13, 0),
    ("SEXO", "C", 1, 0),
    ("DT_INTER", "C", 8, 0),
    ("DIAS_PERM", "N", 5, 0),
    ("VAL_TOT", "N", 14, 2),
]
ROWS = [
    ("1200002022010", "1", "20220103", 4, "1508094.36"),
    ("1200002022011", "3", "20220131", 0, "0.29"),
]


def test_header_offsets_are_filled_as_running_sum(tmp_path):
    path = make_dbf(tmp_path / "x.dbf", FIELDS, ROWS)
    raw = path.read_bytes()
    fixed = _with_field_offsets(raw[: 32 + 32 * len(FIELDS) + 1])
    offsets = [
        struct.unpack("<I", fixed[32 + 32 * i + 12 : 32 + 32 * i + 16])[0]
        for i in range(len(FIELDS))
    ]
    assert offsets == [1, 14, 15, 23, 28]
    assert [f.name for f in _dbf_fields(fixed)] == [f[0] for f in FIELDS]


def test_header_with_inconsistent_record_length_raises(tmp_path):
    path = make_dbf(tmp_path / "x.dbf", FIELDS, ROWS)
    raw = bytearray(path.read_bytes())
    raw[10:12] = struct.pack("<H", 99)
    with pytest.raises(ValueError, match="declara 99"):
        _with_field_offsets(bytes(raw[: 32 + 32 * len(FIELDS) + 1]))


@pytest.mark.parametrize("chunk_bytes", [None, 40])
def test_read_dbf_reads_each_field_from_its_own_position(tmp_path, chunk_bytes):
    path = make_dbf(tmp_path / "x.dbf", FIELDS, ROWS)
    df = read_dbf(path, chunk_bytes=chunk_bytes)

    assert df["N_AIH"].to_list() == ["1200002022010", "1200002022011"]
    assert df["SEXO"].to_list() == ["1", "3"]
    assert df["DT_INTER"].to_list() == ["20220103", "20220131"]
    assert df["DIAS_PERM"].to_list() == [4, 0]


def test_numeric_fields_with_decimals_are_exact(tmp_path):
    path = make_dbf(tmp_path / "x.dbf", FIELDS, ROWS)
    df = read_dbf(path)

    assert df.schema["VAL_TOT"] == pl.Decimal(precision=14, scale=2)
    assert df["VAL_TOT"].to_list() == [Decimal("1508094.36"), Decimal("0.29")]
    assert df["VAL_TOT"].sum() == Decimal("1508094.65")


def test_fixture_fastdbf_matches_dbfread_on_every_column(tmp_path):
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture não encontrada")
    dbf = decompress_dbc(FIXTURE_DBC, tmp_path / "doac1996.dbf")

    fast = read_dbf(dbf)
    slow = _read_dbf_dbfread(dbf, "latin1")
    columns = [c for c in slow.columns if c != "_deleted"]

    assert fast.height == slow.height
    different = [
        c
        for c in columns
        if fast[c].cast(pl.String).to_list() != slow[c].cast(pl.String).to_list()
    ]
    assert different == []
    assert fast["SEXO"].is_in(["0", "1", "2", "9"]).all()


def test_wrangle_keeps_codes_and_sim_dates_as_text():
    raw = pl.DataFrame(
        {
            "SEXO": ["M", "F", "I"],
            "RACA_COR": ["01", "04", "99"],
            "IDADE": ["487", "203", "999"],
            # SIM: DDMMAAAA, às vezes parcial (só o ano ou mês e ano)
            "DTOBITO": ["31122020", "1996", "011996"],
            "DT_INTER": ["20220103", "00000000", "20220131"],
            "DIAS_PERM": ["4", "0", " "],
        }
    )
    df = wrangle_datasus(raw)

    assert df["sexo"].to_list() == ["M", "F", "I"]
    assert df["raca_cor"].to_list() == ["01", "04", "99"]
    assert df["idade"].to_list() == ["487", "203", "999"]
    assert df["dtobito"].to_list() == ["31122020", "1996", "011996"]
    assert df["dt_inter"].to_list() == [dt.date(2022, 1, 3), None, dt.date(2022, 1, 31)]
    assert df["dias_perm"].to_list() == [4, 0, None]


def test_wrangle_keeps_exact_decimal_monetary_columns(tmp_path):
    path = make_dbf(tmp_path / "x.dbf", FIELDS, ROWS)
    df = wrangle_datasus(read_dbf(path))
    assert df["val_tot"].to_list() == [Decimal("1508094.36"), Decimal("0.29")]


@pytest.mark.parametrize(
    ("column", "valid", "invalid"),
    [
        ("DT_INTER", "20220103", "20220231"),
        ("DIAS_PERM", "0", "4a"),
        ("VAL_TOT", "10,50", "10,5x"),
    ],
)
def test_wrangle_raises_instead_of_nulling_invalid_values(column, valid, invalid):
    raw = pl.DataFrame({column: [valid, invalid]})
    with pytest.raises(ValueError, match=f"{column}: 1 valor"):
        wrangle_datasus(raw)


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        (
            "sih-rd_202201-ac@20230206.dbc",
            {"dataset": "sih-rd", "ano": 2022, "mes": 1, "uf": "ac"},
        ),
        (
            "sim-do-cid10_2022-ac_20231221.dbc",
            {"dataset": "sim-do-cid10", "ano": 2022, "uf": "ac"},
        ),
        (
            "sim-do-cid10_2022-br@20231221.dbc",
            {"dataset": "sim-do-cid10", "ano": 2022, "uf": "br"},
        ),
        (
            "sim-doext-cid10_2024_20251223.dbc",
            {"dataset": "sim-doext-cid10", "ano": 2024},
        ),
        (
            "sia-pa_201501-ac@20160912.dbc",
            {"dataset": "sia-pa", "ano": 2015, "mes": 1, "uf": "ac"},
        ),
    ],
)
def test_parse_filename_metadata_reads_stored_names(name, expected):
    assert parse_filename_metadata(name) == expected
