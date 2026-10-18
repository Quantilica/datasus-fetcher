# `sih-er` — ER - AIH Rejeitadas com código de erro

`sih-er` registra os **erros de processamento das AIH rejeitadas**: cada linha associa uma AIH rejeitada (por número, estabelecimento e datas) ao **código do erro** (`CO_ERRO`) que motivou a rejeição. É o complemento diagnóstico do `sih-rj`, indispensável para entender por que uma internação não foi paga.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sih` — SIH: Sistema de Informação Hospitalar |
| **Código no `datasus-fetcher`** | `sih-er` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 2011-01 a 2026-08 (conforme `index.json`; 27 UFs com arquivos; última atualização no FTP em 2026-10-16) |
| **Volume aproximado no FTP** | 4.958 arquivos (~321,3 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIHSUS/200801_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIHSUS/200801_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações Hospitalares do SUS (SIH/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES), com processamento e disseminação a cargo do DATASUS — e tem como finalidade operacionalizar o pagamento das internações realizadas em hospitais públicos e privados conveniados ao SUS. Por ser um sistema de faturamento, cobre apenas a assistência financiada pelo SUS (não inclui saúde suplementar nem internações particulares) e é a principal fonte nacional para estudar morbidade hospitalar, perfil assistencial e gasto hospitalar.

O evento gerador é a **crítica de consistência** do processamento da AIH, que grava, para cada inconsistência encontrada, o código de erro correspondente (tabela de críticas do SIHSUS). A unidade de análise é a **ocorrência de erro por AIH e competência**; uma AIH com múltiplas críticas pode gerar mais de uma linha, e `SEQUENCIA`/`REMESSA` identificam o lote do gestor. Cada hospital preenche a Autorização de Internação Hospitalar (AIH) e a remete mensalmente ao gestor municipal/estadual, que a valida e a envia ao DATASUS para processamento na competência (`ANO_CMPT`/`MES_CMPT`). O processamento classifica cada AIH como aprovada (arquivo RD), rejeitada (RJ/ER) e detalha os atos profissionais (SP).

O inventário do FTP inicia em 2011-01 (embora o RJ comece em 2008-01) e segue até a competência corrente. O arquivo é pequeno (~0,3 GB para 4.958 arquivos) e tem leiaute fixo de 13 campos, bem distinto do RD: traz apenas identificação da AIH, datas, municípios e o erro. A tabela de significado dos códigos `CO_ERRO` encontra-se nas tabelas auxiliares do SIH (`TAB_SIH.zip`) e no Informe Técnico do SIHSUS.

Aplicações: ranking das causas de rejeição por hospital e município; mensuração do impacto financeiro de cada tipo de erro (quando ligado ao `sih-rj`); apoio à qualificação do faturamento e à capacitação de equipes de faturamento hospitalar; auditoria de gestores que enviam remessas com alto índice de erros; e monitoramento da evolução da qualidade da informação hospitalar.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIHSUS/200801_/Dados` | `ER` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `ERSP2401.dbc` — `ER` (AIH Rejeitadas com código de erro) + `SP` (UF) + `24` (ano 2024) + `01` (mês de competência).
- **No armazenamento local do `datasus-fetcher`**: `data/sih-er/<AAAAMM>/sih-er_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sih-er/202401/sih-er_sp_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/IT_SIHSUS_1603.pdf` (Informe Técnico do SIHSUS, 57 KB, 2016) é o dicionário oficial de variáveis; `Auxiliar/TAB_SIH.zip` (~6,1 MB, tabelas e conversores `.cnv`/`.def` atuais) e as versões históricas `TAB_SIH_199201-199712.zip`, `TAB_SIH_199801-200307.zip` e `TAB_SIH_200308-200712.zip` trazem as tabelas de procedimentos, CID e códigos usadas em cada fase.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

