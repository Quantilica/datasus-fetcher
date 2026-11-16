---
dataset:
  id: sim-doinf-cid09
  fonte: datasus
  titulo: Declarações de Óbito Infantis CID-9
  resumo: Microdados nacionais do SIM/SVSA-MS com as Declarações de Óbito de menores de 1 ano de 1979 a 1995, codificadas pela CID-9.
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), Coordenação-Geral de Informações e Análise Epidemiológicas (CGIAE)
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '1979'
    fim: '1995'
  unidade: um óbito de menor de 1 ano, de 1979 a 1995 (CID-9)
  granularidade:
    espacial: município de residência e de ocorrência do óbito
    temporal: dia do óbito; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por ano (por UF de residência no dataset `do`; nacional nos recortes)
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 51
  dados_pessoais:
  - coluna: datanasc
    categoria: data de nascimento
  - coluna: baires
    categoria: bairro (código) de residência ou ocorrência
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Declarações de Óbito Infantis CID-9 (`sim-doinf-cid09`)

## Resumo

Microdados nacionais do SIM/SVSA-MS com as Declarações de Óbito de menores de 1 ano de 1979 a 1995, codificadas pela CID-9. Cada linha é um óbito infantil.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `year`
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 1979 a 1995 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 17 arquivos (~60,8 MB); 1 UF(s) na partição; última atualização 2020-01-31
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Não
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SIM/CID9/DOCS`, `/dissemin/publicos/SIM/CID10/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SIM/CID9/TAB`, `/dissemin/publicos/SIM/CID10/TAB`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIM/CID9/DOFET` | `DOINF` | `year2_pattern` — ano com 2 dígitos (arquivo nacional, sem UF) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `DOINF95.dbc` — `DOINF` (óbitos infantis, CID-9) + `95` (ano com 2 dígitos, 1995); arquivo nacional, sem sufixo de UF.
- **No armazenamento local do `datasus-fetcher`**: `data/sim-doinf-cid09/<AAAA>/sim-doinf-cid09_<AAAA>@<AAAAMMDD>.dbc` (ex.: `data/sim-doinf-cid09/1995/sim-doinf-cid09_1995@20260828.dbc`); como não há UF na partição, o nome contém apenas o ano.
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação (`datasus-metadata/metadata/documentation/sim.json`):
    - `/dissemin/publicos/SIM/CID9/DOCS/Docs-Tabs-CID9.zip` (0.7 MB)
    - `/dissemin/publicos/SIM/CID9/DOCS/INTRO.pdf` (0.0 MB)
    - `/dissemin/publicos/SIM/CID9/DOCS/MORT98.HLP` (0.1 MB)
    - `/dissemin/publicos/SIM/CID9/DOCS/MTAB16M.pdf` (2.3 MB)
    - `/dissemin/publicos/SIM/CID10/DOCS/Docs_Tabs_CID10.zip` (2.3 MB)
    - `/dissemin/publicos/SIM/CID10/DOCS/Estrutura_do_SIM_2025.pdf` (0.6 MB)
    - `/dissemin/publicos/SIM/CID10/DOCS/Estrutura_SIM_Anterior.pdf` (0.1 MB)
    - `/dissemin/publicos/SIM/CID10/DOCS/Estrutura_SIM_para_CD.pdf` (0.4 MB)
    - `/dissemin/publicos/SIM/CID10/DOCS/Legislacao_PDF.pdf` (0.9 MB)
    - `/dissemin/publicos/SIM/CID10/DOCS/Portaria.pdf` (0.0 MB)
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/sim.json`):
    - `/dissemin/publicos/SIM/CID9/TAB/OBITOS_CID9_TAB.zip` (0.4 MB)
    - `/dissemin/publicos/SIM/CID10/TAB/CNVS_CID10_v2019.rar` (1.1 MB)
    - `/dissemin/publicos/SIM/CID10/TAB/OBITOS_CID10_TAB.zip` (10.3 MB)

## Conteúdo

O Sistema de Informação sobre Mortalidade (SIM) foi criado pelo Ministério da Saúde em 1975 e hoje é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), por meio da Coordenação-Geral de Informações e Análises Epidemiológicas (CGIAE), com descentralização para as secretarias municipais e estaduais de saúde. Sua finalidade é prover estatísticas vitais de mortalidade para vigilância epidemiológica, planejamento e avaliação de políticas, com cobertura nacional e identificação do local de residência e de ocorrência. O evento gerador é o óbito, registrado na Declaração de Óbito (DO), documento padronizado em todo o país e de preenchimento obrigatório pelo médico (ou, na ausência, por duas testemunhas em cartório). A DO é organizada em nove blocos (identificação, residência, ocorrência, fetal/menor de 1 ano, condições da mãe, causas do óbito, médico, causas externas, cartório e localidade sem médico) e é alimentada nos municípios, com consolidação estadual e federal.

Série histórica pré-1996 de óbitos de menores de 1 ano, na CID-9. Permite reconstruir a queda da mortalidade infantil brasileira nas décadas de 1980 e 1990, ressalvada a elevada subnotificação de óbitos e nascimentos nas regiões Norte e Nordeste.

A principal ruptura histórica é a mudança de classificação: a CID-9 vigorou até 1995 e a CID-10 passou a ser usada a partir de 1996, o que torna as séries de causa de morte não diretamente comparáveis sem compatibilização (por exemplo, por agrupamentos de causas). O FTP organiza os arquivos em dois blocos (`SIM/CID9` e `SIM/CID10`), cada um com seu layout, sua pasta de documentação (`DOCS`) e seus arquivos de tabulação (`TAB`). Portarias que regulam a vigilância de óbitos específicos (maternos, Portaria GM/MS nº 1.119/2008; infantis e fetais, Portaria GM/MS nº 72/2010) e o fluxo de coleta de dados do SIM e do SINASC (Portaria SVS/MS nº 116/2009) ampliaram a investigação e melhoraram a captação. Os dados dos anos mais recentes são divulgados primeiro como preliminares e depois consolidados.

Cobertura no FTP: 1979 a 1995, em um único arquivo nacional por ano. Uso: séries históricas de mortalidade infantil, combinadas com nascidos vivos do SINASC (a partir de 1994 no FTP) ou estimativas demográficas indiretas para o período anterior.

### Cobertura observada

- Índice do FTP (2026-10): 17 arquivos, de 1979 a 1995, 1 UF(s) com arquivos, última atualização em 2020-01-31.
- Conversão local de amostras (5 arquivo(s) Parquet, de 1979 a 1995), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Layout CID-9: **confirme por ano** a presença de cada coluna em `Docs-Tabs-CID9.zip`.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DTOBITO` | String `DDMMAAAA` | Data do óbito. |
| `DTNASC` | String `DDMMAAAA` | Data de nascimento da criança. |
| `IDADE` | Inteiro (código composto) | Idade ao morrer: valores `0xx`/`1xx` (minutos/horas), `2xx` (dias), `3xx` (meses); sempre menor que 1 ano. |
| `SEXO` | Inteiro | Sexo: `1`, `2`, `0`/`9` ignorado. |
| `RACACOR` | String | Raça/cor da criança. |
| `PESO` | String / Inteiro (g) | Peso ao nascer em gramas. |
| `GESTACAO / SEMAGESTAC` | Inteiro | Duração da gestação (faixa e semanas). |
| `GRAVIDEZ / PARTO` | Inteiro | Tipo de gravidez e de parto. |
| `IDADEMAE` | String / Inteiro | Idade da mãe em anos. |
| `ESCMAE` | String | Escolaridade da mãe. |
| `QTDFILVIVO / QTDFILMORT` | Inteiro | Filhos nascidos vivos e perdas fetais anteriores. |
| `CODMUNRES` | String (IBGE, 6) | Município de residência da mãe/criança. |
| `CODMUNOCOR` | String (IBGE, 6) | Município de ocorrência. |
| `LOCOCOR` | String | Local de ocorrência do óbito. |
| `CAUSABAS` | String (CID) | Causa básica do óbito (CID-10 ou CID-9 conforme o dataset). |
| `ASSISTMED / NECROPSIA` | String | Assistência médica e necropsia. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `contador` | `CONTADOR` | texto | Contador: número sequencial do registro no arquivo (campo interno) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `cartorio` | `CARTORIO` | texto | Cartório de registro civil onde o óbito foi registrado (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `registro` | `REGISTRO` | texto | Número do registro do óbito (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `datareg` | `DATAREG` | texto | Data do registro do óbito (DDMMAAAA, leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tipobito` | `TIPOBITO` | texto | Tipo do óbito Óbito fetal: morte antes da expulsão ou da extração completa do corpo da Mãe, independentemente da duração da gravidez. Indica o óbito o fato de o feto, depois da expulsão do corpo materno, não respirar nem apresentar nenhum outro sinal de vida, como batimentos do coração, pulsações do cordão umbilical ou movimentos efetivos dos músculos de contração voluntária | 1-Fetal; 2-Não Fetal | todos |
| `dataobito` | `DATAOBITO` | texto | Data do óbito (DDMMAAAA, leiaute antigo; equivale a `DTOBITO`) | — | todos |
| `estcivil` | `ESTCIVIL` | texto | Estado civil do falecido (leiaute antigo; equivale a `ESTCIV`) | — | todos |
| `sexo` | `SEXO` | texto | Sexo do falecido. “Ignorado” selecionada em casos especiais como cadáveres mutilados, em estado avançado de decomposição, genitália indefinida ou hermafroditismo | M,1 – masculino; F,2 – feminino; I,0,9 - ignorado | todos |
| `datanasc` | `DATANASC` | texto | Data de nascimento do falecido (DDMMAAAA, leiaute antigo; equivale a `DTNASC`) | — | todos |
| `idade` | `IDADE` | texto | Idade do falecido em minutos, horas, dias, meses ou anos | Idade: composto de dois subcampos. - O primeiro, de 1 dígito, indica a unidade da idade (se 1 = minuto, se 2 = hora, se 3 = mês, se 4 = ano, se = 5 idade maior que 100 anos). - O segundo, de dois dígitos, indica a qua... | todos |
| `lococor` | `LOCOCOR` | texto | Local de ocorrência do óbito | 1 – hospital; 2 – outros estabelecimentos de saúde; 3 – domicílio; 4 – via pública; 5 – outros; 6 - aldeia indígena; 9 – ignorado. | todos |
| `codigo` | `CODIGO` | texto | Código do leiaute antigo do SIM sem definição na documentação consultada | — | todos |
| `muniocor` | `MUNIOCOR` | texto | Município de ocorrência do óbito (leiaute antigo; equivale a `CODMUNOCOR`) | — | todos |
| `munires` | `MUNIRES` | texto | Município de residência do falecido (leiaute antigo; equivale a `CODMUNRES`) | — | todos |
| `baires` | `BAIRES` | texto | Bairro de residência do falecido (código) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `areares` | `AREARES` | texto | Área de residência do falecido (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ocupacao` | `OCUPACAO` | texto | Ocupação do falecido (leiaute antigo; equivale a `OCUP`) | — | todos |
| `natural` | `NATURAL` | texto | Município e Unidade da Federação onde o falecido nasceu. Se estrangeiro informar País | Números | todos |
| `instrucao` | `INSTRUCAO` | texto | Escolaridade do falecido (leiaute antigo; equivale a `ESC`) | — | todos |
| `ocuppai` | `OCUPPAI` | texto | Ocupação do pai (leiaute antigo) | — | todos |
| `instrpai` | `INSTRPAI` | texto | Escolaridade do pai (leiaute antigo) | — | todos |
| `ocupmae` | `OCUPMAE` | texto | Tipo de trabalho exercido habitualmente pela Mãe, de acordo com Classificação Brasileira de Ocupações – CBO 2002. No caso da mãe do falecido(a) ser “aposentada”, preencher com a ocupação habitual anterior. | — | todos |
| `idademae` | `IDADEMAE` | texto | Idade da mãe | Números | todos |
| `instrmae` | `INSTRMAE` | texto | Escolaridade da mãe (leiaute antigo; equivale a `ESCMAE`) | — | todos |
| `filhvivos` | `FILHVIVOS` | texto | Número de filhos tidos vivos pela mãe (leiaute antigo; equivale a `QTDFILVIVO`) | — | todos |
| `filhmort` | `FILHMORT` | texto | Número de filhos tidos mortos pela mãe (leiaute antigo; equivale a `QTDFILMORT`) | — | todos |
| `semangest` | `SEMANGEST` | texto | Semanas de gestação (leiaute antigo; equivale a `GESTACAO`) | — | todos |
| `tipograv` | `TIPOGRAV` | texto | Tipo de gravidez (leiaute antigo; equivale a `GRAVIDEZ`) | — | todos |
| `tipoparto` | `TIPOPARTO` | texto | Tipo de parto (leiaute antigo; equivale a `PARTO`) | — | todos |
| `pesonasc` | `PESONASC` | texto | Peso ao nascer em gramas (leiaute antigo; equivale a `PESO`) | — | todos |
| `assistmed` | `ASSISTMED` | texto | Se refere ao atendimento médico continuado que o paciente recebeu, ou não, durante a enfermidade que ocasionou o óbito | 1 – sim; 2 – não; 9 – ignorado | todos |
| `atestante` | `ATESTANTE` | texto | Condição do médico atestante | 1 - Assistente; 2 – Substituto; 3 – IML; 4 – SVO; 5 – Outro | todos |
| `exame` | `EXAME` | texto | Realização de exame | 1 – sim; 2 – não; 9 – ignorado | todos |
| `cirurgia` | `CIRURGIA` | texto | Realização de cirurgia | 1 – sim; 2 – não; 9 – ignorado | todos |
| `necropsia` | `NECROPSIA` | texto | Refere-se a execução ou não de necropsia para confirmação do diagnóstico | 1 – sim; 2 – não; 9 – ignorado | todos |
| `obitofe1` | `OBITOFE1` | texto | Campo do óbito fetal do leiaute antigo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `obitofe2` | `OBITOFE2` | texto | Campo do óbito fetal do leiaute antigo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `causabas` | `CAUSABAS` | texto | Causa básica da DO | *;letras; números; | todos |
| `tipoviol` | `TIPOVIOL` | texto | Tipo de violência (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tipoacid` | `TIPOACID` | texto | Tipo de acidente (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `fontinfo` | `FONTINFO` | texto | Fonte de informação sobre a circunstância do óbito por causa externa (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `acidtrab` | `ACIDTRAB` | texto | Indica se o evento que desencadeou o óbito está relacionado ao processo de trabalho | 1 – sim; 2 – não; 9 – ignorado | todos |
| `locacid` | `LOCACID` | texto | Local de ocorrência do acidente ou da violência (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `critica` | `CRITICA` | texto | Código da crítica aplicada ao registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `numexport` | `NUMEXPORT` | texto | Número de exportação do lote (campo interno) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `crsocor` | `CRSOCOR` | texto | Coordenadoria Regional de Saúde (CRS) do local de ocorrência (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `crsres` | `CRSRES` | texto | Coordenadoria Regional de Saúde (CRS) do local de residência (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ufinform` | `UFINFORM` | texto | UF que informou o registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `racacor` | `RACACOR` | texto | Cor informada pelo responsável pelas informações do falecido | 1 – Branca; 2 – Preta; 3 – Amarela; 4 – Parda; 5 – Indígena | 1995 a 1995 |
| `etnia` | `ETNIA` | texto | Etnia do falecido, quando indígena (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 1995 a 1995 |

## No lake

- **Dataset no lake:** `datasus/sim-doinf-cid09`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): texto: 51.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sim-doinf-cid09.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- **Colunas que não existem em todo o período:** 2 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sim-doinf-cid09/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sim-doinf-cid09
quantilica datasus list sim-doinf-cid09

# 2. Baixar microdados de sim-doinf-cid09 com recorte adequado à partição (year)
quantilica datasus sync sim-doinf-cid09 -o ./data --start 2015 --end 2023

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sim-doinf-cid09 -o ./data --start 2015 --end 2023 --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sim-doinf-cid09 -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2023
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

frame = df.read_dbc(
    "data/sim-doinf-cid09/1995/sim-doinf-cid09_1995@20200131.dbc",
    dataset="sim-doinf-cid09",
)
print(frame.shape)

frame = frame.with_columns(
    pl.col("dtobito").str.to_date("%d%m%Y", strict=False).alias("data_obito"),
)
print(frame.columns)
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID9/DOFET`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde / SVSA — Sistema de Informação sobre Mortalidade (SIM)**: https://www.gov.br/saude/pt-br/composicao/svsa/sistemas-de-informacao/sim
- **Documentação no FTP (`DOCS`)**: `Estrutura_do_SIM_2025.pdf`, `Estrutura_SIM_para_CD.pdf`, `Docs_Tabs_CID10.zip` (CID-10) e `Docs-Tabs-CID9.zip` (CID-9).
- **Manual de Instruções para o Preenchimento da Declaração de Óbito** (Ministério da Saúde/SVS) e legislação em `Legislacao_PDF.pdf` e `Portaria.pdf` (FTP).
- **PCDaS / Fiocruz** — plataforma de dados com séries do SIM: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde / Wiki SIM** (documentação comunitária do SIM e do DATASUS): https://wiki.saude.gov.br/
