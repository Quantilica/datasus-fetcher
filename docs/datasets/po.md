# `po` — Painel de Oncologia

O `po` contém os registros do **Painel de Oncologia**, que reúne informações sobre **diagnóstico e tratamento de câncer** no Brasil a partir de dados do SIA/SUS, SIH/SUS e do Sistema de Informação do Câncer (SISCAN). Cada registro (linha) representa um **caso** em que houve realização de **procedimento diagnóstico e/ou terapêutico oncológico**, com dados de residência e de atendimento, datas de diagnóstico e de tratamento, sexo, idade ao diagnóstico e estadiamento. É a principal base de acesso público para análise da atenção oncológica no SUS.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `po` — PO: Painel de Oncologia |
| **Código no `datasus-fetcher`** | `po` |
| **Formato dos arquivos** | `.dbc` (compactado do DBF) |
| **Particionamento** | `uf`, `year` (na prática um único arquivo nacional `BR` por ano) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2013 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 14 arquivos (~194 MB; cobertura apenas nacional `BR`) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/PAINEL_ONCOLOGIA/DOC` (`Dicionario_Painel_Oncologia.txt`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/PAINEL_ONCOLOGIA/AUXILIAR` (`PAINEL_ONCOLOGIA.zip`, `tab_*.zip`) |

## 1. Contexto Institucional e Epidemiológico

O Painel de Oncologia é mantido pelo **Ministério da Saúde/DATASUS** em parceria com o **Instituto Nacional de Câncer (INCA)** e integra as informações de diagnóstico e tratamento oncológicos do SUS. Sua criação responde à necessidade de monitorar a linha do cuidado do câncer — do diagnóstico ao tratamento — usando os registros administrativos de procedimentos (SIA/SUS, SIH/SUS) e os dados do SISCAN.

O **evento gerador** é a **realização de procedimento oncológico** — exame diagnóstico (APAC de diagnóstico), tratamento (quimioterapia, radioterapia, cirurgia oncológica) ou confirmação anatomopatológica. A **unidade de análise é o caso/procedimento oncológico**, identificado pelos campos `ano_diagn`, `anomes_dia` (competência do diagnóstico), `ano_tratam`, `anomes_tra` (competência do tratamento), `uf_resid`/`mun_resid` (residência), `uf_tratam`/`mun_tratam` (estabelecimento de tratamento), `uf_diagn`/`mun_diag` (estabelecimento de diagnóstico), `tratamento`, `diagnostic`, `idade`, `sexo`, `estadiam` (estadiamento), `cnes_diag`/`cnes_trat` (estabelecimentos), `tempo_trat` (tempo até o tratamento), `cns_pac`, `diag_deth`, `dt_diag`, `dt_trat` e `dt_nasc`.

Os arquivos são anuais e **nacionais** (prefixo `POBR` + ano de 4 dígitos, ex.: `POBR2013.dbc` … `POBR2026.dbc`), com cerca de 194 MB no total e 14 arquivos. Não há quebra por UF no FTP — o particionamento é apenas por ano, com um único "uf" (`BR`). Não há diretório preliminar.

