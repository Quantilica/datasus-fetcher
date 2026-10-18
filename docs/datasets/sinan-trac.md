# `sinan-trac` — Inquérito de Tracoma

Registros de inquéritos populacionais de tracoma (busca ativa de casos) conduzidos no âmbito da vigilância epidemiológica e registrados no SINAN. Cada linha representa o resultado do exame oftalmológico de um indivíduo examinado durante um inquérito domiciliar, escolar ou comunitário.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-trac` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido) |
| **Particionamento** | `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2009 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 18 arquivos (~1,8 MB) |
| **Arquivos preliminares** | Sim (diretório PRELIM, 2025–2026; Finais até 2024) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

O inquérito de tracoma integra o Programa de Vigilância e Controle do Tracoma da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), alinhado à meta da OMS de eliminação do tracoma como problema de saúde pública até 2030. O tracoma é uma ceratoconjuntivite crônica causada por *Chlamydia trachomatis*, doença tropical negligenciada associada a condições precárias de saneamento, aglomeração e higiene, com maior prevalência em áreas rurais, ribeirinhas e periferias urbanas.

O evento gerador é o exame oftalmológico realizado em massa durante inquéritos de busca ativa, com o objetivo de estimar a prevalência de tracoma, especialmente a forma folicular (TF) em crianças de 1 a 9 anos — indicador-chave de eliminação. A unidade de análise é o **indivíduo examinado** (um registro por pessoa), e não apenas os casos confirmados; por isso a base é mais ampla que a notificação individual. O diagnóstico segue a classificação OMS (TF, TI, TS, TT, CO).

O instrumento é a *Ficha de Inquérito de Tracoma*, que registra dados do município e localidade investigada, características do indivíduo examinado (idade, sexo, escola), data do exame, resultado por olho (direito/esquerdo), forma clínica e tratamento. A série no FTP inicia em 2009; os dados de 2025 e 2026 estão em PRELIM e sujeitos a revisão.

Principais usos: cálculo de prevalência de tracoma e de TF em crianças, monitoramento de indicadores de eliminação, avaliação de campanhas de tratamento em massa com azitromicina e priorização de municípios e localidades para intervenção (saneamento, educação em saúde e busca ativa).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `TRAC` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `TRAC` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `TRACBR24.dbc`, em que `TRAC` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-trac/<partição>/sinan-trac_br_2009_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`Inquérito de Tracoma`) é distribuído no Portal SINAN; não há PDF por agravo no FTP.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

As colunas abaixo foram extraídas do cabeçalho do arquivo mais recente (`TRACBR26.dbc`). Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação do registro. |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado (A71). |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | String | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE, 6 dígitos). |
| `ID_REGIONA` | String | Código da regional de saúde. |
| `ID_UNIDADE` | String | Código CNES da unidade responsável (7 dígitos). |
| `CS_INQUERI` | String | Tipo de inquérito realizado. |
| `NU_CASO` | Inteiro | Número de casos registrados. |
| `SG_UF` | String | UF de residência (código IBGE de 2 dígitos). |
| `ID_MUNI_RE` | String | Município de residência (código IBGE, 6 dígitos). |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `NU_IDADE_N` | Inteiro | Idade. |
| `FORMA_TF` / `FORMA_TI` / `FORMA_TS` / `FORMA_TT` / `FORMA_CO` | String | Indicadores das formas clínicas: TF (folicular), TI (inflamatório intenso), TS (cicatricial), TT (triquíase) e CO (opacificação da córnea). |
| `ENCAMINHA` | String | Encaminhamento do examinado. |
| `DT_DIGITA` | Data (AAAAMMDD) | Data de digitação do registro. |
| `DT_TRANSUS` / `DT_TRANSDM` / `DT_TRANSSM` / `DT_TRANSRM` / `DT_TRANSRS` / `DT_TRANSSE` | Data (AAAAMMDD) | Datas de transferência do registro entre as esferas do SINAN (US, distrital/municipal, estadual/regional, federal). |
| `NU_LOTE_V` / `NU_LOTE_H` | String | Números dos lotes de transferência vertical e horizontal. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios (`ID_MUNICIP`) usam código IBGE de 6 dígitos; `ID_UNIDADE` é CNES de 7 dígitos; `SG_UF_NOT` é código IBGE de 2 dígitos. `ID_AGRAVO` (CID-10) deve ficar como `String`, mantendo zeros à esquerda (`zfill`).
- **Datas e competências**: datas `DT_*` são gravadas em `AAAAMMDD` nos DBF e convertidas para `pl.Date`. 
- **Valores ausentes e sentinelas**: o SINAN usa `9`, `99`, `999` e `I` (ignorado) como categorias válidas; elas **não** são nulos automáticos. Espaços em branco e `""` viram nulos, e registros marcados como excluídos no dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: este é o **inquérito** (busca ativa, indivíduos examinados), distinto da **notificação individual** de casos em `sinan-ntra`. O denominador é o número de examinados, e a base não deve ser usada para contagem de casos notificados. Os leiautes variam substancialmente entre campanhas, especialmente nos indicadores de forma clínica (`FORMA_*`). Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` ou `ID_MUNICIP` conforme a pergunta. Arquivos do diretório PRELIM (2025+) são preliminares; deduplique com cautela ao combinar as fontes.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-trac
quantilica datasus list sinan-trac

# 2. Baixar microdados de sinan-trac (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-trac -o ./data --start 2015 --end 2022 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-trac -o ./data --docs --aux --start 2015 --end 2022 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-trac -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2022 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/TRACBR22.dbc", dataset="sinan-trac")

# Total de examinados por UF e ano (denominador do inquérito)
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("examinados"))
    .sort("sg_uf_not", "nu_ano")
)

# Resultado do exame e zona
print(frame.group_by("zona").agg(pl.len().alias("n")).sort("n", descending=True))
print(resumo.head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do inquérito (Inquérito de Tracoma): https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Tracoma: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- OMS — Eliminação do tracoma como problema de saúde pública (metas 2030): https://www.who.int/health-topics/trachoma
