# `resp` — Notificações de casos suspeitos de SCZ

O `resp` contém as **notificações de casos suspeitos de Síndrome Congênita associada à infecção pelo vírus Zika (SCZ)**, incluindo microcefalia e outras alterações do sistema nervoso central, registradas no sistema **RESP (Registro de Eventos em Saúde Pública)**. Cada registro (linha) é uma **notificação individual** de um caso suspeito, com dados de notificação, residência, dados clínicos e de investigação laboratorial. É a base usada pelo Ministério da Saúde no monitoramento da emergência de saúde pública de 2015-2016 e nas análises de desfechos congênitos associados ao Zika.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `resp` — RESP: Notificações de casos suspeitos de SCZ |
| **Código no `datasus-fetcher`** | `resp` |
| **Formato dos arquivos** | `.dbc` (compactado do DBF) |
| **Particionamento** | `uf`, `year` (um arquivo por UF e ano) |
| **Periodicidade** | Anual (competências consolidadas por ano) |
| **Cobertura temporal no FTP** | 2015 a 2024 (conforme `index.json`; 28 UFs com dados) |
| **Volume aproximado no FTP** | 280 arquivos (~3,4 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/RESP/DOCS` (`DIC_DADOS_RESP.txt`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/RESP/AUXILIAR` (`tabresp.zip`) |

## 1. Contexto Institucional e Epidemiológico

Em resposta à **emergência de saúde pública** deflagrada a partir de 2015, quando se observou o aumento de casos de microcefalia e alterações do sistema nervoso central possivelmente associados à infecção pelo vírus Zika durante a gestação, o Ministério da Saúde implantou um **registro específico de notificação** — o sistema **RESP** — para captar os casos suspeitos de **Síndrome Congênita associada ao Zika (SCZ)**. O sistema complementa os instrumentos do SINAN para essa condição.

O **evento gerador** é a **notificação de um caso suspeito de SCZ/microcefalia** por uma unidade de saúde. A **unidade de análise é a notificação individual**, com os campos típicos de notificação (`TP_NOT`, `ID_AGRAVO`, `DT_NOTIFIC`, `SEM_NOT`, `NU_ANO`, `SG_UF_NOT`, `ID_MUNICIP`, `ID_REGIONA`, `ID_UNIDADE`), dados da mãe e da gestação (`CS_GESTANT`, `NU_IDADE_N`, `CS_SEXO`, `CS_RACA`, `CS_ESCOL_N`), residência (`SG_UF`, `ID_MN_RESI`, `ID_RG_RESI`), dados clínicos e de investigação (classificação final, critério de confirmação/descarte, resultados de exames e evolução), além de datas como `DT_SIN_PRI` (primeiros sintomas) e `DT_INVEST` (investigação).

Os dados são organizados por UF e ano (prefixo `RESP` + UF + dois dígitos do ano, ex.: `RESPAC15.dbc`) e cobrem 2015 a 2024. Apenas UFs com notificações aparecem (28 UFs). Não há diretório preliminar.

Aplicações analíticas típicas: monitoramento temporal e espacial da SCZ, cálculo de prevalência/incidência de microcefalia, análise de desfechos gestacionais, avaliação da completude e da qualidade da notificação, investigação de associação com arboviroses e avaliação da resposta à emergência.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/RESP/DADOS` | `RESP` | UF + AA (ex.: `AC15`, `SP16`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `RESPAC15.dbc` — `RESP` é o prefixo, `AC` a UF e `15` o ano (2015). Há um `.dbc` por UF e ano, de 2015 a 2024.
- **No armazenamento local do `datasus-fetcher`**: `data/resp/2024/resp_2024-sp@20251029.dbc` (partição por UF e ano).
- **Documentação e Tabelas Auxiliares associadas**: em `RESP/DOCS` está `DIC_DADOS_RESP.txt` (dicionário de dados, com as variáveis e seus domínios); em `RESP/AUXILIAR` está `tabresp.zip`, com o arquivo `RESP.def` (definições) e tabelas de conversão `.cnv` usadas pelo TabWin.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (individual/negativa etc.) |
| `ID_AGRAVO` | String | Código do agravo (SCZ/Zika) |
| `DT_NOTIFIC` | Data (`AAAAMMDD`) | Data da notificação |
| `SEM_NOT` | String (`AAAAWW`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município notificante |
| `ID_MUNICIP` | String | Código do município notificante |
| `ID_UNIDADE` | String | Código da unidade notificante (CNES) |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data dos primeiros sintomas |
| `NU_IDADE_N` | String | Código de idade (unidade + valor) |
| `CS_SEXO` | String | Sexo do paciente |
| `CS_GESTANT` | String | Situação/idade gestacional |
| `CS_RACA` / `CS_ESCOL_N` | String | Raça/cor e escolaridade |
| `SG_UF` / `ID_MN_RESI` / `ID_RG_RESI` | String | UF, município e região de residência |
| `CLASSI_FIN` / `CRITERIO` | String | Classificação final e critério de confirmação/descarte |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |

> A lista completa de variáveis (inclusive as laboratoriais e de desfecho) está no dicionário `DIC_DADOS_RESP.txt` (documentação oficial no FTP).

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP`, `ID_MN_RESI`, `SG_UF`, `ID_UNIDADE` e `NU_IDADE_N` devem permanecer `String` (códigos com zeros à esquerda e o código de idade não é um número simples).
- **Datas e competências**: `DT_NOTIFIC`, `DT_SIN_PRI`, `DT_INVEST` são `AAAAMMDD`; `SEM_NOT` é semana epidemiológica (`AAAAWW`) e não deve passar pela conversão de data.
- **Valores ausentes e sentinelas**: campos ignorados do SINAN/RESP (`9`, `99` etc.) devem ser tratados como ausentes; datas podem vir preenchidas como ignoradas.
- **Particularidades do dataset**: a notificação é **individual**, mas sujeita a subnotificação e a alterações retroativas; o sistema surgiu em 2015 para a emergência do Zika, portanto a série começa abruptamente; `NU_IDADE_N` codifica unidade (hora/dia/mês/ano) e valor; a cobertura varia por UF; e a base é pequena em volume mas deve ser analisada com atenção às definições de caso vigentes em cada período.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para resp
quantilica datasus list resp

# 2. Baixar microdados com recorte de anos e UFs (partition uf+year)
quantilica datasus sync resp -o ./data --start 2015 --end 2024 --regions pe sp ba

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync resp -o ./data --docs --aux --start 2015 --end 2024 --regions pe

# 4. Pipeline completo: download, descompactação do .dbc e conversão para Parquet
quantilica datasus pipeline resp -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2024 --regions pe
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

resp = read_dbc("data/raw/resp/2024/resp_2024-pe.dbc", clean=True)

# Notificações por classificação final
casos = resp.group_by("classi_fin").agg(pl.len().alias("n")).sort("n", descending=True)
print(casos)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/RESP/DADOS`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde — Síndrome Congênita associada ao Zika e microcefalia**: https://www.gov.br/saude/pt-br
- **Boletins Epidemiológicos do MS (SCZ/Zika)**
- **Dicionário `DIC_DADOS_RESP.txt`** e pacote `tabresp.zip` no FTP DATASUS
