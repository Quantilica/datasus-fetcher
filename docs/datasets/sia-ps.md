# `sia-ps` — Psicossocial

`sia-ps` contém os registros **Psicossociais** do SIA/SUS, originados do Registro das Ações Ambulatoriais de Saúde — RAAS-PSI: cada linha é uma ação de atenção psicossocial prestada a um paciente (identificado por CNS codificado) em CAPS e demais pontos da Rede de Atenção Psicossocial, com dados de diagnóstico, origem do paciente, situação de rua, uso de drogas, local de realização e quantidade de atendimentos.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sia` — SIA: Sistema de Informações Ambulatoriais |
| **Código no `datasus-fetcher`** | `sia-ps` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 2012-11 a 2026-07 (conforme `index.json`; 27 UFs com arquivos; última atualização no FTP em 2026-09-14) |
| **Volume aproximado no FTP** | 4.394 arquivos (~3,3 GB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIASUS/200801_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIASUS/200801_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **registro de atendimento psicossocial** na RAAS (Registro das Ações Ambulatoriais de Saúde), módulo Atenção Psicossocial (RAAS-PSI), preenchido por CAPS, serviços residenciais terapêuticos, unidades de acolhimento e ambulatórios de saúde mental. A unidade de análise é o **registro de ação por paciente, procedimento e período** (`DT_INICIO`–`DT_FIM`), com `QTDATE` (quantidade de atendimentos) e `QTDPCN` (quantidade de pacientes) no leiaute.

O RAAS foi instituído em 2012 para substituir a produção em BPA/APAC de CAPS, no contexto da Rede de Atenção Psicossocial (Portaria GM/MS nº 3.088/2011). O inventário do FTP começa em 2012-11 e segue até 2026-07 (27 UFs, ~3,3 GB). Em relação ao PA, o PS oferece vínculo com a pessoa (CNS), situação de rua (`SIT_RUA`), tipo de droga (`TP_DROGA`) e `DESTINOPAC`, informações inexistentes no BPA-C.

Aplicações: perfil dos usuários de CAPS por diagnóstico (`CIDPRI`), sexo, idade e raça/cor; uso de substâncias (`TP_DROGA`) e população em situação de rua (`SIT_RUA`); origem e destino dos pacientes (`ORIGEM_PAC`, `DESTINOPAC`); cobertura de CAPS por município; intensidade do cuidado (atendimentos por paciente) e continuidade do tratamento; avaliação da desinstitucionalização e da articulação com a Atenção Básica (`COB_ESF`, `CNES_ESF`).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `PS` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `PSSP2401.dbc` — `PS` (Psicossocial / RAAS-PSI) + `SP` (UF) + `24` (ano) + `01` (mês).
- **No armazenamento local do `datasus-fetcher`**: `data/sia-ps/<AAAAMM>/sia-ps_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sia-ps/202401/sia-ps_sp_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

