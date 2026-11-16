---
dataset:
  id: sinasc-dn
  fonte: datasus
  titulo: Declarações de nascidos vivos
  resumo: 'Declarações de nascidos vivos do DATASUS: uma Declaração de Nascido Vivo (um nascimento).'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), Coordenação-Geral de Informações e Análise Epidemiológicas (CGIAE)
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '1994'
    fim: em-curso
  unidade: uma Declaração de Nascido Vivo (um nascimento)
  granularidade:
    espacial: município de residência da mãe e de ocorrência do nascimento
    temporal: dia do nascimento; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por ano (por UF de residência da mãe)
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 93
  unidades_de_medida:
    consultas: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: data_nasc
    categoria: data de nascimento
  - coluna: bairro_mae
    categoria: bairro (código) de residência ou ocorrência
  - coluna: codbainasc
    categoria: bairro (código) de residência ou ocorrência
  - coluna: codbaires
    categoria: bairro (código) de residência ou ocorrência
  - coluna: dtnasc
    categoria: data de nascimento
  - coluna: horanasc
    categoria: hora do nascimento
  - coluna: dtnascmae
    categoria: data de nascimento
  eras:
  - desde: 1996-01
    mudanca: novo diretório e leiaute (os arquivos de 1994 e 1995 têm prefixo `DNR` e leiaute anterior)
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Declarações de nascidos vivos (`sinasc-dn`)

## Resumo

Microdados do Sistema de Informações sobre Nascidos Vivos (SINASC/SVSA-MS) de 1994 em diante, agrupados por UF de residência da mãe. Cada linha representa uma Declaração de Nascido Vivo (um nascimento).

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINASC/ANT/DOCS`, `/dissemin/publicos/SINASC/NOV/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINASC/1994_1995/Auxiliar`, `/dissemin/publicos/SINASC/1996_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINASC/1994_1995/Dados/DNRES` | `DNR` | `uf_year_pattern` — UF (2 letras) + ano com 4 dígitos | `dbc` | Não |
| `/dissemin/publicos/SINASC/1996_/Dados/DNRES` | `DN` | `uf_year_pattern` — UF (2 letras) + ano com 4 dígitos | `dbc` | Não |
| `/dissemin/publicos/SINASC/PRELIM/DNRES` | `DN` | `uf_year_pattern` — UF (2 letras) + ano com 4 dígitos (dados preliminares) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `DNSP2023.dbc` — `DN` (declaração de nascido vivo) + `SP` (UF de residência da mãe) + `2023` (ano do nascimento). Para 1994–1995 o prefixo é `DNR` (ex.: `DNRSP1994.dbc`). Preliminares ficam em `SINASC/PRELIM/DNRES`.
- **No armazenamento local do `datasus-fetcher`**: `data/sinasc-dn/<AAAA>/sinasc-dn_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinasc-dn/2024/sinasc-dn_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
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

O evento gerador é o nascimento vivo, registrado na Declaração de Nascido Vivo (DN), documento padronizado em todo o território, preenchido no estabelecimento de saúde ou, em partos domiciliares, pelo cartório ou parteira tradicional. A unidade de análise é o nascido vivo; cada registro traz dados da criança, da mãe, da gestação e do parto.

A DN substituiu a coleta heterogênea feita a partir do registro civil, e o SINASC consolidou-se como a principal fonte de dados de natalidade do país, com cobertura estimada acima de 95% em nível nacional (variável entre regiões). A coleta é regulada pela Portaria SVS/MS nº 116/2009; a DN passou por revisões de leiaute, com inclusão de variáveis como o grupo de Robson e a anomalia congênita detalhada em CID-10. O FTP separa dois períodos: 1994–1995 (layout anterior, prefixo `DNR`) e 1996 em diante.

Aplicações: taxa bruta de natalidade e fecundidade, proporção de nascimentos prematuros e de baixo peso, proporção de cesáreas e grupos de Robson, adequação do pré-natal (7 ou mais consultas), gravidez na adolescência, nascidos com anomalias congênitas, perfil por raça/cor e escolaridade da mãe, e denominador para mortalidade infantil (`sim-doinf-*`) e materna (`sim-domat-cid10`).

### Cobertura observada

