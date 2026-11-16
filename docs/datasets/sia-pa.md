---
dataset:
  id: sia-pa
  fonte: datasus
  titulo: Produção Ambulatorial
  resumo: 'Produção Ambulatorial do DATASUS: a produção ambulatorial aprovada de um procedimento em um estabelecimento, agregada por competência, ocupação, faixa etária, sexo e município.'
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 1994-07
    fim: em-curso
  unidade: a produção ambulatorial aprovada de um procedimento em um estabelecimento, agregada por competência, ocupação, faixa etária, sexo e município
  granularidade:
    espacial: estabelecimento (CNES) e município de atendimento e de residência; um arquivo por UF
    temporal: competência (mês) e data do atendimento
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e competência mensal (a produção ambulatorial de UFs grandes pode vir em partes com sufixo de letra)
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 77
  unidades_de_medida:
    pa_qtdpro: 'número inteiro: contagem ou código numérico (ver Descrição)'
    pa_qtdapr: 'número inteiro: contagem ou código numérico (ver Descrição)'
    pa_valpro: R$ (reais)
    pa_valapr: R$ (reais)
    pa_dif_val: valor decimal (ver Descrição)
    nu_vpa_tot: valor decimal (ver Descrição)
    nu_pa_tot: valor decimal (ver Descrição)
    pa_vl_cf: R$ (reais)
    pa_vl_cl: R$ (reais)
    pa_vl_inc: R$ (reais)
    pa_vl_crd: R$ (reais)
  dados_pessoais:
  - coluna: pa_cnpjcpf
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  - coluna: pa_cnsmed
    categoria: Cartão Nacional de Saúde (CNS)
  eras:
  - desde: 2008-01
    mudanca: Tabela Unificada SIGTAP (procedimentos de 10 dígitos) e novo diretório (`200801_`); antes, tabela de procedimentos de 8 dígitos
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Produção Ambulatorial (`sia-pa`)

## Resumo

