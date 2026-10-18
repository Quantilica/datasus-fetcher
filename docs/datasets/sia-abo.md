# `sia-abo` — APAC Acompanhamento Pós Cirurgia Bariátrica

`sia-abo` registra as **APAC de Acompanhamento Pós-Cirurgia Bariátrica** do SIA/SUS: cada linha é a cobrança mensal de uma APAC que financia o seguimento multiprofissional de longo prazo do paciente após a cirurgia bariátrica, com os mesmos campos `AB_*` do `sia-ab` e campos adicionais de adesão ao seguimento.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sia` — SIA: Sistema de Informações Ambulatoriais |
| **Código no `datasus-fetcher`** | `sia-abo` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 2014-01 a 2026-07 (conforme `index.json`; 18 UFs com arquivos; última atualização no FTP em 2026-09-14) |
| **Volume aproximado no FTP** | 1.607 arquivos (~38,6 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIASUS/200801_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIASUS/200801_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **seguimento pós-operatório** (consultas, suplementação e orientação nutricional, atividade física) autorizado por APAC aos pacientes operados pelo SUS. A unidade de análise é a **APAC por competência**. A Autorização de Procedimentos de Alta Complexidade/Custo (APAC) é o instrumento de autorização e cobrança de procedimentos ambulatoriais de alta complexidade ou de uso continuado: o tratamento é autorizado por um gestor com validade de até três competências, e cada mês de cobrança gera uma linha no arquivo. A chave do registro é o número da APAC (`AP_AUTORIZ`, 13 dígitos) combinado com a competência (`AP_CMP`/`AP_MVM`); a APAC subsequente de um mesmo tratamento referencia a anterior em `AP_APACANT`. Além do IMC e do vínculo com a internação cirúrgica (`AB_NUMAIH`), o leiaute inclui comorbidades (`AP_COMORB`, `AP_CID_C1…C5`, `AP_CID_CO`), uso de medicamentos/polivitamínico (`AP_MEDICAM`, `AP_POLIVIT`), atividade física (`AP_ATV_FIS`) e adesão (`AP_ADESAO`).

No FTP cobre 2014-01 a 2026-07 e sucede o `sia-ab` na prática, após a reformulação da linha de cuidado em 2013 (Portarias GM/MS nº 424 e nº 425/2013), que determinou o acompanhamento pós-operatório obrigatório. São 79 colunas (as maiores do grupo de APACs bariátricas) e arquivos de 18 UFs. O campo `AP_NATJUR` (natureza jurídica) está presente, assim como os campos de segundo procedimento (`AB_PRCAIH2…6`, `AB_T_PRC2…6`).

Aplicações: monitoramento da adesão ao seguimento pós-bariátrico, uso de polivitamínicos e atividade física, comorbidades associadas e tempo de acompanhamento (`AB_MESACOM`/`AB_ANOACOM`); estimativa do custo da linha de cuidado; avaliação da cobertura do seguimento por serviço habilitado; análise de desfechos (`AP_OBITO`, `AP_ALTA`, `AP_TRANSF`, `AP_MOTSAI`) em estudos de coorte pós-bariátrica quando ligado ao SIH.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `ABO` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `ABOSP2401.dbc` — `ABO` (APAC Acompanhamento Pós-Cirurgia Bariátrica) + `SP` (UF) + `24` (ano) + `01` (mês). Prefixo de 3 letras: não confunda com `AB`.
- **No armazenamento local do `datasus-fetcher`**: `data/sia-abo/<AAAAMM>/sia-abo_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sia-abo/202401/sia-abo_ac_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

