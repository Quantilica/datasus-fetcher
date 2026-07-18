# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [0.7.0] - 2026-07-17

Primeiro release publicado no PyPI desde a migração para `quantilica-core`
(as versões 0.5.0 e 0.6.0 foram apenas internas — dependiam de `quantilica-core`
via `git+https`, o que impedia o upload ao índice).

### Corrigido

- Dependência de `quantilica-core` trocada de `git+https://...` para
  `quantilica-core>=0.3.1` (versão publicada no PyPI), removendo o bloqueador de
  upload ao índice. `typer`/`rich` (usados pelo `plugin.py`) são fornecidos pelo host
  `quantilica-cli`, não declarados pelo fetcher — a CLI standalone (`cli.py`) usa
  `argparse` e não precisa deles.

### Adicionado

- `py.typed` (marcador de pacote tipado) + classifier `Typing :: Typed`
- Metadados PEP 639 de licença (`license = "MIT"` + `license-files`)
- Configuração de `ruff` (`line-length=88`, regras `E/F/I/UP/B`) e `pytest`
- Workflow de publicação no PyPI via Trusted Publishing (OIDC) e workflow de teste
  padronizado com `uv` + `ruff` + `pytest`
