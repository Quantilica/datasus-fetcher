# `sinan-dift` — Difteria

O `sinan-dift` contém os microdados das notificações e investigações epidemiológicas de casos de Difteria (CID-10 A36) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de difteria, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. É uma base de baixa incidência (difteria é agravo raro no Brasil, com registros individuais habitualmente associados a inquéritos e surtos), mas com leiaute detalhado (92 colunas na v5.0) que registra a pseudo-membrana, complicações (faringe, laringe, cordae, miocardite, nefrite, paralisias), o tratamento com soro antitoxina e antibiótico, a síntese de contato e a investigação vacinal.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-dift` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (bases `FINAIS` históricas e anos recentes apenas em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 20 arquivos (~0,2 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A difteria é agravo de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, atualmente constando da Lista Nacional de Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) em articulação com o GT-SINAN, a rede laboratorial de referência para o diagnóstico de *Corynebacterium diphtheriae* e o Programa Nacional de Imunizações, cuja cobertura vacinal (vacina tríplice bacteriana/D3 e D3a) é decisiva para manter a doença em níveis raros. Com poucos casos esperados por ano, a base serve à investigação de casos individualizados, à identificação de bolsões de cobertura vacinal insuficiente e à resposta rápida a surtos localizados.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Difteria** do SINAN. A notificação nasce com a suspeição clínica (pseudo-membrana sogra nos pilares, amígdalas, palato, faringe ou laringe, acompanhada de edema cervical, prostração e febre) e é completada ao longo da investigação com o registro detalhado da topografia da pseudo-membrana, das complicações (miocardite, nefrite, paralisias bulbar/palatina/de membros e arritmias), do material clínico coletado e do tratamento (soro antitoxina e antibiótico, com datas `TRA_DATA_S`/`TRA_DATA_A`). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. Mudanças incrementais no dicionário (versão revisada em julho/2010) refletiram a organização das opções do critério de confirmação (cultura com provas de toxigenicidade, cultura sem prova de toxigenicidade, vínculo epidemiológico, morte pós-clínica compatível, clínico e necrópsia) e o registro do antibiótico terapêutico em rodapé (data de início com uso de responsabilidade clínica).

Aplicações analíticas típicas: manutenção da vigilância caso a caso (o volume é baixo); letalidade da difteria (`EVOLUCAO` 3/4 com `DT_OBITO`); proporção de casos com cobertura vacinal incompleta (`ANT_DOS_N`, `ANT_ULTI_D`) e tipo de contato do caso (`ANT_TIPOCO`); confirmação pela cultura com prova de toxigenicidade (`CRITERIO` = 1), o padrão-ouro laboratorial; e registro de sequelas (`EVOLUCAO` 1/2) e do manejo terapêutico (antitoxina/antibiótico).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `DIFT` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `DIFT` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `DIFTBR25.dbc` — `DIFT` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As consolidações até 2023 estão em `FINAIS` e os anos de 2024 a 2026 estão apenas em `PRELIM` (ex.: `DIFTBR26.dbc`, atualização de 07/10/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-dift/<ano>/sinan-dift_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-dift/2026/sinan-dift_preliminar_2026-br@20261007.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `DIFTBR25.dbc` (92 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE do município de notificação e de residência |
| `NU_LOTE_V`/`NU_LOTE_H` | String | Lote da transferência vertical (hierárquica) da investigação|
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `ID_OCUPA_N` | String (6) | Código CBO da ocupação do paciente |
| `ANT_TIPOCO` | Inteiro | Tipo de contato com caso de difteria (domiciliar, escolar, colega de trabalho, ignorado) |
| `ANT_DOS_N` / `ANT_ULTI_D` | Inteiro / Data | Nº de doses do esquema vacinal (D3/TD) e data da última dose |
| `CLI_EDEMAG`/`CLI_PESCOC`/`CLI_FEBRE`/`CLI_PROSTR`/`CLI_PSEUDO`/`CLI_PALIDE`/`CLI_TEMPER` | Inteiro | Sinais e sintomas: edema de pescoço ("pescoço de touro"), feb­re, prostração, pseudo-membrana, palidez e temperatura elevada |
| `CLI_CAVIDA`/`CLI_AMIGDA`/`CLI_CORDAO`/`CLI_FARING`/`CLI_LARING`/`CLI_ORGAOS`/`CLI_PALATO` | Inteiro | Localização da pseudomembrana: cavidade nasal, amigdalas, cordas vocais, faringe, laringe, outros órgãos, palato |
| `CLI_MIOCAR`/`CLI_NEFRIT`/`CLI_PARALB`/`CLI_PARALP`/`CLI_ARRITM`/`CLI_PARALM` | Inteiro | Complicações: miocardite, nefrite, paralisia bulbar, paralisia palatina, arritmias, paralisia de membros |
| `ATE_HOSPIT`/`ATE_INTERN` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |
| `LAB_MATE_N`/`LAB_DATA_C`/`LAB_CULTUR`/`LAB_PROVAS` | Inteiro/Data | Material coletado (swab), data da coleta, resultado da cultura e provas de toxigenicidade |
| `TRA_DATA_S` | Data | Data da aplicação de soro antitoxina difiteria |
| `TRA_ANTIBI`/`TRA_DATA_A` | Inteiro/Data | Antibiótico instituído e data da administração |
| `CLASSI_FIN` | Inteiro | Classificação final do caso: 1 - Confirmado, 2 - Descartado |
| `CRITERIO` | Inteiro | Critério de confirmação: 1 - Cultura com prova de toxigenicidade, 2 - Cultura sem prova de toxigenicidade, 3 - Vínculo epidemiológico, 4 - Morte pós clínica compatível, 5 - Clínico, 6 - Necrópsia |
| `EVOLUCAO` | Inteiro | Evolução do caso: 1 - Cura com sequela, 2 - Cura sem sequela, 3 - Óbito por difteria, 4 - Óbito por outras causas, 9 - Ignorado |
| `DT_OBITO` / `DT_ENCERRA` | Data (`AAAAMMDD`) | Data do óbito e de encerramento do caso |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE, `String` com `zfill`), `ID_UNIDADE` (CNES), `ID_OCUPA_N` (CBO); códigos de classificação (`CLASSI_FIN`, `CRITERIO`, `EVOLUCAO`) só viram categóricos após mapeamento explícito.
- **Datas e competências**: `DT_NOTIFIC`, `DT_SIN_PRI`, `DT_INVEST`, `LAB_DATA_C`, `TRA_DATA_S`, `TRA_DATA_A`, `DT_OBITO` e `DT_ENCERRA` vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`).
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: a base tem poucos casos por ano (doença rara na era pós-vacinal), de modo que tabelas agregadas simples tendem a ser esparsas; os dois critérios de cultura (com/sem prova de toxigenicidade) marcam a diferença entre confirmação definitiva (`CRITERIO` = 1) e isolamento sem prova da toxigenicidade (`CRITERIO` = 2); a evolução com/sem sequela (`EVOLUCAO` = 1/2) requer mapeamento antes de qualquer tabulação; e a série de 2024 a 2026 está apenas em `PRELIM`, com casos ainda passíveis de revisão.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-dift
quantilica datasus list sinan-dift

# 2. Baixar microdados de sinan-dift com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-dift -o ./data --start 2007 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-dift -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-dift -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-dift/2025/sinan-dift_preliminar_2025-br@20261007.dbc", clean=True)

# Casos confirmados e o critério de confirmação utilizado
conf = qdf.filter(pl.col("classi_fin") == 1).group_by("criterio").len().sort("criterio")
print(conf)

# Evolução do caso (com/sem sequela, óbitos)
evol = qdf.filter(pl.col("classi_fin") == 1).group_by("evolucao").len().sort("evolucao")
print(evol)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Difteria (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de difteria; Norma de Manejo e tratamento da difteria (MS)