`sia-pa` é a **Produção Ambulatorial** do SIA/SUS: o arquivo principal e mais volumoso do sistema, em que cada linha agrega a produção aprovada de um procedimento SIGTAP em um estabelecimento, por competência, ocupação (CBO), faixa etária, sexo, município de residência e demais atributos, consolidando BPA (consolidado e individualizado) e a produção das APAC e RAAS processadas.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/SIASUS/200801_/Doc`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SIASUS/200801_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/199407_200712/Dados` | `PA` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |
| `/dissemin/publicos/SIASUS/200801_/Dados` | `PA` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) + sufixo opcional de 1 letra (`a`, `b`, `c`…) quando a UF/mês é dividida em mais de um arquivo | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `PASP2401a.dbc` — `PA` (Produção Ambulatorial) + `SP` (UF) + `24` (ano) + `01` (mês) + `a` (parte do arquivo, opcional a partir de 2008). Para a série antiga (1994–2007): `PAAC9407.dbc` (sem sufixo).
- **No armazenamento local do `datasus-fetcher`**: `data/sia-pa/<AAAAMM>/sia-pa_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sia-pa/202401/sia-pa_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## Conteúdo

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **atendimento ambulatorial registrado** no Boletim de Produção Ambulatorial — BPA-C (consolidado: contagens por procedimento, CBO e idade) e BPA-I (individualizado: um registro por atendimento, com CNS do paciente) — e nas APAC/RAAS, todos validados e valorados pelo SIA. A unidade de análise do PA não é o paciente nem o atendimento, e sim a **linha de produção aprovada** (procedimento × estabelecimento × CBO × idade/sexo/município × competência) com quantidade (`PA_QTDPRO`/`PA_QTDAPR`) e valor (`PA_VALPRO`/`PA_VALAPR`) produzidos e aprovados.

O FTP traz duas séries: 1994-07 a 2007-12 (diretório `199407_200712`, leiaute antigo do SIA-SUS com tabela de procedimentos de 8 dígitos) e 2008-01 em diante (`200801_`, Tabela Unificada SIGTAP, 10 dígitos). Para UFs e meses de grande volume, os arquivos de 2008 em diante podem ser divididos em partes com sufixo de letra (`PASP2401a.dbc`, `…b.dbc`, …), como indicado no padrão de nome. Em 2008 a SIGTAP unificou SIA e SIH; o leiaute de 61 campos (2024) inclui indicadores de aprovação (`PA_INDICA`, `PA_CODOCO`), diferenças de valor (`PA_DIF_VAL`) e incentivos (`PA_VL_CF`, `PA_VL_CL`, `PA_VL_INC`). Os arquivos somam cerca de 218 GB.

Aplicações: produção ambulatorial por procedimento, grupo/subgrupo/forma de organização SIGTAP, estabelecimento, município e CBO; cobertura de ações de atenção básica registradas no SIA; consultas especializadas e exames de apoio diagnóstico por 1.000 habitantes; gasto ambulatorial do SUS (`PA_VALAPR`); fluxo de pacientes entre municípios (`PA_MUNPCN` vs. `PA_UFMUN`); avaliação da oferta de serviços para o Plano Diretor de Regionalização e para a programação pactuada e integrada.

### Cobertura observada

- Índice do FTP (2026-10): 10862 arquivos, de 1994-07 a 2026-08, 27 UF(s) com arquivos, última atualização em 2026-10-30.
- Conversão local de amostras (5 arquivo(s) Parquet, de 1994-12 a 2026-04), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Eras

- **2008-01**: Tabela Unificada SIGTAP (procedimentos de 10 dígitos) e novo diretório (`200801_`); antes, tabela de procedimentos de 8 dígitos

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

61 colunas no arquivo de 2024-01 (`PAAC2401.dbc`); o leiaute anterior a 2008 tem menos campos.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `PA_CODUNI` | String (7) | Código CNES do estabelecimento executor. |
| `PA_GESTAO / PA_UFMUN` | String (6) | Código do gestor e município do estabelecimento (IBGE 6 dígitos). |
| `PA_MVM / PA_CMP` | String (AAAAMM) | Mês de movimentação (processamento) e mês de competência da produção. |
| `PA_PROC_ID` | String (10) | Procedimento SIGTAP da produção (campo preservado como `String`). |
| `PA_CBOCOD` | String (6) | CBO da ocupação do profissional executor. |
| `PA_CIDPRI / PA_CIDSEC / PA_CIDCAS` | String (CID-10) | Diagnóstico principal, secundário e causas associadas (`0000` = não informado). |
| `PA_IDADE / IDADEMIN / IDADEMAX / PA_FLIDADE` | String | Idade informada (`999` = ignorada) e faixa de idade permitida pelo procedimento; `PA_FLIDADE` indica compatibilidade. |
| `PA_SEXO` | String | Sexo (`M`, `F`; `0` = não informado/ambos). |
| `PA_RACACOR / PA_ETNIA` | String | Raça/cor (`01`–`05`, `99`) e etnia indígena. |
| `PA_MUNPCN` | String (6) | Município de residência do paciente (`999999` = ignorado → `null`). |
| `PA_QTDPRO / PA_QTDAPR` | Inteiro | Quantidade produzida (apresentada) e aprovada. |
| `PA_VALPRO / PA_VALAPR` | Float | Valor (R$) produzido e aprovado. |
| `PA_TPFIN / PA_SUBFIN / PA_NIVCPL` | String | Tipo e subtipo de financiamento (FAEC, MAC, PAB…) e nível de complexidade. |
| `PA_DOCORIG` | String | Código do documento de origem da produção (BPA consolidado, BPA individualizado, APAC, RAAS…; domínio no Informe Técnico). |
| `PA_CODOCO / PA_INDICA / PA_FLQT / PA_FLER` | String | Código de ocorrência, indicador de aprovação e flags de crítica de quantidade e de erro. |
| `PA_AUTORIZ` | String (13) | Número da APAC (preenchido nas linhas originárias de APAC). |
| `PA_NAT_JUR / PA_TPUPS / PA_TIPPRE / PA_MN_IND` | String | Natureza jurídica, tipo de unidade, tipo de prestador e indicador próprio/mantida do estabelecimento. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `pa_condic` | `PA_CONDIC` | texto | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado | — | todos |
| `pa_gestao` | `PA_GESTAO` | texto | Código da Unidade da Federação7 (IBGE) + Código do Município (IBGE) do Gestor, ou UF0000 se o estabelecimento estiver sob Gestão Estadual | — | todos |
| `pa_coduni` | `PA_CODUNI` | texto | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde)6 | — | todos |
| `pa_datref` | `PA_DATREF` | texto | Data de referência da produção (competência) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 1994-12 a 2004-08 |
| `pa_codpro` | `PA_CODPRO` | texto | Código do procedimento (tabela de procedimentos do leiaute antigo, anterior à SIGTAP) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 1994-12 a 2004-08 |
| `pa_codesp` | `PA_CODESP` | texto | Código da especialidade (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 1994-12 a 2004-08 |
| `pa_tippro` | `PA_TIPPRO` | texto | Tipo de procedimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 1994-12 a 2004-08 |
| `pa_tipate` | `PA_TIPATE` | texto | Tipo de atendimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 1994-12 a 2004-08 |
| `pa_qtdpro` | `PA_QTDPRO` | inteiro ou texto | Quantidade Produzida (APRESENTADA) | — | todos |
| `pa_qtdapr` | `PA_QTDAPR` | inteiro ou texto | Quantidade Aprovada do procedimento | — | todos |
| `pa_indica` | `PA_INDICA` | texto | Indicativo de situação da produção produzida: 0 = não aprovado; 5 = aprovado total; 6 = aprovado parcial | — | todos |
| `pa_tippre` | `PA_TIPPRE` | texto | Tipo de Prestador | — | todos |
| `pa_datpr` | `PA_DATPR` | texto | Data de processamento da produção (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 1994-12 a 2004-08 |
| `pa_valpro` | `PA_VALPRO` | decimal(10,2) ou decimal(20,2) | Valor Produzido (APRESENTADO) | — | todos |
| `pa_valapr` | `PA_VALAPR` | decimal(10,2) ou decimal(20,2) | Valor Aprovado do procedimento | — | todos |
| `pa_ufmun` | `PA_UFMUN` | texto | Unidade da Federação + Código do Município onde está localizado o estabelecimento | — | todos |
| `pa_munat` | `PA_MUNAT` | texto | Município de atendimento (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 1994-12 a 2004-08 |
| `pa_numapa` | `PA_NUMAPA` | texto | Número da APAC (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 1994-12 a 2004-08 |
| `pa_codoco` | `PA_CODOCO` | texto | Código de Ocorrência | — | todos |
| `pa_docorig` | `PA_DOCORIG` | texto | Instrumento de Registro (conforme explicado na página 2) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `pa_fxetar` | `PA_FXETAR` | texto | Faixa etária (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2004-08 |
| `pa_cidpri` | `PA_CIDPRI` | texto | CID9 Principal (APAC ou BPA-I) | — | 2004-08 a 2026-04 |
| `pa_cidsec` | `PA_CIDSEC` | texto | CID Secundário (APAC) | — | 2004-08 a 2026-04 |
| `pa_morfol` | `PA_MORFOL` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2004-08 |
| `pa_cnpj_cc` | `PA_CNPJ_CC` | texto | CNPJ do Órgão que recebeu pela produção por cessão de crédito ou zeros, caso não o tenha | — | 2004-08 a 2026-04 |
| `pa_rcb` | `PA_RCB` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2004-08 |
| `pa_rcbdf` | `PA_RCBDF` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2004-08 |
| `pa_nh` | `PA_NH` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2004-08 |
| `pa_regct` | `PA_REGCT` | texto | Código da Regra Contratual | — | 2010-01 a 2026-04 |
| `pa_incout` | `PA_INCOUT` | texto | Incremento Outros | — | 2010-01 a 2026-04 |
| `pa_incurg` | `PA_INCURG` | texto | Incremento Urgência | — | 2010-01 a 2026-04 |
| `pa_tpups` | `PA_TPUPS` | texto | Tipo de Estabelecimento | — | 2010-01 a 2026-04 |
| `pa_mn_ind` | `PA_MN_IND` | texto | Estabelecimento Mantido / Individual | — | 2010-01 a 2026-04 |
| `pa_cnpjcpf` | `PA_CNPJCPF` | texto | CNPJ do Estabelecimento executante | — | 2010-01 a 2026-04 |
| `pa_cnpjmnt` | `PA_CNPJMNT` | texto | CNPJ da Mantenedora do estabelecimento ou zeros, caso não a tenha | — | 2010-01 a 2026-04 |
| `pa_mvm` | `PA_MVM` | texto | Data de Processamento / Movimento (AAAAMM) | — | 2010-01 a 2026-04 |
| `pa_cmp` | `PA_CMP` | texto | Data da Realização do Procedimento / Competência (AAAAMM) | — | 2010-01 a 2026-04 |
| `pa_proc_id` | `PA_PROC_ID` | texto | Código do Procedimento Ambulatorial | — | 2010-01 a 2026-04 |
| `pa_tpfin` | `PA_TPFIN` | texto | Tipo de Financiamento da produção | — | 2010-01 a 2026-04 |
| `pa_subfin` | `PA_SUBFIN` | texto | Subtipo de Financiamento da produção | — | 2010-01 a 2026-04 |
| `pa_nivcpl` | `PA_NIVCPL` | texto | Complexidade do Procedimento | — | 2010-01 a 2026-04 |
| `pa_autoriz` | `PA_AUTORIZ` | texto | Número da APAC ou número de autorização do BPA-I, conforme o caso. No BPA-I, não é obrigatório, portanto, não é criticado. Lei de formação: UFAATsssssssd, onde: UF – Unid. da Federação, AA – ano, T – tipo, sssssss – sequencial, d – dígito | — | 2010-01 a 2026-04 |
| `pa_cnsmed` | `PA_CNSMED` | texto | Número do CNS (Cartão Nacional de Saúde) do profissional de saúde executante | — | 2010-01 a 2026-04 |
| `pa_cbocod` | `PA_CBOCOD` | texto | Código da Ocupação do profissional na Classificação Brasileira de Ocupações8 (Ministério do Trabalho) | — | 2010-01 a 2026-04 |
| `pa_motsai` | `PA_MOTSAI` | texto | Motivo de saída ou zeros, caso não tenha | — | 2010-01 a 2026-04 |
| `pa_obito` | `PA_OBITO` | texto | Indicador de Óbito (APAC) | — | 2010-01 a 2026-04 |
| `pa_encerr` | `PA_ENCERR` | texto | Indicador de Encerramento (APAC) | — | 2010-01 a 2026-04 |
| `pa_perman` | `PA_PERMAN` | texto | Indicador de Permanência (APAC) | — | 2010-01 a 2026-04 |
| `pa_alta` | `PA_ALTA` | texto | Indicador de Alta (APAC) | — | 2010-01 a 2026-04 |
| `pa_transf` | `PA_TRANSF` | texto | Indicador de Transferência (APAC) | — | 2010-01 a 2026-04 |
| `pa_cidcas` | `PA_CIDCAS` | texto | CID Causas Associadas (APAC) | — | 2010-01 a 2026-04 |
| `pa_catend` | `PA_CATEND` | texto | Caráter de Atendimento (APAC ou BPA-I) | — | 2010-01 a 2026-04 |
| `pa_idade` | `PA_IDADE` | texto | Idade do paciente em anos | — | 2010-01 a 2026-04 |
| `idademin` | `IDADEMIN` | texto | Idade mínima do paciente para realização do procedimento | — | 2010-01 a 2026-04 |
| `idademax` | `IDADEMAX` | texto | Idade máxima do paciente para realização do procedimento | — | 2010-01 a 2026-04 |
| `pa_flidade` | `PA_FLIDADE` | texto | Compatibilidade com a faixa de idade do procedimento (SIGTAP – Sistema de Gerenciamento da Tabela de Procedimentos do SUS): 0 = Idade não exigida; 1 = Idade compatível com o SIGTAP; 2 = Idade fora da faixa do SIGTAP; 3 = Idade inexistente; 4 = Idade EM BRANCO | — | 2010-01 a 2026-04 |
| `pa_sexo` | `PA_SEXO` | texto | Sexo do paciente | — | 2010-01 a 2026-04 |
| `pa_racacor` | `PA_RACACOR` | texto | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação | — | 2010-01 a 2026-04 |
| `pa_munpcn` | `PA_MUNPCN` | texto | Código da Unidade da Federação + Código do Município de residência do paciente ou do estabelecimento, caso não se tenha a identificação do paciente, o que ocorre no (BPA) | — | 2010-01 a 2026-04 |
| `pa_ufdif` | `PA_UFDIF` | texto | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento: 0 = mesma UF; 1 = UF diferente | — | 2010-01 a 2026-04 |
| `pa_mndif` | `PA_MNDIF` | texto | Indica se o município de residência do paciente é diferente do município de localização do estabelecimento: 0 = mesmo município; 1 = município diferente | — | 2010-01 a 2026-04 |
| `pa_dif_val` | `PA_DIF_VAL` | decimal(20,2) | Diferença do Valor Unitário do procedimento praticado na Tabela Unificada com Valor Unitário praticado pelo Gestor da Produção, multiplicado pela Quantidade Aprovada | — | 2010-01 a 2026-04 |
| `nu_vpa_tot` | `NU_VPA_TOT` | decimal(20,2) | Valor Unitário do Procedimento da Tabela VPA | — | 2010-01 a 2026-04 |
| `nu_pa_tot` | `NU_PA_TOT` | decimal(20,2) | Valor Unitário do Procedimento da Tabela SIGTAP | — | 2010-01 a 2026-04 |
| `pa_flqt` | `PA_FLQT` | texto | Indicador de erro de Quantidade Produzida | — | 2010-01 a 2026-04 |
| `pa_fler` | `PA_FLER` | texto | Indicador de erro de corpo da APAC | — | 2010-01 a 2026-04 |
| `pa_etnia` | `PA_ETNIA` | texto | Etnia do paciente | — | 2010-01 a 2026-04 |
| `pa_vl_cf` | `PA_VL_CF` | decimal(20,2) | Valor do Complemento Federal | — | 2017-11 a 2026-04 |
| `pa_vl_cl` | `PA_VL_CL` | decimal(20,2) | Valor do Complemento Local | — | 2017-11 a 2026-04 |
| `pa_vl_inc` | `PA_VL_INC` | decimal(20,2) | Valor do Incremento | — | 2017-11 a 2026-04 |
| `pa_srv_c` | `PA_SRV_C` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2017-11 a 2026-04 |
| `pa_ine` | `PA_INE` | texto | Código de Identificação Nacional de Equipes10, para registrar a atuação das equipes na execução de ações de saúde | — | 2017-11 a 2026-04 |
| `pa_nat_jur` | `PA_NAT_JUR` | texto | Código da Natureza Juridica11 | — | 2017-11 a 2026-04 |
| `pa_fntorc` | `PA_FNTORC` | texto | Fonte orçamentária (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2026-04 |
| `pa_vl_crd` | `PA_VL_CRD` | decimal(20,2) | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-04 |

## No lake

- **Dataset no lake:** `datasus/sia-pa`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): decimal(10,2): 2, decimal(20,2): 9, inteiro: 2, texto: 68.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sia-pa.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) use **aprovado** (`PA_QTDAPR`/`PA_VALAPR`), não produzido, para estimar o que foi pago; linhas com `PA_INDICA`/`PA_FLER` indicando glosa devem ser analisadas à parte; (ii) para atendimentos individualizados não há CNS do paciente; os campos `PA_CNSMED` (CNS do profissional) são codificados; (iii) UF do arquivo = UF do estabelecimento/gestor, não do paciente — use `PA_MUNPCN` para a residência; (iv) as partes `a`, `b`, … de um mesmo mês devem ser concatenadas sem deduplicar; (v) o dataset é enorme (~218 GB): sempre filtre por UF e período e use leitura em pedaços/Parquet; (vi) o 'PA' pré-2008 usa tabela de procedimentos de 8 dígitos (confira `TAB_SIA_199407-199910.zip` etc.) — não misture com a SIGTAP sem crosswalk. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Tipo que varia entre períodos:** `pa_qtdpro`, `pa_qtdapr`, `pa_valpro`, `pa_valapr` aparecem com mais de um tipo nas amostras (por exemplo, inteiro em alguns períodos e texto em outros); leia a coluna `Tipo` do dicionário e converta explicitamente antes de empilhar períodos. Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Colunas que não existem em todo o período:** 63 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sia-pa").glob("**/*.parquet"))
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
datasus-fetcher list sia-pa

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sia-pa -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sia-pa
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
- **Portal DATASUS — SIA/SUS (TabNet)**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/ (Assistência à Saúde → Produção Ambulatorial).
