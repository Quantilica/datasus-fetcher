# `sinan-ltan` — Leishmaniose Tegumentar Americana

O `sinan-ltan` contém os microdados das notificações e investigações de casos de Leishmaniose Tegumentar Americana (LTA, CID-10 B55.1) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de LTA — formas cutânea, mucocutânea e disseminada — digitado no SINAN Net/Sinan Online pelos serviços de saúde. A LTA é de notificação compulsória em todo o país e constitui a base oficial para monitorar a incidência, a distribuição e o desfecho dos casos humanos.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-ltan` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 2000 a 2025 (conforme `index.json`) |
| **Volume aproximado no FTP** | 26 arquivos (~38,8 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A leishmaniose tegumentar americana é uma zoonose parasitária causada por espécies do complexo *Leishmania (Viannia) braziliensis* e afins, transmitida por flebotomíneos (popularmente "mosquito palha") com ampla gama de reservatórios silvestres. A vigilância é coordenada pela SVSA/MS, por meio do Programa de Vigilância e Controle da Leishmaniose Tegumentar, cuja ficha de investigação é revisada periodicamente. A notificação é compulsória de acordo com a Portaria SVS/MS nº 104/2011 (consolidação da Portaria GM/MS nº 204/2016), de forma individual para casos humanos confirmados e suspeitos.

O evento gerador é a **Ficha de Investigação da Leishmaniose Tegumentar Americana** do SINAN (ficha `LTA_v5`, com dicionário próprio), preenchida no caso suspeito — lesão cutânea ulcerada ou mucosa com tempo de evolução compatível e exposição em áreas de transmissão — e completada com exames parasitológicos (raspado/escarificação para amastigotas), intradermorreação de Montenegro e diagnóstico sorológico/molecular conforme disponibilidade. A unidade de análise é o caso notificado individual.

Marcos normativos e de leiaute: a ficha vigente data da revisão de 2006 e flui pelo SINAN Net (2007+) e Sinan Online (2014+), com dicionário de dados LTA próprio. A classificação final variou ao longo do tempo entre formas clínicas (cutânea, mucocutânea, cutânea difusa/disseminada). O registro histórico concentra-se em áreas rurais endêmicas (Amazônia Legal, Centro-Oeste e Nordeste), mas a expansão periurbana, os ecoturismos e o lazer em áreas endêmicas prescrevem vigilância permanente, particularmente em trabalhadores rurais (floresta, agropecuária, extrativismo).

Aplicações analíticas: coeficiente de detecção anual por 100 mil habitantes, distribuição por forma clínica, proporção de casos com comprometimento mucoso (maior gravidade), perfil ocupacional via CBO, acompanhamento de abandono de tratamento (possível dado da coluna `evolucao`) e mapeamento de recrudescentes endêmicos.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `LTAN` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `LTAN` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `LTANBR00.dbc` — prefixo `LTAN`, `BR` (consolidação nacional) e `00` (ano 2000, início da série disponível), até `LTANBR25.dbc` (2025). Não há arquivo em `PRELIM` para o `sinan-ltan` no inventário atual.
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-ltan/<ano>/sinan-ltan_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-ltan/2025/sinan-ltan_2025-br@20260914.dbc`; arquivos preliminares, quando publicados, recebem o sufixo `-preliminar`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (LTA — CID-10 B55.1) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (lesão cutânea/mucosa) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) — forte predominância de homens em áreas ocupacionais |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_RACA` | Inteiro | Raça/cor (1-Branca ... 5-Indígena, 9-Ignorado) |
| `ID_OCUPA_C` | String (6) | Ocupação do paciente, código CBO (trabalhadores rurais predominantes) |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `CLASSI_FIN` | Inteiro | Classificação final (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Abandono, 3 - Óbito por LTA, 4 - Óbito por outras causas, 5 - Transferência, 6 - Mudança de diagnóstico) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: manter `ID_MUNICIP`, `ID_MN_RESI` (IBGE 6/7 dígitos), `ID_UNIDADE` (CNES) e `ID_OCUPA_C` (CBO) como texto com `zfill`; `CLASSI_FIN`/`CRITERIO`/`EVOLUCAO` só devem ser convertidos em categóricos após o mapeamento de rótulos.
- **Datas e competências**: `DT_NOTIF`, `DT_SIN_PRI`, `DT_INVEST`, `DT_OBITO` e `DT_ENCERRA` são datas `AAAAMMDD` convertidas para `pl.Date`; semanas (`SEM_NOT`, `SEM_PRI`) ficam como `Int64`.
- **Valores ausentes e sentinelas**: células em branco, datas `00000000`, códigos ignorados e RQ (`999999`/`99999999`) normalizados para nulo por `SENTINEL_NULLS`; registros com marcador lógico de exclusão dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: a completude dos resultados laboratoriais é frequentemente insuficiente — boa parte dos casos é confirmado por critério clínico-epidemiológico (`CRITERIO = 2`); volume considerável por ano (~38,8 MB em 26 consolidações), pois a LTA é endêmica em dezenas de países municipais, sobretudo no Norte e Centro-Oeste; a ausência de arquivos `PRELIM` no inventário atual para este agravo (ver `quantilica datasus list sinan-ltan`) recomenda o uso dos FINAIS como fonte principal.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-ltan
quantilica datasus list sinan-ltan

# 2. Baixar microdados de sinan-ltan com recorte adequado à partição do dataset
quantilica datasus sync sinan-ltan -o ./data --start 2000 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-ltan -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-ltan -o ./data/raw --parquet-dir ./data/parquet --start 2000
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de LTA já tratado
qdf = read_dbc("data/sinan-ltan/2025/sinan-ltan_2025-br@20260914.dbc", clean=True)

# Casos confirmados por ano e UF
confirmados = qdf.filter(pl.col("classi_fin") == 1)
print(
    confirmados.group_by("nu_ano", "sg_uf_not")
    .len()
    .sort(["nu_ano", "sg_uf_not"])
)

# Perfil de critério de confirmação (laboratorial ou clínico-epidemiológico)
print(
    confirmados.group_by("criterio")
    .len()
    .sort("len", descending=True)
)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Leishmaniose Tegumentar Americana**: https://portalsinan.saude.gov.br/leishmaniose-tegumentar-americana
- **Dicionário de Dados LTA v5 (SINAN NET)**: http://portalsinan.saude.gov.br/images/documentos/Agravos/Leishmaniose%20Tegumentar%20Americana/DIC_DADOS_LTA_v5.pdf
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo Leishmanioses
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
