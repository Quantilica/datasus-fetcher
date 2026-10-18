# `sih-rd` — RD - AIH Reduzida

`sih-rd` reúne as **AIH Reduzidas**: o arquivo principal do Sistema de Informações Hospitalares do SUS (SIH/SUS), em que cada linha é uma Autorização de Internação Hospitalar **aprovada e paga** em uma competência de processamento, com dados do paciente, do estabelecimento, do diagnóstico, do procedimento realizado, da permanência e dos valores faturados. É a base mais usada no Brasil para estudar internações financiadas pelo SUS.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sih` — SIH: Sistema de Informação Hospitalar |
| **Código no `datasus-fetcher`** | `sih-rd` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 1992-01 a 2026-08 (conforme `index.json`; 27 UFs com arquivos; última atualização no FTP em 2026-10-16) |
| **Volume aproximado no FTP** | 11.211 arquivos (~25,6 GB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIHSUS/200801_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIHSUS/200801_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações Hospitalares do SUS (SIH/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES), com processamento e disseminação a cargo do DATASUS — e tem como finalidade operacionalizar o pagamento das internações realizadas em hospitais públicos e privados conveniados ao SUS. Por ser um sistema de faturamento, cobre apenas a assistência financiada pelo SUS (não inclui saúde suplementar nem internações particulares) e é a principal fonte nacional para estudar morbidade hospitalar, perfil assistencial e gasto hospitalar.

O evento gerador é a **internação hospitalar** formalizada pela Autorização de Internação Hospitalar (AIH). A unidade de análise do RD é a **AIH aprovada** (e não o paciente: o SIH não possui identificador único de pessoa, de modo que reinternações do mesmo indivíduo aparecem como AIH distintas). Cada hospital preenche a Autorização de Internação Hospitalar (AIH) e a remete mensalmente ao gestor municipal/estadual, que a valida e a envia ao DATASUS para processamento na competência (`ANO_CMPT`/`MES_CMPT`). O processamento classifica cada AIH como aprovada (arquivo RD), rejeitada (RJ/ER) e detalha os atos profissionais (SP). O campo `IDENT` distingue a AIH normal (tipo 1) da AIH de continuação/longa permanência (tipo 5), que reaparece em competências sucessivas com o mesmo paciente e deve ser tratada para evitar dupla contagem de internações.

O FTP mantém duas séries contínuas: 1992-01 a 2007-12 (diretório `199201_200712`, antes da Tabela Unificada) e 2008-01 em diante (`200801_`). Marcos relevantes: adoção da CID-10 em substituição à CID-9 (a partir de 1998 no SIH), a implantação da Tabela Unificada de Procedimentos, Medicamentos e OPM do SUS (SIGTAP) a partir de 2008, que alterou os códigos de procedimento (10 dígitos) e o leiaute, e a inclusão de campos de diagnósticos secundários (`DIAGSEC1`–`DIAGSEC9`) e de repasse federal/gestor (`VAL_*_FED`/`VAL_*_GES`) nos leiautes recentes. O mês do arquivo é a **competência de processamento**, não a data da internação: use `DT_INTER`/`DT_SAIDA` para análises temporais clínicas.

Indicadores típicos: taxa de internação por 10.000 habitantes por causa (CID-10 do `DIAG_PRINC`) e por município de residência; internações por condições sensíveis à atenção primária (ICSAP); tempo médio de permanência (`DIAS_PERM`); letalidade hospitalar (`MORTE`); taxa de ocupação de UTI (`UTI_MES_TO`); custo médio por internação e por procedimento (`VAL_TOT`, `VAL_SH`, `VAL_SP`); fluxos de pacientes entre município de residência (`MUNIC_RES`) e de internação (`MUNIC_MOV`); e partos, cesarianas e mortalidade materna/neonatal hospitalar.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIHSUS/199201_200712/Dados` | `RD` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |
| `/dissemin/publicos/SIHSUS/200801_/Dados` | `RD` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `RDSP2401.dbc` — `RD` (AIH Reduzida) + `SP` (UF de gestão/internação: São Paulo) + `24` (ano 2024) + `01` (mês de competência janeiro). Arquivos de 1992–2007 seguem o mesmo padrão, p.ex. `RDAC9201.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/sih-rd/<AAAAMM>/sih-rd_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sih-rd/202401/sih-rd_sp_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/IT_SIHSUS_1603.pdf` (Informe Técnico do SIHSUS, 57 KB, 2016) é o dicionário oficial de variáveis; `Auxiliar/TAB_SIH.zip` (~6,1 MB, tabelas e conversores `.cnv`/`.def` atuais) e as versões históricas `TAB_SIH_199201-199712.zip`, `TAB_SIH_199801-200307.zip` e `TAB_SIH_200308-200712.zip` trazem as tabelas de procedimentos, CID e códigos usadas em cada fase.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Colunas do leiaute atual (114 campos no arquivo de 2024-01, `RDAC2401.dbc`); o leiaute antes de 2008 é mais enxuto.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `UF_ZI` | String (6) | Código IBGE da UF/município de gestão (zona de informação) do estabelecimento; na prática o código do gestor, p.ex. `120000` para o Acre. |
| `ANO_CMPT / MES_CMPT` | String (4 / 2) | Ano e mês da competência de processamento da AIH (não é a data da internação). |
| `N_AIH` | String (13) | Número da AIH; chave do registro dentro da competência. Mantido como texto. |
| `IDENT` | String (1) | Tipo da AIH: `1` normal; `5` continuação/longa permanência. |
| `CNES` | String (7) | Código CNES do estabelecimento de saúde que realizou a internação. |
| `MUNIC_RES / MUNIC_MOV` | String (6) | Município de residência do paciente / município do estabelecimento (movimento), código IBGE de 6 dígitos. |
| `NASC / IDADE / COD_IDADE` | String AAAAMMDD / Int / String | Data de nascimento; idade; unidade da idade (`2` dias, `3` meses, `4` anos, `5` > 100 anos). |
| `SEXO` | Inteiro | Sexo do paciente (`1` masculino, `3` feminino, `0`/`9` ignorado). |
| `RACA_COR / ETNIA` | String | Raça/cor (`01` branca, `02` preta, `03` parda, `04` amarela, `05` indígena, `99` sem informação) e etnia indígena. |
| `DT_INTER / DT_SAIDA` | String AAAAMMDD → `pl.Date` | Datas de internação e de saída (alta, transferência ou óbito). |
| `PROC_SOLIC / PROC_REA` | String (10) | Procedimento SIGTAP solicitado e efetivamente realizado (principal da internação). |
| `DIAG_PRINC / DIAG_SECUN / DIAGSEC1–9` | String (CID-10) | Diagnóstico principal, secundário e diagnósticos secundários adicionais; `CID_NOTIF`, `CID_ASSO` e `CID_MORTE` completam as causas. |
| `DIAS_PERM / QT_DIARIAS` | Inteiro | Dias de permanência e quantidade de diárias. |
| `UTI_MES_TO / UTI_INT_TO / MARCA_UTI` | Inteiro / String | Total de diárias de UTI no mês e na internação; tipo de leito de UTI utilizado. |
| `VAL_SH / VAL_SP / VAL_SADT / VAL_UTI / VAL_TOT` | Float | Valores (R$) de serviços hospitalares, profissionais, SADT, UTI e total da AIH. |
| `MORTE` | Inteiro | Indicador de óbito durante a internação (`1` sim, `0` não). |
| `CAR_INT / COBRANCA` | String | Caráter da internação (`01` eletiva, `02` urgência …) e motivo de saída/cobrança (`11` alta curado, `41` óbito etc.). |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios aparecem com 6 dígitos (código IBGE sem dígito verificador, p.ex. `120040`); `wrangle_datasus` mantém como `String` `MUNIC_RES`, `MUNIC_MOV`, `CEP`, `CNES`, `PROC_REA`/`PROC_SOLIC` (SIGTAP, 10 dígitos), `DIAG_PRINC`/`DIAG_SECUN`/`DIAGSEC1–9`/`CID_NOTIF`/`CID_MORTE` (CID-10) e `N_AIH` (13 dígitos). Nunca converta esses campos para inteiro, pois os zeros à esquerda são significativos; para juntar com bases que usam 7 dígitos, calcule o dígito verificador do IBGE ou use a tabela de municípios (`TAB_*.zip`).
- **Valores ausentes e sentinelas**: strings vazias e os literais `999999`, `99999999` e `00000000` (após `strip`) viram `null`; códigos `0000` de CID e `0000000000000` de AIH/APAC permanecem como texto e devem ser tratados manualmente como "não informado". Registros com marca de exclusão dBASE (`_deleted = True`) são descartados e a coluna `_deleted` é removida.
- **Datas e competências**: `DT_INTER` e `DT_SAIDA` estão em `AAAAMMDD` e são convertidas para `pl.Date` (valores inválidos viram `null`). `NASC` **não** consta em `DATE_COLUMNS` e permanece `String` `AAAAMMDD`; converta com `pl.col('nasc').str.to_date('%Y%m%d', strict=False)`. `ANO_CMPT`/`MES_CMPT` seguem como texto e coincidem com o nome do arquivo.
- **Tipos numéricos**: `VAL_*` viram `Float64` (o separador decimal vírgula é normalizado); `IDADE`, `SEXO`, `RACA_COR`, `MORTE` e `DIAS_PERM` viram `Int64`. `COD_IDADE` não é convertida — sempre combine `IDADE` com `COD_IDADE` antes de calcular faixa etária (idade em dias/meses/anos).
- **Particularidades do dataset**: (i) o RD contém apenas AIH **aprovadas**; AIH rejeitadas estão em `sih-rj`/`sih-er` e podem ser reapresentadas e aprovadas em competência posterior, portanto não some RD+RJ sem deduplicar `N_AIH`; (ii) AIH tipo 5 (`IDENT = 5`) repete-se por competência — exclua-as ao contar admissões; (iii) `MUNIC_RES` `999999`/ignorado vira `null`; (iv) UF do arquivo = UF de gestão (`UF_ZI`), não necessariamente a UF de residência — pacientes de outras UFs aparecem em `MUNIC_RES`; (v) valores monetários são nominais da época (não deflacionados) e mudam de regra com a SIGTAP.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sih-rd
quantilica datasus list sih-rd

