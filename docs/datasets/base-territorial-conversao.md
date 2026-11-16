---
dataset:
  id: base-territorial-conversao
  fonte: datasus
  titulo: Base Territorial - Conversão
  resumo: 'Base Territorial - Conversão do DATASUS: um código de uma categoria de conversão do TabWin (arquivo `.cnv`), por UF.'
  orgao: Ministério da Saúde — DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/territorio/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: por versão publicada (sem periodicidade regular)
  cobertura:
    inicio: '2026'
    fim: em-curso
  unidade: um código de uma categoria de conversão do TabWin (arquivo `.cnv`), por UF
  granularidade:
    espacial: UF e município
    temporal: versão (mês de publicação)
  formato_bruto: ZIP
  lake:
    estado: convertido
    particoes: []
    chave: []
    colunas: 7
  unidades_de_medida:
    sequencia: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nivel: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Base Territorial - Conversão (`base-territorial-conversao`)

## Resumo

O `base-territorial-conversao` contém as **tabelas de conversão** (`.cnv`) entre códigos territoriais usados pelos sistemas de informação do DATASUS e os códigos da Base Territorial. Cada arquivo `.cnv` é um mapeamento de uma UF (ou do Brasil) que permite traduzir códigos antigos/legados de município, região de saúde, macrorregião, microrregião IBGE, região metropolitana, divisão administrativa e distritos sanitários indígenas para os códigos vigentes. É ferramenta essencial para compatibilizar séries históricas com a divisão territorial atual.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/territorio/doc` (`bases_territoriais.pdf`, `registro_de_alteracoes.pdf`)
- **Tabelas auxiliares no FTP:** Não aplicável

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/territorio/conversoes` | (vazio) | `<uf>_cnv` (ex.: `sp_cnv`, `br_cnv`, `todos_cnv`) | `zip` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `sp_cnv.zip` — `sp` é a UF e `cnv` indica conversões. Contém arquivos como `sp_divadm.cnv`, `sp_municip.cnv`, `SP_macsaud.cnv`, `sp_regsaud.cnv`, `SP_regsaudmun.cnv`, `sp_regmetr.cnv`, `sp_micibge.cnv`, `sp_municgestor.cnv`. Existem também `br_cnv.zip` e `todos_cnv.zip`.
- **No armazenamento local do `datasus-fetcher`**: `data/base-territorial-conversao/base-territorial-conversao_<uf>@<AAAAMMDD>.zip` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `bases_territoriais.pdf` e `registro_de_alteracoes.pdf` em `/territorio/doc` explicam a estrutura das conversões e o histórico de mudanças territoriais. As conversões também são acompanhadas pelos pacotes de auxiliares dos sistemas produtores (ex.: `TAB_POP.zip`, `tab_pce.zip`, `tabresp.zip`), que repetem conversões de município/região.

## Conteúdo

As tabelas de conversão fazem parte do conjunto da **Base Territorial** mantida pelo **Ministério da Saúde/DATASUS**. Elas resolvem um problema central da análise de dados em saúde: os códigos territoriais mudam ao longo do tempo (criação, fusão e desmembramento de municípios; reorganização de regiões de saúde; alterações de divisão administrativa), enquanto as bases históricas mantêm os códigos originais. Sem conversão, séries longas ficariam inconsistentes.

O **evento gerador** é a publicação, pelo DATASUS, dos arquivos de conversão atualizados conforme a Base Territorial. A **unidade de análise é a linha de conversão**, que associa um código de origem a um código de destino segundo um recorte (município, região de saúde, macrorregião etc.). O particionamento é por **UF** (arquivo `<uf>_cnv.zip`), havendo também `br_cnv.zip` e `todos_cnv.zip` consolidando o país. Cada ZIP contém variantes: sem sufixo (tabela base), `*c.cnv` (cadastro/consolidado), `*mun.cnv` (por município) e `*n.cnv` (nomes/atributos), conforme o recorte — por exemplo `sp_municip.cnv`, `sp_regsaud.cnv`, `SP_regsaudmun.cnv`, `sp_macsaudn.cnv`.

Não há recorte temporal no índice (a versão é a corrente) nem diretório preliminar. Os arquivos `.cnv` são no formato texto indexado do TabWin (semelhante a um DBF de tabela de domínio), com pares de códigos/descrições.

