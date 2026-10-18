# `sia-acf` — APAC Confeção de Fístula Arteriovenosa

`sia-acf` contém as **APAC de Confecção de Fístula Arteriovenosa** do SIA/SUS: cada linha é a cobrança de uma APAC para a confecção/revisão de acesso vascular (fístula arteriovenosa) de pacientes em terapia renal substitutiva, com campos clínicos do procedimento (duplex, uso prévio de cateter, complicações).

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sia` — SIA: Sistema de Informações Ambulatoriais |
| **Código no `datasus-fetcher`** | `sia-acf` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 2014-08 a 2026-07 (conforme `index.json`; 27 UFs com arquivos; última atualização no FTP em 2026-09-14) |
| **Volume aproximado no FTP** | 3.768 arquivos (~32,3 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIASUS/200801_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIASUS/200801_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é a **cirurgia ambulatorial de confecção de fístula arteriovenosa (FAV)** para hemodiálise, autorizada por APAC específica. A unidade de análise é a **APAC por competência**. A Autorização de Procedimentos de Alta Complexidade/Custo (APAC) é o instrumento de autorização e cobrança de procedimentos ambulatoriais de alta complexidade ou de uso continuado: o tratamento é autorizado por um gestor com validade de até três competências, e cada mês de cobrança gera uma linha no arquivo. A chave do registro é o número da APAC (`AP_AUTORIZ`, 13 dígitos) combinado com a competência (`AP_CMP`/`AP_MVM`); a APAC subsequente de um mesmo tratamento referencia a anterior em `AP_APACANT`. Os campos `ACF_*` registram achados do pré e pós-operatório: realização de duplex, uso prévio de cateter, FAV prévia, flebite, hematoma, diâmetro de veia/artéria, frêmito e pulso.

No FTP cobre 2014-08 a 2026-07 (27 UFs). A APAC específica foi criada na reorganização da assistência à doença renal crônica de 2014, simultaneamente à APAC de Tratamento Dialítico (`sia-atd`, também a partir de 2014-08), que sucedeu a antiga APAC de Nefrologia (`sia-an`, até 2014-10). Só existem 57 colunas e o volume é pequeno (~32 MB).

Aplicações: acesso vascular definitivo vs. cateter na terapia renal substitutiva; taxa de FAV por UF/serviço; complicações pós-operatórias (hematoma, flebite); tempo entre início da diálise e confecção da fístula (cruzando com `sia-atd`); gasto com acesso vascular e qualidade do cuidado nefrológico.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `ACF` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `ACFSP2401.dbc` — `ACF` (APAC Confecção de Fístula Arteriovenosa) + `SP` (UF) + `24` + `01`.
- **No armazenamento local do `datasus-fetcher`**: `data/sia-acf/<AAAAMM>/sia-acf_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sia-acf/202401/sia-acf_ac_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

57 colunas no arquivo de 2024-01 (`ACFAC2401.dbc`).

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
| `ACF_DUPLEX` | String (`S`/`N`) | Realização de duplex (ultrassom Doppler) de mapeamento vascular. |
| `ACF_USOCAT` | String (`S`/`N`) | Uso prévio de cateter para diálise. |
| `ACF_PREFAV` | String (`S`/`N`) | Existência de fístula arteriovenosa prévia. |
| `ACF_FLEBIT / ACF_HEMATO` | String (`S`/`N`) | Ocorrência de flebite e de hematoma. |
| `ACF_VEIAVI / ACF_VEIDIA / ACF_ARTDIA` | String | Veia utilizada e diâmetros (mm, em faixas) de veia e artéria (ver Informe Técnico). |
| `ACF_PULSO / ACF_FREMIT` | String | Pulso e frêmito da fístula após a cirurgia. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Valores ausentes e sentinelas**: strings vazias e os literais `999999`, `99999999` e `00000000` (após `strip`) viram `null`; códigos `0000` de CID e `0000000000000` de AIH/APAC permanecem como texto e devem ser tratados manualmente como "não informado". Registros com marca de exclusão dBASE (`_deleted = True`) são descartados e a coluna `_deleted` é removida.
- **Preservação de códigos estruturados**: os campos de procedimento (`AP_PRIPAL`, 10 dígitos), CNES (`AP_CODUNI`), CID (`AP_CIDPRI`…), CBO e número de APAC (`AP_AUTORIZ`, 13 dígitos) **não** constam em `CODE_COLUMNS` (que usa nomes de outros sistemas, como `PA_PROC_ID`, `CNES_EXEC`, `PROC_REA`); mesmo assim chegam do DBF como `String` com zeros à esquerda e não devem ser convertidos para inteiro. Municípios são códigos IBGE de 6 dígitos (sem dígito verificador).
- **Datas e competências**: no SIA as datas usam prefixo `AP_` (`AP_DTINIC`, `AP_DTFIM`, `AP_DTSOLIC`, `AP_DTAUT`, `AP_DTOCOR`, formato `AAAAMMDD`) e **não** estão em `DATE_COLUMNS`: permanecem `String`; converta com `pl.col('ap_dtinic').str.to_date('%Y%m%d', strict=False)`. Competências (`AP_MVM`, `AP_CMP`) são `AAAAMM`.
- **Valores monetários e sentinelas**: `AP_VL_AP` já é numérico no DBF (`Float64`). O sentinela `0000000000000` em `AP_APACANT` e `0000` em CID indicam "não se aplica" e não são anulados automaticamente. Estas colunas são lidas em minúsculas (`ap_pripal`, `ap_cidpri`…).
- **Particularidades do dataset**: (i) as descrições dos campos `ACF_*` foram interpretadas a partir dos nomes e do Informe Técnico do SIASUS; valide os domínios (`S`/`N` ou faixas numéricas) antes de usar como indicadores; (ii) a coluna `AP_TIPPRE` aparece com grafia diferente de `AP_TPPRE` em alguns leiautes — normalize nomes ao empilhar anos; (iii) os campos `AP_DTOCOR`/`AP_APACANT` seguem o mesmo padrão de APAC; (iv) como o dataset é pequeno, a leitura de todo o histórico para uma UF é viável em memória.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sia-acf
quantilica datasus list sia-acf

# 2. Baixar microdados de sia-acf com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sia-acf -o ./data --start 2023-01 --end 2024-12 --regions ac sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sia-acf -o ./data --start 2023-01 --end 2024-12 --regions ac sp --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sia-acf -o ./data/raw --parquet-dir ./data/parquet --start 2023-01 --end 2024-12 --regions ac sp
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sia-acf/202401").glob("sia-acf_ac_202401_*.dbc"))
acf = df.read_dbc(arquivo, dataset="sia-acf")

# Fístulas realizadas com/sem uso prévio de cateter e valor aprovado
tabela = acf.group_by("acf_usocat").agg(pl.len().alias("apacs"), pl.col("ap_vl_ap").sum().alias("valor"))
print(tabela)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
