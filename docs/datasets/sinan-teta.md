# `sinan-teta` — Tétano Acidental

O `sinan-teta` contém os microdados das notificações e investigações epidemiológicas de casos de Tétano Acidental (CID-10 A35) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de tétano acidental, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. É uma base de baixa incidência (a doença é evitável por vacinação) mas com leiaute detalhado (66 colunas na v5.0) que documenta a possível porta de entrada do agente (ferimento, queimadura, abortamento séptico, cirurgia), o estado vacinal do paciente, as manifestações clínicas (trismo, riso sardônico, opistótono, rigidez), a profilaxia pós-exposição e o desfecho do caso.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-teta` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (bases `FINAIS` históricas e anos recentes apenas em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 20 arquivos (~0,8 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

O tétano acidental é agravo de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, constando hoje da Lista Nacional de Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) em articulação com o GT-SINAN e o Programa Nacional de Imunizações (vacinas DTP/DT/dT/TD e imunização antitetânica). O agravo é distinto do tétano neonatal (dataset `sinan-tetn`), pois monitora casos em qualquer idade com porta de entrada por lesão (excluído o período neonatal e o cordão umbilical); os indicadores oficiais incluem incidência, letalidade e a proporção de casos com esquema vacinal incompleto, bem como a identificação de municípios com falhas de cobertura vacinal — em especial nos grupos vulneráveis (gestantes e idosos).

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Tétano Acidental** do SINAN. A notificação nasce com a suspeição clínica (trismo, riso sardônico, opistótono, rigidez de nuca ou abdômen "em prancha" associada a ferimento nos 21 dias anteriores) e é completada ao longo da investigação com o registro da possível porta de entrada (`TP_CAUSA`, com descrição quando "outros"), o local da lesão (`TP_LOCALLE`), o estado vacinal (`NU_DOSE` e `DT_ULT_DOS`, incluindo "nunca vacinado"), a profilaxia/tratamento específico utilizados (`TP_PROFILA`: soro antitetânico, imunoglobulina, vacina ou antibiótico), as manifestações clínicas e o desfecho do caso (cura, óbito, e o local provável da fonte de infecção). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. Revisões do dicionário datam de fevereiro/2012 e organizaram as opções de dose aplicada, profilaxia e medidas de análise (imunização de pessoas vulneráveis), além dos campos de fonte de infecção (domicílio, trabalho, via pública, escola, campo, unidade de saúde ou outro local: `CS_LOCAL`) e do caso ser autóctone de residência (`TPAUTOCTO`), o que permite estudar o território de exposição.

Aplicações analíticas típicas: incidência e letalidade por faixa etária (adultos idosos concentram os casos); percentual de casos "nunca vacinados" ou com esquema incompleto (`NU_DOSE`); distribuição das portas de entrada e locais de infecção (`TP_CAUSA`, `TP_LOCALLE`, `CS_LOCAL`); uso de profilaxia pós-exposição `SAT/IG`/vacina/antibiótico (`TP_PROFILA`) e estudo da brecha entre ferimento recente (checklist de 21/30 dias) e admissão tardia na rede; e comparativo com o tétano neonatal (`sinan-tetn`) e o tétano por outras causais de outros grupos.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `TETA` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `TETA` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `TETABR25.dbc` — `TETA` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As consolidações até 2023 estão em `FINAIS` e os anos de 2024 a 2026 estão apenas em `PRELIM` (ex.: `TETABR26.dbc`, atualização de 07/10/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-teta/<ano>/sinan-teta_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-teta/2026/sinan-teta_preliminar_2026-br@20261007.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `TETABR25.dbc` (66 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE do município de notificação e de residência |
| `NU_IDADE_N` | Inteiro composto | Idade (o primeiro dígito indica a unidade: dia/mês/ano) |
| `TP_CAUSA` | Inteiro | Possível causa (porta de entrada): 1 - Injeção, 2 - Laceração, 3 - Queimadura, 4 - Cirúrgico, 5 - Perfuração, 6 - Escoriação, 7 - Abortamento Séptico, 8 - Outros, 9 - Ignorado |
| `TP_CAUSOUT` | String (30) | Descrição da outra possível causa (habilitado se `TP_CAUSA` = 8) |
| `TP_LOCALLE` | Inteiro | Local da lesão: 1 - Membros Inferiores, 2 - Membros Superiores, 3 - Tronco, 4 - Cabeça/Pescoço, 5 - Cavidade Oral, 9 - Ignorado |
| `NU_DOSE` | Inteiro | Nº de doses de vacina (DTP, DT, dT, TT ou tetravalente) recebidas antes da lesão: 1 a 3, 4/5 com reforços, 6 - Nunca vacinado, 9 - Ignorado |
| `DT_ULT_DOS` | Data (`AAAAMMDD`) | Data da última dose da vacina contra tétano |
| `TP_PROFILA` | Inteiro | Tratamento específico/profilaxia utilizada após ferimento: 1 - Soro Antitetânico, 2 - Imunoglobulina, 3 - Vacina, 4 - Antibiótico, 5 - Nenhum |
| `CS_TRISMO`/`CS_RISO`/`CS_OPISTOT`/`CS_NUCA`/`CS_ABDOMIN`/`CS_MEMBROS`/`CS_CRISES`/`CS_SIN_OUT` | Inteiro | Manifestações clínicas: trismo, riso sardônico, opistótono, rigidez de nuca, abdômen em prancha, rigidez de membros, crises, outros sintomas (com descrição em `NM_SIN_OUT`) |
| `TP_ORIGEM` | Inteiro | Origem do caso (notificação por estabelecimento de saúde ou inquérito) |
| `CS_HOSPITA` / `DT_INTERNA` | Inteiro / Data | Internação hospitalar e data de internação |
| `TP_IDENTFI` / `TP_VACINA` / `TP_ANALISE` | Inteiro | Identificação do caso, esquemas vacinais aplicados e imunização/medidas adotadas na população suscetível |
| `CLASSI_FIN` | Inteiro | Classificação final do caso: 1 - Confirmado, 2 - Descartado |
| `CS_LOCAL` | Inteiro | Local provável da fonte de infecção: 1 - Domicílio, 2 - Trabalho, 3 - Via pública, 4 - Escola, 5 - Campo, 6 - Unidade de saúde, 7 - Outro local, 9 - Ignorado |
| `TPAUTOCTO` | Inteiro | O caso é autóctone do município de residência (1 - Sim, 2 - Não, 3 - Indeterminado) |
| `COUFINF`/`COPAISINF`/`COMUNINF` | String/Data | UF, país e municpio prováveis da fonte de infecção (autoctonia) |
| `EVOLUCAO` | Inteiro | Evolução do caso: 1 - Cura, 2 - Óbito por tétano, 3 - Óbito por outras causas, 9 - Ignorado |
| `DT_OBITO` / `DT_ENCERRA` | Data (`AAAAMMDD`) | Data do óbito e de encerramento do caso |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE, `String` com `zfill`), `ID_UNIDADE` (CNES), `ID_OCUPA_N` (CBO); códigos de classificação (`CLASSI_FIN`, `TP_CAUSA`, `TP_PROFILA`, `EVOLUCAO`) só viram categóricos após mapeamento explícito.
- **Datas e competências**: `DT_NOTIFIC`, `DT_SIN_PRI`, `DT_INVEST`, `DT_ULT_DOS`, `DT_INTERNA`, `DT_OBITO` e `DT_ENCERRA` vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`).
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: o código 6 de `NU_DOSE` ("nunca vacinado") deve ser tratado como valor explícito, não nulo; `TP_CAUSOUT`/`NM_SIN_OUT` são campos de texto livre com descrições que demandam revisão ortográfica antes de agregar; o baixo número de casos anuais recomenda tabulações por agregações de anos; e o corte das janelas de 21/30 dias pós-ferimento (história de injeção nas últimas 3 semanas e demais causas nas últimas 4) deve ser replicado manualmente a partir das datas do caso.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-teta
quantilica datasus list sinan-teta

# 2. Baixar microdados de sinan-teta com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-teta -o ./data --start 2007 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-teta -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-teta -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-teta/2025/sinan-teta_preliminar_2025-br@20261007.dbc", clean=True)

# Casos "nunca vacinados" ou com esquema incompleto previamente à lesão
des = qdf.filter(pl.col("nu_dose").is_in([1, 2, 3, 6]).not_())  # 4 e 5 = com reforços
print(des.group_by("evolucao").len().sort("evolucao"))

# Portas de entrada mais frequentes (não "outros")
causas = qdf.group_by("tp_causa").len().sort("tp_causa")
print(causas)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Tétano Acidental (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de tétano acidental e tétano neonatal (eliminação do tétano materno e neonatal)
