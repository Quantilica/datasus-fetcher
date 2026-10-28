"""Bases auxiliares em ZIP: população IBGE, base territorial e .cnv do TabWin."""

import zipfile
from pathlib import Path

import pytest

pl = pytest.importorskip("polars")
pytest.importorskip("quantilica.analytics.lake")

from quantilica.analytics.lake import scan_dataset  # noqa: E402

from datasus_fetcher.lake import converter  # noqa: E402
from datasus_fetcher.lake_bases import expand_codes, read_cnv  # noqa: E402

DBF = Path(__file__).parent / "fixtures" / "dbf" / "DOAC2022_head.dbf"

CNV_SIMPLES = (
    "4 6\r\n"
    "      1  12001 Alto Acre                                    120005,120010\r\n"
    "      2  12002 Baixo Acre                                   120020-120022\r\n"
)
CNV_SUBTOTAL = (
    "N 3 6\r\n"
    "      1  1201 MACRO UNICA - AC\r\n"
    "      1      2     ..... RIO BRANCO                         120040\r\n"
    "  1   3  .... Assis Brasil                                  120005\r\n"
)


def test_expand_codes() -> None:
    assert expand_codes("120001,120005-120007") == [
        "120001",
        "120005",
        "120006",
        "120007",
    ]
    assert expand_codes("A01-B02") == ["A01-B02"]


def test_read_cnv_layouts() -> None:
    simples = read_cnv(CNV_SIMPLES, "ac_regsaud")
    assert simples["codigo"].to_list() == [
        "120005",
        "120010",
        "120020",
        "120021",
        "120022",
    ]
    assert simples["descricao"][0] == "12001 Alto Acre"

    sub = read_cnv(CNV_SUBTOTAL, "ac_macsaudmun")
    # o título de grupo (sem código) fica de fora
    assert sub.select("sequencia", "nivel", "descricao", "codigo").rows() == [
        (2, 1, "RIO BRANCO", "120040"),
        (3, 1, "Assis Brasil", "120005"),
    ]


def _zip(path: Path, members: dict[str, bytes]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w") as zf:
        for name, data in members.items():
            zf.writestr(name, data)
    return path


def test_convert_base_zips(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    _zip(
        raw
        / "base-populacional-ibge-pop/2022"
        / "base-populacional-ibge-pop_2022-br@20240101.zip",
        {"POPBR22.DBF": DBF.read_bytes(), "POPBR22.csv": b"x"},
    )
    _zip(
        raw / "base-territorial-conversao/base-territorial-conversao_ac@20261015.zip",
        {"AC_regsaud.cnv": CNV_SIMPLES.encode("latin-1")},
    )
    old = "base-territorial/base-territorial_01-base_territorial_jan24@20240117.zip"
    new = "base-territorial/base-territorial_01-base_territorial_jan25@20250117.zip"
    _zip(raw / old, {"tb_antiga.csv": b"a;b\n1;2\n"})
    _zip(
        raw / new,
        {
            "tb_regiao.csv": b"co_regiao;ds_nome\n1;Norte\n2;Nordeste\n",
            "tb_regiao_layout.csv": b"campo;tipo\n",
        },
    )
    _zip(
        raw / "base-territorial-mapas/2025/base-territorial-mapas_2025-ac@20260918.zip",
        {"ac.MAP": b"\x00"},
    )

    res = converter.convert(raw, tmp_path / "lake")

    assert res.errors == []
    assert res.converted == 3
    lake = tmp_path / "lake" / "datasus"
    assert sorted(p.name for p in lake.iterdir()) == [
        "base-populacional-ibge-pop",
        "base-territorial-conversao",
        "base-territorial-tb-regiao",
    ]
    assert scan_dataset(lake / "base-territorial-tb-regiao").collect()[
        "ds_nome"
    ].to_list() == [
        "Norte",
        "Nordeste",
    ]
    pop = scan_dataset(lake / "base-populacional-ibge-pop").collect()
    assert pop["ano"].unique().to_list() == ["2022"]
    assert converter.convert(raw, tmp_path / "lake").skipped == 3
