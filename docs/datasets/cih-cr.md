# `cih-cr` — Comunicação de Internação Hospitalar

`cih-cr` contém a **Comunicação de Internação Hospitalar (CIH)**: cada linha é uma internação ocorrida em estabelecimento de saúde que **não é remunerada por AIH do SUS** (por exemplo, hospitais próprios ou filantrópicos que informam a produção ao gestor), registrada para dar visibilidade à totalidade das internações do território. Cobre apenas o período 2008–2011 no FTP.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cih` — CIH: Sistema de Comunicação de Informação Hospitalar |
| **Código no `datasus-fetcher`** | `cih-cr` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 2008-01 a 2011-04 (conforme `index.json`; 24 UFs com arquivos; última atualização no FTP em 2017-07-06) |
| **Volume aproximado no FTP** | 868 arquivos (~165,1 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | Não aplicável |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CIH/200801_201012/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Comunicação de Informação Hospitalar (CIH) foi criado pelo Ministério da Saúde/DATASUS para complementar o SIH/SUS, captando internações que não geram pagamento via AIH — por exemplo, as realizadas em hospitais sob outra forma de financiamento ou convênio — e que, sem a CIH, ficariam invisíveis nas estatísticas hospitalares. É gerido pela SAES/MS com processamento do DATASUS.

O evento gerador é a **internação hospitalar comunicada** pelo estabelecimento ao gestor por meio do leiaute CIH, com variáveis análogas às da AIH (paciente, município de residência, procedimento, diagnóstico principal e secundário, datas, tempo de permanência, óbito). A unidade de análise é a **internação comunicada por competência**. Não há valores financeiros (`VAL_*`) nem número de AIH, pois a CIH não é um instrumento de faturamento.

O inventário do FTP cobre apenas 2008-01 a 2011-04 (24 UFs com arquivos, ~165 MB, última atualização em 2017). O sistema foi sucedido pelo CIHA (`ciha`, a partir de 2011-01), que amplia a comunicação para o atendimento ambulatorial; por isso a CIH é um dataset **descontinuado**, com leiaute reduzido de 28 colunas e sem campos de valor. Os dados de CIH foram usados para melhorar a completude de internações hospitalares nos municípios que não registravam AIH.

Aplicações: completar o panorama de internações em municípios com hospitais fora do faturamento por AIH; análise de causas de internação (CID-10 do `DIAG_PRINC`), permanência e mortalidade hospitalar da rede não-SUS comunicante; estudos de oferta e fluxo de pacientes (`MUNIC_RES` vs. `MUNIC_MOV`); e como ponte histórica para a série do `ciha` (2011 em diante).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CIH/200801_201012/Dados` | `CR` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `CRSP0801.dbc` — `CR` (Comunicação de Internação Hospitalar) + `SP` (UF) + `08` (ano 2008) + `01` (mês de competência). Exemplo real de menor porte: `CRAC0801.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cih-cr/<AAAAMM>/cih-cr_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/cih-cr/200801/cih-cr_sp_200801_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: o grupo `cih` **não possui diretório de documentação** em `meta.docs` (sem Informe Técnico próprio no FTP); o leiaute é semelhante ao do SIH/RD (consulte `IT_SIHSUS_1603.pdf` em `SIHSUS/200801_/Doc`). Em `Auxiliar/` há `TAB_CIH.zip` (~15,3 MB, tabelas e conversores `.cnv`/`.def` de procedimento, CID e municípios).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

28 colunas no arquivo de 2008-01 (`CRAC0801.dbc`); a CIH não traz campos de valor financeiro nem número de AIH.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `ANO_CMPT / MES_CMPT` | String (4 / 2) | Ano e mês da competência da comunicação. |
| `ESPEC` | String | Especialidade do leito. |
| `CGC_HOSP` | String (14) | CNPJ do hospital comunicante. |
| `CNES` | String (7) | Código CNES do estabelecimento. |
| `MUNIC_RES / MUNIC_MOV` | String (6) | Município de residência do paciente e do estabelecimento (IBGE 6 dígitos). |
| `NASC / IDADE / COD_IDADE` | String AAAAMMDD / Int / String | Data de nascimento, idade e unidade (`2` dias, `3` meses, `4` anos). |
| `SEXO` | Inteiro | Sexo (`1` masculino, `3` feminino, `0`/`9` ignorado). |
| `PROC_REA` | String (10) | Procedimento realizado na internação (SIGTAP). |
| `DT_INTER / DT_SAIDA` | String AAAAMMDD → `pl.Date` | Datas de internação e saída. |
| `DIAG_PRINC / DIAG_SECUN` | String (CID-10) | Diagnósticos principal e secundário. |
| `DIAS_PERM` | Inteiro | Dias de permanência. |
| `UTI_MES_TO / UTI_INT_TO` | Inteiro | Dias de UTI no mês e na internação. |
| `COBRANCA / NATUREZA / GESTAO` | String | Motivo de saída/cobrança, natureza do hospital e tipo de gestão. |
| `MORTE` | Inteiro | Indicador de óbito. |
| `CAR_INT / FONTE / HOMONIMO / NACIONAL` | String | Caráter da internação, fonte da informação, indicador de homônimo e nacionalidade. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios aparecem com 6 dígitos (código IBGE sem dígito verificador, p.ex. `120040`); `wrangle_datasus` mantém como `String` `MUNIC_RES`, `MUNIC_MOV`, `CEP`, `CNES`, `PROC_REA`/`PROC_SOLIC` (SIGTAP, 10 dígitos), `DIAG_PRINC`/`DIAG_SECUN`/`DIAGSEC1–9`/`CID_NOTIF`/`CID_MORTE` (CID-10) e `N_AIH` (13 dígitos). Nunca converta esses campos para inteiro, pois os zeros à esquerda são significativos; para juntar com bases que usam 7 dígitos, calcule o dígito verificador do IBGE ou use a tabela de municípios (`TAB_*.zip`).
- **Valores ausentes e sentinelas**: strings vazias e os literais `999999`, `99999999` e `00000000` (após `strip`) viram `null`; códigos `0000` de CID e `0000000000000` de AIH/APAC permanecem como texto e devem ser tratados manualmente como "não informado". Registros com marca de exclusão dBASE (`_deleted = True`) são descartados e a coluna `_deleted` é removida.
- **Datas e competências**: `DT_INTER` e `DT_SAIDA` (`AAAAMMDD`) → `pl.Date`; `NASC` permanece texto `AAAAMMDD`. `ANO_CMPT` e `MES_CMPT` identificam a competência (2008-01 a 2011-04).
- **Tipos numéricos**: `IDADE`, `SEXO`, `MORTE`, `DIAS_PERM` → `Int64` (em `INTEGER_COLUMNS`). `IDADE` precisa ser combinada com `COD_IDADE`. Não há colunas `VAL_*` neste dataset.
- **Particularidades do dataset**: (i) é uma série **encerrada** e pequena; (ii) não substitui o SIH — não há identificador de AIH, portanto não é possível deduplicar contra o `sih-rd` pelo número; (iii) `CGC_HOSP` e `CNES` identificam o hospital, mas a cobertura varia por UF (24 UFs com arquivo); (iv) a CIH foi sucedida pelo `ciha` a partir de 2011-01 — há sobreposição em 2011-01 a 2011-04, cuja deduplicação deve ser feita por hospital+competência.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cih-cr
quantilica datasus list cih-cr

# 2. Baixar microdados de cih-cr com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync cih-cr -o ./data --start 2008-01 --end 2011-04 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cih-cr -o ./data --start 2008-01 --end 2011-04 --regions sp rj --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline cih-cr -o ./data/raw --parquet-dir ./data/parquet --start 2008-01 --end 2011-04 --regions sp rj
```

> O grupo `cih` não possui diretório de documentação mapeado em `meta.docs`; por isso a flag `--docs` foi omitida acima.

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/cih-cr/200801").glob("cih-cr_sp_200801_*.dbc"))
cr = df.read_dbc(arquivo, dataset="cih-cr")

# Internações comunicadas por diagnóstico principal e permanência média
q = (
    cr.with_columns(pl.col("diag_princ").str.slice(0, 3).alias("cid3"))
      .group_by("cid3")
      .agg(pl.len().alias("internacoes"), pl.col("dias_perm").mean().alias("permanencia_media"))
      .sort("internacoes", descending=True)
)
print(q.head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CIH/200801_201012/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIHSUS** (leiaute de referência): `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/IT_SIHSUS_1603.pdf`
- **Tabelas auxiliares CIH**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CIH/200801_201012/Auxiliar/TAB_CIH.zip`
- **Biblioteca Virtual em Saúde do Ministério da Saúde** (normas e manuais do SIH/SIA/CIHA): https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz**: https://pcdas.icict.fiocruz.br/
