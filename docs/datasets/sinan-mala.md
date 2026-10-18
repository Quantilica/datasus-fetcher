# `sinan-mala` — Malária

O `sinan-mala` contém os microdados das notificações e investigações de casos de Malária (CID-10 B50-B54) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de malária digitado no SINAN Net/Sinan Online. Importante: a base SINAN cobre primordialmente a malária extra-amazônica, pois os casos das unidades federadas da Amazônia Legal são registrados no SIVEP-Malária — o SINAN observa o padrão de vigilância fora dessa região.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-mala` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 2004 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 23 arquivos (~2,9 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A malária é uma doença parasitária causada por plasmódios (*Plasmodium falciparum*, *P. vivax*, *P. malariae* e, mais recentemente, *P. knowlesi*), transmitida pela picada do mosquito *Anopheles* e considerada doença prioritária do cenário de eliminação nacional. A vigilância é híbrida: a Portaria SVS/MS nº 104/2011 (hoje consubstanciada na Portaria de Consolidação GM/MS nº 204/2016) determinou que os casos de malária na Região da Amazônia Legal (Acre, Amapá, Amazonas, Maranhão, Mato Grosso, Pará, Rondônia, Roraima e Tocantins) sejam registrados no **SIVEP-Malária**, enquanto a malária **extra-amazônica** deve ser notificada no **SINAN**. O FTP do DATASUS, no entanto, divulga a consolidação nacional `BR` da base SINAN, que concentra sobretudo a malária registrada fora da Amazônia Legal, além de remanescentes de notificação polinomiais da série histórica.

O evento gerador neste dataset é a **Ficha de Notificação/Investigação de Malária do SINAN** (ficha `Malaria_v5`). A unidade de análise é o caso suspeito/confirmado notificado individualmente, com confirmação por exame do tipo de plasmódio (gota espessa/lâmina delgada ou teste rápido TDR) registrada na investigação. A notificação é compulsória em todo o território nacional mediante confirmação, com o caso classificado por espécie infectante.

Aplicações analíticas: coeficiente parasitário anual (casos confirmados por 10 mil habitantes) especialmente em territórios extra-amazônicos, distribuição por espécie infectante, vigilância de casos importados/viajantes e de reintroduções em áreas de fronteira, letalidade da *P. falciparum*, e análises de integração com a base do SIVEP-Malária.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `MALA` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `MALA` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `MALABR04.dbc` — prefixo `MALA`, `BR` (consolidação nacional) e `04` (ano 2004, primeiro ano da série do SINAN no FTP); a série de arquivos finais vai até `MALABR23.dbc` (2023), com os anos recentes em `PRELIM` (ex.: `MALABR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-mala/<ano>/sinan-mala_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-mala/2023/sinan-mala_2023-br@20260831.dbc`; o dataset também mantém a variante `-preliminar` para os arquivos do `PRELIM`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/descompactação/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Malária — CID-10 B50-B54) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (8-30 dias antes do exame) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_RACA` | Inteiro | Raça/cor (1-Branca, 2-Preta, 3-Amarela, 4-Parda, 5-Indígena, 9-Ignorado) |
| `ID_OCUPA_C` | String (6) | Ocupação do paciente, código CBO (relevante para exposição ocupacional em áreas florestais e rurais) |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `CLASSI_FIN` | Inteiro | Classificação final: 1 - Confirmado (quando o resultado do exame ≠ negativo), 2 - Descartado (exame negativo), 8 - Inconclusivo |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Abandono, 3 - Óbito pelo agravo, 4 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: manter `ID_MUNICIP`, `ID_MN_RESI` (IBGE 6/7 dígitos), `ID_UNIDADE` (CNES) e `ID_OCUPA_C` (CBO) como `String` com `zfill`; códigos de classificação final, critério e evolução permanecem categóricos apenas após mapeamento.
- **Datas e competências**: `DT_NOTIF`, `DT_SIN_PRI`, `DT_INVEST`, `DT_OBITO` e `DT_ENCERRA` em `AAAAMMDD` convertidos para `pl.Date`; semanas epidemiológicas (`SEM_NOT`, `SEM_PRI`) como `Int64`.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`, `999999`), datas `00000000` e strings em branco normalizados para nulo por `SENTINEL_NULLS`; registros com marcador de exclusão dBASE (`_deleted`) descartados.
- **Particularidades do dataset**: como os registros estão em arquivos consolidados `BR` anuais, o volume é pequeno (23 arquivos, ~2,9 MB), pois a malária da Amazônia Legal está majoritariamente registrada no SIVEP-Malária em vez do SINAN — a base SINAN subestima a carga total nacional de malária, devendo ser combinada com o SIVEP para séries completas; os arquivos dos anos recentes em `PRELIM` ainda são sujeitos a revisão.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-mala
quantilica datasus list sinan-mala

# 2. Baixar microdados de sinan-mala com recorte adequado à partição do dataset
quantilica datasus sync sinan-mala -o ./data --start 2004 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-mala -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-mala -o ./data/raw --parquet-dir ./data/parquet --start 2004
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de malária (casos SINAN, visão extra-amazônica)
qdf = read_dbc("data/sinan-mala/2023/sinan-mala_2023-br@20260831.dbc", clean=True)

# Casos confirmados por ano e UF
print(
    qdf.filter(pl.col("classi_fin") == 1)
    .group_by("nu_ano", "sg_uf_not")
    .len()
    .sort(["nu_ano", "sg_uf_not"])
)

# Casos confirmados por município de residência, para vigilância extra-amazônica
print(
    qdf.filter(pl.col("classi_fin") == 1)
    .group_by("id_mn_resi")
    .len()
    .sort("len", descending=True)
)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Malária (ficha/procedimentos)**: https://portalsinan.saude.gov.br/malaria
- **Ficha de Investigação Malária SINAN NET**: http://portalsinan.saude.gov.br/images/documentos/Agravos/Malaria/Malaria_v5.pdf
- **SIVEP-Malária (Amazônia Legal)**: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/m/sivep-malaria
- **Portaria SVS/MS nº 104/2011** e **Portaria GM/MS nº 204/2016** (notificação compulsória)
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
