"""Código de saída do `sync` com erros de arquivo (0 / 3 parcial / 1 nada baixou)."""

import pytest

pytest.importorskip("typer")

from typer.testing import CliRunner  # noqa: E402

import datasus_fetcher.plugin as plugin  # noqa: E402
from tests.test_sync_from_plan import DATASET, ftp_falso  # noqa: E402,F401

runner = CliRunner()


def _download(monkeypatch, downloaded, total, errors):
    monkeypatch.setattr(
        plugin.fetcher_app,
        "download_datasets",
        lambda entries, output, workers=2, **kw: (downloaded, total, errors),
    )


def test_sync_exit_code_helper():
    assert plugin.sync_exit_code(2, []) == 0
    assert plugin.sync_exit_code(1, [("a", "x")]) == plugin.EXIT_SYNC_PARTIAL == 3
    assert plugin.sync_exit_code(0, [("a", "x")]) == 1


def test_sync_sem_erros_sai_com_zero(tmp_path, ftp_falso, monkeypatch):  # noqa: F811
    _download(monkeypatch, 2, 2, [])
    r = runner.invoke(plugin.app, ["sync", DATASET, "-o", str(tmp_path)])
    assert r.exit_code == 0, r.output
    assert "2/2 arquivo(s) baixado(s)" in r.output


def test_sync_parcial_sai_com_tres(tmp_path, ftp_falso, monkeypatch):  # noqa: F811
    _download(monkeypatch, 1, 2, [("RDAC2002", "boom")])
    r = runner.invoke(plugin.app, ["sync", DATASET, "-o", str(tmp_path)])
    assert r.exit_code == 3, r.output
    assert "1 erro(s)" in r.output
    assert "RDAC2002: boom" in r.output


def test_sync_nada_baixado_sai_com_um(tmp_path, ftp_falso, monkeypatch):  # noqa: F811
    _download(monkeypatch, 0, 2, [("a", "x"), ("b", "y")])
    r = runner.invoke(plugin.app, ["sync", DATASET, "-o", str(tmp_path)])
    assert r.exit_code == 1, r.output