79 colunas no arquivo de 2024-01 (`ABOAC2401.dbc`): campos comuns `AP_*` mais `AB_*` e indicadores de seguimento.

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
| `AB_IMC` | String/Inteiro | Índice de massa corporal do paciente. |
| `AB_PROCAIH / AB_NUMAIH / AB_DTCIRUR` | String / String / AAAAMMDD | Procedimento, AIH e data da cirurgia bariátrica de origem. |
| `AB_PRCAIH2…6 / AB_T_PRC2…6` | String | Procedimentos adicionais da internação cirúrgica e respectivos tipos. |
| `AB_MESACOM / AB_ANOACOM` | String | Mês e ano de acompanhamento pós-operatório. |
| `AP_COMORB / AP_CID_C1…C5 / AP_CID_CO` | String | Indicador de comorbidade (`S`/`N`) e CIDs das comorbidades. |
| `AP_MEDICAM / AP_POLIVIT / AP_ATV_FIS / AP_REG_PES / AP_ADESAO` | String | Indicadores (códigos do Informe Técnico) de uso de medicamentos, polivitamínico, atividade física, registro de peso e adesão ao seguimento. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Valores ausentes e sentinelas**: strings vazias e os literais `999999`, `99999999` e `00000000` (após `strip`) viram `null`; códigos `0000` de CID e `0000000000000` de AIH/APAC permanecem como texto e devem ser tratados manualmente como "não informado". Registros com marca de exclusão dBASE (`_deleted = True`) são descartados e a coluna `_deleted` é removida.
- **Preservação de códigos estruturados**: os campos de procedimento (`AP_PRIPAL`, 10 dígitos), CNES (`AP_CODUNI`), CID (`AP_CIDPRI`…), CBO e número de APAC (`AP_AUTORIZ`, 13 dígitos) **não** constam em `CODE_COLUMNS` (que usa nomes de outros sistemas, como `PA_PROC_ID`, `CNES_EXEC`, `PROC_REA`); mesmo assim chegam do DBF como `String` com zeros à esquerda e não devem ser convertidos para inteiro. Municípios são códigos IBGE de 6 dígitos (sem dígito verificador).
- **Datas e competências**: no SIA as datas usam prefixo `AP_` (`AP_DTINIC`, `AP_DTFIM`, `AP_DTSOLIC`, `AP_DTAUT`, `AP_DTOCOR`, formato `AAAAMMDD`) e **não** estão em `DATE_COLUMNS`: permanecem `String`; converta com `pl.col('ap_dtinic').str.to_date('%Y%m%d', strict=False)`. Competências (`AP_MVM`, `AP_CMP`) são `AAAAMM`.
- **Valores monetários e sentinelas**: `AP_VL_AP` já é numérico no DBF (`Float64`). O sentinela `0000000000000` em `AP_APACANT` e `0000` em CID indicam "não se aplica" e não são anulados automaticamente. Estas colunas são lidas em minúsculas (`ap_pripal`, `ap_cidpri`…).
- **Particularidades do dataset**: (i) é o conjunto "vivo" de seguimento pós-bariátrico, com a mesma lógica de APAC por competência do `sia-ab`; (ii) trate `AB_*` e `AP_*` vazios (`''`) como `null` — muitos campos só são preenchidos em determinadas APAC; (iii) os indicadores `AP_COMORB`, `AP_MEDICAM`, `AP_POLIVIT`, `AP_ATV_FIS`, `AP_REG_PES`, `AP_ADESAO` são códigos de domínio (consulte o Informe Técnico antes de interpretá-los como booleanos); (iv) para contar pacientes use `AP_CNSPCN` (codificado) e não a quantidade de linhas.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sia-abo
quantilica datasus list sia-abo

# 2. Baixar microdados de sia-abo com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sia-abo -o ./data --start 2023-01 --end 2024-12 --regions ac sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sia-abo -o ./data --start 2023-01 --end 2024-12 --regions ac sp --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sia-abo -o ./data/raw --parquet-dir ./data/parquet --start 2023-01 --end 2024-12 --regions ac sp
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sia-abo/202401").glob("sia-abo_ac_202401_*.dbc"))
abo = df.read_dbc(arquivo, dataset="sia-abo")

# Adesão ao seguimento e valor aprovado por estabelecimento
adesao = (
    abo.group_by("ap_adesao")
       .agg(pl.len().alias("apacs"), pl.col("ap_vl_ap").sum().alias("valor"))
       .sort("apacs", descending=True)
)
print(adesao)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
