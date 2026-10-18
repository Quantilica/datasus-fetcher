# `base-populacional-ibge-popt` — POPT - Estimativas TCU

O `base-populacional-ibge-popt` contém as **estimativas anuais de população residente** dos municípios brasileiros, com data de referência de 1º de julho, publicadas pelo IBGE para o **Tribunal de Contas da União (TCU)**. Cada registro (linha) representa a população total estimada de um município em um ano. É a base de denominadores utilizada oficialmente para o cálculo das cotas do **Fundo de Participação dos Estados e Municípios (FPE/FPM)** e, no SUS, como referência para alguns repasses e indicadores.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `base-populacional-ibge` — Base Populacional - IBGE |
| **Código no `datasus-fetcher`** | `base-populacional-ibge-popt` |
| **Formato dos arquivos** | `.zip` (contendo um arquivo `.dbf`) |
| **Particionamento** | `uf`, `year` (na prática um único arquivo nacional `BR` por ano) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 1992 a 2025 (conforme `index.json`) |
| **Volume aproximado no FTP** | 33 arquivos (~2,5 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/IBGE/DOC` (`Pop_Residente_TCU_2024.pdf`, `Pop_Residente_TCU_ate_2023.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/IBGE/Auxiliar` (`TAB_POP.zip`) |

## 1. Contexto Institucional e Epidemiológico

As estimativas são elaboradas pelo **IBGE** e publicadas anualmente no **Diário Oficial da União (DOU)** em cumprimento ao **art. 102 da Lei nº 8.443/1992** (Lei Orgânica do TCU), que determina a publicação das populações municipais até 31 de agosto e das estaduais até 31 de dezembro de cada ano. A **Lei Complementar nº 143/2013** atualizou esse dispositivo. Essas estimativas embasam o cálculo das cotas do **Fundo de Participação dos Estados e Municípios (FPE/FPM)**, a definição de áreas para criação de novos municípios/distritos e a verificação de limites territoriais.

O **evento gerador** é o levantamento anual de estimativas do IBGE para o TCU, com data de referência de 1º de julho. A **unidade de análise é a população total estimada do município no ano** (`MUNIC_RES`, `ANO`, `POPULACAO`) — sem abertura por sexo idade ou situação. Conforme a nota técnica `Pop_Residente_TCU_2024.pdf`, recomenda-se **cautela ao usar a série como série temporal**, pois as estimativas **não são estatisticamente comparáveis ao longo do tempo**: mudam as metodologias, os dados de base (novos censos/projeções) e a Divisão Político-Administrativa do país (criação de municípios e trocas territoriais). O exemplo clássico é o município de São Paulo, cuja estimativa caiu de 12.396.372 (2021) para 11.895.578 (2024) não por redução real, mas por diferenças metodológicas.

A cobertura no FTP vai de 1992 a 2025. A série tem dois blocos de documentação: `Pop_Residente_TCU_2024.pdf` (ano corrente, com a tabela de resoluções/publicações no DOU) e `Pop_Residente_TCU_ate_2023.pdf` (histórico). Não há diretório preliminar.

Aplicações analíticas típicas: denominador populacional total para taxas gerais, verificação de cotas de FPM, comparação com as bases `POP`/`POPS`, e uso como referência rápida de população municipal — sempre evitando interpretações de tendência temporal entre anos metodologicamente distintos.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/IBGE/POPTCU` | `POPT` | UF + AA (ex.: `BR24`) | `zip` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `POPTBR24.zip` — `POPT` é o prefixo da série TCU, `BR` indica cobertura nacional e `24` o ano (2024). O ZIP contém `poptbr24.dbf` com as colunas `MUNIC_RES`, `ANO` e `POPULACAO`. Há arquivos desde `POPTBR92.zip`, com `POPTBR14.zip` em diante mais compactos.
- **No armazenamento local do `datasus-fetcher`**: `data/base-populacional-ibge-popt/2024/base-populacional-ibge-popt_2024-br@20260121.zip`.
- **Documentação e Tabelas Auxiliares associadas**: em `IBGE/DOC` estão `Pop_Residente_TCU_2024.pdf` e `Pop_Residente_TCU_ate_2023.pdf`; em `IBGE/Auxiliar` está `TAB_POP.zip` com conversões para tabulação (inclusive `br_municip.cnv`).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `MUNIC_RES` | String (7) | Código IBGE do município (7 dígitos, com dígito verificador) |
| `ANO` | String (`AAAA`) | Ano de referência da estimativa (1992 a 2025) |
| `POPULACAO` | Inteiro (até 8) | População residente estimada em 1º de julho do ano de referência |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `MUNIC_RES` tem 7 dígitos e deve permanecer `String` com zeros à esquerda (difere da base `POP`, de 6 dígitos).
- **Datas e competências**: `ANO` é o ano de referência (texto `AAAA`); não há datas `AAAAMMDD`.
- **Valores ausentes e sentinelas**: a série é publicada consolidada; não há códigos ignorados relevantes.
- **Particularidades do dataset**: é a base mais enxuta (apenas população total, sem sexo/idade); a série **não é temporalmente consistente** (metodologias e divisão administrativa mudam ano a ano), portanto não deve ser usada para medir crescimento populacional; os códigos de município de 7 dígitos devem ser padronizados para 6 dígitos (sem DV) ao cruzar com bases de saúde; e o DATASUS recomenda usar `POPS` (por sexo e idade) ou a série do Censo quando o objetivo for consistência temporal.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para base-populacional-ibge-popt
quantilica datasus list base-populacional-ibge-popt

# 2. Baixar microdados (partition uf+year; na prática br)
quantilica datasus sync base-populacional-ibge-popt -o ./data --start 2000 --end 2025

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync base-populacional-ibge-popt -o ./data --docs --aux --start 2000 --end 2025

# 4. Pipeline completo: download, extração do .zip e conversão do DBF para Parquet
quantilica datasus pipeline base-populacional-ibge-popt -o ./data/raw --parquet-dir ./data/parquet --start 2000 --end 2025
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbf

popt = read_dbf("data/raw/base-populacional-ibge-popt/2024/poptbr24.dbf", clean=True)

# População estimada para um município específico (ex.: São Paulo 3550308)
sp = popt.filter(pl.col("munic_res").str.starts_with("3550308"))
print(sp)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/POPTCU`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **IBGE — Estimativas de População (TCU)**: https://www.ibge.gov.br/estatisticas/sociais/populacao.html
- **Notas técnicas `Pop_Residente_TCU_2024.pdf` e `Pop_Residente_TCU_ate_2023.pdf`** no FTP DATASUS
- **Lei nº 8.443/1992 (art. 102)** e **Lei Complementar nº 143/2013** (publicação das populações para o TCU)
