# `sia-pa` — Produção Ambulatorial

`sia-pa` é a **Produção Ambulatorial** do SIA/SUS: o arquivo principal e mais volumoso do sistema, em que cada linha agrega a produção aprovada de um procedimento SIGTAP em um estabelecimento, por competência, ocupação (CBO), faixa etária, sexo, município de residência e demais atributos, consolidando BPA (consolidado e individualizado) e a produção das APAC e RAAS processadas.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sia` — SIA: Sistema de Informações Ambulatoriais |
| **Código no `datasus-fetcher`** | `sia-pa` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 1994-07 a 2026-07 (conforme `index.json`; 27 UFs com arquivos; última atualização no FTP em 2026-09-17) |
| **Volume aproximado no FTP** | 10.828 arquivos (~218,2 GB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIASUS/200801_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIASUS/200801_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **atendimento ambulatorial registrado** no Boletim de Produção Ambulatorial — BPA-C (consolidado: contagens por procedimento, CBO e idade) e BPA-I (individualizado: um registro por atendimento, com CNS do paciente) — e nas APAC/RAAS, todos validados e valorados pelo SIA. A unidade de análise do PA não é o paciente nem o atendimento, e sim a **linha de produção aprovada** (procedimento × estabelecimento × CBO × idade/sexo/município × competência) com quantidade (`PA_QTDPRO`/`PA_QTDAPR`) e valor (`PA_VALPRO`/`PA_VALAPR`) produzidos e aprovados.

O FTP traz duas séries: 1994-07 a 2007-12 (diretório `199407_200712`, leiaute antigo do SIA-SUS com tabela de procedimentos de 8 dígitos) e 2008-01 em diante (`200801_`, Tabela Unificada SIGTAP, 10 dígitos). Para UFs e meses de grande volume, os arquivos de 2008 em diante podem ser divididos em partes com sufixo de letra (`PASP2401a.dbc`, `…b.dbc`, …), como indicado no padrão de nome. Em 2008 a SIGTAP unificou SIA e SIH; o leiaute de 61 campos (2024) inclui indicadores de aprovação (`PA_INDICA`, `PA_CODOCO`), diferenças de valor (`PA_DIF_VAL`) e incentivos (`PA_VL_CF`, `PA_VL_CL`, `PA_VL_INC`). Os arquivos somam cerca de 218 GB.

Aplicações: produção ambulatorial por procedimento, grupo/subgrupo/forma de organização SIGTAP, estabelecimento, município e CBO; cobertura de ações de atenção básica registradas no SIA; consultas especializadas e exames de apoio diagnóstico por 1.000 habitantes; gasto ambulatorial do SUS (`PA_VALAPR`); fluxo de pacientes entre municípios (`PA_MUNPCN` vs. `PA_UFMUN`); avaliação da oferta de serviços para o Plano Diretor de Regionalização e para a programação pactuada e integrada.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/199407_200712/Dados` | `PA` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |
| `/dissemin/publicos/SIASUS/200801_/Dados` | `PA` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) + sufixo opcional de 1 letra (`a`, `b`, `c`…) quando a UF/mês é dividida em mais de um arquivo | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `PASP2401a.dbc` — `PA` (Produção Ambulatorial) + `SP` (UF) + `24` (ano) + `01` (mês) + `a` (parte do arquivo, opcional a partir de 2008). Para a série antiga (1994–2007): `PAAC9407.dbc` (sem sufixo).
- **No armazenamento local do `datasus-fetcher`**: `data/sia-pa/<AAAAMM>/sia-pa_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sia-pa/202401/sia-pa_sp_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

61 colunas no arquivo de 2024-01 (`PAAC2401.dbc`); o leiaute anterior a 2008 tem menos campos.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `PA_CODUNI` | String (7) | Código CNES do estabelecimento executor. |
| `PA_GESTAO / PA_UFMUN` | String (6) | Código do gestor e município do estabelecimento (IBGE 6 dígitos). |
| `PA_MVM / PA_CMP` | String (AAAAMM) | Mês de movimentação (processamento) e mês de competência da produção. |
| `PA_PROC_ID` | String (10) | Procedimento SIGTAP da produção (campo preservado como `String`). |
| `PA_CBOCOD` | String (6) | CBO da ocupação do profissional executor. |
| `PA_CIDPRI / PA_CIDSEC / PA_CIDCAS` | String (CID-10) | Diagnóstico principal, secundário e causas associadas (`0000` = não informado). |
| `PA_IDADE / IDADEMIN / IDADEMAX / PA_FLIDADE` | String | Idade informada (`999` = ignorada) e faixa de idade permitida pelo procedimento; `PA_FLIDADE` indica compatibilidade. |
| `PA_SEXO` | String | Sexo (`M`, `F`; `0` = não informado/ambos). |
| `PA_RACACOR / PA_ETNIA` | String | Raça/cor (`01`–`05`, `99`) e etnia indígena. |
| `PA_MUNPCN` | String (6) | Município de residência do paciente (`999999` = ignorado → `null`). |
| `PA_QTDPRO / PA_QTDAPR` | Inteiro | Quantidade produzida (apresentada) e aprovada. |
| `PA_VALPRO / PA_VALAPR` | Float | Valor (R$) produzido e aprovado. |
| `PA_TPFIN / PA_SUBFIN / PA_NIVCPL` | String | Tipo e subtipo de financiamento (FAEC, MAC, PAB…) e nível de complexidade. |
| `PA_DOCORIG` | String | Código do documento de origem da produção (BPA consolidado, BPA individualizado, APAC, RAAS…; domínio no Informe Técnico). |
| `PA_CODOCO / PA_INDICA / PA_FLQT / PA_FLER` | String | Código de ocorrência, indicador de aprovação e flags de crítica de quantidade e de erro. |
| `PA_AUTORIZ` | String (13) | Número da APAC (preenchido nas linhas originárias de APAC). |
| `PA_NAT_JUR / PA_TPUPS / PA_TIPPRE / PA_MN_IND` | String | Natureza jurídica, tipo de unidade, tipo de prestador e indicador próprio/mantida do estabelecimento. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios aparecem com 6 dígitos (código IBGE sem dígito verificador, p.ex. `120040`); `wrangle_datasus` mantém como `String` `MUNIC_RES`, `MUNIC_MOV`, `CEP`, `CNES`, `PROC_REA`/`PROC_SOLIC` (SIGTAP, 10 dígitos), `DIAG_PRINC`/`DIAG_SECUN`/`DIAGSEC1–9`/`CID_NOTIF`/`CID_MORTE` (CID-10) e `N_AIH` (13 dígitos). Nunca converta esses campos para inteiro, pois os zeros à esquerda são significativos; para juntar com bases que usam 7 dígitos, calcule o dígito verificador do IBGE ou use a tabela de municípios (`TAB_*.zip`).
- **Valores ausentes e sentinelas**: strings vazias e os literais `999999`, `99999999` e `00000000` (após `strip`) viram `null`; códigos `0000` de CID e `0000000000000` de AIH/APAC permanecem como texto e devem ser tratados manualmente como "não informado". Registros com marca de exclusão dBASE (`_deleted = True`) são descartados e a coluna `_deleted` é removida.
- **Datas e competências**: o PA não possui colunas de data de atendimento (`DT_*`); a referência temporal é `PA_CMP`/`PA_MVM` (`AAAAMM`, `String`). Converta com `pl.col('pa_cmp').str.to_date('%Y%m', strict=False)` se precisar de `pl.Date`. `PA_PROC_ID` e `PA_CODUNI` (CNES) são `String` (apenas `PA_PROC_ID` consta explicitamente em `CODE_COLUMNS`).
- **Tipos numéricos**: `PA_QTDPRO`/`PA_QTDAPR` já são inteiros no DBF e `PA_VALPRO`/`PA_VALAPR` são `Float64`; `PA_IDADE` permanece texto de 3 dígitos — converta com `cast(pl.Int64, strict=False)` e trate `999` como ignorada.
- **Particularidades do dataset**: (i) use **aprovado** (`PA_QTDAPR`/`PA_VALAPR`), não produzido, para estimar o que foi pago; linhas com `PA_INDICA`/`PA_FLER` indicando glosa devem ser analisadas à parte; (ii) para atendimentos individualizados não há CNS do paciente; os campos `PA_CNSMED` (CNS do profissional) são codificados; (iii) UF do arquivo = UF do estabelecimento/gestor, não do paciente — use `PA_MUNPCN` para a residência; (iv) as partes `a`, `b`, … de um mesmo mês devem ser concatenadas sem deduplicar; (v) o dataset é enorme (~218 GB): sempre filtre por UF e período e use leitura em pedaços/Parquet; (vi) o 'PA' pré-2008 usa tabela de procedimentos de 8 dígitos (confira `TAB_SIA_199407-199910.zip` etc.) — não misture com a SIGTAP sem crosswalk.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sia-pa
quantilica datasus list sia-pa

# 2. Baixar microdados de sia-pa com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sia-pa -o ./data --start 2024-01 --end 2024-03 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sia-pa -o ./data --start 2024-01 --end 2024-03 --regions sp --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sia-pa -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-03 --regions sp
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sia-pa/202401").glob("sia-pa_sp_202401_*.dbc"))
pa = df.read_dbc(arquivo, dataset="sia-pa")

# Procedimentos mais produzidos (quantidade aprovada) e valor aprovado
top = (
    pa.group_by("pa_proc_id")
      .agg(pl.col("pa_qtdapr").sum().alias("qtd_aprovada"), pl.col("pa_valapr").sum().alias("valor_aprovado"))
      .sort("qtd_aprovada", descending=True)
)
print(top.head(10))

# Distribuição por faixa etária (excluindo 999 = ignorada)
idade = pa.with_columns(pl.col("pa_idade").cast(pl.Int64, strict=False)).filter(pl.col("pa_idade") != 999)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
- **Portal DATASUS — SIA/SUS (TabNet)**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/ (Assistência à Saúde → Produção Ambulatorial).
