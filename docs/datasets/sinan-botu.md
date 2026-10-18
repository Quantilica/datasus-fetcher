# `sinan-botu` — Botulismo

O `sinan-botu` contém os microdados das notificações e investigações epidemiológicas de casos de Botulismo (CID-10 A05.1) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de botulismo, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. É uma base de baixa incidência e alta gravidade (doença paralítica aguda, com uso frequente de ventilação mecânica), com 149 colunas: quadro neurológico detalhado (sintomas cranio-neuro-oftalmológicos de bulbar a respiratório), a forma de botulismo, o extenso bloco de investigação do alimento incriminado e materiais (soro, fezes e alimentos coletados com resultado e tipo de toxina), o tratamento com soro antibotulínico e a evolução do caso.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-botu` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (bases `FINAIS` históricas e anos recentes apenas em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 20 arquivos (~0,2 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

O botulismo é agravo de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, constando hoje da Lista Nacional de Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), com apoio dos laboratórios de referência (LACEN e institutos como Adolfo Lutz) para confirmação pela detecção da toxina botulínica. É um dos agravos com resposta CIEVS mais ágil: notificação imediata por telefone/fax pelo profissional de saúde, pela baixa incidência, alta letalidade e dependência do tratamento precoce com soro antibotulínico — a detecção rápida de casos permite o bloqueio de transmispor via alimentos e permite o envio assistido de soro para os serviços de assistência.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Botulismo** do SINAN (dicionário de dados v5.0, revisado em julho/2010). A notificação nasce com a suspeição clínica de doença paralítica aguda (sintomas: diplopia/visão dupla, ptose palpebral, disfagia, disartria, disfonia, boca seca, fraqueza muscular flácida/simétrica descendente, dispneia/insuficiência respiratória: campos `ST*`) nas suas três formas — alimentar (`STALIMENTO`: suspeita de transmissão alimentar), intestinal (lactente) e por ferimento (`TPBOTULISM`: 1 - Alimentar, 2 - Intestinal, 3 - Por ferimento, 4 - Outra) — e é completada ao longo da investigação com o bloco neurológico de exames e sinais (reflexos `TPNEURO`, sinais cranio-neuro-oftalmológicos/bulbares e de membros e sensibilidade `STPTOSE`/`STOFTALMO`/`STMIDRIASE`/`STFACIAL`/`STBULBAR`/`STMEMSUP`, `STMEMINF`, `STSENSIVEL`, `TP_MOTORA`/`TP_REPETE`, eletromiografia `STELETRO`), o material coletado para pesquisa de toxina (soro, fezes e amostras de alimentos, com resultado e tipo de toxina: `STSOROMAT`/`DTSOROCOL`/`STSORORES`/`TPSOROTOX`, `STFEZESMAT`/`DTFEZESCOL`/`STFEZESRES`/`TPFEZESTOX`, amostras de alimentos/bromatológicas), o alimento incriminado e o local de ingestão/coleta (`STCASEIRA`, `STCOMERCIO`, `STEXPALIM`, `DS_INDUS`, `DS_INGEST`, locais `STDOMICILI`...`STFESTA`), o tratamento (soro antibotulínico `STSORO`, antibiótico e ventilação mecânica `STVENTILA`) e o agente incriminado se descartado (`AGENTE_OUT`). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net); as bases de 2007 a 2024 estão em `FINAIS` e os anos de 2025 e 2026 apenas em `PRELIM` (ex.: `BOTUBR25.dbc`, atualização de 25/05/2026). O dicionário de dados v5.0 (revisado em julho/2010) provê tabela de classificação final em dois grupos (1 - Confirmado; 2 - Descartado, com especificação de outro agente em `AGENTE_OUT`) e o critério de confirmação/descarte (1 - Laboratorial, 2 - Clínico-epidemiológico). O tipo de toxina botulínica é identificado no soro e nas fezes (campos `TPSOROTOX` e `TPFEZESTOX`, tipos A a G, 7 - Outra, 9 - Ignorado).

Aplicações analíticas típicas: número e distribuição de casos confirmados (baixa incidência, com foco em conservas caseiras `STCASEIRA`); formas de botulismo (`TPBOTULISM`); uso de soro antibotulínico e ventilação mecânica em UTI (`STSORO`, `STVENTILA`); letalidade (`EVOLUCAO`); e investigação do alimento incriminado e das toxinas identificadas (`TPSOROTOX`, `TPFEZESTOX`, `TP_ALI1TOX`), fundamental para bloqueios e alertas CIEVS.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `BOTU` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `BOTU` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `BOTUBR25.dbc` — `BOTU` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As bases de 2007 a 2024 estão em `FINAIS` e os anos de 2025 e 2026 apenas em `PRELIM` (atualização de 25/05/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-botu/<ano>/sinan-botu_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-botu/2025/sinan-botu_preliminar_2025-br@20260525.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip`, as instruções POP_I/II/III de acesso, descompactação e tabulação e a ficha/instruções de botulismo; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `BOTUBR25.dbc` (149 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `SEM_NOT` / `NU_ANO` | Data (`AAAAMMDD`)/Inteiro | Data, semana epidemiológica e ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `DT_SIN_PRI` / `SEM_PRI` | Data/Inteiro | Data e semana de início dos sintomas |
| `NU_IDADE_N` / `CS_SEXO` | Inteiro/String | Idade decomposta por unidade e sexo |
| `DT_INVEST` / `DTATEND` / `NUATEND` | Data/Inteiro | Data da investigação e dados de atendimento |
| `DTSUSPEIC` | Data (`AAAAMMDD`) | Data suspeição/primeira atuação clínica |
| `STHOSPITAL` / `DTINTERNA` / `DTALTA` | Inteiro/Data | Hospitalização, data de internação e de alta |
| `STFEBRE`/`STNAUSEA`/`STVOMITO`/`STDIARREIA`/`STCONSTIPA`/`STCEFALEIA`/`STTONTURA` | Inteiro | Sintomas prodômicos: febre, náuseas, vômitos, diarreia, constipação, cefaleia, tontura |
| `STVISAO`/`STDIPLOPIA`/`STDISARTRI`/`STDISFONIA`/`STDISFAGIA`/`STBOCA` | Inteiro | Sintomas neurológicos: visão turva/diplopia, disartria, disfonia, disfagia, boca seca |
| `STFERIMENT`/`STFLACIDEZ`/`STDISPNEIA`/`STRESPIRA`/`STCARDIACA`/`STCOMA`/`STPARESTES` | Inteiro | Ferimento, flacidez, dispneia, insuficiência respiratória/cardíaca, coma, parestesias |
| `STPTOSE`/`STOFTALMO`/`STMIDRIASE`/`STFACIAL`/`STBULBAR` | Inteiro | Sinais de envolvimento de nervos cranianos: ptose, oftalmoparesia, midriase, paralisia facial, bulbar |
| `STMEMINF`/`STMEMSUP`/`STDESCENDE`/`STSIMETRIC`/`STSENSIVEL` | Inteiro | Paralisia em membros inferiores/superiores, forma descendente, simetria e sensibilidade |
| `TPNEURO` | Inteiro | Reflexos neurológicos: 1 - Normais, 2 - Aumentados, 3 - Reduzidos/Ausentes, 9 - Ignorado |
| `STALIMENTO` / `DSALIMENTO` | Inteiro/String | Suspeita de transmissão alimentar (1 - Sim) e descrição do alimento |
| `TPBOTULISM` | Inteiro | Forma de botulismo: 1 - Alimentar, 2 - Intestinal, 3 - Por ferimento, 4 - Outra |
| `STCASEIRA` / `STCOMERCIO` / `STEXPALIM` / `DS_INDUS` | Inteiro/String | Natureza do alimento: doméstico caseiro, comercial, exportação e descrição do industrializado |
| `STDOMICILI` / `STESCOLA` / `STTRABALHO` / `STRESTAURA` / `STFESTA` / `STOUTROLOC` | Inteiro | Local de ocorrência da ingestão: domicílio, escola, trabalho, restaurante, festa, outro |
| `NUCONSOME` | Inteiro | Número de pessoas que consumiram o alimento |
| `STSORO` / `STANTIBIO` / `STOUTROTRA` / `STVENTILA` | Inteiro | Tratamento: soro antibotulínico, antibiótico, outro tratamento, ventilação mecânica |
| `DTSORO` / `STANTIBOTU` | Data/Inteiro | Data de aplicação do soro antitoxina e aplicação |
| `STSOROMAT` / `DTSOROCOL` / `STSORORES` / `TPSOROTOX` | Inteiro/Data | Soro coletado: data, resultado da pesquisa de toxina e tipo de toxina (A-G, 7 - Outra, 9 - Ignorado) |
| `STFEZESMAT` / `DTFEZESCOL` / `STFEZESRES` / `TPFEZESTOX` | Inteiro/Data | Fezes coletadas: data, resultado da pesquisa de toxina e tipo de toxina |
| `ST_ALI1COL` / `DS_ALI1OUT` / `DT_ALI1COL` / `RESALIM1` / `TP_ALI1TOX` | Inteiro/Data/String | Alimento 1 coletado: descrição, data, resultado e tipo de toxina identificada |
| `ST_ALI2COL` / `DS_ALI2OUT` / `DT_ALI2COL` / `ST_ALI2RES` / `TP_ALI2TO` | Inteiro/Data/String | Alimento 2 coletado: descrição, data, resultado e tipo de toxina identificada |
| `STELETRO` / `DTELETRO` | Inteiro/Data | Eletromiografia realizada e data |
| `TP_LIQUOR` / `NU_CELULA` / `NU_PROTEI` / `DT_LIQUOR` | Inteiro/Data | Exame de liquor: resultado, células, proteínas e data |
| `CLASSI_FIN` | Inteiro | Classificação final do caso: 1 - Confirmado, 2 - Descartado (especificar outro agente) |
| `AGENTE_OUT` | String | Outro agente identificado quando o caso é descartado |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte: 1 - Laboratorial, 2 - Clínico-epidemiológico |
| `TPCLINICA` / `TPBROMATO` / `DSCAUSALIM` | Inteiro/String | Avaliação clínica e bromatológica e descrição da causa/alimento |
| `TP_MOTORA` / `TP_REPETE` / `TP_SENSITI` | Inteiro | Aspectos clínicos: padrão motor, repetição e sensibilidade |
| `DOENCA_TRA` | Inteiro | Doença relacionada ao trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `EVOLUCAO` | Inteiro | Evolução do caso: 1 - Cura, 2 - Óbito por botulismo, 3 - Óbito por outras causas, 9 - Ignorado |
| `DT_OBITO` / `DT_ENCERRA` / `DT_DIGITA` | Data (`AAAAMMDD`) | Data do óbito, de encerramento e de digitação |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE, `String` com `zfill`), `ID_UNIDADE` (CNES), `ID_OCUPA_N` (CBO); códigos de classificação (`CLASSI_FIN`, `CRITERIO`, `EVOLUCAO`, `TPBOTULISM`) só viram categóricos após mapeamento explícito.
- **Datas e competências**: todas as datas (`DT_NOTIFIC`, `DT_SIN_PRI`, `DTATEND`, `DTSUSPEIC`, `DTINTERNA`, `DTALTA`, `DTSORO`, `DTSOROCOL`, `DTFEZESCOL`, `DTELETRO`, `DT_ALI1COL`, `DT_OBITO`, `DT_ENCERRA`) vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`); `SEM_NOT`/`SEM_PRI` são semanas epidemiológicas `AAAASS`.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: base de casuística rara (dezenas de casos por ano) — qualquer validação de agregação é sensível a erros: atenção com `CLASSI_FIN` (descartado exige especificar outro agente em `AGENTE_OUT`); a forma alimentar exige o bloco do alimento suspeito (`STALIMENTO`/`DSALIMENTO`, natureza caseira/comercial `STCASEIRA`, local de ingestão `STDOMICILI`) e as amostras bromatológicas (`ST_ALI1COL`...); `TPSOROTOX`/`TPFEZESTOX` devem ser tratados como código do tipo de toxina (A–G/Outra) e não como caso confirmado; e o campo `NU_LOTE_V` (lote do soro antibotulínico do PNI) e a natureza do alimento implicado (caseiro vs comercial `STCASEIRA`/`STCOMERCIO`) são fundamentais para estudos de botulismo alimentar.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-botu
quantilica datasus list sinan-botu

# 2. Baixar microdados de sinan-botu com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-botu -o ./data --start 2007 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-botu -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-botu -o ./data/raw --parquet-dir ./data/parquet --start 2007
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-botu/2025/sinan-botu_preliminar_2025-br@20260525.dbc", clean=True)

# Casos confirmados por forma de botulismo
formas = qdf.filter(pl.col("classi_fin") == 1).group_by("tpbotulism").len().sort("tpbotulism")
print(formas)

# Evolução dos casos confirmados
evol = qdf.filter(pl.col("classi_fin") == 1).group_by("evolucao").len().sort("evolucao")
print(evol)

# Uso de soro antibotulínico e ventilação mecânica
trat = qdf.group_by(["stsoro", "stventila"]).len().sort("stsoro")
print(trat)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Botulismo (ficha e dicionário de dados v5.0, rev. julho/2010)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de Botulismo (epidemiologia e vigilância de conservas caseiras)