Aplicações analíticas típicas: compatibilizar bases de SIH/SIA/SINAN/SIM com a malha municipal vigente, remapear municípios extintos para seus sucessores, agregar produção/procedimentos aos recortes regionais atuais, apoiar estudos de série histórica municipal e converter códigos legados usados por versões antigas dos sistemas.

### Cobertura observada

- Sem recorte temporal: o FTP publica o cadastro vigente (última atualização em 2026-10-15); o início da cobertura no cabeçalho é o ano de publicação da versão mais antiga ou da atual, não um período de dados.
- Conversão local de amostras (1 arquivo(s) Parquet, de — a —), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Arquivo (`.cnv`) | Conteúdo | Descrição |
|---|---|---|
| `<uf>_municip.cnv` | Código e nome de município | Conversão de código antigo para município vigente |
| `<uf>_regsaud.cnv` | Código e nome de região de saúde | Mapeamento para regiões de saúde atuais |
| `SP_<uf>_macsaud.cnv` | Código de macrorregião de saúde | Mapeamento para macrorregiões |
| `<uf>_regmetr.cnv` | Código de região metropolitana | Mapeamento para regiões metropolitanas |
| `<uf>_micibge.cnv` | Código de microrregião IBGE | Mapeamento para microrregiões IBGE |
| `<uf>_divadm.cnv` | Código de divisão administrativa | Mapeamento da divisão administrativa estadual |
| `<uf>_municgestor.cnv` | Município gestor | Município responsável pela gestão de saúde da localidade |
| `<uf>_*mun.cnv` | Variante por município | Relaciona cada município aos códigos do recorte |

Os `.cnv` seguem o formato texto indexado do TabWin (tipicamente `chave;descrição`), com campos equivalentes a "código" e "nome", mas a estrutura exata varia por arquivo e por versão.

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tabela` | `TABELA` | texto | Nome do arquivo `.cnv` (tabela de conversão do TabWin) de que a linha vem, em minúsculas | — | todos |
| `sequencia` | `SEQUENCIA` | inteiro | Número de sequência da categoria dentro do `.cnv` | — | todos |
| `nivel` | `NIVEL` | inteiro | Nível hierárquico da categoria (indentação do `.cnv` dividida por 4; 0 é o nível mais alto) | — | todos |
| `descricao` | `DESCRICAO` | texto | Descrição da categoria (por exemplo, o nome do município ou da região) | — | todos |
| `codigo` | `CODIGO` | texto | Código que pertence à categoria; há uma linha por código (faixas do `.cnv` são expandidas) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/base-territorial-conversao`, particionado por  (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): inteiro: 2, texto: 5.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `base-territorial-conversao.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- os `.cnv` **não são DBF** e exigem leitura própria (parser TabWin) ou conversão prévia; existem múltiplas variantes por recorte no mesmo ZIP (`*`, `*c`, `*mun`, `*n`) com significados distintos; a conversão é **muitos-para-um** (vários códigos antigos convergem para um novo município em fusões) e pode ser **um-para-muitos** em desmembramentos, exigindo definir a regra de rateio; e, por ser versionada, recomenda-se fixar a versão usada na análise. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/base-territorial-conversao").glob("**/*.parquet"))
dados = pl.concat(  # períodos diferentes têm colunas e tipos diferentes
    [pl.scan_parquet(a, hive_partitioning=True) for a in arquivos],
    how="diagonal_relaxed",
)

(dados.group_by("uf").agg(pl.len().alias("linhas")).sort("uf").collect())
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Pela linha de comando (`datasus-fetcher`)

```bash
# o que o FTP publica para o dataset (arquivos e tamanho)
datasus-fetcher list base-territorial-conversao

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync base-territorial-conversao -o ./data --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset base-territorial-conversao
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/territorio/conversoes`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Documentação `bases_territoriais.pdf` e `registro_de_alteracoes.pdf`**: `ftp://ftp.datasus.gov.br/territorio/doc`
- **IBGE — Divisão Político-Administrativa**: https://www.ibge.gov.br/geociencias/organizacao-do-territorio.html
- **TabWin — formato de conversão `.cnv`** (aplicativo oficial do DATASUS)
