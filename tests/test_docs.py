"""Documentação dos dados conforme a norma (normas/documentacao-dados no site)."""

from pathlib import Path

from quantilica.core import docs

from datasus_fetcher.lake import converter


def test_documentacao_dos_dados() -> None:
    docs.assert_fetcher_docs(
        Path(__file__).parents[1] / "docs", converter.datasets(), converter.source_id
    )
