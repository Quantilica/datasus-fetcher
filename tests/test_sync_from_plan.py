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


@pytest.fixture
def sem_download_com_force(monkeypatch):
    """Captura entradas e o flag `force` passado ao download (sem rede)."""
    chamadas: list = []

    def _fake(entries, output, workers=2, *, force=False):
        chamadas.append((list(entries), Path(output), workers, force))
        return (len(entries), len(entries), [])

    monkeypatch.setattr(plugin.fetcher_app, "download_datasets", _fake)
    return chamadas


def _check_plan_com_itens(tmp_path, ftp_falso):
    """Gera o plano do check para ftp_falso e o salva em JSON."""
    saida_check = tmp_path / "check-out"
    entradas = plugin.datasus_list_datasets(DATASET)
    itens = [plugin._datasus_check_entry(e, saida_check) for e in entradas]
    plano = CheckPlan(
        fetcher="datasus-fetcher",
        output_dir=str(saida_check),
        generated_at="2026-01-01T00:00:00+00:00",
        items=itens,
    )
    dd = json.loads(plano.to_json())
    plano_json = tmp_path / "plano.json"
    plano_json.write_text(plano.to_json(), encoding="utf-8")
    return dd, plano_json, itens


def test_check_preenche_remote_last_modified_dados(tmp_path, ftp_falso):
    ftp_falso[0].datetime = dt.datetime(2020, 2, 1, 3, 4, 5)
    ftp_falso[1].datetime = dt.datetime(2021, 7, 8, 9, 10, 11)
    entradas = plugin.datasus_list_datasets(DATASET)
    itens = [plugin._datasus_check_entry(e, tmp_path) for e in entradas]
    obtido = {item.id: item.remote_last_modified for item in itens}
    assert obtido == {
        ftp_falso[0].filename: dt.datetime(2020, 2, 1, 3, 4, 5).isoformat(),
        ftp_falso[1].filename: dt.datetime(2021, 7, 8, 9, 10, 11).isoformat(),
    }


def test_check_preenche_remote_last_modified_documentacao(tmp_path, monkeypatch):
    monkeypatch.setattr(plugin, "_FTP_CONN", _FakeFtp())
    monkeypatch.setattr(plugin, "_get_ftp", lambda: plugin._FTP_CONN)
    doc_dataset = "cnes"

    def _doc(nome, dt_):
        return {
            "filename": nome,
            "full_path": f"/docs/{nome}",
            "datetime": dt_,
            "size": 7,
        }

    monkeypatch.setattr(
        fetcher_module,
        "list_documentation_files",
        lambda ftp, dataset: [_doc("doc.pdf", dt.datetime(2024, 3, 4, 5, 6, 7))],
    )
    monkeypatch.setattr(fetcher_module, "list_dataset_files", lambda ftp, dataset: [])
    monkeypatch.setattr(
        fetcher_module, "list_auxiliary_tables_files", lambda ftp, dataset: []
    )
    entradas = plugin.datasus_list_datasets(doc_dataset)
    itens = [plugin._datasus_check_entry(e, tmp_path) for e in entradas]
    assert itens[0].remote_last_modified == dt.datetime(2024, 3, 4, 5, 6, 7).isoformat()
    assert itens[0].remote_size == 7
    assert (
        itens[0]
        .local_path.replace("\\", "/")
        .endswith("_documentacao/cnes/doc@20240304.pdf")
    )


def test_entry_last_modified_none_sem_data():
    assert plugin._entry_last_modified({"type": "data", "id": "x"}) is None
    assert plugin._entry_last_modified({"type": "doc", "id": "x"}) is None
    assert (
        plugin._entry_last_modified(
            {"type": "data", "id": "x", "remote_file": {"filename": "x.dbc"}}
        )
        is None
    )
    assert (
        plugin._entry_last_modified({"type": "aux", "id": "x", "datetime": None})
        is None
    )
    assert plugin._entry_last_modified(
        {
            "type": "data",
            "remote_file": {"__datetime__": True, "value": "2020-02-01T00:00:00"},
        }
    ) == dt.datetime(2020, 2, 1)


def test_entry_last_modified_aceita_date():
    esperado = dt.datetime(2024, 3, 4)
    assert (
        plugin._entry_last_modified({"type": "doc", "datetime": dt.date(2024, 3, 4)})
        == esperado
    )
    assert (
        plugin._entry_last_modified(
            {"type": "aux", "datetime": {"__date__": True, "value": "2024-03-04"}}
        )
        == esperado
    )
    entrada = {"type": "doc", "id": "d", "datetime": dt.date(2024, 3, 4)}
    assert plugin._entry_last_modified(entrada).isoformat() == "2024-03-04T00:00:00"


def test_check_plano_roundtrip_remote_last_modified(tmp_path, ftp_falso):
    dd, _plano_json, _itens = _check_plan_com_itens(tmp_path, ftp_falso)
    esperado = dt.datetime(2020, 2, 1).isoformat()
    assert all(i["remote_last_modified"] == esperado for i in dd["items"])
    restaurado = CheckPlan.from_dict(dd)
    assert all(i.remote_last_modified == esperado for i in restaurado.items)
    for item in restaurado.items:
        data = plugin._entry_from_plan_dict(dict(item.entry))
        assert data["remote_file"].datetime == dt.datetime(2020, 2, 1)


def test_sync_from_plan_force_true(tmp_path, ftp_falso, sem_download_com_force):
    _dd, plano_json, itens = _check_plan_com_itens(tmp_path, ftp_falso)
    resultado = runner.invoke(
        plugin.app,
        ["sync", "--from-plan", str(plano_json), "-o", str(tmp_path), "--force"],
    )
    assert resultado.exit_code == 0, resultado.output
    baixadas, destino, workers, force = sem_download_com_force[0]
    assert force is True
    assert destino == tmp_path
    assert [e["id"] for e in baixadas] == [
        item.id for item in itens if item.action == "download"
    ]


def test_sync_sem_force_mantem_chamada_original(tmp_path, ftp_falso, monkeypatch):
    chamadas: list = []

    def _fake(*args, **kwargs):
        chamadas.append((args, kwargs))
        return (0, 0, [])

    monkeypatch.setattr(plugin.fetcher_app, "download_datasets", _fake)
    _dd, plano_json, itens = _check_plan_com_itens(tmp_path, ftp_falso)
    resultado = runner.invoke(
        plugin.app,
        ["sync", "--from-plan", str(plano_json), "-o", str(tmp_path), "-t", "3"],
    )
    assert resultado.exit_code == 0, resultado.output
    assert len(chamadas) == 1
    args, kwargs = chamadas[0]
    entradas, destino = args[0], args[1]
    assert [e["id"] for e in entradas] == [item.id for item in itens]
    assert Path(destino) == tmp_path
    assert kwargs == {"workers": 3}
    assert "force" not in kwargs


def test_sync_force_sem_from_plan(tmp_path, ftp_falso, sem_download_com_force):
    resultado = runner.invoke(
        plugin.app, ["sync", DATASET, "-o", str(tmp_path), "--force"]
    )
    assert resultado.exit_code == 0, resultado.output
    baixadas, destino, _workers, force = sem_download_com_force[0]
    assert force is True
    assert destino == tmp_path
    assert len(baixadas) == 2


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
