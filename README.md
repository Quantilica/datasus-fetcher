# datasus-fetcher: Download de microdados do DATASUS

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square) ![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=flat-square)

**datasus-fetcher** é um pacote Python e ferramenta de linha de comando para baixar em massa arquivos brutos de microdados (`.dbc`) do servidor FTP público do [DATASUS](https://datasus.saude.gov.br) (`ftp.datasus.gov.br`). Não lê nem analisa os arquivos — é um downloader confiável que organiza cópias locais do maior banco de dados de saúde pública do Brasil.

## Por que usar datasus-fetcher?

- **113 datasets** cobrindo todos os principais sistemas de informação de saúde do Brasil
- **320+ GB** de microdados históricos, com séries que remontam a 1979
- **Downloads multi-thread** — conexões paralelas configuráveis para maior velocidade
- **Filtros precisos** — recorte por intervalo de datas e/ou UF antes de baixar
- **Verificação de integridade** — pula arquivos já baixados comparando tamanhos
- **Retentativas automáticas** — até 3 tentativas em erros de FTP
- **Versionamento de arquivos** — armazena cada versão baixada com nome datado; arquiva versões antigas automaticamente
- **Documentação e tabelas auxiliares** — baixe dicionários de dados e tabelas de referência junto com os microdados
- **Sem dependências externas** — Python puro 3.10+

## Instalação

```bash
pip install datasus-fetcher
```

Para instalação global isolada (recomendado para uso apenas como CLI):

```bash
pipx install datasus-fetcher
```

## Uso Rápido

Baixar SIH-RD (Internações Hospitalares) para São Paulo, Rio de Janeiro e Minas Gerais, de 2020 a 2023:

```sh
datasus-fetcher data --data-dir /caminho/para/dados sih-rd \
    --start 2020-01 \
    --end 2023-12 \
    --regions sp rj mg
```

Baixar todos os datasets (atenção: 320+ GB no total):

```sh
datasus-fetcher data --data-dir /caminho/para/dados
```

## CLI

O `datasus-fetcher` expõe cinco subcomandos:

```
datasus-fetcher <subcommand> [options]

Subcommands:
  data            Baixa arquivos de microdados
  list-datasets   Inspeciona datasets disponíveis no FTP
  docs            Baixa arquivos de documentação (dicionários)
  aux             Baixa tabelas auxiliares de referência
  archive         Move versões antigas para um diretório de arquivo
```

---

### `data` — Baixar microdados

```sh
datasus-fetcher data --data-dir <DIR> [DATASETS...] [OPTIONS]
```

| Argumento | Descrição |
|---|---|
| `DATASETS` | Um ou mais códigos de dataset (ex: `sih-rd cnes-st`). Omita para baixar todos. |
| `--data-dir DIR` | **Obrigatório.** Diretório local onde os arquivos serão armazenados. |
| `--start PERIOD` | Início do filtro de datas. Formato: `YYYY` ou `YYYY-MM`. |
| `--end PERIOD` | Fim do filtro de datas. Formato: `YYYY` ou `YYYY-MM`. |
| `--regions UF ...` | Um ou mais códigos de UF em minúsculas (ex: `sp rj mg ba`). |
| `-t, --threads N` | Número de threads de download paralelas (padrão: `2`). |
| `--dry-run` | Lista os arquivos que seriam baixados (com tamanhos e totais) sem baixar. |

**Exemplos:**

```sh
# Notificações de Dengue (SINAN) — todos os anos, todos os estados
datasus-fetcher data --data-dir ./data sinan-deng

# Estabelecimentos CNES para o Nordeste inteiro, a partir de 2015
datasus-fetcher data --data-dir ./data cnes-st \
    --start 2015-01 \
    --regions al ba ce ma pb pe pi rn se

# Declarações de óbito SIM (CID-10) de 2000 a 2023
datasus-fetcher data --data-dir ./data sim-do-cid10 \
    --start 2000 --end 2023

# Accelerar downloads com mais threads paralelas
datasus-fetcher data --data-dir ./data sih-rd --threads 4

# Múltiplos datasets em uma chamada
datasus-fetcher data --data-dir ./data \
    sinasc-dn sim-do-cid10 sih-rd \
    --start 2010-01 --end 2023-12

# HIV: adultos, crianças e gestantes — histórico completo
datasus-fetcher data --data-dir ./data \
    sinan-hiva sinan-hivc sinan-hivg sinan-hive

# Mortalidade materna e infantil — ambas versões CID
datasus-fetcher data --data-dir ./data \
    sim-domat-cid10 sim-doinf-cid09 sim-doinf-cid10

# CNES completo para São Paulo, anos recentes
datasus-fetcher data --data-dir ./data \
    cnes-st cnes-pf cnes-lt cnes-eq cnes-ep \
    --start 2020-01 \
    --regions sp

# Tríade da sífilis: adquirida, congênita e em gestante
datasus-fetcher data --data-dir ./data \
    sinan-sifa sinan-sifc sinan-sifg \
    --start 2010 --end 2023

# AIH Reduzida (SIH-RD) para o Sul — últimos 5 anos
datasus-fetcher data --data-dir ./data sih-rd \
    --start 2019-01 --end 2023-12 \
    --regions pr rs sc

# Produção ambulatorial (SIA-PA) para um estado — alto volume, usar mais threads
datasus-fetcher data --data-dir ./data sia-pa \
    --start 2010-01 --end 2023-12 \
    --regions sp \
    --threads 6

# Oncologia: painel + quimioterapia + radioterapia (APACs)
datasus-fetcher data --data-dir ./data \
    po sia-aq sia-ar \
    --start 2013 --end 2023

# Tuberculose e hanseníase — nacional, histórico completo
datasus-fetcher data --data-dir ./data \
    sinan-tube sinan-hans

# Arboviroses: Dengue, Zika e Chikungunya — apenas Nordeste
datasus-fetcher data --data-dir ./data \
    sinan-deng sinan-zika sinan-chik \
    --regions al ba ce ma pb pe pi rn se

# Nascidos vivos e mortalidade infantil lado a lado — todos os estados
datasus-fetcher data --data-dir ./data \
    sinasc-dn sim-doinf-cid10 \
    --start 2010 --end 2023
```

---

### `list-datasets` — Inspecionar datasets disponíveis

Conecta ao FTP do DATASUS e exibe contagem de arquivos, tamanhos e intervalos de datas de cada dataset:

```sh
datasus-fetcher list-datasets

# Inspecionar datasets específicos
datasus-fetcher list-datasets sih-rd sia-pa cnes-pf
```

Exemplo de saída:

```
-----------Dataset----------|---Nº files---|--Total size--|------Period range------
sih-rd                      | 10673 files  |  22639.1 MB  | from 1992-01 to 2024-12
sia-pa                      | 10193 files  | 163258.4 MB  | from 1994-07 to 2024-12
sinan-deng                  |    26 files  |   1229.0 MB  | from 2000    to 2025
```

---

### `docs` — Baixar documentação

Baixa os arquivos oficiais de documentação (dicionários de dados, manuais) de cada sistema:

```sh
# Documentação para sistemas específicos
datasus-fetcher docs --data-dir ./docs sih cnes sia sim sinan

# Documentação de todos os sistemas
datasus-fetcher docs --data-dir ./docs
```

---

### `aux` — Baixar tabelas auxiliares

Baixa tabelas de referência (CID, municípios, procedimentos, CBO, etc.):

```sh
# Tabelas auxiliares para sistemas específicos
datasus-fetcher aux --data-dir ./aux sih cnes

# Tabelas auxiliares de todos os sistemas
datasus-fetcher aux --data-dir ./aux
```

---

### `archive` — Arquivar versões antigas

O DATASUS atualiza seus arquivos periodicamente. O datasus-fetcher armazena cada versão com nome datado. Use `archive` para mover versões não mais recentes para um diretório separado:

```sh
datasus-fetcher archive \
    --data-dir ./data \
    --archive-data-dir ./data-archive
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

Estatísticas geradas em **18 de fevereiro de 2025**.

| Dataset | Nº arquivos | Tamanho total | Período |
| --- | ---: | ---: | --- |
| base-populacional-ibge-pop | 33 | 150,4 MB | de 1980 a 2012 |
| base-populacional-ibge-pops | 25 | 81,3 MB | de 2000 a 2024 |
| base-populacional-ibge-popt | 32 | 2,4 MB | de 1992 a 2024 |
| base-territorial | 14 | 20,9 MB | — |
| base-territorial-conversao | 28 | 35,7 MB | — |
| base-territorial-mapas | 83 | 122,2 MB | de 1991 a 2013 |
| cih-cr | 868 | 157,5 MB | de 2008-01 a 2011-04 |
| ciha | 4201 | 4354,5 MB | de 2011-01 a 2024-09 |
| cnes-dc | 6318 | 115,4 MB | de 2005-08 a 2025-01 |
| cnes-ee | 3201 | 4,3 MB | de 2007-03 a 2021-07 |
| cnes-ef | 5374 | 10,0 MB | de 2007-03 a 2025-01 |
| cnes-ep | 5778 | 498,8 MB | de 2007-04 a 2025-01 |
| cnes-eq | 6317 | 1329,2 MB | de 2005-08 a 2025-01 |
| cnes-gm | 5459 | 11,9 MB | de 2007-03 a 2025-01 |
| cnes-hb | 5805 | 122,2 MB | de 2007-03 a 2025-01 |
| cnes-in | 5520 | 36,4 MB | de 2007-10 a 2025-01 |
| cnes-lt | 6264 | 131,3 MB | de 2005-10 a 2025-01 |
| cnes-pf | 6318 | 38238,1 MB | de 2005-08 a 2025-01 |
| cnes-rc | 5744 | 67,2 MB | de 2007-03 a 2025-01 |
| cnes-sr | 6316 | 1389,8 MB | de 2005-08 a 2025-01 |
| cnes-st | 6310 | 2805,5 MB | de 2005-08 a 2025-01 |
| pce | 409 | 14,1 MB | de 1995 a 2021 |
| po | 12 | 129,5 MB | de 2013 a 2024 |
| resp | 280 | 3,4 MB | de 2015 a 2024 |
| sia-ab | 544 | 13,9 MB | de 2008-01 a 2017-04 |
| sia-abo | 1352 | 32,2 MB | de 2014-01 a 2024-12 |
| sia-acf | 3263 | 26,7 MB | de 2014-08 a 2024-12 |
| sia-ad | 5506 | 2683,1 MB | de 2008-01 a 2024-12 |
| sia-am | 5447 | 14762,8 MB | de 2008-01 a 2024-12 |
| sia-an | 2145 | 437,6 MB | de 2008-01 a 2014-10 |
| sia-aq | 5466 | 4202,1 MB | de 2008-01 a 2024-12 |
| sia-ar | 4982 | 318,9 MB | de 2008-01 a 2024-12 |
| sia-atd | 3371 | 855,0 MB | de 2014-08 a 2024-12 |
| sia-pa | 10193 | 163258,4 MB | de 1994-07 a 2024-12 |
| sia-ps | 3881 | 2543,1 MB | de 2012-11 a 2024-12 |
| sia-sad | 1088 | 51,0 MB | de 2012-04 a 2018-10 |
| sih-er | 4419 | 270,4 MB | de 2011-01 a 2024-12 |
| sih-rd | 10673 | 22639,1 MB | de 1992-01 a 2024-12 |
| sih-rj | 5348 | 815,8 MB | de 2008-01 a 2024-12 |
| sih-sp | 8928 | 48377,4 MB | de 1997-06 a 2024-12 |
| sim-do-cid09 | 466 | 722,2 MB | de 1979 a 1995 |
| sim-do-cid10 | 784 | 4307,5 MB | de 1996 a 2023 |
| sim-doext-cid09 | 17 | 42,0 MB | de 1979 a 1995 |
| sim-doext-cid10 | 28 | 260,2 MB | de 1996 a 2023 |
| sim-dofet-cid09 | 17 | 23,0 MB | de 1979 a 1995 |
| sim-dofet-cid10 | 28 | 60,9 MB | de 1996 a 2023 |
| sim-doinf-cid09 | 17 | 58,0 MB | de 1979 a 1995 |
| sim-doinf-cid10 | 28 | 92,0 MB | de 1996 a 2023 |
| sim-domat-cid10 | 28 | 4,1 MB | de 1996 a 2023 |
| sim-dorext-cid10 | 11 | 0,4 MB | de 2013 a 2023 |
| sinan-acbi | 19 | 44,2 MB | de 2006 a 2024 |
| sinan-acgr | 19 | 112,4 MB | de 2006 a 2024 |
| sinan-aida | 17 | 17,1 MB | de 2007 a 2023 |
| sinan-aidc | 17 | 0,3 MB | de 2007 a 2023 |
| sinan-anim | 17 | 127,5 MB | de 2007 a 2023 |
| sinan-antr | 19 | 432,7 MB | de 2006 a 2024 |
| sinan-botu | 18 | 0,1 MB | de 2007 a 2024 |
| sinan-canc | 18 | 0,3 MB | de 2007 a 2024 |
| sinan-chag | 24 | 4,0 MB | de 2000 a 2023 |
| sinan-chik | 11 | 70,7 MB | de 2015 a 2025 |
| sinan-cole | 18 | 0,0 MB | de 2007 a 2024 |
| sinan-coqu | 19 | 9,1 MB | de 2007 a 2025 |
| sinan-deng | 26 | 1229,0 MB | de 2000 a 2025 |
| sinan-derm | 19 | 0,5 MB | de 2006 a 2024 |
| sinan-dift | 16 | 0,1 MB | de 2007 a 2022 |
| sinan-espo | 10 | 0,4 MB | de 2013 a 2022 |
| sinan-esqu | 17 | 7,6 MB | de 2007 a 2023 |
| sinan-exan | 18 | 14,0 MB | de 2007 a 2024 |
| sinan-fmac | 17 | 3,9 MB | de 2007 a 2023 |
| sinan-ftif | 18 | 0,8 MB | de 2007 a 2024 |
| sinan-hans | 24 | 53,6 MB | de 2001 a 2024 |
| sinan-hant | 25 | 2,1 MB | de 1999 a 2023 |
| sinan-hepa | 17 | 28,1 MB | de 2007 a 2023 |
| sinan-hiva | 17 | 15,3 MB | de 2007 a 2023 |
| sinan-hivc | 17 | 0,1 MB | de 2007 a 2023 |
| sinan-hive | 9 | 1,0 MB | de 2015 a 2023 |
| sinan-hivg | 17 | 3,4 MB | de 2007 a 2023 |
| sinan-iexo | 19 | 150,3 MB | de 2006 a 2024 |
| sinan-leiv | 25 | 12,1 MB | de 2000 a 2024 |
| sinan-lept | 18 | 21,5 MB | de 2007 a 2024 |
| sinan-lerd | 19 | 6,5 MB | de 2006 a 2024 |
| sinan-ltan | 25 | 36,2 MB | de 2000 a 2024 |
| sinan-mala | 20 | 2,5 MB | de 2004 a 2023 |
| sinan-meni | 18 | 40,9 MB | de 2007 a 2024 |
| sinan-ment | 19 | 1,2 MB | de 2006 a 2024 |
| sinan-ntra | 13 | 0,6 MB | de 2010 a 2022 |
| sinan-pair | 19 | 0,5 MB | de 2006 a 2024 |
| sinan-pest | 14 | 0,0 MB | de 2007 a 2020 |
| sinan-pfan | 10 | 0,5 MB | de 2012 a 2021 |
| sinan-pneu | 19 | 0,3 MB | de 2006 a 2024 |
| sinan-raiv | 15 | 0,1 MB | de 2007 a 2021 |
| sinan-rota | 16 | 1,2 MB | de 2009 a 2024 |
| sinan-sdta | 14 | 0,8 MB | de 2007 a 2021 |
| sinan-sifa | 15 | 28,3 MB | de 2010 a 2024 |
| sinan-sifc | 18 | 13,3 MB | de 2007 a 2024 |
| sinan-sifg | 17 | 16,7 MB | de 2007 a 2023 |
| sinan-src | 16 | 0,2 MB | de 2007 a 2022 |
| sinan-teta | 16 | 0,6 MB | de 2007 a 2022 |
| sinan-tetn | 8 | 0,0 MB | de 2014 a 2021 |
| sinan-toxc | 6 | 0,8 MB | de 2019 a 2024 |
| sinan-toxg | 6 | 2,3 MB | de 2019 a 2024 |
| sinan-trac | 14 | 1,6 MB | de 2009 a 2022 |
| sinan-tube | 23 | 97,8 MB | de 2001 a 2023 |
| sinan-varc | 17 | 33,2 MB | de 2007 a 2023 |
| sinan-viol | 15 | 242,4 MB | de 2009 a 2023 |
| sinan-zika | 10 | 8,9 MB | de 2016 a 2025 |
| sinasc-dn | 838 | 6114,7 MB | de 1994 a 2023 |
| sinasc-dnex | 10 | 0,5 MB | de 2014 a 2023 |
| siscolo-cc | 2858 | 2380,9 MB | de 2006-01 a 2015-10 |
| siscolo-hc | 2858 | 38,9 MB | de 2006-01 a 2015-10 |
| sismama-cm | 1675 | 4,8 MB | de 2009-01 a 2015-07 |
| sismama-hm | 1674 | 5,7 MB | de 2009-01 a 2015-07 |
| sisprenatal-pn | 944 | 221,6 MB | de 2012-01 a 2014-12 |

**Total: 320,7 GB em 170.543 arquivos**

### Datasets por sistema

- **Base Populacional - IBGE** — Estimativas populacionais do Censo e TCU
  - `base-populacional-ibge-pop`: Censo e Estimativas
  - `base-populacional-ibge-pops`: Estimativas por Sexo e Idade
  - `base-populacional-ibge-popt`: Estimativas TCU

- **Base Territorial** — Limites geográficos e tabelas de conversão
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
  - `sim-do-cid10`: Declarações de Óbito (CID-10, 1996–presente)
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

## Fontes de Dados

- Consultas online (TabNet): https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- Transferência de microdados (FTP): https://datasus.saude.gov.br/transferencia-de-arquivos/

## Lendo arquivos DBC

O datasus-fetcher baixa arquivos `.dbc`, formato compactado utilizado pelo DATASUS. Para lê-los em Python, use um dos pacotes abaixo:

- [PySUS](https://github.com/AlertaDengue/PySUS)
- [read.dbc](https://github.com/dankkom/read.dbc) (R)
- [dbf2dbc](https://github.com/AlertaDengue/dbf2dbc) (ferramenta de conversão)

## Desenvolvimento

```bash
git clone https://github.com/Quantilica/datasus-fetcher.git
cd datasus-fetcher
uv sync --dev
python -m unittest discover
```

## Licença

MIT — veja [LICENSE](LICENSE).
