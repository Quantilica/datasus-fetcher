# `sinan-hant` — Hantavirose

O `sinan-hant` contém os microdados das notificações e investigações de casos de Hantavirose (principalmente a síndrome cardiopulmonar por hantavírus, CID-10 B33.4) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de hantavirose, digitado no SINAN Net/Sinan Online. O agravo é de notificação compulsória imediata (até 24 horas) por tratar-se de zoonose grave, de alta letalidade e com potencial de surto, por exemplo em roedores silvestres.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-hant` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 1999 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 28 arquivos (~2,3 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A hantavirose brasileira é causada por hantavirus (Orthohantavirus da família Hantaviridae) mantidos por roedores silvestres das famílias Cricetidae (ex.: *Oligoryzomys nigripes*, *O. flavescens*, *Necromys lasiurus* — principais, com variantes regionais Araraquara, Juquitiba, Castelo dos Sonhos e Laguna Negra). A transmissão humana dá-se por inalação de aerossóis de urina, fezes e saliva de roedores infectados, tipicamente em ambientes rurais e florestais. A vigilância é da SVSA/MS; a doença é de notificação compulsória imediata desde a Portaria SVS/MS nº 5/2006 e está na LNC consolidada (Portaria GM/MS nº 204/2016). A forma mais comum no Brasil é a síndrome cardiopulmonar por hantavírus (SCPH), grave, em pacientes jovens, com letalidade historicamente em torno de 40%.

O evento gerador é a **Ficha de Investigação de Hantavirose** do SINAN (ficha `Hantavirose_v5`, de 19/05/2006, com instrucional e dicionário de dados próprios), preenchida no caso suspeito e completada com exames sorológicos — IgM (imunofluorescência), imunohistoquímica (em material de necropsia) e RT-PCR — e com a investigação do local provável de infecção (LPI). A unidade de análise é o caso suspeito/confirmado individual.

A literatura documenta três versões de ficha na série histórica (1996-2000 SINAN-DOS, 2001-2006 SINAN-Windows, 2007+ SINAN NET), o que introduz quebras de leiaute nos campos específicos. No FTP, a série de arquivos finais disponíveis inicia em 1999 e casos notificados concentram-se em biomas de Cerrado, Mata Atlântica e Pampa (Minas Gerais, São Paulo, Mato Grosso, Paraná, Santa Catarina, Rio Grande do Sul e oeste do Espírito Santo).

Aplicações analíticas: coeficiente de incidência e letalidade anual, distribuição geográfica pelo local provável de infecção (campo LPI), proporção de casos confirmados entre notificados (a maior parte descartada — relevância da qualidade de triagem), resultados de métodos laboratoriais (IgM, imunohistoquímica, RT-PCR), e vigilância de trabalhadores rurais e atividades de risco (colheitas, desmatamento, armazenamento de grãos).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `HANT` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `HANT` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `HANTBR99.dbc` — prefixo `HANT`, `BR` (consolidação nacional) e `99` (ano 1999), até `HANTBR24.dbc` (2024); os anos recentes aparecem em `PRELIM` (ex.: `HANTBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-hant/<ano>/sinan-hant_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-hant/2024/sinan-hant_2024-br@20260515.dbc`; arquivos preliminares recebem o sufixo `-preliminar`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Hantavirose — CID-10 B33.4) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave; notificação imediata) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data do início dos sintomas (síndrome febril, mialgia, dispnéia) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `LPI` | String | Local provável de infecção (município/UF onde ocorreu a exposição) — campo essencial da ficha de hantavirose |
| `CLASSI_FIN` | Inteiro | Classificação final (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: manter `ID_MUNICIP`, `ID_MN_RESI`, `ID_UNIDADE` (IBGE 6/7 e CNES) e campos do local provável de infecção como texto com `zfill`; códigos de classificação final/critério/evolução só permitem mapeamento categórico explícito.
- **Datas e competências**: `DT_NOTIF`, `DT_SIN_PRI`, `DT_INVEST`, `DT_OBITO` e `DT_ENCERRA` em `AAAAMMDD` convertidas para `pl.Date`; semanas epidemiológicas permanecem inteiras.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`, `999999`), datas `00000000`, strings em branco e `99999999` normalizados para nulo por `SENTINEL_NULLS`; registros com marcador lógico de exclusão dBASE (`_deleted`) removidos.
- **Particularidades do dataset**: grande proporção de notificações descartadas (o agravo exige exclusão de outras causas de insuficiência respiratória aguda); o campo do local provável de infecção (LPI) tem alto índice de incompletude, e as vigilâncias estaduais costumam reconstruir a LPI para assegurar a distinção entre residência e exposição; há três versões de ficha históricas (leiautes distintos por período) e os casos anuais em consolidações `BR` são poucos (total ~2,3 MB em 28 arquivos), exigindo cautela no cálculo de coeficientes.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-hant
quantilica datasus list sinan-hant

# 2. Baixar microdados de sinan-hant com recorte adequado à partição do dataset
quantilica datasus sync sinan-hant -o ./data --start 2007 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-hant -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-hant -o ./data/raw --parquet-dir ./data/parquet --start 2007
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de hantavirose já tratado
qdf = read_dbc("data/sinan-hant/2024/sinan-hant_2024-br@20260515.dbc", clean=True)

# Proporção de casos confirmados entre notificados, por ano
print(
    qdf.group_by("nu_ano")
    .agg(
        notificados=pl.len(),
        confirmados=(pl.col("classi_fin") == 1).sum(),
    )
    .sort("nu_ano")
    .with_columns(
        (pl.col("confirmados") / pl.col("notificados")).alias("prop_confirm")
    )
)

# Letalidade entre casos confirmados
confirmados = qdf.filter(pl.col("classi_fin") == 1)
print(
    confirmados.group_by("nu_ano")
    .agg(
        casos=pl.len(),
        obitos=(pl.col("evolucao") == 2).sum(),
    )
    .sort("nu_ano")
)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Hantavirose (ficha, instrucional e dicionário)**: https://portalsinan.saude.gov.br/hantavirose
- **Instrucional da ficha de hantavirose SINAN NET**: http://portalsinan.saude.gov.br/images/documentos/Agravos/Hantavirose/Hantavirose_v5_instr.pdf
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo Hantavirose
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
