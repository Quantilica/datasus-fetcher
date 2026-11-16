---
dataset:
  id: base-populacional-ibge-pop
  fonte: datasus
  titulo: POP - Censo e Estimativas
  resumo: 'POP - Censo e Estimativas do DATASUS: a população residente de um município, em um ano, por sexo, situação e faixa etária.'
  orgao: Instituto Brasileiro de Geografia e Estatística (IBGE), distribuído pelo DATASUS / Ministério da Saúde
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '1980'
    fim: '2012'
  unidade: a população residente de um município, em um ano, por sexo, situação e faixa etária
  granularidade:
    espacial: município; arquivo nacional por ano
    temporal: ano
  formato_bruto: ZIP com um DBF (ou DBC, em 2025) por ano
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 7
  unidades_de_medida:
    populacao: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# POP - Censo e Estimativas (`base-populacional-ibge-pop`)

## Resumo

O `base-populacional-ibge-pop` contém as **populações residentes** dos municípios brasileiros, estratificadas por sexo, situação de domicílio (urbano/rural) e faixa etária, obtidas dos Censos Demográficos, Contagens Populacionais e Projeções Intercensitárias do IBGE e disponibilizadas pelo DATASUS. Cada registro (linha) representa a população de um município, em um ano, para uma combinação de sexo, situação e faixa etária. É a base de denominadores populacionais usada nos indicadores de saúde do SUS para o período de 1980 a 2012.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/IBGE/DOC` (`populacao.pdf`, etc.)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/IBGE/Auxiliar` (`TAB_POP.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/IBGE/POP` | `POP` | UF + AA (ex.: `BR12`) | `zip` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `POPBR12.zip` — `POP` é o prefixo, `BR` indica a cobertura nacional e `12` o ano de referência (2012). O ZIP contém `POPBR12.DBF`, `POPBR12.csv` e `POPBR12.xml`; há um arquivo por ano.
- **No armazenamento local do `datasus-fetcher`**: `data/base-populacional-ibge-pop/<AAAA>/base-populacional-ibge-pop_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/base-populacional-ibge-pop/2024/base-populacional-ibge-pop_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `IBGE/DOC` estão `populacao.pdf` (este dataset), `NT-POPULACAO-RESIDENTE-2000-2024.pdf` (série `POPS`) e `Pop_Residente_TCU_*.pdf` (série `POPT`); em `IBGE/Auxiliar` está `TAB_POP.zip`, com definições e conversões `.cnv`/`.def` para tabulação (inclusive `PROJPOPUF.DEF` e conversões de ano, município e região).

## Conteúdo

A base é produzida pelo **IBGE** (Censos Demográficos, Contagens Populacionais e Projeções da População) e disseminada pelo **Ministério da Saúde/DATASUS**, que padroniza e publica os contingentes populacionais municipais por sexo e faixa etária. O objetivo é fornecer denominadores homogêneos para o cálculo de indicadores epidemiológicos e de gestão do SUS (taxas de incidência, prevalência, mortalidade, cobertura etc.), cobrindo os anos de 1980 a 2012.

O **evento gerador** são os levantamentos demográficos oficiais do IBGE: os **Censos** de 1980, 1991, 2000 e 2010; as **Contagens Populacionais** de 1996; e as **Projeções Intercensitárias/Estimativas** dos demais anos. Conforme a nota técnica `populacao.pdf`, cada período tem metodologia própria: as estimativas de 2001 a 2006 usaram a distribuição etária do Censo 2000 aplicada às estimativas TCU; as de 2007 a 2009 vieram de projeto UNFPA/IBGE (método AiBi e Relação de Coortes); as de 2011 e 2012 aplicaram a estrutura do Censo 2010 sobre as estimativas TCU. A **unidade de análise é a população residente por município, ano, sexo, situação e faixa etária**. Os campos são `MUNIC_RES` (código IBGE de 6 dígitos, sem dígito verificador), `ANO`, `SEXO` (1 - Masculino, 2 - Feminino), `SITUACAO` (1 - Urbano, 2 - Rural, 3 - Não levantado), `FXETARIA` (faixa etária em 4 dígitos: `0000` menor de 1 ano, `0101`..`1919` idades simples, `0004`, `0509`, `1014`... grupos quinquenais, `8099` 80 anos e mais, `I000` idade ignorada) e `POPULACAO`.

A base só contempla detalhamento por situação urbano/rural nos anos censitários e em 1996, conforme a tabela de disponibilidade da nota técnica. As estimativas de 2011 e 2012 não têm abertura urbano/rural (recebem `SITUACAO = 3`). Não há diretório preliminar. A cobertura no FTP encerra-se em 2012, quando passou a ser publicada a série `POPS` (2000 em diante, por sexo e idade simples).

Aplicações analíticas típicas: denominadores de taxas de mortalidade/incidência, cobertura de atenção básica e de vacinação, distribuição etária e por sexo da população, índices de envelhecimento e razão de sexos, planejamento de serviços por porte populacional e estudos demográficos de série histórica longa.

### Cobertura observada

- Índice do FTP (2026-10): 33 arquivos, de 1980 a 2012, 1 UF(s) com arquivos, última atualização em 2015-11-10.
- Conversão local de amostras (2 arquivo(s) Parquet, de 1980 a 2012), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `MUNIC_RES` | String (6) | Código IBGE do município de residência (sem dígito verificador) |
| `ANO` | Inteiro (`AAAA`) | Ano de referência da população |
| `SEXO` | Inteiro (1) | Sexo: 1 - Masculino, 2 - Feminino |
| `SITUACAO` | Inteiro (1) | Situação de domicílio: 1 - Urbano, 2 - Rural, 3 - Não levantado |
| `FXETARIA` | String (4) | Faixa etária (idade simples, quinquenal, `8099` = 80+, `I000` = ignorada) |
| `POPULACAO` | Inteiro (até 9) | População residente para a combinação município/ano/sexo/situação/faixa |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `munic_res` | `MUNIC_RES` | texto | Código do município pelo padrão IBGE, com 6 dígitos (sem o dígito verificador) | — | todos |
| `sexo` | `SEXO` | texto | Sexo: 1 masculino; 2 feminino | 1 masculino; 2 feminino | todos |
| `situacao` | `SITUACAO` | texto | Situação de domicílio: 1 urbano; 2 rural; 3 não levantado (só nos anos em que há detalhamento) | 1 urbano; 2 rural; 3 não levantado | todos |
| `fxetaria` | `FXETARIA` | texto | Faixa etária da população, em 4 dígitos | 0000 menor de 1 ano; 0101 a 1919 idades de 1 a 19 anos; 0004, 0509, 1014... 7579 grupos de 5 anos; 8099 80 anos e mais; I000 idade ignorada | todos |
| `populacao` | `POPULACAO` | inteiro | População residente estimada ou recenseada, em pessoas | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/base-populacional-ibge-pop`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): inteiro: 1, texto: 6.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `base-populacional-ibge-pop.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- a disponibilidade de abertura por situação urbano/rural e por idade simples varia por ano (ver nota técnica); o total de municípios muda ao longo da série por criação/emancipação de municípios e mudanças de divisão administrativa; houve quebras metodológicas em 1992, 2007 (método AiBi) e 2011-2012, recomendando cautela em séries longas; e o município de Pinto Bandeira/RS teve população agregada a Bento Gonçalves/RS em 2003-2012 por decisão judicial. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/base-populacional-ibge-pop").glob("**/*.parquet"))
dados = pl.concat(  # períodos diferentes têm colunas e tipos diferentes
    [pl.scan_parquet(a, hive_partitioning=True) for a in arquivos],
    how="diagonal_relaxed",
)

(dados.group_by("ano", "uf").agg(pl.len().alias("linhas")).sort("ano", "uf").collect())
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Pela linha de comando (`datasus-fetcher`)

```bash
# o que o FTP publica para o dataset (arquivos e tamanho)
datasus-fetcher list base-populacional-ibge-pop

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync base-populacional-ibge-pop -o ./data --start 2020 --end 2024 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset base-populacional-ibge-pop
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/POP`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **IBGE — Censos e Projeções da População**: https://www.ibge.gov.br/estatisticas/sociais/populacao.html
- **Nota técnica `populacao.pdf`** (📎 "População Residente — Censos, Contagens Populacionais e Projeções Intercensitárias") e pacote `TAB_POP.zip` no FTP DATASUS
- **RIPSA — Rede Interagencial de Informações para a Saúde**: https://www.ripsa.org.br/