46 colunas no arquivo de 2024-01 (`PSAC2401.dbc`), com leiaute distinto das APACs (sem prefixo `AP_`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES_EXEC` | String (7) | CNES do estabelecimento executor (CAPS ou outro serviço). |
| `GESTAO / UFMUN` | String (6) | Código do gestor e município do estabelecimento. |
| `DT_PROCESS` | String (AAAAMM) | Competência de processamento. |
| `DT_ATEND` | String (AAAAMM) | Competência do atendimento. |
| `CNS_PAC` | String (cifrado) | CNS do paciente, codificado pelo DATASUS no DBF. |
| `DTNASC / IDADEPAC / TPIDADEPAC` | String AAAAMMDD / String / String | Data de nascimento; idade e unidade da idade do paciente. |
| `SEXOPAC / RACACOR / ETNIA` | String | Sexo (`M`/`F`), raça/cor e etnia. |
| `MUNPAC` | String (6) | Município de residência do paciente. |
| `CIDPRI / CIDASSOC` | String (CID-10) | Diagnóstico principal e associado (p.ex. `F192`). |
| `ORIGEM_PAC / DESTINOPAC` | String | Origem do paciente (demanda espontânea, UBS, internação…) e destino após o atendimento. |
| `DT_INICIO / DT_FIM / INICIO / FIM` | String AAAAMMDD | Início e fim do acompanhamento/registro. |
| `PA_PROC_ID` | String (10) | Procedimento SIGTAP realizado. |
| `PA_QTDPRO / PA_QTDAPR` | String | Quantidade produzida e aprovada (note: `String` no DBF). |
| `SIT_RUA / TP_DROGA / LOC_REALIZ` | String | Situação de rua (`S`/`N`), tipo de droga (`A` álcool, `C` crack, `O` outras…) e local de realização (`C` CAPS, território…). |
| `QTDATE / QTDPCN / PERMANEN` | String | Quantidade de atendimentos, de pacientes e permanência no serviço. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios aparecem com 6 dígitos (código IBGE sem dígito verificador, p.ex. `120040`); `wrangle_datasus` mantém como `String` `MUNIC_RES`, `MUNIC_MOV`, `CEP`, `CNES`, `PROC_REA`/`PROC_SOLIC` (SIGTAP, 10 dígitos), `DIAG_PRINC`/`DIAG_SECUN`/`DIAGSEC1–9`/`CID_NOTIF`/`CID_MORTE` (CID-10) e `N_AIH` (13 dígitos). Nunca converta esses campos para inteiro, pois os zeros à esquerda são significativos; para juntar com bases que usam 7 dígitos, calcule o dígito verificador do IBGE ou use a tabela de municípios (`TAB_*.zip`).
- **Valores ausentes e sentinelas**: strings vazias e `999999`, `99999999`, `00000000` viram `null`; registros com `_deleted = True` são descartados.
- **Datas e competências — atenção**: `DT_PROCESS` e `DT_ATEND` fazem parte de `DATE_COLUMNS` e são convertidas com formato `%Y%m%d`, mas neste dataset trazem apenas **`AAAAMM`** (6 dígitos) — a conversão estrita falha silenciosamente e **as colunas viram `null`** (verificado em `PSAC2401.dbc`: 100% nulos). Para recuperar a competência, leia com `clean=False` e converta com `pl.col('DT_PROCESS').str.to_date('%Y%m', strict=False)`. `DTNASC`, `DT_INICIO`, `DT_FIM`, `INICIO` e `FIM` (`AAAAMMDD`) não constam em `DATE_COLUMNS` e permanecem texto; converta-os com `str.to_date('%Y%m%d', strict=False)`.
- **Códigos**: `CNES_EXEC`, `CNS_PAC`, `PA_PROC_ID` e `CID*` são `String` (os três primeiros constam em `CODE_COLUMNS`); `MUNPAC`/`UFMUN` têm 6 dígitos IBGE. `SEXOPAC` é `M`/`F` (não está em `INTEGER_COLUMNS`).
- **Particularidades do dataset**: (i) em alguns arquivos o cabeçalho DBF traz o nome do campo `TIPPRE` com espaços à direita (`'TIPPRE  '`) — aplique `strip()` aos nomes das colunas antes de selecionar; (ii) `PA_QTDPRO`/`PA_QTDAPR` são texto: use `cast(pl.Int64, strict=False)`; (iii) o CNS é codificado e serve apenas para contar pacientes distintos; (iv) um mesmo paciente tem várias linhas por competência (uma por procedimento/dia).

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sia-ps
quantilica datasus list sia-ps

# 2. Baixar microdados de sia-ps com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sia-ps -o ./data --start 2024-01 --end 2024-12 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sia-ps -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sia-ps -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sia-ps/202401").glob("sia-ps_ac_202401_*.dbc"))
# clean=False para preservar DT_PROCESS/DT_ATEND (AAAAMM), que o saneamento padrão anularia
ps = df.read_dbc(arquivo, clean=False).rename(str.lower).filter(~pl.col("_deleted"))
ps = ps.with_columns(
    pl.col("dt_process").str.to_date("%Y%m", strict=False).alias("competencia"),
    pl.col("qtdate").cast(pl.Int64, strict=False),
)

# Atendimentos por CID principal e pacientes distintos
q = ps.group_by("cidpri").agg(pl.col("qtdate").sum().alias("atendimentos"), pl.col("cns_pac").n_unique().alias("pacientes"))
print(q.sort("atendimentos", descending=True).head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
- **Portaria GM/MS nº 3.088/2011** — institui a Rede de Atenção Psicossocial (RAPS): https://bvsms.saude.gov.br/bvs/saudelegis/gm/2011/prt3088_23_12_2011_rep.html
