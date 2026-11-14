"""Identidade do fetcher: o FetcherInfo, a distribuição e o repositório concordam.

A regra do registro: id ``<id>``, distribuição e repositório ``<id>-fetcher``.
"""

from __future__ import annotations

import tomllib
from pathlib import Path

import pytest

from datasus_fetcher.plugin import fetcher_app as fetcher

ID = "datasus"
PYPROJECT = Path(__file__).resolve().parents[1] / "pyproject.toml"


@pytest.fixture(scope="module")
def project() -> dict:
    return tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))["project"]


def test_info_declarado() -> None:
    assert fetcher.info_declared is True
    assert fetcher.info.id == ID
    assert fetcher.info.orgao


def test_distribuicao_segue_a_regra(project: dict) -> None:
    assert project["name"] == f"{fetcher.info.id}-fetcher"


def test_repositorio_segue_a_regra(project: dict) -> None:
    repo = project["urls"]["Repository"].rstrip("/")
    assert repo.rsplit("/", 1)[-1] == project["name"]
