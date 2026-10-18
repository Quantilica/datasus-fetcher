# `sinan-espo` — Esporotricose (Epizootia)

O `sinan-espo` contém os registros de **notificação de epizootias e casos animais** de Esporotricose (dermatofitose por *Sporothrix* spp., transmissível de felinos a humanos) registrados no módulo específico do Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a notificação consolidada de ocorrência de esporotricose em animais (com destaque para felinos, principal reservatório dos surtos urbanos), registrada por unidades de saúde e serviços de zoonoses e digitada no SINAN Net — leiaute compacto de 17 colunas com identificação da notificação, período (semana/mês), local (UF/município), zona e ambiente de ocorrência (`TP_ZN_OCO`/`TP_AMB_OCO`), espécie animal (`ESPECIE`) e indicadores de ocorrência em gatos (`G_D`/`G_M`) e cães (`C_D`/`C_M`) — suporte à Vigilância Integrada em Zoonoses (esporotricose felina/canina e notificação humana) instituída pela Nota Técnica nº 60/2023-CGZV/DEDT.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-espo` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (apenas bases `FINAIS`; sem diretório `PRELIM`) |
| **Cobertura temporal no FTP** | 2013 a 2022, apenas em `FINAIS` (conforme `index.json`) |
| **Volume aproximado no FTP** | 10 arquivos (~0,4 MB) |
| **Arquivos preliminares** | Sim — `meta.py` também consulta `PRELIM`, mas hoje o diretório não contém arquivos do agravo (toda a série está em `FINAIS`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A esporotricose é uma zoonose micótica em expansão no Brasil, associada à transmissão preferencial por felinos domiciliados e errantes (*Sporothrix brasiliensis*), com surtos urbanos reiteradamente descritos desde os anos 1990 (notadamente no Rio de Janeiro). Em 2023, a vigilância do agravo foi normatizada pela **Nota Técnica nº 60/2023-CGZV/DEDT** (Coordenação-Geral de Vigilância das Zoonoses e Doenças de Transmissão Veterinária/DEDT/SVSA), que institui a vigilância integrada de esporotricose em humanos e animais — as epizootias em felinos e cães passam a ser registradas em módulo próprio do SINAN, em regra pelos serviços de zoonoses e pelas unidades de saúde

O evento gerador deste dataset é a ficha de notificação de esporotricose animal do SINAN (módulo de epizootias, referenciado pela Nota Técnica do agravo). Cada registro é uma notificação consolidada por município-semana, com: identificação da notificação (`ID_NOTIFIC`, sequencial), ano (`NU_ANO`), data de notificação e de digitação (`DT_NOTIFIC`, `DT_DIGITA`), UF e município (`SG_UF_NOT`, `ID_MUNICIP`), semanas epidemiológicas de notificação e de início da epizootia (`SEM_NOT`, `SEM_PRI`), data de início da epizootia (`DT_INI_EPI`), zona da ocorrência (`TP_ZN_OCO`: urbana, rural, periurbana, ignorado), ambiente onde ocorreu a epizootia (`TP_AMB_OCO`: 1 - Domicílio, 2 - Parque, praça ou zoológico, 3 - Área Silvestre, 4 - Reserva Ecológica, 5 - Outro, com descrição em `DS_OUT_AMB`), espécie animal afetada (`ESPECIE`, código conforme dicionário — nos dados observados, o valor 1 concentra a vigilância de felinos) e presença de animais sintomáticos/óbitos por espécie: gatos (`G_D` = doentes, `G_M` = mortos) e cães (`C_D` = doentes, `C_M` = mortos), campos binários/contagem conforme a ficha. A unidade de análise é a notificação de epizootia/caso animal.

A série histórica é curta e recente: o FTP contém apenas as bases `FINAIS` de **2013 a 2022** (10 arquivos, sem diretório `PRELIM`), com última atualização em 08/01/2024 (dois arquivos reenviados em 18/01/2024). O volume inicial é minúsculo (arquivo de 2013 com poucas dezenas de registros, concentrados em municípios do Rio de Janeiro — `SG_UF_NOT` 33) e cresce ao longo dos anos: a vigilância de esporotricose animal (notificação por município/felino) se expande nacionalmente nos anos seguintes, via serviços de zoonoses/CIEVS (módulo de "Sistemas Auxiliares" do SINAN — Epizootias).

Aplicações analíticas típicas: evolução do número de notificações por ano/UF (`NU_ANO`, `SG_UF_NOT`); distribuição de zona e ambiente (`TP_ZN_OCO`, `TP_AMB_OCO`) — perfil urbano/domiciliar da esporotricose felina; espécie e indicadores por espécie (`ESPECIE`, gatos vs cães em `G_D`/`C_D`); sazonalidade por semana epidemiológica (`SEM_NOT`, `SEM_PRI`); e correlação com casos humanos de esporotricose em municípios com notificação ativa (vigilância integrada NT 60/2023).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ESPO` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ESPO` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `ESPOBR22.dbc` — `ESPO` é o prefixo do agravo (Esporotricose), `BR` indica a consolidação nacional de todo o país e `22` é o ano de notificação (2022). O agravo publica apenas em `FINAIS`, de 2013 a 2022 (sem `PRELIM`), com atualizações em 08–18/01/2024.
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-espo/<ano>/sinan-espo_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-espo/2022/sinan-espo_2022-br@20240108.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais). A normatização do agravo está na **Nota Técnica nº 60/2023-CGZV/DEDT** (Vigilância da Esporotricose).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `ESPOBR13.dbc` (17 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `ID_NOTIFIC` | Inteiro | Número sequencial da notificação de epizootia/caso animal |
| `NU_ANO` | Inteiro | Ano da notificação |
| `DT_NOTIFIC` / `DT_DIGITA` | Data (`AAAAMMDD`) | Data da notificação e de digitação no SINAN |
| `SG_UF_NOT` / `ID_MUNICIP` | String 2/6 | Código das UF (IBGE) e de município (IBGE) de notificação |
| `SEM_NOT` / `SEM_PRI` | String `AAAASS` | Semanas epidemiológicas de notificação e de início da epizootia |
| `DT_INI_EPI` | Data (`AAAAMMDD`) | Data do início da epizootia (não deve ser maior que a data de notificação) |
| `TP_ZN_OCO` | String (1) | Zona onde ocorreu a epizootia: 1 - Urbana, 2 - Rural, 3 - Periurbana, 9 - Ignorado |
| `TP_AMB_OCO` | String (1) | Ambiente onde ocorreu a epizootia: 1 - Domicílio, 2 - Parque/praça/zoológico, 3 - Área Silvestre, 4 - Reserva Ecológica, 5 - Outro |
| `DS_OUT_AMB` | String (30) | Descrição do outro ambiente (habilitado se `TP_AMB_OCO` = 5) |
| `ESPECIE` | Inteiro | Espécie animal notificada (código conforme ficha; nos dados observados o valor 1 concentra a vigilância de felinos) |
| `G_D` / `G_M` | String (1) | Presença/ocorrência de gatos doentes e de gatos mortos |
| `C_D` / `C_M` | String (1) | Presença/ocorrência de cães doentes e de cães mortos |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` (IBGE, `String` com `zfill`); `TP_ZN_OCO`, `TP_AMB_OCO` e `ESPECIE` são códigos de dicionário e só devem virar categóricos após mapeamento explícito.
- **Datas e competências**: `DT_NOTIFIC`, `DT_DIGITA` e `DT_INI_EPI` vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`); `SEM_NOT`/`SEM_PRI` são semanas epidemiológicas no formato `AAAASS` (texto com ano + semana).
- **Valores ausentes e sentinelas**: códigos ignorados (`9`), o literal `00000000` em datas e espaços em branco viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: base de **notificação de epizootia/casos animais** — não há registros individuais de pacientes, dados clínicos, exames ou desfechos humanos neste dataset (casos humanos de esporotricose migraram para vigilância integrada à parte, via NT 60/2023); cobertura restrita a `FINAIS` 2013–2022 sem arquivos preliminares; e os campos `G_D`/`G_M`/`C_D`/`C_M` frequentemente vêm em branco (ex.: em `ESPOBR13.dbc` `C_D`/`C_M` vazios), exigindo tratamento cuidadoso de nulos para não confundir "sem info" com "não ocorreu".

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-espo
quantilica datasus list sinan-espo

# 2. Baixar microdados de sinan-espo com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-espo -o ./data --start 2013 --end 2022 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-espo -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-espo -o ./data/raw --parquet-dir ./data/parquet --start 2013
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-espo/2022/sinan-espo_2022-br@20240108.dbc", clean=True)

# Notificações por UF e zona de ocorrência
zonas = qdf.group_by(["sg_uf_not", "tp_zn_oco"]).len().sort("sg_uf_not")
print(zonas)

# Ambientes onde ocorreram as epizootias de esporotricose
amb = qdf.group_by("tp_amb_oco").len().sort("tp_amb_oco")
print(amb)

# Municípios com mais notificações no arquivo
mun = qdf.group_by("id_municip").len().sort("len", descending=True)
print(mun.head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Epizootias/Esporotricose (Sistemas Auxiliares do SINAN)**: https://portalsinan.saude.gov.br
- **Nota Técnica nº 60/2023-CGZV/DEDT** (Vigilância da Esporotricose, humana e em animais — CGZV/DEDT/SESSAS/MS)
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de micose cutânea/dermatofitoses e vigilância de zoonoses (zoonoses urbanas)
