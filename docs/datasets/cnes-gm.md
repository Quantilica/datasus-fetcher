# `cnes-gm` — Gestão e Metas

O `cnes-gm` contém os microdados do arquivo de **Gestão e Metas** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra as metas e compromissos de gestão vinculados aos estabelecimentos. Cada registro (linha) representa um **grupo de meta/gestão** (`SGRUPHAB`) de um estabelecimento, em uma competência, com o período de vigência e a portaria correspondente. Complementa as habilitações ao registrar os compromissos assumidos pelo estabelecimento no âmbito da gestão do SUS.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cnes` — CNES: Cadastro Nacional de Estabelecimentos de Saúde |
| **Código no `datasus-fetcher`** | `cnes-gm` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`) |
| **Periodicidade** | Mensal (extração por competência) |
| **Cobertura temporal no FTP** | 2007-03 a 2026-09 (conforme `index.json`) |
| **Volume aproximado no FTP** | 5975 arquivos (~13 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`) |

## 1. Contexto Institucional e Epidemiológico

O arquivo `GM` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS. O bloco de gestão e metas documenta os vínculos de compromisso do estabelecimento com a gestão do SUS (por exemplo, metas de atenção e termos de compromisso de gestão), relacionados às pactuações entre gestores e prestadores.

O **evento gerador** é a atualização desses compromissos no SCNES a cada competência. A **unidade de análise é o grupo de meta/gestão de um estabelecimento na competência** (`CNES` + `SGRUPHAB` + `COMPETEN`), com vigência em `CMPT_INI`/`CMPT_FIM` e a portaria correspondente em `PORTARIA`/`DTPORTAR`/`MAPORTAR`. O leiaute compartilha o bloco de habilitação/portaria com os arquivos `HB`, `RC`, `EE`, `EF` e `IN`.

A série histórica no FTP começa em março de 2007. É o menor arquivo do CNES em volume, porque poucos estabelecimentos possuem metas/gestão formalmente cadastradas. Não há diretório preliminar.

Aplicações analíticas típicas: identificação de estabelecimentos com metas/compromissos de gestão formalizados, análise da distribuição regional desses compromissos, acompanhamento temporal de pactuações e apoio à verificação de pré-requisitos de financiamento e de qualificação da gestão.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/GM` | `GM` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `GMSP2401.dbc` — `GM` (Gestão e Metas), `SP` (UF), `24` (ano), `01` (mês). Há também `GMBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-gm/2024-01/cnes-gm_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Gestão e Metas — GM*.dbf") e `TAB_CNES.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `SGRUPHAB` | String (4) | Código do grupo de gestão/meta |
| `CMPT_INI` / `CMPT_FIM` | String (`AAAAMM`) | Competência inicial / final de vigência |
| `DTPORTAR` | String (10) | Data da portaria |
| `PORTARIA` | String (50) | Identificação da portaria |
| `MAPORTAR` | String (`AAAAMM`) | Data da portaria formatada como competência |
| `TP_PREST` | String (2) | Tipo de prestador |
| `VINC_SUS` | String (2) | Vínculo com o SUS: 1 - Sim, 0 - Não |
| `NAT_JUR` | String (6) | Natureza jurídica |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `TPGESTAO` | String (1) | Tipo de gestão de saúde |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CNES` (7), `CODUFMUN` (6), `SGRUPHAB`, `TP_PREST`, `NAT_JUR` e `PORTARIA` permanecem `String` com zeros à esquerda.
- **Datas e competências**: `CMPT_INI`, `CMPT_FIM` e `MAPORTAR` são `AAAAMM` textuais; `DTPORTAR` tem formato de data de 10 caracteres e não é convertido automaticamente.
- **Valores ausentes e sentinelas**: espaços, `""` e códigos ignorados viram nulo por `SENTINEL_NULLS`; registros `_deleted` são removidos.
- **Particularidades do dataset**: por ser um arquivo pequeno e especializado, não representa toda a rede — sua ausência não significa ausência de gestão; o código `SGRUPHAB` deve ser interpretado com a tabela de domínio; e a vigência (`CMPT_INI`/`CMPT_FIM`) precisa ser considerada para saber quais metas estavam ativas na competência.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-gm
quantilica datasus list cnes-gm

# 2. Baixar microdados de cnes-gm (uf+yearmonth)
quantilica datasus sync cnes-gm -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-gm -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-gm -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-gm/2024-01/cnes-gm_202401-sp@20261015.dbc", clean=True)

print(qdf.group_by("sgruphab").len().sort("len", descending=True))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/GM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout GM) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
