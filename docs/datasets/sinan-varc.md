# `sinan-varc` — Varicela

O `sinan-varc` contém os microdados das notificações de casos suspeitos/descartados de Varicela (CID-10 B01) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação de um caso, em leiaute compacto da ficha básica de notificação (42 colunas no arquivo verificado), cobrindo identificação do caso, pessoa, endereço, classificação final, critério, autoctonia e trabalho. É a base de morbidade de varicela no país, publicada no FTP exclusivamente em consolidações preliminares (não há bases `FINAIS` para o agravo) — leiaute e política de notificação refletem que a varicela é notificada de forma universal apenas em situações de surto e/ou óbito.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-varc` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2007 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 20 arquivos (~35,9 MB) |
| **Arquivos preliminares** | Sim — todos os arquivos estão em `PRELIM`; `meta.py` também consulta `FINAIS`, que hoje não contém arquivos do agravo |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A varicela (catapora) é agravo de notificação compulsória em situações de surto e/ou óbito desde o início da vigilância nacional brasileira (Lei nº 6.259/1975 e Decreto nº 78.231/1976), e seu acompanhamento analítico é responsabilidade da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) em conjunto com o GT-SINAN e o Programa Nacional de Imunizações — o registro de casos é fundamental para a avaliação da vacinação programática do calendário do PNI e a gestão das formas graves em imunossuprimidos. A base alimenta a vigilância do excesso de morbidade sazonal (pico no outono/inverno), a investigação de formas graves e de surtos em escolas e demais locais de convivência.

O evento gerador deste dataset é a **Ficha de Notificação de Varicela** do SINAN (ficha básica, no padrão gvIMS do SINAN). A notificação é individual, com o campo `ID_AGRAVO` marcando o CID-10 B01, data dos primeiros sintomas e demografia do caso — não há blocos laboratoriais complexos nem ficha de investigação epidemiológica dedicada como nas fichas de agravos de notificação universal. A unidade de análise é o caso notificado, e o encerramento ocorre com classificação final (confirmado/descartado) e critério de confirmação (laboratorial ou clínico-epidemiológico, mais comum em surtos).

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. A base é publicada e revisada no ciclo de atualização corrente — todas as consolidações estão em `PRELIM`. Mudanças recentes de instrumento refletem a institucionalização da notificação de surtos e óbitos (com alinhamento ao Guia de Vigilância e às notas técnicas da vigilância de doenças inume-preventíveis da CGVDI/DPNI sobre o manejo da varicela), mantendo o leiaute compacto da ficha básica e facilitando a comparação ao longo de toda a série.

Aplicações analíticas típicas: curvas epidêmicas por semana de início dos sintomas (`SEM_PRI`); distribuição por faixa etária e sexo; surtos detectados por município/UF (`ID_MUNICIP`, `SG_UF_NOT`); letalidade em casos notificados com `DT_OBITO` (raro, mas crítico); casos associados à fonte de infecção fora do município de residência (`COUFINF`/`COMUNINF`); e, como não há bloco de antecedentes vacinais na ficha, estudos de efetividade da vacina consomem esta base em conjunto com os registros do PNI (SI-PNI).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `VARC` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `VARC` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `VARCBR07.dbc` — `VARC` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `07` é o ano de notificação (2007). Não há arquivos em `FINAIS` para o agravo: toda a série (2007 a 2026) está em `PRELIM` (ex.: `VARCBR26.dbc`, atualização de 01/10/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-varc/<ano>/sinan-varc_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-varc/2026/sinan-varc_preliminar_2026-br@20261001.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `VARCBR07.dbc` (42 colunas depois de remover `_deleted`) — leiaule compacto, baseado na ficha básica de notificação do SINAN.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual, 3 - Surto e outros) |
| `ID_AGRAVO` | String | Código do agravo conforme CID-10 (B01) |
| `DT_NOTIFIC` | Data (`AAAAMMDD`) | Data de preenchimento da ficha de notificação |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano da notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_REGIONA` | String (7) | Código do município de referência regional |
| `ID_UNIDADE` | String (7) | Código CNES da unidade de saúde notificadora |
| `DT_SIN_PRI` / `SEM_PRI` | Data / Inteiro | Data e semana epidemiológica de início dos sintomas |
| `ANO_NASC` | Inteiro | Ano de nascimento do paciente |
| `NU_IDADE_N` | Inteiro composto | Idade (o primeiro dígito indica a unidade: dia/mês/ano) |
| `CS_SEXO` / `CS_GESTANT`/`CS_RACA`/`CS_ESCOL_N` | String/Inteiro | Sexo, gestação (feminino), raça/cor e escolaridade |
| `SG_UF` / `ID_MN_RESI` / `ID_RG_RESI` / `ID_PAIS` | String | UF, município, regional e país de residência |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `ID_OCUPA_N` | String (6) | Código CBO da ocupação do paciente |
| `CLASSI_FIN` | Inteiro | Classificação final do caso (confirmado/descartado) |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte (laboratorial, clínico-epidemiológico ou em investigação) |
| `TPAUTOCTO` | Inteiro | O caso é autóctone do município de residência (1 - Sim, 2 - Não, 3 - Indeterminado) |
| `COUFINF`/`COPAISINF`/`COMUNINF` | String | UF, país e município prováveis da fonte de infecção |
| `DOENCA_TRA` | Inteiro | Doença relacionada ao trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` / `DT_ENCERRA` / `DT_DIGITA` | Data (`AAAAMMDD`) | Data do óbito, de encerramento do caso e de digitação |
| `MIGRADO_W` / `TP_SISTEMA` / `TPUNINOT` | Inteiro | Indicadores do sistema de origem (registro migrado do Sinan-Windows) e da unidade notificadora |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE, `String` com `zfill`), `ID_UNIDADE` (CNES), `ID_OCUPA_N` (CBO); códigos de classificação (`CLASSI_FIN`, `CRITERIO`, `EVOLUCAO`, `TPAUTOCTO`) só viram categóricos após mapeamento explícito.
- **Datas e competências**: `DT_NOTIFIC`, `DT_SIN_PRI`, `DT_INVEST`, `DT_OBITO`, `DT_ENCERRA` e `DT_DIGITA` vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`); `SEM_NOT`/`SEM_PRI` são semanas epidemiológicas `AAAASS`.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: toda a série está em `PRELIM` (sem consolidações `FINAIS` publicadas), com risco maior de revisão retroativa dos dados; o leiaute é o da ficha básica de notificação (sem bloco laboratorial e sem registro detalhado de doses da vacina), o que limita estudos de efetividade vacinal a partir desta base isolada; e, por se tratar de notificação compulsória restrita a surtos e/ou óbitos, a base é sensível ao comportamento de notificação de surtos — não representa a incidência endêmica da doença.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-varc
quantilica datasus list sinan-varc

# 2. Baixar microdados de sinan-varc com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-varc -o ./data --start 2007 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-varc -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-varc -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-varc/2007/sinan-varc_preliminar_2007-br@20240522.dbc", clean=True)

# Distribuição das notificações por ano de notificação e sexo
print(qdf.group_by(["nu_ano", "cs_sexo"]).len().sort(["nu_ano", "cs_sexo"]))

# Casos com evolução fatal
obitos = qdf.filter(pl.col("evolucao") == 2)
print(obitos.select(["nu_ano", "sg_uf_not", "dt_obito"]))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Varicela (ficha de notificação)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de varicela/doenças exantemáticas; Notas técnicas da CGVDI/DPNI sobre notificação de surtos e manejo de casos de varicela
