# `cnes-rc` — Regra Contratual

O `cnes-rc` contém os microdados do arquivo de **Regra Contratual** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra as regras contratuais dos estabelecimentos com o SUS. Cada registro (linha) representa uma **regra contratual** (`SGRUPHAB`) de um estabelecimento, em uma competência, com o período de vigência e a portaria correspondente. Documenta as condições contratuais que definem a forma de relacionamento do prestador com o gestor do SUS.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cnes` — CNES: Cadastro Nacional de Estabelecimentos de Saúde |
| **Código no `datasus-fetcher`** | `cnes-rc` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`) |
| **Periodicidade** | Mensal (extração por competência) |
| **Cobertura temporal no FTP** | 2007-03 a 2026-09 (conforme `index.json`) |
| **Volume aproximado no FTP** | 6284 arquivos (~78 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`) |

## 1. Contexto Institucional e Epidemiológico

O arquivo `RC` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS. As regras contratuais registram as condições pelas quais o estabelecimento (prestador) se relaciona contratualmente com o SUS, incluindo a caracterização do contrato/convênio e a regra aplicável ao seu relacionamento, o que é pré-requisito para o faturamento de procedimentos.

O **evento gerador** é a atualização das regras contratuais no SCNES a cada competência. A **unidade de análise é a regra contratual de um estabelecimento na competência** (`CNES` + `SGRUPHAB` + `COMPETEN`), com vigência em `CMPT_INI`/`CMPT_FIM` e a portaria em `PORTARIA`/`DTPORTAR`/`MAPORTAR`. Compartilha o bloco de habilitação/portaria com os arquivos `HB`, `GM`, `EE`, `EF` e `IN`.

A série histórica no FTP começa em março de 2007. Não há diretório preliminar.

Aplicações analíticas típicas: caracterização do vínculo contratual dos prestadores com o SUS, apoio à análise da rede contratada, verificação de conformidade contratual para faturamento e acompanhamento temporal de mudanças nas regras contratuais.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/RC` | `RC` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `RCSP2401.dbc` — `RC` (Regra Contratual), `SP` (UF), `24` (ano), `01` (mês). Há também `RCBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-rc/2024-01/cnes-rc_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Regras Contratuais — RC*.dbf") e `TAB_CNES.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `SGRUPHAB` | String (4) | Código da regra contratual |
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
- **Particularidades do dataset**: o leiaute `RC` é quase idêntico ao de `HB`, `GM`, `EE`, `EF` e `IN`, diferindo apenas no contexto do código `SGRUPHAB`; a vigência deve ser considerada para saber quais regras estavam ativas na competência; e a interpretação de `SGRUPHAB` depende das tabelas de domínio do `TAB_CNES.zip`.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-rc
quantilica datasus list cnes-rc

# 2. Baixar microdados de cnes-rc (uf+yearmonth)
quantilica datasus sync cnes-rc -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-rc -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-rc -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-rc/2024-01/cnes-rc_202401-sp@20261015.dbc", clean=True)

print(qdf.group_by("sgruphab").len().sort("len", descending=True).head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/RC`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout RC) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
