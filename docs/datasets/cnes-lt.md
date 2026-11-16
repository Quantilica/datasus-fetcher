---
dataset:
  id: cnes-lt
  fonte: datasus
  titulo: Leitos
  resumo: 'Leitos do DATASUS: um conjunto de leitos de um tipo e especialidade em um estabelecimento, em uma competência.'
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2005-10
    fim: em-curso
  unidade: um conjunto de leitos de um tipo e especialidade em um estabelecimento, em uma competência
  granularidade:
    espacial: estabelecimento de saúde (CNES) e município; um arquivo por UF
    temporal: competência (mês)
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e competência mensal
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 30
  unidades_de_medida:
    qt_exist: quantidade
    qt_contr: quantidade
    qt_sus: quantidade
    qt_nsus: quantidade
  dados_pessoais:
  - coluna: cpf_cnpj
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Leitos (`cnes-lt`)

## Resumo

O `cnes-lt` contém os microdados do arquivo de **Leitos** do Cadastro Nacional de Estabelecimentos de Saúde (CNES). Cada registro (linha) representa um conjunto de leitos de um **tipo e especialidade** (`TP_LEITO` + `CODLEITO`) existente em um estabelecimento, em uma competência mensal, com a quantidade existente, contratada e disponível para o SUS. É a base oficial para dimensionamento da oferta de leitos hospitalares no país.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/LT` | `LT` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `LTSP2401.dbc` — `LT` (Leitos), `SP` (UF), `24` (ano), `01` (mês). Há também `LTBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-lt/<AAAAMM>/cnes-lt_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/cnes-lt/202401/cnes-lt_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Leitos — LT*.dbf") e `TAB_CNES.zip` (domínios de tipo e especialidade de leito).

## Conteúdo

O arquivo `LT` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), sob gestão do Ministério da Saúde/DATASUS e manutenção dos gestores estaduais e municipais. Os leitos são a unidade física de internação e sua declaração no CNES é condição para o faturamento de internações no SIH/SUS e para o planejamento da regulação de vagas.

O **evento gerador** é a declaração das quantidades de leitos por tipo e especialidade na FCES/SCNES a cada competência. A **unidade de análise é o par tipo–especialidade de leito em um estabelecimento na competência** (`CNES` + `TP_LEITO` + `CODLEITO` + `COMPETEN`). O campo `QT_EXIST` registra os leitos existentes, `QT_CONTR` os contratados e `QT_SUS` os disponibilizados ao SUS — a diferença entre eles mede a parcela não ofertada ao sistema público. As categorias de tipo de leito (cirúrgico, clínico, complementar, obstétrico, pediátrico, UTI adulto/neonatal/pediátrica, etc.) estão nas tabelas de domínio do `TAB_CNES.zip`.

A série histórica no FTP inicia em outubro de 2005 e as quantidades refletem o autocadastro mensal do estabelecimento. Não há diretório preliminar. Ao longo dos anos surgiram especialidades e tipos de leito (por exemplo, leitos de UTI COVID-19 durante a pandemia de 2020), alterando as categorias disponíveis.

Aplicações analíticas típicas: oferta de leitos por habitante, taxa de ocupação e de leitos SUS, acompanhamento da capacidade de UTI, planejamento regional de internações, comparação leitos SUS vs. não SUS e integração com o SIH para cálculo de taxas de ocupação e tempo médio de permanência.

### Cobertura observada

