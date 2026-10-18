# `sinan-anim` — Acidente por Animais Peçonhentos

O `sinan-anim` contém os microdados das notificações de acidentes por animais peçonhentos (CID-10 X20-X29) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação de um acidente por serpente (botrópico, crotálico, elapídico, laquético), aranha (foneutrismo/loxoscelismo/latrodectismo), escorpião, lagarta (lonomia), abelha ou outro animal peçonhento, digitada no SINAN Net/Sinan Online. O agravo é de notificação compulsória e é um dos maiores volumes do SINAN, pois os acidentes escorpiônicos no Brasil superam 150 mil casos por ano na atualidade.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-anim` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 20 arquivos (~207 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A vigilância dos acidentes por animais peçonhentos é gerida pela SVSA/MS com o programa de saneamento e controle de peçonhentos: serpentes (*Bothrops*, *Crotalus durissus*, *Micrurus*, *Lachesis*), aranhas (*Phoneutria*, *Loxosceles*, *Latrodectus*), escorpiões (sobretudo o *Tityus serrulatus* em expansão urbana), lagartas (*Lonomia obliqua*), abelhas e outros artrópodes. As notificações humanas — de grande impacto sanitário, sobretudo na população urbana em expansão do escorpionismo — são compulsórias desde a Portaria SVS/MS nº 5/2006 e permanecem na lista nacional consolidada (Portaria GM/MS nº 204/2016). A notificação usa ficha própria, notificação individual de acidente por animal peçonhento (ficha `Animais_Peconhentos_v5`), de interesse nacional.

O evento gerador é a ficha de acidente por animais peçonhentos, que registra o tipo de animal (1-Serpente, 2-Aranha, 3-Escorpião, 4-Lagarta, 5-Abelha, 6-Outros), tipo de serpente (botrópico, crotálico, elapídico, laquético e não peçonhenta); aranha (foneutrismo, loxoscelismo, latrodectismo, outra); manifestações locais e sistêmicas, tempo de coagulação e soroterapia — o caso confirmado é definido por evidências clínicas de envenenamento, independentemente da identificação do animal. A unidade de análise é o acidente notificado individualmente (não o atendimento de soroterapia em si, registrado na internação).

A série de 2007 em diante coincide com a expansão da notificação obrigatória e do conhecimento (decada 2007 unluvutitlus): os acidentes explosivos nos anos 2010-2020 em zoneamento urbano — escorpões (*Tityus serrulatus* sinte e tipo presente) — são mais notados emuther Télba-água municípios das regiões Sudeste e Norte; no ambiente rural, as serpentes ainda predominam em trabalhador rural (CBO grandes grupos agropastoris). O OGMB/SINAN foi crescentamente e a base espaço-temporal é sólida para séries de acidentes.

Aplicações analíticas: coeficiente de incidência por 100 mil habitantes, letalidade específica por tipo de acidente (escorpionismo, ofidismo, araneismo e lonomismo), distribuição por parte do corpo picada (local da picada), tempo decorrido picada/atendimento (qualidade da assistência), uso de soroterapia (soro antibotrópico/anticrotálico/antielapídico/antilonômico) e vigilância ocupacional (fichas com campo de relação com trabalho).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ANIM` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ANIM` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `ANIMBR07.dbc` — prefixo `ANIM`, `BR` (consolidação nacional) e `07` (ano 2007), até `ANIMBR22.dbc` (2022); os anos recentes ficam em `PRELIM` (ex.: `ANIMBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-anim/<ano>/sinan-anim_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-anim/2022/sinan-anim_2022-br@20260921.dbc`; arquivos preliminares recebem o sufixo `-preliminar`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Acidente por animais peçonhentos — CID-10 X20-X29) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_ACID` | Data (`AAAAMMDD`) | Data do acidente (campo específico da ficha) |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_RACA` | Inteiro | Raça/cor (1-Branca ... 5-Indígena, 9-Ignorado) |
| `ID_OCUPA_C` | String (6) | Ocupação do paciente, código CBO (trabalhador rural predominante) |
| `DOENCA_TRA` | Inteiro | Relação do acidente com o trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `CLASSI_FIN` | Inteiro | Classificação final do caso (conforme dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (conforme dicionário; acidente é estruturalmente clínico) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito por acidente, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: manter `ID_MUNICIP`, `ID_MN_RESI` (IBGE 6/7 dígitos), `ID_UNIDADE` (CNES) e `ID_OCUPA_C` (CBO) como texto com `zfill`; códigos de tipo de acidente (serpente/aranha/escorpião/lagarta/abelha), gênero da serpente/aranha, tipo de aranha e gravidade devem ser mapeados como categóricos apenas depois do saneamento.
- **Datas e competências**: `DT_NOTIF`, `DT_ACID`, `DT_OBITO` e `DT_ENCERRA` em `AAAAMMDD` convertidos para `pl.Date`; semanas epidemiológicas permanecem inteiras.
- **Valores ausentes e sentinelas**: células em branco, datas `00000000`, códigos ignorados `9`/`99` (ex.: local de picada `99 - Ignorado`) e `999999` normalizados para nulo por `SENTINEL_NULLS`; registros com marcador dBASE de exclusão (`_deleted`) removidos.
- **Particularidades do dataset**: volume enorme (20 consolidações anuais com ~207 MB) e sazonalidade de pico em estações quentes; o tipo de acidente e o gênero da serpente/aranha podem ficar em branco quando o animal não é identificado — não tratar blank como "outros"; município de residência vs. município de ocorrência do acidente podem divergir (campos específicos da ficha registram UF/localidade de ocorrência); acidentes de trabalho exigem o cruzamento de `DOENCA_TRA` com `ID_OCUPA_C`, como fazem as análises oficiais do Boletim Epidemiológico da SVSA.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-anim
quantilica datasus list sinan-anim

# 2. Baixar microdados de sinan-anim com recorte adequado à partição do dataset
quantilica datasus sync sinan-anim -o ./data --start 2010 --end 2022 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-anim -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-anim -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de acidentes por animais peçonhentos já tratado
qdf = read_dbc("data/sinan-anim/2022/sinan-anim_2022-br@20260921.dbc", clean=True)

# Volume de acidentes por ano e UF
print(
    qdf.group_by("nu_ano", "sg_uf_not")
    .len()
    .sort(["nu_ano", "sg_uf_not"])
)

# Proporção de acidentes relacionados ao trabalho
print(
    qdf.group_by("doenca_tra")
    .len()
    .sort("len", descending=True)
)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Acidente por Animais Peçonhentos (ficha e instrucional)**: https://portalsinan.saude.gov.br/acidente-por-animais-peconhentos
- **Ficha de Investigação Acidentes por Animais Peçonhentos (Animais_Peconhentos_v5)**: http://portalsinan.saude.gov.br/images/documentos/Agravos/AAP/Animais_Peconhentos_v5.pdf
- **Boletim Epidemiológico SVSA — acidentes por animais peçonhentos**: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/a/animais-peconhentos
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo peçonhentos
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
