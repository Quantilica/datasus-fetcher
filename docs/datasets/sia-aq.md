# `sia-aq` — APAC de Quimioterapia

`sia-aq` reúne as **APAC de Quimioterapia** do SIA/SUS: cada linha é a cobrança mensal de uma APAC oncológica de tratamento sistêmico, com campos de estadiamento, grau histológico, data de identificação patológica, tratamento anterior, esquema quimioterápico e medicamentos.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sia` — SIA: Sistema de Informações Ambulatoriais |
| **Código no `datasus-fetcher`** | `sia-aq` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 2008-01 a 2026-07 (conforme `index.json`; 27 UFs com arquivos; última atualização no FTP em 2026-09-14) |
| **Volume aproximado no FTP** | 5.979 arquivos (~5,1 GB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIASUS/200801_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIASUS/200801_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **tratamento quimioterápico do câncer** autorizado por APAC (laudo por CACON/UNACON). A unidade de análise é a **APAC por competência**. A Autorização de Procedimentos de Alta Complexidade/Custo (APAC) é o instrumento de autorização e cobrança de procedimentos ambulatoriais de alta complexidade ou de uso continuado: o tratamento é autorizado por um gestor com validade de até três competências, e cada mês de cobrança gera uma linha no arquivo. A chave do registro é o número da APAC (`AP_AUTORIZ`, 13 dígitos) combinado com a competência (`AP_CMP`/`AP_MVM`); a APAC subsequente de um mesmo tratamento referencia a anterior em `AP_APACANT`. Os campos `AQ_*` descrevem o caso oncológico: `AQ_ESTADI` (estadiamento), `AQ_GRAHIS` (grau histológico), `AQ_DTIDEN` (data de identificação patológica), `AQ_TRANTE` (tratamento anterior), `AQ_CIDINI1…3`/`AQ_DTINI1…3` (tratamentos iniciais), `AQ_CONTTR` (continuidade), `AQ_DTINTR` (início do tratamento), `AQ_ESQU_P1/P2` (esquema), `AQ_TOTMPL`/`AQ_TOTMAU` (meses planejados/autorizados) e `AQ_MED01…10` (medicamentos).

No FTP cobre 2008-01 a 2026-07 (27 UFs, ~5,1 GB). O enquadramento legal inclui a Lei nº 12.732/2012 (início do tratamento oncológico em até 60 dias do diagnóstico) e a Lei nº 13.896/2019 (exames em até 30 dias); a Política Nacional para a Prevenção e Controle do Câncer (Portaria GM/MS nº 874/2013) orienta a rede de atenção oncológica. A APAC oncológica é a principal fonte administrativa de produção de quimioterapia do SUS.

Aplicações: volume de tratamentos de quimioterapia por tipo de câncer (CID `C00–C97`) e estadiamento; oportunidade do tratamento (intervalo entre `AQ_DTIDEN` e `AQ_DTINTR`, referência da Lei 12.732); mapeamento da oferta (CACON/UNACON); gasto com esquemas quimioterápicos; e estudos de acesso e fluxo de pacientes entre municípios (`AP_MUNPCN` vs. `AP_UFMUN`). Para registros de câncer de base populacional, combine com `siscan`/RHC.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `AQ` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `AQSP2401.dbc` — `AQ` (APAC de Quimioterapia) + `SP` (UF) + `24` + `01`.
- **No armazenamento local do `datasus-fetcher`**: `data/sia-aq/<AAAAMM>/sia-aq_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sia-aq/202401/sia-aq_ac_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

