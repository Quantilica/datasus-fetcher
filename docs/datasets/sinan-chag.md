# `sinan-chag` — Doença de Chagas Aguda

O `sinan-chag` contém os microdados das notificações e investigações de casos de Doença de Chagas em fase aguda (CID-10 B57.0/B57.1/B57.2) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de Chagas agudo, digitada no SINAN Net/Sinan Online pelas unidades de saúde. Embora a cardiopatia crônica do Chagas não seja notificada no SINAN, a fase aguda da doença — especialmente via transmissão oral em surtos familiares — é de notificação compulsória imediata.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-chag` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 2000 a 2025 (conforme `index.json`) |
| **Volume aproximado no FTP** | 26 arquivos (~5,1 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A doença de Chagas aguda (infecção pelo *Trypanosoma cruzi* com fase aguda sintomática) é de notificação compulsória imediata — em até 24 horas — conforme a lista nacional (Portaria SVS/MS nº 104/2011; consolidada na Portaria GM/MS nº 204/2016). A vigilância é gerida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), com foco na detecção de casos de transmissão vetorial (triatomíneos domiciliados e peridomiciliados), transmissão oral (consumo de açaí, caldo de cana e outros alimentos contaminados por fezes de triatomíneos — principal mecanismo atual de surtos no país), transmissão congênita e acidental (laboratorial). A base dimensiona a persistência da morbidade chagásica em áreas rurais e a emergência de transmissões por via alimentar em contexto urbano.

O evento gerador é a **Ficha de Investigação da Doença de Chagas Aguda** do SINAN (ficha `Chagas_agudo_v5`), preenchida na suspeição do caso (febre com sinais como chagoma de inoculação, sinal de Romaña, hepatoesplenomegalia) e completada com dados da investigação, exames parasitológicos/sorológicos (gota espessa, hemocultura, anticorpos IgM e IgG), identificação da via de transmissão e sorovigilância de comunicantes. A unidade de análise é o caso suspeito/confirmado individual.

Marcos históricos: a notificação compulsória da fase aguda constava já da lista da Portaria SVS/MS nº 5/2006; a expansão da transmissão oral nos anos 2000 (grandes surtos detectados a partir de 2005-2006) recalibrou os protocolos de investigação na ficha mais recente, com enfoque na investigação alimentar de surtos, e a vigilância passou a integrar o registro de insetos triatomíneos capturados; surtos de maiores dimensões podem ser registrados também no módulo de surto do SINAN.

Aplicações analíticas: coeficiente de incidência de Chagas agudo por 100 mil habitantes, distribuição por via de transmissão (vetorial, oral, congênita, acidental, transfusional), letalidade da fase aguda, mapeamento de municípios com transmissão ativa, monitoramento de surtos alimentares (ação conjunta entre vigilância epidemiológica e vigilância sanitária) e vigilância de comunicantes/famíliares infectados.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `CHAG` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `CHAG` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `CHAGBR00.dbc` — prefixo `CHAG`, `BR` (consolidação nacional) e `00` (ano 2000, primeira série do FTP); os arquivos finais vão até `CHAGBR22.dbc` (2022), com os anos recentes em `PRELIM` (ex.: `CHAGBR25.dbc`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-chag/<ano>/sinan-chag_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-chag/2022/sinan-chag_2022-br@20260928.dbc`, com a variante `-preliminar` para os arquivos do `PRELIM`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Doença de Chagas aguda — CID-10 B57.x) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave, compulsória em até 24h) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (febre, chagoma, sinal de Romaña etc.) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_RACA` | Inteiro | Raça/cor (1-Branca, 2-Preta, 3-Amarela, 4-Parda, 5-Indígena, 9-Ignorado) |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `CLASSI_FIN` | Inteiro | Classificação final (1 - Confirmado, 5 - Descartado ou equivalente agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento (cierre) do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: manter `ID_MUNICIP`, `ID_MN_RESI` (IBGE 6/7 dígitos), `ID_UNIDADE` (CNES) e ocupação CBO como `String` com `zfill`; códigos de classificação final/critério/evolução devem ser mapeados somente após normalização.
- **Datas e competências**: `DT_NOTIF`, `DT_SIN_PRI`, `DT_INVEST`, `DT_OBITO` e `DT_ENCERRA` em `AAAAMMDD` convertidos para `pl.Date`; semanas epidemiológicas (`SEM_NOT`, `SEM_PRI`) como inteiras.
- **Valores ausentes e sentinelas**: células em branco, datas `00000000`, códigos `999999`, `99999999` e `9` (ignorado) viram nulo por `SENTINEL_NULLS`; registros com marcador de exclusão dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: o volume é baixo e disperso (26 consolidações `BR` anuais de ~5 MB), com poucos casos por ano — o cálculo de coeficientes por 100 mil habitantes exige denominadores precisos; os arquivos finais vão até 2022 e os anos recentes aparecem apenas em `PRELIM`, sinalizando que os dados mais recentes podem ser revisados; surtos alimentares e vetoriais são caracterizados apenas nos campos de investigação específicos da ficha, que frequentemente ficam incompletos.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-chag
quantilica datasus list sinan-chag

# 2. Baixar microdados de sinan-chag com recorte adequado à partição do dataset
quantilica datasus sync sinan-chag -o ./data --start 2000 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-chag -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-chag -o ./data/raw --parquet-dir ./data/parquet --start 2000
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de Chagas agudo já tratado
qdf = read_dbc("data/sinan-chag/2022/sinan-chag_2022-br@20260928.dbc", clean=True)

# Casos confirmados por ano
print(
    qdf.filter(pl.col("classi_fin").is_in([1, 10, 11]))
    .group_by("nu_ano")
    .len()
    .sort("nu_ano")
)

# Distribuição por UF de notificação
print(
    qdf.filter(pl.col("classi_fin").is_in([1, 10, 11]))
    .group_by("sg_uf_not")
    .len()
    .sort("len", descending=True)
)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Doença de Chagas Aguda**: https://portalsinan.saude.gov.br/doenca-de-chagas-aguda
- **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo Doença de Chagas aguda; **Portaria GM/MS nº 204/2016**
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
