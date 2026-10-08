"""Tests for datasus_fetcher.cli import guard (host absent)."""

import importlib.abc
import importlib.machinery
import sys

import pytest

import datasus_fetcher.cli as cli_module

PLUGIN_MODULE = "datasus_fetcher.plugin"


@pytest.fixture
def host_bloqueado():
    """Simular host ausente (typer); o import do plugin e feito em main()."""
    salvo_typer = sys.modules.get("typer")
    salvo_plugin = sys.modules.pop(PLUGIN_MODULE, None)
    sys.modules["typer"] = None
    try:
        yield cli_module
    finally:
        sys.modules.pop("typer", None)
        if salvo_typer is not None:
            sys.modules["typer"] = salvo_typer
        sys.modules.pop(PLUGIN_MODULE, None)
        if salvo_plugin is not None:
            sys.modules[PLUGIN_MODULE] = salvo_plugin


def test_main_sem_host_sai_com_codigo_1_e_mensagem(host_bloqueado, capsys):
    with pytest.raises(SystemExit) as excinfo:
        host_bloqueado.main(["sync"])
    assert excinfo.value.code == 1
    saida = capsys.readouterr().err
    assert "quantilica install datasus" in saida
    assert "Detalhe:" in saida


def test_erro_interno_do_plugin_propaga():
    """ImportError de modulo alheio nao e mascarado como host ausente."""
    salvo_plugin = sys.modules.pop(PLUGIN_MODULE, None)

    class _FalhaLoader(importlib.abc.Loader):
        def create_module(self, spec):
            return None

        def exec_module(self, module):
            raise ModuleNotFoundError(
                "No module named 'outro_modulo'", name="outro_modulo"
            )

    class _FalhaFinder(importlib.abc.MetaPathFinder):
        def find_spec(self, fullname, path, target=None):
            if fullname == PLUGIN_MODULE:
                return importlib.machinery.ModuleSpec(fullname, _FalhaLoader())
            return None

    finder = _FalhaFinder()
    sys.meta_path.insert(0, finder)
    try:
        with pytest.raises(ModuleNotFoundError):
            cli_module.main(["sync"])
    finally:
        sys.meta_path.remove(finder)
        sys.modules.pop(PLUGIN_MODULE, None)
        if salvo_plugin is not None:
            sys.modules[PLUGIN_MODULE] = salvo_plugin
