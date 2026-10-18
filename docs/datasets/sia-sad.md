# `sia-sad` — Atenção Domiciliar

`sia-sad` reúne os registros de **Atenção Domiciliar** do SIA/SUS, originados da RAAS-AD (Registro das Ações Ambulatoriais de Saúde — Atenção Domiciliar) entre 2012 e 2018: cada linha é uma ação de assistência domiciliar a um paciente (CNS codificado), com equipe, CID, origem do paciente e quantidades.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sia` — SIA: Sistema de Informações Ambulatoriais |
| **Código no `datasus-fetcher`** | `sia-sad` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 2012-04 a 2018-10 (conforme `index.json`; 25 UFs com arquivos; última atualização no FTP em 2020-01-10) |
| **Volume aproximado no FTP** | 1.088 arquivos (~53,4 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIASUS/200801_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIASUS/200801_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **atendimento domiciliar** prestado por equipes do Programa Melhor em Casa (EMAD/EMAP) e serviços de atenção domiciliar, registrado na RAAS-AD. A unidade de análise é o **registro de ação por paciente, procedimento e período** (`DT_INICIO`–`DT_FIM`), com `QTDATE` e `QTDPCN`; os campos `PA_EQUIPE`/`PA_TP_EQP` identificam a equipe e `PA_CID` o CID do atendimento.

O FTP só traz competências de 2012-04 a 2018-10 (25 UFs, ~53 MB; última atualização em 2020): é um dataset **descontinuado** na publicação do SIA. A atenção domiciliar foi regulamentada pelo SUS a partir da Portaria GM/MS nº 2.527/2011 e redefinida na Portaria GM/MS nº 825/2016 (Programa Melhor em Casa). Depois de 2018 os registros não são mais publicados neste arquivo; consulte o `sia-pa` e o e-SUS/SISAB para a atenção domiciliar mais recente.

Aplicações: cobertura e produção de equipes de atenção domiciliar por município; perfil dos usuários (CID, idade, sexo); substituição de internações por atendimento domiciliar (cruzar com `sih-rd`); intensidade do cuidado; distribuição de EMAD/EMAP; e avaliação do Programa Melhor em Casa.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `SAD` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `SADSP1401.dbc` — `SAD` (Atenção Domiciliar / RAAS-AD) + `SP` (UF) + `14` (ano 2014) + `01` (mês). Prefixo de 3 letras.
- **No armazenamento local do `datasus-fetcher`**: `data/sia-sad/<AAAAMM>/sia-sad_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sia-sad/201401/sia-sad_sp_201401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

44 colunas no arquivo de 2014-01 (`SADAC1401.dbc`), com o mesmo leiaute-base do `sia-ps` e campos próprios de equipe.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES_EXEC` | String (7) | CNES do estabelecimento executor. |
| `GESTAO / UFMUN` | String (6) | Código do gestor e município do estabelecimento. |
| `DT_PROCESS / DT_ATEND` | String (AAAAMM) | Competência de processamento e do atendimento. |
| `CNS_PAC` | String (cifrado) | CNS do paciente, codificado. |
| `DTNASC / IDADEPAC / TPIDADEPAC` | String | Data de nascimento (`AAAAMMDD`), idade e unidade da idade. |
| `SEXOPAC / RACACOR` | String | Sexo (`M`/`F`) e raça/cor. |
| `MUNPAC` | String (6) | Município de residência do paciente. |
| `CIDPRI / CIDASSOC / PA_CID` | String (CID-10) | Diagnóstico principal, associado e CID do atendimento. |
| `ORIGEM_PAC / DESTINOPAC` | String | Origem do paciente e destino após a atenção domiciliar. |
| `DT_INICIO / DT_FIM` | String AAAAMMDD | Início e fim da assistência. |
| `PA_PROC_ID` | String (10) | Procedimento SIGTAP (visita domiciliar, atendimento fisioterapêutico, etc.). |
| `PA_QTDPRO / PA_QTDAPR` | String | Quantidade produzida e aprovada. |
| `PA_EQUIPE / PA_TP_EQP` | String | Equipe (INE) e tipo de equipe (EMAD, EMAP). |
| `QTDATE / QTDPCN` | String | Quantidade de atendimentos e de pacientes. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios aparecem com 6 dígitos (código IBGE sem dígito verificador, p.ex. `120040`); `wrangle_datasus` mantém como `String` `MUNIC_RES`, `MUNIC_MOV`, `CEP`, `CNES`, `PROC_REA`/`PROC_SOLIC` (SIGTAP, 10 dígitos), `DIAG_PRINC`/`DIAG_SECUN`/`DIAGSEC1–9`/`CID_NOTIF`/`CID_MORTE` (CID-10) e `N_AIH` (13 dígitos). Nunca converta esses campos para inteiro, pois os zeros à esquerda são significativos; para juntar com bases que usam 7 dígitos, calcule o dígito verificador do IBGE ou use a tabela de municípios (`TAB_*.zip`).
- **Valores ausentes e sentinelas**: strings vazias e `999999`, `99999999`, `00000000` viram `null`; registros `_deleted = True` são descartados.
- **Datas e competências — atenção**: como no `sia-ps`, `DT_PROCESS` e `DT_ATEND` estão em `DATE_COLUMNS`, mas o dado nativo é `AAAAMM`; o parse com `%Y%m%d` resulta em `null`. Recupere a competência lendo com `clean=False` e usando `str.to_date('%Y%m')`. `DT_INICIO`/`DT_FIM`/`DTNASC` (`AAAAMMDD`) ficam como texto.
- **Particularidades do dataset**: (i) série **encerrada** em 2018-10; (ii) 25 UFs com arquivos; (iii) `PA_QTDPRO`/`PA_QTDAPR`/`QTDATE`/`QTDPCN` são texto — converta para `Int64`; (iv) o CNS é codificado, serve apenas para contar pacientes distintos.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sia-sad
quantilica datasus list sia-sad

# 2. Baixar microdados de sia-sad com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sia-sad -o ./data --start 2014-01 --end 2018-10 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sia-sad -o ./data --start 2014-01 --end 2018-10 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sia-sad -o ./data/raw --parquet-dir ./data/parquet --start 2014-01 --end 2018-10 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sia-sad/201401").glob("sia-sad_ac_201401_*.dbc"))
sad = df.read_dbc(arquivo, clean=False).rename(str.lower).filter(~pl.col("_deleted"))
sad = sad.with_columns(
    pl.col("dt_process").str.to_date("%Y%m", strict=False).alias("competencia"),
    pl.col("qtdate").cast(pl.Int64, strict=False),
)

# Atendimentos domiciliares por CID principal
q = sad.group_by("cidpri").agg(pl.col("qtdate").sum().alias("atendimentos"), pl.col("cns_pac").n_unique().alias("pacientes"))
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
- **Portarias GM/MS nº 2.527/2011 e nº 825/2016** (Atenção Domiciliar / Programa Melhor em Casa), na Biblioteca Virtual em Saúde: https://bvsms.saude.gov.br/
