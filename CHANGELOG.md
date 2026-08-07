# Changelog

## [0.9.0] - 2026-08-07
### Alterado
- Refatoração arquitetural: Remoção de dependências (`quantilica-cli` e `quantilica-catalog`) e limpeza de imports. Os fetchers agora são pacotes de extração puros, dependendo estritamente do `quantilica-core`.

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [0.8.2] - 2026-08-07

### Corrigido

- Corrigido o download do dataset `base-territorial`, onde arquivos submetidos no mesmo dia colidiam de nome local e eram rebaixados repetidamente a cada sincronização. A "versão" da partição (nome original) agora é extraída e preservada no nome do arquivo local.

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
