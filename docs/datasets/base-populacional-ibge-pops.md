---
dataset:
  id: base-populacional-ibge-pops
  fonte: datasus
  titulo: POPS - Estimativas por Sexo e Idade
  resumo: 'POPS - Estimativas por Sexo e Idade do DATASUS: a população estimada de um município, em um ano, por sexo e idade simples.'
  orgao: Instituto Brasileiro de Geografia e Estatística (IBGE), distribuído pelo DATASUS / Ministério da Saúde
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2000'
    fim: '2025'
  unidade: a população estimada de um município, em um ano, por sexo e idade simples
  granularidade:
    espacial: município; arquivo nacional por ano
    temporal: ano
  formato_bruto: ZIP com um DBF (ou DBC, em 2025) por ano
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 6
  unidades_de_medida:
    pop: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# POPS - Estimativas por Sexo e Idade (`base-populacional-ibge-pops`)

## Resumo

O `base-populacional-ibge-pops` contém as **estimativas populacionais municipais** revisadas do IBGE para o período de 2000 a 2025, desagregadas por **sexo e idade simples**, disponibilizadas pelo Ministério da Saúde (CGIAE/SVSA). Cada registro (linha) representa a população estimada de um município, em um ano, para uma combinação de sexo e idade (0 a 79 anos ano a ano e 80 anos e mais). É a base de denominadores populacionais mais detalhada e metodologicamente consistente usada atualmente para indicadores de saúde no SUS.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/IBGE/DOC` (`NT-POPULACAO-RESIDENTE-2000-2024.pdf`)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/IBGE/Auxiliar` (`TAB_POP.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/IBGE/POPSVS` | `POPS` | UF + AA (ex.: `BR24`) | `zip` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `POPSBR24.zip` — `POPS` é o prefixo da série, `BR` indica cobertura nacional e `24` o ano (2024). O ZIP contém `POP24.dbf` com as colunas `COD_MUN`, `ANO`, `SEXO`, `IDADE` e `POP`.
- **No armazenamento local do `datasus-fetcher`**: `data/base-populacional-ibge-pops/<AAAA>/base-populacional-ibge-pops_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/base-populacional-ibge-pops/2024/base-populacional-ibge-pops_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: a Nota Técnica `NT-POPULACAO-RESIDENTE-2000-2024.pdf` no diretório `IBGE/DOC` descreve método, pressupostos e limitações; o pacote `TAB_POP.zip` em `IBGE/Auxiliar` traz definições/conversões `.cnv` (incluindo `ANOPOPSVS.CNV` e conversões de município/região) para tabulação.

## Conteúdo

As estimativas são produzidas a partir do **Censo Demográfico 2022** e das **Projeções da População** do IBGE (Revisão 2024) e operacionalizadas pela **Coordenação-Geral de Informações e Análises Epidemiológicas (CGIAE)**, vinculada à **Secretaria de Vigilância em Saúde e Ambiente (SVSA)** do Ministério da Saúde. A metodologia segue o método definido pelo **Comitê Temático Interdisciplinar (CTI) das Estimativas Municipais** da RIPSA, com parceria do IBGE para compatibilização territorial e informações sobre mudanças de limites entre municípios.

O **evento gerador** é a revisão das estimativas populacionais municipais após a divulgação do Censo 2022, com uma série consistente de 2000 a 2024/2025. Conforme a nota técnica, o método (a) fez compatibilização territorial da malha municipal de 2022 para o período 2000–2024; (b) ajustou as populações municipais por sexo e idade dos Censos 2000, 2010 e 2022 para convergir com os totais estaduais projetados; (c) aplicou o método **RCoortes** em duas etapas (fatores de crescimento das Regiões Geográficas Intermediárias em relação às UFs e dos municípios em relação às RGInts); e (d) interpolou as populações para os anos intermediários, garantindo convergência com os totais estaduais e com as estimativas de 1º de julho publicadas no DOU. A **unidade de análise é a população residente estimada por município, ano, sexo e idade** (`COD_MUN`, `ANO`, `SEXO`, `IDADE`, `POP`).

Os dados podem ser consultados por idade simples (0 a 79 anos ano a ano, 80+), Faixa Etária 1 (0-4, 5-9, 10-14, 15-19, 20-69 de 10 em 10, 80+) e Faixa Etária 2 (grupos quinquenais até 79 e 80+). Não há diretório preliminar. Esta série substitui, para anos recentes, a antiga base `POP` (que termina em 2012) e é a base preferencial para o cálculo de indicadores com abertura etária.

Aplicações analíticas típicas: taxas de mortalidade e incidência específicas por faixa etária, cobertura de programas por ciclo de vida, construção de pirâmides etárias, projeções e análises demográficas municipais e cálculo de indicadores de envelhecimento — sempre com a cautela metodológica indicada pela nota técnica para pequenas áreas.

### Cobertura observada

- Índice do FTP (2026-10): 26 arquivos, de 2000 a 2025, 1 UF(s) com arquivos, última atualização em 2025-10-29.
- Conversão local de amostras (2 arquivo(s) Parquet, de 2000 a 2025), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `COD_MUN` | String (7) | Código IBGE do município (7 dígitos, com dígito verificador) |
| `ANO` | String (`AAAA`) | Ano de referência da estimativa (2000 a 2024/2025) |
| `SEXO` | String (1) | Sexo: 1 - Masculino, 2 - Feminino |
| `IDADE` | String (3) | Idade simples de 0 a 79 (`000`..`079`), 80+ consolidado (`080`) |
| `POP` | Inteiro (até 9) | População residente estimada para município/ano/sexo/idade |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `cod_mun` | `COD_MUN` | texto | Código do município pelo padrão IBGE, com 6 dígitos (sem o dígito verificador) | — | todos |
| `sexo` | `SEXO` | texto | Sexo da população estimada | — | todos |
| `idade` | `IDADE` | texto | Idade simples, em anos completos | — | todos |
| `pop` | `POP` | inteiro | População residente estimada, em pessoas | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/base-populacional-ibge-pops`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): inteiro: 1, texto: 5.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `base-populacional-ibge-pops.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- `COD_MUN` usa o código de 7 dígitos (com DV), diferentemente da série `POP` (6 dígitos) — padronizar antes de cruzar; a série é anual e converge com os totais estaduais, então somas municipais reproduzem o total da UF; há mudança metodológica em relação à série `POP` (não comparável diretamente); e a nota técnica alerta para limitações inerentes a estimativas de pequenas áreas (choques econômicos, migratórios e ambientais). A série no FTP vai até 2025, embora a nota técnica documente oficialmente 2000–2024. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/base-populacional-ibge-pops").glob("**/*.parquet"))
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
datasus-fetcher list base-populacional-ibge-pops

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync base-populacional-ibge-pops -o ./data --start 2020 --end 2024 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset base-populacional-ibge-pops
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/POPSVS`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **IBGE — Projeções da População e Censo 2022**: https://www.ibge.gov.br/estatisticas/sociais/populacao.html
- **Nota técnica `NT-POPULACAO-RESIDENTE-2000-2024.pdf`** e pacote `TAB_POP.zip` no FTP DATASUS
- **RIPSA / CTI de Estimativas Municipais** e **SVSA/CGIAE**: cgiae@saude.gov.br
