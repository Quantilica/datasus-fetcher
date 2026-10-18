# `sia-atd` — APAC de Tratamento Dialítico

`sia-atd` contém as **APAC de Tratamento Dialítico** do SIA/SUS: cada linha é a cobrança mensal de uma APAC de terapia renal substitutiva (hemodiálise e diálise peritoneal), com indicadores laboratoriais e de qualidade da diálise. Substitui, a partir de 2014-08, a antiga APAC de Nefrologia (`sia-an`).

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sia` — SIA: Sistema de Informações Ambulatoriais |
| **Código no `datasus-fetcher`** | `sia-atd` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 2014-08 a 2026-07 (conforme `index.json`; 27 UFs com arquivos; última atualização no FTP em 2026-09-14) |
| **Volume aproximado no FTP** | 3.884 arquivos (~1,1 GB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIASUS/200801_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIASUS/200801_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **tratamento dialítico de pacientes com doença renal crônica**, autorizado por APAC específica criada na reorganização de 2014. A unidade de análise é a **APAC por competência**. A Autorização de Procedimentos de Alta Complexidade/Custo (APAC) é o instrumento de autorização e cobrança de procedimentos ambulatoriais de alta complexidade ou de uso continuado: o tratamento é autorizado por um gestor com validade de até três competências, e cada mês de cobrança gera uma linha no arquivo. A chave do registro é o número da APAC (`AP_AUTORIZ`, 13 dígitos) combinado com a competência (`AP_CMP`/`AP_MVM`); a APAC subsequente de um mesmo tratamento referencia a anterior em `AP_APACANT`. Os campos `ATD_*` registram hemoglobina, fósforo, Kt/V semanal (`ATD_KTVSEM`), taxa de redução da ureia (`ATD_TRU`), albumina, paratormônio (`ATD_PTH`), sorologias (HIV, HCV, HBsAg), acesso vascular (`ATD_ACEVAS`) e intercorrências (`ATD_INTERC`, `ATD_SEPERI`).

No FTP cobre 2014-08 a 2026-07 (27 UFs, ~1,05 GB). Em 2014 foi reorganizada a Linha de Cuidado da Doença Renal Crônica, com criação de APAC específicas (diálise e fístula) em substituição à APAC de nefrologia (`sia-an`, até 2014-10). A base continua ativa e é a principal fonte administrativa da terapia renal substitutiva no SUS.

Aplicações: prevalência de pacientes em diálise por UF/serviço; indicadores de qualidade (Kt/V, TRU, hemoglobina, fósforo, PTH, albumina) conforme metas regulatórias; proporção de acesso vascular definitivo; cobertura de sorologias; gasto com TRS; e série histórica concatenando `sia-an` (2008–2014) e `sia-atd` (2014 em diante).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `ATD` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `ATDSP2401.dbc` — `ATD` (APAC de Tratamento Dialítico) + `SP` (UF) + `24` + `01`. Prefixo de 3 letras.
- **No armazenamento local do `datasus-fetcher`**: `data/sia-atd/<AAAAMM>/sia-atd_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sia-atd/202401/sia-atd_ac_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

66 colunas no arquivo de 2024-01 (`ATDAC2401.dbc`).

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
| `ATD_CARACT` | String | Caráter do atendimento/tratamento dialítico. |
| `ATD_DTPDR / ATD_DTCLI` | String AAAAMMDD | Datas de referência do tratamento (início da terapia e de ingresso na clínica; ver Informe Técnico). |
| `ATD_ACEVAS` | String | Acesso vascular utilizado. |
| `ATD_HB / ATD_FOSFOR / ATD_PTH / ATD_ALBUMI` | String | Hemoglobina, fósforo, paratormônio e albumina. |
| `ATD_KTVSEM / ATD_TRU` | String | Kt/V semanal e taxa de redução da ureia. |
| `ATD_HIV / ATD_HCV / ATD_HBSAG` | String (`S`/`N`) | Sorologias. |
| `ATD_SITTRA / ATD_INTERC / ATD_SEPERI` | String | Situação de transplante e intercorrências/separação do tratamento (domínios do Informe Técnico). |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Valores ausentes e sentinelas**: strings vazias e os literais `999999`, `99999999` e `00000000` (após `strip`) viram `null`; códigos `0000` de CID e `0000000000000` de AIH/APAC permanecem como texto e devem ser tratados manualmente como "não informado". Registros com marca de exclusão dBASE (`_deleted = True`) são descartados e a coluna `_deleted` é removida.
- **Preservação de códigos estruturados**: os campos de procedimento (`AP_PRIPAL`, 10 dígitos), CNES (`AP_CODUNI`), CID (`AP_CIDPRI`…), CBO e número de APAC (`AP_AUTORIZ`, 13 dígitos) **não** constam em `CODE_COLUMNS` (que usa nomes de outros sistemas, como `PA_PROC_ID`, `CNES_EXEC`, `PROC_REA`); mesmo assim chegam do DBF como `String` com zeros à esquerda e não devem ser convertidos para inteiro. Municípios são códigos IBGE de 6 dígitos (sem dígito verificador).
- **Datas e competências**: no SIA as datas usam prefixo `AP_` (`AP_DTINIC`, `AP_DTFIM`, `AP_DTSOLIC`, `AP_DTAUT`, `AP_DTOCOR`, formato `AAAAMMDD`) e **não** estão em `DATE_COLUMNS`: permanecem `String`; converta com `pl.col('ap_dtinic').str.to_date('%Y%m%d', strict=False)`. Competências (`AP_MVM`, `AP_CMP`) são `AAAAMM`.
- **Valores monetários e sentinelas**: `AP_VL_AP` já é numérico no DBF (`Float64`). O sentinela `0000000000000` em `AP_APACANT` e `0000` em CID indicam "não se aplica" e não são anulados automaticamente. Estas colunas são lidas em minúsculas (`ap_pripal`, `ap_cidpri`…).
- **Particularidades do dataset**: (i) para séries anteriores a 2014-08 use `sia-an`; na janela 2014-08 a 2014-10 ambos coexistem; (ii) valores laboratoriais `0` ou vazio significam "não informado" e devem ser tratados como `null` antes de calcular médias; (iii) a descrição dos campos `ATD_*` baseia-se nos nomes e no Informe Técnico — valide os domínios; (iv) `AP_TPAPAC` distingue APAC inicial de continuidade.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sia-atd
quantilica datasus list sia-atd

# 2. Baixar microdados de sia-atd com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sia-atd -o ./data --start 2024-01 --end 2024-12 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sia-atd -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sia-atd -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sia-atd/202401").glob("sia-atd_ac_202401_*.dbc"))
atd = df.read_dbc(arquivo, dataset="sia-atd")

# Hemoglobina média (excluindo zeros = não informado) e valor aprovado por estabelecimento
q = (
    atd.with_columns(pl.col("atd_hb").cast(pl.Float64, strict=False).replace(0.0, None))
       .group_by("ap_coduni")
       .agg(pl.len().alias("apacs"), pl.col("atd_hb").mean().alias("hb_media"), pl.col("ap_vl_ap").sum().alias("valor"))
       .sort("apacs", descending=True)
)
print(q.head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
