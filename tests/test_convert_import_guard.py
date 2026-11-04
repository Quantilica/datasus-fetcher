"""Sem o extra ``analysis``, ``convert`` falha com saída limpa (sem traceback)."""

from __future__ import annotations

import sys

import pytest
from typer.testing import CliRunner

import datasus_fetcher
from datasus_fetcher.plugin import app


def _sem_lake(monkeypatch) -> None:
    """Simula o extra ausente: importar o módulo lake levanta ImportError."""
    monkeypatch.delattr(datasus_fetcher, "lake", raising=False)
    monkeypatch.setitem(sys.modules, "datasus_fetcher.lake", None)


def test_convert_sem_extra_analysis_sai_com_codigo_1(tmp_path, monkeypatch):
    """O ImportError do módulo lake vira saída 1 com instrução de instalação."""
    _sem_lake(monkeypatch)

    result = CliRunner().invoke(
        app, ["convert", "-i", str(tmp_path), "-o", str(tmp_path / "lake")]
    )

    assert result.exit_code == 1
    assert isinstance(result.exception, SystemExit), repr(result.exception)
    assert "analysis" in result.output


def test_plugin_traduz_importerror_com_mensagem_acionavel(tmp_path, monkeypatch):
    """A mensagem do ImportError manda instalar o extra, sem ``pip install``."""
    from datasus_fetcher import plugin

    _sem_lake(monkeypatch)

    with pytest.raises(ImportError, match="--extra analysis") as info:
        plugin.convert(tmp_path, tmp_path / "lake")

    assert "pip install" not in str(info.value)
