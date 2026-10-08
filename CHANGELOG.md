# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Não lançado]

### Alterado
- Consolidação de `cli.py` em thin wrapper canônico delegando para o plugin Typer/Rich (redução de 691 para 70 LOC), eliminando código duplicado de parsing de sistemas/datasets.
- Remoção do extra opcional duplicado `analytics` (idêntico a `analysis`); a referência canônica passa a ser `datasus-fetcher[analysis]` (README, mensagens de erro e testes atualizados).

### Corrigido
- Deteção de analytics em `__init__.py`: validação de backend de leitura DBF (`fastdbf` ou `dbfread`) junto ao `polars` para evitar que `_HAS_ANALYTICS` retorne `True` indevidamente quando apenas `polars` estiver no ambiente compartilhado.
- Testes de conversão DBF/Parquet passam a verificar `_HAS_ANALYTICS` e pular graciosamente caso os backends de DBF não estejam instalados.
- Inclusão de `dbfread` e `fastdbf` no grupo `dev` de `pyproject.toml`.

## [0.11.3] - 2026-10-02
### Alterado
- Migração do check incremental (`is_cached_download`) para a política canônica `IncrementalSyncStrategy(policy="strict_manifest")` de `quantilica-core` 0.8.0: a decisão de skip (artefato presente + sidecar `*.manifest.json` válido com `sha256`/`size_bytes` consistentes) agora é delegada inteiramente ao core, mantendo a verificação de tamanho remoto (`is_complete_file`) na borda.
- `is_manifest_valid` passa a ser reexportada de `quantilica.core.sync` (compatibilidade preservada com testes e código existente).
- Dependência atualizada para `quantilica-core>=0.8.0`.

## [0.11.2] - 2026-10-02
### Corrigido
- Padronizado o extra analítico para `[project.optional-dependencies].analysis` conforme normas do ecossistema (`docs/docs/normas/pyproject.md`), mantendo `analytics` como alias retrocompatível.
- Adicionado `--extra analysis` ao passo de instalação do CI (`.github/workflows/test.yml`), garantindo que dependências analíticas (`polars`, `pyarrow`, `fastdbf`, `dbfread`) sejam provisionadas durante a execução dos testes.
- Inclusão da fixture de teste `DOAC1996.dbc` em `tests/fixtures/`, garantindo isolamento total do repositório em CI sem referenciar diretórios externos do workspace.

## [0.11.1] - 2026-10-02
### Corrigido
- Adicionado `pytest.importorskip("typer")` em `tests/test_plugin_systems.py` para permitir que os testes unitários da biblioteca rodem sem falha em ambientes de CI isolados onde `typer` não está instalado.

## [0.11.0] - 2026-10-02
### Adicionado
- Opção `--system` / `-s` (suporte a múltiplos sistemas, lista separada por vírgula, case-insensitive) nos comandos `list`, `sync` e `pipeline` em `plugin.py` e `cli.py`.
- Mapeamento dinâmico de 16 subsistemas de saúde em `meta.py` (`SYSTEM_DATASETS`, `get_system_datasets`, `expand_systems`), incluindo `SIM`, `SINASC`, `SIH`, `CNES`, `SIA` e `SINAN`.
- Modo de sincronização incremental inteligente em `storage.py` e `fetcher.py` (`is_cached_download`): validação prévia de tamanho e manifesto SHA-256 (`.manifest.json`), evitando re-downloads redundantes.
- Abertura diferida de conexão FTP (evita conexão de rede quando todos os arquivos solicitados já estão em cache).
- Extensão nativa in-tree em Rust (`_datasus_dbc`) compilada com Maturin e PyO3 para descompactação direta de arquivos `.dbc` em alta performance sem dependências externas em tempo de execução, liberando a GIL do Python (`py.allow_threads`).
- Função `decompress_dbc(input_path, output_path)` exposta incondicionalmente na raiz do pacote.
- Subcomando CLI `decompress` para descompactação direta de arquivos `.dbc` para `.dbf`.
- Extra opcional `analytics` (`datasus-fetcher[analytics]`) integrando `polars`, `pyarrow`, `fastdbf` e `dbfread`.
- Módulos `reader` e `wrangling` com funções analíticas `read_dbc`, `read_dbf`, `wrangle_datasus`, `write_parquet`, `convert_file` e `convert_directory`.
- Subcomando CLI `convert` para conversão de arquivos individuais ou diretórios completos para Parquet tratado com compressão ZSTD.
- Subcomando CLI `pipeline` e flags `--convert`/`--parquet-dir` integradas ao comando `sync`.
- Regras de higienização de dados: saneamento de sentinelas nulos (`\N`, `999999`, etc.), preservação de zeros à esquerda em códigos estruturados (municípios IBGE, CID-10, CBO, CNES, procedimentos SUS), conversão para tipo de data nativo (`pl.Date`) e descarte automático de registros excluídos no padrão dBASE (`_deleted`).

### Corrigido
- Restauração de `download_data` na API pública e saneamento de sentinelas nulos em fallbacks.
- Normalização de hifens de datas e suporte a filtro de ano para arquivos mensais no `Slicer`.

### Alterado
- Build backend migrado de `hatchling` para `maturin` (`[build-system] requires = ["maturin>=1.5,<2.0"]`).

## [0.10.2] - 2026-08-31
### Corrigido
- Quitação de dívida de lint (E501/docstrings longas) herdada dos sweeps de
  documentação de 2026-08-14; nenhum comportamento alterado.

## [0.10.1] - 2026-08-10
### Corrigido
- Atualizada dependência `quantilica-core` para `>=0.5.0` devido às novas assinaturas requeridas pelo CLI.

## [0.10.0] - 2026-08-10
### Alterado
- Migração completa da CLI para utilização da SDK unificada (`FetcherApp`).
- Remoção do gerenciamento manual de cliente FTP (`ftplib`) em favor do `FtpClient` provido pelo `quantilica-core`.

## [0.9.0] - 2026-08-07
### Alterado
- Refatoração arquitetural: Remoção de dependências (`quantilica-cli` e `quantilica-catalog`) e limpeza de imports. Os fetchers agora são pacotes de extração puros, dependendo estritamente do `quantilica-core`.

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
