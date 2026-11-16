---
dataset:
  id: cnes-eq
  fonte: datasus
  titulo: Equipamentos
  resumo: O cnes-eq contém os microdados do arquivo de Equipamentos do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra os equipamentos médico-hospitalares e odontológicos existentes nos estabelecimentos.
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2005-08
    fim: em-curso
  unidade: um tipo de equipamento de um estabelecimento, em uma competência
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
    qt_uso: quantidade
  dados_pessoais:
  - coluna: cpf_cnpj
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Equipamentos (`cnes-eq`)

## Resumo

O `cnes-eq` contém os microdados do arquivo de **Equipamentos** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra os equipamentos médico-hospitalares e odontológicos existentes nos estabelecimentos. Cada registro (linha) representa um **tipo de equipamento** (`TIPEQUIP` + `CODEQUIP`) de um estabelecimento, em uma competência mensal, com as quantidades existente e em uso e os indicadores de disponibilidade para o SUS. É a principal fonte oficial sobre a capacidade tecnológica instalada da rede de saúde.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2005-08 a 2026-09 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 6857 arquivos (~1,6 GB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Não
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`)
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/EQ` | `EQ` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `EQSP2401.dbc` — `EQ` (Equipamentos), `SP` (UF), `24` (ano), `01` (mês). Há também `EQBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-eq/2024-01/cnes-eq_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Equipamentos — EQ*.dbf") e `TAB_CNES.zip` (domínios de tipo/código de equipamento).

## Conteúdo

O arquivo `EQ` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS e alimentado pelos estabelecimentos no SCNES. Os equipamentos cadastrados são pré-requisito para habilitação de serviços e para o faturamento de diversos procedimentos (por exemplo, imagem, diálise, radioterapia e exames laboratoriais) e são usados na regulação e no planejamento da oferta de tecnologia em saúde.

O **evento gerador** é a declaração dos equipamentos na FCES/SCNES a cada competência. A **unidade de análise é o tipo de equipamento de um estabelecimento na competência** (`CNES` + `TIPEQUIP` + `CODEQUIP` + `COMPETEN`). `QT_EXIST` é a quantidade existente, `QT_USO` a efetivamente em uso, e `IND_SUS`/`IND_NSUS` indicam se o equipamento está ou não disponível para o SUS. O tipo (`TIPEQUIP`) agrupa grandes categorias (diagnóstico por imagem, métodos gráficos, infraestrutura, equipamentos para manutenção da vida, etc.) e `CODEQUIP` detalha o item.

A série histórica começa em agosto de 2005 e as categorias de equipamentos evoluíram com a incorporação tecnológica e com revisões das tabelas de domínio. Não há diretório preliminar.

Aplicações analíticas típicas: disponibilidade de tomógrafos, ressonâncias, mamógrafos e outros equipamentos de imagem por região, equipamentos para atenção oncológica e nefrológica, identificação de equipamentos ociosos (`QT_EXIST - QT_USO`), apoio à política de incorporação tecnológica e à regulação de acesso a exames de alta complexidade.

### Cobertura observada

- Índice do FTP (2026-10): 6857 arquivos, de 2005-08 a 2026-09, 27 UF(s) com arquivos, última atualização em 2026-10-15.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2005-11 a 2026-01), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `TIPEQUIP` | String (1) | Código do tipo/grupo do equipamento |
| `CODEQUIP` | String (2) | Código do equipamento dentro do tipo |
| `QT_EXIST` | Inteiro | Quantidade existente do equipamento |
| `QT_USO` | Inteiro | Quantidade em uso do equipamento |
| `IND_SUS` | String (1) | Indicador de disponibilidade para o SUS: 1 - Sim, 0 - Não |
| `IND_NSUS` | String (1) | Indicador de equipamento não disponível para o SUS: 1 - Sim, 0 - Não |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `NATUREZA` | String (2) | Código da natureza da organização |
| `TPGESTAO` | String (1) | Tipo de gestão de saúde |
| `PF_PJ` | String (1) | Indicador de pessoa: 1 - Física, 3 - Jurídica |
| `NAT_JUR` | String (4) | Natureza jurídica |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `cnes` | `CNES` | texto | Número nacional do estabelecimento de saúde | — | todos |
| `codufmun` | `CODUFMUN` | texto | Código do município do estabelecimento UF+ MUNIC (sem dígito) | — | todos |
| `regsaude` | `REGSAUDE` | texto | Código da região de saúde | — | todos |
| `micr_reg` | `MICR_REG` | texto | Código da micro-região de saúde NOAS | — | todos |
| `distrsan` | `DISTRSAN` | texto | Código do distrito sanitário | — | todos |
| `distradm` | `DISTRADM` | texto | Código do distrito administrativo | — | todos |
| `tpgestao` | `TPGESTAO` | texto | Gestão de saúde | — | todos |
| `pf_pj` | `PF_PJ` | texto | Indicador de pessoa: 1-Física3-Jurídica | — | todos |
| `cpf_cnpj` | `CPF_CNPJ` | texto | CPF, caso pessoa física OU CNPJ, caso pessoa jurídica | — | todos |
| `niv_dep` | `NIV_DEP` | texto | Grau de dependência, onde: 1-Individual 3-Mantida | — | todos |
| `cnpj_man` | `CNPJ_MAN` | texto | CNPJ da mantenedora do Estabelecimento | — | todos |
| `esfera_a` | `ESFERA_A` | texto | Código da esfera administrativa | — | todos |
| `atividad` | `ATIVIDAD` | texto | Código da atividade de ensino | — | todos |
| `retencao` | `RETENCAO` | texto | Código de retenção de tributos | — | todos |
| `natureza` | `NATUREZA` | texto | Código da natureza da organização | — | todos |
| `clientel` | `CLIENTEL` | texto | Código de fluxo da clientela | — | todos |
| `tp_unid` | `TP_UNID` | texto | Tipo de unidade | — | todos |
| `turno_at` | `TURNO_AT` | texto | Código de turno de atendimento | — | todos |
| `niv_hier` | `NIV_HIER` | texto | Código do nível de hierarquia | — | todos |
| `terceiro` | `TERCEIRO` | texto | O estabelecimento é terceiro: 1-Sim 0-Não | — | todos |
| `tipequip` | `TIPEQUIP` | texto | Código do tipo do equipamento | — | todos |
| `codequip` | `CODEQUIP` | texto | Código do equipamento | — | todos |
| `qt_exist` | `QT_EXIST` | inteiro | Quantidade existente do equipamento | — | todos |
| `qt_uso` | `QT_USO` | inteiro | Quantidade em uso do equipamento | — | todos |
| `ind_sus` | `IND_SUS` | texto | Indicador de disponibilidade para o SUS, onde: 1 =SIM 0 = NÃO | — | todos |
| `ind_nsus` | `IND_NSUS` | texto | Indicador de EQUIPAMENTO NÃO DISPONÍVEL para o SUS, onde: 1 = SIM 0 = NÃO | — | todos |
| `competen` | `COMPETEN` | texto | Ano e Mês de competência da informação (AAAAMM) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `nat_jur` | `NAT_JUR` | texto | Natureza Jurídica de Serviço Especializado - Nomenclatura (SR*.dbf) | — | 2016-04 a 2026-01 |

## No lake

- **Dataset no lake:** `datasus/cnes-eq`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): inteiro: 2, texto: 28.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `cnes-eq.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- no leiaute `EQ` as quantidades `QT_EXIST`/`QT_USO` aparecem como texto (`CHAR(3)`), exigindo conversão cuidadosa para inteiro; como no `LT`, a granularidade é tipo–item, exigindo agregação por estabelecimento; `IND_SUS` e `IND_NSUS` podem ser inconsistentes e requerem validação; e as tabelas de domínio de equipamentos são atualizadas periodicamente, de modo que análises históricas longas precisam mapear códigos ao longo do tempo. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 1 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/cnes-eq/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "mes", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "mes", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-eq
quantilica datasus list cnes-eq

# 2. Baixar microdados de cnes-eq (uf+yearmonth)
quantilica datasus sync cnes-eq -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-eq -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-eq -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-eq/2024-01/cnes-eq_202401-sp@20261015.dbc", clean=True)

# Equipamentos em uso disponíveis para o SUS por grupo
eq = (
    qdf.filter(pl.col("ind_sus") == "1")
    .group_by("tipequip")
    .agg(pl.col("qt_uso").sum().alias("em_uso_sus"))
    .sort("em_uso_sus", descending=True)
)
print(eq)
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EQ`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout EQ) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
