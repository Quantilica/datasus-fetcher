# datasus-fetcher: Download de microdados do DATASUS

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square) ![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=flat-square)

**datasus-fetcher** é um pacote Python e ferramenta de linha de comando de alta performance para baixar em massa microdados do [DATASUS](https://datasus.saude.gov.br) (`ftp.datasus.gov.br`), descompactar arquivos `.dbc` nativamente em Rust e converter microdados para formato colunar Parquet otimizado para análise.

Para a documentação completa, consulte **[https://docs.quantilica.com](https://docs.quantilica.com)**.

## Por que usar datasus-fetcher?

- **Descompactação nativa em Rust** — rotinas de alta performance compiladas in-tree com Maturin e PyO3 (`_datasus_dbc`), liberando a GIL e sem dependência de runtime externo
- **Tratamento e conversão para Parquet** — extra opcional `analytics` (`polars`, `pyarrow`, `fastdbf`) com saneamento de sentinelas nulos (`\N`, `999999`, etc.), preservação de zeros à esquerda em códigos (município, CID-10, CBO, CNES, procedimento) e parsing de datas
- **113 datasets** cobrindo todos os principais sistemas de informação de saúde do Brasil
- **320+ GB** de microdados históricos, com séries que remontam a 1979
- **Downloads multi-thread** — conexões paralelas configuráveis para maior velocidade
- **Filtros precisos** — recorte por intervalo de datas e/ou UF antes de baixar
- **Verificação de integridade** — pula arquivos já baixados comparando tamanhos
- **Retentativas automáticas** — até 3 tentativas em erros de FTP
- **Versionamento de arquivos** — armazena cada versão baixada com nome datado; arquiva versões antigas automaticamente
- **Documentação e tabelas auxiliares** — baixe dicionários de dados e tabelas de referência junto com os microdados

## Instalação

Pela CLI unificada (recomendado):

```bash
quantilica install datasus
# com o extra de análise (comandos convert e pipeline):
quantilica install datasus --extra analysis
```

Como biblioteca num projeto, a partir do índice próprio (este pacote não é publicado no PyPI):

```bash
uv add datasus-fetcher --index https://index.quantilica.com/simple/
# com o extra de análise:
uv add 'datasus-fetcher[analysis]' --index https://index.quantilica.com/simple/
```

A extensão Rust vem pronta nos wheels do índice, sem compilar: Linux (x86_64 e aarch64, `manylinux2014`), macOS (Intel e Apple Silicon) e Windows x64, para Python 3.12 ou superior (wheel `cp312-abi3`). Em outra combinação (Alpine/musl, Python com free-threading) o instalador usa o código-fonte, que exige a toolchain Rust e o `maturin`.

O download e a descompactação nativa DBC → DBF não exigem dependências analíticas. O extra `analysis` traz Polars, `fastdbf` e `dbfread` para a leitura direta, a limpeza e a conversão para Parquet.

## Uso Rápido

Baixar SIH-RD (Internações Hospitalares) para São Paulo, Rio de Janeiro e Minas Gerais, de 2020 a 2023:

```sh
datasus-fetcher sync sih-rd -o /caminho/para/dados \
    --start 2020-01 \
    --end 2023-12 \
    --regions sp rj mg
```

Baixar todos os datasets (atenção: 320+ GB no total):

```sh
datasus-fetcher sync -o /caminho/para/dados
```

## CLI

O `datasus-fetcher` expõe seis subcomandos:

```
datasus-fetcher <subcommand> [options]

Subcommands:
  sync        Baixa arquivos de microdados (e opcionalmente converte para Parquet)
  list        Inspeciona datasets disponíveis no FTP
  archive     Move versões antigas para um diretório de arquivo
  decompress  Descompacta arquivo .dbc em .dbf nativamente em Rust
  convert     Converte arquivo ou diretório .dbc/.dbf para Parquet tratado
  pipeline    Executa download, descompactação e conversão em lote
```

---

### `sync` — Baixar microdados

```sh
datasus-fetcher sync [DATASETS...] -o <DIR> [OPTIONS]
```

| Argumento | Descrição |
|---|---|
| `DATASETS` | Um ou mais códigos de dataset (ex: `sih-rd cnes-st`). Omita para baixar todos. |
| `-o, --output DIR` | Diretório local onde os arquivos serão armazenados (padrão: `/data/datasus`). |
| `--start PERIOD` | Início do filtro de datas. Formato: `YYYY` ou `YYYY-MM`. |
| `--end PERIOD` | Fim do filtro de datas. Formato: `YYYY` ou `YYYY-MM`. |
| `--regions UF ...` | Um ou mais códigos de UF em minúsculas (ex: `sp rj mg ba`). |
| `-t, --threads N` | Número de threads de download paralelas (padrão: `2`). |
| `--docs` | Também baixa a documentação oficial dos datasets. |
| `--aux` | Também baixa as tabelas de referência auxiliares. |
| `--dry-run` | Lista os arquivos que seriam baixados (com tamanhos e totais) sem baixar. |
| `--convert` | Converte os arquivos baixados automaticamente para Parquet tratado (requer `analytics`). |
| `--parquet-dir DIR` | Diretório de destino para os arquivos Parquet (usado com `--convert`). |

**Exemplos:**

```sh
# Notificações de Dengue (SINAN) — todos os anos, todos os estados
datasus-fetcher sync -o ./data sinan-deng

# Estabelecimentos CNES para o Nordeste inteiro, a partir de 2015
datasus-fetcher sync -o ./data cnes-st \
    --start 2015-01 \
    --regions al ba ce ma pb pe pi rn se

# Declarações de óbito SIM (CID-10) de 2000 a 2023
datasus-fetcher sync -o ./data sim-do-cid10 \
    --start 2000 --end 2023

# Accelerar downloads com mais threads paralelas
datasus-fetcher sync -o ./data sih-rd --threads 4

# Múltiplos datasets em uma chamada
datasus-fetcher sync -o ./data \
    sinasc-dn sim-do-cid10 sih-rd \
    --start 2010-01 --end 2023-12

# HIV: adultos, crianças e gestantes — histórico completo
datasus-fetcher sync -o ./data \
    sinan-hiva sinan-hivc sinan-hivg sinan-hive

# Mortalidade materna e infantil — ambas versões CID
datasus-fetcher sync -o ./data \
    sim-domat-cid10 sim-doinf-cid09 sim-doinf-cid10

# CNES completo para São Paulo, anos recentes
datasus-fetcher sync -o ./data \
    cnes-st cnes-pf cnes-lt cnes-eq cnes-ep \
    --start 2020-01 \
    --regions sp

# Tríade da sífilis: adquirida, congênita e em gestante
datasus-fetcher sync -o ./data \
    sinan-sifa sinan-sifc sinan-sifg \
    --start 2010 --end 2023

# AIH Reduzida (SIH-RD) para o Sul — últimos 5 anos
datasus-fetcher sync -o ./data sih-rd \
    --start 2019-01 --end 2023-12 \
    --regions pr rs sc

# Produção ambulatorial (SIA-PA) para um estado — alto volume, usar mais threads
datasus-fetcher sync -o ./data sia-pa \
    --start 2010-01 --end 2023-12 \
    --regions sp \
    --threads 6

# Oncologia: painel + quimioterapia + radioterapia (APACs)
datasus-fetcher sync -o ./data \
    po sia-aq sia-ar \
    --start 2013 --end 2023

# Tuberculose e hanseníase — nacional, histórico completo
datasus-fetcher sync -o ./data \
    sinan-tube sinan-hans

# Arboviroses: Dengue, Zika e Chikungunya — apenas Nordeste
datasus-fetcher sync -o ./data \
    sinan-deng sinan-zika sinan-chik \
    --regions al ba ce ma pb pe pi rn se

# Nascidos vivos e mortalidade infantil lado a lado — todos os estados
datasus-fetcher sync -o ./data \
    sinasc-dn sim-doinf-cid10 \
    --start 2010 --end 2023
```

---

### `list` — Inspecionar datasets disponíveis

Conecta ao FTP do DATASUS e exibe contagem de arquivos, tamanhos e intervalos de datas de cada dataset:

```sh
datasus-fetcher list

# Inspecionar datasets específicos
datasus-fetcher list sih-rd sia-pa cnes-pf
```

Exemplo de saída:

```
-----------Dataset----------|---Nº files---|--Total size--|------Period range------
sih-rd                      | 10673 files  |  22639.1 MB  | from 1992-01 to 2024-12
sia-pa                      | 10193 files  | 163258.4 MB  | from 1994-07 to 2024-12
sinan-deng                  |    26 files  |   1229.0 MB  | from 2000    to 2025
```

---

### Documentação e tabelas auxiliares

A documentação oficial (dicionários de dados, manuais) e as tabelas de
referência (CID, municípios, procedimentos, CBO, etc.) são baixadas pelo
próprio `sync` através das flags `--docs` e `--aux`:

```sh
# Microdados + documentação + tabelas auxiliares
datasus-fetcher sync -o ./data sim-do-cid10 --docs --aux

# Apenas microdados, sem extras
datasus-fetcher sync -o ./data sim-do-cid10
```

---

### `archive` — Arquivar versões antigas

O DATASUS atualiza seus arquivos periodicamente. O datasus-fetcher armazena cada versão com nome datado. Use `archive` para mover versões não mais recentes para um diretório separado:

```sh
datasus-fetcher archive \
    -o ./data \
    --archive-data-dir ./data-archive
```

---

### `decompress` — Descompactar DBC nativamente (Rust)

Descompacta um arquivo `.dbc` para `.dbf` utilizando o motor de descompressão in-tree compilado em Rust, com zero dependências externas em Python:

```sh
datasus-fetcher decompress entrada.dbc saida.dbf
```

---

### `convert` — Converter para Parquet tratado

Converte arquivos `.dbc` ou `.dbf` diretamente em Parquet colunar de alta compressão (ZSTD), higienizando sentinelas nulos, preservando zeros à esquerda em identificadores e tipando datas. Requer a instalação com o extra `analysis`:

```sh
# Converter um único arquivo DBC para Parquet
datasus-fetcher convert entrada.dbc saida.parquet

# Converter todos os arquivos DBC de um diretório em paralelo
datasus-fetcher convert --dir ./dados/dbc --parquet-dir ./dados/parquet --threads 4
```

| Argumento | Descrição |
|---|---|
| `input_path` | Caminho do arquivo de entrada `.dbc` ou `.dbf`. |
| `output_path` | Caminho do arquivo de saída `.parquet`. |
| `--dir DIR` | Diretório de entrada contendo arquivos `.dbc` a converter em lote. |
| `--parquet-dir DIR` | Diretório de destino para os arquivos `.parquet`. |
| `-t, --threads N` | Quantidade de threads de conversão paralela (padrão: `4`). |

---

### `pipeline` — Pipeline integrado de ponta a ponta

Executa o fluxo completo: sincroniza os arquivos brutos via FTP, descompacta em Rust e converte para Parquet tratado em uma única execução:

```sh
datasus-fetcher pipeline sih-rd \
    -o ./data/raw \
    --parquet-dir ./data/parquet \
    --start 2023-01 \
    --end 2023-12 \
    --regions sp rj
```

---

## Estrutura de Armazenamento

Os arquivos baixados são organizados em uma árvore de diretórios estruturada:

```
data/
└── sih-rd/
    ├── 199201/                              ← partição YYYYMM
    │   └── sih-rd_sp_199201_20250218.dbc   ← dataset_uf_periodo_datadownload.dbc
    ├── 202001/
    │   ├── sih-rd_sp_202001_20250218.dbc
    │   └── sih-rd_rj_202001_20250218.dbc
    └── 202312/
        └── sih-rd_mg_202312_20250218.dbc
```

Para datasets anuais (ex: SIM, SINASC):

```
data/
└── sim-do-cid10/
    └── 2023/
        ├── sim-do-cid10_sp_2023_20250218.dbc
        └── sim-do-cid10_rj_2023_20250218.dbc
```

Cada nome de arquivo codifica: **dataset** + **UF** + **período** + **data do download**.

## Logging

O datasus-fetcher registra o progresso dos downloads no console por padrão. Para personalizar, coloque um arquivo `logging.ini` no diretório de trabalho:

```ini
[loggers]
keys=root,datasus_fetcher

[handlers]
keys=console,file

[formatters]
keys=default

[logger_root]
level=WARNING
handlers=console

[logger_datasus_fetcher]
level=INFO
handlers=console,file
qualname=datasus_fetcher
propagate=0

[handler_console]
class=StreamHandler
level=INFO
formatter=default
args=(sys.stdout,)

[handler_file]
class=FileHandler
level=INFO
formatter=default
args=('datasus-fetcher.log', 'a')

[formatter_default]
format=%(asctime)s %(levelname)s %(message)s
```

## Códigos de UF

Use códigos de duas letras em minúsculas com `--regions`. Use `br` para arquivos de abrangência nacional, quando disponíveis.

| Código | Estado | Código | Estado |
|--------|--------|--------|--------|
| `ac` | Acre | `pb` | Paraíba |
| `al` | Alagoas | `pe` | Pernambuco |
| `am` | Amazonas | `pi` | Piauí |
| `ap` | Amapá | `pr` | Paraná |
| `ba` | Bahia | `rj` | Rio de Janeiro |
| `ce` | Ceará | `rn` | Rio Grande do Norte |
| `df` | Distrito Federal | `ro` | Rondônia |
| `es` | Espírito Santo | `rr` | Roraima |
| `go` | Goiás | `rs` | Rio Grande do Sul |
| `ma` | Maranhão | `sc` | Santa Catarina |
| `mg` | Minas Gerais | `se` | Sergipe |
| `ms` | Mato Grosso do Sul | `sp` | São Paulo |
| `mt` | Mato Grosso | `to` | Tocantins |
| `pa` | Pará | `br` | Brasil (arquivos nacionais) |

## Datasets Disponíveis

Para a documentação detalhada de cada dataset — ficha técnica, contexto institucional, variáveis, regras de saneamento e exemplos de uso — consulte o **[índice geral da documentação dos 113 datasets](docs/datasets/README.md)**. Todos os códigos abaixo são links diretos para a respectiva página individual em `docs/datasets/`.

Estatísticas geradas em **18 de fevereiro de 2025**.

| Dataset | Nº arquivos | Tamanho total | Período |
| --- | ---: | ---: | --- |
| [`base-populacional-ibge-pop`](docs/datasets/base-populacional-ibge-pop.md) | 33 | 150,4 MB | de 1980 a 2012 |
| [`base-populacional-ibge-pops`](docs/datasets/base-populacional-ibge-pops.md) | 25 | 81,3 MB | de 2000 a 2024 |
| [`base-populacional-ibge-popt`](docs/datasets/base-populacional-ibge-popt.md) | 32 | 2,4 MB | de 1992 a 2024 |
| [`base-territorial`](docs/datasets/base-territorial.md) | 14 | 20,9 MB | — |
| [`base-territorial-conversao`](docs/datasets/base-territorial-conversao.md) | 28 | 35,7 MB | — |
| [`base-territorial-mapas`](docs/datasets/base-territorial-mapas.md) | 83 | 122,2 MB | de 1991 a 2013 |
| [`cih-cr`](docs/datasets/cih-cr.md) | 868 | 157,5 MB | de 2008-01 a 2011-04 |
| [`ciha`](docs/datasets/ciha.md) | 4201 | 4354,5 MB | de 2011-01 a 2024-09 |
| [`cnes-dc`](docs/datasets/cnes-dc.md) | 6318 | 115,4 MB | de 2005-08 a 2025-01 |
| [`cnes-ee`](docs/datasets/cnes-ee.md) | 3201 | 4,3 MB | de 2007-03 a 2021-07 |
| [`cnes-ef`](docs/datasets/cnes-ef.md) | 5374 | 10,0 MB | de 2007-03 a 2025-01 |
| [`cnes-ep`](docs/datasets/cnes-ep.md) | 5778 | 498,8 MB | de 2007-04 a 2025-01 |
| [`cnes-eq`](docs/datasets/cnes-eq.md) | 6317 | 1329,2 MB | de 2005-08 a 2025-01 |
| [`cnes-gm`](docs/datasets/cnes-gm.md) | 5459 | 11,9 MB | de 2007-03 a 2025-01 |
| [`cnes-hb`](docs/datasets/cnes-hb.md) | 5805 | 122,2 MB | de 2007-03 a 2025-01 |
| [`cnes-in`](docs/datasets/cnes-in.md) | 5520 | 36,4 MB | de 2007-10 a 2025-01 |
| [`cnes-lt`](docs/datasets/cnes-lt.md) | 6264 | 131,3 MB | de 2005-10 a 2025-01 |
| [`cnes-pf`](docs/datasets/cnes-pf.md) | 6318 | 38238,1 MB | de 2005-08 a 2025-01 |
| [`cnes-rc`](docs/datasets/cnes-rc.md) | 5744 | 67,2 MB | de 2007-03 a 2025-01 |
| [`cnes-sr`](docs/datasets/cnes-sr.md) | 6316 | 1389,8 MB | de 2005-08 a 2025-01 |
| [`cnes-st`](docs/datasets/cnes-st.md) | 6310 | 2805,5 MB | de 2005-08 a 2025-01 |
| [`pce`](docs/datasets/pce.md) | 409 | 14,1 MB | de 1995 a 2021 |
| [`po`](docs/datasets/po.md) | 12 | 129,5 MB | de 2013 a 2024 |
| [`resp`](docs/datasets/resp.md) | 280 | 3,4 MB | de 2015 a 2024 |
| [`sia-ab`](docs/datasets/sia-ab.md) | 544 | 13,9 MB | de 2008-01 a 2017-04 |
| [`sia-abo`](docs/datasets/sia-abo.md) | 1352 | 32,2 MB | de 2014-01 a 2024-12 |
| [`sia-acf`](docs/datasets/sia-acf.md) | 3263 | 26,7 MB | de 2014-08 a 2024-12 |
| [`sia-ad`](docs/datasets/sia-ad.md) | 5506 | 2683,1 MB | de 2008-01 a 2024-12 |
| [`sia-am`](docs/datasets/sia-am.md) | 5447 | 14762,8 MB | de 2008-01 a 2024-12 |
| [`sia-an`](docs/datasets/sia-an.md) | 2145 | 437,6 MB | de 2008-01 a 2014-10 |
| [`sia-aq`](docs/datasets/sia-aq.md) | 5466 | 4202,1 MB | de 2008-01 a 2024-12 |
| [`sia-ar`](docs/datasets/sia-ar.md) | 4982 | 318,9 MB | de 2008-01 a 2024-12 |
| [`sia-atd`](docs/datasets/sia-atd.md) | 3371 | 855,0 MB | de 2014-08 a 2024-12 |
| [`sia-pa`](docs/datasets/sia-pa.md) | 10193 | 163258,4 MB | de 1994-07 a 2024-12 |
| [`sia-ps`](docs/datasets/sia-ps.md) | 3881 | 2543,1 MB | de 2012-11 a 2024-12 |
| [`sia-sad`](docs/datasets/sia-sad.md) | 1088 | 51,0 MB | de 2012-04 a 2018-10 |
| [`sih-er`](docs/datasets/sih-er.md) | 4419 | 270,4 MB | de 2011-01 a 2024-12 |
| [`sih-rd`](docs/datasets/sih-rd.md) | 10673 | 22639,1 MB | de 1992-01 a 2024-12 |
| [`sih-rj`](docs/datasets/sih-rj.md) | 5348 | 815,8 MB | de 2008-01 a 2024-12 |
| [`sih-sp`](docs/datasets/sih-sp.md) | 8928 | 48377,4 MB | de 1997-06 a 2024-12 |
| [`sim-do-cid09`](docs/datasets/sim-do-cid09.md) | 466 | 722,2 MB | de 1979 a 1995 |
| [`sim-do-cid10`](docs/datasets/sim-do-cid10.md) | 784 | 4307,5 MB | de 1996 a 2023 |
| [`sim-doext-cid09`](docs/datasets/sim-doext-cid09.md) | 17 | 42,0 MB | de 1979 a 1995 |
| [`sim-doext-cid10`](docs/datasets/sim-doext-cid10.md) | 28 | 260,2 MB | de 1996 a 2023 |
| [`sim-dofet-cid09`](docs/datasets/sim-dofet-cid09.md) | 17 | 23,0 MB | de 1979 a 1995 |
| [`sim-dofet-cid10`](docs/datasets/sim-dofet-cid10.md) | 28 | 60,9 MB | de 1996 a 2023 |
| [`sim-doinf-cid09`](docs/datasets/sim-doinf-cid09.md) | 17 | 58,0 MB | de 1979 a 1995 |
| [`sim-doinf-cid10`](docs/datasets/sim-doinf-cid10.md) | 28 | 92,0 MB | de 1996 a 2023 |
| [`sim-domat-cid10`](docs/datasets/sim-domat-cid10.md) | 28 | 4,1 MB | de 1996 a 2023 |
| [`sim-dorext-cid10`](docs/datasets/sim-dorext-cid10.md) | 11 | 0,4 MB | de 2013 a 2023 |
| [`sinan-acbi`](docs/datasets/sinan-acbi.md) | 19 | 44,2 MB | de 2006 a 2024 |
| [`sinan-acgr`](docs/datasets/sinan-acgr.md) | 19 | 112,4 MB | de 2006 a 2024 |
| [`sinan-aida`](docs/datasets/sinan-aida.md) | 17 | 17,1 MB | de 2007 a 2023 |
| [`sinan-aidc`](docs/datasets/sinan-aidc.md) | 17 | 0,3 MB | de 2007 a 2023 |
| [`sinan-anim`](docs/datasets/sinan-anim.md) | 17 | 127,5 MB | de 2007 a 2023 |
| [`sinan-antr`](docs/datasets/sinan-antr.md) | 19 | 432,7 MB | de 2006 a 2024 |
| [`sinan-botu`](docs/datasets/sinan-botu.md) | 18 | 0,1 MB | de 2007 a 2024 |
| [`sinan-canc`](docs/datasets/sinan-canc.md) | 18 | 0,3 MB | de 2007 a 2024 |
| [`sinan-chag`](docs/datasets/sinan-chag.md) | 24 | 4,0 MB | de 2000 a 2023 |
| [`sinan-chik`](docs/datasets/sinan-chik.md) | 11 | 70,7 MB | de 2015 a 2025 |
| [`sinan-cole`](docs/datasets/sinan-cole.md) | 18 | 0,0 MB | de 2007 a 2024 |
| [`sinan-coqu`](docs/datasets/sinan-coqu.md) | 19 | 9,1 MB | de 2007 a 2025 |
| [`sinan-deng`](docs/datasets/sinan-deng.md) | 26 | 1229,0 MB | de 2000 a 2025 |
| [`sinan-derm`](docs/datasets/sinan-derm.md) | 19 | 0,5 MB | de 2006 a 2024 |
| [`sinan-dift`](docs/datasets/sinan-dift.md) | 16 | 0,1 MB | de 2007 a 2022 |
| [`sinan-espo`](docs/datasets/sinan-espo.md) | 10 | 0,4 MB | de 2013 a 2022 |
| [`sinan-esqu`](docs/datasets/sinan-esqu.md) | 17 | 7,6 MB | de 2007 a 2023 |
| [`sinan-exan`](docs/datasets/sinan-exan.md) | 18 | 14,0 MB | de 2007 a 2024 |
| [`sinan-fmac`](docs/datasets/sinan-fmac.md) | 17 | 3,9 MB | de 2007 a 2023 |
| [`sinan-ftif`](docs/datasets/sinan-ftif.md) | 18 | 0,8 MB | de 2007 a 2024 |
| [`sinan-hans`](docs/datasets/sinan-hans.md) | 24 | 53,6 MB | de 2001 a 2024 |
| [`sinan-hant`](docs/datasets/sinan-hant.md) | 25 | 2,1 MB | de 1999 a 2023 |
| [`sinan-hepa`](docs/datasets/sinan-hepa.md) | 17 | 28,1 MB | de 2007 a 2023 |
| [`sinan-hiva`](docs/datasets/sinan-hiva.md) | 17 | 15,3 MB | de 2007 a 2023 |
| [`sinan-hivc`](docs/datasets/sinan-hivc.md) | 17 | 0,1 MB | de 2007 a 2023 |
| [`sinan-hive`](docs/datasets/sinan-hive.md) | 9 | 1,0 MB | de 2015 a 2023 |
| [`sinan-hivg`](docs/datasets/sinan-hivg.md) | 17 | 3,4 MB | de 2007 a 2023 |
| [`sinan-iexo`](docs/datasets/sinan-iexo.md) | 19 | 150,3 MB | de 2006 a 2024 |
| [`sinan-leiv`](docs/datasets/sinan-leiv.md) | 25 | 12,1 MB | de 2000 a 2024 |
| [`sinan-lept`](docs/datasets/sinan-lept.md) | 18 | 21,5 MB | de 2007 a 2024 |
| [`sinan-lerd`](docs/datasets/sinan-lerd.md) | 19 | 6,5 MB | de 2006 a 2024 |
| [`sinan-ltan`](docs/datasets/sinan-ltan.md) | 25 | 36,2 MB | de 2000 a 2024 |
| [`sinan-mala`](docs/datasets/sinan-mala.md) | 20 | 2,5 MB | de 2004 a 2023 |
| [`sinan-meni`](docs/datasets/sinan-meni.md) | 18 | 40,9 MB | de 2007 a 2024 |
| [`sinan-ment`](docs/datasets/sinan-ment.md) | 19 | 1,2 MB | de 2006 a 2024 |
| [`sinan-ntra`](docs/datasets/sinan-ntra.md) | 13 | 0,6 MB | de 2010 a 2022 |
| [`sinan-pair`](docs/datasets/sinan-pair.md) | 19 | 0,5 MB | de 2006 a 2024 |
| [`sinan-pest`](docs/datasets/sinan-pest.md) | 14 | 0,0 MB | de 2007 a 2020 |
| [`sinan-pfan`](docs/datasets/sinan-pfan.md) | 10 | 0,5 MB | de 2012 a 2021 |
| [`sinan-pneu`](docs/datasets/sinan-pneu.md) | 19 | 0,3 MB | de 2006 a 2024 |
| [`sinan-raiv`](docs/datasets/sinan-raiv.md) | 15 | 0,1 MB | de 2007 a 2021 |
| [`sinan-rota`](docs/datasets/sinan-rota.md) | 16 | 1,2 MB | de 2009 a 2024 |
| [`sinan-sdta`](docs/datasets/sinan-sdta.md) | 14 | 0,8 MB | de 2007 a 2021 |
| [`sinan-sifa`](docs/datasets/sinan-sifa.md) | 15 | 28,3 MB | de 2010 a 2024 |
| [`sinan-sifc`](docs/datasets/sinan-sifc.md) | 18 | 13,3 MB | de 2007 a 2024 |
| [`sinan-sifg`](docs/datasets/sinan-sifg.md) | 17 | 16,7 MB | de 2007 a 2023 |
| [`sinan-src`](docs/datasets/sinan-src.md) | 16 | 0,2 MB | de 2007 a 2022 |
| [`sinan-teta`](docs/datasets/sinan-teta.md) | 16 | 0,6 MB | de 2007 a 2022 |
| [`sinan-tetn`](docs/datasets/sinan-tetn.md) | 8 | 0,0 MB | de 2014 a 2021 |
| [`sinan-toxc`](docs/datasets/sinan-toxc.md) | 6 | 0,8 MB | de 2019 a 2024 |
| [`sinan-toxg`](docs/datasets/sinan-toxg.md) | 6 | 2,3 MB | de 2019 a 2024 |
| [`sinan-trac`](docs/datasets/sinan-trac.md) | 14 | 1,6 MB | de 2009 a 2022 |
| [`sinan-tube`](docs/datasets/sinan-tube.md) | 23 | 97,8 MB | de 2001 a 2023 |
| [`sinan-varc`](docs/datasets/sinan-varc.md) | 17 | 33,2 MB | de 2007 a 2023 |
| [`sinan-viol`](docs/datasets/sinan-viol.md) | 15 | 242,4 MB | de 2009 a 2023 |
| [`sinan-zika`](docs/datasets/sinan-zika.md) | 10 | 8,9 MB | de 2016 a 2025 |
| [`sinasc-dn`](docs/datasets/sinasc-dn.md) | 838 | 6114,7 MB | de 1994 a 2023 |
| [`sinasc-dnex`](docs/datasets/sinasc-dnex.md) | 10 | 0,5 MB | de 2014 a 2023 |
| [`siscolo-cc`](docs/datasets/siscolo-cc.md) | 2858 | 2380,9 MB | de 2006-01 a 2015-10 |
| [`siscolo-hc`](docs/datasets/siscolo-hc.md) | 2858 | 38,9 MB | de 2006-01 a 2015-10 |
| [`sismama-cm`](docs/datasets/sismama-cm.md) | 1675 | 4,8 MB | de 2009-01 a 2015-07 |
| [`sismama-hm`](docs/datasets/sismama-hm.md) | 1674 | 5,7 MB | de 2009-01 a 2015-07 |
| [`sisprenatal-pn`](docs/datasets/sisprenatal-pn.md) | 944 | 221,6 MB | de 2012-01 a 2014-12 |

**Total: 320,7 GB em 170.543 arquivos**

### Datasets por sistema

- **Base Populacional - IBGE** — Estimativas populacionais do Censo e TCU
  - [`base-populacional-ibge-pop`](docs/datasets/base-populacional-ibge-pop.md): Censo e Estimativas
  - [`base-populacional-ibge-pops`](docs/datasets/base-populacional-ibge-pops.md): Estimativas por Sexo e Idade
  - [`base-populacional-ibge-popt`](docs/datasets/base-populacional-ibge-popt.md): Estimativas TCU

- **Base Territorial** — Limites geográficos e tabelas de conversão
  - [`base-territorial`](docs/datasets/base-territorial.md): Base Territoriais
  - [`base-territorial-mapas`](docs/datasets/base-territorial-mapas.md): Mapas
  - [`base-territorial-conversao`](docs/datasets/base-territorial-conversao.md): Conversões

- **CIH** — Sistema de Comunicação de Informação Hospitalar
  - [`cih-cr`](docs/datasets/cih-cr.md): Comunicação de Internação Hospitalar

- **CIHA** — Sistema de Comunicação de Informação Hospitalar e Ambulatorial
  - [`ciha`](docs/datasets/ciha.md): Sistema de Comunicação de Informação Hospitalar e Ambulatorial

- **CNES** — Cadastro Nacional de Estabelecimentos de Saúde
  - [`cnes-lt`](docs/datasets/cnes-lt.md): Leitos
  - [`cnes-st`](docs/datasets/cnes-st.md): Estabelecimentos
  - [`cnes-dc`](docs/datasets/cnes-dc.md): Dados Complementares
  - [`cnes-eq`](docs/datasets/cnes-eq.md): Equipamentos
  - [`cnes-sr`](docs/datasets/cnes-sr.md): Serviço Especializado
  - [`cnes-hb`](docs/datasets/cnes-hb.md): Habilitação
  - [`cnes-pf`](docs/datasets/cnes-pf.md): Profissional
  - [`cnes-ep`](docs/datasets/cnes-ep.md): Equipes
  - [`cnes-rc`](docs/datasets/cnes-rc.md): Regra Contratual
  - [`cnes-in`](docs/datasets/cnes-in.md): Incentivos
  - [`cnes-ee`](docs/datasets/cnes-ee.md): Estabelecimento de Ensino
  - [`cnes-ef`](docs/datasets/cnes-ef.md): Estabelecimento Filantrópico
  - [`cnes-gm`](docs/datasets/cnes-gm.md): Gestão e Metas

- **PCE** — Programa de Controle da Esquistossomose
  - [`pce`](docs/datasets/pce.md): Programa de Controle da Esquistossomose

- **PO** — Painel de Oncologia
  - [`po`](docs/datasets/po.md): Painel de Oncologia

- **RESP** — Notificações de casos suspeitos de SCZ
  - [`resp`](docs/datasets/resp.md): Notificações de casos suspeitos de SCZ

- **SIA** — Sistema de Informações Ambulatoriais
  - [`sia-ab`](docs/datasets/sia-ab.md): APAC de Acompanhamento a Cirurgia Bariátrica
  - [`sia-abo`](docs/datasets/sia-abo.md): APAC Acompanhamento Pós Cirurgia Bariátrica
  - [`sia-acf`](docs/datasets/sia-acf.md): APAC Confecção de Fístula Arteriovenosa
  - [`sia-ad`](docs/datasets/sia-ad.md): APAC de Laudos Diversos
  - [`sia-am`](docs/datasets/sia-am.md): APAC de Medicamentos
  - [`sia-an`](docs/datasets/sia-an.md): APAC de Nefrologia
  - [`sia-aq`](docs/datasets/sia-aq.md): APAC de Quimioterapia
  - [`sia-ar`](docs/datasets/sia-ar.md): APAC de Radioterapia
  - [`sia-atd`](docs/datasets/sia-atd.md): APAC de Tratamento Dialítico
  - [`sia-pa`](docs/datasets/sia-pa.md): Produção Ambulatorial
  - [`sia-ps`](docs/datasets/sia-ps.md): Psicossocial
  - [`sia-sad`](docs/datasets/sia-sad.md): Atenção Domiciliar

- **SIH** — Sistema de Informação Hospitalar
  - [`sih-rd`](docs/datasets/sih-rd.md): AIH Reduzida
  - [`sih-rj`](docs/datasets/sih-rj.md): AIH Rejeitadas
  - [`sih-sp`](docs/datasets/sih-sp.md): Serviços Profissionais
  - [`sih-er`](docs/datasets/sih-er.md): AIH Rejeitadas com código de erro

- **SIM** — Sistema de Informação de Mortalidade
  - [`sim-do-cid09`](docs/datasets/sim-do-cid09.md): Declarações de Óbito (CID-9, 1979–1995)
  - [`sim-do-cid10`](docs/datasets/sim-do-cid10.md): Declarações de Óbito (CID-10, 1996–presente)
  - [`sim-doext-cid09`](docs/datasets/sim-doext-cid09.md): Declarações de Óbitos por causas externas (CID-9)
  - [`sim-doext-cid10`](docs/datasets/sim-doext-cid10.md): Declarações de Óbitos por causas externas (CID-10)
  - [`sim-dofet-cid09`](docs/datasets/sim-dofet-cid09.md): Declarações de Óbitos fetais (CID-9)
  - [`sim-dofet-cid10`](docs/datasets/sim-dofet-cid10.md): Declarações de Óbitos fetais (CID-10)
  - [`sim-doinf-cid09`](docs/datasets/sim-doinf-cid09.md): Declarações de Óbitos infantis (CID-9)
  - [`sim-doinf-cid10`](docs/datasets/sim-doinf-cid10.md): Declarações de Óbitos infantis (CID-10)
  - [`sim-domat-cid10`](docs/datasets/sim-domat-cid10.md): Declarações de Óbitos maternos (CID-10)
  - [`sim-dorext-cid10`](docs/datasets/sim-dorext-cid10.md): Mortalidade de residentes no exterior (CID-10)

- **SINAN** — Sistema de agravos de notificação compulsória
  - [`sinan-acbi`](docs/datasets/sinan-acbi.md): Acidente de trabalho com material biológico
  - [`sinan-acgr`](docs/datasets/sinan-acgr.md): Acidente de trabalho
  - [`sinan-aida`](docs/datasets/sinan-aida.md): AIDS em adultos
  - [`sinan-aidc`](docs/datasets/sinan-aidc.md): AIDS em crianças
  - [`sinan-anim`](docs/datasets/sinan-anim.md): Acidente por Animais Peçonhentos
  - [`sinan-antr`](docs/datasets/sinan-antr.md): Atendimento Antirrábico
  - [`sinan-botu`](docs/datasets/sinan-botu.md): Botulismo
  - [`sinan-canc`](docs/datasets/sinan-canc.md): Câncer relacionado ao trabalho
  - [`sinan-chag`](docs/datasets/sinan-chag.md): Doença de Chagas Aguda
  - [`sinan-chik`](docs/datasets/sinan-chik.md): Febre de Chikungunya
  - [`sinan-cole`](docs/datasets/sinan-cole.md): Cólera
  - [`sinan-coqu`](docs/datasets/sinan-coqu.md): Coqueluche
  - [`sinan-deng`](docs/datasets/sinan-deng.md): Dengue
  - [`sinan-derm`](docs/datasets/sinan-derm.md): Dermatoses ocupacionais
  - [`sinan-dift`](docs/datasets/sinan-dift.md): Difteria
  - [`sinan-espo`](docs/datasets/sinan-espo.md): Esporotricose (Epizootia)
  - [`sinan-esqu`](docs/datasets/sinan-esqu.md): Esquistossomose
  - [`sinan-exan`](docs/datasets/sinan-exan.md): Doenças exantemáticas
  - [`sinan-fmac`](docs/datasets/sinan-fmac.md): Febre Maculosa
  - [`sinan-ftif`](docs/datasets/sinan-ftif.md): Febre Tifóide
  - [`sinan-hans`](docs/datasets/sinan-hans.md): Hanseníase
  - [`sinan-hant`](docs/datasets/sinan-hant.md): Hantavirose
  - [`sinan-hepa`](docs/datasets/sinan-hepa.md): Hepatites Virais
  - [`sinan-hiva`](docs/datasets/sinan-hiva.md): HIV em adultos
  - [`sinan-hivc`](docs/datasets/sinan-hivc.md): HIV em crianças
  - [`sinan-hive`](docs/datasets/sinan-hive.md): HIV em crianças expostas
  - [`sinan-hivg`](docs/datasets/sinan-hivg.md): HIV em gestante
  - [`sinan-iexo`](docs/datasets/sinan-iexo.md): Intoxicação Exógena
  - [`sinan-leiv`](docs/datasets/sinan-leiv.md): Leishmaniose Visceral
  - [`sinan-lept`](docs/datasets/sinan-lept.md): Leptospirose
  - [`sinan-lerd`](docs/datasets/sinan-lerd.md): LER/DORT
  - [`sinan-ltan`](docs/datasets/sinan-ltan.md): Leishmaniose Tegumentar Americana
  - [`sinan-mala`](docs/datasets/sinan-mala.md): Malária
  - [`sinan-meni`](docs/datasets/sinan-meni.md): Meningite
  - [`sinan-ment`](docs/datasets/sinan-ment.md): Transtornos mentais relacionados ao trabalho
  - [`sinan-ntra`](docs/datasets/sinan-ntra.md): Notificação de Tracoma
  - [`sinan-pair`](docs/datasets/sinan-pair.md): Perda auditiva por ruído relacionado ao trabalho
  - [`sinan-pest`](docs/datasets/sinan-pest.md): Peste
  - [`sinan-pfan`](docs/datasets/sinan-pfan.md): Paralisia Flácida Aguda
  - [`sinan-pneu`](docs/datasets/sinan-pneu.md): Pneumoconioses relacionadas ao trabalho
  - [`sinan-raiv`](docs/datasets/sinan-raiv.md): Raiva
  - [`sinan-rota`](docs/datasets/sinan-rota.md): Rotavírus
  - [`sinan-sdta`](docs/datasets/sinan-sdta.md): Surto de Doenças Transmitidas por Alimentos
  - [`sinan-sifa`](docs/datasets/sinan-sifa.md): Sífilis Adquirida
  - [`sinan-sifc`](docs/datasets/sinan-sifc.md): Sífilis Congênita
  - [`sinan-sifg`](docs/datasets/sinan-sifg.md): Sífilis em Gestante
  - [`sinan-src`](docs/datasets/sinan-src.md): Síndrome da Rubéola Congênita
  - [`sinan-teta`](docs/datasets/sinan-teta.md): Tétano Acidental
  - [`sinan-tetn`](docs/datasets/sinan-tetn.md): Tétano Neonatal
  - [`sinan-toxc`](docs/datasets/sinan-toxc.md): Toxoplasmose Congênita
  - [`sinan-toxg`](docs/datasets/sinan-toxg.md): Toxoplasmose Gestacional
  - [`sinan-trac`](docs/datasets/sinan-trac.md): Inquérito de Tracoma
  - [`sinan-tube`](docs/datasets/sinan-tube.md): Tuberculose
  - [`sinan-varc`](docs/datasets/sinan-varc.md): Varicela
  - [`sinan-viol`](docs/datasets/sinan-viol.md): Violência doméstica, sexual e/ou outras violências
  - [`sinan-zika`](docs/datasets/sinan-zika.md): Zika Vírus

- **SINASC** — Sistema de Informação de Nascidos Vivos
  - [`sinasc-dn`](docs/datasets/sinasc-dn.md): Declarações de nascidos vivos
  - [`sinasc-dnex`](docs/datasets/sinasc-dnex.md): Declarações de nascidos vivos no exterior

- **SISCOLO** — Sistema de Informações de Cânceres de Colo de Útero
  - [`siscolo-cc`](docs/datasets/siscolo-cc.md): Citopatológico de Colo de Útero
  - [`siscolo-hc`](docs/datasets/siscolo-hc.md): Histopatológico de Colo de Útero

- **SISMAMA** — Sistema de Informações de Cânceres de Mama
  - [`sismama-cm`](docs/datasets/sismama-cm.md): Citopatológico de Mama
  - [`sismama-hm`](docs/datasets/sismama-hm.md): Histopatológico de Mama

- **SISPRENATAL** — Sistema de Monitoramento e Avaliação do Pré-Natal, Parto, Puerpério e Criança
  - [`sisprenatal-pn`](docs/datasets/sisprenatal-pn.md): Pré-Natal

## Fontes de Dados

- Consultas online (TabNet): https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- Transferência de microdados (FTP): https://datasus.saude.gov.br/transferencia-de-arquivos/

## Descompactação e Processamento em Python

O `datasus-fetcher` possui rotinas nativas compiladas em Rust (`_datasus_dbc`) para descompactação direta de arquivos `.dbc`, sem necessidade de bibliotecas C legadas externas.

### 1. Descompactação nativa (Rust)

Disponível diretamente no pacote base, com zero dependências analíticas externas:

```python
import datasus_fetcher as df

# Descompacta DBC para DBF (libera a GIL internamente, seguro para multithreading)
df.decompress_dbc("DOSP2023.dbc", "DOSP2023.dbf")
```

### 2. Leitura e conversão analítica para Parquet

Requer o extra opcional: `quantilica install datasus --extra analysis` (CLI) ou `uv add 'datasus-fetcher[analysis]' --index https://index.quantilica.com/simple/` (biblioteca).

```python
import datasus_fetcher as df

# Lê DBC diretamente para um DataFrame Polars já higienizado:
df_obitos = df.read_dbc("DOSP2023.dbc")

# Ou lê um DBF já descompactado:
df_obitos = df.read_dbf("DOSP2023.dbf")

# Higienização customizada de um DataFrame bruto:
df_limpo = df.wrangle_datasus(df_obitos)

# Gravação atômica em Parquet comprimido com ZSTD:
df.write_parquet(df_limpo, "DOSP2023.parquet")

# Conversão direta de arquivos ou diretórios:
from datasus_fetcher.wrangling import convert_directory, convert_file

convert_file("DOSP2023.dbc", "DOSP2023.parquet")
convert_directory(
    input_dir="./dados/dbc",
    output_dir="./dados/parquet",
    max_workers=4,
)
```

### Regras de Tratamento e Saneamento dos Dados

Ao utilizar o extra `analysis`, o pipeline aplica regras canônicas de qualidade:
- **Sentinelas Nulos:** Converte sequências como `"\N"`, `""`, `"999999"`, `"000000"`, `"NA"` em valores nulos reais (`null`).
- **Preservação de Códigos:** Colunas de códigos estruturados (ex: `CODMUNRES`, `CODMUNNAT`, `CAUSABAS`, `CID10`, `CBO`, `CNES`, procedimentos SUS) são preservadas estritamente como string com preenchimento correto de zeros à esquerda (`zfill`), impedindo truncamento numérico acidental.
- **Tipagem de Datas:** Colunas temporais (`DTOBITO`, `DTNASC`, `DTNOTIF`, etc.) são convertidas para o tipo `Date` nativo do Polars (`pl.Date`), tratando formatos brasileiros `DDMMAAAA`.
- **Registros Deletados:** Filtra marcadores de exclusão lógica nativos do formato dBASE (`_deleted`) e remove a coluna auxiliar.

## Desenvolvimento

```bash
# Sincronizar ambiente de desenvolvimento uv (compila extensão Rust automaticamente)
uv sync --all-packages

# Executar a suíte de testes
uv run --package datasus-fetcher pytest datasus-fetcher/tests/

# Lint e formatação
uv run ruff check datasus-fetcher/
uv run ruff format datasus-fetcher/
```

## Licença

MIT — veja [LICENSE](LICENSE).
