# `sinan-raiv` — Raiva

O `sinan-raiv` contém os microdados das notificações e investigações de casos de Raiva Humana (CID-10 A82) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de raiva humana, digitado no SINAN Net/Sinan Online. A raiva humana é de notificação compulsória imediata (em até 24 horas) e a base é o insumo oficial para acompanhar o último elo do ciclo de vigilância da raiva, cuja meta é a eliminação mediada pelo atendimento antirrábico (dataset `sinan-antr`).

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-raiv` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 20 arquivos (~0,2 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A raiva humana é uma encefalite viral de quase 100% de letalidade, uma vez iniciados os sintomas, com notificação compulsória imediata (Portaria SVS/MS nº 104/2011; consolidada na Portaria GM/MS nº 204/2016). A vigilância é da SVSA/MS, por meio do Programa de Vigilância da Raiva, que integra o registro de casos humanos (deste dataset), a vigilância de epizootias em animais (canina, felina, silvestre — morcegos hematófagos e não hematófagos) e o registro de atendimentos antirrábicos (`sinan-antr`). O Brasil reduziu drasticamente o número de casos humanos: a grande maioria na atualidade envolve morcegos silvestres e populações rurais indígenas.

O evento gerador é a **Ficha de Investigação de Raiva Humana** do SINAN (ficha `Raiva_v5`, de 2006, com instrucional e dicionário próprios), preenchida diante do caso suspeito — pessoa com encefalite aguda progressiva (excitação, paralisia, sialorreia, hidrofobia) ou morte súbita por encefalite sem causa, com história de exposição (mordedura, arranhadura, lambedura em mucosa, contato indireto) e/ou epizootia precedente — e completada com exames (imunofluorescência direta e RT-PCR em material clínico) e o desfecho fatal, pois praticamente todos os casos confirmados terminam em óbito. A unidade de análise é o caso suspeito/confirmado individual.

Marcos de leiaute: a ficha `Raiva_v5` (2006) padronizada no SINAN Net traz campos de exposição ao vírus (tipo de exposição, localização), espécie do animal agressor (canina, felina, quiróptera/morcego, primata, raposa), tratamento em curso e datas de aplicação de doses de vacina e soro. Com a expansão da cobertura da vacinação canina, a cadeia dominante de casos humanos atuais envolve morcegos (hematófagos e não hematófagos).

Aplicações analíticas: monitor da eliminação da raiva, espécie do animal agressor e localização provável de infecção, letalidade (aprox. 100% nos casos confirmados), casos em população indígena e rural, e integração com epizootias e atendimentos antirrábicos (dataset `sinan-antr`).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `RAIV` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `RAIV` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `RAIVBR07.dbc` — prefixo `RAIV`, `BR` (consolidação nacional) e `07` (ano 2007), até `RAIVBR24.dbc` (2024); os anos recentes ficam em `PRELIM` (ex.: `RAIVBR26.dbc`). O volume é minúsculo (~163 kB em 20 arquivos), pois os casos humanos de raiva são eventos raríssimos e esporádicos.
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-raiv/<ano>/sinan-raiv_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-raiv/2024/sinan-raiv_2024-br@20260602.dbc`; arquivos preliminares recebem o sufixo `-preliminar`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Raiva Humana — CID-10 A82.9 e demais A82.x) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave; compulsória imediata) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (encefalite progressiva) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `ESP_ANIMAL` | String | Espécie do animal agressor (1 - Canina, 2 - Felina, 3 - Quiróptera/Morcego, 4 - Primata, 5 - Raposa, 7 - Outra, 9 - Ignorado) |
| `CLASSI_FIN` | Inteiro | Classificação final (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: manter `ID_MUNICIP`, `ID_MN_RESI` (IBGE 6/7 dígitos) e `ID_UNIDADE` (CNES) como texto com `zfill`; códigos de classificação final/critério/evolução e espécie de animal agressor mapeados como categóricos apenas posteriormente.
- **Datas e competências**: `DT_NOTIF`, `DT_SIN_PRI`, `DT_INVEST`, `DT_OBITO` e `DT_ENCERRA` em `AAAAMMDD` convertidos para `pl.Date`; semanas epidemiológicas permanecem inteiras.
- **Valores ausentes e sentinelas**: células em branco, datas `00000000`, códigos `9`/`99`/`999999` tratados como nulo por `SENTINEL_NULLS`; registros com marcador dBASE de exclusão (`_deleted`) removidos.
- **Particularidades do dataset**: volume mínimo (20 consolidações `BR` anuais, ~163 kB) — cada caso humano é um evento raro e muito investigado; cada leitura anual recupera casos confirmados dispersos em poucas UFs; casos registrados em município de internação podem divergir do município de residência (exposição rural), e o arquivo do ano corrente em `PRELIM` é sujeito a revisão.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-raiv
quantilica datasus list sinan-raiv

# 2. Baixar microdados de sinan-raiv com recorte adequado à partição do dataset
quantilica datasus sync sinan-raiv -o ./data --start 2007 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-raiv -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-raiv -o ./data/raw --parquet-dir ./data/parquet --start 2007
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de raiva humana já tratado
qdf = read_dbc("data/sinan-raiv/2024/sinan-raiv_2024-br@20260602.dbc", clean=True)

# Casos confirmados por ano
print(qdf.filter(pl.col("classi_fin") == 1).group_by("nu_ano").len().sort("nu_ano"))

# Espécie do animal agressor nos casos confirmados
print(
    qdf.filter(pl.col("classi_fin") == 1)
    .group_by("esp_animal")
    .len()
    .sort("len", descending=True)
)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Raiva Humana**: https://portalsinan.saude.gov.br/raiva-humana
- **Ficha de Investigação Raiva Humana (Raiva_v5)**: http://portalsinan.saude.gov.br/images/documentos/Agravos/Raiva%20Humana/Raiva_v5.pdf
- **Portaria GM/MS nº 204/2016**, **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo raiva; Programa Nacional de Profilaxia da Raiva
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
