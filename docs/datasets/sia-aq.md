---
dataset:
  id: sia-aq
  fonte: datasus
  titulo: APAC de Quimioterapia
  resumo: sia-aq reúne as APAC de Quimioterapia do SIA/SUS
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2008-01
    fim: em-curso
  unidade: uma APAC de quimioterapia, por competência
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
    colunas: 76
  unidades_de_medida:
    ap_vl_ap: R$ (reais)
  dados_pessoais:
  - coluna: ap_cnpjcpf
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  - coluna: ap_cnspcn
    categoria: Cartão Nacional de Saúde (CNS)
  - coluna: ap_ceppcn
    categoria: CEP
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# APAC de Quimioterapia (`sia-aq`)

## Resumo

`sia-aq` reúne as **APAC de Quimioterapia** do SIA/SUS: cada linha é a cobrança mensal de uma APAC oncológica de tratamento sistêmico, com campos de estadiamento, grau histológico, data de identificação patológica, tratamento anterior, esquema quimioterápico e medicamentos.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf / yearmonth`
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2008-01 a 2026-07 (conforme `index.json`; 27 UFs com arquivos; última atualização no FTP em 2026-09-14)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 5.979 arquivos (~5,1 GB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Não
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SIASUS/200801_/Doc`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SIASUS/200801_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `AQ` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `AQSP2401.dbc` — `AQ` (APAC de Quimioterapia) + `SP` (UF) + `24` + `01`.
- **No armazenamento local do `datasus-fetcher`**: `data/sia-aq/<AAAAMM>/sia-aq_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sia-aq/202401/sia-aq_ac_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## Conteúdo

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **tratamento quimioterápico do câncer** autorizado por APAC (laudo por CACON/UNACON). A unidade de análise é a **APAC por competência**. A Autorização de Procedimentos de Alta Complexidade/Custo (APAC) é o instrumento de autorização e cobrança de procedimentos ambulatoriais de alta complexidade ou de uso continuado: o tratamento é autorizado por um gestor com validade de até três competências, e cada mês de cobrança gera uma linha no arquivo. A chave do registro é o número da APAC (`AP_AUTORIZ`, 13 dígitos) combinado com a competência (`AP_CMP`/`AP_MVM`); a APAC subsequente de um mesmo tratamento referencia a anterior em `AP_APACANT`. Os campos `AQ_*` descrevem o caso oncológico: `AQ_ESTADI` (estadiamento), `AQ_GRAHIS` (grau histológico), `AQ_DTIDEN` (data de identificação patológica), `AQ_TRANTE` (tratamento anterior), `AQ_CIDINI1…3`/`AQ_DTINI1…3` (tratamentos iniciais), `AQ_CONTTR` (continuidade), `AQ_DTINTR` (início do tratamento), `AQ_ESQU_P1/P2` (esquema), `AQ_TOTMPL`/`AQ_TOTMAU` (meses planejados/autorizados) e `AQ_MED01…10` (medicamentos).

No FTP cobre 2008-01 a 2026-07 (27 UFs, ~5,1 GB). O enquadramento legal inclui a Lei nº 12.732/2012 (início do tratamento oncológico em até 60 dias do diagnóstico) e a Lei nº 13.896/2019 (exames em até 30 dias); a Política Nacional para a Prevenção e Controle do Câncer (Portaria GM/MS nº 874/2013) orienta a rede de atenção oncológica. A APAC oncológica é a principal fonte administrativa de produção de quimioterapia do SUS.

Aplicações: volume de tratamentos de quimioterapia por tipo de câncer (CID `C00–C97`) e estadiamento; oportunidade do tratamento (intervalo entre `AQ_DTIDEN` e `AQ_DTINTR`, referência da Lei 12.732); mapeamento da oferta (CACON/UNACON); gasto com esquemas quimioterápicos; e estudos de acesso e fluxo de pacientes entre municípios (`AP_MUNPCN` vs. `AP_UFMUN`). Para registros de câncer de base populacional, combine com `siscan`/RHC.

### Cobertura observada

- Índice do FTP (2026-10): 6006 arquivos, de 2008-01 a 2026-08, 27 UF(s) com arquivos, última atualização em 2026-10-30.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2008-04 a 2026-04), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

75 colunas no arquivo de 2024-01 (`AQAC2401.dbc`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `AP_MVM / AP_CMP` | String (AAAAMM) | Mês de movimentação (processamento) e mês de competência da APAC. |
| `AP_AUTORIZ` | String (13) | Número da APAC (chave do tratamento); `AP_APACANT` aponta a APAC anterior do mesmo paciente/tratamento. |
| `AP_CODUNI` | String (7) | Código CNES do estabelecimento executor. |
| `AP_GESTAO / AP_UFMUN` | String (6) | Código do gestor e município do estabelecimento (IBGE 6 dígitos). |
| `AP_PRIPAL` | String (10) | Procedimento principal SIGTAP da APAC. |
| `AP_VL_AP` | Float | Valor (R$) aprovado da APAC na competência. |
| `AP_CNSPCN` | String (cifrado) | CNS do paciente — gravado de forma codificada pelo DATASUS no DBF; usar apenas como chave de pareamento, não como CNS legível. |
| `AP_SEXO / AP_COIDADE / AP_NUIDADE` | String | Sexo (`M`/`F`); unidade da idade (`4` = anos) e idade. |
| `AP_RACACOR / AP_ETNIA` | String | Raça/cor (`01`–`05`, `99`) e etnia indígena. |
| `AP_MUNPCN / AP_CEPPCN` | String (6 / 8) | Município de residência e CEP do paciente. |
| `AP_DTINIC / AP_DTFIM` | String AAAAMMDD | Início e fim da validade da APAC no período. |
| `AP_DTSOLIC / AP_DTAUT` | String AAAAMMDD | Datas de solicitação e de autorização. |
| `AP_CIDPRI / AP_CIDSEC / AP_CIDCAS` | String (CID-10) | Diagnóstico principal, secundário e causas associadas (`0000` = não informado). |
| `AP_MOTSAI / AP_OBITO / AP_ALTA / AP_TRANSF / AP_PERMAN / AP_ENCERR` | String | Motivo de saída/cobrança e indicadores de óbito, alta, transferência, permanência e encerramento (flags `0`/`1`). |
| `AP_TPATEN / AP_TPAPAC` | String | Tipo de atendimento e tipo da APAC (`1` inicial, `2` continuidade, `3` única). |
| `AP_NATJUR / AP_TPUPS / AP_TIPPRE` | String | Natureza jurídica, tipo de unidade e tipo de prestador do estabelecimento. |
| `AQ_ESTADI` | String | Estadiamento clínico/patológico (TNM ou estágio agrupado). |
| `AQ_GRAHIS` | String | Grau histológico (`01`–`99`). |
| `AQ_DTIDEN / AQ_DTINTR` | String AAAAMMDD | Data de identificação patológica do câncer e data de início do tratamento. |
| `AQ_TRANTE / AQ_CONTTR` | String | Tratamento anterior e continuidade de tratamento (`S`/`N`). |
| `AQ_CIDINI1…3 / AQ_DTINI1…3` | String | CID e data de tratamentos oncológicos iniciais. |
| `AQ_ESQU_P1 / AQ_ESQU_P2` | String | Esquema quimioterápico (siglas, p.ex. `ACT`). |
| `AQ_TOTMPL / AQ_TOTMAU` | Inteiro | Meses planejados e meses já autorizados. |
| `AQ_MED01…10` | String | Medicamentos do esquema (código e/ou dose). |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `ap_mvm` | `AP_MVM` | texto | Data de Processamento / Movimento (AAAAMM) | — | todos |
| `ap_condic` | `AP_CONDIC` | texto | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado | — | todos |
| `ap_gestao` | `AP_GESTAO` | texto | Código da Unidade de Federação + Código do Município de Gestão, ou UF0000 se o estabelecimento está sob Gestão Estadual | — | todos |
| `ap_coduni` | `AP_CODUNI` | texto | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde) | — | todos |
| `ap_autoriz` | `AP_AUTORIZ` | texto | Número da APAC. Lei de formação: UFAATsssssssd, onde: UF – Unid. da Federação, AA – ano, T – tipo, sssssss – sequencial, d – dígito | — | todos |
| `ap_cmp` | `AP_CMP` | texto | Data de Atendimento ao paciente / Competência (AAAAMM) | — | todos |
| `ap_pripal` | `AP_PRIPAL` | texto | Procedimento Principal da APAC | — | todos |
| `ap_vl_ap` | `AP_VL_AP` | decimal(12,2) | Valor Total da APAC Aprovado | — | todos |
| `ap_ufmun` | `AP_UFMUN` | texto | Código da Unidade da Federação + Código do Município do Estabelecimento | — | todos |
| `ap_tpups` | `AP_TPUPS` | texto | Tipo de Estabelecimento | — | todos |
| `ap_tippre` | `AP_TIPPRE` | texto | Tipo de Prestador | — | todos |
| `ap_mn_ind` | `AP_MN_IND` | texto | Estabelecimento Mantido / Individual | — | todos |
| `ap_cnpjcpf` | `AP_CNPJCPF` | texto | CNPJ do Estabelecimento executante | — | todos |
| `ap_cnpjmnt` | `AP_CNPJMNT` | texto | CNPJ da Mantenedora do estabelecimento ou zeros, caso não a tenha | — | todos |
| `ap_cnspcn` | `AP_CNSPCN` | texto | Número do CNS (Cartão Nacional de Saúde) do paciente | — | todos |
| `ap_coidade` | `AP_COIDADE` | texto | Código da Idade do paciente | — | todos |
| `ap_nuidade` | `AP_NUIDADE` | texto | Número da Idade | — | todos |
| `ap_sexo` | `AP_SEXO` | texto | Sexo do paciente | — | todos |
| `ap_racacor` | `AP_RACACOR` | texto | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação | — | todos |
| `ap_munpcn` | `AP_MUNPCN` | texto | Código da Unidade de Federação + Código Município de Residência do paciente | — | todos |
| `ap_ufnacio` | `AP_UFNACIO` | texto | Código da Nacionalidade do paciente | — | todos |
| `ap_ceppcn` | `AP_CEPPCN` | texto | CEP do endereço do paciente | — | todos |
| `ap_ufdif` | `AP_UFDIF` | texto | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento: 0 = mesma UF; 1 = UF diferente | — | todos |
| `ap_mndif` | `AP_MNDIF` | texto | Indica se o município de residência do paciente é diferente do município de localização do estabelecimento: 0 = mesmo município; 1 = município diferente | — | todos |
| `ap_dtinic` | `AP_DTINIC` | texto | Data de INÍCIO validade (AAAAMMDD) | — | todos |
| `ap_dtfim` | `AP_DTFIM` | texto | Data de FIM validade (AAAAMMDD) | — | todos |
| `ap_tpaten` | `AP_TPATEN` | texto | Tipo de Atendimento de APAC | — | todos |
| `ap_tpapac` | `AP_TPAPAC` | texto | Indica se a APAC é 1 - inicial, 2 - continuidade, 3 - única | — | todos |
| `ap_motsai` | `AP_MOTSAI` | texto | Motivo de Saída e Permanência | — | todos |
| `ap_obito` | `AP_OBITO` | texto | Indicador de Óbito | — | todos |
| `ap_encerr` | `AP_ENCERR` | texto | Indicador de Encerramento | — | todos |
| `ap_perman` | `AP_PERMAN` | texto | Indicador de Permanência | — | todos |
| `ap_alta` | `AP_ALTA` | texto | Indicador de Alta | — | todos |
| `ap_transf` | `AP_TRANSF` | texto | Indicador de Transferência | — | todos |
| `ap_dtocor` | `AP_DTOCOR` | texto | Data de Ocorrência que substitui a data de FIM de validade | — | todos |
| `ap_codemi` | `AP_CODEMI` | texto | Código do Órgão emissor | — | todos |
| `ap_catend` | `AP_CATEND` | texto | Caráter do Atendimento | — | todos |
| `ap_apacant` | `AP_APACANT` | texto | Número APAC Anterior | — | todos |
| `ap_unisol` | `AP_UNISOL` | texto | Código do Estabelecimento solicitante no CNES (Cadastro Nacional de Estabelecimentos de Saúde) | — | todos |
| `ap_dtsolic` | `AP_DTSOLIC` | texto | Data da Solicitação (AAAAMMDD) | — | todos |
| `ap_dtaut` | `AP_DTAUT` | texto | Data da Autorização (AAAAMMDD) | — | todos |
| `ap_cidcas` | `AP_CIDCAS` | texto | CID Causas Associadas | — | todos |
| `ap_cidpri` | `AP_CIDPRI` | texto | CID Principal | — | todos |
| `ap_cidsec` | `AP_CIDSEC` | texto | CID Secundário | — | todos |
| `ap_etnia` | `AP_ETNIA` | texto | Etnia do paciente | — | todos |
| `aq_cid10` | `AQ_CID10` | texto | CID 10 – Topografia | — | todos |
| `aq_linfin` | `AQ_LINFIN` | texto | Linfonodos regionais invadidos (S = Sim; N = Não; 3 = Não Avaliáveis) | — | todos |
| `aq_estadi` | `AQ_ESTADI` | texto | Estádio - UICC (0; 1; 2; 3; 4) | — | todos |
| `aq_grahis` | `AQ_GRAHIS` | texto | Grau Histopatológico | — | todos |
| `aq_dtiden` | `AQ_DTIDEN` | texto | Data da identificação patológica do caso (AAAAMMDD) | — | todos |
| `aq_trante` | `AQ_TRANTE` | texto | Tratamentos anteriores (S = Sim; N = Não) | — | todos |
| `aq_cidini1` | `AQ_CIDINI1` | texto | CID 1º Tratamento anterior | — | todos |
| `aq_dtini1` | `AQ_DTINI1` | texto | Data de início (AAAAMMDD) 1º tratamento anterior | — | todos |
| `aq_cidini2` | `AQ_CIDINI2` | texto | CID 2º Tratamento anterior | — | todos |
| `aq_dtini2` | `AQ_DTINI2` | texto | Data de início (AAAAMMDD) 2º tratamento anterior | — | todos |
| `aq_cidini3` | `AQ_CIDINI3` | texto | CID 3º Tratamento anterior | — | todos |
| `aq_dtini3` | `AQ_DTINI3` | texto | Data de início (AAAAMMDD) 3º tratamento anterior | — | todos |
| `aq_conttr` | `AQ_CONTTR` | texto | Continuidade do tratamento (S = Sim; N = Não) | — | todos |
| `aq_dtintr` | `AQ_DTINTR` | texto | Data de INÍCIO do tratamento solicitado (AAAAMMDD) | — | todos |
| `aq_esqu_p1` | `AQ_ESQU_P1` | texto | ESQUEMA (Sigla ou abrev.) - 5 primeiras posições | — | todos |
| `aq_totmpl` | `AQ_TOTMPL` | texto | Total de MESES Planejados | — | todos |
| `aq_totmau` | `AQ_TOTMAU` | texto | Total de MESES Autorizados | — | todos |
| `aq_esqu_p2` | `AQ_ESQU_P2` | texto | ESQUEMA (Sigla ou abrev.) - 10 últimas posições | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `ap_natjur` | `AP_NATJUR` | texto | Código da Natureza Jurídica | — | 2017-02 a 2026-04 |
| `aq_med01` | `AQ_MED01` | texto | Medicamento do esquema quimioterápico (1º registro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2021-01 a 2026-04 |
| `aq_med02` | `AQ_MED02` | texto | Medicamento do esquema quimioterápico (2º registro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2021-01 a 2026-04 |
| `aq_med03` | `AQ_MED03` | texto | Medicamento do esquema quimioterápico (3º registro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2021-01 a 2026-04 |
| `aq_med04` | `AQ_MED04` | texto | Medicamento do esquema quimioterápico (4º registro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2021-01 a 2026-04 |
| `aq_med05` | `AQ_MED05` | texto | Medicamento do esquema quimioterápico (5º registro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2021-01 a 2026-04 |
| `aq_med06` | `AQ_MED06` | texto | Medicamento do esquema quimioterápico (6º registro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2021-01 a 2026-04 |
| `aq_med07` | `AQ_MED07` | texto | Medicamento do esquema quimioterápico (7º registro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2021-01 a 2026-04 |
| `aq_med08` | `AQ_MED08` | texto | Medicamento do esquema quimioterápico (8º registro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2021-01 a 2026-04 |
| `aq_med09` | `AQ_MED09` | texto | Medicamento do esquema quimioterápico (9º registro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2021-01 a 2026-04 |
| `aq_med10` | `AQ_MED10` | texto | Medicamento do esquema quimioterápico (10º registro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2021-01 a 2026-04 |

## No lake

- **Dataset no lake:** `datasus/sia-aq`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): decimal(12,2): 1, texto: 75.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sia-aq.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) os campos oncológicos (`AQ_*`) vêm como `String` e vazios onde não se aplicam — converta vazios para `null` e `AQ_DTIDEN`/`AQ_DTINTR` para `pl.Date`; (ii) a APAC é mensal e o mesmo paciente aparece em várias competências: conte tratamentos por `AP_AUTORIZ`/`AP_CNSPCN` e use `AP_TPAPAC` (`1` inicial, `2` continuidade); (iii) `AP_CIDPRI` é o CID do câncer — filtre `C*` para tumores malignos; (iv) municípios de residência e do estabelecimento podem ser diferentes (fluxo oncológico). (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 11 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sia-aq/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "mes", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "mes", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sia-aq
quantilica datasus list sia-aq

# 2. Baixar microdados de sia-aq com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sia-aq -o ./data --start 2024-01 --end 2024-12 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sia-aq -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sia-aq -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sia-aq/202401").glob("sia-aq_ac_202401_*.dbc"))
aq = df.read_dbc(arquivo, dataset="sia-aq")

# Tempo entre identificação patológica e início do tratamento (dias)
aq = aq.with_columns(
    pl.col("aq_dtiden").str.to_date("%Y%m%d", strict=False).alias("dt_iden"),
    pl.col("aq_dtintr").str.to_date("%Y%m%d", strict=False).alias("dt_ini"),
).with_columns(
    (pl.col("dt_ini") - pl.col("dt_iden")).dt.total_days().alias("dias_ate_tratamento")
)
print(aq.select("ap_cidpri", "aq_estadi", "dias_ate_tratamento").head())
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
