# datasus-fetcher

**datasus-fetcher** is a Python package and command-line tool to bulk-download raw microdata files (`.dbc`) from [DATASUS](https://datasus.saude.gov.br)'s public FTP server (`ftp.datasus.gov.br`). It does **not** parse or read files — it is a pure, reliable downloader that gives you organized local copies of Brazil's largest public health database.

## Why datasus-fetcher?

- **113 datasets** across all major Brazilian health information systems
- **320+ GB** of historical microdata, some series going back to 1979
- **Multi-threaded downloads** — configurable parallel connections for faster retrieval
- **Smart filtering** — slice by date range and/or Brazilian state (UF) before downloading
- **File integrity checks** — skips already-downloaded files by comparing sizes
- **Automatic retries** — up to 3 retries on transient FTP errors
- **File versioning** — stores every downloaded version with a date-stamped filename; archive old ones automatically
- **Documentation & auxiliary tables** — download codebooks and reference tables alongside data
- **No external dependencies** — pure Python 3.10+, just `pip install`

## Installation

```sh
pip install datasus-fetcher
```

For isolated global installation (recommended for CLI-only use):

```sh
pipx install datasus-fetcher
```

## Quick start

Download SIH-RD (Hospital Admissions) for São Paulo, Rio de Janeiro, and Minas Gerais from 2020 to 2023:

```sh
datasus-fetcher data --data-dir /path/to/data sih-rd \
    --start 2020-01 \
    --end 2023-12 \
    --regions sp rj mg
```

Download all datasets (warning: 320+ GB total):

```sh
datasus-fetcher data --data-dir /path/to/data
```

## Command reference

datasus-fetcher exposes five subcommands:

```
datasus-fetcher <subcommand> [options]

Subcommands:
  data            Download microdata files
  list-datasets   Inspect available datasets on the FTP server
  docs            Download official documentation files (codebooks)
  aux             Download auxiliary reference tables
  archive         Move non-latest file versions to an archive directory
```

---

### `data` — Download microdata files

```sh
datasus-fetcher data --data-dir <DIR> [DATASETS...] [OPTIONS]
```

| Argument | Description |
|---|---|
| `DATASETS` | One or more dataset codes (e.g. `sih-rd cnes-st`). Omit to download all datasets. |
| `--data-dir DIR` | **Required.** Local directory where files will be stored. |
| `--start PERIOD` | Start of the date filter. Format: `YYYY` or `YYYY-MM`. |
| `--end PERIOD` | End of the date filter. Format: `YYYY` or `YYYY-MM`. |
| `--regions UF ...` | One or more state codes in lowercase (e.g. `sp rj mg ba`). |
| `-t, --threads N` | Number of concurrent download threads (default: `2`). |

**Examples:**

```sh
# Dengue notifications from SINAN — all years, all states
datasus-fetcher data --data-dir ./data sinan-deng

# CNES establishments for the entire Northeast, from 2015 onwards
datasus-fetcher data --data-dir ./data cnes-st \
    --start 2015-01 \
    --regions al ba ce ma pb pe pi rn se

# SIM death records (ICD-10) from 2000 to 2023
datasus-fetcher data --data-dir ./data sim-do-cid10 \
    --start 2000 --end 2023

# Speed up downloads with more parallel threads
datasus-fetcher data --data-dir ./data sih-rd --threads 4

# Multiple datasets in one call
datasus-fetcher data --data-dir ./data \
    sinasc-dn sim-do-cid10 sih-rd \
    --start 2010-01 --end 2023-12

# HIV surveillance: adults, children, and pregnant women — full history
datasus-fetcher data --data-dir ./data \
    sinan-hiva sinan-hivc sinan-hivg sinan-hive

# Maternal and infant mortality — both CID versions
datasus-fetcher data --data-dir ./data \
    sim-domat-cid10 sim-doinf-cid09 sim-doinf-cid10

# Complete CNES snapshot for São Paulo state, latest years
datasus-fetcher data --data-dir ./data \
    cnes-st cnes-pf cnes-lt cnes-eq cnes-ep \
    --start 2020-01 \
    --regions sp

# Syphilis triad: acquired, congenital, and in pregnant women
datasus-fetcher data --data-dir ./data \
    sinan-sifa sinan-sifc sinan-sifg \
    --start 2010 --end 2023

# Hospital admissions (SIH-RD) for the South region — recent 5 years
datasus-fetcher data --data-dir ./data sih-rd \
    --start 2019-01 --end 2023-12 \
    --regions pr rs sc

# Outpatient production (SIA-PA) for a single state — high volume, use more threads
datasus-fetcher data --data-dir ./data sia-pa \
    --start 2010-01 --end 2023-12 \
    --regions sp \
    --threads 6

# Cancer-related: oncology panel + chemotherapy + radiotherapy APACs
datasus-fetcher data --data-dir ./data \
    po sia-aq sia-ar \
    --start 2013 --end 2023

# Tuberculosis and leprosy notifications — nationwide, full history
datasus-fetcher data --data-dir ./data \
    sinan-tube sinan-hans

# Arbovirus trio: dengue, Zika, and Chikungunya — Northeast only
datasus-fetcher data --data-dir ./data \
    sinan-deng sinan-zika sinan-chik \
    --regions al ba ce ma pb pe pi rn se

# Live births and infant deaths side by side — all states
datasus-fetcher data --data-dir ./data \
    sinasc-dn sim-doinf-cid10 \
    --start 2010 --end 2023
```

---

### `list-datasets` — Inspect available datasets

Connects to the DATASUS FTP server and prints file counts, sizes, and date ranges for each dataset:

```sh
datasus-fetcher list-datasets

# Inspect specific datasets only
datasus-fetcher list-datasets sih-rd sia-pa cnes-pf
```

Sample output:

```
-----------Dataset----------|---Nº files---|--Total size--|------Period range------
sih-rd                      | 10673 files  |  22639.1 MB  | from 1992-01 to 2024-12
sia-pa                      | 10193 files  | 163258.4 MB  | from 1994-07 to 2024-12
sinan-deng                  |    26 files  |   1229.0 MB  | from 2000    to 2025
```

---

### `docs` — Download documentation files

Downloads the official documentation files (data dictionaries, codebooks) for each system:

```sh
# Download docs for specific systems
datasus-fetcher docs --data-dir ./docs sih cnes sia sim sinan

# Download docs for all systems
datasus-fetcher docs --data-dir ./docs
```

---

### `aux` — Download auxiliary reference tables

Downloads lookup/reference tables (ICD codes, municipality codes, procedure tables, occupation codes, etc.):

```sh
# Download auxiliary tables for specific systems
datasus-fetcher aux --data-dir ./aux sih cnes

# Download auxiliary tables for all systems
datasus-fetcher aux --data-dir ./aux
```

---

### `archive` — Move old file versions to an archive

DATASUS periodically updates its files. datasus-fetcher stores every downloaded version with a date-stamped filename. Use `archive` to move non-latest versions to a separate directory:

```sh
datasus-fetcher archive \
    --data-dir ./data \
    --archive-data-dir ./data-archive
```

---

## File storage structure

Downloaded files are organized into a structured directory tree:

```
data/
└── sih-rd/
    ├── 199201/                              ← YYYYMM partition directory
    │   └── sih-rd_sp_199201_20250218.dbc   ← dataset_uf_period_downloaddate.dbc
    ├── 202001/
    │   ├── sih-rd_sp_202001_20250218.dbc
    │   └── sih-rd_rj_202001_20250218.dbc
    └── 202312/
        └── sih-rd_mg_202312_20250218.dbc
```

For year-only datasets (e.g. SIM, SINASC):

```
data/
└── sim-do-cid10/
    └── 2023/
        ├── sim-do-cid10_sp_2023_20250218.dbc
        └── sim-do-cid10_rj_2023_20250218.dbc
```

Each filename encodes: **dataset** + **state (UF)** + **period** + **download date**.

## Logging

datasus-fetcher logs download progress to the console by default. You can override this by placing a `logging.ini` file in your working directory. Example:

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

## Brazilian states (UF codes)

Use lowercase two-letter codes with `--regions`. You can also use `br` for national-level files where available.

| Code | State | Code | State |
|------|-------|------|-------|
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
| `pa` | Pará | `br` | Brasil (national files) |

## Available datasets

Statistics generated on **2025-02-18**.

| Dataset | Nº files | Total size | Period range |
| --- | ---: | ---: | --- |
| base-populacional-ibge-pop | 33 files | 150.4 MB | from 1980 to 2012 |
| base-populacional-ibge-pops | 25 files | 81.3 MB | from 2000 to 2024 |
| base-populacional-ibge-popt | 32 files | 2.4 MB | from 1992 to 2024 |
| base-territorial | 14 files | 20.9 MB | — |
| base-territorial-conversao | 28 files | 35.7 MB | — |
| base-territorial-mapas | 83 files | 122.2 MB | from 1991 to 2013 |
| cih-cr | 868 files | 157.5 MB | from 2008-01 to 2011-04 |
| ciha | 4201 files | 4354.5 MB | from 2011-01 to 2024-09 |
| cnes-dc | 6318 files | 115.4 MB | from 2005-08 to 2025-01 |
| cnes-ee | 3201 files | 4.3 MB | from 2007-03 to 2021-07 |
| cnes-ef | 5374 files | 10.0 MB | from 2007-03 to 2025-01 |
| cnes-ep | 5778 files | 498.8 MB | from 2007-04 to 2025-01 |
| cnes-eq | 6317 files | 1329.2 MB | from 2005-08 to 2025-01 |
| cnes-gm | 5459 files | 11.9 MB | from 2007-03 to 2025-01 |
| cnes-hb | 5805 files | 122.2 MB | from 2007-03 to 2025-01 |
| cnes-in | 5520 files | 36.4 MB | from 2007-10 to 2025-01 |
| cnes-lt | 6264 files | 131.3 MB | from 2005-10 to 2025-01 |
| cnes-pf | 6318 files | 38238.1 MB | from 2005-08 to 2025-01 |
| cnes-rc | 5744 files | 67.2 MB | from 2007-03 to 2025-01 |
| cnes-sr | 6316 files | 1389.8 MB | from 2005-08 to 2025-01 |
| cnes-st | 6310 files | 2805.5 MB | from 2005-08 to 2025-01 |
| pce | 409 files | 14.1 MB | from 1995 to 2021 |
| po | 12 files | 129.5 MB | from 2013 to 2024 |
| resp | 280 files | 3.4 MB | from 2015 to 2024 |
| sia-ab | 544 files | 13.9 MB | from 2008-01 to 2017-04 |
| sia-abo | 1352 files | 32.2 MB | from 2014-01 to 2024-12 |
| sia-acf | 3263 files | 26.7 MB | from 2014-08 to 2024-12 |
| sia-ad | 5506 files | 2683.1 MB | from 2008-01 to 2024-12 |
| sia-am | 5447 files | 14762.8 MB | from 2008-01 to 2024-12 |
| sia-an | 2145 files | 437.6 MB | from 2008-01 to 2014-10 |
| sia-aq | 5466 files | 4202.1 MB | from 2008-01 to 2024-12 |
| sia-ar | 4982 files | 318.9 MB | from 2008-01 to 2024-12 |
| sia-atd | 3371 files | 855.0 MB | from 2014-08 to 2024-12 |
| sia-pa | 10193 files | 163258.4 MB | from 1994-07 to 2024-12 |
| sia-ps | 3881 files | 2543.1 MB | from 2012-11 to 2024-12 |
| sia-sad | 1088 files | 51.0 MB | from 2012-04 to 2018-10 |
| sih-er | 4419 files | 270.4 MB | from 2011-01 to 2024-12 |
| sih-rd | 10673 files | 22639.1 MB | from 1992-01 to 2024-12 |
| sih-rj | 5348 files | 815.8 MB | from 2008-01 to 2024-12 |
| sih-sp | 8928 files | 48377.4 MB | from 1997-06 to 2024-12 |
| sim-do-cid09 | 466 files | 722.2 MB | from 1979 to 1995 |
| sim-do-cid10 | 784 files | 4307.5 MB | from 1996 to 2023 |
| sim-doext-cid09 | 17 files | 42.0 MB | from 1979 to 1995 |
| sim-doext-cid10 | 28 files | 260.2 MB | from 1996 to 2023 |
| sim-dofet-cid09 | 17 files | 23.0 MB | from 1979 to 1995 |
| sim-dofet-cid10 | 28 files | 60.9 MB | from 1996 to 2023 |
| sim-doinf-cid09 | 17 files | 58.0 MB | from 1979 to 1995 |
| sim-doinf-cid10 | 28 files | 92.0 MB | from 1996 to 2023 |
| sim-domat-cid10 | 28 files | 4.1 MB | from 1996 to 2023 |
| sim-dorext-cid10 | 11 files | 0.4 MB | from 2013 to 2023 |
| sinan-acbi | 19 files | 44.2 MB | from 2006 to 2024 |
| sinan-acgr | 19 files | 112.4 MB | from 2006 to 2024 |
| sinan-aida | 17 files | 17.1 MB | from 2007 to 2023 |
| sinan-aidc | 17 files | 0.3 MB | from 2007 to 2023 |
| sinan-anim | 17 files | 127.5 MB | from 2007 to 2023 |
| sinan-antr | 19 files | 432.7 MB | from 2006 to 2024 |
| sinan-botu | 18 files | 0.1 MB | from 2007 to 2024 |
| sinan-canc | 18 files | 0.3 MB | from 2007 to 2024 |
| sinan-chag | 24 files | 4.0 MB | from 2000 to 2023 |
| sinan-chik | 11 files | 70.7 MB | from 2015 to 2025 |
| sinan-cole | 18 files | 0.0 MB | from 2007 to 2024 |
| sinan-coqu | 19 files | 9.1 MB | from 2007 to 2025 |
| sinan-deng | 26 files | 1229.0 MB | from 2000 to 2025 |
| sinan-derm | 19 files | 0.5 MB | from 2006 to 2024 |
| sinan-dift | 16 files | 0.1 MB | from 2007 to 2022 |
| sinan-espo | 10 files | 0.4 MB | from 2013 to 2022 |
| sinan-esqu | 17 files | 7.6 MB | from 2007 to 2023 |
| sinan-exan | 18 files | 14.0 MB | from 2007 to 2024 |
| sinan-fmac | 17 files | 3.9 MB | from 2007 to 2023 |
| sinan-ftif | 18 files | 0.8 MB | from 2007 to 2024 |
| sinan-hans | 24 files | 53.6 MB | from 2001 to 2024 |
| sinan-hant | 25 files | 2.1 MB | from 1999 to 2023 |
| sinan-hepa | 17 files | 28.1 MB | from 2007 to 2023 |
| sinan-hiva | 17 files | 15.3 MB | from 2007 to 2023 |
| sinan-hivc | 17 files | 0.1 MB | from 2007 to 2023 |
| sinan-hive | 9 files | 1.0 MB | from 2015 to 2023 |
| sinan-hivg | 17 files | 3.4 MB | from 2007 to 2023 |
| sinan-iexo | 19 files | 150.3 MB | from 2006 to 2024 |
| sinan-leiv | 25 files | 12.1 MB | from 2000 to 2024 |
| sinan-lept | 18 files | 21.5 MB | from 2007 to 2024 |
| sinan-lerd | 19 files | 6.5 MB | from 2006 to 2024 |
| sinan-ltan | 25 files | 36.2 MB | from 2000 to 2024 |
| sinan-mala | 20 files | 2.5 MB | from 2004 to 2023 |
| sinan-meni | 18 files | 40.9 MB | from 2007 to 2024 |
| sinan-ment | 19 files | 1.2 MB | from 2006 to 2024 |
| sinan-ntra | 13 files | 0.6 MB | from 2010 to 2022 |
| sinan-pair | 19 files | 0.5 MB | from 2006 to 2024 |
| sinan-pest | 14 files | 0.0 MB | from 2007 to 2020 |
| sinan-pfan | 10 files | 0.5 MB | from 2012 to 2021 |
| sinan-pneu | 19 files | 0.3 MB | from 2006 to 2024 |
| sinan-raiv | 15 files | 0.1 MB | from 2007 to 2021 |
| sinan-rota | 16 files | 1.2 MB | from 2009 to 2024 |
| sinan-sdta | 14 files | 0.8 MB | from 2007 to 2021 |
| sinan-sifa | 15 files | 28.3 MB | from 2010 to 2024 |
| sinan-sifc | 18 files | 13.3 MB | from 2007 to 2024 |
| sinan-sifg | 17 files | 16.7 MB | from 2007 to 2023 |
| sinan-src | 16 files | 0.2 MB | from 2007 to 2022 |
| sinan-teta | 16 files | 0.6 MB | from 2007 to 2022 |
| sinan-tetn | 8 files | 0.0 MB | from 2014 to 2021 |
| sinan-toxc | 6 files | 0.8 MB | from 2019 to 2024 |
| sinan-toxg | 6 files | 2.3 MB | from 2019 to 2024 |
| sinan-trac | 14 files | 1.6 MB | from 2009 to 2022 |
| sinan-tube | 23 files | 97.8 MB | from 2001 to 2023 |
| sinan-varc | 17 files | 33.2 MB | from 2007 to 2023 |
| sinan-viol | 15 files | 242.4 MB | from 2009 to 2023 |
| sinan-zika | 10 files | 8.9 MB | from 2016 to 2025 |
| sinasc-dn | 838 files | 6114.7 MB | from 1994 to 2023 |
| sinasc-dnex | 10 files | 0.5 MB | from 2014 to 2023 |
| siscolo-cc | 2858 files | 2380.9 MB | from 2006-01 to 2015-10 |
| siscolo-hc | 2858 files | 38.9 MB | from 2006-01 to 2015-10 |
| sismama-cm | 1675 files | 4.8 MB | from 2009-01 to 2015-07 |
| sismama-hm | 1674 files | 5.7 MB | from 2009-01 to 2015-07 |
| sisprenatal-pn | 944 files | 221.6 MB | from 2012-01 to 2014-12 |

**Total: 320.7 GB across 170,543 files**

### Datasets by system

- **Base Populacional - IBGE** — Population estimates from Census and TCU
  - `base-populacional-ibge-pop`: Censo e Estimativas
  - `base-populacional-ibge-pops`: Estimativas por Sexo e Idade
  - `base-populacional-ibge-popt`: Estimativas TCU

- **Base Territorial** — Geographic boundaries and conversion tables
  - `base-territorial`: Base Territoriais
  - `base-territorial-mapas`: Mapas
  - `base-territorial-conversao`: Conversões

- **CIH** — Sistema de Comunicação de Informação Hospitalar
  - `cih-cr`: Comunicação de Internação Hospitalar

- **CIHA** — Sistema de Comunicação de Informação Hospitalar e Ambulatorial
  - `ciha`: Sistema de Comunicação de Informação Hospitalar e Ambulatorial

- **CNES** — Cadastro Nacional de Estabelecimentos de Saúde
  - `cnes-lt`: Leitos
  - `cnes-st`: Estabelecimentos
  - `cnes-dc`: Dados Complementares
  - `cnes-eq`: Equipamentos
  - `cnes-sr`: Serviço Especializado
  - `cnes-hb`: Habilitação
  - `cnes-pf`: Profissional
  - `cnes-ep`: Equipes
  - `cnes-rc`: Regra Contratual
  - `cnes-in`: Incentivos
  - `cnes-ee`: Estabelecimento de Ensino
  - `cnes-ef`: Estabelecimento Filantrópico
  - `cnes-gm`: Gestão e Metas

- **PCE** — Programa de Controle da Esquistossomose
  - `pce`: Programa de Controle da Esquistossomose

- **PO** — Painel de Oncologia
  - `po`: Painel de Oncologia

- **RESP** — Notificações de casos suspeitos de SCZ
  - `resp`: Notificações de casos suspeitos de SCZ

- **SIA** — Sistema de Informações Ambulatoriais
  - `sia-ab`: APAC de Acompanhamento a Cirurgia Bariátrica
  - `sia-abo`: APAC Acompanhamento Pós Cirurgia Bariátrica
  - `sia-acf`: APAC Confecção de Fístula Arteriovenosa
  - `sia-ad`: APAC de Laudos Diversos
  - `sia-am`: APAC de Medicamentos
  - `sia-an`: APAC de Nefrologia
  - `sia-aq`: APAC de Quimioterapia
  - `sia-ar`: APAC de Radioterapia
  - `sia-atd`: APAC de Tratamento Dialítico
  - `sia-pa`: Produção Ambulatorial
  - `sia-ps`: Psicossocial
  - `sia-sad`: Atenção Domiciliar

- **SIH** — Sistema de Informação Hospitalar
  - `sih-rd`: AIH Reduzida
  - `sih-rj`: AIH Rejeitadas
  - `sih-sp`: Serviços Profissionais
  - `sih-er`: AIH Rejeitadas com código de erro

- **SIM** — Sistema de Informação de Mortalidade
  - `sim-do-cid09`: Declarações de Óbito (CID-9, 1979–1995)
  - `sim-do-cid10`: Declarações de Óbito (CID-10, 1996–present)
  - `sim-doext-cid09`: Declarações de Óbitos por causas externas (CID-9)
  - `sim-doext-cid10`: Declarações de Óbitos por causas externas (CID-10)
  - `sim-dofet-cid09`: Declarações de Óbitos fetais (CID-9)
  - `sim-dofet-cid10`: Declarações de Óbitos fetais (CID-10)
  - `sim-doinf-cid09`: Declarações de Óbitos infantis (CID-9)
  - `sim-doinf-cid10`: Declarações de Óbitos infantis (CID-10)
  - `sim-domat-cid10`: Declarações de Óbitos maternos (CID-10)
  - `sim-dorext-cid10`: Mortalidade de residentes no exterior (CID-10)

- **SINAN** — Sistema de agravos de notificação compulsória
  - `sinan-acbi`: Acidente de trabalho com material biológico
  - `sinan-acgr`: Acidente de trabalho
  - `sinan-aida`: AIDS em adultos
  - `sinan-aidc`: AIDS em crianças
  - `sinan-anim`: Acidente por Animais Peçonhentos
  - `sinan-antr`: Atendimento Antirrábico
  - `sinan-botu`: Botulismo
  - `sinan-canc`: Câncer relacionado ao trabalho
  - `sinan-chag`: Doença de Chagas Aguda
  - `sinan-chik`: Febre de Chikungunya
  - `sinan-cole`: Cólera
  - `sinan-coqu`: Coqueluche
  - `sinan-deng`: Dengue
  - `sinan-derm`: Dermatoses ocupacionais
  - `sinan-dift`: Difteria
  - `sinan-espo`: Esporotricose (Epizootia)
  - `sinan-esqu`: Esquistossomose
  - `sinan-exan`: Doenças exantemáticas
  - `sinan-fmac`: Febre Maculosa
  - `sinan-ftif`: Febre Tifóide
  - `sinan-hans`: Hanseníase
  - `sinan-hant`: Hantavirose
  - `sinan-hepa`: Hepatites Virais
  - `sinan-hiva`: HIV em adultos
  - `sinan-hivc`: HIV em crianças
  - `sinan-hive`: HIV em crianças expostas
  - `sinan-hivg`: HIV em gestante
  - `sinan-iexo`: Intoxicação Exógena
  - `sinan-leiv`: Leishmaniose Visceral
  - `sinan-lept`: Leptospirose
  - `sinan-lerd`: LER/DORT
  - `sinan-ltan`: Leishmaniose Tegumentar Americana
  - `sinan-mala`: Malária
  - `sinan-meni`: Meningite
  - `sinan-ment`: Transtornos mentais relacionados ao trabalho
  - `sinan-ntra`: Notificação de Tracoma
  - `sinan-pair`: Perda auditiva por ruído relacionado ao trabalho
  - `sinan-pest`: Peste
  - `sinan-pfan`: Paralisia Flácida Aguda
  - `sinan-pneu`: Pneumoconioses relacionadas ao trabalho
  - `sinan-raiv`: Raiva
  - `sinan-rota`: Rotavírus
  - `sinan-sdta`: Surto de Doenças Transmitidas por Alimentos
  - `sinan-sifa`: Sífilis Adquirida
  - `sinan-sifc`: Sífilis Congênita
  - `sinan-sifg`: Sífilis em Gestante
  - `sinan-src`: Síndrome da Rubéola Congênita
  - `sinan-teta`: Tétano Acidental
  - `sinan-tetn`: Tétano Neonatal
  - `sinan-toxc`: Toxoplasmose Congênita
  - `sinan-toxg`: Toxoplasmose Gestacional
  - `sinan-trac`: Inquérito de Tracoma
  - `sinan-tube`: Tuberculose
  - `sinan-varc`: Varicela
  - `sinan-viol`: Violência doméstica, sexual e/ou outras violências
  - `sinan-zika`: Zika Vírus

- **SINASC** — Sistema de Informação de Nascidos Vivos
  - `sinasc-dn`: Declarações de nascidos vivos
  - `sinasc-dnex`: Declarações de nascidos vivos no exterior

- **SISCOLO** — Sistema de Informações de Cânceres de Colo de Útero
  - `siscolo-cc`: Citopatológico de Colo de Útero
  - `siscolo-hc`: Histopatológico de Colo de Útero

- **SISMAMA** — Sistema de Informações de Cânceres de Mama
  - `sismama-cm`: Citopatológico de Mama
  - `sismama-hm`: Histopatológico de Mama

- **SISPRENATAL** — Sistema de Monitoramento e Avaliação do Pré-Natal, Parto, Puerpério e Criança
  - `sisprenatal-pn`: Pré-Natal

## Data sources

Online queries (TabNet): https://datasus.saude.gov.br/informacoes-de-saude-tabnet/

Microdata transfer (FTP): https://datasus.saude.gov.br/transferencia-de-arquivos/

## Reading DBC files

datasus-fetcher downloads `.dbc` files, which is a compressed format used by DATASUS. To read these files in Python, you can use packages such as:

- [PySUS](https://github.com/AlertaDengue/PySUS)
- [read.dbc](https://github.com/dankkom/read.dbc) (R)
- [dbf2dbc](https://github.com/AlertaDengue/dbf2dbc) (conversion tool)

## Development

Install an editable development version from GitHub:

```sh
pip install -e git+https://github.com/dankkom/datasus-fetcher.git
```

Run unit tests with:

```sh
python -m unittest discover
```

### Build and publish package

Build the package with:

```sh
python -m build
```

Publish to PyPI with:

```sh
python -m twine upload dist/*
```

See [Python Packaging User Guide: The Packaging Workflow](https://packaging.python.org/en/latest/flow/) for more information.
