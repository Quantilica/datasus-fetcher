"""O build das bases auxiliares pula, sem abrir o ZIP, o que já está em dia."""

from __future__ import annotations

import builtins
import hashlib
import io
import json
import zipfile
from pathlib import Path
from typing import Any

import pytest

pytest.importorskip("polars")
pytest.importorskip("quantilica.analytics.lake")

import datasus_fetcher.lake_bases as bases  # noqa: E402
from datasus_fetcher.lake import converter  # noqa: E402

DBF = Path(__file__).parent / "fixtures" / "dbf" / "DOAC2022_head.dbf"
CNV = (
    "4 6\r\n"
    "      1  12001 Alto Acre                                    120005,120010\r\n"
)
TERRITORIAL = "base-territorial"
NOVO = "base-territorial/base-territorial_01-base_territorial_jan25@20250117.zip"
ANTIGO = "base-territorial/base-territorial_01-base_territorial_jan24@20240117.zip"


def _zip(path: Path, members: dict[str, bytes]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w") as zf:
        for name, data in members.items():
            zf.writestr(name, data)
    data = path.read_bytes()
    path.with_name(path.name + ".manifest.json").write_text(
        json.dumps(
            {"sha256": hashlib.sha256(data).hexdigest(), "size_bytes": len(data)}
        ),
        encoding="utf-8",
    )
    return path


def _bruto(tmp_path: Path) -> Path:
    raw = tmp_path / "raw"
    _zip(raw / ANTIGO, {"tb_antiga.csv": b"a;b\n1;2\n"})
    _zip(
        raw / NOVO,
        {
            "tb_regiao.csv": b"co_regiao;ds_nome\n1;Norte\n2;Nordeste\n",
            "tb_uf.csv": b"co_uf;sg_uf\n12;AC\n",
            "tb_regiao_layout.csv": b"campo;tipo\n",
        },
    )
    _zip(
        raw / "base-territorial-conversao/base-territorial-conversao_ac@20261015.zip",
        {"AC_regsaud.cnv": CNV.encode("latin-1")},
    )
    _zip(
        raw
        / "base-populacional-ibge-pop/2022"
        / "base-populacional-ibge-pop_2022-br@20240101.zip",
        {"POPBR22.DBF": DBF.read_bytes()},
    )
    return raw


@pytest.fixture
def acessos(monkeypatch: pytest.MonkeyPatch) -> list[str]:
    """Registra todo acesso ao bruto: ``ZipFile``, leitores e ``open``."""
    vistos: list[str] = []

    def espia(nome: str, original: Any) -> Any:
        def _f(*args: Any, **kwargs: Any) -> Any:
            vistos.append(nome)
            return original(*args, **kwargs)

        return _f

    monkeypatch.setattr(zipfile, "ZipFile", espia("ZipFile", zipfile.ZipFile))
    for nome in ("read_dbf", "decompress_dbc"):
        monkeypatch.setattr(
            bases.reader, nome, espia(nome, getattr(bases.reader, nome))
        )
    monkeypatch.setattr(bases.pl, "read_csv", espia("read_csv", bases.pl.read_csv))

    original_open = builtins.open

    def aberto(file: Any, *args: Any, **kwargs: Any) -> Any:
        if "raw" in Path(str(file)).parts and not str(file).endswith(".manifest.json"):
            vistos.append(f"open:{file}")
        return original_open(file, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", aberto)
    monkeypatch.setattr(io, "open", aberto)
    return vistos


@pytest.mark.parametrize(
    ("dataset", "convertidos"),
    [
        (TERRITORIAL, 2),
        ("base-territorial-conversao", 1),
        ("base-populacional-ibge-pop", 1),
    ],
)
def test_segunda_rodada_por_dataset_nao_abre_o_zip(
    tmp_path: Path, acessos: list[str], dataset: str, convertidos: int
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    res = converter.convert(raw, lake, datasets=[dataset])
    assert res.errors == []
    assert (res.converted, res.skipped) == (convertidos, 0)
    assert acessos  # a primeira rodada abre o ZIP

    acessos.clear()
    res2 = converter.convert(raw, lake, datasets=[dataset])
    assert (res2.converted, res2.skipped, res2.errors) == (0, convertidos, [])
    assert acessos == []


def test_sem_datasets_continua_convertendo_e_pulando(
    tmp_path: Path, acessos: list[str]
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    res = converter.convert(raw, lake)
    assert (res.converted, res.skipped, res.errors) == (4, 0, [])
    acessos.clear()
    res2 = converter.convert(raw, lake)
    assert (res2.converted, res2.skipped, res2.errors) == (0, 4, [])
    assert acessos == []


def test_force_abre_o_zip_e_reconverte(tmp_path: Path, acessos: list[str]) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=[TERRITORIAL])
    acessos.clear()
    res = converter.convert(raw, lake, datasets=[TERRITORIAL], force=True)
    assert (res.converted, res.skipped) == (2, 0)
    assert "ZipFile" in acessos


def test_zip_novo_converte_e_o_antigo_nao_e_aberto(
    tmp_path: Path, acessos: list[str]
) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=[TERRITORIAL])
    mais_novo = (
        raw / "base-territorial/base-territorial_01-base_territorial_jul25@20250717.zip"
    )
    _zip(mais_novo, {"tb_regiao.csv": b"co_regiao;ds_nome\n1;Norte\n"})

    acessos.clear()
    res = converter.convert(raw, lake, datasets=[TERRITORIAL])
    assert (res.converted, res.skipped, res.errors) == (1, 0, [])
    assert acessos.count("ZipFile") == 1  # só o ZIP novo


def test_zip_alterado_reconverte(tmp_path: Path, acessos: list[str]) -> None:
    raw, lake = _bruto(tmp_path), tmp_path / "lake"
    converter.convert(raw, lake, datasets=[TERRITORIAL])
    _zip(
        raw / NOVO,
        {
            "tb_regiao.csv": b"co_regiao;ds_nome\n1;Norte\n2;Nordeste\n3;Sul\n",
            "tb_uf.csv": b"co_uf;sg_uf\n12;AC\n",
        },
    )

    acessos.clear()
    res = converter.convert(raw, lake, datasets=[TERRITORIAL])
    assert (res.converted, res.skipped, res.errors) == (2, 0, [])
    assert "ZipFile" in acessos
