# `sia-an` — APAC de Nefrologia

`sia-an` guarda as **APAC de Nefrologia** (Terapia Renal Substitutiva) do SIA/SUS entre 2008 e 2014: cada linha é a cobrança mensal de uma APAC de diálise (hemodiálise ou diálise peritoneal), com parâmetros laboratoriais e clínicos do paciente renal crônico.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sia` — SIA: Sistema de Informações Ambulatoriais |
| **Código no `datasus-fetcher`** | `sia-an` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 2008-01 a 2014-10 (conforme `index.json`; 27 UFs com arquivos; última atualização no FTP em 2019-06-07) |
| **Volume aproximado no FTP** | 2.145 arquivos (~458,8 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIASUS/200801_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIASUS/200801_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **tratamento dialítico de pacientes com doença renal crônica**, autorizado por APAC de nefrologia. A unidade de análise é a **APAC por competência**. A Autorização de Procedimentos de Alta Complexidade/Custo (APAC) é o instrumento de autorização e cobrança de procedimentos ambulatoriais de alta complexidade ou de uso continuado: o tratamento é autorizado por um gestor com validade de até três competências, e cada mês de cobrança gera uma linha no arquivo. A chave do registro é o número da APAC (`AP_AUTORIZ`, 13 dígitos) combinado com a competência (`AP_CMP`/`AP_MVM`); a APAC subsequente de um mesmo tratamento referencia a anterior em `AP_APACANT`. Os campos `AN_*` registram peso, altura, diurese residual, glicemia, hematócrito/hemoglobina (`AN_HB`), albumina, taxa de redução de ureia (`AN_TRU`), sorologias (HIV, HBsAg, HCV) e acesso vascular (`AN_ACEVAS`).

É um dataset **descontinuado**: o FTP traz arquivos de 2008-01 a 2014-10 (27 UFs, ~0,46 GB, última atualização em 2019). Em 2014 a assistência à doença renal crônica foi reorganizada e a APAC de nefrologia foi substituída pelas APAC de Tratamento Dialítico (`sia-atd`, desde 2014-08) e de Confecção de Fístula (`sia-acf`), havendo sobreposição de competências entre 2014-08 e 2014-10 no FTP — para séries longas, combine `sia-an` e `sia-atd` e evite duplicidade nessa janela.

Aplicações: prevalência de pacientes em terapia renal substitutiva por UF; qualidade da diálise (TRU, albumina, hemoglobina); proporção de acesso vascular definitivo vs. cateter; sorologias em serviços de diálise; evolução histórica do gasto com TRS; série longa de 2008–2014 antes do `sia-atd`.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `AN` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `ANSP1401.dbc` — `AN` (APAC de Nefrologia) + `SP` (UF) + `14` (ano 2014) + `01` (mês). Último período publicado: `1410`.
- **No armazenamento local do `datasus-fetcher`**: `data/sia-an/<AAAAMM>/sia-an_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sia-an/201401/sia-an_ac_201401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

61 colunas no arquivo de 2014-01 (`ANAC1401.dbc`).

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
| `AN_DTPDR` | String AAAAMMDD | Data de início da terapia dialítica (primeira diálise). |
| `AN_ALTURA / AN_PESO` | String | Altura (cm) e peso (kg) do paciente. |
| `AN_DIURES / AN_GLICOS` | String | Diurese residual (mL/dia) e glicemia. |
| `AN_HB / AN_ALBUMI / AN_TRU` | String | Hemoglobina, albumina e taxa de redução da ureia. |
| `AN_HCV / AN_HBSAG / AN_HIV` | String (`S`/`N`) | Resultados de sorologias (hepatite C, hepatite B, HIV). |
| `AN_ACEVAS / AN_ULSOAB / AN_CNCDO / AN_INTFIS` | String | Acesso vascular e indicadores clínicos/funcionais registrados na APAC (ver Informe Técnico). |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Valores ausentes e sentinelas**: strings vazias e os literais `999999`, `99999999` e `00000000` (após `strip`) viram `null`; códigos `0000` de CID e `0000000000000` de AIH/APAC permanecem como texto e devem ser tratados manualmente como "não informado". Registros com marca de exclusão dBASE (`_deleted = True`) são descartados e a coluna `_deleted` é removida.
- **Preservação de códigos estruturados**: os campos de procedimento (`AP_PRIPAL`, 10 dígitos), CNES (`AP_CODUNI`), CID (`AP_CIDPRI`…), CBO e número de APAC (`AP_AUTORIZ`, 13 dígitos) **não** constam em `CODE_COLUMNS` (que usa nomes de outros sistemas, como `PA_PROC_ID`, `CNES_EXEC`, `PROC_REA`); mesmo assim chegam do DBF como `String` com zeros à esquerda e não devem ser convertidos para inteiro. Municípios são códigos IBGE de 6 dígitos (sem dígito verificador).
- **Datas e competências**: no SIA as datas usam prefixo `AP_` (`AP_DTINIC`, `AP_DTFIM`, `AP_DTSOLIC`, `AP_DTAUT`, `AP_DTOCOR`, formato `AAAAMMDD`) e **não** estão em `DATE_COLUMNS`: permanecem `String`; converta com `pl.col('ap_dtinic').str.to_date('%Y%m%d', strict=False)`. Competências (`AP_MVM`, `AP_CMP`) são `AAAAMM`.
- **Valores monetários e sentinelas**: `AP_VL_AP` já é numérico no DBF (`Float64`). O sentinela `0000000000000` em `AP_APACANT` e `0000` em CID indicam "não se aplica" e não são anulados automaticamente. Estas colunas são lidas em minúsculas (`ap_pripal`, `ap_cidpri`…).
- **Particularidades do dataset**: (i) série encerrada em 2014-10: não espere novos arquivos; (ii) para continuidade temporal, concatene com `sia-atd` removendo a sobreposição de 2014-08 a 2014-10 (use `AP_AUTORIZ` + competência); (iii) as sorologias e exames estão em `String` — converta valores numéricos com `cast(strict=False)` e trate zeros/espaços como "não realizado"; (iv) o dataset tem arquivos nos 27 UFs, mas o volume pequeno (≈ 2.145 arquivos) permite leitura integral.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sia-an
quantilica datasus list sia-an

# 2. Baixar microdados de sia-an com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sia-an -o ./data --start 2013-01 --end 2014-10 --regions ac sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sia-an -o ./data --start 2013-01 --end 2014-10 --regions ac sp --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sia-an -o ./data/raw --parquet-dir ./data/parquet --start 2013-01 --end 2014-10 --regions ac sp
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sia-an/201401").glob("sia-an_ac_201401_*.dbc"))
an = df.read_dbc(arquivo, dataset="sia-an")

# Hemoglobina média (campo AN_HB) por estabelecimento
hb = (
    an.with_columns(pl.col("an_hb").cast(pl.Float64, strict=False))
      .group_by("ap_coduni")
      .agg(pl.len().alias("apacs"), pl.col("an_hb").mean().alias("hb_media"))
      .sort("apacs", descending=True)
)
print(hb.head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
