# `sinan-hans` — Hanseníase

O `sinan-hans` contém os microdados das notificações e investigações epidemiológicas de casos de Hanseníase/Doença de Hansen (CID-10 A30) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha de notificação/investigação (ou boletim de acompanhamento) de um caso de hanseníase, preenchida pelas unidades de saúde do SUS em todo o país a partir da avaliação dermatoneurológica do paciente. É a base oficial para dimensionamento da morbidade da hanseníase no país, com 64 campos da rotina v5.0 cobrindo desde forma clínica e classificação operacional até desfecho de alta (cura, transferência, óbito, abandono, erro diagnóstico) e contatos examinados.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-hans` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (bases `FINAIS` históricas e anos recentes apenas em `PRELIM`) |
| **Cobertura temporal no FTP** | 2001 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 26 arquivos (~60,9 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

Hanseníase é doença infecciosa crônica de notificação compulsória desde o início da vigilância nacional brasileira (Lei nº 6.259/1975 e Decreto nº 78.231/1976) e, hoje, consta na Lista Nacional de Doenças e Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). O programa de controle é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), por meio do Departamento de Doenças de Condições Crônicas e Infecções Sexualmente Transmissíveis (DCCI), em articulação com o GT-SINAN. O Brasil concentra um dos maiores contingentes de casos novos do mundo; a base alimenta os indicadores oficiais de incidência por 100 mil habitantes, de prevalência (casos em tratamento), detecção em menores de 15 anos, grau de incapacidade física no diagnóstico e atuação dos serviços de referência em dermatologia sanitária.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Hanseníase** (ficha v5.0; o acompanhamento de casos já notificados ocorre por meio do boletim individual, o mesmo instrumento do Sinan Net). Cada notificação nasce quando o paciente é diagnosticado por exame dermatoneurológico (lesão ou placa cutânea com perda de sensibilidade, nervo periférico acometido e, quando indicado, baciloscopia intradérmica) e é completada ao longo da investigação e do acompanhamento com dados de classificação operacional (paucibacilar/multibacilar), esquema antileprótico (PQT/6 e PQT/MB/12 doses), doses supervisionadas, episódios reacionais, notificação do grau de incapacidade física no diagnóstico e no acompanhamento e desfecho da alta. A unidade de análise é o caso (paciente) registrado no SINAN — cada ficha é a unidade de notificação individual do agravo.

A série histórica registra três fases do sistema de informação: de **2001 a 2006** os dados provêm do Sinan-Windows (com campo `MIGRADO_W` distinguindo registros migrados); de **2007 em diante**, as bases provêm do Sinan Net com o Sinan Online (mesma base disseminada). Mudanças importantes do instrumento incluem a separação da notificação em **ficha de notificação** (diagnóstico) e o **boletim/transferência vertical** de acompanhamento em anos subsequentes, e a inclusão de campos administrativos das transferências (`UFATUAL`, `ID_MUNI_AT`, `DT_NOTI_AT`, `UFRESAT` para registrar a unidade responsável pelo acompanhamento atual do caso) e controles de vinculação de registros (`IN_VINCULA`, `NU_LOTE_IA`).

Aplicações analíticas típicas: incidência de casos novos e densidade de pacientes multibacilares; detecção de casos em menores de 15 anos (idade e fonte de infecção); distribuição de formas clínicas (indeterminada, tuberculóide, dimorfa, virchowiana) e da classificação operacional (PB/MB); percentual de casos com grau de incapacidade física (0, I, II) no diagnóstico e no acompanhamento; doses de poliquimioterapia supervisionada (`DOSE_RECEB`); frequência de episódios reacionais (`EPIS_RACIO`); proporções de cura, abandono e óbito (tipo de saída `TPALTA_N`); e cobertura de contatos registrados e examinados (`CONTREG`/`CONTEXAM`).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `HANS` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `HANS` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `HANSBR23.dbc` — `HANS` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `23` é o ano de notificação (2023). As consolidações até 2023 estão em `FINAIS` e os anos de 2024 a 2026 estão apenas em `PRELIM` (ex.: `HANSBR26.dbc`, atualização de 29/09/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-hans/<ano>/sinan-hans_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-hans/2026/sinan-hans_preliminar_2026-br@20260929.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `HANSBR23.dbc` (64 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_DIAG` | Data (`AAAAMMDD`) | Data do diagnóstico (base da abertura da ficha epidemiológica) |
| `SEM_DIAG` | Inteiro (`AAAASS`) | Semana epidemiológica do diagnóstico |
| `NU_IDADE_N` | Inteiro composto | Idade (o primeiro dígito indica a unidade: dia/mês/ano) |
| `CS_SEXO` | String (1) | Sexo do paciente (M/F/I - Ignorado) |
| `ID_MN_RESI` | String (6/7) | Código IBGE do município de residência (base de contagem) |
| `NU_LESOES` | Inteiro | Número de lesões cutâneas identificadas no exame dermatoneurológico |
| `FORMACLINI` | Inteiro | Forma clínica pela classificação de Madrid: 1 - Indeterminada, 2 - Tuberculóide, 3 - Dimorfa, 4 - Virchowiana, 5 - Não classificado |
| `AVALIA_N` | Inteiro | Grau de incapacidade física no diagnóstico: 0 - Grau zero, 1 - Grau I, 2 - Grau II, 3 - Não avaliado |
| `CLASSOPERA` | Inteiro | Classificação operacional: 1 - PB (Paucibacilar), 2 - MB (Multibacilar) |
| `MODOENTR` | Inteiro | Modo de entrada: caso novo, recorrentes/recidiva ou transferências entre unidades, municípios, estados e países |
| `MODODETECT` | Inteiro | Modo de detecção do caso (espontâneo, por encaminhamento, exame de contato/coletividade) |
| `BACILOSCOP` | Inteiro | Resultado da baciloscopia (positiva/negativa/não realizada) |
| `DTINICTRAT` | Data (`AAAAMMDD`) | Data de início do tratamento RS/PQT (base do indicador de cumprimento do esquema) |
| `ESQ_INI_N` / `ESQ_ATU_N` | Inteiro | Esquema terapêutico inicial e atual: PQT/PB (6 doses), PQT/MB (12 doses) ou outros esquemas substitutivos |
| `CONTREG` | Inteiro | Nº de contatos domiciliares registrados (residiram nos últimos 5 anos com o paciente) |
| `NERVOSAFET` | Inteiro | Número de nervos afetados no exame dermatoneurológico |
| `UFATUAL`/`ID_MUNI_AT`/`ID_UNID_AT` | String | Unidade federativa atual, município e unidade de saúde (CNES) responsáveis pelo acompanhamento atual do caso |
| `DT_NOTI_AT` | Data (`AAAAMMDD`) | Data da atualização da notificação (boletim de acompanhamento/transferência) |
| `DTULTCOMP` | Data (`AAAAMMDD`) | Data da última consulta/atendimento de acompanhamento |
| `CLASSATUAL` | Inteiro | Classificação operacional atual (PB/MB) no acompanhamento |
| `AVAL_ATU_N` | Inteiro | Avaliação do grau de incapacidade física no acompanhamento (0/I/II/não avaliado) |
| `DOSE_RECEB` | Inteiro | Número de doses supervisionadas já recebidas pelo paciente |
| `EPIS_RACIO` | Inteiro | Ocorrência de episódios reacionais durante o acompanhamento |
| `DTMUDESQ` | Data (`AAAAMMDD`) | Data de mudança do esquema terapêutico (se pertinente) |
| `CONTEXAM` | Inteiro | Número de contatos examinados (sempre ≤ contatos registrados) |
| `DTALTA_N` | Data (`AAAAMMDD`) | Data da alta (encerramento do caso) |
| `TPALTA_N` | Inteiro | Tipo de saída/alta: 1 - Cura, 2 - Transferência para o mesmo município, 3 - Transferência para outro município, 4 - Transferência para outro estado, 5 - Transferência para outro país, 6 - Óbito, 7 - Abandono, 8 - Erro diagnóstico |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP`, `ID_MN_RESI` e `ID_MUNI_AT` (códigos IBGE, `String` com `zfill`), `ID_UNIDADE` e `ID_UNID_AT` (CNES de 7 dígitos), `ID_OCUPA_N` (CBO); códigos de classificação (`FORMACLINI`, `CLASSOPERA`, `MODOENTR`, `TPALTA_N`) só viram categóricos após mapeamento explícito.
- **Datas e competências**: `DT_DIAG`, `DTINICTRAT`, `DT_NOTI_AT`, `DTULTCOMP`, `DTMUDESQ`, `DTALTA_N` vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`).
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com o marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: a hanseníase cobre tanto **fichas de notificação** quanto **boletins de acompanhamento** de casos transferidos entre municípios/unidades — um caso pode aparecer mais de uma vez seguido de atualizações (`UFATUAL`, `DT_NOTI_AT`), exigindo deduplicação por caso antes de indicadores agregados; contar casos novos exige filtrar `MODOENTR` = 1 (Caso novo); o inventário de bases muda entre `FINAIS` (2001 a 2023) e `PRELIM` (2024 a 2026); a idade em `NU_IDADE_N` requer decomposição do primeiro dígito; e o campo `IN_VINCULA` marca notificações vinculadas pelo sistema a outras fichas (hanseníase/tuberculose).

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-hans
quantilica datasus list sinan-hans

# 2. Baixar microdados de sinan-hans com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-hans -o ./data --start 2001 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-hans -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-hans -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-hans/2023/sinan-hans_2023-br@20240912.dbc", clean=True)

# Casos novos multibacilares (maior grau de transmissibilidade e complexidade clínica)
casos_mb = qdf.filter(
    (pl.col("modoentr") == 1) & (pl.col("classopera") == 2)
)
print(casos_mb.group_by("formaclini").len().sort("formaclini"))

# Grau de incapacidade física no diagnóstico por ano de diagnóstico
grau = (
    casos_mb.group_by(["avalia_n", "nu_ano"])
    .len()
    .sort(["nu_ano", "avalia_n"])
)
print(grau)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Hanseníase (ficha, dicionário e boletim de acompanhamento v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de hanseníase e Diretrizes para vigilância, atenção e eliminação da hanseníase
