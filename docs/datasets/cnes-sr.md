# `cnes-sr` — Serviço Especializado

O `cnes-sr` contém os microdados do arquivo de **Serviço Especializado** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra os serviços especializados ofertados pelos estabelecimentos. Cada registro (linha) representa um **serviço/classificação** (`SERV_ESP` + `CLASS_SR`) oferecido por um estabelecimento, em uma competência mensal, com a caracterização do serviço e a indicação do tipo de atendimento (ambulatorial/hospitalar e SUS/não SUS). É a base para mapear a oferta de serviços especializados, de referência e de alta complexidade.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cnes` — CNES: Cadastro Nacional de Estabelecimentos de Saúde |
| **Código no `datasus-fetcher`** | `cnes-sr` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`) |
| **Periodicidade** | Mensal (extração por competência) |
| **Cobertura temporal no FTP** | 2005-08 a 2026-09 (conforme `index.json`) |
| **Volume aproximado no FTP** | 6856 arquivos (~1,55 GB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`) |

## 1. Contexto Institucional e Epidemiológico

O arquivo `SR` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS e alimentado pelos estabelecimentos no SCNES. Os serviços especializados cadastrados são a base para habilitar o estabelecimento a ofertar determinados procedimentos e para a organização da Rede de Atenção à Saúde (RAS), incluindo serviços de referência (oncologia, cardiologia, nefrologia, saúde mental, reabilitação, entre outros).

O **evento gerador** é a declaração dos serviços na FCES/SCNES a cada competência. A **unidade de análise é o serviço/classificação de um estabelecimento na competência** (`CNES` + `SERV_ESP` + `CLASS_SR` + `COMPETEN`). `SERV_ESP` é o código do serviço especializado e `CLASS_SR` a classificação dentro do serviço (usando `999` quando inexistente). O campo `CARACTER` caracteriza o serviço e `AMB_HOSP` indica se o atendimento é ambulatorial SUS, ambulatorial não SUS, hospitalar SUS ou hospitalar não SUS. `CNESTERC` referencia o CNES de um estabelecimento terceiro quando o serviço é prestado por terceiros.

A série histórica no FTP começa em agosto de 2005. As tabelas de serviços e classificações evoluíram com as portarias do Ministério da Saúde (recomposições periódicas das tabelas de serviços/classificações, como a Portaria SAS/MS nº 154/2008). Não há diretório preliminar.

Aplicações analíticas típicas: distribuição regional de serviços especializados e de alta complexidade, identificação de estabelecimentos de referência, análise da oferta de serviços por tipo de atendimento (SUS vs. não SUS), apoio à regulação e à pactuação de referências e integração com SIA/SIH para verificar a oferta declarada versus a produção realizada.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/SR` | `SR` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `SRSP2401.dbc` — `SR` (Serviço Especializado), `SP` (UF), `24` (ano), `01` (mês). Há também `SRBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-sr/2024-01/cnes-sr_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Serviço Especializado — SR*.dbf") e `TAB_CNES.zip` (tabelas de serviços/classificações).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `SERV_ESP` | String (3) | Código do serviço especializado |
| `CLASS_SR` | String (3) | Código da classificação do serviço (ou `999` se inexistente) |
| `SRVUNICO` | String (3) | Código do serviço especializado único |
| `CARACTER` | String (1) | Caracterização do serviço |
| `AMB_HOSP` | String (4) | Ambulatorial/hospitalar e SUS/não SUS (1 - Sim, 0 - Não) |
| `CNESTERC` | String (7) | CNES do estabelecimento terceiro |
| `NAT_JUR` | String (4) | Natureza jurídica |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `TPGESTAO` | String (1) | Tipo de gestão de saúde |
| `NIV_DEP` | String (1) | Grau de dependência: 1 - Individual, 3 - Mantida |
| `TERCEIRO` | String (1) | O estabelecimento é terceiro: 1 - Sim, 0 - Não |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CNES`, `CNESTERC` (7), `CODUFMUN` (6), `SERV_ESP`, `CLASS_SR` e `SRVUNICO` permanecem `String` com zeros à esquerda; `CLASS_SR = "999"` é sentinela de inexistência.
- **Datas e competências**: `COMPETEN` é `AAAAMM` e permanece textual.
- **Valores ausentes e sentinelas**: espaços, `""` e o código especial `999` são convertidos para nulo por `SENTINEL_NULLS`; registros `_deleted` são removidos.
- **Particularidades do dataset**: como um estabelecimento pode ofertar vários serviços/classificações, a contagem de "serviços" exige agrupar por `SERV_ESP`; `AMB_HOSP` é um código de 4 caracteres que representa combinações de flags e precisa de dicionário; códigos de serviço são recompostos por portaria periodicamente, exigindo mapeamentos históricos; e `CNESTERC` revela arranjos de terceirização que devem ser considerados ao atribuir produção ao estabelecimento.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-sr
quantilica datasus list cnes-sr

# 2. Baixar microdados de cnes-sr (uf+yearmonth)
quantilica datasus sync cnes-sr -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-sr -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-sr -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-sr/2024-01/cnes-sr_202401-sp@20261015.dbc", clean=True)

# Estabelecimentos por serviço especializado
servicos = (
    qdf.group_by("serv_esp")
    .agg(pl.col("cnes").n_unique().alias("estabelecimentos"))
    .sort("estabelecimentos", descending=True)
)
print(servicos)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/SR`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout SR) e `TAB_CNES.zip`
- **Portaria SAS/MS nº 154/2008** (recomposição da Tabela de Serviços/Classificações) e **Portaria GM/MS nº 1.646/2015**
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