- Índice do FTP (2026-10): 922 arquivos, de 1994 a 2026, 28 UF(s) com arquivos, última atualização em 2026-09-28.
- Conversão local de amostras (5 arquivo(s) Parquet, de 1994 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Eras

- **1996-01**: novo diretório e leiaute (os arquivos de 1994 e 1995 têm prefixo `DNR` e leiaute anterior)

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Colunas do layout 1996 em diante; os anos recentes têm colunas adicionais. Confirme em `Estrutura_SINASC_para_CD.pdf` e use `frame.columns` por ano.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DTNASC` | String `DDMMAAAA` | Data de nascimento. |
| `HORANASC` | String `HHMM` | Hora do nascimento. |
| `SEXO` | Inteiro | Sexo do recém-nascido: `1` masculino, `2` feminino, `0`/`9` ignorado. Em arquivos antigos pode vir como `M`/`F`/`I`. |
| `PESO` | String / Inteiro (g) | Peso ao nascer em gramas. |
| `APGAR1 / APGAR5` | String / Inteiro (0–10) | Índice de Apgar no 1º e no 5º minuto. |
| `RACACOR` | String | Raça/cor do recém-nascido. |
| `CODMUNNASC` | String (IBGE, 6) | Município de ocorrência do nascimento. |
| `CODMUNRES` | String (IBGE, 6) | Município de residência da mãe. |
| `LOCNASC` | String | Local de nascimento: hospital, outro estabelecimento, domicílio, outros. |
| `CODESTAB` | String (CNES, 7) | Estabelecimento de saúde onde ocorreu o nascimento. |
| `IDADEMAE` | Inteiro | Idade da mãe em anos. |
| `ESCMAE` | String | Escolaridade da mãe (anos de estudo, em faixas). |
| `ESTCIVMAE` | String | Estado civil da mãe. |
| `QTDFILVIVO / QTDFILMORT` | Inteiro | Filhos nascidos vivos e perdas fetais/abortos anteriores. |
| `GESTACAO / SEMAGESTAC` | Inteiro | Faixa e número de semanas de gestação. |
| `GRAVIDEZ / PARTO` | Inteiro | Tipo de gravidez (única, dupla…) e de parto (vaginal, cesáreo). |
| `CONSULTAS / CONSPRENAT` | Inteiro | Faixa de consultas de pré-natal (`CONSULTAS`) e número informado (`CONSPRENAT`, layouts recentes). |
| `IDANOMAL / CODANOMAL` | String | Presença de anomalia congênita e sua descrição em CID-10 (capítulo XVII). |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `contador` | `CONTADOR` | texto | Contador: número sequencial do registro no arquivo (campo interno) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `cartorio` | `CARTORIO` | texto | Cartório de registro civil do nascimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `data_cart` | `DATA_CART` | texto | Data de registro no cartório (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `local_ocor` | `LOCAL_OCOR` | texto | Local de ocorrência do nascimento (leiaute antigo; equivale a `LOCNASC`) | — | só em 1994 |
| `muni_ocor` | `MUNI_OCOR` | texto | Município de ocorrência do nascimento (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `crs_ocor` | `CRS_OCOR` | texto | Coordenadoria Regional de Saúde (CRS) de ocorrência do nascimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `estab_ocor` | `ESTAB_OCOR` | texto | Estabelecimento de ocorrência do nascimento (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `data_nasc` | `DATA_NASC` | texto | Data de nascimento (leiaute antigo; equivale a `DTNASC`) | — | só em 1994 |
| `sexo` | `SEXO` | texto | Sexo do falecido. “Ignorado” selecionada em casos especiais como cadáveres mutilados, em estado avançado de decomposição, genitália indefinida ou hermafroditismo | M,1 – masculino; F,2 – feminino; I,0,9 - ignorado | todos |
| `peso` | `PESO` | texto | Peso ao nascer em gramas | Número (quatro algarismos) | todos |
| `raccor` | `RACCOR` | texto | Raça/cor do recém-nascido (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `etnia` | `ETNIA` | texto | Etnia da mãe ou do recém-nascido, quando indígena (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `apgar1` | `APGAR1` | texto | Índice de Apgar no 1º minuto | — | todos |
| `apgar5` | `APGAR5` | texto | Índice de Apgar no 5º minuto | — | todos |
| `gestacao` | `GESTACAO` | texto | Faixas de semanas de gestação | 1 - Menos de 22 semanas; 2 - 22 a 27 semanas; 3 - 28 a 31 semanas; 4 - 32 a 36 semanas; 5 - 37 a 41 semanas; 6 - 42 e + semanas | todos |
| `tipo_grav` | `TIPO_GRAV` | texto | Tipo de gravidez (leiaute antigo; equivale a `GRAVIDEZ`) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `tipo_parto` | `TIPO_PARTO` | texto | Tipo de parto (leiaute antigo; equivale a `PARTO`) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `pre_natal` | `PRE_NATAL` | texto | Número de consultas de pré-natal (leiaute antigo; equivale a `CONSULTAS`) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `idade_mae` | `IDADE_MAE` | texto | Idade da mãe em anos (leiaute antigo; equivale a `IDADEMAE`) | — | só em 1994 |
| `instr_mae` | `INSTR_MAE` | texto | Escolaridade da mãe (leiaute antigo; equivale a `ESCMAE`) | — | só em 1994 |
| `area` | `AREA` | texto | Área de residência da mãe (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `bairro_mae` | `BAIRRO_MAE` | texto | Bairro de residência da mãe (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `muni_mae` | `MUNI_MAE` | texto | Município de residência da mãe (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `crs_mae` | `CRS_MAE` | texto | Coordenadoria Regional de Saúde (CRS) de residência da mãe (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `fil_vivos` | `FIL_VIVOS` | texto | Número de filhos nascidos vivos em gestações anteriores (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `fil_mortos` | `FIL_MORTOS` | texto | Número de filhos nascidos mortos em gestações anteriores (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `fil_abort` | `FIL_ABORT` | texto | Número de perdas fetais e abortos em gestações anteriores (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `num_export` | `NUM_EXPORT` | texto | Número de exportação do lote (campo interno) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `critica` | `CRITICA` | texto | Código da crítica aplicada ao registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1994 |
| `ufinform` | `UFINFORM` | texto | UF que informou o registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 1994 a 2004 |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `locnasc` | `LOCNASC` | texto | Local de ocorrência do nascimento: 1 hospital; 2 outro estabelecimento de saúde; 3 domicílio; 4 outros; 9 ignorado | — | 2004 a 2026 |
| `codestab` | `CODESTAB` | texto | Código do estabelecimento de saúde constante do Cadastro Nacional de Estabelecimento de Saúde | Números | 2004 a 2026 |
| `codbainasc` | `CODBAINASC` | texto | Código do bairro de ocorrência do nascimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2004 |
| `codmunnasc` | `CODMUNNASC` | texto | Código do município de ocorrência do nascimento (IBGE) | — | 2004 a 2026 |
| `idademae` | `IDADEMAE` | texto | Idade da mãe | Números | 2004 a 2026 |
| `estcivmae` | `ESTCIVMAE` | texto | Situação conjugal da mãe | — | 2004 a 2026 |
| `escmae` | `ESCMAE` | texto | Escolaridade da mãe em anos | 1 – Nenhuma; 2 – de 1 a 3 anos; 3 – de 4 a 7 anos; 4 – de 8 a 11 anos; 5 – 12 anos e mais; 9 – Ignorado | 2004 a 2026 |
| `codocupmae` | `CODOCUPMAE` | texto | Ocupação habitual da mãe (CBO) | — | 2004 a 2026 |
| `qtdfilvivo` | `QTDFILVIVO` | texto | Número de filhos vivos | Número; 9 - igonorado | 2004 a 2026 |
| `qtdfilmort` | `QTDFILMORT` | texto | Número de filhos mortos. Não incluir a criança cujo óbito se notifica na respectiva DO | Número; 9 - igonorado | 2004 a 2026 |
| `codbaires` | `CODBAIRES` | texto | Código do bairro de residência da mãe (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2004 |
| `codmunres` | `CODMUNRES` | texto | Código do município de residência. Em caso de óbito fetal, considerar o município de residência da mãe | Números | 2004 a 2026 |
| `gravidez` | `GRAVIDEZ` | texto | Tipo de gravidez | 1 – única; 2 – dupla; 3 – tripla e mais; 9 – ignorada | 2004 a 2026 |
| `parto` | `PARTO` | texto | Tipo de parto | 1 – vaginal; 2 – cesáreo; 9 – ignorado | 2004 a 2026 |
| `consultas` | `CONSULTAS` | inteiro | Número de consultas de pré-natal (categorias) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2004 a 2026 |
| `dtnasc` | `DTNASC` | texto | Data do nascimento do falecido. Em caso de óbito fetal as datas de óbito e nascimento deverão ser iguais. | Data no padrão ddmmaaaa | 2004 a 2026 |
| `racacor` | `RACACOR` | texto | Cor informada pelo responsável pelas informações do falecido | 1 – Branca; 2 – Preta; 3 – Amarela; 4 – Parda; 5 – Indígena | 2004 a 2026 |
| `idanomal` | `IDANOMAL` | texto | Indica se foi detectada anomalia congênita (1 sim; 2 não; 9 ignorado) | — | 2004 a 2026 |
| `codanomal` | `CODANOMAL` | texto | Código da anomalia congênita (CID-10, capítulo Q) | — | 2004 a 2026 |
| `origem` | `ORIGEM` | texto | Origem do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2010 a 2026 |
| `codcart` | `CODCART` | texto | Código do cartório de registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2010 |
| `numregcart` | `NUMREGCART` | texto | Número do registro no cartório (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2010 |
| `dtregcart` | `DTREGCART` | texto | Data de registro no cartório (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2010 |
| `codpaisres` | `CODPAISRES` | texto | Código do país de residência da mãe (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2010 a 2026 |
| `horanasc` | `HORANASC` | texto | Hora do nascimento | — | 2010 a 2026 |
| `dtcadastro` | `DTCADASTRO` | texto | Data do cadastro do óbito | Data no padrão ddmmaaaa | 2010 a 2026 |
| `numerolote` | `NUMEROLOTE` | texto | Número do lote | Números | 2010 a 2026 |
| `versaosist` | `VERSAOSIST` | texto | Versão do sistema | Números; . | 2010 a 2026 |
| `dtrecebim` | `DTRECEBIM` | texto | Data do recebimento | Data no padrão ddmmaaaa | 2010 a 2026 |
| `difdata` | `DIFDATA` | texto | Diferença entre a data de óbito e data do recebimento original da DO ([DTOBITO] – [DTRECORIG]) | Números | 2010 a 2026 |
| `dtrecorig` | `DTRECORIG` | texto | Data de recebimento original do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2010 |
| `naturalmae` | `NATURALMAE` | texto | Naturalidade da mãe (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2010 a 2026 |
| `codmunnatu` | `CODMUNNATU` | texto | Código do município de naturalidade do falecido. | Números | 2010 a 2026 |
| `seriescmae` | `SERIESCMAE` | texto | Última série escolar concluída pela mãe | Números de 1 a 8 | 2010 a 2026 |
| `dtnascmae` | `DTNASCMAE` | texto | Data de nascimento da mãe | — | 2010 a 2026 |
| `racacormae` | `RACACORMAE` | texto | Raça/cor da mãe | — | 2010 a 2026 |
| `qtdgestant` | `QTDGESTANT` | texto | Número de gestações anteriores | — | 2010 a 2026 |
| `qtdpartnor` | `QTDPARTNOR` | texto | Número de partos vaginais anteriores | — | 2010 a 2026 |
| `qtdpartces` | `QTDPARTCES` | texto | Número de partos cesáreos anteriores | — | 2010 a 2026 |
| `idadepai` | `IDADEPAI` | texto | Idade do pai em anos | — | 2010 a 2026 |
| `dtultmenst` | `DTULTMENST` | texto | Data da última menstruação (DUM) | — | 2010 a 2026 |
| `semagestac` | `SEMAGESTAC` | texto | Semanas de gestação com dois algarismos | Números com dois algarismos; 9 - igonorado | 2010 a 2026 |
| `tpmetestim` | `TPMETESTIM` | texto | Método usado para estimar a idade gestacional | — | 2010 a 2026 |
| `consprenat` | `CONSPRENAT` | texto | Número de consultas de pré-natal (categorias) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2010 a 2026 |
| `mesprenat` | `MESPRENAT` | texto | Mês de gestação em que o pré-natal começou | — | 2010 a 2026 |
| `tpapresent` | `TPAPRESENT` | texto | Tipo de apresentação do recém-nascido (cefálico, pélvico ou transverso) | — | 2010 a 2026 |
| `sttrabpart` | `STTRABPART` | texto | Trabalho de parto induzido (1 sim; 2 não; 3 não se aplica) | — | 2010 a 2026 |
| `stcesparto` | `STCESPARTO` | texto | Cesárea ocorreu antes do trabalho de parto (1 sim; 2 não; 3 não se aplica) | — | 2010 a 2026 |
| `tprobson` | `TPROBSON` | texto | Grupo de Robson (classificação de partos por perfil obstétrico) | — | 2010 a 2026 |
| `stdnepidem` | `STDNEPIDEM` | texto | Indicador de DN do circuito de vigilância epidemiológica (campo interno) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2010 a 2026 |
| `stdnnova` | `STDNNOVA` | texto | Indicador de formulário novo da DN (campo interno) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2010 a 2026 |
| `dtrecoriga` | `DTRECORIGA` | texto | Campo Criado no Tratamento para Data do recebimento original | Data no padrão ddmmaaaa | 2017 a 2026 |
| `codufnatu` | `CODUFNATU` | texto | Código da UF de naturalidade da mãe (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2017 a 2026 |
| `escmae2010` | `ESCMAE2010` | texto | Escolaridade 2010. Nível da última série concluída pela mãe | 0 – Sem escolaridade; 1 – Fundamental I (1ª a 4ª série); 2 – Fundamental II (5ª a 8ª série); 3 – Médio (antigo 2º Grau); 4 – Superior incompleto; 5 – Superior completo; 9 – Ignorado | 2017 a 2026 |
| `tpnascassi` | `TPNASCASSI` | texto | Nascimento assistido por (médico, enfermeira/obstetriz, parteira ou outro) | — | 2017 a 2026 |
| `tpfuncresp` | `TPFUNCRESP` | texto | Função do responsável pelo preenchimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2017 a 2026 |
| `tpdocresp` | `TPDOCRESP` | texto | Tipo de documento do responsável pelo preenchimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2017 a 2026 |
| `dtdeclarac` | `DTDECLARAC` | texto | Data da declaração de nascido vivo | — | 2017 a 2026 |
| `escmaeagr1` | `ESCMAEAGR1` | texto | Escolaridade da mãe agregada (ormulário a partir de 2010) | 00 – Sem Escolaridade; 01 – Fundamental I Incompleto; 02 – Fundamental I Completo; 03 – Fundamental II Incompleto; 04 – Fundamental II Completo; 05 – Ensino Médio Incompleto; 06 – Ensino Médio Completo; 07 – Superior ... | 2017 a 2026 |
| `paridade` | `PARIDADE` | texto | Indica se a mãe teve gestações anteriores (0 nulípara; 1 multípara) | — | 2017 a 2026 |
| `kotelchuck` | `KOTELCHUCK` | texto | Índice de Kotelchuck de adequação do pré-natal (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2017 a 2026 |

## No lake

- **Dataset no lake:** `datasus/sinasc-dn`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): inteiro: 1, texto: 92.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sinasc-dn.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- **Colunas que não existem em todo o período:** 85 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinasc-dn").glob("**/*.parquet"))
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
datasus-fetcher list sinasc-dn

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinasc-dn -o ./data --start 2020 --end 2024 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinasc-dn
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1994_1995/Dados/DNRES`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde / SVSA — Sistema de Informações sobre Nascidos Vivos (SINASC)**: https://www.gov.br/saude/pt-br/composicao/svsa/sistemas-de-informacao/sinasc
- **Documentação no FTP (`DOCS`)**: `Estrutura_SINASC_para_CD.pdf`, `NASC98.HLP` (layout até 1995), `Legislacao_PDF.pdf` e `Portaria.pdf`.
- **Manual de Instruções para o Preenchimento da Declaração de Nascido Vivo** (Ministério da Saúde/SVS).
- **PCDaS / Fiocruz** — plataforma de dados com séries do SINASC: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde** (DATASUS): https://wiki.saude.gov.br/
