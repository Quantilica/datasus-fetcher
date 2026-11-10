"""O plugin declara o FetcherInfo do registro de fetchers."""

from datasus_fetcher.plugin import fetcher_app


def test_info_declarado():
    app = fetcher_app
    assert app.info_declared is True
    assert app.info.id == "datasus"
    assert app.info.orgao
