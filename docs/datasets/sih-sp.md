# `sih-sp` — SP - Serviços Profissionais

`sih-sp` contém os **Serviços Profissionais** do SIH/SUS: cada linha é um ato profissional ou serviço (procedimento, quantidade e valor) lançado dentro de uma AIH aprovada, com o profissional/estabelecimento executor e o município do hospital e do paciente. Complementa o RD detalhando a composição do valor de serviços profissionais (`VAL_SP`) por AIH.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sih` — SIH: Sistema de Informação Hospitalar |
| **Código no `datasus-fetcher`** | `sih-sp` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 1997-06 a 2026-08 (conforme `index.json`; 27 UFs com arquivos; última atualização no FTP em 2026-10-16) |
| **Volume aproximado no FTP** | 9.466 arquivos (~57,0 GB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIHSUS/200801_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIHSUS/200801_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações Hospitalares do SUS (SIH/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES), com processamento e disseminação a cargo do DATASUS — e tem como finalidade operacionalizar o pagamento das internações realizadas em hospitais públicos e privados conveniados ao SUS. Por ser um sistema de faturamento, cobre apenas a assistência financiada pelo SUS (não inclui saúde suplementar nem internações particulares) e é a principal fonte nacional para estudar morbidade hospitalar, perfil assistencial e gasto hospitalar.

O evento gerador são os **atos profissionais registrados na AIH** (cirurgias, anestesias, partos, consultas e outros procedimentos remunerados como serviço profissional, além de procedimentos especiais). A unidade de análise é o **ato/serviço profissional por AIH** — uma AIH pode ter dezenas de linhas, ligadas ao RD por `SP_NAIH` = `N_AIH`, `SP_CNES` = `CNES` e à competência. Cada hospital preenche a Autorização de Internação Hospitalar (AIH) e a remete mensalmente ao gestor municipal/estadual, que a valida e a envia ao DATASUS para processamento na competência (`ANO_CMPT`/`MES_CMPT`). O processamento classifica cada AIH como aprovada (arquivo RD), rejeitada (RJ/ER) e detalha os atos profissionais (SP).

O FTP traz o SP em duas séries (1992–2007 e 2008 em diante), com início efetivo do inventário em 1997-06. O arquivo é o maior do SIH (~57 GB para 9.466 arquivos), porque replica o detalhamento por ato. Com a Tabela Unificada/SIGTAP (2008) o campo `SP_ATOPROF` passou a usar códigos de procedimento de 10 dígitos e foram incluídos campos de complexidade (`SP_COMPLEX`), financiamento (`SP_FINANC`/`SP_CO_FAEC`) e CBO/documento do profissional (`SP_PF_CBO`, `SP_PF_DOC`).

Usos principais: análise do gasto com serviços profissionais por procedimento, especialidade (CBO) e hospital; produção por tipo de ato (cirurgias, partos, anestesia); verificação de pontos (`SP_PTSP`) e valor unitário dos atos; estudos de remuneração e de cobertura de especialidades; e reconciliação com `VAL_SP` do RD. Não contém dados clínicos do paciente além de `SP_CIDPRI`/`SP_CIDSEC` e das datas da AIH.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIHSUS/199201_200712/Dados` | `SP` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |
| `/dissemin/publicos/SIHSUS/200801_/Dados` | `SP` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `SPSP2401.dbc` — `SP` (Serviços Profissionais) + `SP` (UF) + `24` (ano) + `01` (mês de competência). Atenção: prefixo e UF podem coincidir (`SPSP…`), o que é esperado.
- **No armazenamento local do `datasus-fetcher`**: `data/sih-sp/<AAAAMM>/sih-sp_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sih-sp/202401/sih-sp_sp_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/IT_SIHSUS_1603.pdf` (Informe Técnico do SIHSUS, 57 KB, 2016) é o dicionário oficial de variáveis; `Auxiliar/TAB_SIH.zip` (~6,1 MB, tabelas e conversores `.cnv`/`.def` atuais) e as versões históricas `TAB_SIH_199201-199712.zip`, `TAB_SIH_199801-200307.zip` e `TAB_SIH_200308-200712.zip` trazem as tabelas de procedimentos, CID e códigos usadas em cada fase.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

