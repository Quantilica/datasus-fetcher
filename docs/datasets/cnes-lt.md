# `cnes-lt` — Leitos

O `cnes-lt` contém os microdados do arquivo de **Leitos** do Cadastro Nacional de Estabelecimentos de Saúde (CNES). Cada registro (linha) representa um conjunto de leitos de um **tipo e especialidade** (`TP_LEITO` + `CODLEITO`) existente em um estabelecimento, em uma competência mensal, com a quantidade existente, contratada e disponível para o SUS. É a base oficial para dimensionamento da oferta de leitos hospitalares no país.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cnes` — CNES: Cadastro Nacional de Estabelecimentos de Saúde |
| **Código no `datasus-fetcher`** | `cnes-lt` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`) |
| **Periodicidade** | Mensal (extração por competência) |
| **Cobertura temporal no FTP** | 2005-10 a 2026-09 (conforme `index.json`) |
| **Volume aproximado no FTP** | 6804 arquivos (~143 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`) |

## 1. Contexto Institucional e Epidemiológico

O arquivo `LT` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), sob gestão do Ministério da Saúde/DATASUS e manutenção dos gestores estaduais e municipais. Os leitos são a unidade física de internação e sua declaração no CNES é condição para o faturamento de internações no SIH/SUS e para o planejamento da regulação de vagas.

O **evento gerador** é a declaração das quantidades de leitos por tipo e especialidade na FCES/SCNES a cada competência. A **unidade de análise é o par tipo–especialidade de leito em um estabelecimento na competência** (`CNES` + `TP_LEITO` + `CODLEITO` + `COMPETEN`). O campo `QT_EXIST` registra os leitos existentes, `QT_CONTR` os contratados e `QT_SUS` os disponibilizados ao SUS — a diferença entre eles mede a parcela não ofertada ao sistema público. As categorias de tipo de leito (cirúrgico, clínico, complementar, obstétrico, pediátrico, UTI adulto/neonatal/pediátrica, etc.) estão nas tabelas de domínio do `TAB_CNES.zip`.

A série histórica no FTP inicia em outubro de 2005 e as quantidades refletem o autocadastro mensal do estabelecimento. Não há diretório preliminar. Ao longo dos anos surgiram especialidades e tipos de leito (por exemplo, leitos de UTI COVID-19 durante a pandemia de 2020), alterando as categorias disponíveis.

Aplicações analíticas típicas: oferta de leitos por habitante, taxa de ocupação e de leitos SUS, acompanhamento da capacidade de UTI, planejamento regional de internações, comparação leitos SUS vs. não SUS e integração com o SIH para cálculo de taxas de ocupação e tempo médio de permanência.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/LT` | `LT` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `LTSP2401.dbc` — `LT` (Leitos), `SP` (UF), `24` (ano), `01` (mês). Há também `LTBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-lt/2024-01/cnes-lt_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Leitos — LT*.dbf") e `TAB_CNES.zip` (domínios de tipo e especialidade de leito).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `TP_LEITO` | String (2) | Tipo do leito (cirúrgico, clínico, complementar, obstétrico, etc.) |
| `CODLEITO` | String (2) | Especialidade do leito |
| `QT_EXIST` | Inteiro | Quantidade de leitos existentes |
| `QT_CONTR` | Inteiro | Quantidade de leitos contratados |
| `QT_SUS` | Inteiro | Quantidade de leitos disponíveis para o SUS |
| `TPGESTAO` | String (1) | Tipo de gestão de saúde |
| `PF_PJ` | String (1) | Indicador de pessoa: 1 - Física, 3 - Jurídica |
| `NIV_DEP` | String (1) | Grau de dependência: 1 - Individual, 3 - Mantida |
| `NATUREZA` | String (2) | Código da natureza da organização |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `TERCEIRO` | String (1) | O estabelecimento é terceiro: 1 - Sim, 0 - Não |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CNES` (7), `CODUFMUN` (6), `TP_LEITO`, `CODLEITO`, `TP_UNID` e `TPGESTAO` são códigos e devem permanecer `String` com zeros à esquerda.
- **Datas e competências**: `COMPETEN` é `AAAAMM` e permanece textual; não há datas `AAAAMMDD`.
- **Valores ausentes e sentinelas**: quantidades vazias, `""` e códigos ignorados (`9/99`) são convertidos para nulo por `SENTINEL_NULLS`; registros `_deleted` são removidos.
- **Particularidades do dataset**: a granularidade é tipo+especialidade, portanto a soma de `QT_EXIST` por estabelecimento exige agregação; `QT_SUS` pode ser menor que `QT_CONTR` e `QT_EXIST` (nem todo leito é ofertado ao SUS); categorias de leito mudam com o tempo (novos tipos de UTI) e exigem os domínios atualizados de `TAB_CNES.zip`; e o autocadastro pode apresentar inconsistências que precisam de validação contra o SIH.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-lt
quantilica datasus list cnes-lt

# 2. Baixar microdados de cnes-lt (uf+yearmonth)
quantilica datasus sync cnes-lt -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-lt -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-lt -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-lt/2024-01/cnes-lt_202401-sp@20261015.dbc", clean=True)

# Total de leitos SUS por tipo de leito
leitos = (
    qdf.group_by("tp_leito")
    .agg(pl.col("qt_sus").sum().alias("leitos_sus"))
    .sort("leitos_sus", descending=True)
)
print(leitos)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/LT`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout LT) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
