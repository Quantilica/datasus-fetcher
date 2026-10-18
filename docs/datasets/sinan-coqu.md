# `sinan-coqu` — Coqueluche

O `sinan-coqu` contém os microdados das notificações e investigações epidemiológicas de casos de Coqueluche/Pertússis (CID-10 A37) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de coqueluche, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. Com 83 colunas no leiaute v5.0, cobre o detalhamento clínico do período paroxístico (crises, cianose, apneia, vomitos), o histórico vacinal do paciente (doses de cómic DPT ou tetravalente), a situação da investigação de contatos e quimioprofilaxia (bloqueio) — instrumento central para a vigilância da coqueluche em menores de 1 ano e das ondas epidemicas registradas em intervalos de três a cinco anos no Brasil.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-coqu` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (bases `FINAIS` históricas e anos recentes apenas em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 20 arquivos (~10,8 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A coqueluche é doença de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, integrando hoje a Lista Nacional de Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) em articulação com o GT-SINAN, o Programa Nacional de Imunizações (DTP e dTpa, incluindo a vacinação de gestantes) e a rede de laboratórios de referência. A dinâmica epidemiológica da doença é cíclica (ondas epidêmicas a cada 3 a 5 anos) e a letalidade se concentra em lactentes menores de 6 meses — a base alimenta a detecção de situações de recrudescimento da pertússis e as análises de cobertura vacinal do PNI.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Coqueluche** do SINAN. A notificação nasce com a suspeição clínica (condição de tosse paroxística de mais de 15 dias, crises de tosse seguidas de vômitos ou cianose, tosse com tosso convulsivo) já na fase catarral (`DT_CATARRA`), e é completada ao longo da investigação com o registro clínico do período paroxístico (crises, cianose, apneia, vômitos, hospitalização), o histórico vacinal (`CS_VAC_N`, doses de DPT ou tetravalente e `DT_ULT_DOS`), a confirmação laboratorial por coleta de material de nasofaringe (`CS_COLETA`, `CS_CULTURA`) e a investigação de contatos com bloqueio (bloqueio vacinal, quimioprofilaxia ou ambos: `MED_BLOQUE`). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. Importantes revisões do instrumento e do vocabulário do dicionário datam de fevereiro/2012, período que acompanhou a vigência da vigilância intensificada de coqueluche, com a definição de casos clínicos para menores de 4 meses e casos confirmados por critério laboratorial ou vínculo epidemiológico — o histórico de doses reforçadas do PNI permanece registrado no instrumento.

Aplicações analíticas típicas: incidência anual de casos confirmados e taxa de letalidade; curva epidêmica por semana do início da tosse (`SEM_PRI`); desfechos de hospitalização (`CS_HOSPITA`, `DT_INTERNA`) e óbito (`EVOLUCAO`); percentual de casos com esquema vacinal conforme o PNI (análise de falhas de cobertura); investigação de comunicantes e bloqueios realizados (`QUAN_COMUN`, `QUAN_POSIT`, `MED_BLOQUE`); e análise específica de menores de 1 ano, grupo prioritário da vigilância.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `COQU` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `COQU` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `COQUBR25.dbc` — `COQU` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As consolidações até 2022 estão em `FINAIS` e os anos de 2023 a 2026 estão apenas em `PRELIM` (ex.: `COQUBR26.dbc`, atualização de 07/10/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-coqu/<ano>/sinan-coqu_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-coqu/2026/sinan-coqu_preliminar_2026-br@20261007.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `COQUBR25.dbc` (83 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE do município de notificação e de residência |
| `NU_IDADE_N` | Inteiro composto | Idade (o primeiro dígito indica a unidade: dia/mês/ano) — grupo etário prioritário são os menores de 1 ano |
| `ANT_SENTIN` | Inteiro | Unidade sentinela de vigilância da coqueluche |
| `FC_CONTATO` | Inteiro | Contato com caso de coqueluche até 14 dias antes do início dos sintomas (domiciliar, vizinho, outro município/Estado, sem história de contato, ignorado) |
| `CS_VAC_N` | Inteiro | Nº de doses de vacina tríplice (DPT) ou tetravalente (DTP+Hib): 1 a 2 doses, 3 doses, 3 doses + reforços (opção 4/5), 6 - Nunca vacinado, 9 - Ignorado |
| `DT_ULT_DOS` | Data (`AAAAMMDD`) | Data da última dose da vacina DPT/tetravalente |
| `DT_CATARRA` | Data (`AAAAMMDD`) | Data de início do período catarral (referência epidemiológica para investigação de contatos) |
| `CS_TOSSE_E`/`CS_TOSSE_P` | Inteiro | Tosse com mais de 15 dias e tosse paroxística (1 - Sim, 2 - Não) |
| `CS_CRISE`/`CS_CIANOSE`/`CS_VOMITOS`/`CS_APNEIA` | Inteiro | Manifestações do período paroxístico: crises de tosse, cianose, vômitos e apneia |
| `CS_TEMP37`/`CS_TEMP_38` | Inteiro | Resposta térmica do paciente (temperatura ≥37,5 ºC e ≥38 ºC) |
| `CS_PNEUMON`/`CS_ENCEFAL`/`CS_DESITRA`/`CS_OTITE` | Inteiro | Complicações: pneumonia, encefalopatia, fissura/lesão do aspareza desidratação e otite média |
| `CS_HOSPITA` / `DT_INTERNA` | Inteiro / Data | Internação hospitalar e data de internação |
| `CS_COLETA`/`DT_COLETA`/`CS_CULTURA` | Inteiro/Data | Coleta de material (swab nasofaríngeo para cultura), data e resultado da cultura |
| `MED_IDEN_C`/`MED_QUAN_C`/`MED_CASO_S` | Inteiro | Contatos identificadas e suspeitos com eventos de caso índice, para orientar o bloqueio |
| `COLET_COMU`/`QUAN_COMUN`/`QUAN_POSIT` | Inteiro | Comunicantes com coleta de cultura, nº de comunicantes com resultado e nº de resultados positivos |
| `MED_BLOQUE` | Inteiro | Medidas de prevenção/controle: 1 - Bloqueio vacinal, 2 - Quimioprofilaxia, 3 - Ambos, 4 - Não, 9 - Ignorado |
| `CLASSI_FIN` | Inteiro | Classificação final do caso: 1 - Confirmado, 2 - Descartado |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte: 1 - Laboratorial, 2 - Vínculo Epidemiológico, 3 - Clínico |
| `DOENCA_TRA` | Inteiro | Doença relacionada ao trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `EVOLUCAO` | Inteiro | Evolução do caso: 1 - Cura, 2 - Óbito por coqueluche, 3 - Óbito por outras causas, 9 - Ignorado |
| `DT_OBITO` / `DT_ENCERRA` | Data (`AAAAMMDD`) | Data do óbito e de encerramento do caso |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE, `String` com `zfill`), `ID_UNIDADE` (CNES), `ID_OCUPA_N` (CBO); códigos de classificação (`CLASSI_FIN`, `CRITERIO`, `EVOLUCAO`, `MED_BLOQUE`) só viram categóricos após mapeamento explícito.
- **Datas e competências**: `DT_NOTIFIC`, `DT_SIN_PRI`, `DT_CATARRA`, `DT_ULT_DOS`, `DT_INTERNA`, `DT_COLETA`, `DT_OBITO` e `DT_ENCERRA` vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`); `SEM_NOT`/`SEM_PRI` são semanas epidemiológicas `AAAASS`.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: a classificação final segue o vocabulário do dicionário revisado em fevereiro/2012 (confirmado/descartado, com critérios laboratorial, vínculo epidemiológico e clínico); o período catarral (`DT_CATARRA`) pode anteceder `DT_SIN_PRI` e sustenta a janela de 14 dias usada na investigação de contatos; o histórico vacinal (`CS_VAC_N`) exige cuidado com os códigos de reforços (três doses + um ou dois reforços) e nunca vacinado; e o campo `ANT_SENTIN` identifica casos notificados em unidades-sentinela do agravo, com as bases de 2023 a 2026 disponibilizadas apenas em `PRELIM`.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-coqu
quantilica datasus list sinan-coqu

# 2. Baixar microdados de sinan-coqu com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-coqu -o ./data --start 2007 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-coqu -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-coqu -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-coqu/2025/sinan-coqu_preliminar_2025-br@20261007.dbc", clean=True)

# Casos confirmados por critério de confirmação e evolução do caso
conf = qdf.filter(pl.col("classi_fin") == 1).group_by("criterio").len().sort("criterio")
print(conf)

# Hospitalização e complicações (pneumonia) nos casos confirmados
hosp = qdf.filter(
    (pl.col("classi_fin") == 1) & (pl.col("cs_hospita") == 1)
).group_by("cs_pneumon").len().sort("cs_pneumon")
print(hosp)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Coqueluche (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de coqueluche e situações de óbitos em lactentes (vigilância intensificada)
