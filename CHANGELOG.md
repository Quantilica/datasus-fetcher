# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [0.14.0] - 2026-10-20

### Corrigido
- **Leitura corrompida pelo fastdbf.** Os .dbf do DATASUS trazem zerado o
  deslocamento de cada campo no cabeçalho (bytes 12-15 do descritor), e o
  fastdbf lia todos os campos a partir do início do registro: no SIH,
  `DT_INTER=' 1200002'` e `VAL_TOT` de 1,2 trilhão; no SIM, `SEXO` vazio. O
  SIA-PA só saía certo porque o lixo fazia o fastdbf falhar e cair no
  dbfread. O cabeçalho agora é corrigido (soma dos tamanhos a partir do byte
  de deleção) na cópia lida pelo fastdbf; o arquivo de origem não é alterado.
  Um cabeçalho cujos campos não somam o tamanho do registro levanta
  `ValueError`. Com os deslocamentos certos, o fastdbf coincide com o dbfread
  em todas as colunas da fixture e não cai mais no fallback nesses arquivos.
- Checagem de sanidade em cada pedaço lido pelo `fastdbf`: as primeiras
  `DBF_SANITY_ROWS` (50) linhas são comparadas com o `dbfread`; se divergirem,
  o pedaço é relido com o `dbfread` e um aviso (`logging.WARNING`) é
  registrado. Um defeito parecido no futuro não volta a corromper os dados em
  silêncio.
- Parquets e DataFrames gerados com versões anteriores a partir de
  `.dbc`/`.dbf` do DATASUS devem ser regenerados.
- **Conversões estritas em `wrangle_datasus`.** Data `AAAAMMDD`, valor
  monetário em texto ou contagem que não é sentinela e não converte levanta
  `ValueError` com a coluna e exemplos; antes virava nulo sem aviso.
- **Códigos categóricos como texto.** `SEXO`, `RACA_COR`/`RACACOR`, `MORTE`,
  `OBITO`, `PARTO`, `GRAVIDEZ`, `GESTACAO`, `ESTCIV`, `ESC`, `ESCOL` saem de
  `INTEGER_COLUMNS` para `CODE_COLUMNS`: como inteiro, "01" virava 1 e, com o
  cast tolerante, códigos com letra (SEXO "M"/"F" do SINAN) viravam nulo.
  `IDADE` fica no tipo de origem: texto codificado no SIM ("487" = 87 anos),
  número no SIH. `QTDFILVIVO` e `QTDFILMORT` (SIM, SINASC) saem de
  `INTEGER_COLUMNS` e ficam texto: "99" é "ignorado", não 99 filhos, e há
  valores não numéricos na origem ("XX" no SIM 1996 GO, "9." no SIM 2002 SP).
- `parse_filename_metadata` reconhece os nomes gravados pelo próprio fetcher
  (`sih-rd_202201-ac@20230206.dbc`, `sim-do-cid10_2022-ac_20231221.dbc`) e
  devolve `dataset`, `ano`, `mes` e `uf`; antes devolvia `{}`, e `uf`/`ano`/`mes`
  não eram injetados na conversão.

### Alterado
- **Incompatível:** campos numéricos do .dbf com casas decimais (`VAL_*` do
  SIH, `PA_VAL*` do SIA) saem como `Decimal(tamanho, decimais)` exatos, em vez
  de `Float64`; a conversão passa pelo texto mais curto do float, que é o
  valor escrito no arquivo.
- As datas do SIM (`DTOBITO`, `DTNASC`...; `DDMMAAAA`) continuam texto, agora
  documentado: de 1996 a 2005 centenas de valores por ano são parciais (só o
  ano ou mês e ano) e alguns não são datas.


### Adicionado
- `tests/test_dbf_displacement.py` e `tests/fixtures/dbf/*_head.dbf`: os 25
  primeiros registros de arquivos reais (SIM, SINASC, SIH-RD e SINAN) com o
  cabeçalho original, comparados com o `dbfread` com e sem leitura em pedaços.
  Esses testes falham com o leitor anterior.

## [0.13.0] - 2026-10-20

### Adicionado
- Listagem `metadata-first` no plugin via snapshot JSON do `datasus-metadata` com fallback automático ao `LIST` FTP quando indisponível ou expirado (`DATASUS_METADATA_DIR` e `DATASUS_METADATA_MAX_AGE_HOURS`).
- Injeção de metadados canônicos de proveniência (`quantilica.*`) no esquema Parquet em `write_parquet`.
- Documentação canônica completa dos 113 datasets do DATASUS e índice geral.

### Alterado
- Dependências atualizadas: `quantilica-core>=0.12.0` e `quantilica-analytics>=0.4.0`.

### Corrigido
- Testes unitários do snapshot desacoplados do `typer` para execução em ambientes mínimos sem extra `cli`.
- Normalização de caminhos de arquivos para suporte multiplataforma (Windows/POSIX).

## [0.12.1] - 2026-10-14

