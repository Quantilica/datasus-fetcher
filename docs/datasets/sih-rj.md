# `sih-rj` — RJ - AIH Rejeitadas

`sih-rj` contém as **AIH Rejeitadas** no processamento do SIH/SUS: cada linha é uma Autorização de Internação Hospitalar apresentada pelo hospital que **não foi aprovada** para pagamento na competência, com o mesmo leiaute do arquivo RD acrescido de campos de situação e bloqueio. Permite auditar glosas, qualidade do faturamento e o volume de internações não pagas.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sih` — SIH: Sistema de Informação Hospitalar |
| **Código no `datasus-fetcher`** | `sih-rj` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 2008-01 a 2026-08 (conforme `index.json`; 27 UFs com arquivos; última atualização no FTP em 2026-10-16) |
| **Volume aproximado no FTP** | 5.887 arquivos (~945,8 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIHSUS/200801_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIHSUS/200801_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações Hospitalares do SUS (SIH/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES), com processamento e disseminação a cargo do DATASUS — e tem como finalidade operacionalizar o pagamento das internações realizadas em hospitais públicos e privados conveniados ao SUS. Por ser um sistema de faturamento, cobre apenas a assistência financiada pelo SUS (não inclui saúde suplementar nem internações particulares) e é a principal fonte nacional para estudar morbidade hospitalar, perfil assistencial e gasto hospitalar.

O evento gerador é a **apresentação de uma AIH que falha nas críticas do processamento** (inconsistência cadastral, procedimento incompatível com CID/sexo/idade, teto financeiro, duplicidade, entre outras). A unidade de análise é a **AIH rejeitada por competência**. Cada hospital preenche a Autorização de Internação Hospitalar (AIH) e a remete mensalmente ao gestor municipal/estadual, que a valida e a envia ao DATASUS para processamento na competência (`ANO_CMPT`/`MES_CMPT`). O processamento classifica cada AIH como aprovada (arquivo RD), rejeitada (RJ/ER) e detalha os atos profissionais (SP). O motivo detalhado da rejeição não está no RJ: ele é registrado, por AIH, no arquivo `sih-er` (campo `CO_ERRO`), que pode ser ligado ao RJ por `N_AIH`/`AIH`, `CNES` e competência.

O RJ existe no FTP somente a partir de 2008-01, na estrutura do SIH com Tabela Unificada (SIGTAP); não há RJ para o período 1992–2007. As colunas de valores e diagnóstico seguem o RD, porém sem os diagnósticos secundários adicionais (`DIAGSEC1–9`) e sem os campos de repasse (`VAL_SH_FED`…), e com três campos extras de situação (`ST_SITUAC`, `ST_BLOQ`, `ST_MOT_BLO`). Uma AIH rejeitada pode ser corrigida e reapresentada, voltando como aprovada (RD) em competência posterior.

Aplicações: taxa de rejeição/glosa por hospital, município e gestor (RJ ÷ (RD + RJ)); valor financeiro retido (`VAL_TOT` das AIH rejeitadas); identificação de hospitais com maior inconsistência de faturamento; análise de causas de rejeição quando combinado com `sih-er`; auditoria e controle e avaliação de contratos; e estimativa de subnotificação de internações quando se compara a produção apresentada com a aprovada.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIHSUS/200801_/Dados` | `RJ` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `RJSP2401.dbc` — `RJ` (AIH Rejeitada) + `SP` (UF) + `24` (ano 2024) + `01` (mês de competência). Disponível apenas no diretório `200801_`.
- **No armazenamento local do `datasus-fetcher`**: `data/sih-rj/<AAAAMM>/sih-rj_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sih-rj/202401/sih-rj_sp_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/IT_SIHSUS_1603.pdf` (Informe Técnico do SIHSUS, 57 KB, 2016) é o dicionário oficial de variáveis; `Auxiliar/TAB_SIH.zip` (~6,1 MB, tabelas e conversores `.cnv`/`.def` atuais) e as versões históricas `TAB_SIH_199201-199712.zip`, `TAB_SIH_199801-200307.zip` e `TAB_SIH_200308-200712.zip` trazem as tabelas de procedimentos, CID e códigos usadas em cada fase.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

