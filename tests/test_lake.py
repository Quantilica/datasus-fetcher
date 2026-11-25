"""Tests for Hive lake conversion of DATASUS microdata."""

from __future__ import annotations

import json
import weakref
from importlib.metadata import entry_points
from pathlib import Path

import polars as pl
import pyarrow.parquet as pq
import pytest

pytest.importorskip("quantilica.analytics.lake")
pytest.importorskip("duckdb")

from quantilica.analytics.lake import check_dataset, scan_dataset  # noqa: E402
from typer.testing import CliRunner  # noqa: E402

import datasus_fetcher.lake as lake_module  # noqa: E402
from datasus_fetcher.lake import (  # noqa: E402
    SOURCE_ID,
    converter,
    resolve_dataset_id,
    resolve_partitions,
)
from datasus_fetcher.plugin import app  # noqa: E402

FIXTURE_DBC = Path(__file__).parent / "fixtures" / "DOAC1996.dbc"


def test_entry_point_registered() -> None:
    eps = entry_points(group="quantilica.lake")
    matches = [ep for ep in eps if ep.name == "datasus"]
    assert len(matches) == 1
    loaded = matches[0].load()
    assert loaded is converter
    assert loaded.source_id == SOURCE_ID


def test_resolve_dataset_id() -> None:
    assert (
        resolve_dataset_id(Path("DOAC1996.dbc"), {"dataset": "sim-do", "ano": 1996})
        == "sim-do-cid10"
    )
    assert (
        resolve_dataset_id(Path("DOAC1995.dbc"), {"dataset": "sim-do", "ano": 1995})
        == "sim-do-cid09"
    )
    assert (
        resolve_dataset_id(Path("sih-rd/RDSP2401.dbc"), {"dataset": "sih-rd"})
        == "sih-rd"
    )


def test_resolve_partitions() -> None:
    keys, values = resolve_partitions(
        {"uf": "sp", "ano": 2024, "mes": 1, "dataset": "sih-rd"}
    )
    assert keys == ["uf", "ano", "mes"]
    assert values == {"uf": "sp", "ano": "2024", "mes": "01"}

    keys_sim, values_sim = resolve_partitions(
        {"uf": "ac", "ano": 1996, "dataset": "sim-do"}
    )
    assert keys_sim == ["uf", "ano"]
    assert values_sim == {"uf": "ac", "ano": "1996"}


def test_converter_datasets() -> None:
    datasets = converter.datasets()
    assert "sim-do-cid10" in datasets
    assert "sih-rd" in datasets
    assert "sinasc-dn" in datasets


