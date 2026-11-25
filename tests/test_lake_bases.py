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
    assert pop["ano"].unique().to_list() == [2022]
    assert converter.convert(raw, tmp_path / "lake").skipped == 4


POP_DIR = "base-populacional-ibge-pop/2022"
POP = "base-populacional-ibge-pop_2022-br"
CONV_DIR = "base-territorial-conversao"
CNV_OUTRO = (
    "4 6\r\n"
    "      1  13001 Rio Negro                                    130010,130020\r\n"
)


def _pop_zip(raw: Path, stamp: str, *, extra: bool = False) -> Path:
    members = {"POPBR22.DBF": DBF.read_bytes()}
    if extra:  # bytes diferentes, mesmos dados
        members["LEIAME.txt"] = b"revisao"
    return _zip(raw / POP_DIR / f"{POP}@{stamp}.zip", members)


def _linhas(lake: Path, dataset: str) -> int:
    return scan_dataset(lake / "datasus" / dataset).collect().height


def test_versoes_antigas_das_bases_nao_sao_abertas(tmp_path: Path) -> None:
    raw, lake = tmp_path / "raw", tmp_path / "lake"
    # As versões antigas são ZIPs inválidos: abri-las seria erro contado.
    for antigo in (
        raw / POP_DIR / f"{POP}@20240101.zip",
        raw / CONV_DIR / f"{CONV_DIR}_ac@20261001.zip",
    ):
        antigo.parent.mkdir(parents=True, exist_ok=True)
        antigo.write_bytes(b"nao e um zip")
    _pop_zip(raw, "20240601")
    _zip(
        raw / CONV_DIR / f"{CONV_DIR}_ac@20261015.zip",
        {"AC_regsaud.cnv": CNV_SIMPLES.encode("latin-1")},
    )

    res = converter.convert(raw, lake)
    assert (res.converted, res.errors) == (2, [])

    res2 = converter.convert(raw, lake)
    assert (res2.converted, res2.skipped, res2.errors) == (0, 4, [])


def test_versao_nova_das_bases_substitui_sem_duplicar(tmp_path: Path) -> None:
    raw, lake = tmp_path / "raw", tmp_path / "lake"
    _pop_zip(raw, "20240101")
    _zip(
        raw / CONV_DIR / f"{CONV_DIR}_ac@20261001.zip",
        {"AC_regsaud.cnv": CNV_SIMPLES.encode("latin-1")},
    )
    assert converter.convert(raw, lake).errors == []
    pop_antes = _linhas(lake, "base-populacional-ibge-pop")
    cnv_antes = _linhas(lake, "base-territorial-conversao")

    _pop_zip(raw, "20240601", extra=True)
    _zip(
        raw / CONV_DIR / f"{CONV_DIR}_ac@20261015.zip",
        {
            "AC_regsaud.cnv": CNV_SIMPLES.encode("latin-1"),
            "AC_outro.cnv": CNV_OUTRO.encode("latin-1"),
        },
    )
    res = converter.convert(raw, lake)
    assert (res.converted, res.skipped, res.errors) == (2, 2, [])

    # mesmas linhas da população (a versão nova, não a soma das duas) e as da
    # conversão da versão nova (5 + 2 códigos), sem sobra da antiga
    assert _linhas(lake, "base-populacional-ibge-pop") == pop_antes
    assert cnv_antes == 5
    assert _linhas(lake, "base-territorial-conversao") == 7

    # e a rodada seguinte não reconverte nada
    res3 = converter.convert(raw, lake)
    assert (res3.converted, res3.skipped, res3.errors) == (0, 4, [])


def test_inventario_marca_as_versoes_antigas_das_bases(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    antigo_pop = _pop_zip(raw, "20240101")
    novo_pop = _pop_zip(raw, "20240601")
    antigo_cnv = _zip(
        raw / CONV_DIR / f"{CONV_DIR}_ac@20261001.zip", {"AC.cnv": CNV_SIMPLES.encode()}
    )
    novo_cnv = _zip(
        raw / CONV_DIR / f"{CONV_DIR}_ac@20261015.zip", {"AC.cnv": CNV_SIMPLES.encode()}
    )
    outra_uf = _zip(
        raw / CONV_DIR / f"{CONV_DIR}_am@20261001.zip", {"AM.cnv": CNV_SIMPLES.encode()}
    )

    got = {p.path: (p.dataset, p.skip_reason) for p in converter.inventory(raw)}
    assert got[antigo_pop] == (None, "superado")
    assert got[novo_pop] == ("base-populacional-ibge-pop", None)
    assert got[antigo_cnv] == (None, "superado")
    assert got[novo_cnv] == (CONV_DIR, None)
    assert got[outra_uf] == (CONV_DIR, None)  # outra UF é outro arquivo


def test_versoes_superadas_contam_em_skipped(tmp_path: Path) -> None:
    raw, lake = tmp_path / "raw", tmp_path / "lake"
    antigo = raw / POP_DIR / f"{POP}@20240101.zip"
    antigo.parent.mkdir(parents=True, exist_ok=True)
    antigo.write_bytes(b"nao e um zip")
    _pop_zip(raw, "20240601")
    # Primeira rodada: a vigente converte, a superada conta em skipped.
    res = converter.convert(raw, lake)
    assert (res.converted, res.skipped, res.errors) == (1, 1, [])
    # Filtrar por outro dataset não conta as superadas das bases não pedidas.
    res2 = converter.convert(raw, lake, datasets=[CONV_DIR])
    assert (res2.converted, res2.skipped, res2.errors) == (0, 0, [])
