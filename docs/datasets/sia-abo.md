---
dataset:
  id: sia-abo
  fonte: datasus
  titulo: APAC Acompanhamento Pós Cirurgia Bariátrica
  resumo: sia-abo registra as APAC de Acompanhamento Pós-Cirurgia Bariátrica do SIA/SUS
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2014-01
    fim: em-curso
  unidade: uma APAC de acompanhamento pós-cirurgia bariátrica, por competência
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
    colunas: 80
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

# APAC Acompanhamento Pós Cirurgia Bariátrica (`sia-abo`)

## Resumo

`sia-abo` registra as **APAC de Acompanhamento Pós-Cirurgia Bariátrica** do SIA/SUS: cada linha é a cobrança mensal de uma APAC que financia o seguimento multiprofissional de longo prazo do paciente após a cirurgia bariátrica, com os mesmos campos `AB_*` do `sia-ab` e campos adicionais de adesão ao seguimento.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf / yearmonth`
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2014-01 a 2026-07 (conforme `index.json`; 18 UFs com arquivos; última atualização no FTP em 2026-09-14)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 1.607 arquivos (~38,6 MB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Não
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SIASUS/200801_/Doc`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SIASUS/200801_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `ABO` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `ABOSP2401.dbc` — `ABO` (APAC Acompanhamento Pós-Cirurgia Bariátrica) + `SP` (UF) + `24` (ano) + `01` (mês). Prefixo de 3 letras: não confunda com `AB`.
- **No armazenamento local do `datasus-fetcher`**: `data/sia-abo/<AAAAMM>/sia-abo_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sia-abo/202401/sia-abo_ac_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## Conteúdo

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **seguimento pós-operatório** (consultas, suplementação e orientação nutricional, atividade física) autorizado por APAC aos pacientes operados pelo SUS. A unidade de análise é a **APAC por competência**. A Autorização de Procedimentos de Alta Complexidade/Custo (APAC) é o instrumento de autorização e cobrança de procedimentos ambulatoriais de alta complexidade ou de uso continuado: o tratamento é autorizado por um gestor com validade de até três competências, e cada mês de cobrança gera uma linha no arquivo. A chave do registro é o número da APAC (`AP_AUTORIZ`, 13 dígitos) combinado com a competência (`AP_CMP`/`AP_MVM`); a APAC subsequente de um mesmo tratamento referencia a anterior em `AP_APACANT`. Além do IMC e do vínculo com a internação cirúrgica (`AB_NUMAIH`), o leiaute inclui comorbidades (`AP_COMORB`, `AP_CID_C1…C5`, `AP_CID_CO`), uso de medicamentos/polivitamínico (`AP_MEDICAM`, `AP_POLIVIT`), atividade física (`AP_ATV_FIS`) e adesão (`AP_ADESAO`).

No FTP cobre 2014-01 a 2026-07 e sucede o `sia-ab` na prática, após a reformulação da linha de cuidado em 2013 (Portarias GM/MS nº 424 e nº 425/2013), que determinou o acompanhamento pós-operatório obrigatório. São 79 colunas (as maiores do grupo de APACs bariátricas) e arquivos de 18 UFs. O campo `AP_NATJUR` (natureza jurídica) está presente, assim como os campos de segundo procedimento (`AB_PRCAIH2…6`, `AB_T_PRC2…6`).

Aplicações: monitoramento da adesão ao seguimento pós-bariátrico, uso de polivitamínicos e atividade física, comorbidades associadas e tempo de acompanhamento (`AB_MESACOM`/`AB_ANOACOM`); estimativa do custo da linha de cuidado; avaliação da cobertura do seguimento por serviço habilitado; análise de desfechos (`AP_OBITO`, `AP_ALTA`, `AP_TRANSF`, `AP_MOTSAI`) em estudos de coorte pós-bariátrica quando ligado ao SIH.

### Cobertura observada

- Índice do FTP (2026-10): 1621 arquivos, de 2014-01 a 2026-08, 18 UF(s) com arquivos, última atualização em 2026-10-30.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2014-08 a 2026-01), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

79 colunas no arquivo de 2024-01 (`ABOAC2401.dbc`): campos comuns `AP_*` mais `AB_*` e indicadores de seguimento.

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
| `AB_IMC` | String/Inteiro | Índice de massa corporal do paciente. |
| `AB_PROCAIH / AB_NUMAIH / AB_DTCIRUR` | String / String / AAAAMMDD | Procedimento, AIH e data da cirurgia bariátrica de origem. |
| `AB_PRCAIH2…6 / AB_T_PRC2…6` | String | Procedimentos adicionais da internação cirúrgica e respectivos tipos. |
| `AB_MESACOM / AB_ANOACOM` | String | Mês e ano de acompanhamento pós-operatório. |
| `AP_COMORB / AP_CID_C1…C5 / AP_CID_CO` | String | Indicador de comorbidade (`S`/`N`) e CIDs das comorbidades. |
| `AP_MEDICAM / AP_POLIVIT / AP_ATV_FIS / AP_REG_PES / AP_ADESAO` | String | Indicadores (códigos do Informe Técnico) de uso de medicamentos, polivitamínico, atividade física, registro de peso e adesão ao seguimento. |

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
| `ap_vl_ap` | `AP_VL_AP` | decimal(20,2) | Valor Total da APAC Aprovado | — | todos |
| `ap_ufmun` | `AP_UFMUN` | texto | Código da Unidade da Federação + Código do Município do Estabelecimento | — | todos |
| `ap_tpups` | `AP_TPUPS` | texto | Tipo de Estabelecimento | — | todos |
| `ap_tppre` | `AP_TPPRE` | texto | Tipo de prestador do estabelecimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
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
| `ap_tpatend` | `AP_TPATEND` | texto | Tipo de atendimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_tpapac` | `AP_TPAPAC` | texto | Indica se a APAC é 1 - inicial, 2 - continuidade, 3 - única | — | todos |
| `ap_motsai` | `AP_MOTSAI` | texto | Motivo de Saída e Permanência | — | todos |
| `ap_obito` | `AP_OBITO` | texto | Indicador de Óbito | — | todos |
| `ap_encerr` | `AP_ENCERR` | texto | Indicador de Encerramento | — | todos |
| `ap_perman` | `AP_PERMAN` | texto | Indicador de Permanência | — | todos |
| `ap_alta` | `AP_ALTA` | texto | Indicador de Alta | — | todos |
| `ap_transf` | `AP_TRANSF` | texto | Indicador de Transferência | — | todos |
| `ap_dtoocor` | `AP_DTOOCOR` | texto | Data da ocorrência (APAC) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_codemi` | `AP_CODEMI` | texto | Código do Órgão emissor | — | todos |
| `ap_catend` | `AP_CATEND` | texto | Caráter do Atendimento | — | todos |
| `ap_apacan` | `AP_APACAN` | texto | Número da APAC anterior (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_unisol` | `AP_UNISOL` | texto | Código do Estabelecimento solicitante no CNES (Cadastro Nacional de Estabelecimentos de Saúde) | — | todos |
| `ap_dtsolic` | `AP_DTSOLIC` | texto | Data da Solicitação (AAAAMMDD) | — | todos |
| `ap_dtaut` | `AP_DTAUT` | texto | Data da Autorização (AAAAMMDD) | — | todos |
| `ap_cidcas` | `AP_CIDCAS` | texto | CID Causas Associadas | — | todos |
| `co_cidprim` | `CO_CIDPRIM` | texto | CID-10 da doença principal (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_cidsec` | `CO_CIDSEC` | texto | CID-10 da doença secundária (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_etnia` | `AP_ETNIA` | texto | Etnia do paciente | — | todos |
| `ab_imc` | `AB_IMC` | texto | IMC do paciente | — | todos |
| `ab_procaih` | `AB_PROCAIH` | texto | Procedimento do AIH | — | todos |
| `ab_dtcirur` | `AB_DTCIRUR` | texto | Data da Cirurgia | — | todos |
| `ab_numaih` | `AB_NUMAIH` | texto | Número da AIH | — | todos |
| `ab_prcaih2` | `AB_PRCAIH2` | texto | Procedimento do AIH | — | todos |
| `ab_t_prc2` | `AB_T_PRC2` | texto | Procedimento da cirurgia bariátrica (2º registro) — tipo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ab_prcaih3` | `AB_PRCAIH3` | texto | Procedimento do AIH | — | todos |
| `ab_t_prc3` | `AB_T_PRC3` | texto | Procedimento da cirurgia bariátrica (3º registro) — tipo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ab_prcaih4` | `AB_PRCAIH4` | texto | Procedimento da AIH da cirurgia (4º registro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ab_t_prc4` | `AB_T_PRC4` | texto | Procedimento da cirurgia bariátrica (4º registro) — tipo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ab_prcaih5` | `AB_PRCAIH5` | texto | Procedimento da AIH da cirurgia (5º registro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ab_t_prc5` | `AB_T_PRC5` | texto | Procedimento da cirurgia bariátrica (5º registro) — tipo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ab_prcaih6` | `AB_PRCAIH6` | texto | Procedimento da AIH da cirurgia (6º registro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ab_t_prc6` | `AB_T_PRC6` | texto | Procedimento da cirurgia bariátrica (6º registro) — tipo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ab_numaih2` | `AB_NUMAIH2` | texto | Número da AIH | — | todos |
| `ab_dtcirg2` | `AB_DTCIRG2` | texto | Data da Cirurgia | — | todos |
| `ab_mesacom` | `AB_MESACOM` | texto | Número em MESES de Acompanhamento | — | todos |
| `ab_anoacom` | `AB_ANOACOM` | texto | Ano de Acompanhamento | — | todos |
| `ab_pontbar` | `AB_PONTBAR` | texto | Pontuação de Baros12 | — | todos |
| `ab_tabbarr` | `AB_TABBARR` | texto | Tabela de Baros | — | todos |
| `ap_comorb` | `AP_COMORB` | texto | Presença de comorbidades (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_cid_c1` | `AP_CID_C1` | texto | CID-10 da comorbidade 1 (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_cid_c2` | `AP_CID_C2` | texto | CID-10 da comorbidade 2 (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_cid_c3` | `AP_CID_C3` | texto | CID-10 da comorbidade 3 (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_cid_c4` | `AP_CID_C4` | texto | CID-10 da comorbidade 4 (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_cid_c5` | `AP_CID_C5` | texto | CID-10 da comorbidade 5 (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_cid_co` | `AP_CID_CO` | texto | CID-10 da comorbidade (campo consolidado) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_medicam` | `AP_MEDICAM` | texto | Uso de medicamentos no seguimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_polivit` | `AP_POLIVIT` | texto | Uso de polivitamínico no seguimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_atv_fis` | `AP_ATV_FIS` | texto | Prática de atividade física no seguimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_reg_pes` | `AP_REG_PES` | texto | Registro do peso no seguimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ap_adesao` | `AP_ADESAO` | texto | Adesão do paciente ao seguimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `ap_natjur` | `AP_NATJUR` | texto | Código da Natureza Jurídica | — | 2018-10 a 2026-01 |

## No lake

- **Dataset no lake:** `datasus/sia-abo`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): decimal(20,2): 1, texto: 79.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sia-abo.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) é o conjunto "vivo" de seguimento pós-bariátrico, com a mesma lógica de APAC por competência do `sia-ab`; (ii) trate `AB_*` e `AP_*` vazios (`''`) como `null` — muitos campos só são preenchidos em determinadas APAC; (iii) os indicadores `AP_COMORB`, `AP_MEDICAM`, `AP_POLIVIT`, `AP_ATV_FIS`, `AP_REG_PES`, `AP_ADESAO` são códigos de domínio (consulte o Informe Técnico antes de interpretá-los como booleanos); (iv) para contar pacientes use `AP_CNSPCN` (codificado) e não a quantidade de linhas. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 1 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sia-abo/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "mes", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "mes", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sia-abo
quantilica datasus list sia-abo

# 2. Baixar microdados de sia-abo com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sia-abo -o ./data --start 2023-01 --end 2024-12 --regions ac sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sia-abo -o ./data --start 2023-01 --end 2024-12 --regions ac sp --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sia-abo -o ./data/raw --parquet-dir ./data/parquet --start 2023-01 --end 2024-12 --regions ac sp
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sia-abo/202401").glob("sia-abo_ac_202401_*.dbc"))
abo = df.read_dbc(arquivo, dataset="sia-abo")

# Adesão ao seguimento e valor aprovado por estabelecimento
adesao = (
    abo.group_by("ap_adesao")
    .agg(pl.len().alias("apacs"), pl.col("ap_vl_ap").sum().alias("valor"))
    .sort("apacs", descending=True)
)
print(adesao)
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