13 colunas no arquivo de 2024-01 (`ERAC2401.dbc`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `SEQUENCIA` | Inteiro | Número sequencial do registro dentro da remessa. |
| `REMESSA` | String | Nome da remessa enviada pelo gestor (padrão `HE<código do gestor>…<AAAAMM>.DTS`). |
| `CNES` | String (7) | Estabelecimento que apresentou a AIH. |
| `AIH` | String (13) | Número da AIH rejeitada (equivale a `N_AIH` do RD/RJ). |
| `ANO / MES` | Inteiro | Ano e mês da competência do processamento. |
| `DT_INTER / DT_SAIDA` | String AAAAMMDD → `pl.Date` | Datas de internação e saída informadas. |
| `MUN_MOV` | String (6) | Município do estabelecimento (movimento). |
| `UF_ZI` | String (6) | Código do gestor/UF de gestão. |
| `MUN_RES` | String (6) | Município de residência do paciente. |
| `UF_RES` | String (2) | UF de residência do paciente (código IBGE de 2 dígitos). |
| `CO_ERRO` | String (6) | Código do erro/crítica que causou a rejeição (p.ex. `020081`); consultar tabela de erros do SIH. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios aparecem com 6 dígitos (código IBGE sem dígito verificador, p.ex. `120040`); `wrangle_datasus` mantém como `String` `MUNIC_RES`, `MUNIC_MOV`, `CEP`, `CNES`, `PROC_REA`/`PROC_SOLIC` (SIGTAP, 10 dígitos), `DIAG_PRINC`/`DIAG_SECUN`/`DIAGSEC1–9`/`CID_NOTIF`/`CID_MORTE` (CID-10) e `N_AIH` (13 dígitos). Nunca converta esses campos para inteiro, pois os zeros à esquerda são significativos; para juntar com bases que usam 7 dígitos, calcule o dígito verificador do IBGE ou use a tabela de municípios (`TAB_*.zip`).
- **Valores ausentes e sentinelas**: strings vazias e os literais `999999`, `99999999` e `00000000` (após `strip`) viram `null`; códigos `0000` de CID e `0000000000000` de AIH/APAC permanecem como texto e devem ser tratados manualmente como "não informado". Registros com marca de exclusão dBASE (`_deleted = True`) são descartados e a coluna `_deleted` é removida.
- **Datas e competências**: `DT_INTER`/`DT_SAIDA` (`AAAAMMDD`) → `pl.Date`; `ANO`/`MES` estão em `INTEGER_COLUMNS` e viram `Int64`. Os nomes diferem do RD (`AIH`, `MUN_MOV`, `MUN_RES`, `UF_RES`): essas colunas **não** estão em `CODE_COLUMNS`, mas o DBF já as entrega como texto e os zeros à esquerda são preservados (`CO_ERRO` deve continuar `String`).
- **Particularidades do dataset**: (i) o par (`AIH`, `CNES`, competência) liga o ER ao `sih-rj`; (ii) pode haver várias linhas por AIH — conte AIH distintas com `n_unique` ao calcular taxas; (iii) o ER só existe a partir de 2011-01, então rejeições anteriores não têm código de erro neste dataset; (iv) o significado de `CO_ERRO` muda com o tempo, use a tabela auxiliar da data correspondente.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sih-er
quantilica datasus list sih-er

# 2. Baixar microdados de sih-er com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sih-er -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sih-er -o ./data --start 2024-01 --end 2024-12 --regions sp --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sih-er -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12 --regions sp
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sih-er/202401").glob("sih-er_sp_202401_*.dbc"))
er = df.read_dbc(arquivo, dataset="sih-er")

# Principais causas de rejeição e hospitais afetados
causas = (
    er.group_by("co_erro")
      .agg(pl.col("aih").n_unique().alias("aih_distintas"), pl.col("cnes").n_unique().alias("hospitais"))
      .sort("aih_distintas", descending=True)
)
print(causas.head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIHSUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/IT_SIHSUS_1603.pdf`
- **Manual Técnico Operacional do SIH/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **PCDaS/Fiocruz** (SIH/SUS para pesquisa): https://pcdas.icict.fiocruz.br/