Aplicações analíticas típicas: avaliação do acesso e do tempo entre diagnóstico e tratamento, análise de estadiamento ao diagnóstico, distribuição de casos por sexo, idade e localização, comparação entre local de residência e local de tratamento (fluxos/deslocamento), planejamento de redes de atenção oncológica e monitoramento de políticas de controle do câncer.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/PAINEL_ONCOLOGIA/DADOS` | `PO` | UF + AAAA (ex.: `BR2013`, `BR2026`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `POBR2013.dbc` — `PO` é o prefixo, `BR` a cobertura nacional e `2013` o ano de quatro dígitos. Existem arquivos de 2013 a 2026, sempre nacionais (não há arquivos por UF).
- **No armazenamento local do `datasus-fetcher`**: `data/po/2024/po_2024-br@20251120.dbc` (partição por ano, uf=`br`).
- **Documentação e Tabelas Auxiliares associadas**: em `PAINEL_ONCOLOGIA/DOC` está `Dicionario_Painel_Oncologia.txt` (dicionário de variáveis); em `PAINEL_ONCOLOGIA/AUXILIAR` estão `PAINEL_ONCOLOGIA.zip` e `tab_*.zip`, com definições e conversões (CID, procedimento, município, UF) para tabulação no TabWin.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `ano_diagn` / `anomes_dia` | Inteiro | Ano e competência (AAAAMM) do diagnóstico |
| `ano_tratam` / `anomes_tra` | Inteiro | Ano e competência (AAAAMM) do tratamento |
| `uf_resid` / `mun_resid` | String | UF e município de residência do paciente |
| `uf_diagn` / `mun_diag` | String | UF e município do estabelecimento de diagnóstico |
| `uf_tratam` / `mun_tratam` | String | UF e município do estabelecimento de tratamento |
| `tratamento` | String | Código do procedimento de tratamento oncológico |
| `diagnostic` | String | Código do procedimento diagnóstico |
| `idade` | Inteiro | Idade (ao diagnóstico) |
| `sexo` | String | Sexo do paciente |
| `estadiam` | String | Estadiamento (extensão da doença ao diagnóstico) |
| `cnes_diag` / `cnes_trat` | String | CNES dos estabelecimentos de diagnóstico/tratamento |
| `tempo_trat` | Inteiro | Tempo decorrido entre diagnóstico e tratamento |
| `cns_pac` | String | Cartão Nacional de Saúde do paciente |
| `diag_deth` | String | Diagnóstico de óbito (quando aplicável) |
| `dt_diag` / `dt_trat` / `dt_nasc` | Data | Datas de diagnóstico, tratamento e nascimento |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `mun_resid`, `mun_diag`, `mun_tratam` (código de município) e `cnes_*`, `cns_pac`, `uf_*` devem permanecer `String` — códigos com zeros à esquerda seriam corrompidos se convertidos a número.
- **Datas e competências**: os campos `anomes_dia`/`anomes_tra` são competências `AAAAMM`; as datas plenas (`dt_diag`, `dt_trat`, `dt_nasc`) são `AAAAMMDD`; a rotina de datas aplica-se às segundas, não às competências.
- **Valores ausentes e sentinelas**: `estadiam`, `diag_deth`, `tempo_trat` e datas podem vir vazios/ignorados; campos ignorados do DATASUS devem ser tratados como ausentes.
- **Particularidades do dataset**: é uma base de **casos agregados por procedimento**, não um registro clínico completo; um mesmo paciente pode aparecer em múltiplos registros (diagnóstico e tratamento); a identificação usa `cns_pac` (atenção à privacidade e ao pareamento); `tempo_trat` pode ser negativo/inconsistente quando o tratamento precede o registro de diagnóstico; a base é nacional e grande (requer processamento por ano); e há quebras de cobertura/atualização entre anos, recomendando verificar o `index.json` antes de séries longas.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para po
quantilica datasus list po

# 2. Baixar microdados com recorte de anos (partição apenas por ano; uf = br)
quantilica datasus sync po -o ./data --start 2015 --end 2024

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync po -o ./data --docs --aux --start 2015 --end 2024

# 4. Pipeline completo: download, descompactação do .dbc e conversão para Parquet
quantilica datasus pipeline po -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2024
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

po = read_dbc("data/raw/po/2024/po_2024-br.dbc", clean=True)

# Casos por sexo em 2024
casos = po.group_by("sexo").agg(pl.len().alias("casos")).sort("casos", descending=True)
print(casos)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/PAINEL_ONCOLOGIA/DADOS`
- **Painel de Oncologia (DATASUS)**: https://datasus.saude.gov.br/painel-oncologia/
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **INCA — Instituto Nacional de Câncer**: https://www.gov.br/inca/pt-br
- **Dicionário `Dicionario_Painel_Oncologia.txt`** e pacote `PAINEL_ONCOLOGIA.zip` no FTP DATASUS
- **SISCAN — Sistema de Informação do Câncer**: https://www.gov.br/inca/pt-br
