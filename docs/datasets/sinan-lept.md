# `sinan-lept` — Leptospirose

O `sinan-lept` contém os microdados das notificações e investigações de casos de Leptospirose (CID-10 A27) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de leptospirose, digitado no SINAN Net/Sinan Online. A doença é de notificação compulsória e a base concentra grande parte dos registros do ciclo de enchentes e desastres climáticos, ao lado dos casos ocupacionais em ambientes com água e inundações.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-lept` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 2000 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 27 arquivos (~31,8 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A leptospirose é uma zoonose causada por espiroquetas do gênero *Leptospira* (principalmente *L. interrogans*), transmitida ao homem por contato direto ou indireto com urina de animais infectados — sobretudo roedores urbanos —, bem como por inundações e água contaminada na época das chuvas. No âmbito ocupacional, a exposição é relevante para trabalhadores de saneamento e limpeza urbana, coleta de resíduos, esgoto, agricultura e pesca. A vigilância é da SVSA/MS, com o agravo na Lista de Notificação Compulsória desde a Portaria de Consolidação (GM/MS nº 204/2016) e anteriormente desde a Portaria SVS/MS nº 5/2006; a notificação imediata é mandatória para os casos graves.

O instrumento é a **Ficha de Investigação de Leptospirose** do SINAN (ficha `Leptospirose_v5`), que registra a notificação do caso suspeito e, ao longo da investigação, os exames laboratoriais empregados (MAT — teste de aglutinação microscópica, ELISA, macroaglutinação e PCR) e o desfecho clínico. A unidade de análise é o caso suspeito/confirmado notificado individualmente, com atenção ao contexto de exposição (transporte, ambiente ocupacional, inundação).

O número anual de casos é compatível com um padrão sazonal marcado por chuvas intensas e desastres climáticos — por exemplo, as grandes inundações de 2008 em Santa Catarina e de 2011 no Rio de Janeiro produziram picos de notificação. A capacidade do SINAN de registrar casos pós-desastre facilita a articulação entre vigilância epidemiológica e gestão de riscos ambientais.

Aplicações analíticas: coeficiente de incidência por 100 mil, letalidade (a leptospirose grave tem letalidade elevada), distribuição por sexo/idade/ocupação, análise de fatores de exposição (inundações, ambientes urbanos deteriorados), associação climática por semana epidemiológica e respostas posteriormente a desastres.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `LEPT` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `LEPT` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `LEPTBR00.dbc` — prefixo `LEPT`, `BR` (consolidação nacional) e `00` (ano 2000), até `LEPTBR24.dbc` (2024); arquivos preliminares em `PRELIM` (ex.: `LEPTBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-lept/<ano>/sinan-lept_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-lept/2024/sinan-lept_2024-br@20260715.dbc`; arquivos preliminares recebem o sufixo `-preliminar`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Leptospirose — CID-10 A27) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave; notificação imediata nos casos graves) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data do início dos sintomas |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_RACA` | Inteiro | Raça/cor (1-Branca ... 5-Indígena, 9-Ignorado) |
| `ID_OCUPA_C` | String (6) | Ocupação do paciente, em código CBO (limpeza urbana, saneamento etc.) |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DOENCA_TRA` | Inteiro | Relação do caso com o trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `CLASSI_FIN` | Inteiro | Classificação final (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: manter `ID_MUNICIP`, `ID_MN_RESI` (IBGE 6/7 dígitos), `ID_UNIDADE` (CNES) e `ID_OCUPA_C` (CBO), e `DOENCA_TRA` como mapeamento de rótulo apenas posterior; nunca converter códigos para numérico antes de normalizar.
- **Datas e competências**: `DT_NOTIF`, `DT_SIN_PRI`, `DT_INVEST`, `DT_OBITO` e `DT_ENCERRA` em `AAAAMMDD` convertidos para `pl.Date`; semanas epidemiológicas `SEM_NOT`/`SEM_PRI` ficam como `Int64`.
- **Valores ausentes e sentinelas**: células em branco, datas `00000000`, códigos `9`/`99`/`999999` tratados como nulo por `SENTINEL_NULLS`; registros com marcador de exclusão dBASE (`_deleted`) removidos.
- **Particularidades do dataset**: forte sazonalidade com picos de chuvas e enchentes; atenção à separação entre incidência e subnotificação de casos laboratoriais não confirmados em surtos; cuidado com o grande número de notificações descartadas (diagnósticos diferenciais de outras febres agudas); parte dos casos ocupacionais também aparece em bases de vigilância de acidentes de trabalho, o que exige deduplicação; e o arquivo do ano em curso em `PRELIM` é sujeito a revisão.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-lept
quantilica datasus list sinan-lept

# 2. Baixar microdados de sinan-lept com recorte adequado à partição do dataset
quantilica datasus sync sinan-lept -o ./data --start 2000 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-lept -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-lept -o ./data/raw --parquet-dir ./data/parquet --start 2000
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de leptospirose já tratado
qdf = read_dbc("data/sinan-lept/2024/sinan-lept_2024-br@20260715.dbc", clean=True)

# Casos confirmados por ano e UF
confirmados = qdf.filter(pl.col("classi_fin") == 1)
print(
    confirmados.group_by("nu_ano", "sg_uf_not")
    .len()
    .sort(["nu_ano", "sg_uf_not"])
)

# Sazonalidade: casos confirmados por mês de início dos sintomas
print(
    confirmados.select(
        pl.col("dt_sin_pri").dt.month().alias("mes")
    )
    .group_by("mes")
    .len()
    .sort("mes")
)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Leptospirose (ficha e dicionário)**: https://portalsinan.saude.gov.br/leptospirose
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo Leptospirose
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
