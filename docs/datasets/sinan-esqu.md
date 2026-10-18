# `sinan-esqu` — Esquistossomose

O `sinan-esqu` contém os microdados das notificações e investigações epidemiológicas de casos de Esquistossomose mansoni (CID-10 B65.x) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de esquistossomose, preenchida pelas unidades de saúde de todo o país (com concentração histórica nas áreas endêmicas do Nordeste e Sudeste) e digitada no SINAN Net/Sinan Online. É a única base do SINAN com foco em doença parasitária crônica e laboratório de parasitologia (Kato-Katz), com 53 colunas: exames parasitológicos (Análise Quantitativa — número de ovos no Kato-Katz; Análise Qualitativa — Hoffman; e outros exames), quadro clínico e forma de apresentação (intestinal, hepato-intestinal, hepatoesplênica, aguda), tratamento (praziquantel/oxamniquine, e motivo da não realização), verificação de cura em até 3 amostras e a geolocalização da fonte provável de infecção (com nome de propriedade rural e coleção hídrica).

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-esqu` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (bases `FINAIS` históricas e anos recentes apenas em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 20 arquivos (~8,4 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) em articulação com as Vigilâncias em Saúde dos estados e municípios das áreas endêmicas — bolsões históricos no Nordeste (Pernambuco, Bahia, Alagoas, Sergipe) e Sudeste (Minas Gerais e Espírito Santo) — e é complementada pelo Programa de Vigilância e Controle da Esquistossomose (PCE). A transmissão se dá por contato com coleções hídricas contaminadas com larvas (cercárias) de *Schistosoma mansoni*, liberadas por caramujos *Biomphalaria* — o que amarra a vigilância epidemiológica a fatores de saneamento, uso de água para trabalho (trabalhadores rurais), lazer e irrigação.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Esquistossomose** do SINAN Net (dicionário de dados v5.0, seções específicas revisadas em março/2012). A notificação nasce com a suspeição clínico-laboratorial e a confirmação se dá por exames parasitológicos de fezes: a **Análise Quantitativa (Kato-Katz)** registra a carga parasitária em ovos (`AN_QUANT`: 0 - 0 ovos; 1 - 1 ou mais ovos) e a **Análise Qualitativa (Hoffman)** o resultado do exame qualitativo (`AN_QUALI`: 1 - Positivo, 2 - Negativo, 3 - Não realizado), com data da coproscopia (`DT_COPRO`) e outros exames (`OUTROS`/`OUTRO_EX`). A investigação é completada com: a forma clínica (`FORMA`: 1 - Intestinal, 2 - Hepato-intestinal, 3 - Hepatoesplênica, 4 - Aguda, 5 - Outra, com descrição em `DS_FORMA`); o tratamento (realizado — praziquantel ou oxamniquine — `TRATAM` e `DTTRAT`, ou o motivo da não realização: contra-indicação, recusa ou ausente em `TRATANAO`); a verificação de cura em até 3 amostras (`STCURA1`, `STCURA2`, `STCURA3`: 0 - zero ovos, 1 - um ou mais ovos, 2 - Não realizado, com datas `DT_RESU3`); e a localização da fonte provável de infecção — UF, país, município, distrito, bairro (`COUFINF`, `COPAISINF`, `COMUNINF`, `CODISINF`, `CO_BAINFC`/`NOBAIINF`), nome da propriedade rural (`NOPROPIN`) e nome da coleção hídrica onde ocorreu a transmissão (`NOCOLINF`), campos essenciais para o mapeamento dos focos. A unidade de análise é o caso notificado.

A série histórica em `FINAIS` inicia em **2007** (implantação nacional do Sinan Net) e vai até **2022**; os anos de 2023 a 2026 estão apenas em `PRELIM` (ex.: `ESQUBR26.dbc`, atualização de 02/06/2026). O agravo autóctone é assinalado em `TPAUTOCTO` (1 - Sim, o sistema preenche automaticamente UF/país/município com os da residência; 2 - Não; 3 - Indeterminado) — mecanismo central para a distinção entre casos de transmissão local e casos em que a infecção ocorreu em outra área (não endêmica no município de residência). A cada caso notificado é possível o acompanhamento longitudinal do tratamento e da cura (até 3 amostras de fezes), o que permite estimar a efetividade do tratamento (cura parasitológica) e a recrudescência de carga parasitária em áreas de reinfecção.

Aplicações analíticas típicas: carga total de ovos por caso (Kato-Katz) e sua evolução por região endêmica; distribuição de formas clínicas (`FORMA`, com destaque para a forma hepatoesplênica/sévera); cobertura e resultado de tratamento (`TRATAM`, `TRATANAO`) e taxa de cura parasitológica (`STCURA1..3` — "0 ovos" na amostra de controle); mapeamento de focos de transmissão pela coleção hídrica e propriedade (`NOCOLINF`, `NOPROPIN`, local `COUFINF`/`COMUNINF`); estudo da autoctonia (`TPAUTOCTO`) e do risco associado ao trabalho (`DOENCA_TRA`); e letalidade (`EVOLUCAO`: 1 - Cura, 2 - Não Cura, 3 - Óbito por esquistossomose, 4 - Óbito por outras causas, 9 - Ignorado).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ESQU` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ESQU` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `ESQUBR25.dbc` — `ESQU` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). A série em `FINAIS` vai de 2007 a 2022 e os anos de 2023 a 2026 estão apenas em `PRELIM` (ex.: `ESQUBR26.dbc`, atualização de 02/06/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-esqu/<ano>/sinan-esqu_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-esqu/2026/sinan-esqu_preliminar_2026-br@20260602.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip`, as instruções POP_I/II/III de acesso, descompactação e tabulação e a ficha/dicionário de esquistossomose; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `ESQUBR24.dbc` (53 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` / `DT_NOTIFIC` / `SEM_NOT` / `NU_ANO` | Data/Inteiro | Tipo de notificação, data, semana epidemiológica e ano |
| `ID_MUNICIP` / `SG_UF` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município e UF de notificação e residência |
| `ID_UNIDADE` / `ID_REGIONA` | String | Código CNES da unidade notificante e região de saúde |
| `DT_SIN_PRI` / `SEM_PRI` | Data/Inteiro | Data e semana de início dos sintomas |
| `NU_IDADE_N` / `CS_SEXO` / `CS_GESTANT` / `CS_RACA` / `CS_ESCOL_N` | Inteiro/String | Idade decomposta, sexo, gestação, raça/cor e escolaridade |
| `DT_INVEST` / `ID_OCUPA_N` | Data/Inteiro | Data da investigação e ocupação (CBO — relevante no agravo: trabalhadores rurais) |
| `DT_COPRO` | Data (`AAAAMMDD`) | Data da coproscopia |
| `AN_QUANT` | Inteiro | Análise Quantitativa (Kato-Katz): número de ovos — 0 - 0 (zero) ovos, 1 - 1 (um) ou mais ovos |
| `AN_QUALI` | Inteiro | Análise Qualitativa (Hoffman): 1 - Positivo, 2 - Negativo, 3 - Não realizado |
| `OUTROS` / `OUTRO_EX` | Inteiro/String | Resultado de outros exames parasitológicos e sua especificação |
| `TRATAM` | Inteiro | Fez tratamento? (1 - Sim, 3 - Não, 9 - Ignorado) |
| `DTTRAT` | Data (`AAAAMMDD`) | Data do tratamento |
| `TRATANAO` | Inteiro | Motivo do não tratamento: 1 - Contra-indicação, 2 - Recusa, 3 - Ausente, 9 - Ignorado |
| `STCURA1` / `STCURA2` / `STCURA3` | Inteiro | Verificação de cura (1ª, 2ª e 3ª amostra): 0 - 0 (zero) ovos, 1 - 1 (um) ou mais ovos, 2 - Não realizado |
| `DT_RESU3` | Data (`AAAAMMDD`) | Data do resultado da análise de verificação de cura (3ª amostra) |
| `FORMA` | Inteiro | Forma clínica: 1 - Intestinal, 2 - Hepato-intestinal, 3 - Hepatoesplênica, 4 - Aguda, 5 - Outra |
| `DS_FORMA` | String | Descrição da outra forma clínica (quando `FORMA` = 5) |
| `TPAUTOCTO` | Inteiro | O caso é autóctone do município de residência? 1 - Sim (preenche automaticamente UF/país/município da fonte de infecção), 2 - Não, 3 - Indeterminado |
| `COUFINF` / `COPAISINF` / `COMUNINF` / `CODISINF` | String | UF, país, município e distrito prováveis da fonte de infecção |
| `CO_BAINFC` / `NOBAIINF` | String | Bairro provável da fonte de infecção (código ou nome digitado) |
| `NOPROPIN` | String | Nome da propriedade onde ocorreu a transmissão (área rural) |
| `NOCOLINF` | String | Nome da coleção hídrica onde ocorreu a transmissão |
| `DOENCA_TRA` | Inteiro | Doença relacionada ao trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `EVOLUCAO` | Inteiro | Evolução do caso: 1 - Cura, 2 - Não Cura, 3 - Óbito por esquistossomose, 4 - Óbito por outras causas, 9 - Ignorado |
| `DT_OBITO` / `DT_ENCERRA` / `DT_DIGITA` | Data (`AAAAMMDD`) | Data do óbito, de encerramento do caso e de digitação |
| `DT_TRANS*` | Data (`AAAAMMDD`) | Datas de tramitação e trânsito entre níveis do sistema |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE, `String` com `zfill`), `ID_UNIDADE` (CNES), `ID_OCUPA_N` (CBO), `COMUNINF` (município IBGE da fonte de infecção); códigos de classificação (`FORMA`, `TRATAM`, `TRATANAO`, `EVOLUCAO`, `TPAUTOCTO`) só viram categóricos após mapeamento explícito.
- **Datas e competências**: todas as datas (`DT_NOTIFIC`, `DT_SIN_PRI`, `DT_INVEST`, `DT_COPRO`, `DTTRAT`, `DT_RESU3`, `DT_OBITO`, `DT_ENCERRA`) vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`); `SEM_NOT`/`SEM_PRI` são semanas epidemiológicas `AAAASS`.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: a verificação de cura usa a codificação "0/1" (número de ovos) e não "positivo/negativo" — diferente de `AN_QUALI`/`OUTROS` (1 - Positivo/2 - Negativo/3 - Não realizado), o que exige mapeamentos distintos; `AN_QUANT` = 0 pode significar "negativo" ou resultado de cura, e o campo só distingue presença/ausência de ovos (não a carga exata); os campos de fonte de infecção são preenchidos automaticamente quando `TPAUTOCTO` = 1 (durante análises, filtrar casos autóctones separa transmissão local de importação); `NOPROPIN` e `NOCOLINF` são texto livre (nome de propriedade e coleção hídrica) e exigem normalização para estudos de focos.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-esqu
quantilica datasus list sinan-esqu

# 2. Baixar microdados de sinan-esqu com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-esqu -o ./data --start 2007 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-esqu -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-esqu -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-esqu/2022/sinan-esqu_2022-br@20260602.dbc", clean=True)

# Formas clínicas dos casos notificados
formas = qdf.group_by("forma").len().sort("forma")
print(formas)

# Taxa de cura verificada na 1ª amostra de controle (0 ovos)
curados = qdf.filter(pl.col("stcura1") == 0).shape[0]
examinados = qdf.filter(pl.col("stcura1").is_in([0, 1])).shape[0]
print(curados / examinados)

# Distribuição por ocupação (trabalhadores rurais)
ocupa = qdf.group_by("id_ocupa_n").len().sort("len", descending=True)
print(ocupa.head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Esquistossomose (ficha e dicionário de dados v5.0, rev. março/2012)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de Esquistossomose (Programa de Vigilância e Controle da Esquistossomose, PCE)
