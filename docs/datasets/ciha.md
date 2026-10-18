# `ciha` — Sistema de Comunicação de Informação Hospitalar e Ambulatorial

`ciha` é o **Sistema de Comunicação de Informação Hospitalar e Ambulatorial (CIHA)**: cada linha é um atendimento (internação ou ambulatorial) realizado em estabelecimento que não fatura pelo SIH/SIA do SUS, comunicado mensalmente ao DATASUS para que o gestor conheça a totalidade da produção do território. É o sucessor do CIH (2008–2011) e cobre de 2011-01 em diante.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `ciha` — CIHA: Sistema de Comunicação de Informação Hospitalar e Ambulatorial |
| **Código no `datasus-fetcher`** | `ciha` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal (um arquivo por UF e competência) |
| **Cobertura temporal no FTP** | 2011-01 a 2026-07 (conforme `index.json`; 26 UFs com arquivos; última atualização no FTP em 2026-10-13) |
| **Volume aproximado no FTP** | 4.802 arquivos (~5,7 GB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CIHA/201101_/Doc` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CIHA/201101_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O CIHA é mantido pelo Ministério da Saúde/DATASUS (SAES) como **complemento ao SIH e ao SIA** para estabelecimentos que realizam atendimentos mas não são remunerados por esses sistemas (hospitais e ambulatórios privados, filantrópicos com outras formas de contratação, serviços próprios de entes federados, de universidades e de forças armadas, entre outros). Sua finalidade é dar visibilidade, para planejamento e regulação, à oferta assistencial que fica fora do faturamento do SUS.

O evento gerador é o **atendimento comunicado** (internação ou procedimento ambulatorial) pelo estabelecimento ao gestor, no leiaute do CIHA. A unidade de análise é o **atendimento comunicado por competência**: para internações há `DT_SAIDA`, `DIAS_PERM` e `MORTE`; para o ambulatório há `QT_PROC` (quantidade do procedimento). O campo `MODALIDADE` distingue a modalidade de atendimento, `FONTE` indica a fonte do dado e `CGC_CONSOR` identifica consórcio intermunicipal quando aplicável.

O inventário do FTP cobre 2011-01 a 2026-07 (26 UFs, ~5,7 GB, 4.802 arquivos). O CIHA nasceu como evolução do CIH (`cih-cr`), incorporando o atendimento ambulatorial. O leiaute tem 31 colunas, parecido com o do SIH/RD mas sem campos de valor financeiro e com `DT_ATEND` (data do atendimento) no lugar de `DT_INTER`. A tabela de procedimentos acompanha a SIGTAP (`PROC_REA`, 10 dígitos) e o CID é o CID-10.

Aplicações: ampliar a cobertura das estatísticas de morbidade hospitalar e de produção ambulatorial com os estabelecimentos não-SUS; estimar a oferta total de serviços e a ocupação da rede privada; análise de fluxos de pacientes (`MUNIC_RES` vs. `MUNIC_MOV`); perfil de diagnósticos (`DIAG_PRINC`) e permanência; e subsídio à regulação e ao planejamento regional, em conjunto com o CNES.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CIHA/201101_/Dados` | `CIHA` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `CIHASP2401.dbc` — `CIHA` (prefixo do sistema, 4 letras) + `SP` (UF) + `24` (ano 2024) + `01` (mês de competência).
- **No armazenamento local do `datasus-fetcher`**: `data/ciha/<AAAAMM>/ciha_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/ciha/202401/ciha_sp_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Layout_Arquivos_CIHA.pdf` (leiaute oficial, 10 KB, 2014) descreve os campos; `Auxiliar/TAB_CIHA.zip` (~68,8 MB, tabelas de procedimento, CID, município e conversores `.cnv`).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

31 colunas no arquivo de 2024-01 (`CIHAAC2401.dbc`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `ANO_CMPT / MES_CMPT` | String (4 / 2) | Ano e mês da competência da comunicação. |
| `ESPEC` | String | Especialidade do leito/atendimento. |
| `CGC_HOSP` | String (14) | CNPJ do estabelecimento comunicante. |
| `CNES` | String (7) | Código CNES do estabelecimento. |
| `MUNIC_RES / MUNIC_MOV` | String (6) | Município de residência do paciente e do estabelecimento. |
| `NASC / IDADE / COD_IDADE` | String AAAAMMDD / Int / String | Data de nascimento, idade e unidade da idade. |
| `SEXO` | Inteiro | Sexo (`1` masculino, `3` feminino, `0`/`9` ignorado). |
| `PROC_REA / QT_PROC` | String (10) / Inteiro | Procedimento realizado (SIGTAP) e quantidade. |
| `DT_ATEND / DT_SAIDA` | String AAAAMMDD → `pl.Date` | Datas do atendimento/internação e da saída. |
| `DIAG_PRINC / DIAG_SECUN` | String (CID-10) | Diagnósticos principal e secundário. |
| `DIAS_PERM` | Inteiro | Dias de permanência (internações). |
| `UTI_MES_TO / UTI_INT_TO` | Inteiro | Dias de UTI no mês e na internação. |
| `MORTE` | Inteiro | Indicador de óbito. |
| `CAR_INT / COBRANCA / NATUREZA / GESTAO` | String | Caráter do atendimento, motivo de saída/cobrança, natureza e gestão do estabelecimento. |
| `FONTE / CGC_CONSOR / MODALIDADE / HOMONIMO` | String | Fonte da informação, CNPJ do consórcio, modalidade do atendimento e indicador de homônimo. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios aparecem com 6 dígitos (código IBGE sem dígito verificador, p.ex. `120040`); `wrangle_datasus` mantém como `String` `MUNIC_RES`, `MUNIC_MOV`, `CEP`, `CNES`, `PROC_REA`/`PROC_SOLIC` (SIGTAP, 10 dígitos), `DIAG_PRINC`/`DIAG_SECUN`/`DIAGSEC1–9`/`CID_NOTIF`/`CID_MORTE` (CID-10) e `N_AIH` (13 dígitos). Nunca converta esses campos para inteiro, pois os zeros à esquerda são significativos; para juntar com bases que usam 7 dígitos, calcule o dígito verificador do IBGE ou use a tabela de municípios (`TAB_*.zip`).
- **Valores ausentes e sentinelas**: strings vazias e os literais `999999`, `99999999` e `00000000` (após `strip`) viram `null`; códigos `0000` de CID e `0000000000000` de AIH/APAC permanecem como texto e devem ser tratados manualmente como "não informado". Registros com marca de exclusão dBASE (`_deleted = True`) são descartados e a coluna `_deleted` é removida.
- **Datas e competências**: `DT_ATEND` e `DT_SAIDA` estão em `DATE_COLUMNS` e são convertidas de `AAAAMMDD` para `pl.Date`; `NASC` permanece texto `AAAAMMDD`. Para atendimentos ambulatoriais `DT_SAIDA` pode coincidir com `DT_ATEND` ou vir vazio. A competência é `ANO_CMPT`/`MES_CMPT`.
- **Tipos numéricos**: `IDADE`, `SEXO`, `MORTE`, `DIAS_PERM` → `Int64`. `QT_PROC` não consta em `INTEGER_COLUMNS` (apenas `QTDE_PROC`): converta com `cast(pl.Int64, strict=False)`. `IDADE` deve ser interpretada junto de `COD_IDADE`.
- **Particularidades do dataset**: (i) mistura internação e atendimento ambulatorial — distinga-os por `MODALIDADE` e pela presença de `DIAS_PERM`/`DT_SAIDA`; (ii) não há `N_AIH` nem valores financeiros; (iii) apenas 26 UFs com arquivos; a participação varia entre estados e muda ao longo do tempo (o envio é obrigatório para estabelecimentos fora do SIH/SIA, mas a adesão não é uniforme); (iv) não some `ciha` a `sih-rd` sem verificar se o estabelecimento (`CNES`) já fatura no SIH, para evitar dupla contagem.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para ciha
quantilica datasus list ciha

# 2. Baixar microdados de ciha com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync ciha -o ./data --start 2024-01 --end 2024-12 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync ciha -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline ciha -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/ciha/202401").glob("ciha_sp_202401_*.dbc"))
ciha = df.read_dbc(arquivo, dataset="ciha")

# Atendimentos por modalidade e estabelecimento
q = (
    ciha.group_by("modalidade", "cnes")
        .agg(pl.len().alias("atendimentos"), pl.col("morte").sum().alias("obitos"))
        .sort("atendimentos", descending=True)
)
print(q.head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CIHA/201101_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Layout oficial do CIHA**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CIHA/201101_/Doc/Layout_Arquivos_CIHA.pdf`
- **Tabelas auxiliares CIHA**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CIHA/201101_/Auxiliar/TAB_CIHA.zip`
- **Biblioteca Virtual em Saúde do Ministério da Saúde** (normas e manuais do SIH/SIA/CIHA): https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz**: https://pcdas.icict.fiocruz.br/
