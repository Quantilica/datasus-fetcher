"""Regressão: o fastdbf lia colunas deslocadas nos .dbf do DATASUS.

Os descritores de campo do DATASUS deixam zerados os bytes 12-15 (deslocamento do
campo no registro, no FoxPro). O fastdbf 0.5.2 confia neles e lia todos os campos a
partir do byte 0 do registro: ``DTOBITO=" 1207052"`` em vez de ``"07052022"``.

As fixtures são os 25 primeiros registros de arquivos reais do FTP do DATASUS, com
o cabeçalho original (só a contagem de registros ajustada): SIM ``DOAC2022``,
SINASC ``DNAC2022``, SIH-RD ``RDAC2201`` e SINAN ``BOTUBR22`` e ``DENGBR24`` (20
primeiros registros mais 5 com ``DT_OBITO`` preenchido).
"""

import logging
import shutil
from pathlib import Path

import pytest

pl = pytest.importorskip("polars")
pytest.importorskip("fastdbf")
dbfread = pytest.importorskip("dbfread")

from datasus_fetcher import reader  # noqa: E402

FIXTURES = Path(__file__).parent / "fixtures" / "dbf"
DBF_FIXTURES = sorted(FIXTURES.glob("*_head.dbf"))


def _diferencas(frame, path: Path) -> list[str]:
    """Células em que ``frame`` diverge do dbfread lendo o mesmo arquivo."""
    table = dbfread.DBF(str(path), encoding="latin1")
    ref = list(table)
    assert frame.height == len(ref)
    erros = []
    for field in table.field_names:
        valores = frame[field.upper()].to_list()
        for i, (got, rec) in enumerate(zip(valores, ref, strict=True)):
            if not reader._same_value(got, rec[field]):  # noqa: SLF001
                erros.append(f"{field}[{i}]: {got!r} != {rec[field]!r}")
    return erros


def test_fixtures_presentes():
    assert {p.name for p in DBF_FIXTURES} == {
        "BOTUBR22_head.dbf",
        "DENGBR24_head.dbf",
        "DNAC2022_head.dbf",
        "DOAC2022_head.dbf",
        "RDAC2201_head.dbf",
    }


@pytest.mark.parametrize("path", DBF_FIXTURES, ids=lambda p: p.stem)
@pytest.mark.parametrize("chunk_bytes", [None, reader.DBF_CHUNK_BYTES, 2048])
def test_read_dbf_igual_ao_dbfread(path: Path, chunk_bytes, caplog):
    with caplog.at_level(logging.WARNING, logger=reader.__name__):
        frame = reader.read_dbf(path, chunk_bytes=chunk_bytes)
    assert _diferencas(frame, path) == []
    # O caminho rápido (fastdbf com cabeçalho corrigido) não deve precisar do fallback.
    assert not [r for r in caplog.records if "divergiu" in r.getMessage()]


def test_valores_conhecidos_do_sim():
    """Valores conferidos à mão no primeiro registro de DOAC2022 (SIM, Acre)."""
    frame = reader.read_dbf(FIXTURES / "DOAC2022_head.dbf")
    primeiro = frame.row(0, named=True)
    assert primeiro["DTOBITO"] == "07052022"
    assert primeiro["CAUSABAS"] == "I461"
    assert primeiro["CODMUNRES"] == "120017"


def test_read_dbf_nao_altera_o_arquivo_de_origem(tmp_path: Path):
    src = tmp_path / "doac.dbf"
    shutil.copy(FIXTURES / "DOAC2022_head.dbf", src)
    antes = src.read_bytes()
    reader.read_dbf(src)
    assert src.read_bytes() == antes


def test_fix_field_displacements():
    raw = (FIXTURES / "DOAC2022_head.dbf").read_bytes()
    header_len = int.from_bytes(raw[8:10], "little")
    header = raw[:header_len]
    assert reader._has_wrong_displacements(FIXTURES / "DOAC2022_head.dbf")  # noqa: SLF001
    fixed = reader._fix_field_displacements(header)  # noqa: SLF001
    assert len(fixed) == len(header)
    # O primeiro campo começa depois do byte de deleção; os seguintes, em sequência.
    assert int.from_bytes(fixed[32 + 12 : 32 + 16], "little") == 1
    segundo = 1 + fixed[32 + 16]
    assert int.from_bytes(fixed[64 + 12 : 64 + 16], "little") == segundo
    # Só os bytes de deslocamento mudam.
    for off in range(32, header_len - 1, 32):
        assert fixed[off : off + 12] == header[off : off + 12]
        assert fixed[off + 16 : off + 32] == header[off + 16 : off + 32]
    assert reader._fix_field_displacements(fixed) == fixed  # noqa: SLF001


def test_checagem_de_sanidade_cai_no_dbfread(monkeypatch, caplog):
    """Sem a correção do cabeçalho, a checagem detecta o deslocamento e avisa."""
    monkeypatch.setattr(reader, "_fix_field_displacements", lambda header: header)
    path = FIXTURES / "DOAC2022_head.dbf"
    with caplog.at_level(logging.WARNING, logger=reader.__name__):
        frame = reader.read_dbf(path)
    assert _diferencas(frame, path) == []
    assert any("divergiu" in r.getMessage() for r in caplog.records)


def test_sem_correcao_nem_checagem_o_fastdbf_desloca(monkeypatch):
    """Documenta o defeito do fastdbf que a correção contorna."""
    monkeypatch.setattr(reader, "_fix_field_displacements", lambda header: header)
    path = FIXTURES / "DOAC2022_head.dbf"
    frame = reader._read_dbf_piece(path, "latin1", sanity_rows=0)  # noqa: SLF001
    if frame["DTOBITO"][0] == "07052022":
        pytest.skip("fastdbf passou a ignorar o deslocamento zerado")
    assert frame["DTOBITO"][0] != "07052022"