75 colunas no arquivo de 2024-01 (`AQAC2401.dbc`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `AP_MVM / AP_CMP` | String (AAAAMM) | Mês de movimentação (processamento) e mês de competência da APAC. |
| `AP_AUTORIZ` | String (13) | Número da APAC (chave do tratamento); `AP_APACANT` aponta a APAC anterior do mesmo paciente/tratamento. |
| `AP_CODUNI` | String (7) | Código CNES do estabelecimento executor. |
| `AP_GESTAO / AP_UFMUN` | String (6) | Código do gestor e município do estabelecimento (IBGE 6 dígitos). |
| `AP_PRIPAL` | String (10) | Procedimento principal SIGTAP da APAC. |
| `AP_VL_AP` | Float | Valor (R$) aprovado da APAC na competência. |
| `AP_CNSPCN` | String (cifrado) | CNS do paciente — gravado de forma codificada pelo DATASUS no DBF; usar apenas como chave de pareamento, não como CNS legível. |
| `AP_SEXO / AP_COIDADE / AP_NUIDADE` | String | Sexo (`M`/`F`); unidade da idade (`4` = anos) e idade. |
| `AP_RACACOR / AP_ETNIA` | String | Raça/cor (`01`–`05`, `99`) e etnia indígena. |
| `AP_MUNPCN / AP_CEPPCN` | String (6 / 8) | Município de residência e CEP do paciente. |
| `AP_DTINIC / AP_DTFIM` | String AAAAMMDD | Início e fim da validade da APAC no período. |
| `AP_DTSOLIC / AP_DTAUT` | String AAAAMMDD | Datas de solicitação e de autorização. |
| `AP_CIDPRI / AP_CIDSEC / AP_CIDCAS` | String (CID-10) | Diagnóstico principal, secundário e causas associadas (`0000` = não informado). |
| `AP_MOTSAI / AP_OBITO / AP_ALTA / AP_TRANSF / AP_PERMAN / AP_ENCERR` | String | Motivo de saída/cobrança e indicadores de óbito, alta, transferência, permanência e encerramento (flags `0`/`1`). |
| `AP_TPATEN / AP_TPAPAC` | String | Tipo de atendimento e tipo da APAC (`1` inicial, `2` continuidade, `3` única). |
| `AP_NATJUR / AP_TPUPS / AP_TIPPRE` | String | Natureza jurídica, tipo de unidade e tipo de prestador do estabelecimento. |
| `AQ_ESTADI` | String | Estadiamento clínico/patológico (TNM ou estágio agrupado). |
| `AQ_GRAHIS` | String | Grau histológico (`01`–`99`). |
| `AQ_DTIDEN / AQ_DTINTR` | String AAAAMMDD | Data de identificação patológica do câncer e data de início do tratamento. |
| `AQ_TRANTE / AQ_CONTTR` | String | Tratamento anterior e continuidade de tratamento (`S`/`N`). |
| `AQ_CIDINI1…3 / AQ_DTINI1…3` | String | CID e data de tratamentos oncológicos iniciais. |
| `AQ_ESQU_P1 / AQ_ESQU_P2` | String | Esquema quimioterápico (siglas, p.ex. `ACT`). |
| `AQ_TOTMPL / AQ_TOTMAU` | Inteiro | Meses planejados e meses já autorizados. |
| `AQ_MED01…10` | String | Medicamentos do esquema (código e/ou dose). |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Valores ausentes e sentinelas**: strings vazias e os literais `999999`, `99999999` e `00000000` (após `strip`) viram `null`; códigos `0000` de CID e `0000000000000` de AIH/APAC permanecem como texto e devem ser tratados manualmente como "não informado". Registros com marca de exclusão dBASE (`_deleted = True`) são descartados e a coluna `_deleted` é removida.
- **Preservação de códigos estruturados**: os campos de procedimento (`AP_PRIPAL`, 10 dígitos), CNES (`AP_CODUNI`), CID (`AP_CIDPRI`…), CBO e número de APAC (`AP_AUTORIZ`, 13 dígitos) **não** constam em `CODE_COLUMNS` (que usa nomes de outros sistemas, como `PA_PROC_ID`, `CNES_EXEC`, `PROC_REA`); mesmo assim chegam do DBF como `String` com zeros à esquerda e não devem ser convertidos para inteiro. Municípios são códigos IBGE de 6 dígitos (sem dígito verificador).
- **Datas e competências**: no SIA as datas usam prefixo `AP_` (`AP_DTINIC`, `AP_DTFIM`, `AP_DTSOLIC`, `AP_DTAUT`, `AP_DTOCOR`, formato `AAAAMMDD`) e **não** estão em `DATE_COLUMNS`: permanecem `String`; converta com `pl.col('ap_dtinic').str.to_date('%Y%m%d', strict=False)`. Competências (`AP_MVM`, `AP_CMP`) são `AAAAMM`.
- **Valores monetários e sentinelas**: `AP_VL_AP` já é numérico no DBF (`Float64`). O sentinela `0000000000000` em `AP_APACANT` e `0000` em CID indicam "não se aplica" e não são anulados automaticamente. Estas colunas são lidas em minúsculas (`ap_pripal`, `ap_cidpri`…).
- **Particularidades do dataset**: (i) os campos oncológicos (`AQ_*`) vêm como `String` e vazios onde não se aplicam — converta vazios para `null` e `AQ_DTIDEN`/`AQ_DTINTR` para `pl.Date`; (ii) a APAC é mensal e o mesmo paciente aparece em várias competências: conte tratamentos por `AP_AUTORIZ`/`AP_CNSPCN` e use `AP_TPAPAC` (`1` inicial, `2` continuidade); (iii) `AP_CIDPRI` é o CID do câncer — filtre `C*` para tumores malignos; (iv) municípios de residência e do estabelecimento podem ser diferentes (fluxo oncológico).

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sia-aq
quantilica datasus list sia-aq

# 2. Baixar microdados de sia-aq com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sia-aq -o ./data --start 2024-01 --end 2024-12 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sia-aq -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sia-aq -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sia-aq/202401").glob("sia-aq_ac_202401_*.dbc"))
aq = df.read_dbc(arquivo, dataset="sia-aq")

# Tempo entre identificação patológica e início do tratamento (dias)
aq = aq.with_columns(
    pl.col("aq_dtiden").str.to_date("%Y%m%d", strict=False).alias("dt_iden"),
    pl.col("aq_dtintr").str.to_date("%Y%m%d", strict=False).alias("dt_ini"),
).with_columns((pl.col("dt_ini") - pl.col("dt_iden")).dt.total_days().alias("dias_ate_tratamento"))
print(aq.select("ap_cidpri", "aq_estadi", "dias_ate_tratamento").head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