91 colunas no arquivo de 2024-01 (`RJAC2401.dbc`); o leiaute coincide com o do RD, exceto pelas colunas de situação/bloqueio.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `UF_ZI` | String (6) | Código do gestor/UF de gestão do estabelecimento. |
| `ANO_CMPT / MES_CMPT` | String | Competência de processamento em que a AIH foi rejeitada. |
| `N_AIH` | String (13) | Número da AIH rejeitada (chave de ligação com `sih-er`). |
| `CNES` | String (7) | Estabelecimento que apresentou a AIH. |
| `MUNIC_RES / MUNIC_MOV` | String (6) | Município de residência do paciente e do estabelecimento. |
| `NASC / IDADE / COD_IDADE / SEXO` | String / Int / String / Int | Dados demográficos do paciente informados na AIH. |
| `DT_INTER / DT_SAIDA` | `pl.Date` | Datas de internação e saída informadas. |
| `PROC_SOLIC / PROC_REA` | String (10) | Procedimento SIGTAP solicitado e realizado. |
| `DIAG_PRINC / DIAG_SECUN` | String (CID-10) | Diagnósticos informados. |
| `VAL_SH / VAL_SP / VAL_TOT` | Float | Valores calculados da AIH que **não foram pagos** (R$). |
| `COBRANCA` | String | Motivo de saída/cobrança informado na AIH. |
| `ST_SITUAC` | String | Situação da AIH no processamento (códigos do Informe Técnico do SIHSUS). |
| `ST_BLOQ / ST_MOT_BLO` | String | Indicador e motivo de bloqueio da AIH. |
| `SEQUENCIA / REMESSA` | Inteiro / String | Sequência do registro e nome da remessa (`HE<gestor>…<AAAAMM>.DTS`) enviada pelo gestor; útil para rastrear o lote de origem. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios aparecem com 6 dígitos (código IBGE sem dígito verificador, p.ex. `120040`); `wrangle_datasus` mantém como `String` `MUNIC_RES`, `MUNIC_MOV`, `CEP`, `CNES`, `PROC_REA`/`PROC_SOLIC` (SIGTAP, 10 dígitos), `DIAG_PRINC`/`DIAG_SECUN`/`DIAGSEC1–9`/`CID_NOTIF`/`CID_MORTE` (CID-10) e `N_AIH` (13 dígitos). Nunca converta esses campos para inteiro, pois os zeros à esquerda são significativos; para juntar com bases que usam 7 dígitos, calcule o dígito verificador do IBGE ou use a tabela de municípios (`TAB_*.zip`).
- **Valores ausentes e sentinelas**: strings vazias e os literais `999999`, `99999999` e `00000000` (após `strip`) viram `null`; códigos `0000` de CID e `0000000000000` de AIH/APAC permanecem como texto e devem ser tratados manualmente como "não informado". Registros com marca de exclusão dBASE (`_deleted = True`) são descartados e a coluna `_deleted` é removida.
- **Datas e competências**: `DT_INTER`/`DT_SAIDA` (`AAAAMMDD`) → `pl.Date`; `NASC` permanece `String` `AAAAMMDD`. A competência refere-se ao processamento da rejeição, não à data da internação.
- **Tipos numéricos**: `VAL_*` → `Float64`; `IDADE`, `SEXO`, `RACA_COR`, `MORTE`, `DIAS_PERM` → `Int64`; `SEQUENCIA` já vem numérica do DBF.
- **Particularidades do dataset**: (i) o RJ **não** contém o motivo da rejeição — junte com `sih-er` pelo número da AIH, CNES e competência; (ii) a mesma AIH pode ser rejeitada em mais de uma competência e depois aprovada, então deduplique antes de calcular taxas; (iii) os valores representam o que o hospital apresentou e **não foi pago**, não despesa do SUS; (iv) `ST_SITUAC`/`ST_BLOQ`/`ST_MOT_BLO` seguem tabelas de domínio do SIHSUS presentes em `TAB_SIH.zip`.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sih-rj
quantilica datasus list sih-rj

# 2. Baixar microdados de sih-rj com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sih-rj -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sih-rj -o ./data --start 2024-01 --end 2024-12 --regions sp --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sih-rj -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12 --regions sp
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sih-rj/202401").glob("sih-rj_sp_202401_*.dbc"))
rj = df.read_dbc(arquivo, dataset="sih-rj")

# Valor apresentado e não pago, por hospital (CNES)
por_hospital = (
    rj.group_by("cnes")
      .agg(pl.len().alias("aih_rejeitadas"), pl.col("val_tot").sum().alias("valor_rejeitado"))
      .sort("valor_rejeitado", descending=True)
)
print(por_hospital.head(10))

# Ligação com o motivo da rejeição (sih-er): N_AIH == AIH
er = df.read_dbc(next(Path("./data/sih-er/202401").glob("sih-er_sp_202401_*.dbc")), dataset="sih-er")
rj_com_erro = rj.join(er.select("aih", "cnes", "co_erro"), left_on=["n_aih", "cnes"], right_on=["aih", "cnes"], how="left")
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIHSUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/IT_SIHSUS_1603.pdf`
- **Manual Técnico Operacional do SIH/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **PCDaS/Fiocruz** (SIH/SUS para pesquisa): https://pcdas.icict.fiocruz.br/