def test_convert_end_to_end(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")

    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    # Copy fixture
    raw_file = raw_dir / "DOAC1996.dbc"
    raw_file.write_bytes(FIXTURE_DBC.read_bytes())

    lake_dir = tmp_path / "lake"
    res = converter.convert(raw_dir, lake_dir)
    assert not res.errors, res.errors
    assert res.converted == 1
    assert res.skipped == 0

    dataset_dir = lake_dir / SOURCE_ID / "sim-do-cid10"
    assert check_dataset(dataset_dir) == []

    df = scan_dataset(dataset_dir).collect()
    assert df.height == 2263
    assert "uf" in df.columns
    assert "ano" in df.columns
    assert df["uf"][0] == "ac"
    assert df["ano"][0] == 1996

    # Second pass skips without decoding the DBC again
    def no_decode(*args, **kwargs):
        raise AssertionError("DBC decodificado de novo")

    monkeypatch.setattr(lake_module.reader, "read_dbc", no_decode)
    res2 = converter.convert(raw_dir, lake_dir)
    assert not res2.errors
    assert res2.converted == 0
    assert res2.skipped == 1


def test_cli_convert_lake(tmp_path: Path) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")

    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    raw_file = raw_dir / "DOAC1996.dbc"
    raw_file.write_bytes(FIXTURE_DBC.read_bytes())

    lake_dir = tmp_path / "lake"
    runner = CliRunner()
    result = runner.invoke(
        app,
        ["convert", "-i", str(raw_dir), "--lake", str(lake_dir)],
    )
    assert result.exit_code == 0, result.output
    assert (lake_dir / SOURCE_ID / "sim-do-cid10").exists()


def test_ufs_do_mesmo_periodo_dividem_um_parquet(tmp_path: Path) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    # O mesmo conteúdo publicado como AC e como RO: um Parquet para 1996, com a UF
    # numa coluna e o bruto de cada linha em _origem.
    (raw_dir / "DOAC1996.dbc").write_bytes(FIXTURE_DBC.read_bytes())
    (raw_dir / "DORO1996.dbc").write_bytes(FIXTURE_DBC.read_bytes())
    lake_dir = tmp_path / "lake"
    res = converter.convert(raw_dir, lake_dir)
    assert not res.errors, res.errors
    assert res.converted == 2

    dataset_dir = lake_dir / SOURCE_ID / "sim-do-cid10"
    files = [
        p.relative_to(dataset_dir).as_posix() for p in dataset_dir.rglob("*.parquet")
    ]
    assert files == ["ano=1996/sim-do-cid10_1996.parquet"]
    assert check_dataset(dataset_dir) == []
    df = scan_dataset(dataset_dir).collect()
    assert df.height == 2 * 2263
    assert df["uf"].unique().sort().to_list() == ["ac", "ro"]
    assert df["_origem"].unique().sort().to_list() == ["DOAC1996", "DORO1996"]


def _periodo_com_ufs(raw_dir: Path, ufs: tuple[str, ...]) -> None:
    raw_dir.mkdir(exist_ok=True)
    for uf in ufs:
        (raw_dir / f"DO{uf}1996.dbc").write_bytes(FIXTURE_DBC.read_bytes())


def _metodo_antigo(raw_dir: Path, lake_dir: Path) -> None:
    """O que o conversor fazia: um ``write_member`` por arquivo, na ordem."""
    from quantilica.analytics.lake import LakeWriter
    from quantilica.core.lake import DatasetDescriptor, partition_types_for

    from datasus_fetcher import lake_bases, reader

    writer = LakeWriter(
        lake_dir / SOURCE_ID / "sim-do-cid10",
        DatasetDescriptor(
            source_id=SOURCE_ID,
            dataset_id="sim-do-cid10",
            alias="sim-do-cid10",
            partition_keys=["ano"],
            partition_types=partition_types_for(["ano"]),
        ),
    )
    for path in sorted(raw_dir.glob("*.dbc")):
        dataset_id, meta_dict = lake_module.route_file(path)
        keys, values, member, group = lake_bases.group_partitions(
            dataset_id, *resolve_partitions(meta_dict)
        )
        writer.write_member(
            reader.read_dbc(path, clean=True, dataset=dataset_id, lowercase=True),
            path,
            group_key=group,
            partitions=values,
            member_columns=member,
        )


def test_grupo_em_uma_passada_igual_ao_membro_a_membro(tmp_path: Path) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")
    raw = tmp_path / "raw"
    _periodo_com_ufs(raw, ("AC", "RO", "SP"))
    novo, antigo = tmp_path / "novo", tmp_path / "antigo"

    res = converter.convert(raw, novo)
    assert not res.errors, res.errors
    assert (res.converted, res.skipped) == (3, 0)
    _metodo_antigo(raw, antigo)

    rel = Path(SOURCE_ID) / "sim-do-cid10" / "ano=1996" / "sim-do-cid10_1996.parquet"
    a, b = pq.ParquetFile(antigo / rel), pq.ParquetFile(novo / rel)
    # Mesmo arquivo, mesmas colunas e tipos, mesma contagem de linhas.
    assert [(f.name, f.type) for f in a.schema_arrow] == [
        (f.name, f.type) for f in b.schema_arrow
    ]
    assert a.metadata.num_rows == b.metadata.num_rows == 3 * 2263
    keys = ["uf", "_origem"]
    da = pl.read_parquet(antigo / rel).sort(keys, maintain_order=True)
    db = pl.read_parquet(novo / rel)
    # Blocos na mesma ordem (UF, depois o bruto) e o mesmo conteúdo.
    assert db.select(keys).to_series(0).to_list() == da["uf"].to_list()
    assert db["_origem"].to_list() == da["_origem"].to_list()
    assert db.sort(db.columns).equals(da.sort(da.columns))

    # O rodapé guarda os mesmos membros.
    def members(path: Path) -> dict:
        kv = pq.ParquetFile(path).schema_arrow.metadata
        entries = json.loads(kv[b"quantilica.members"])
        return {
            k: {f: v for f, v in e.items() if f != "converted_at"}
            for k, e in entries.items()
        }

    assert members(antigo / rel) == members(novo / rel)
    assert check_dataset(novo / SOURCE_ID / "sim-do-cid10") == []


def test_grupo_nao_usa_write_member_nem_segura_dois_arquivos(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")
    raw = tmp_path / "raw"
    _periodo_com_ufs(raw, ("AC", "RO", "SP"))

    def refuses(*args, **kwargs):
        raise AssertionError("write_member não deve ser usado")

    monkeypatch.setattr(lake_module.LakeWriter, "write_member", refuses)
    alive: list[weakref.ref] = []
    decode = lake_module._decode

    def watched(path: Path, dataset_id: str) -> pl.DataFrame:
        # Os arquivos anteriores já foram soltos quando o próximo é decodificado.
        assert [r for r in alive if r() is not None] == []
        frame = decode(path, dataset_id)
        alive.append(weakref.ref(frame))
        return frame

    monkeypatch.setattr(lake_module, "_decode", watched)
    res = converter.convert(raw, tmp_path / "lake")
    assert not res.errors, res.errors
    assert res.converted == 3
    assert len(alive) == 3


def test_grupo_so_decodifica_o_membro_novo(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")
    raw, lake = tmp_path / "raw", tmp_path / "lake"
    _periodo_com_ufs(raw, ("AC",))
    assert converter.convert(raw, lake).converted == 1

    _periodo_com_ufs(raw, ("AC", "RO"))
    decoded: list[str] = []
    decode = lake_module._decode

    def counting(path: Path, dataset_id: str) -> pl.DataFrame:
        decoded.append(path.name)
        return decode(path, dataset_id)

    monkeypatch.setattr(lake_module, "_decode", counting)
    res = converter.convert(raw, lake)
    assert not res.errors, res.errors
    assert (res.converted, res.skipped) == (1, 1)
    assert decoded == ["DORO1996.dbc"]
    df = scan_dataset(lake / SOURCE_ID / "sim-do-cid10").collect()
    assert df["uf"].unique().sort().to_list() == ["ac", "ro"]
    # Nada a fazer na terceira vez.
    decoded.clear()
    res = converter.convert(raw, lake)
    assert (res.converted, res.skipped) == (0, 2)
    assert decoded == []


def test_grupo_arquivo_ruim_nao_derruba_os_outros(tmp_path: Path) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")
    raw, lake = tmp_path / "raw", tmp_path / "lake"
    _periodo_com_ufs(raw, ("AC", "SP"))
    (raw / "DORO1996.dbc").write_bytes(b"isto nao e um dbc")

    res = converter.convert(raw, lake)
    assert len(res.errors) == 1
    assert res.errors[0].startswith("DORO1996.dbc:")
    assert (res.converted, res.skipped) == (2, 0)
    df = scan_dataset(lake / SOURCE_ID / "sim-do-cid10").collect()
    assert df["uf"].unique().sort().to_list() == ["ac", "sp"]


def test_grupo_recusado_cai_para_membro_a_membro(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")
    raw, lake = tmp_path / "raw", tmp_path / "lake"
    _periodo_com_ufs(raw, ("AC", "RO"))

    def refuses(*args, **kwargs):
        raise lake_module.LakeError(
            "x: column 'a' is BIGINT but the group has VARCHAR; "
            "declare the type in `schema`"
        )

    monkeypatch.setattr(lake_module.LakeWriter, "write_group", refuses)
    res = converter.convert(raw, lake)
    assert not res.errors, res.errors
    assert (res.converted, res.skipped, res.fallbacks) == (2, 0, 1)
    df = scan_dataset(lake / SOURCE_ID / "sim-do-cid10").collect()
    assert df.height == 2 * 2263
    assert df["uf"].unique().sort().to_list() == ["ac", "ro"]
    # Pulado na segunda rodada, também pelo caminho de reserva.
    res = converter.convert(raw, lake)
    assert (res.converted, res.skipped) == (0, 2)


def test_grupo_recusa_de_integridade_e_erro_nao_queda(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")
    raw = tmp_path / "raw"
    _periodo_com_ufs(raw, ("AC", "RO"))

    def refuses(*args, **kwargs):
        raise lake_module.LakeError("group: the file has 1 rows but its members add up")

    monkeypatch.setattr(lake_module.LakeWriter, "write_group", refuses)
    monkeypatch.setattr(lake_module.LakeWriter, "write_member", refuses)
    res = converter.convert(raw, tmp_path / "lake")
    assert res.fallbacks == 0
    assert res.converted == 0
    assert len(res.errors) == 1
    assert res.errors[0].startswith("sim-do-cid10_1996:")


def test_duas_versoes_do_mesmo_bruto_valem_a_mais_nova(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")
    raw, lake = tmp_path / "raw", tmp_path / "lake"
    _periodo_com_ufs(raw, ("RO",))
    # AC publicado duas vezes: a versão velha está ilegível e não pode ser aberta.
    (raw / "DOAC1996@20260906.dbc").write_bytes(b"versao velha")
    (raw / "DOAC1996@20261016.dbc").write_bytes(FIXTURE_DBC.read_bytes())
    decoded: list[str] = []
    decode = lake_module._decode

    def counting(path: Path, dataset_id: str) -> pl.DataFrame:
        decoded.append(path.name)
        return decode(path, dataset_id)

    monkeypatch.setattr(lake_module, "_decode", counting)
    res = converter.convert(raw, lake)
    assert not res.errors, res.errors
    assert (res.converted, res.skipped) == (2, 1)
    assert sorted(decoded) == ["DOAC1996@20261016.dbc", "DORO1996.dbc"]
    df = scan_dataset(lake / SOURCE_ID / "sim-do-cid10").collect()
    assert df["uf"].unique().sort().to_list() == ["ac", "ro"]
    assert df["_origem"].unique().sort().to_list() == ["DOAC1996", "DORO1996"]


def test_grupo_cada_bruto_e_decodificado_uma_vez_mesmo_com_um_ruim(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")
    raw = tmp_path / "raw"
    _periodo_com_ufs(raw, ("AC", "RO"))
    (raw / "DOSP1996.dbc").write_bytes(b"isto nao e um dbc")  # o último da ordem
    decoded: list[str] = []
    decode = lake_module._decode

    def counting(path: Path, dataset_id: str) -> pl.DataFrame:
        decoded.append(path.name)
        return decode(path, dataset_id)

    monkeypatch.setattr(lake_module, "_decode", counting)
    res = converter.convert(raw, tmp_path / "lake")
    assert len(res.errors) == 1 and res.errors[0].startswith("DOSP1996.dbc:")
    assert (res.converted, res.skipped) == (2, 0)
    assert sorted(decoded) == ["DOAC1996.dbc", "DORO1996.dbc", "DOSP1996.dbc"]


def test_grupo_temporarios_ficam_no_scratch_e_somem(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")
    raw = tmp_path / "raw"
    _periodo_com_ufs(raw, ("AC", "RO", "SP"))
    scratch = tmp_path / "scratch"
    monkeypatch.setenv("QUANTILICA_LAKE_SCRATCH", str(scratch))
    seen: list[Path] = []
    decode = lake_module._decode
    alive: list[int] = []
    stage = lake_module.LakeWriter._stage_member

    def staging(self, *args, **kwargs):
        # O temporário do membro anterior sai quando o escritor pede o próximo.
        alive.append(len(list(scratch.glob("datasus-members-*/*.parquet"))))
        return stage(self, *args, **kwargs)

    monkeypatch.setattr(lake_module.LakeWriter, "_stage_member", staging)

    def watching(path: Path, dataset_id: str) -> pl.DataFrame:
        seen.extend(scratch.glob("datasus-members-*"))
        return decode(path, dataset_id)

    monkeypatch.setattr(lake_module, "_decode", watching)
    res = converter.convert(raw, tmp_path / "lake")
    assert not res.errors, res.errors
    assert seen and all(p.parent == scratch for p in seen)
    assert alive == [3, 2, 1]
    assert list(scratch.glob("datasus-members-*")) == []


def test_inventory_roteia_e_ignora(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    (raw / "sih-rd").mkdir(parents=True)
    (raw / "base-territorial").mkdir()
    (raw / "base-territorial-mapas").mkdir()
    (raw / "sih-rd" / "RDSP2401.dbc").write_bytes(b"x")
    (raw / "sih-rd" / "RDSP2401.dbc.manifest.json").write_text("{}")
    (raw / "sih-rd" / "RDSP2402.dbc.tmp").write_bytes(b"x")
    (raw / "sih-rd" / "LEIAME.pdf").write_bytes(b"x")
    (raw / "base-territorial" / "base-territorial@20240101.zip").write_bytes(b"x")
    (raw / "base-territorial" / "base-territorial@20250101.zip").write_bytes(b"x")
    (raw / "base-territorial-mapas" / "mapas@20250101.zip").write_bytes(b"x")
    (raw / "AC.map").write_bytes(b"x")

    got = {p.path.relative_to(raw).as_posix(): p for p in converter.inventory(raw)}

    assert set(got) == {
        "sih-rd/RDSP2401.dbc",
        "sih-rd/LEIAME.pdf",
        "base-territorial/base-territorial@20240101.zip",
        "base-territorial/base-territorial@20250101.zip",
        "base-territorial-mapas/mapas@20250101.zip",
        "AC.map",
    }
    assert got["sih-rd/RDSP2401.dbc"].dataset == "sih-rd"
    assert got["sih-rd/RDSP2401.dbc"].skip_reason is None
    assert got["sih-rd/LEIAME.pdf"].skip_reason == "nao_tabular"
    assert got["AC.map"].skip_reason == "nao_tabular"
    assert got["base-territorial-mapas/mapas@20250101.zip"].skip_reason == "nao_tabular"
    old = got["base-territorial/base-territorial@20240101.zip"]
    assert old.skip_reason == "superado"
    new = got["base-territorial/base-territorial@20250101.zip"]
    assert (new.dataset, new.skip_reason) == ("base-territorial", None)


def test_inventory_marca_versoes_antigas_do_dbc(tmp_path: Path) -> None:
    raw = tmp_path / "raw" / "sih-rd"
    raw.mkdir(parents=True)
    for nome in ("RDSP2401@20260906.dbc", "RDSP2401@20261016.dbc", "RDSP2402.dbc"):
        (raw / nome).write_bytes(b"x")

    got = {p.path.name: (p.dataset, p.skip_reason) for p in converter.inventory(raw)}
    assert got["RDSP2401@20260906.dbc"] == (None, "superado")
    assert got["RDSP2401@20261016.dbc"] == ("sih-rd", None)
    assert got["RDSP2402.dbc"] == ("sih-rd", None)


def test_inventory_coincide_com_convert(tmp_path: Path) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")
    raw = tmp_path / "raw"
    raw.mkdir()
    (raw / "DOAC1996.dbc").write_bytes(FIXTURE_DBC.read_bytes())

    (item,) = converter.inventory(raw)
    assert item.dataset == "sim-do-cid10"
    converter.convert(raw, tmp_path / "lake")
    assert (tmp_path / "lake" / SOURCE_ID / item.dataset).is_dir()
    assert converter.inventory(tmp_path / "ausente") == []


def test_dbc_superado_conta_em_skipped_so_dos_datasets_pedidos(
    tmp_path: Path,
) -> None:
    if not FIXTURE_DBC.exists():
        pytest.skip("Fixture DOAC1996.dbc não encontrada")
    raw, lake = tmp_path / "raw", tmp_path / "lake"
    raw.mkdir()
    (raw / "DOAC1996@20260906.dbc").write_bytes(b"versao velha")
    (raw / "DOAC1996@20261016.dbc").write_bytes(FIXTURE_DBC.read_bytes())
    res = converter.convert(raw, lake, datasets=["sih-rd"])
    assert (res.converted, res.skipped, res.errors) == (0, 0, [])
    res = converter.convert(raw, lake, datasets=["sim-do-cid10"])
    assert (res.converted, res.skipped, res.errors) == (1, 1, [])