37 colunas no arquivo de 2024-01 (`SPAC2401.dbc`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `SP_GESTOR` | String (6) | Código do gestor responsável pelo estabelecimento. |
| `SP_UF` | String (2) | Código IBGE da UF do estabelecimento (p.ex. `12` = Acre). |
| `SP_AA / SP_MM` | String | Ano e mês da competência. |
| `SP_CNES` | String (7) | Estabelecimento (CNES) que realizou a internação. |
| `SP_NAIH` | String (13) | Número da AIH a que o ato pertence (chave para o RD). |
| `SP_PROCREA` | String (10) | Procedimento principal realizado na AIH. |
| `SP_DTINTER / SP_DTSAIDA` | String AAAAMMDD | Datas de internação e saída da AIH. |
| `SP_ATOPROF` | String (10) | Código SIGTAP do ato profissional executado. |
| `SP_QTD_ATO / SP_QT_PROC` | Inteiro | Quantidade do ato e de procedimentos. |
| `SP_PTSP` | String | Pontos de serviços profissionais do ato. |
| `SP_VALATO` | Float | Valor (R$) do ato profissional. |
| `SP_M_HOSP / SP_M_PAC` | String (6) | Município do hospital e município de residência do paciente. |
| `SP_PF_CBO` | String (6) | CBO da ocupação do profissional que executou o ato. |
| `SP_PF_DOC / SP_PJ_DOC` | String | Documento do profissional (pessoa física, CPF/CNS) e da pessoa jurídica (CNPJ); dados pessoais, tratar conforme a LGPD. |
| `SP_CIDPRI / SP_CIDSEC` | String (CID-10) | Diagnóstico principal e secundário da AIH. |
| `SP_COMPLEX / SP_FINANC / SP_CO_FAEC` | String | Complexidade, tipo de financiamento e subtipo FAEC do ato. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios aparecem com 6 dígitos (código IBGE sem dígito verificador, p.ex. `120040`); `wrangle_datasus` mantém como `String` `MUNIC_RES`, `MUNIC_MOV`, `CEP`, `CNES`, `PROC_REA`/`PROC_SOLIC` (SIGTAP, 10 dígitos), `DIAG_PRINC`/`DIAG_SECUN`/`DIAGSEC1–9`/`CID_NOTIF`/`CID_MORTE` (CID-10) e `N_AIH` (13 dígitos). Nunca converta esses campos para inteiro, pois os zeros à esquerda são significativos; para juntar com bases que usam 7 dígitos, calcule o dígito verificador do IBGE ou use a tabela de municípios (`TAB_*.zip`).
- **Valores ausentes e sentinelas**: strings vazias e os literais `999999`, `99999999` e `00000000` (após `strip`) viram `null`; códigos `0000` de CID e `0000000000000` de AIH/APAC permanecem como texto e devem ser tratados manualmente como "não informado". Registros com marca de exclusão dBASE (`_deleted = True`) são descartados e a coluna `_deleted` é removida.
- **Datas e competências**: `SP_DTINTER`/`SP_DTSAIDA` (`AAAAMMDD`) **não** pertencem a `DATE_COLUMNS` (os nomes não coincidem com `DT_INTER`/`DT_SAIDA`) e permanecem como texto; converta explicitamente com `str.to_date('%Y%m%d', strict=False)`. `SP_AA` e `SP_MM` identificam a competência.
- **Tipos e códigos**: as colunas `SP_*` não estão em `CODE_COLUMNS`/`FLOAT_COLUMNS`; chegam com o tipo nativo do DBF (`SP_VALATO`/`SP_QTD_ATO` numéricos, demais `String`) com zeros à esquerda preservados. Nomes são minúsculos (`sp_naih`, `sp_atoprof`…) e `uf`, `ano`, `mes` são acrescentados a partir do nome do arquivo.
- **Particularidades do dataset**: (i) é um arquivo **muito grande** — prefira filtrar por UF/mês e usar leitura em pedaços/Parquet; (ii) o grão é o ato, então some `SP_VALATO` por `SP_NAIH` antes de comparar com `VAL_SP` do RD; (iii) `SP_PF_DOC` identifica pessoas físicas — não publique sem anonimização; (iv) atos de AIH tipo 5 repetem-se por competência.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sih-sp
quantilica datasus list sih-sp

# 2. Baixar microdados de sih-sp com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sih-sp -o ./data --start 2024-01 --end 2024-03 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sih-sp -o ./data --start 2024-01 --end 2024-03 --regions sp --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sih-sp -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-03 --regions sp
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sih-sp/202401").glob("sih-sp_sp_202401_*.dbc"))
sp = df.read_dbc(arquivo, dataset="sih-sp")

# Valor de serviços profissionais por ocupação (CBO) do executor
por_cbo = (
    sp.group_by("sp_pf_cbo")
      .agg(pl.col("sp_qtd_ato").sum().alias("atos"), pl.col("sp_valato").sum().alias("valor"))
      .sort("valor", descending=True)
)
print(por_cbo.head(10))

# Valor de SP por AIH, pronto para conferir com VAL_SP do RD
sp_por_aih = sp.group_by("sp_naih").agg(pl.col("sp_valato").sum().alias("val_sp_atos"))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIHSUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/IT_SIHSUS_1603.pdf`
- **Manual Técnico Operacional do SIH/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **PCDaS/Fiocruz** (SIH/SUS para pesquisa): https://pcdas.icict.fiocruz.br/
