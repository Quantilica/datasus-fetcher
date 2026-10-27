"""Tests for Hive lake conversion of DATASUS microdata."""

from __future__ import annotations

from importlib.metadata import entry_points
from pathlib import Path

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
    assert df["ano"][0] == "1996"

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