# 2. Baixar microdados de sih-rd com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sih-rd -o ./data --start 2024-01 --end 2024-12 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sih-rd -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sih-rd -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

# Leitura (descompacta o .dbc em Rust, aplica o saneamento canônico e retorna um pl.DataFrame)
arquivo = next(Path("./data/sih-rd/202401").glob("sih-rd_sp_202401_*.dbc"))
rd = df.read_dbc(arquivo, dataset="sih-rd")

# Internações aprovadas, permanência média e letalidade por diagnóstico principal (CID-10, 3 caracteres)
resumo = (
    rd.filter(pl.col("ident") == "1")                      # só AIH normais (exclui continuação tipo 5)
      .with_columns(pl.col("diag_princ").str.slice(0, 3).alias("cid3"))
      .group_by("cid3")
      .agg(
          pl.len().alias("internacoes"),
          pl.col("dias_perm").mean().alias("permanencia_media"),
          (pl.col("morte").sum() / pl.len()).alias("letalidade"),
          pl.col("val_tot").sum().alias("valor_total"),
      )
      .sort("internacoes", descending=True)
)
print(resumo.head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIHSUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/IT_SIHSUS_1603.pdf`
- **Manual Técnico Operacional do SIH/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **PCDaS/Fiocruz** (SIH/SUS para pesquisa): https://pcdas.icict.fiocruz.br/
- **Portal DATASUS — SIH/SUS (TabNet)**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/ (Assistência à Saúde → Morbidade Hospitalar do SUS).
