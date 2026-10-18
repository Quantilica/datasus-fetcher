# `cnes-hb` — Habilitação

O `cnes-hb` contém os microdados do arquivo de **Habilitações** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra as habilitações de serviços dos estabelecimentos. Cada registro (linha) representa uma **habilitação concedida** a um estabelecimento, em uma competência, com o grupo de habilitação (`SGRUPHAB`), o período de vigência (`CMPT_INI`/`CMPT_FIM`) e a portaria que a concedeu. É a base que materializa as habilitações de alta complexidade e de serviços especializados previstas em portarias específicas do Ministério da Saúde.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cnes` — CNES: Cadastro Nacional de Estabelecimentos de Saúde |
| **Código no `datasus-fetcher`** | `cnes-hb` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`) |
| **Periodicidade** | Mensal (extração por competência) |
| **Cobertura temporal no FTP** | 2007-03 a 2026-09 (conforme `index.json`) |
| **Volume aproximado no FTP** | 6345 arquivos (~140 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`) |

## 1. Contexto Institucional e Epidemiológico

O arquivo `HB` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS. As habilitações registram o reconhecimento formal, por portaria, de que um estabelecimento atende aos requisitos para ofertar serviços específicos — por exemplo, Unidade de Alta Complexidade em Oncologia (UNACON/CACON), Centro de Referência em Saúde do Trabalhador (CEREST), habilitação em alta complexidade cardiovascular, nefrologia, fisioterapia, entre outras.

O **evento gerador** é a concessão/mantenação da habilitação, refletida no SCNES a cada competência. A **unidade de análise é a habilitação de um estabelecimento na competência** (`CNES` + `SGRUPHAB` + `COMPETEN`). O código `SGRUPHAB` (4 dígitos) identifica o grupo/subgrupo de habilitação conforme a tabela de domínio do CNES; `CMPT_INI` e `CMPT_FIM` delimitam a validade da habilitação; `DTPORTAR`/`PORTARIA`/`MAPORTAR` documentam a portaria concessora; e `NULEITOS` registra a quantidade de leitos associada quando aplicável.

A série histórica no FTP começa em março de 2007. Como as habilitações dependem de portarias específicas que são publicadas e revogadas ao longo do tempo, a base funciona como um retrato mensal das habilitações vigentes. Não há diretório preliminar.

Aplicações analíticas típicas: mapeamento de estabelecimentos habilitados por tipo de serviço, distribuição regional de referências de alta complexidade, acompanhamento temporal de concessões e revogações de habilitações, apoio à regulação regional e à verificação de pré-requisitos para procedimentos de alta complexidade e custeio.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/HB` | `HB` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `HBSP2401.dbc` — `HB` (Habilitações), `SP` (UF), `24` (ano), `01` (mês). Há também `HBBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-hb/2024-01/cnes-hb_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Habilitações — HB*.dbf") e `TAB_CNES.zip` (tabela de grupos de habilitação e portarias).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `SGRUPHAB` | String (4) | Código da habilitação (grupo/subgrupo) |
| `CMPT_INI` / `CMPT_FIM` | String (`AAAAMM`) | Competência inicial / final de vigência da habilitação |
| `DTPORTAR` | String (10) | Data da portaria (formato de data) |
| `PORTARIA` | String (50) | Identificação da portaria concessora |
| `MAPORTAR` | String (`AAAAMM`) | Data da portaria formatada como competência |
| `NULEITOS` | Inteiro | Quantidade de leitos associada à habilitação |
| `TP_PREST` | String (2) | Tipo de prestador |
| `VINC_SUS` | String (2) | Vínculo com o SUS: 1 - Sim, 0 - Não |
| `NAT_JUR` | String (4) | Natureza jurídica |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `TERCEIRO` | String (1) | O estabelecimento é terceiro: 1 - Sim, 0 - Não |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CNES` (7), `CODUFMUN` (6), `SGRUPHAB`, `TP_PREST`, `NAT_JUR` e `PORTARIA` permanecem `String` com zeros à esquerda; o número de portaria nunca deve ser convertido a número.
- **Datas e competências**: `CMPT_INI`, `CMPT_FIM` e `MAPORTAR` são competências `AAAAMM` (textuais); `DTPORTAR` tem 10 caracteres e formato de data e não é convertido automaticamente pela rotina de `AAAAMMDD`.
- **Valores ausentes e sentinelas**: espaços, `""` e códigos ignorados são convertidos para nulo por `SENTINEL_NULLS`; registros `_deleted` são removidos.
- **Particularidades do dataset**: as habilitações têm vigência, de modo que o recorte de um estabelecimento "habilitado" em determinada competência exige checar `CMPT_INI`/`CMPT_FIM`; um mesmo CNES pode acumular várias habilitações; o leiaute `HB` compartilha o bloco de habilitação com os arquivos `RC`, `GM`, `EE`, `EF` e `IN`, cujo significado difere apenas no contexto; e `PORTARIA`/`DTPORTAR` podem conter erros de digitação, exigindo tratamento textual.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-hb
quantilica datasus list cnes-hb

# 2. Baixar microdados de cnes-hb (uf+yearmonth)
quantilica datasus sync cnes-hb -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-hb -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-hb -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-hb/2024-01/cnes-hb_202401-sp@20261015.dbc", clean=True)

# Habilitações vigentes por grupo
hab = (
    qdf.filter(pl.col("cmpt_fim").is_null())
    .group_by("sgruphab")
    .agg(pl.col("cnes").n_unique().alias("estabelecimentos"))
    .sort("estabelecimentos", descending=True)
)
print(hab)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/HB`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout HB) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
