# `cnes-ef` — Estabelecimento Filantrópico

O `cnes-ef` contém os microdados do arquivo de **Estabelecimento Filantrópico** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra a condição de filantropia dos estabelecimentos de saúde. Cada registro (linha) representa um **registro de filantropia** (`SGRUPHAB`) de um estabelecimento, em uma competência, com vigência e portaria. Identifica entidades beneficentes de assistência social na área da saúde (CEBAS-Saúde), relevantes para a certificação e para a imunidade/isenção de contribuições.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cnes` — CNES: Cadastro Nacional de Estabelecimentos de Saúde |
| **Código no `datasus-fetcher`** | `cnes-ef` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`) |
| **Periodicidade** | Mensal (extração por competência) |
| **Cobertura temporal no FTP** | 2007-03 a 2026-09 (conforme `index.json`) |
| **Volume aproximado no FTP** | 5874 arquivos (~11 MB, 25 UFs) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`) |

## 1. Contexto Institucional e Epidemiológico

O arquivo `EF` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS. A condição de estabelecimento filantrópico é relevante porque entidades beneficentes certificadas (CEBAS-Saúde, concedido pelo Ministério da Saúde) têm tratamento tributário específico e são parceiras importantes do SUS, sobretudo em hospitais de referência.

O **evento gerador** é o registro/atualização da condição de filantropia no SCNES a cada competência. A **unidade de análise é o registro de filantropia de um estabelecimento na competência** (`CNES` + `SGRUPHAB` + `COMPETEN`), com vigência em `CMPT_INI`/`CMPT_FIM` e a portaria em `PORTARIA`/`DTPORTAR`/`MAPORTAR`. Compartilha o bloco de habilitação/portaria com os arquivos `HB`, `GM`, `RC`, `EE` e `IN`. A cobertura aparece com 25 UFs (sem arquivos para algumas UFs, o que reflete a inexistência de estabelecimentos filantrópicos cadastrados em todas as competências).

A série histórica no FTP começa em março de 2007. Não há diretório preliminar.

Aplicações analíticas típicas: identificação de entidades filantrópicas que ofertam serviços ao SUS, análise da participação filantrópica na rede hospitalar, apoio à certificação/renovação do CEBAS-Saúde e estudos sobre a composição público-privada da oferta assistencial.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/EF` | `EF` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `EFSP2401.dbc` — `EF` (Estabelecimento Filantrópico), `SP` (UF), `24` (ano), `01` (mês). Há também `EFBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-ef/2024-01/cnes-ef_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Estabelecimento Filantrópico — EF*.dbf") e `TAB_CNES.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `SGRUPHAB` | String (4) | Código do grupo de habilitação/filantropia |
| `CMPT_INI` / `CMPT_FIM` | String (`AAAAMM`) | Competência inicial / final de vigência |
| `DTPORTAR` | String (10) | Data da portaria |
| `PORTARIA` | String (50) | Identificação da portaria |
| `MAPORTAR` | String (`AAAAMM`) | Data da portaria formatada como competência |
| `TP_PREST` | String (2) | Tipo de prestador |
| `VINC_SUS` | String (2) | Vínculo com o SUS: 1 - Sim, 0 - Não |
| `NAT_JUR` | String (4) | Natureza jurídica |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `TPGESTAO` | String (1) | Tipo de gestão de saúde |
| `TERCEIRO` | String (1) | O estabelecimento é terceiro: 1 - Sim, 0 - Não |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CNES` (7), `CODUFMUN` (6), `SGRUPHAB`, `TP_PREST`, `NAT_JUR` e `PORTARIA` permanecem `String` com zeros à esquerda.
- **Datas e competências**: `CMPT_INI`, `CMPT_FIM` e `MAPORTAR` são `AAAAMM` textuais; `DTPORTAR` tem formato de data e não é convertido automaticamente.
- **Valores ausentes e sentinelas**: espaços, `""` e códigos ignorados viram nulo por `SENTINEL_NULLS`; registros `_deleted` são removidos.
- **Particularidades do dataset**: cobertura parcial de UFs (algumas não possuem estabelecimentos filantrópicos na competência); leiaute quase idêntico a `HB`, `GM`, `RC`, `EE` e `IN`; vigência deve ser considerada para saber quais estabelecimentos eram filantrópicos em cada competência; e a interpretação de `SGRUPHAB` exige as tabelas de domínio.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-ef
quantilica datasus list cnes-ef

# 2. Baixar microdados de cnes-ef (uf+yearmonth)
quantilica datasus sync cnes-ef -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-ef -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-ef -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-ef/2024-01/cnes-ef_202401-sp@20261015.dbc", clean=True)

# Estabelecimentos filantrópicos cadastrados na competência
print(qdf.select(pl.col("cnes").n_unique().alias("estabelecimentos_filantropicos")))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EF`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout EF) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **Certificação de Entidades Beneficentes de Assistência Social na área da Saúde (CEBAS-Saúde)**
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