### Alterado
- A extensão Rust (`_datasus_dbc`) passa a ser compilada como `abi3-py312`: um único wheel por plataforma serve do Python 3.12 em diante, em vez de um wheel por versão do Python. Saída conferida byte a byte contra a extensão anterior (`DOAC1996.dbc`, 662.109 bytes, mesmo `sha256`) em Python 3.12 e 3.13.
- `publish.yml` deixa de rodar `uv build` num só runner e passa a chamar o workflow reutilizável `wheels.yml`: wheels `manylinux2014` para Linux x86_64 e aarch64, macOS x86_64 e arm64 e Windows x64, mais o sdist. O Release só é criado, e o `quantilica-index` só é avisado, depois de todos os jobs passarem. Antes, o único wheel era `cp312-cp312-linux_x86_64` (sem tag `manylinux`), e qualquer outra combinação compilava o sdist.
- `pyproject.toml`: o classificador `Operating System :: OS Independent` dá lugar a Linux, macOS e Windows; acrescentado `Implementation :: CPython` (o `abi3` é só CPython).
- `Cargo.toml`: versão alinhada à do `pyproject.toml` (estava em 0.11.0).

### Adicionado
- `.github/workflows/wheels.yml`: constrói os wheels e o sdist, e instala o wheel recém-compilado num ambiente limpo (Python 3.12 e 3.13, Linux x86_64, macOS arm64 e Windows x64) para descomprimir uma fixture e conferir o `sha256`. Também roda por `workflow_dispatch` e em PRs que tocam a extensão, sem publicar.
- `tests/smoke_extension.py`: a verificação acima, fora da coleta do pytest.

### Corrigido
- `README.md` ainda citava o extra `analytics`, removido na 0.12.0; o nome correto é `analysis`.

## [0.12.0] - 2026-10-14

### Alterado
- `README.md`: a seção de instalação deixa de mandar `pip install` (fetchers do Fluxo B não estão no PyPI) e passa a mostrar `quantilica install datasus` (com `--extra analysis`) e `uv add --index` para uso como biblioteca.
- Helpers de resolução de sistemas/datasets (`_systems_to_datasets`, `resolve_dataset_targets`, `parse_systems`, `resolve_targets`) movidos de `cli.py` para o módulo novo `datasus_fetcher.targets`; `plugin.py` e `cli.py` importam de lá (`cli.py` mantém re-exports para compatibilidade; `plugin.py` não importa mais `cli.py`).
- `cli.py` padronizado no bloco top-level dos demais fetchers (importe de `app` com guarda de host, `--version`, delegação via `app(argv)`, `KeyboardInterrupt` → exit 130 e `SystemExit` preservados).
- `.gitignore`: removida a entrada `logging.ini` (arquivo versionado e documentado no README como template de customização de logging).
- Consolidação de `cli.py` em thin wrapper canônico delegando para o plugin Typer/Rich (redução de 691 para 70 LOC), eliminando código duplicado de parsing de sistemas/datasets.
- Remoção do extra opcional duplicado `analytics` (idêntico a `analysis`); a referência canônica passa a ser `datasus-fetcher[analysis]` (README, mensagens de erro e testes atualizados).

### Corrigido
- `read_dbf` e `read_dbc` usavam memória desproporcional em arquivos grandes: um `.dbc` de 166 MB do SIA-PA (4,7 milhões de linhas, 62 colunas) chegou a 18,8 GB de RAM. Havia duas causas. (1) O `fastdbf` monta a tabela Arrow inteira de uma vez e fica em cerca de 12 vezes o tamanho do `.dbf` (529 MiB de `.dbf` levaram 6,4 GB). (2) Arquivos SIA têm campos numéricos com lixo (`invalid numeric payload: "2165198310000EP3170"`) que o `fastdbf` recusa, e o fallback do `dbfread` lia o arquivo inteiro em listas Python. Agora o `.dbf` acima de 64 MiB é lido em pedaços de 32 MiB (`DBF_CHUNK_BYTES`, parâmetro `chunk_bytes`), o fallback para o `dbfread` vale só para o pedaço que falha, e `read_dbc`/`convert_file` tipam cada pedaço (`transform=`) antes de juntá-los. Medido: SINASC de 69 MB, de 6.442 para 1.503 MiB de pico; SIA-PA de 166 MB, de 18,8 GB para 4,7 GB. O DataFrame é idêntico (mesmo hash de linhas). O `dbfread` passa a devolver nomes em maiúsculas e a coluna `_deleted`, como o `fastdbf`, para que pedaços de backends diferentes se juntem.
- `plugin.py`: a dica de instalação do extra `analysis` mandava `pip install datasus-fetcher[analysis]`, que não funciona para fetchers do Fluxo B (fora do PyPI), e o Rich ainda engolia o `[analysis]` por tratá-lo como marcação, deixando só `pip install datasus-fetcher`. Agora a mensagem é `quantilica install datasus --extra analysis`. No guard de `reader.py`, que atende quem importa o pacote, a mensagem é `uv add 'datasus-fetcher[analysis]' --index https://index.quantilica.com/simple/`.
- `sync` e `list` com dataset inexistente (por exemplo `sim`, que é um sistema, não um dataset) imprimiam "não reconhecido" e terminavam com código 0, o que em scripts e crons parecia sucesso. Agora validam os IDs antes de conectar ao FTP e falham com erro de uso (código 2), indicando `quantilica datasus list` e `--system` para sistemas inteiros.
- Comando `sync` custom passa a aceitar `--from-plan` (paridade com o `sync` do SDK: lê o plano JSON gerado por `check --json` via `CheckPlan.from_json` e baixa somente as entradas com ação `download`, ignorando a seleção de datasets/sistemas).
- Veredito `check --json` agora funciona de ponta a ponta com o FTP do DATASUS: probe `check_entry` próprio (heurística local honesta `local-exists`/`not-present`, pois `FtpClient` não implementa HTTP `HEAD`) e entradas do plano serializadas para JSON (`RemoteFile`/`DataPartition`/`datetime` reidratados no `sync --from-plan`).
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
