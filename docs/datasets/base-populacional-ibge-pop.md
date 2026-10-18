# `base-populacional-ibge-pop` — POP: Censo e Estimativas

O `base-populacional-ibge-pop` contém as **populações residentes** dos municípios brasileiros, estratificadas por sexo, situação de domicílio (urbano/rural) e faixa etária, obtidas dos Censos Demográficos, Contagens Populacionais e Projeções Intercensitárias do IBGE e disponibilizadas pelo DATASUS. Cada registro (linha) representa a população de um município, em um ano, para uma combinação de sexo, situação e faixa etária. É a base de denominadores populacionais usada nos indicadores de saúde do SUS para o período de 1980 a 2012.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `base-populacional-ibge` — Base Populacional - IBGE |
| **Código no `datasus-fetcher`** | `base-populacional-ibge-pop` |
| **Formato dos arquivos** | `.zip` (contendo arquivos `.DBF`, `.CSV` e `.XML`) |
| **Particionamento** | `uf`, `year` (na prática um único arquivo nacional `BR` por ano) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 1980 a 2012 (conforme `index.json`) |
| **Volume aproximado no FTP** | 33 arquivos (~150 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/IBGE/DOC` (`populacao.pdf`, etc.) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/IBGE/Auxiliar` (`TAB_POP.zip`) |

## 1. Contexto Institucional e Epidemiológico

A base é produzida pelo **IBGE** (Censos Demográficos, Contagens Populacionais e Projeções da População) e disseminada pelo **Ministério da Saúde/DATASUS**, que padroniza e publica os contingentes populacionais municipais por sexo e faixa etária. O objetivo é fornecer denominadores homogêneos para o cálculo de indicadores epidemiológicos e de gestão do SUS (taxas de incidência, prevalência, mortalidade, cobertura etc.), cobrindo os anos de 1980 a 2012.

O **evento gerador** são os levantamentos demográficos oficiais do IBGE: os **Censos** de 1980, 1991, 2000 e 2010; as **Contagens Populacionais** de 1996; e as **Projeções Intercensitárias/Estimativas** dos demais anos. Conforme a nota técnica `populacao.pdf`, cada período tem metodologia própria: as estimativas de 2001 a 2006 usaram a distribuição etária do Censo 2000 aplicada às estimativas TCU; as de 2007 a 2009 vieram de projeto UNFPA/IBGE (método AiBi e Relação de Coortes); as de 2011 e 2012 aplicaram a estrutura do Censo 2010 sobre as estimativas TCU. A **unidade de análise é a população residente por município, ano, sexo, situação e faixa etária**. Os campos são `MUNIC_RES` (código IBGE de 6 dígitos, sem dígito verificador), `ANO`, `SEXO` (1 - Masculino, 2 - Feminino), `SITUACAO` (1 - Urbano, 2 - Rural, 3 - Não levantado), `FXETARIA` (faixa etária em 4 dígitos: `0000` menor de 1 ano, `0101`..`1919` idades simples, `0004`, `0509`, `1014`... grupos quinquenais, `8099` 80 anos e mais, `I000` idade ignorada) e `POPULACAO`.

A base só contempla detalhamento por situação urbano/rural nos anos censitários e em 1996, conforme a tabela de disponibilidade da nota técnica. As estimativas de 2011 e 2012 não têm abertura urbano/rural (recebem `SITUACAO = 3`). Não há diretório preliminar. A cobertura no FTP encerra-se em 2012, quando passou a ser publicada a série `POPS` (2000 em diante, por sexo e idade simples).

Aplicações analíticas típicas: denominadores de taxas de mortalidade/incidência, cobertura de atenção básica e de vacinação, distribuição etária e por sexo da população, índices de envelhecimento e razão de sexos, planejamento de serviços por porte populacional e estudos demográficos de série histórica longa.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/IBGE/POP` | `POP` | UF + AA (ex.: `BR12`) | `zip` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `POPBR12.zip` — `POP` é o prefixo, `BR` indica a cobertura nacional e `12` o ano de referência (2012). O ZIP contém `POPBR12.DBF`, `POPBR12.csv` e `POPBR12.xml`; há um arquivo por ano.
- **No armazenamento local do `datasus-fetcher`**: `data/base-populacional-ibge-pop/2012/base-populacional-ibge-pop_2012-br@20151110.zip`.
- **Documentação e Tabelas Auxiliares associadas**: em `IBGE/DOC` estão `populacao.pdf` (este dataset), `NT-POPULACAO-RESIDENTE-2000-2024.pdf` (série `POPS`) e `Pop_Residente_TCU_*.pdf` (série `POPT`); em `IBGE/Auxiliar` está `TAB_POP.zip`, com definições e conversões `.cnv`/`.def` para tabulação (inclusive `PROJPOPUF.DEF` e conversões de ano, município e região).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `MUNIC_RES` | String (6) | Código IBGE do município de residência (sem dígito verificador) |
| `ANO` | Inteiro (`AAAA`) | Ano de referência da população |
| `SEXO` | Inteiro (1) | Sexo: 1 - Masculino, 2 - Feminino |
| `SITUACAO` | Inteiro (1) | Situação de domicílio: 1 - Urbano, 2 - Rural, 3 - Não levantado |
| `FXETARIA` | String (4) | Faixa etária (idade simples, quinquenal, `8099` = 80+, `I000` = ignorada) |
| `POPULACAO` | Inteiro (até 9) | População residente para a combinação município/ano/sexo/situação/faixa |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `MUNIC_RES` (6 dígitos) e `FXETARIA` (4 caracteres, incluindo o literal `I000`) devem permanecer `String` com zeros à esquerda — converter a faixa etária a número destruiria as distinções (`0000`, `0101`, `I000`).
- **Datas e competências**: o arquivo não possui datas `AAAAMMDD`; `ANO` é o ano de referência e já é numérico.
- **Valores ausentes e sentinelas**: a série é publicada como microdados já consolidados; atenção ao valor `I000` (idade ignorada) em alguns anos e às células de situação `3` (não levantado).
- **Particularidades do dataset**: a disponibilidade de abertura por situação urbano/rural e por idade simples varia por ano (ver nota técnica); o total de municípios muda ao longo da série por criação/emancipação de municípios e mudanças de divisão administrativa; houve quebras metodológicas em 1992, 2007 (método AiBi) e 2011-2012, recomendando cautela em séries longas; e o município de Pinto Bandeira/RS teve população agregada a Bento Gonçalves/RS em 2003-2012 por decisão judicial.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para base-populacional-ibge-pop
quantilica datasus list base-populacional-ibge-pop

# 2. Baixar microdados com recorte de anos (partition uf+year; na prática br)
quantilica datasus sync base-populacional-ibge-pop -o ./data --start 2000 --end 2012

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync base-populacional-ibge-pop -o ./data --docs --aux --start 2000 --end 2012

# 4. Pipeline completo: download e extração do .zip
quantilica datasus pipeline base-populacional-ibge-pop -o ./data/raw --parquet-dir ./data/parquet --start 2000 --end 2012
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

df_pop = pl.read_csv("data/raw/base-populacional-ibge-pop/2010/POPBR10.csv",
                     separator=";", infer_schema_length=0)

# População total por sexo em 2010
total = (
    df_pop.with_columns(pl.col("POPULACAO").cast(pl.Int64))
    .group_by("SEXO")
    .agg(pl.col("POPULACAO").sum().alias("populacao"))
)
print(total)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/POP`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **IBGE — Censos e Projeções da População**: https://www.ibge.gov.br/estatisticas/sociais/populacao.html
- **Nota técnica `populacao.pdf`** (📎 "População Residente — Censos, Contagens Populacionais e Projeções Intercensitárias") e pacote `TAB_POP.zip` no FTP DATASUS
- **RIPSA — Rede Interagencial de Informações para a Saúde**: https://www.ripsa.org.br/
