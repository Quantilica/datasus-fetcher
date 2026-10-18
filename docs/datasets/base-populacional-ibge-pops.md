# `base-populacional-ibge-pops` — POPS: Estimativas por Sexo e Idade

O `base-populacional-ibge-pops` contém as **estimativas populacionais municipais** revisadas do IBGE para o período de 2000 a 2025, desagregadas por **sexo e idade simples**, disponibilizadas pelo Ministério da Saúde (CGIAE/SVSA). Cada registro (linha) representa a população estimada de um município, em um ano, para uma combinação de sexo e idade (0 a 79 anos ano a ano e 80 anos e mais). É a base de denominadores populacionais mais detalhada e metodologicamente consistente usada atualmente para indicadores de saúde no SUS.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `base-populacional-ibge` — Base Populacional - IBGE |
| **Código no `datasus-fetcher`** | `base-populacional-ibge-pops` |
| **Formato dos arquivos** | `.zip` (contendo um arquivo `.dbf`) |
| **Particionamento** | `uf`, `year` (na prática um único arquivo nacional `BR` por ano) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2000 a 2025 (conforme `index.json`; a nota técnica descreve 2000–2024) |
| **Volume aproximado no FTP** | 26 arquivos (~86 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/IBGE/DOC` (`NT-POPULACAO-RESIDENTE-2000-2024.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/IBGE/Auxiliar` (`TAB_POP.zip`) |

## 1. Contexto Institucional e Epidemiológico

As estimativas são produzidas a partir do **Censo Demográfico 2022** e das **Projeções da População** do IBGE (Revisão 2024) e operacionalizadas pela **Coordenação-Geral de Informações e Análises Epidemiológicas (CGIAE)**, vinculada à **Secretaria de Vigilância em Saúde e Ambiente (SVSA)** do Ministério da Saúde. A metodologia segue o método definido pelo **Comitê Temático Interdisciplinar (CTI) das Estimativas Municipais** da RIPSA, com parceria do IBGE para compatibilização territorial e informações sobre mudanças de limites entre municípios.

O **evento gerador** é a revisão das estimativas populacionais municipais após a divulgação do Censo 2022, com uma série consistente de 2000 a 2024/2025. Conforme a nota técnica, o método (a) fez compatibilização territorial da malha municipal de 2022 para o período 2000–2024; (b) ajustou as populações municipais por sexo e idade dos Censos 2000, 2010 e 2022 para convergir com os totais estaduais projetados; (c) aplicou o método **RCoortes** em duas etapas (fatores de crescimento das Regiões Geográficas Intermediárias em relação às UFs e dos municípios em relação às RGInts); e (d) interpolou as populações para os anos intermediários, garantindo convergência com os totais estaduais e com as estimativas de 1º de julho publicadas no DOU. A **unidade de análise é a população residente estimada por município, ano, sexo e idade** (`COD_MUN`, `ANO`, `SEXO`, `IDADE`, `POP`).

Os dados podem ser consultados por idade simples (0 a 79 anos ano a ano, 80+), Faixa Etária 1 (0-4, 5-9, 10-14, 15-19, 20-69 de 10 em 10, 80+) e Faixa Etária 2 (grupos quinquenais até 79 e 80+). Não há diretório preliminar. Esta série substitui, para anos recentes, a antiga base `POP` (que termina em 2012) e é a base preferencial para o cálculo de indicadores com abertura etária.

Aplicações analíticas típicas: taxas de mortalidade e incidência específicas por faixa etária, cobertura de programas por ciclo de vida, construção de pirâmides etárias, projeções e análises demográficas municipais e cálculo de indicadores de envelhecimento — sempre com a cautela metodológica indicada pela nota técnica para pequenas áreas.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/IBGE/POPSVS` | `POPS` | UF + AA (ex.: `BR24`) | `zip` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `POPSBR24.zip` — `POPS` é o prefixo da série, `BR` indica cobertura nacional e `24` o ano (2024). O ZIP contém `POP24.dbf` com as colunas `COD_MUN`, `ANO`, `SEXO`, `IDADE` e `POP`.
- **No armazenamento local do `datasus-fetcher`**: `data/base-populacional-ibge-pops/2024/base-populacional-ibge-pops_2024-br@20251029.zip`.
- **Documentação e Tabelas Auxiliares associadas**: a Nota Técnica `NT-POPULACAO-RESIDENTE-2000-2024.pdf` no diretório `IBGE/DOC` descreve método, pressupostos e limitações; o pacote `TAB_POP.zip` em `IBGE/Auxiliar` traz definições/conversões `.cnv` (incluindo `ANOPOPSVS.CNV` e conversões de município/região) para tabulação.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `COD_MUN` | String (7) | Código IBGE do município (7 dígitos, com dígito verificador) |
| `ANO` | String (`AAAA`) | Ano de referência da estimativa (2000 a 2024/2025) |
| `SEXO` | String (1) | Sexo: 1 - Masculino, 2 - Feminino |
| `IDADE` | String (3) | Idade simples de 0 a 79 (`000`..`079`), 80+ consolidado (`080`) |
| `POP` | Inteiro (até 9) | População residente estimada para município/ano/sexo/idade |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `COD_MUN` tem 7 dígitos e deve permanecer `String` com zeros à esquerda; `SEXO` e `IDADE` também são texto (`"000"`..`"080"`) — converter `IDADE` a inteiro é possível após o `zfill`, mas cuidado com o valor `080` (80+).
- **Datas e competências**: `ANO` é o ano de referência (texto de 4 dígitos); não há datas `AAAAMMDD`.
- **Valores ausentes e sentinelas**: a série é publicada consolidada; não há códigos ignorados de idade (o 80+ já é agregado) nem espaços relevantes.
- **Particularidades do dataset**: `COD_MUN` usa o código de 7 dígitos (com DV), diferentemente da série `POP` (6 dígitos) — padronizar antes de cruzar; a série é anual e converge com os totais estaduais, então somas municipais reproduzem o total da UF; há mudança metodológica em relação à série `POP` (não comparável diretamente); e a nota técnica alerta para limitações inerentes a estimativas de pequenas áreas (choques econômicos, migratórios e ambientais). A série no FTP vai até 2025, embora a nota técnica documente oficialmente 2000–2024.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para base-populacional-ibge-pops
quantilica datasus list base-populacional-ibge-pops

# 2. Baixar microdados (partition uf+year; na prática br)
quantilica datasus sync base-populacional-ibge-pops -o ./data --start 2010 --end 2024

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync base-populacional-ibge-pops -o ./data --docs --aux --start 2010 --end 2024

# 4. Pipeline completo: download, extração do .zip e conversão do DBF para Parquet
quantilica datasus pipeline base-populacional-ibge-pops -o ./data/raw --parquet-dir ./data/parquet --start 2010 --end 2024
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbf

pop = read_dbf("data/raw/base-populacional-ibge-pops/2024/POP24.dbf", clean=True)

# População total e pirâmide por sexo em 2024
piramide = (
    pop.group_by(["idade", "sexo"])
    .agg(pl.col("pop").sum().alias("pop"))
    .sort(["idade", "sexo"])
)
print(piramide.head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/POPSVS`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **IBGE — Projeções da População e Censo 2022**: https://www.ibge.gov.br/estatisticas/sociais/populacao.html
- **Nota técnica `NT-POPULACAO-RESIDENTE-2000-2024.pdf`** e pacote `TAB_POP.zip` no FTP DATASUS
- **RIPSA / CTI de Estimativas Municipais** e **SVSA/CGIAE**: cgiae@saude.gov.br
