# `sinan-sdta` — Surto Doenças Transmitidas por Alimentos

O `sinan-sdta` contém os microdados dos **inquéritos e planilhas de acompanhamento de surtos** de Doenças Transmitidas por Alimentos (DTA — CID-10 A04–A09, inclusive Rotavírus/Norovírus/Adenovírus por veículo comum) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a **planilha consolidada de um surto** — caso típico em que o modo de transmissão provável é indireto/veículo comum — preenchida pela Vigilância Epidemiológica municipal/estadual ao longo da investigação do surto e digitada no SINAN Net/Sinan Online. É a base de agregados epidemiológicos da vigilância de surtos por veículo comum (água e alimentos), com leiaute de 102 colunas: modo e veículo provável de transmissão, contagens de doentes/hospitalizados/óbitos por faixa etária e sexo, sinais e sintomas agregados, tempo de incubação, fatores causais, amostras (clínicas e bromatológicas) e agentes etiológicos/ alimentos implicados — campos agregados voltados à vigilância de surtos.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-sdta` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (bases `FINAIS` históricas e anos recentes apenas em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2018 em `FINAIS` (com lacuna em 2014) e 2019 a 2024 em `PRELIM` (conforme `index.json`) |
| **Volume aproximado no FTP** | 17 arquivos (~1,2 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`, sem arquivo em 2014) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

O componente de vigilância de surtos é operado pela Vigilância Epidemiológica/GVE — municípios, estados e a Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) — nos termos da Lista Nacional de Agravos de Notificação (Portaria GM/MS nº 204/2016) e do Guia de Vigilância em Saúde, com suporte do CIEVS (Centros de Informações Estratégicas em Vigilância em Saúde) para o alerta e o acompanhamento dos eventos de grande porte. No SINAN, surtos por veículo comum (água, alimentos e outros veículos indiretos) são acompanhados por meio das planilhas de investigação de surto — o módulo abre automaticamente a planilha de DTA quando o veículo é alimento/água. Esses registros complementam a vigilância de casos individuais e alimentam os alertas e fichamentos do CIEVS, tornando a base peça central da vigilância epidemiológica de doenças transmitidas por água e alimentos no país.

O evento gerador deste dataset é a **Planilha de Acompanhamento de Surto** do SINAN (ficha de surto de DTA e agravos por veículo comum). A notificação nasce quando o modo provável de transmissão é registrado como indireto/veículo comum (`CS_TRANS` = 2 ou veículo de transmissão provável entre 2 e 9 em `TP_INDIRET`) — inclusive surtos por Rotavírus, Norovírus e Adenovírus por água/alimentos, caso em que a Planilha de DTA é aberta automaticamente pelo sistema. A investigação é completada com: local de produção/preparação (`TP_LOCAL` — domicílio, restaurantes, comemorações, creche/escola, hospital/unidade de saúde); número de entrevistados, doentes, total de doentes e hospitalizações/óbitos (`NU_ENTR`, `NU_ENT_DOE`, `NU_TOT`, `NU_TOT_HOS`, `NU_OBITO`); distribuição de doentes por faixa etária e sexo; sinais e sintomas agregados (náuseas, vômitos, diarreia, cefaleia, abdominais, neurológicos e outros: `NU_NAUSE_P`, `NU_VOMTO_N`, `NU_DIARR_N`, `NU_CEFAL_N`, `NU_ABDOM_N`, `NU_NEURO_N`, `NU_OUTRO_N`, `NU_FEBRE_N`); tempo de incubação (mediana e média, mínimo e máximo); fatores causais (matéria-prima imprópria, conservação inadequada, manipulação incorreta: `ST_IMPRO`, `ST_INAD`, `ST_MANIP`); amostras clínicas e bromatológicas coletadas e resultados (`ST_A_CLINI`, `ST_ALIMEN`, `NU_A_ALIM`); agentes etiológicos etiologia por extenso (`AGENTE_ET1..3`) e alimento suspeito/causal (`ALIMENTO_C`). A unidade de análise é o Surto.

