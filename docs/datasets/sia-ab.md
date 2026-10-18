# `sia-ab` — APAC de Acompanhamento a Cirurgia Bariátrica

`sia-ab` registra as **APAC de Acompanhamento a Cirurgia Bariátrica** do SIA/SUS: cada linha é a cobrança mensal de uma APAC de seguimento de pacientes operados de obesidade grave, com os dados cadastrais da APAC e campos específicos (IMC, procedimento e data da cirurgia, AIH da cirurgia, tempo de acompanhamento).

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sia` — SIA: Sistema de Informações Ambulatoriais |
| **Código no `datasus-fetcher`** | `sia-ab` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 2008-01 a 2025-07 (conforme `index.json`; 18 UFs com arquivos; última atualização no FTP em 2026-02-10) |
| **Volume aproximado no FTP** | 635 arquivos (~16,1 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIASUS/200801_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIASUS/200801_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **acompanhamento ambulatorial pré e pós-operatório da cirurgia bariátrica** realizada pelo SUS, autorizado por APAC (laudo para APAC no estabelecimento habilitado). A unidade de análise é a **APAC por competência**. A Autorização de Procedimentos de Alta Complexidade/Custo (APAC) é o instrumento de autorização e cobrança de procedimentos ambulatoriais de alta complexidade ou de uso continuado: o tratamento é autorizado por um gestor com validade de até três competências, e cada mês de cobrança gera uma linha no arquivo. A chave do registro é o número da APAC (`AP_AUTORIZ`, 13 dígitos) combinado com a competência (`AP_CMP`/`AP_MVM`); a APAC subsequente de um mesmo tratamento referencia a anterior em `AP_APACANT`. Os campos `AB_*` ligam a APAC à internação cirúrgica (`AB_NUMAIH`, `AB_PROCAIH`, `AB_DTCIRUR`) do SIH e registram o IMC (`AB_IMC`) e o tempo de acompanhamento (`AB_MESACOM`, `AB_ANOACOM`).

No FTP o dataset cobre 2008-01 a 2025-07 e tem arquivos para 18 UFs (inventário do FTP; as demais UFs não têm arquivos publicados). A reorganização da linha de cuidado da obesidade e da cirurgia bariátrica pelo Ministério da Saúde em 2013 (Portarias GM/MS nº 424 e nº 425/2013) levou à criação da APAC específica de acompanhamento **pós-**operatório, publicada no FTP como `sia-abo` desde 2014-01; o `sia-ab` permanece como série mais antiga e de menor volume (~16 MB no total). Os campos `AB_PRCAIH2…6`/`AB_T_PRC2…6` só existem nos leiautes recentes.

Aplicações: volume de pacientes em acompanhamento por serviço e UF; perfil de IMC e idade dos operados; tempo entre a cirurgia (`AB_DTCIRUR`) e o início do acompanhamento; elo com internações do SIH para analisar complicações e reoperações (`AB_NUMAIH2`, `AB_DTCIRG2`); avaliação do cumprimento do seguimento recomendado e do gasto com a linha de cuidado da obesidade.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `AB` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `ABSP2401.dbc` — `AB` (APAC de Acompanhamento a Cirurgia Bariátrica) + `SP` (UF) + `24` (ano) + `01` (mês). Disponível em `200801_/Dados`.
- **No armazenamento local do `datasus-fetcher`**: `data/sia-ab/<AAAAMM>/sia-ab_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sia-ab/201001/sia-ab_sp_201001_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

58 colunas no arquivo de 2010-01 (`ABSP1001.dbc`): 47 campos comuns de APAC (`AP_*`) mais os campos `AB_*`.

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
| `AB_IMC` | String/Inteiro | Índice de massa corporal do paciente informado na APAC. |
| `AB_PROCAIH / AB_NUMAIH / AB_DTCIRUR` | String / String / AAAAMMDD | Procedimento SIGTAP, número da AIH e data da cirurgia bariátrica que originou o acompanhamento. |
| `AB_NUMAIH2 / AB_DTCIRG2` | String / AAAAMMDD | AIH e data de uma segunda cirurgia (reoperação), quando houver. |
| `AB_MESACOM / AB_ANOACOM` | String | Mês e ano de acompanhamento pós-operatório. |
| `AB_PONTBAR / AB_TABBARR` | String | Campos de pontuação/escala do paciente (ver Informe Técnico SIASUS). |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Valores ausentes e sentinelas**: strings vazias e os literais `999999`, `99999999` e `00000000` (após `strip`) viram `null`; códigos `0000` de CID e `0000000000000` de AIH/APAC permanecem como texto e devem ser tratados manualmente como "não informado". Registros com marca de exclusão dBASE (`_deleted = True`) são descartados e a coluna `_deleted` é removida.
- **Preservação de códigos estruturados**: os campos de procedimento (`AP_PRIPAL`, 10 dígitos), CNES (`AP_CODUNI`), CID (`AP_CIDPRI`…), CBO e número de APAC (`AP_AUTORIZ`, 13 dígitos) **não** constam em `CODE_COLUMNS` (que usa nomes de outros sistemas, como `PA_PROC_ID`, `CNES_EXEC`, `PROC_REA`); mesmo assim chegam do DBF como `String` com zeros à esquerda e não devem ser convertidos para inteiro. Municípios são códigos IBGE de 6 dígitos (sem dígito verificador).
- **Datas e competências**: no SIA as datas usam prefixo `AP_` (`AP_DTINIC`, `AP_DTFIM`, `AP_DTSOLIC`, `AP_DTAUT`, `AP_DTOCOR`, formato `AAAAMMDD`) e **não** estão em `DATE_COLUMNS`: permanecem `String`; converta com `pl.col('ap_dtinic').str.to_date('%Y%m%d', strict=False)`. Competências (`AP_MVM`, `AP_CMP`) são `AAAAMM`.
- **Valores monetários e sentinelas**: `AP_VL_AP` já é numérico no DBF (`Float64`). O sentinela `0000000000000` em `AP_APACANT` e `0000` em CID indicam "não se aplica" e não são anulados automaticamente. Estas colunas são lidas em minúsculas (`ap_pripal`, `ap_cidpri`…).
- **Particularidades do dataset**: (i) as colunas `AB_*` pertencem apenas a esta APAC e não existem em outros arquivos do SIA; (ii) combine com `sih-rd` pelo número da AIH (`AB_NUMAIH` ↔ `N_AIH`) para estudar a internação cirúrgica; (iii) o mesmo paciente aparece em várias competências — use `AP_AUTORIZ` e o CNS codificado (`AP_CNSPCN`) para contar pacientes distintos, e `AP_TPAPAC` para identificar APAC inicial/continuidade; (iv) apenas 18 UFs têm arquivos publicados; a ausência de uma UF não deve ser lida como zero casos.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sia-ab
quantilica datasus list sia-ab

# 2. Baixar microdados de sia-ab com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sia-ab -o ./data --start 2024-01 --end 2025-07 --regions sp mg

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sia-ab -o ./data --start 2024-01 --end 2025-07 --regions sp mg --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sia-ab -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2025-07 --regions sp mg
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sia-ab/201001").glob("sia-ab_sp_201001_*.dbc"))
ab = df.read_dbc(arquivo, dataset="sia-ab")

# Pacientes em acompanhamento por estabelecimento e IMC médio
resumo = (
    ab.group_by("ap_coduni")
      .agg(pl.len().alias("apacs"), pl.col("ab_imc").cast(pl.Float64, strict=False).mean().alias("imc_medio"))
      .sort("apacs", descending=True)
)
print(resumo.head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
