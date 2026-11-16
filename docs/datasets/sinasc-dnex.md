---
dataset:
  id: sinasc-dnex
  fonte: datasus
  titulo: Declarações de nascidos vivos no exterior
  resumo: 'Declarações de nascidos vivos no exterior do DATASUS: uma Declaração de Nascido Vivo de nascimento ocorrido no exterior.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), Coordenação-Geral de Informações e Análise Epidemiológicas (CGIAE)
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2014'
    fim: '2024'
  unidade: uma Declaração de Nascido Vivo de nascimento ocorrido no exterior
  granularidade:
    espacial: município de residência da mãe e de ocorrência do nascimento
    temporal: dia do nascimento; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por ano (por UF de residência da mãe)
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 62
  unidades_de_medida:
    consultas: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: dtnasc
    categoria: data de nascimento
  - coluna: horanasc
    categoria: hora do nascimento
  - coluna: dtnascmae
    categoria: data de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Declarações de nascidos vivos no exterior (`sinasc-dnex`)

## Resumo

Microdados do SINASC/SVSA-MS com Declarações de Nascido Vivo de nascimentos ocorridos no exterior, de 2014 a 2024. Cada linha é uma DN registrada para um nascimento fora do Brasil, em um arquivo nacional por ano.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/SINASC/ANT/DOCS`, `/dissemin/publicos/SINASC/NOV/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINASC/1994_1995/Auxiliar`, `/dissemin/publicos/SINASC/1996_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINASC/1996_/Dados/DNRES` | `DNEX` | `year_pattern` — ano com 4 dígitos (arquivo nacional, sem UF) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `DNEX2023.dbc` — `DNEX` (declaração de nascido vivo no exterior) + `2023` (ano com 4 dígitos); arquivo nacional, sem UF.
- **No armazenamento local do `datasus-fetcher`**: `data/sinasc-dnex/<AAAA>/sinasc-dnex_<AAAA>@<AAAAMMDD>.dbc`, por exemplo `data/sinasc-dnex/2024/sinasc-dnex_2024@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação (`datasus-metadata/metadata/documentation/sinasc.json`):
    - `/dissemin/publicos/SINASC/ANT/DOCS/NASC98.HLP` (0.1 MB)
    - `/dissemin/publicos/SINASC/NOV/DOCS/Estrutura_SINASC_para_CD.pdf` (0.0 MB)
    - `/dissemin/publicos/SINASC/NOV/DOCS/Legislacao_PDF.pdf` (0.9 MB)
    - `/dissemin/publicos/SINASC/NOV/DOCS/Portaria.pdf` (0.0 MB)
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/sinasc.json`):
    - `/dissemin/publicos/SINASC/1994_1995/Auxiliar/Arq_Para_Tabulacao_Ate_1995.zip` (0.4 MB)
    - `/dissemin/publicos/SINASC/1996_/Auxiliar/Arq_Para_Tabulacao_A_Partir_1996.zip` (3.2 MB)

## Conteúdo

O Sistema de Informações sobre Nascidos Vivos (SINASC) foi implantado pelo Ministério da Saúde em 1990 e é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), com coleta descentralizada pelas secretarias municipais e estaduais de saúde. Sua finalidade é fornecer dados sobre nascimentos para vigilância e planejamento das ações de saúde da mulher e da criança, em especial indicadores de pré-natal, parto, prematuridade, peso ao nascer e anomalias congênitas, além de ser o denominador oficial de indicadores de mortalidade infantil e materna.

Esta base é um recorte pequeno e específico: nascimentos ocorridos no exterior que, por não terem município de ocorrência no Brasil, ficam fora das tabulações por UF. Ela é publicada à parte para que o total de nascimentos não deixe de contar esses registros. A unidade de análise continua sendo o nascido vivo, com dados da criança e da mãe, mas o campo de local de ocorrência refere-se a outro país.

A DN substituiu a coleta heterogênea feita a partir do registro civil, e o SINASC consolidou-se como a principal fonte de dados de natalidade do país, com cobertura estimada acima de 95% em nível nacional (variável entre regiões). A coleta é regulada pela Portaria SVS/MS nº 116/2009; a DN passou por revisões de leiaute, com inclusão de variáveis como o grupo de Robson e a anomalia congênita detalhada em CID-10. O FTP separa dois períodos: 1994–1995 (layout anterior, prefixo `DNR`) e 1996 em diante.

Uso: reconciliação de totais de nascimentos por ocorrência, estudos de migração e de registros de brasileiros nascidos no exterior. Por ter apenas 11 arquivos (~0,6 MB), é adequado para carga completa e inspeção manual.

### Cobertura observada

- Índice do FTP (2026-10): 11 arquivos, de 2014 a 2024, 1 UF(s) com arquivos, última atualização em 2025-12-23.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2014 a 2024), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Nomes verificados contra o arquivo real `DNEX2024.dbc` (61 colunas, layout próprio do `DNEX`, distinto do `DN`). O país de residência da mãe é `CODPAISRES`; não há coluna de país de ocorrência.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DTNASC` | String `DDMMAAAA` | Data de nascimento. |
| `HORANASC` | String `HHMM` | Hora do nascimento. |
| `SEXO` | String | Sexo do recém-nascido. |
| `PESO` | String (g) | Peso ao nascer em gramas. |
| `APGAR1` / `APGAR5` | String | Apgar no 1º e 5º minuto. |
| `RACACOR` | String | Raça/cor do recém-nascido. |
| `CODMUNNASC` | String (IBGE, 7) | Município de ocorrência do nascimento. |
| `CODESTAB` | String (7) | Estabelecimento de ocorrência. |
| `LOCNASC` | String | Local de ocorrência do nascimento. |
| `CODMUNRES` | String (IBGE, 7) | Município de residência da mãe no Brasil, quando informado. |
| `CODPAISRES` | String (3) | País de residência da mãe. |
| `IDADEMAE` / `DTNASCMAE` | String | Idade e data de nascimento da mãe. |
| `ESCMAE` / `ESCMAE2010` / `SERIESCMAE` | String | Escolaridade da mãe (layouts de escolaridade anterior e de 2010, e série). |
| `ESTCIVMAE` / `RACACORMAE` / `CODOCUPMAE` | String | Estado civil, raça/cor e ocupação (CBO) da mãe. |
| `NATURALMAE` / `CODMUNNATU` / `CODUFNATU` | String | Naturalidade da mãe (país, município e UF). |
| `QTDFILVIVO` / `QTDFILMORT` / `QTDGESTANT` / `QTDPARTNOR` / `QTDPARTCES` | String | Histórico obstétrico: filhos vivos e mortos, gestações e partos normais e cesáreos anteriores. |
| `GESTACAO` / `SEMAGESTAC` / `TPMETESTIM` / `DTULTMENST` | String | Duração da gestação, semanas de gestação, método de estimativa e data da última menstruação. |
| `GRAVIDEZ` / `PARTO` / `TPAPRESENT` / `STTRABPART` / `STCESPARTO` | String | Tipo de gravidez, tipo de parto, apresentação fetal, trabalho de parto induzido e cesárea antes do trabalho de parto. |
| `CONSULTAS` / `CONSPRENAT` / `MESPRENAT` | String | Consultas de pré-natal (faixa e número) e mês de início do pré-natal. |
| `TPROBSON` / `PARIDADE` / `KOTELCHUCK` | String | Classificação de Robson, paridade e índice de Kotelchuck. |
| `IDANOMAL` / `CODANOMAL` | String | Indicador de anomalia congênita e anomalia em CID-10 (capítulo XVII). |
| `IDADEPAI` | String | Idade do pai. |
| `DTCADASTRO` / `DTRECEBIM` / `DTRECORIGA` / `DTDECLARAC` | String `DDMMAAAA` | Datas de cadastro, recebimento, recebimento original e declaração. |
| `NUMEROLOTE` / `VERSAOSIST` / `CONTADOR` / `DIFDATA` | String | Controle do sistema: lote, versão, contador e diferença de datas. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `origem` | `ORIGEM` | texto | Origem do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `codestab` | `CODESTAB` | texto | Código do estabelecimento de saúde constante do Cadastro Nacional de Estabelecimento de Saúde | Números | todos |
| `codmunnasc` | `CODMUNNASC` | texto | Código do município de ocorrência do nascimento (IBGE) | — | todos |
| `locnasc` | `LOCNASC` | texto | Local de ocorrência do nascimento: 1 hospital; 2 outro estabelecimento de saúde; 3 domicílio; 4 outros; 9 ignorado | — | todos |
| `idademae` | `IDADEMAE` | texto | Idade da mãe | Números | todos |
| `estcivmae` | `ESTCIVMAE` | texto | Situação conjugal da mãe | — | todos |
| `escmae` | `ESCMAE` | texto | Escolaridade da mãe em anos | 1 – Nenhuma; 2 – de 1 a 3 anos; 3 – de 4 a 7 anos; 4 – de 8 a 11 anos; 5 – 12 anos e mais; 9 – Ignorado | todos |
| `codocupmae` | `CODOCUPMAE` | texto | Ocupação habitual da mãe (CBO) | — | todos |
| `qtdfilvivo` | `QTDFILVIVO` | texto | Número de filhos vivos | Número; 9 - igonorado | todos |
| `qtdfilmort` | `QTDFILMORT` | texto | Número de filhos mortos. Não incluir a criança cujo óbito se notifica na respectiva DO | Número; 9 - igonorado | todos |
| `codmunres` | `CODMUNRES` | texto | Código do município de residência. Em caso de óbito fetal, considerar o município de residência da mãe | Números | todos |
| `gestacao` | `GESTACAO` | texto | Faixas de semanas de gestação | 1 - Menos de 22 semanas; 2 - 22 a 27 semanas; 3 - 28 a 31 semanas; 4 - 32 a 36 semanas; 5 - 37 a 41 semanas; 6 - 42 e + semanas | todos |
| `gravidez` | `GRAVIDEZ` | texto | Tipo de gravidez | 1 – única; 2 – dupla; 3 – tripla e mais; 9 – ignorada | todos |
| `parto` | `PARTO` | texto | Tipo de parto | 1 – vaginal; 2 – cesáreo; 9 – ignorado | todos |
| `consultas` | `CONSULTAS` | inteiro | Número de consultas de pré-natal (categorias) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dtnasc` | `DTNASC` | texto | Data do nascimento do falecido. Em caso de óbito fetal as datas de óbito e nascimento deverão ser iguais. | Data no padrão ddmmaaaa | todos |
| `horanasc` | `HORANASC` | texto | Hora do nascimento | — | todos |
| `sexo` | `SEXO` | texto | Sexo do falecido. “Ignorado” selecionada em casos especiais como cadáveres mutilados, em estado avançado de decomposição, genitália indefinida ou hermafroditismo | M,1 – masculino; F,2 – feminino; I,0,9 - ignorado | todos |
| `apgar1` | `APGAR1` | texto | Índice de Apgar no 1º minuto | — | todos |
| `apgar5` | `APGAR5` | texto | Índice de Apgar no 5º minuto | — | todos |
| `racacor` | `RACACOR` | texto | Cor informada pelo responsável pelas informações do falecido | 1 – Branca; 2 – Preta; 3 – Amarela; 4 – Parda; 5 – Indígena | todos |
| `peso` | `PESO` | texto | Peso ao nascer em gramas | Número (quatro algarismos) | todos |
| `idanomal` | `IDANOMAL` | texto | Indica se foi detectada anomalia congênita (1 sim; 2 não; 9 ignorado) | — | todos |
| `dtcadastro` | `DTCADASTRO` | texto | Data do cadastro do óbito | Data no padrão ddmmaaaa | todos |
| `codanomal` | `CODANOMAL` | texto | Código da anomalia congênita (CID-10, capítulo Q) | — | todos |
| `numerolote` | `NUMEROLOTE` | texto | Número do lote | Números | todos |
| `versaosist` | `VERSAOSIST` | texto | Versão do sistema | Números; . | todos |
| `dtrecebim` | `DTRECEBIM` | texto | Data do recebimento | Data no padrão ddmmaaaa | todos |
| `difdata` | `DIFDATA` | texto | Diferença entre a data de óbito e data do recebimento original da DO ([DTOBITO] – [DTRECORIG]) | Números | todos |
| `dtrecoriga` | `DTRECORIGA` | texto | Campo Criado no Tratamento para Data do recebimento original | Data no padrão ddmmaaaa | todos |
| `naturalmae` | `NATURALMAE` | texto | Naturalidade da mãe (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `codmunnatu` | `CODMUNNATU` | texto | Código do município de naturalidade do falecido. | Números | todos |
| `codufnatu` | `CODUFNATU` | texto | Código da UF de naturalidade da mãe (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `escmae2010` | `ESCMAE2010` | texto | Escolaridade 2010. Nível da última série concluída pela mãe | 0 – Sem escolaridade; 1 – Fundamental I (1ª a 4ª série); 2 – Fundamental II (5ª a 8ª série); 3 – Médio (antigo 2º Grau); 4 – Superior incompleto; 5 – Superior completo; 9 – Ignorado | todos |
| `seriescmae` | `SERIESCMAE` | texto | Última série escolar concluída pela mãe | Números de 1 a 8 | todos |
| `dtnascmae` | `DTNASCMAE` | texto | Data de nascimento da mãe | — | todos |
| `racacormae` | `RACACORMAE` | texto | Raça/cor da mãe | — | todos |
| `qtdgestant` | `QTDGESTANT` | texto | Número de gestações anteriores | — | todos |
| `qtdpartnor` | `QTDPARTNOR` | texto | Número de partos vaginais anteriores | — | todos |
| `qtdpartces` | `QTDPARTCES` | texto | Número de partos cesáreos anteriores | — | todos |
| `idadepai` | `IDADEPAI` | texto | Idade do pai em anos | — | todos |
| `dtultmenst` | `DTULTMENST` | texto | Data da última menstruação (DUM) | — | todos |
| `semagestac` | `SEMAGESTAC` | texto | Semanas de gestação com dois algarismos | Números com dois algarismos; 9 - igonorado | todos |
| `tpmetestim` | `TPMETESTIM` | texto | Método usado para estimar a idade gestacional | — | todos |
| `consprenat` | `CONSPRENAT` | texto | Número de consultas de pré-natal (categorias) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `mesprenat` | `MESPRENAT` | texto | Mês de gestação em que o pré-natal começou | — | todos |
| `tpapresent` | `TPAPRESENT` | texto | Tipo de apresentação do recém-nascido (cefálico, pélvico ou transverso) | — | todos |
| `sttrabpart` | `STTRABPART` | texto | Trabalho de parto induzido (1 sim; 2 não; 3 não se aplica) | — | todos |
| `stcesparto` | `STCESPARTO` | texto | Cesárea ocorreu antes do trabalho de parto (1 sim; 2 não; 3 não se aplica) | — | todos |
| `tpnascassi` | `TPNASCASSI` | texto | Nascimento assistido por (médico, enfermeira/obstetriz, parteira ou outro) | — | todos |
| `tpfuncresp` | `TPFUNCRESP` | texto | Função do responsável pelo preenchimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tpdocresp` | `TPDOCRESP` | texto | Tipo de documento do responsável pelo preenchimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dtdeclarac` | `DTDECLARAC` | texto | Data da declaração de nascido vivo | — | todos |
| `escmaeagr1` | `ESCMAEAGR1` | texto | Escolaridade da mãe agregada (ormulário a partir de 2010) | 00 – Sem Escolaridade; 01 – Fundamental I Incompleto; 02 – Fundamental I Completo; 03 – Fundamental II Incompleto; 04 – Fundamental II Completo; 05 – Ensino Médio Incompleto; 06 – Ensino Médio Completo; 07 – Superior ... | todos |
| `stdnepidem` | `STDNEPIDEM` | texto | Indicador de DN do circuito de vigilância epidemiológica (campo interno) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `stdnnova` | `STDNNOVA` | texto | Indicador de formulário novo da DN (campo interno) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `codpaisres` | `CODPAISRES` | texto | Código do país de residência da mãe (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tprobson` | `TPROBSON` | texto | Grupo de Robson (classificação de partos por perfil obstétrico) | — | todos |
| `paridade` | `PARIDADE` | texto | Indica se a mãe teve gestações anteriores (0 nulípara; 1 multípara) | — | todos |
| `kotelchuck` | `KOTELCHUCK` | texto | Índice de Kotelchuck de adequação do pré-natal (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `contador` | `CONTADOR` | texto | Contador: número sequencial do registro no arquivo (campo interno) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinasc-dnex`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): inteiro: 1, texto: 61.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sinasc-dnex.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinasc-dnex").glob("**/*.parquet"))
dados = pl.concat(  # períodos diferentes têm colunas e tipos diferentes
    [pl.scan_parquet(a, hive_partitioning=True) for a in arquivos],
    how="diagonal_relaxed",
)

(dados.group_by("ano").agg(pl.len().alias("linhas")).sort("ano").collect())
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Pela linha de comando (`datasus-fetcher`)

```bash
# o que o FTP publica para o dataset (arquivos e tamanho)
datasus-fetcher list sinasc-dnex

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinasc-dnex -o ./data --start 2020 --end 2024 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinasc-dnex
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1996_/Dados/DNRES`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde / SVSA — Sistema de Informações sobre Nascidos Vivos (SINASC)**: https://www.gov.br/saude/pt-br/composicao/svsa/sistemas-de-informacao/sinasc
- **Documentação no FTP (`DOCS`)**: `Estrutura_SINASC_para_CD.pdf`, `NASC98.HLP` (layout até 1995), `Legislacao_PDF.pdf` e `Portaria.pdf`.
- **Manual de Instruções para o Preenchimento da Declaração de Nascido Vivo** (Ministério da Saúde/SVS).
- **PCDaS / Fiocruz** — plataforma de dados com séries do SINASC: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde** (DATASUS): https://wiki.saude.gov.br/