- Índice do FTP (2026-10): 6804 arquivos, de 2005-10 a 2026-09, 27 UF(s) com arquivos, última atualização em 2026-10-15.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2005-10 a 2026-06), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `TP_LEITO` | String (2) | Tipo do leito (cirúrgico, clínico, complementar, obstétrico, etc.) |
| `CODLEITO` | String (2) | Especialidade do leito |
| `QT_EXIST` | Inteiro | Quantidade de leitos existentes |
| `QT_CONTR` | Inteiro | Quantidade de leitos contratados |
| `QT_SUS` | Inteiro | Quantidade de leitos disponíveis para o SUS |
| `TPGESTAO` | String (1) | Tipo de gestão de saúde |
| `PF_PJ` | String (1) | Indicador de pessoa: 1 - Física, 3 - Jurídica |
| `NIV_DEP` | String (1) | Grau de dependência: 1 - Individual, 3 - Mantida |
| `NATUREZA` | String (2) | Código da natureza da organização |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `TERCEIRO` | String (1) | O estabelecimento é terceiro: 1 - Sim, 0 - Não |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `cnes` | `CNES` | texto | Número nacional do estabelecimento de saúde | — | todos |
| `codufmun` | `CODUFMUN` | texto | Código do município do estabelecimento UF+ MUNIC (sem dígito) | — | todos |
| `regsaude` | `REGSAUDE` | texto | Código da região de saúde | — | todos |
| `micr_reg` | `MICR_REG` | texto | Código da micro-região de saúde | — | todos |
| `distrsan` | `DISTRSAN` | texto | Código do distrito sanitário | — | todos |
| `distradm` | `DISTRADM` | texto | Código do distrito administrativo | — | todos |
| `tpgestao` | `TPGESTAO` | texto | Gestão de saúde | — | todos |
| `pf_pj` | `PF_PJ` | texto | Indicador de pessoa: 1-Física 3-Jurídica | — | todos |
| `cpf_cnpj` | `CPF_CNPJ` | texto | CPF do Estabelecimento, caso pessoa física OU CNPJ, caso pessoa jurídica | — | todos |
| `niv_dep` | `NIV_DEP` | texto | Grau de dependência: 1-Individual 3-Mantida | — | todos |
| `cnpj_man` | `CNPJ_MAN` | texto | CNPJ da mantenedora do Estabelecimento | — | todos |
| `esfera_a` | `ESFERA_A` | texto | Código da esfera administrativa | — | todos |
| `atividad` | `ATIVIDAD` | texto | Código da atividade de ensino | — | todos |
| `retencao` | `RETENCAO` | texto | Código de retenção de tributos | — | todos |
| `natureza` | `NATUREZA` | texto | Código da natureza da organização | — | todos |
| `clientel` | `CLIENTEL` | texto | Código de fluxo da clientela | — | todos |
| `tp_unid` | `TP_UNID` | texto | Tipo de unidade (Estabelecimento) | — | todos |
| `turno_at` | `TURNO_AT` | texto | Código de turno de atendimento | — | todos |
| `niv_hier` | `NIV_HIER` | texto | Código do nível de hierarquia | — | todos |
| `terceiro` | `TERCEIRO` | texto | O estabelecimento é terceiro: 1-Sim 0-Não | — | todos |
| `tp_leito` | `TP_LEITO` | texto | Tipo do LEITO | — | todos |
| `codleito` | `CODLEITO` | texto | Especialidade do LEITO | — | todos |
| `qt_exist` | `QT_EXIST` | inteiro | Quantidade de leitos existentes | — | todos |
| `qt_contr` | `QT_CONTR` | inteiro | Quantidade de leitos contratados | — | todos |
| `qt_sus` | `QT_SUS` | inteiro | Quantidade de leitos para o SUS | — | todos |
| `qt_nsus` | `QT_NSUS` | inteiro | Quantidade de leitos não SUS | — | todos |
| `competen` | `COMPETEN` | texto | Ano e Mês de competência da informação (AAAAMM) de Equipamentos - Nomenclatura (EQ*.dbf) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `nat_jur` | `NAT_JUR` | texto | Natureza Jurídica | — | 2016-02 a 2026-06 |

## No lake

- **Dataset no lake:** `datasus/cnes-lt`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): inteiro: 4, texto: 26.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `cnes-lt.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- a granularidade é tipo+especialidade, portanto a soma de `QT_EXIST` por estabelecimento exige agregação; `QT_SUS` pode ser menor que `QT_CONTR` e `QT_EXIST` (nem todo leito é ofertado ao SUS); categorias de leito mudam com o tempo (novos tipos de UTI) e exigem os domínios atualizados de `TAB_CNES.zip`; e o autocadastro pode apresentar inconsistências que precisam de validação contra o SIH. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 1 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/cnes-lt").glob("**/*.parquet"))
dados = pl.concat(  # períodos diferentes têm colunas e tipos diferentes
    [pl.scan_parquet(a, hive_partitioning=True) for a in arquivos],
    how="diagonal_relaxed",
)

(
    dados.group_by("ano", "mes", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "mes", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Pela linha de comando (`datasus-fetcher`)

```bash
# o que o FTP publica para o dataset (arquivos e tamanho)
datasus-fetcher list cnes-lt

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync cnes-lt -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset cnes-lt
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/LT`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout LT) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
