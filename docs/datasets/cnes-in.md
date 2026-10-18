# `cnes-in` — Incentivos

O `cnes-in` contém os microdados do arquivo de **Incentivos** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra os incentivos vinculados aos estabelecimentos de saúde. Cada registro (linha) representa um **incentivo** (`SGRUPHAB`) de um estabelecimento, em uma competência, com o período de vigência e a portaria correspondente. Documenta os incentivos federais/estaduais/municipais incorporados à rede, como os incentivos de atenção especializada e de qualificação da gestão.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cnes` — CNES: Cadastro Nacional de Estabelecimentos de Saúde |
| **Código no `datasus-fetcher`** | `cnes-in` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`) |
| **Periodicidade** | Mensal (extração por competência) |
| **Cobertura temporal no FTP** | 2007-10 a 2026-09 (conforme `index.json`) |
| **Volume aproximado no FTP** | 6060 arquivos (~44 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`) |

## 1. Contexto Institucional e Epidemiológico

O arquivo `IN` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS. O bloco de incentivos registra os incentivos financeiros e de qualificação que o estabelecimento recebe/incorpora, sendo relevante para a gestão de custeio e para a qualificação da rede de serviços. Na documentação técnica `IT_CNES_1706`, este arquivo também é referido como "IntegraSUS" na lista de arquivos do sistema.

O **evento gerador** é a habilitação/registro do incentivo no SCNES a cada competência. A **unidade de análise é o incentivo de um estabelecimento na competência** (`CNES` + `SGRUPHAB` + `COMPETEN`), com vigência em `CMPT_INI`/`CMPT_FIM` e a portaria em `PORTARIA`/`DTPORTAR`/`MAPORTAR`. Compartilha o bloco de habilitação/portaria com os arquivos `HB`, `GM`, `RC`, `EE` e `EF`.

A série histórica no FTP começa em outubro de 2007. Não há diretório preliminar.

Aplicações analíticas típicas: mapeamento de incentivos por estabelecimento e região, análise da distribuição de incentivos de custeio, acompanhamento temporal da incorporação de incentivos e apoio à verificação de repasses e à gestão financeira do SUS.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/IN` | `IN` | UF + AA + MM (ex.: `SP2410`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `INSP2410.dbc` — `IN` (Incentivos), `SP` (UF), `24` (ano), `10` (mês). Há também `INBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-in/2024-10/cnes-in_202410-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Incentivos — IN*.dbf") e `TAB_CNES.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `SGRUPHAB` | String (4) | Código do incentivo |
| `CMPT_INI` / `CMPT_FIM` | String (`AAAAMM`) | Competência inicial / final de vigência |
| `DTPORTAR` | String (10) | Data da portaria |
| `PORTARIA` | String (50) | Identificação da portaria |
| `MAPORTAR` | String (`AAAAMM`) | Data da portaria formatada como competência |
| `TP_PREST` | String (2) | Tipo de prestador |
| `VINC_SUS` | String (2) | Vínculo com o SUS: 1 - Sim, 0 - Não |
| `NAT_JUR` | String (4) | Natureza jurídica |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `TPGESTAO` | String (1) | Tipo de gestão de saúde |
| `COD_CEP` | String (8) | CEP do estabelecimento |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CNES` (7), `CODUFMUN` (6), `SGRUPHAB`, `TP_PREST`, `NAT_JUR`, `COD_CEP` e `PORTARIA` permanecem `String` com zeros à esquerda.
- **Datas e competências**: `CMPT_INI`, `CMPT_FIM` e `MAPORTAR` são `AAAAMM` textuais; `DTPORTAR` tem formato de data e não é convertido automaticamente.
- **Valores ausentes e sentinelas**: espaços, `""` e códigos ignorados viram nulo por `SENTINEL_NULLS`; registros `_deleted` são removidos.
- **Particularidades do dataset**: leiaute quase idêntico a `HB`, `GM`, `RC`, `EE` e `EF`, diferindo no contexto de `SGRUPHAB`; a vigência deve ser considerada para saber quais incentivos estavam ativos; e a interpretação de cada código exige as tabelas de domínio do `TAB_CNES.zip`.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-in
quantilica datasus list cnes-in

# 2. Baixar microdados de cnes-in (uf+yearmonth)
quantilica datasus sync cnes-in -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-in -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-in -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-in/2024-10/cnes-in_202410-sp@20261015.dbc", clean=True)

print(qdf.group_by("sgruphab").len().sort("len", descending=True).head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/IN`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout IN) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
