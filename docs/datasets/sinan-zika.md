# `sinan-zika` — Zika Vírus

O `sinan-zika` contém os microdados das notificações e investigações epidemiológicas de casos de Zika vírus (CID-10 A92.8 — "outros febres virais transmitidas por artrópodes") registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de zika (exantemático), digitada no SINAN Net/Sinan Online. A série começa em 2015, quando a circulação do vírus foi identificada no Brasil durante a emergência associada à microcefalia e à síndrome congênita do vírus zika.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-zika` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 2015 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 12 arquivos (~14 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A zika é uma arbovirose urbana transmitida pelo `Aedes aegypti` (e também por via sexual), gerida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS). A emergência sanitária de 2015-2016 — caracterizada pela associação entre a infecção pelo vírus Zika na gestação e a microcefalia e demais anomalias congênitas, além da síndrome de Guillain-Barré — levou à formalização da doença como evento de notificação compulsória consolidada na Portaria GM/MS nº 204/2016 (lista posteriormente atualizada, ex.: Portaria GM/MS nº 10.175/2026). O dataset fornece a base de notificação individual para monitorar a transmissão, os casos em gestantes e as complicações neurológicas.

O evento gerador é a **Ficha de Notificação/Investigação de Zika** do SINAN. Em 2015/2016 a notificação usou a ficha de febre rash viral/exantemática com módulo de conclusão Zika e, a partir da versão de 2016, a ficha única de dengue/chikungunya/zika do Sinan Online (`ID_AGRAVO` distinguindo o agravo). A unidade de análise é o caso suspeito/confirmado de zika, definido por exantema maculopapular associado a febre, conjuntivite não pruriginosa ou poliúrtia/polyarthralgia conforme a definição de caso vigente, em pessoa residente ou procedente de área com transmissão — não o nascido vivo com anomalia congênita nem o caso de microcefalia (que são monitorados em sistemas próprios como RESP/SINASC).

Marcos de evolução do leiaute: 2015 — primeiras notificações na ficha de febre rash viral com conclusão Zika; 2016 — ficha unificada de arboviroses e plena implantação do Sinan Online Gotas. Como consequência, os campos de investigação específica de zika (sinais e sintomas, complicações neurológicas como Guillain-Barré) só existem na ficha mais recente e, no leiaute antigo, permanecem em branco.

Aplicações analíticas: coeficiente de incidência de zika por 100 mil habitantes, proporção de casos entre gestantes e mulheres em idade fértil, monitoramento de complicações neurológicas pós-infecciosas, análise da concorrência espacial com dengue e chikungunya e estruturação de estudos de coorte da síndrome congênita associada ao vírus zika.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ZIKA` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ZIKA` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `ZIKABR16.dbc` — prefixo `ZIKA`, `BR` (consolidação nacional) e `16` (ano 2016); a série vai de `ZIKABR15.dbc` até `ZIKABR25.dbc`, com o ano corrente em `PRELIM` (ex.: `ZIKABR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-zika/<ano>/sinan-zika_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-zika/2025/sinan-zika_2025-br@20261013.dbc`; arquivos preliminares usam o sufixo do dataset `-preliminar`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e PDFs de acesso/descompactação/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo na ficha unificada (Zika — CID-10 A92.8) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (exantema + febre/conjuntivite/outras) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_GESTANTE` | Inteiro | Estado gestacional — crucial para o monitoramento de gestantes |
| `ID_MN_RESI` | String (6/7) | Município de residência do paciente (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `CLASSI_FIN` | Inteiro | Classificação final (confirmação/descarte/inconclusivo da zika conforme o dicionário do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte (1 - Laboratório, 2 - Clínico Epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: manter `ID_MUNICIP`, `ID_MN_RESI` (IBGE 6/7 dígitos), `ID_UNIDADE` (CNES) e `NU_NOTIFIC` como `String` com `zfill`; códigos de classificação e evolução só viram categóricos após o mapeamento de rótulos.
- **Datas e competências**: `DT_NOTIF`, `DT_SIN_PRI`, `DT_INVEST`, `DT_OBITO` e `DT_ENCERRA` em `AAAAMMDD` → `pl.Date`; semanas (`SEM_NOT`, `SEM_PRI`) permanecem `Int64`.
- **Valores ausentes e sentinelas**: células em branco, datas `00000000`, códigos `999999`/`99999999` e `9 - Ignorado` são normalizados para nulo pelo `SENTINEL_NULLS`; registros com marcador de exclusão dBASE (`_deleted`) são descartados.
- **Particularidades do dataset**: volume pequeno (12 consolidações `BR` anuais, ~14 MB) — a notificação de zika decai após a epidemia de 2015-2016, mas casos suspeitos continuam sendo registrados; parte dos casos pode estar embutida na ficha unificada de dengue/chikungunya, exigindo filtro por `ID_AGRAVO` para recompor a base; grande proporção de confirmação clínico-epidemiológica exige cautela com `CLASSI_FIN`; gestantes merecem atenção especial via `CS_GESTANTE` e o arquivo do ano corrente em `PRELIM` é sujeito a revisão.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-zika
quantilica datasus list sinan-zika

# 2. Baixar microdados de sinan-zika com recorte adequado à partição do dataset
quantilica datasus sync sinan-zika -o ./data --start 2015 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-zika -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-zika -o ./data/raw --parquet-dir ./data/parquet --start 2015
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de zika já tratado
qdf = read_dbc("data/sinan-zika/2025/sinan-zika_2025-br@20261013.dbc", clean=True)

# Casos de zika por ano e proporção entre gestantes
por_ano = qdf.group_by("nu_ano").agg(
    n=pl.len(),
    gestantes=(pl.col("cs_gestante").is_in([1, 2, 3, 4])).sum(),
)
print(por_ano.sort("nu_ano").with_columns(
    (pl.col("gestantes") / pl.col("n")).alias("prop_gestantes")
))

# Curva epidêmica mensal de início dos sintomas
mensal = (
    qdf.group_by(pl.col("dt_sin_pri").dt.to_span("month").alias("mes"))
    .len()
    .sort("mes")
)
print(mensal)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Nota técnica SINAN – Dengue/Chikungunya/Zika (Sinan Online)**: https://sistemas.saude.rj.gov.br/tabnetbd/Sinan/NT_dengue_chik_zika.pdf
- **Portal SINAN — Dengue/Chikungunya/Zika (fichas e dicionários)**: https://portalsinan.saude.gov.br/sinan-dengue-chikungunya
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde** (SVSA/MS, capítulo Zika e síndrome congênita)
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
