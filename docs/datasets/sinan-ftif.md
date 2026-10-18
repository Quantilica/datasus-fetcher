# `sinan-ftif` — Febre Tifoide

O `sinan-ftif` contém os microdados das notificações e investigações epidemiológicas de casos de Febre Tifoide (CID-10 A01.0) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de febre tifoide, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. Base de incidência moderada e focada na investigação de transmissão fecal-oral (água/alimentos), com o leiaute da ficha v5.0 (131 colunas): quadro clínico (febre, cefaléia, constipação/diarreia, esplenomegalia), complicações graves (perfuração intestinal e toxemia), o extenso bloco de hemoculturas/uroculturas/coproculturas (3 exames por material) e o tratamento antimicrobiano registrado por classe de antibiótico.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-ftif` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (bases `FINAIS` históricas e anos recentes apenas em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 20 arquivos (~0,8 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A febre tifoide é agravo de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, constando hoje da Lista Nacional de Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), com suporte da rede de laboratórios para o diagnóstico de *Salmonella enterica* sorotipo Typhi e o registro de portadores — a transmissão fecal-oral por água e alimentos aproxima o agravo da vigilância de surtos de Doenças Transmitidas por Alimentos (DTA) e da vigilância do saneamento básico. A base alimenta a vigilância de casos isolados e surtos regionais, o monitoramento da resistência antimicrobiana e a identificação de portadores crônicos.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Febre Tifoide** do SINAN. A notificação nasce com a suspeição clínica (febre prolongada, cefaléia, astenia, constipação/diarreia, tosse, esplenomegalia) e é completada ao longo da investigação com sinais de complicações graves (perfuração intestinal, hemorragia digestiva e toxemia), com o resultado de exames microbiológicos (hemocultura, urocultura, coprocultura e culturas de outros materiais, com data e resultado por material e repetição: `HEMO_R1..3`, `URO_R1..3`, `COPRO_R1..3`, `OUTR_R1..3`) e o tratamento por classes de antibióticos (clorafenicol, ampicilina, sulfa/SMT+TMP, quinolonas e outros, com duração em dias). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. Revisões do dicionário datam de julho/2010 e disciplinaram a leitura de "classicalite final" por caso. Em versões posteriores (categoria de casos de resultado `CLASSI_FIN` não pode ser descartada se qualquer resultado laboratório anexado for *S. typhi*) e a leitura do critério por material (`HEMO/URO/COPRO/OUTR`).

Aplicações analíticas típicas: percentual de casos confirmados com culturas positivas por material (hemocultura, urocultura, coprocultura); frequência de complicações graves (`PERFURA`); investigação de contatos (`CONTATO`, `SUGE_VINCU`/`VINC_OUT`) e fontes prováveis de água/alimentos; percentual de casos com uso de cada classe de antibiótico e duração média do tratamento (`DIAS`); letalidade por ano e região.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `FTIF` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `FTIF` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `FTIFBR25.dbc` — `FTIF` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As consolidações até 2024 estão em `FINAIS` e os anos de 2025 e 2026 estão apenas em `PRELIM` (ex.: `FTIFBR26.dbc`, atualização de 02/06/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-ftif/<ano>/sinan-ftif_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-ftif/2026/sinan-ftif_preliminar_2026-br@20260602.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `FTIFBR23.dbc` (131 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `CONTATO` | Inteiro | Contato com caso parecido de febre tifoide (1 - Sim, 2 - Não) |
| `CONT_OUT` / `SUGE_VINCU` / `VINC_OUT` | Inteiro/String | Detalhe do contato sugerido como vínculo epidemiológico e descrição |
| `ASSINTOMAT` | Inteiro | Caso assintomático (portador) |
| `FEBRE`/`CEFALEIA`/`DIARREIA`/`CONSTIPA`/`ASTENIA`/`TOSSE`/`ESPLENO`/`TIFICA`/`NAUSEAS`/`VOMITOS`/`DOR` | Inteiro | Sinais e sintomas: febre, cefaléia, diarreia, constipação, astenia, tosse, esplenomegalia, "manchas tíficas" (roséolas), náuseas, vômitos e dor abdominal |
| `ENTERO` | Inteiro | Quadro de toxemia/estado entérico grave |
| `PERFURA` | Inteiro | Perfuração intestinal (complicação grave) |
| `COMP_OUT` / `COMP_OUT_D` | Inteiro/String | Outras complicações e sua descrição |
| `ATENDIMENT` / `DT_ATENDE` / `UF` / `MUNICIPIO` | Inteiro/Data/String | Atendimento, data e local (UF/município) |
| `SANGUE`/`FEZES`/`URINA`/`ANTIBIOTIC` | Inteiro | Materiais coletados para exame (sangue, fezes, urina) e uso prévio de antibiótico (interferência no cultivo) |
| `DT_HEMO1`/`HEMO_R1`/`HEMO_D_1` a `DT_HEMO3`/`HEMO_R3`/`HEMO_D_3` | Data/Inteiro | Hemoculturas (1 a 3): data da coleta, resultado e diagnóstico (positivo para *S. typhi*) |
| `DT_URO`/`URO_R1` a `DT_URO3`/`URO_R3` | Data/Inteiro | Uroculturas: data, resultado e diagnóstico |
| `DT_COPRO1`/`COPRO_R1` a `DT_COPRO3`/`COPRO_R3` | Data/Inteiro | Coproculturas: data, resultado e diagnóstico (investigação de portadores) |
| `DT_OUTR1`/`OUTR_R1` a `DT_OUTR3`/`OUTR_R3` | Data/Inteiro | Outros materiais exames: data, resultado e diagnóstico |
| `CLORAFEN`/`AMPICILINA`/`SULFA`/`QUINOLONA` | Inteiro | Antibióticos utilizados no tratamento (1 - Sim, 2 - Não, 9 - Ignorado) |
| `ANT_OUTR` / `ANT_OUT_D` | Inteiro/String | Outros antibióticos e descrição |
| `DIAS` | Inteiro | Duração do tratamento antimicrobiano (dias) |
| `CLASSI_FIN` | Inteiro | Classificação final do caso: 1 - Confirmado, 2 - Descartado |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte (laboratorial, clínico-epidemiológico) |
| `DOENCA_TRA` | Inteiro | Doença relacionada ao trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito por febre tifoide, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` / `DT_ENCERRA` | Data (`AAAAMMDD`) | Data do óbito e de encerramento do caso |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE, `String` com `zfill`), `ID_UNIDADE` (CNES), `ID_OCUPA_N` (CBO); códigos de classificação (`CLASSI_FIN`, `CRITERIO`, `EVOLUCAO`) só viram categóricos após mapeamento explícito.
- **Datas e competências**: todas as datas (`DT_NOTIFIC`, `DT_SIN_PRI`, `DT_INVEST`, `DT_HEMO*`, `DT_URO*`, `DT_COPRO*`, `DT_OUTR*`, `DT_OBITO`, `DT_ENCERRA`) vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`); `SEM_NOT`/`SEM_PRI` são semanas epidemiológicas `AAAASS`.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: o bloco laboratorial é organizado em 3 exames por material (hemocultura, urocultura, coprocultura e outros), que devem ser processados mediante "explodir" colunas por coluna de resultado; a validação do dicionário impede descartar casos com qualquer resultado *S. typhi* positivo — essa consistência deve ser preservada em pipelines; o histórico de contatos e portadores (`COPRO_R*`) é peça-chave para estudos de portador crônico; e o campo `ASSINTOMAT` marca portadores assintomáticos, que não devem ser contabilizados como casos de doença.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-ftif
quantilica datasus list sinan-ftif

# 2. Baixar microdados de sinan-ftif com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-ftif -o ./data --start 2007 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-ftif -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-ftif -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-ftif/2023/sinan-ftif_2023-br@20251202.dbc", clean=True)

# Casos confirmados e critério de confirmação por ano
conf = qdf.filter(pl.col("classi_fin") == 1).group_by(["nu_ano", "criterio"]).len().sort("nu_ano")
print(conf)

# Antibióticos utilizados no tratamento
antibio = qdf.group_by("quinolona").len().sort("quinolona")
print(antibio)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Febre Tifoide (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de febre tifoide (doença de transmissão fecal-oral, vigilância de portadores)
