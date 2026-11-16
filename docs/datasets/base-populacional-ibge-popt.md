---
dataset:
  id: base-populacional-ibge-popt
  fonte: datasus
  titulo: POPT - Estimativas TCU
  resumo: 'POPT - Estimativas TCU do DATASUS: a população total estimada de um município em um ano (estimativas para o TCU).'
  orgao: Instituto Brasileiro de Geografia e Estatística (IBGE), distribuído pelo DATASUS / Ministério da Saúde
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '1992'
    fim: em-curso
  unidade: a população total estimada de um município em um ano (estimativas para o TCU)
  granularidade:
    espacial: município; arquivo nacional por ano
    temporal: ano
  formato_bruto: ZIP com um DBF (ou DBC, em 2025) por ano
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 4
  unidades_de_medida:
    populacao: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# POPT - Estimativas TCU (`base-populacional-ibge-popt`)

## Resumo

O `base-populacional-ibge-popt` contém as **estimativas anuais de população residente** dos municípios brasileiros, com data de referência de 1º de julho, publicadas pelo IBGE para o **Tribunal de Contas da União (TCU)**. Cada registro (linha) representa a população total estimada de um município em um ano. É a base de denominadores utilizada oficialmente para o cálculo das cotas do **Fundo de Participação dos Estados e Municípios (FPE/FPM)** e, no SUS, como referência para alguns repasses e indicadores.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/IBGE/DOC` (`Pop_Residente_TCU_2024.pdf`, `Pop_Residente_TCU_ate_2023.pdf`)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/IBGE/Auxiliar` (`TAB_POP.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/IBGE/POPTCU` | `POPT` | UF + AA (ex.: `BR24`) | `zip` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `POPTBR24.zip` — `POPT` é o prefixo da série TCU, `BR` indica cobertura nacional e `24` o ano (2024). O ZIP contém `poptbr24.dbf` com as colunas `MUNIC_RES`, `ANO` e `POPULACAO`. Há arquivos desde `POPTBR92.zip`, com `POPTBR14.zip` em diante mais compactos.
- **No armazenamento local do `datasus-fetcher`**: `data/base-populacional-ibge-popt/<AAAA>/base-populacional-ibge-popt_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/base-populacional-ibge-popt/2024/base-populacional-ibge-popt_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `IBGE/DOC` estão `Pop_Residente_TCU_2024.pdf` e `Pop_Residente_TCU_ate_2023.pdf`; em `IBGE/Auxiliar` está `TAB_POP.zip` com conversões para tabulação (inclusive `br_municip.cnv`).

## Conteúdo

As estimativas são elaboradas pelo **IBGE** e publicadas anualmente no **Diário Oficial da União (DOU)** em cumprimento ao **art. 102 da Lei nº 8.443/1992** (Lei Orgânica do TCU), que determina a publicação das populações municipais até 31 de agosto e das estaduais até 31 de dezembro de cada ano. A **Lei Complementar nº 143/2013** atualizou esse dispositivo. Essas estimativas embasam o cálculo das cotas do **Fundo de Participação dos Estados e Municípios (FPE/FPM)**, a definição de áreas para criação de novos municípios/distritos e a verificação de limites territoriais.

O **evento gerador** é o levantamento anual de estimativas do IBGE para o TCU, com data de referência de 1º de julho. A **unidade de análise é a população total estimada do município no ano** (`MUNIC_RES`, `ANO`, `POPULACAO`) — sem abertura por sexo idade ou situação. Conforme a nota técnica `Pop_Residente_TCU_2024.pdf`, recomenda-se **cautela ao usar a série como série temporal**, pois as estimativas **não são estatisticamente comparáveis ao longo do tempo**: mudam as metodologias, os dados de base (novos censos/projeções) e a Divisão Político-Administrativa do país (criação de municípios e trocas territoriais). O exemplo clássico é o município de São Paulo, cuja estimativa caiu de 12.396.372 (2021) para 11.895.578 (2024) não por redução real, mas por diferenças metodológicas.

A cobertura no FTP vai de 1992 a 2025. A série tem dois blocos de documentação: `Pop_Residente_TCU_2024.pdf` (ano corrente, com a tabela de resoluções/publicações no DOU) e `Pop_Residente_TCU_ate_2023.pdf` (histórico). Não há diretório preliminar.

Aplicações analíticas típicas: denominador populacional total para taxas gerais, verificação de cotas de FPM, comparação com as bases `POP`/`POPS`, e uso como referência rápida de população municipal — sempre evitando interpretações de tendência temporal entre anos metodologicamente distintos.

### Cobertura observada

- Índice do FTP (2026-10): 33 arquivos, de 1992 a 2025, 1 UF(s) com arquivos, última atualização em 2026-01-21.
- Conversão local de amostras (2 arquivo(s) Parquet, de 1992 a 2025), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `MUNIC_RES` | String (7) | Código IBGE do município (7 dígitos, com dígito verificador) |
| `ANO` | String (`AAAA`) | Ano de referência da estimativa (1992 a 2025) |
| `POPULACAO` | Inteiro (até 8) | População residente estimada em 1º de julho do ano de referência |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `munic_res` | `MUNIC_RES` | texto | Código do município pelo padrão IBGE, com 6 dígitos (sem o dígito verificador) | — | todos |
| `populacao` | `POPULACAO` | inteiro | População residente total estimada para o município, em 1º de julho, em pessoas | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/base-populacional-ibge-popt`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): inteiro: 1, texto: 3.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `base-populacional-ibge-popt.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- é a base mais enxuta (apenas população total, sem sexo/idade); a série **não é temporalmente consistente** (metodologias e divisão administrativa mudam ano a ano), portanto não deve ser usada para medir crescimento populacional; os códigos de município de 7 dígitos devem ser padronizados para 6 dígitos (sem DV) ao cruzar com bases de saúde; e o DATASUS recomenda usar `POPS` (por sexo e idade) ou a série do Censo quando o objetivo for consistência temporal. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/base-populacional-ibge-popt").glob("**/*.parquet"))
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
datasus-fetcher list base-populacional-ibge-popt

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync base-populacional-ibge-popt -o ./data --start 2020 --end 2024 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset base-populacional-ibge-popt
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/IBGE/POPTCU`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **IBGE — Estimativas de População (TCU)**: https://www.ibge.gov.br/estatisticas/sociais/populacao.html
- **Notas técnicas `Pop_Residente_TCU_2024.pdf` e `Pop_Residente_TCU_ate_2023.pdf`** no FTP DATASUS
- **Lei nº 8.443/1992 (art. 102)** e **Lei Complementar nº 143/2013** (publicação das populações para o TCU)
