# `sinan-cole` — Cólera

O `sinan-cole` contém os microdados das notificações e investigações epidemiológicas de casos de Cólera (CID-10 A00) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de cólera, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. É uma base de incidência muito baixa no país atual (desde a introdução do *Vibrio cholerae* em 1991 os casos se concentraram em episódios isolados), com leiaute detalhado de investigação (91 colunas na ficha v5.0): quadro diarréico agudo, desidratação, coleta de fezes/vômito para cultura e sorotipagem, antibióticos, tipo de reidratação (oral/venosa) e fonte provável de infecção.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-cole` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (bases `FINAIS` históricas e anos recentes apenas em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2025, com o ano de 2023 ausente no FTP (conforme `index.json`) |
| **Volume aproximado no FTP** | 18 arquivos (~49 KB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

O cólera é agravo de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, integrando hoje a Lista Nacional de Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), com apoio da rede de laboratórios de referência (Fiocruz/IOC), sob o alerta precoce para reintrodução do agente na região das Américas — onde a doença permanece recorrente em países próximos (Haiti, Peru e outras transmissões recentes). Com transmissão endêmica extinta no Brasil, a base serve principalmente ao registro de casos isolados/importados, à vigilância de surtos episódicos e ao monitoramento da qualidade da rede de diagnóstico de *Vibrio cholerae*.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Cólera** do SINAN. A notificação nasce com a suspeição clínica (diarreia aguda profusa — "água de arroz" — com ou sem desidratação e choque) e é completada ao longo da investigação com sintomas (diarreia, câimbras, vômitos, presença de sangue e muco nas fezes), o grau de desidratação/choque (`CS_CHOQUE`), a coleta de material para cultura (`CS_MATERIA`/`CS_VOMITO`, `DT_COLETA`), resultado da cultura e sorotipagem (`CS_RESULTA`/`CS_POSITIV`/`CS_NEG_ESP`), antibiótico e reidratação (`CS_REIDRAT`: via oral ou venosa), e a fonte provável de infecção (contatos e vínculos de surto: `FC_CONTATO`, `VINCULO`). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo, e as consolidações até 2022 foram publicadas em `FINAIS`, com os anos de 2024 e 2025 apenas em `PRELIM`. Há uma lacuna no FTP: **o arquivo referente a 2023 não está disponível** (nem em `FINAIS` nem em `PRELIM`) — a série anual tem uma quebra que deve ser tratada em agregações. Revisões do dicionário datam de fevereiro/2012 (incluindo o bloco de desdobrams com fontes de água/alimentos e contatos).

Aplicações analíticas típicas: vigilância de casos isolados/importados (com fonte provável de infecção em `COUFINF`/`COPAISINF`/`COMUNINF`); investigação de surtos de diarreia aguda por vínculo epidemiológico (`FC_CONTATO`, `VINCULO`); percentual de casos hospitalizados e letalidade; e o registro de casos confirmados laboratorialmente (cultura e sorotipagem O1/O139), indicador da capacidade da rede de laboratórios de referência.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `COLE` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `COLE` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `COLEBR24.dbc` — `COLE` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `24` é o ano de notificação (2024). As consolidações até 2022 estão em `FINAIS` e os anos de 2024 a 2025 estão apenas em `PRELIM` (ex.: `COLEBR25.dbc`); **o arquivo de 2023 não consta no FTP** (lacuna verificável no inventário `index.json`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-cole/<ano>/sinan-cole_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-cole/2025/sinan-cole_preliminar_2025-br@20260120.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `COLEBR24.dbc` (91 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `FC_CONTATO` | Inteiro | Se sim, tipo de contato com caso de cólera (domiciliar, vizinho, outro, sem contato) |
| `FC_CONT_DE` / `OUT_VINCUL` | Inteiro/String | Tipo de contato detalhado e/outro vínculo (escola, trabalho, mar) |
| `VINCULO` | Inteiro | Vínculo entre os casos notificados (coorte de surto) |
| `CS_ASSINTO` | Inteiro | Assintomático (1 - Sim, 2 - Não, 9 - Ignorado) |
| `CS_DIARRE`/`CS_CAIMBRA`/`CS_FEBRE`/`CS_VOMITOS`/`CS_DOR` | Inteiro | Sintomas: diarreia, câimbras, febre, vômitos e dor abdominal |
| `CS_CHOQUE` / `CS_DESIT` | Inteiro | Choque e desidratação/estado de hidratação |
| `TIP_DIARRE`/`CS_FREQUEN`/`CS_SANGUE`/`CS_MUCO`/`CS_TIPO` | Inteiro | Aspecto da diarreia: tipo (aguada — "água de arroz"), frequência, presença de sangue e muco |
| `DT_ATENDIM` / `DT_INTERNA` / `UF_HOSPITA` / `NM_MUNIC_H` | Data/String | Atendimento, internação hospitalar e local |
| `CS_MATERIA` / `CS_VOMITO` | Inteiro | Material colhido para exame: fezes e vômito (1 - Sim, 2 - Não, 9 - Ignorado) |
| `DT_COLETA` | Data (`AAAAMMDD`) | Data da coleta do material para exame |
| `CS_ANTIB` / `NM_ANTIBIO` / `CS_RESULTA` | Inteiro/String | Antibioticoterapia instituída, nome dos antibióticos e resultado da cultura |
| `CS_POSITIV` / `CS_NEG_ESP` | Inteiro | Resultado positivo da cultura e espécimes negativados (sorotipagem O1/O139) |
| `CS_REIDRAT` | Inteiro | Tipo de reidratação recebida: via oral, venosa |
| `CS_ANTIB_T` / `ANTIB_DES` | Inteiro/String | Antibiótico profilático e descrição |
| `CLASSI_FIN` | Inteiro | Classificação final do caso: 1 - Confirmado, 2 - Descartado |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte: 1 - Laboratorial, 2 - Clínico-epidemiológico |
| `TPAUTOCTO` | Inteiro | O caso é autóctone do município de residência (1 - Sim, 2 - Não, 3 - Indeterminado) |
| `COUFINF`/`COPAISINF`/`COMUNINF`/`CODISINF` | String/Data | UF, país, distrito e município prováveis da fonte de infecção |
| `DOENCA_TRA` | Inteiro | Doença relacionada ao trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito por cólera, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` / `DT_ENCERRA` | Data (`AAAAMMDD`) | Data do óbito e de encerramento do caso |
| `DT_DESC1`/`DT_DESC2`/`DT_DESC3` | Data | Campos repetidos (1 a 3) de descarte/administração de registros — data (co UF / município / país correspondentes em `CO_UF_DES*`, `MUN_DES*`, `PA_DES*` e descrição `DS_TRANS*`)

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE, `String` com `zfill`), `ID_UNIDADE` (CNES), `ID_OCUPA_N` (CBO); códigos de classificação (`CLASSI_FIN`, `CRITERIO`, `EVOLUCAO`) só viram categóricos após mapeamento explícito.
- **Datas e competências**: todas as datas (`DT_NOTIFIC`, `DT_SIN_PRI`, `DT_INVEST`, `DT_COLETA`, `DT_OBITO`, `DT_ENCERRA`) vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`); `SEM_NOT`/`SEM_PRI` são semanas epidemiológicas `AAAASS`.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: o volume anual de casos é mínimo (série com pouquíssimos registros); a **lacuna do ano 2023 no FTP** exige cuidado na consolidação da série anual em agregações; e os campos coleta/cultura (`CS_MATERIA`, `CS_VOMITO`, `CS_POSITIV`) devem ser lidos conforme a ficha revisada de fevereiro/2012 (definição de caso e amostragem obrigatória).

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-cole
quantilica datasus list sinan-cole

# 2. Baixar microdados de sinan-cole com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-cole -o ./data --start 2007 --end 2025 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-cole -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-cole -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-cole/2024/sinan-cole_preliminar_2024-br@20260120.dbc", clean=True)

# Casos confirmados por ano e critério de confirmação
conf = qdf.filter(pl.col("CLASSI_FIN") == 1).group_by(["NU_ANO", "CRITERIO"]).len().sort("NU_ANO")
print(conf)

# Evolução dos casos confirmados (incluindo letalidade)
print(conf.filter(pl.col("EVOLUCAO") == 2))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Cólera (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de cólera e doenças diarréicas agudas (DDA)
