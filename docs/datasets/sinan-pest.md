# `sinan-pest` — Peste

O `sinan-pest` contém os microdados das notificações e investigações de casos de Peste (CID-10 A20) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de peste humana (formas bubônica, pulmonar ou septicêmica), digitado no SINAN Net/Sinan Online. A peste é de notificação compulsória imediata e permanece na lista nacional por sua relevância histórica e pelo risco de reativação nos bolsões naturais de roedores silvestres — especialmente os focos do semiárido nordestino.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-pest` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2025 (conforme `index.json`) |
| **Volume aproximado no FTP** | 19 arquivos (~42 kB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A peste é uma zoonose infecciosa causada pela bactéria *Yersinia pestis*, transmitida ao homem por pulgas de roedores. No Brasil, persiste a vigilância da peste nos focos naturais consolidados pela literatura técnica: planalto da Borborema (Paraíba, Pernambuco e Alagoas), serra da Ibiapaba e Chapada do Araripe (Ceará), credo do Sudoeste da Bahia e planaltos do Piauí/Pernambuco. Nestes ecossistemas, roedores silvestres e comensais infectados e suas pulgas mantêm o potencial de reativação, ainda que casos humanos confirmados sejam raríssimos nas últimas décadas. A vigilância é da SVSA/MS, com o agravo constando da lista de notificação compulsória imediata da Portaria SVS/MS nº 5/2006 e da consolidação vigente (Portaria GM/MS nº 204/2016).

O evento gerador é a **Ficha de Investigação da Peste** do SINAN (ficha `Peste_v5`), preenchida diante do caso suspeito — pessoa com febre aguda acompanhada de linfadenopatia dolorosa (bubão), pneumonia grave com insuficiência respiratória rápida ou septicemia, com vínculo epidemiológico com área de foco — e concluída com exames laboratoriais (coloração de esfregaço/bisnaga, cultivo, serologia anti-F1 e PCR conforme disponibilidade) e o desfecho. A unidade de análise é o caso suspeito/confirmado individual, em número muito pequeno no Brasil (a base publica poucas notificações por ano).

Marcos do sistema: a ficha v5 data do período SINAN Net (2005-2006) e a vigilância integra o monitoramento de roedores e pulgas nos focos, além da notificação negativa anual dos municípios dos bolsões. Como o volume de casos humanos é mínimo, a base praticamente registra investigações de casos suspeitos, mantidas para assegurar a continuidade do estado de vigilância da peste no país.

Aplicações analíticas: monitoramento da endemicidade e da reativação nos bolsões naturais, descrição de casos confirmados (formas clínicas, letalidade), e verificação da operacionalidade da notificação negativa nos municípios sob vigilância.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `PEST` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `PEST` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `PESTBR07.dbc` — prefixo `PEST`, `BR` (consolidação nacional) e `07` (ano 2007), até `PESTBR24.dbc` (2024); o arquivo do ano corrente fica em `PRELIM` (ex.: `PESTBR25.dbc`). A série é minúscula: ~42 kB no total, refletindo poucas notificações.
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-pest/<ano>/sinan-pest_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-pest/2024/sinan-pest_2024-br@20260212.dbc`; arquivos preliminares recebem o sufixo `-preliminar`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Peste — CID-10 A20) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave; compulsória imediata) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `CLASSI_FIN` | Inteiro | Classificação final (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: manter `ID_MUNICIP`, `ID_MN_RESI` (IBGE 6/7 dígitos) e `ID_UNIDADE` (CNES) como `String` com `zfill`; códigos de classificação final, critério e evolução convertidos apenas após mapeamento de rótulos.
- **Datas e competências**: `DT_NOTIF`, `DT_SIN_PRI`, `DT_INVEST`, `DT_OBITO` e `DT_ENCERRA` em `AAAAMMDD` convertidos para `pl.Date`; semanas epidemiológicas permanecem inteiras.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`, `999999`), datas `00000000` e strings em branco normalizados para nulo por `SENTINEL_NULLS`; registros com marcador de exclusão dBASE (`_deleted`) descartados.
- **Particularidades do dataset**: volume minúsculo (~42 kB em 19 consolidações) — quase todas as fichas correspondem a casos investigados nos bolsões; maior parte das fichas corresponde a casos descartados e poucos confirmados; atenção ao município provável de infecção ao usar as colunas de residência, pois a exposição de campo pode ocorrer em município diverso do de notificação.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-pest
quantilica datasus list sinan-pest

# 2. Baixar microdados de sinan-pest com recorte adequado à partição do dataset
quantilica datasus sync sinan-pest -o ./data --start 2007 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-pest -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-pest -o ./data/raw --parquet-dir ./data/parquet --start 2007
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# A base de peste é pequena; abaixo, uma leitura consolidada com polars
qdf = read_dbc("data/sinan-pest/2024/sinan-pest_2024-br@20260212.dbc", clean=True)

# Distribuição dos casos por classificação final e ano
print(qdf.group_by("nu_ano", "classi_fin").len().sort(["nu_ano", "classi_fin"]))

# UF de notificação dos casos registrados
print(qdf.group_by("sg_uf_not").len().sort("len", descending=True))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Peste**: https://portalsinan.saude.gov.br/peste
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo Peste
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
