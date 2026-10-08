"""Tests for `sync --from-plan` and the `check --json` round-trip."""

import datetime as dt
import json
from pathlib import Path

import pytest

pytest.importorskip("typer")

from quantilica.cli.sdk import CheckPlan  # noqa: E402
from typer.testing import CliRunner  # noqa: E402

import datasus_fetcher.plugin as plugin  # noqa: E402
from datasus_fetcher import fetcher as fetcher_module  # noqa: E402
from datasus_fetcher.storage import (  # noqa: E402
    DataPartition,
    RemoteFile,
    get_data_filepath,  # noqa: E402
)

runner = CliRunner()
DATASET = "sih-rd"


def _remote(filename: str, year: int, month: int) -> RemoteFile:
    return RemoteFile(
        filename=filename,
        full_path=f"/dissemin/publicos/SIHSUS/200801_/Dados/{filename}",
        datetime=dt.datetime(2020, 2, 1),
        extension="dbc",
        size=1024,
        dataset=DATASET,
        partition=DataPartition(uf="br", year=year, month=month),
    )


class _FakeFtp:
    def close(self) -> None:
        pass


@pytest.fixture
def ftp_falso(monkeypatch):
    """Lista 2 arquivos de dados para sih-rd sem tocar na rede."""
    arquivos = [_remote("RDAC2001.dbc", 2020, 1), _remote("RDAC2002.dbc", 2020, 2)]
    monkeypatch.setattr(plugin, "_FTP_CONN", _FakeFtp())
    monkeypatch.setattr(plugin, "_get_ftp", lambda: plugin._FTP_CONN)
    monkeypatch.setattr(
        fetcher_module,
        "list_dataset_files",
        lambda ftp, dataset: list(arquivos) if dataset == DATASET else [],
    )
    monkeypatch.setattr(
        fetcher_module, "list_documentation_files", lambda ftp, dataset: []
    )
    monkeypatch.setattr(
        fetcher_module, "list_auxiliary_tables_files", lambda ftp, dataset: []
    )
    return arquivos


@pytest.fixture
def sem_download(monkeypatch):
    """Captura as entradas enviadas para download (sem baixar de verdade)."""
    chamadas: list = []

    def _fake(entries, output, workers=2):
        chamadas.append((list(entries), Path(output), workers))
        return (len(entries), len(entries), [])

    monkeypatch.setattr(plugin.fetcher_app, "download_datasets", _fake)
    return chamadas


def test_entry_plan_roundtrip_preserva_remote_file(ftp_falso):
    entradas = plugin.datasus_list_datasets(DATASET)
    assert len(entradas) == 2
    for entrada in entradas:
        copia = json.loads(json.dumps(plugin._entry_to_plan_dict(entrada)))
        restaurada = plugin._entry_from_plan_dict(copia)
        assert restaurada["remote_file"] == entrada["remote_file"]
        assert isinstance(restaurada["remote_file"].partition, DataPartition)


def test_entry_plan_roundtrip_preserva_datetime():
    entrada = {
        "id": "doc.pdf",
        "url": "/doc/doc.pdf",
        "group": DATASET,
        "dataset": DATASET,
        "type": "doc",
        "datetime": dt.datetime(2021, 5, 6, 7, 8, 9),
        "size": 10,
    }
    copia = json.loads(json.dumps(plugin._entry_to_plan_dict(entrada)))
    restaurada = plugin._entry_from_plan_dict(copia)
    assert restaurada["datetime"] == entrada["datetime"]


def test_sync_from_plan_baixa_apenas_download(tmp_path, ftp_falso, sem_download):
    entradas = plugin.datasus_list_datasets(DATASET)
    # Uma entrada já existe localmente -> vira "skip-up-to-date" no plano.
    existente = get_data_filepath(tmp_path, entradas[0]["remote_file"])
    existente.parent.mkdir(parents=True, exist_ok=True)
    existente.touch()
    itens = [plugin._datasus_check_entry(e, tmp_path) for e in entradas]
    assert {item.action for item in itens} == {"download", "skip-up-to-date"}
    plano = CheckPlan(
        fetcher="datasus-fetcher",
        output_dir=str(tmp_path),
        generated_at="2026-01-01T00:00:00+00:00",
        items=itens,
    )
    plano_json = tmp_path / "plano.json"
    plano_json.write_text(plano.to_json(), encoding="utf-8")

    # Dataset posicional divergente deve ser ignorado (--from-plan manda).
    resultado = runner.invoke(
        plugin.app,
        ["sync", "cnes-dc", "--from-plan", str(plano_json), "-o", str(tmp_path)],
    )
    assert resultado.exit_code == 0, resultado.output
    assert len(sem_download) == 1
    baixadas, destino, _ = sem_download[0]
    assert destino == tmp_path
    assert [e["id"] for e in baixadas] == [
        item.id for item in itens if item.action == "download"
    ]
    assert isinstance(baixadas[0]["remote_file"], RemoteFile)


def test_sync_from_plan_invalido_erro(tmp_path, sem_download):
    ruim = tmp_path / "ruim.json"
    ruim.write_text("{json invalido", encoding="utf-8")
    resultado = runner.invoke(
        plugin.app, ["sync", "--from-plan", str(ruim), "-o", str(tmp_path)]
    )
    assert resultado.exit_code == 1
    assert "Plano inválido" in resultado.output
    assert sem_download == []


def test_check_json_para_sync_from_plan_ponta_a_ponta(
    tmp_path, ftp_falso, sem_download
):
    saida_check = tmp_path / "check-out"
    # Pre-cria um dos arquivos locais: ele deve sair do plano como "skip".
    esperado = get_data_filepath(saida_check, ftp_falso[0])
    esperado.parent.mkdir(parents=True, exist_ok=True)
    esperado.touch()

    resultado = runner.invoke(
        plugin.app, ["check", DATASET, "-o", str(saida_check), "--json"]
    )
    assert resultado.exit_code == 0, resultado.output
    texto = resultado.stdout
    plano_dict = json.loads(texto[texto.index("{") : texto.rindex("}") + 1])
    plano = CheckPlan.from_dict(plano_dict)
    assert len(plano.items) == 2
    acoes = {item.id: item.action for item in plano.items}
    assert acoes[ftp_falso[0].filename] == "skip-up-to-date"
    assert acoes[ftp_falso[1].filename] == "download"

    plano_json = tmp_path / "plano.json"
    plano_json.write_text(json.dumps(plano_dict), encoding="utf-8")
    saida_sync = tmp_path / "sync-out"
    resultado_sync = runner.invoke(
        plugin.app,
        ["sync", "--from-plan", str(plano_json), "-o", str(saida_sync)],
    )
    assert resultado_sync.exit_code == 0, resultado_sync.output
    assert len(sem_download) == 1
    baixadas, destino, _ = sem_download[0]
    assert destino == saida_sync
    assert [e["id"] for e in baixadas] == [ftp_falso[1].filename]
