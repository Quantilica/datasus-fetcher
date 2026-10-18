# `cnes-ee` — Estabelecimento de Ensino

O `cnes-ee` contém os microdados do arquivo de **Estabelecimento de Ensino** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra a condição de ensino/pesquisa dos estabelecimentos de saúde. Cada registro (linha) representa um **registro de ensino** (`SGRUPHAB`) de um estabelecimento, em uma competência, com vigência e portaria. Identifica estabelecimentos que desenvolvem atividades de ensino e pesquisa e que, por isso, recebem tratamento específico na certificação e no custeio.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cnes` — CNES: Cadastro Nacional de Estabelecimentos de Saúde |
| **Código no `datasus-fetcher`** | `cnes-ee` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`) |
| **Periodicidade** | Mensal (extração por competência) |
| **Cobertura temporal no FTP** | 2007-03 a 2021-07 (conforme `index.json`) — **série descontinuada** |
| **Volume aproximado no FTP** | 3201 arquivos (~4,6 MB, 23 UFs) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`) |

## 1. Contexto Institucional e Epidemiológico

O arquivo `EE` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS. A condição de "estabelecimento de ensino" é relevante para as políticas de formação e de residência em saúde e para a certificação de hospitais de ensino, além de influenciar o custeio de determinados serviços. O cadastro de ensino é alimentado no SCNES e refletido nos arquivos mensais.

O **evento gerador** é a atualização da condição de ensino no SCNES a cada competência. A **unidade de análise é o registro de ensino de um estabelecimento na competência** (`CNES` + `SGRUPHAB` + `COMPETEN`), com vigência em `CMPT_INI`/`CMPT_FIM` e a portaria em `PORTARIA`/`DTPORTAR`/`MAPORTAR`. Compartilha o bloco de habilitação/portaria com os arquivos `HB`, `GM`, `RC`, `EF` e `IN`.

**Importante**: a série histórica de `EE` no FTP foi **descontinuada** — os últimos arquivos publicados são de julho de 2021 (a cobertura aparece com 23 UFs, refletindo publicação parcial em alguns anos), diferentemente dos demais arquivos do CNES, que seguem atualizados. Para competências posteriores, a informação de ensino passou a ser tratada em outros campos/arquivos do CNES. Não há diretório preliminar.

Aplicações analíticas típicas: identificação de hospitais e unidades de ensino, estudos sobre a inserção do ensino nos serviços de saúde e apoio a políticas de formação e residência médica; em séries longas, recomenda-se usar o `EE` apenas até 2021.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/EE` | `EE` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `EESP2101.dbc` — `EE` (Estabelecimento de Ensino), `SP` (UF), `21` (ano), `01` (mês).
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-ee/<YYYY-MM>/cnes-ee_<YYYYMM>-<uf>@<AAAAMMDD>.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Estabelecimento de Ensino — EE*.dbf") e `TAB_CNES.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `SGRUPHAB` | String (4) | Código do grupo de habilitação/ensino |
| `CMPT_INI` / `CMPT_FIM` | String (`AAAAMM`) | Competência inicial / final de vigência |
| `DTPORTAR` | String (10) | Data da portaria |
| `PORTARIA` | String (50) | Identificação da portaria |
| `MAPORTAR` | String (`AAAAMM`) | Data da portaria formatada como competência |
| `TP_PREST` | String (2) | Tipo de prestador |
| `VINC_SUS` | String (2) | Vínculo com o SUS: 1 - Sim, 0 - Não |
| `NAT_JUR` | String (4) | Natureza jurídica |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `TPGESTAO` | String (1) | Tipo de gestão de saúde |
| `ATIVIDAD` | String (2) | Código da atividade de ensino/pesquisa |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CNES` (7), `CODUFMUN` (6), `SGRUPHAB`, `TP_PREST`, `NAT_JUR` e `PORTARIA` permanecem `String` com zeros à esquerda.
- **Datas e competências**: `CMPT_INI`, `CMPT_FIM` e `MAPORTAR` são `AAAAMM` textuais; `DTPORTAR` tem formato de data e não é convertido automaticamente.
- **Valores ausentes e sentinelas**: espaços, `""` e códigos ignorados viram nulo por `SENTINEL_NULLS`; registros `_deleted` são removidos.
- **Particularidades do dataset**: série descontinuada em julho/2021 (não usar para datas posteriores); cobertura parcial em algumas UFs; leiaute quase idêntico a `HB`, `GM`, `RC`, `EF` e `IN`; e a vigência (`CMPT_INI`/`CMPT_FIM`) define os registros válidos na competência.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-ee
quantilica datasus list cnes-ee

# 2. Baixar microdados de cnes-ee (uf+yearmonth; série termina em 2021-07)
quantilica datasus sync cnes-ee -o ./data --start 2020-01 --end 2021-07 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-ee -o ./data --docs --aux --start 2020-01 --end 2021-07

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-ee -o ./data/raw --parquet-dir ./data/parquet --start 2020-01 --end 2021-07
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-ee/2021-07/cnes-ee_202107-sp@20210818.dbc", clean=True)

print(qdf.group_by("sgruphab").len().sort("len", descending=True).head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EE`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout EE) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