A série histórica de bases `FINAIS` no FTP inicia em **2007** e vai até **2018**, com **lacuna em 2014** (não há arquivo desse ano no FTP); os anos de 2019 a 2024 estão apenas em `PRELIM`. O dicionário de dados do agravo (revisado em fevereiro/2012) remete à planilha de acompanhamento de surto e às regras de abertura automática da Planilha de DTA.

Aplicações analíticas típicas: frequência de surtos por ano e região (UF/least `ID_MUNICIP`); distribuição do local de produção (`TP_LOCAL`) e do veículo (`TP_INDIRET`); atingimento/letalidade do surto (hospitalizações e óbitos `NU_TOT_HOS`, `NU_OBITO` sobre `NU_TOT`); distribuição agregada por doentes (`NU_TOT`) e por sintoma (`NU_*`); tempo de incubação (mediana/média/min/max) por agente (`AGENTE_ET1..3`) e por alimento (`ALIMENTO_C`) e amostras coletadas (`ST_A_CLINI`, `ST_ALIMEN`, `NU_A_ALIM`).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `SDTA` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `SDTA` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `SDTABR24.dbc` — `SDTA` é o prefixo do agravo (Surto DTA), `BR` indica a consolidação nacional de todo o país e `24` é o ano de notificação (2024). A série em `FINAIS` vai de 2007 a 2018 (com lacuna em 2014) e os anos de 2019 a 2024 estão apenas em `PRELIM` (ex.: `SDTABR24.dbc`, atualização de 24/07/2025).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-sdta/<ano>/sinan-sdta_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-sdta/2024/sinan-sdta_preliminar_2024-br@20250724.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip`, as instruções POP_I/II/III de acesso, descompactação e tabulação e os manuais de vigilância de surtos de DTA; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `SDTABR24.dbc` (102 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `SEM_NOT` / `NU_ANO` | Data (`AAAAMMDD`)/Inteiro | Data e semana epidemiológica e ano da notificação do surto |
| `ID_MUNICIP` / `SG_UF` / `ID_MUNI_RE` | String (6/7) | Códigos IBGE de município e UF de notificação e residência |
| `ID_UNIDADE` / `ID_REGIONA` | String 7 | Código CNES da unidade notificante e região de saúde |
| `DT_SIN_PRI` / `SEM_PRI` | Data/Inteiro | Data e semana epidemiológica de início do surto |
| `QT_TOTAL_C` | Inteiro | Total de casos do surto |
| `DT_INVEST` / `DT_DIGITA` | Data (`AAAAMMDD`) | Data da investigação e de digitação |
| `CS_TRANS` | Inteiro | Modo provável de transmissão: 1 - Direta (pessoa a pessoa), 2 - Indireta (veículo comum ou vetor), 9 - Ignorado |
| `TP_INDIRET` | Inteiro | Veículo provável da transmissão indireta: alimento/água (2–3), vetor (3–4), produto (medicamentos, agrotóxicos, imunobiológicos, sangue), fômite (4–5); a Planilha de DTA é aberta quando veículo entre 2 e 9 |
| `TP_LOCAL` | Inteiro | Local de produção/preparação: 01 - Domicílio, 02 - Comemorações, 03 - Creche/Escola, 04 - Hospital/Unidade de Saúde, restaurantes, entre outros |
| `NU_ENTR` / `NU_ENT_DOE` | Inteiro | Número de entrevistados e de doentes pela Vigilância Epidemiológica (doentes ≤ entrevistados) |
| `NU_TOT` / `NU_TOT_HOS` / `NU_OBITO` | Inteiro | Número total de doentes, de hospitalizados e de óbitos |
| `NU_1_M_NU` a `NU_TOT_IGN` / `NU_F_TOT_N` | Inteiro | Distribuição de doentes por faixa etária e sexo (masculino, feminino e sexo ignorado) |
| `NU_NAUSE_P` / `NU_VOMTO_N` / `NU_DIARR_N` / `NU_CEFAL_N` / `NU_ABDOM_N` / `NU_NEURO_N` / `NU_FEBRE_N` / `NU_OUTRO_N` | Inteiro | Número de doentes com cada sinal/sintoma (nauseas, vômitos, diarreia, cefaleia, dores abdominais, sintomas neurológicos, febre, outros) |
| `NU_INCUB_M` / `MAX_INC` / `NU_INC_ME` | Inteiro | Tempo de incubação: mediana máximo, máximo do período e média |
| `ST_INCUB_M` / `ST_INC_ME` | Inteiro | Unidade do tempo de incubação (horas/dias) |
| `TP_PRO_PRE` | Inteiro | Local principal de produção/preparação do alimento implicado no surto |
| `ST_IMPRO` / `ST_INAD` / `ST_MANIP` / `ST_F_OUTRO`/`DS_F_OUTRO` | Inteiro/String | Fatores causais: matéria-prima imprópria, conservação inadequada, manipulação incorreta e outros fator |
| `ST_A_CLINI` / `NU_A_CLINI` / `NU_CLI_NUM` / `NU_NUM_2` / `NU_RESU_3` | Inteiro | Amostras clínicas coletadas, número de amostras e resultados |
| `ST_ALIMEN` / `NU_A_ALIM` / `NU_A_NUM_1..3` | Inteiro | Amostras de alimentos coletadas (bromatológicas), número e resultados |
| `AGENTE_ET1` / `AGENTE_ET2` / `AGENTE_ET3` | String | Agente etiológico identificado (por extenso), até 3 por surto |
| `ALIMENTO_C` | String | Alimento suspeito/causal (por extenso) |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte: 2 - Clínico, 3 - Laboratorial, 4 - Laboratorial Clínico-Bromatológico, 5 - Inconclusivo |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do surto |
| `DTTRANSUS`/`DTTRANS*` / `DT_TRANS*` | Data (`AAAAMMDD`) | Datas de tramitação e trânsito entre níveis do sistema |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP`/`ID_MN_RE` (IBGE, `String` com `zfill`), `ID_UNIDADE` (CNES); os campos de classificação (`CS_TRANS`, `TP_INDIRET`, `TP_LOCAL`, `CRITERIO`) e campos de "fator causal" (`ST_*`) só devem virar categóricos após mapeamento explícito.
- **Datas e competências**: todas as datas (`DT_NOTIFIC`, `DT_SIN_PRI`, `DT_INVEST`, `DT_ENCERRA`, `DT_TRANS*`) vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`); `SEM_NOT`/`SEM_PRI` são semanas epidemiológicas `AAAASS`.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: a base é de **registros agregados por surto** — o cálculo de taxas deve sempre ser feito com as constantes de doentes (`NU_TOT`), hospitalizados (`NU_TOT_HOS`) e óbitos (`NU_OBITO`); a abertura da planilha condiciona-se ao modo de transmissão (`CS_TRANS` = 2 ou veículo indireto 2–9); "agentes etiológicos" (`AGENTE_ET1..3`) e "alimento causal" (`ALIMENTO_C`) são texto longo, *não* códigos de dicionário; e há lacunas no FTP (ausência do arquivo de 2014 em `FINAIS`).

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-sdta
quantilica datasus list sinan-sdta

# 2. Baixar microdados de sinan-sdta com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-sdta -o ./data --start 2007 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-sdta -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-sdta -o ./data/raw --parquet-dir ./data/parquet --start 2007
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-sdta/2024/sinan-sdta_preliminar_2024-br@20250724.dbc", clean=True)

# Surtos por modo provável de transmissão (direta x indireta/veículo comum)
trans = qdf.group_by("cs_trans").len().sort("cs_trans")
print(trans)

# Letalidade hospitalar nos surtos registrados
letal = qdf.select([
    pl.col("nu_tot").sum().alias("doentes"),
    pl.col("nu_tot_hos").sum().alias("hospitalizados"),
    pl.col("nu_obito").sum().alias("obitos"),
])
print(letal)

# Agentes etiológicos mais frequentes (texto livre)
agentes = qdf.group_by("agente_et1").len().sort("len", descending=True)
print(agentes.head(15))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Surtos de DTA (planilha de acompanhamento de surto e dicionário de dados)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de Doenças Transmitidas por Alimentos (DTA) e procedimentos de vigilância epidemiológica de surtos (CIEVS)
