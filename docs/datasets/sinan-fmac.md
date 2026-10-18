# `sinan-fmac` — Febre Maculosa

O `sinan-fmac` contém os microdados das notificações e investigações de casos de Febre Maculosa (FM Brasileira, CID-10 A77.0) e outras riquetsioses registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de febre maculosa, digitado no SINAN Net/Sinan Online. O agravo é de notificação compulsória imediata (até 24 horas) e a base tem elevada relevância clínica porque a doença tem alta letalidade quando não tratada rapidamente.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-fmac` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 20 arquivos (~6,2 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A Febre Maculosa Brasileira é causada pela bactéria *Rickettsia rickettsii*, transmitida pela picada de carrapatos (sobretudo o carrapato-estrela *Amblyomma cajennense sensu lato*, com reservatórios silvestres como capivaras e roedores), e é a riquetsiose mais grave do continente. A vigilância é gerida pela SVSA/MS; o caso suspeito é de notificação compulsória imediata e a investigação inclui indicadores de letalidade historicamente altos (podendo ser superiores a 30-40% em áreas urbanas, pacientes geralmente internados em UTI). Casos de FM e de outras riquetsioses de interesse são fluxos mantidos em regiões endêmicas da Sudeste (Vale do Anhembi em SP, entre outros) e há ocorrência pontual no Sul e no Nordeste.

O evento gerador é a **Ficha de Investigação de Febre Maculosa** do SINAN (ficha `Febre_Maculosa_v5`, com dicionário de dados revisto em 2012), preenchida na suspeição — indivíduo com febre, cefaléia, mialgia e história de picada de carrapatos e/ou contato com animais domésticos/silvestres e/ou permanência em área sabidamente de transmissão nos últimos 15 dias e/ou exantema máculo-papular ou manifestações hemorrágicas — e completada ao longo da investigação com dados clínicos, laboratoriais (imunofluorescência indireta, reação em cadeia, PCR), hospitalização e desfecho. A unidade de análise é o caso suspeito/confirmado notificado individualmente.

Na lista de notificação compulsória inicial (Portaria SVS/MS nº 5/2006), o agravo constava já na versão SINAN de 2006, mas no FTP o primeiro arquivo final aceito é o de 2007; a partir de então, casos são recorrentes em épocas quentes. O SINAN posteriormente incorporou o registro da notificação de febre maculosa e de outras riquetsioses de interesse, com a vigência de notificação imediata estabelecida pela Portaria de Consolidação (GM/MS nº 204/2016) e atualizações recentes.

Aplicações analíticas: coeficiente de incidência, taxa de letalidade e mortalidade (a FM tem letalidade entre as mais altas dos agravos notificados no SINAN), distribuição por município provável de infecção, faixa etária e exposições (trabalhos em áreas de mata, capivaras urbanas), oportunidade de notificação (intervalo entre inicio de sintomas e notificação é decisivo para o desfecho) e vigilância de áreas com transmissão ativa.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `FMAC` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `FMAC` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `FMACBR07.dbc` — prefixo `FMAC`, `BR` (consolidação nacional) e `07` (ano 2007), até `FMACBR21.dbc` (2021); os anos recentes ficam em `PRELIM` (ex.: `FMACBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-fmac/<ano>/sinan-fmac_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-fmac/2021/sinan-fmac_2021-br@20260825.dbc`; arquivos preliminares recebem o sufixo `-preliminar`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Febre Maculosa — CID-10 A77.0) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data de preenchimento da ficha de notificação (campo-chave; notificação imediata) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (febre, cefaléia, mialgia) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação (campo obrigatório da ficha de FM) |
| `ID_OCUPA_C` | String (6) | Ocupação/ramo de atividade econômica do paciente (CBO 6 dígitos) |
| `CLASSI_FIN` | Inteiro | Classificação final do caso (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP`, `ID_MN_RESI` e `ID_OCUPA_C` (IBGE 6/7 e CBO 6 dígitos) mantidos como `String` com `zfill`; códigos de classificação final, critério e evolução permanecem categóricos apenas após mapeamento.
- **Datas e competências**: `DT_NOTIF`, `DT_SIN_PRI`, `DT_INVEST`, `DT_OBITO` e `DT_ENCERRA` em `AAAAMMDD` convertidos para `pl.Date`; semanas epidemiológicas ficam como inteiras.
- **Valores ausentes e sentinelas**: células em branco, datas `00000000`, códigos `9`/`99`/`999999`/`99999999` tratados como nulo por `SENTINEL_NULLS`; registros com marcador de exclusão dBASE (`_deleted`) removidos.
- **Particularidades do dataset**: volume pequeno (20 consolidações `BR` anuais, ~6 MB), mas com concentrados de grande gravidade — a letalidade da FM é realçada; parte da investigação específica da ficha (exposição a carrapato, exames serológicos) fica em branco (as campos exigem pré-preenchimento apenas em unidades investigadoras); casos podem ser notificados em UF diferente da exposição (casos importados), refletidos nos campos de local provável de infecção; o arquivo do ano corrente em `PRELIM` é sujeito a revisão.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-fmac
quantilica datasus list sinan-fmac

# 2. Baixar microdados de sinan-fmac com recorte adequado à partição do dataset
quantilica datasus sync sinan-fmac -o ./data --start 2007 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-fmac -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-fmac -o ./data/raw --parquet-dir ./data/parquet --start 2007
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de febre maculosa já tratado
qdf = read_dbc("data/sinan-fmac/2021/sinan-fmac_2021-br@20260825.dbc", clean=True)

# Casos confirmados e letalidade por ano
confirmados = qdf.filter(pl.col("classi_fin") == 1)
resumo = confirmados.group_by("nu_ano").agg(
    casos=pl.len(),
    obitos=(pl.col("evolucao") == 2).sum(),
)
print(resumo.sort("nu_ano").with_columns(
    (pl.col("obitos") / pl.col("casos")).alias("letalidade")
))

# Casos confirmados por município de notificação
print(
    confirmados.group_by("id_municip")
    .len()
    .sort("len", descending=True)
)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Febre Maculosa (ficha, instrucional, dicionário)**: http://portalsinan.saude.gov.br/febre-maculosa
- **Dicionário de Dados Febre Maculosa v5**: http://www.portalsinan.saude.gov.br/images/documentos/Agravos/Febre%20Maculosa/DIC_DADOS_Febre_Maculosa_v5.pdf
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo Febre Maculosa
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
