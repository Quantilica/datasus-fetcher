---
dataset:
  id: sih-rd
  fonte: datasus
  titulo: RD - AIH Reduzida
  resumo: 'RD - AIH Reduzida do DATASUS: uma AIH (Autorização de Internação Hospitalar) aprovada, em uma competência de processamento.'
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 1992-01
    fim: em-curso
  unidade: uma AIH (Autorização de Internação Hospitalar) aprovada, em uma competência de processamento
  granularidade:
    espacial: estabelecimento (CNES) e município de residência do paciente; um arquivo por UF
    temporal: dia da internação e da saída; competência de processamento (mês)
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e competência mensal
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 124
  unidades_de_medida:
    uti_total: dias
    val_sh: R$ (reais)
    val_sp: R$ (reais)
    val_sadt: R$ (reais)
    val_ortp: R$ (reais)
    val_sangue: R$ (reais)
    val_tot: R$ (reais)
    us_sh: US$ (dólares)
    us_sp: US$ (dólares)
    us_sadt: US$ (dólares)
    us_ortp: US$ (dólares)
    us_sangue: US$ (dólares)
    us_tot: US$ (dólares)
    idade: 'número inteiro: contagem ou código numérico (ver Descrição)'
    dias_perm: dias
    cont: 'número inteiro: contagem ou código numérico (ver Descrição)'
    uti_mes_in: dias
    uti_mes_an: dias
    uti_mes_al: dias
    uti_mes_to: dias
    uti_int_in: dias
    uti_int_an: dias
    uti_int_al: dias
    uti_int_to: dias
    val_rn: R$ (reais)
    val_sadtsr: R$ (reais)
    val_transp: R$ (reais)
    val_obsang: R$ (reais)
    val_ped1ac: R$ (reais)
    val_uti: R$ (reais)
    tot_pt_sp: 'número inteiro: contagem ou código numérico (ver Descrição)'
    num_filhos: 'número inteiro: contagem ou código numérico (ver Descrição)'
    diar_acom: dias
    qt_diarias: dias
    val_acomp: R$ (reais)
    rubrica: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sequencia: 'número inteiro: contagem ou código numérico (ver Descrição)'
    val_sh_fed: R$ (reais)
    val_sp_fed: R$ (reais)
    val_sh_ges: R$ (reais)
    val_sp_ges: R$ (reais)
    val_uci: R$ (reais)
  dados_pessoais:
  - coluna: nasc
    categoria: data de nascimento
  - coluna: cep
    categoria: CEP
  - coluna: cpf_aut
    categoria: CPF
  - coluna: gestor_cpf
    categoria: CPF
  eras:
  - desde: 1998-01
    mudanca: a CID-10 passa a ser usada no SIH (informação da documentação do DATASUS; antes, CID-9)
  - desde: 2008-01
    mudanca: 'Tabela Unificada de Procedimentos (SIGTAP): códigos de 10 dígitos e novo diretório/leiaute (`200801_`)'
  - desde: 2015-01
    mudanca: '`DIAG_SECUN` passa a vir preenchido com zeros, conforme o informe técnico'
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# RD - AIH Reduzida (`sih-rd`)

## Resumo

`sih-rd` reúne as **AIH Reduzidas**: o arquivo principal do Sistema de Informações Hospitalares do SUS (SIH/SUS), em que cada linha é uma Autorização de Internação Hospitalar **aprovada e paga** em uma competência de processamento, com dados do paciente, do estabelecimento, do diagnóstico, do procedimento realizado, da permanência e dos valores faturados. É a base mais usada no Brasil para estudar internações financiadas pelo SUS.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/SIHSUS/200801_/Doc`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SIHSUS/200801_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIHSUS/199201_200712/Dados` | `RD` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |
| `/dissemin/publicos/SIHSUS/200801_/Dados` | `RD` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `RDSP2401.dbc` — `RD` (AIH Reduzida) + `SP` (UF de gestão/internação: São Paulo) + `24` (ano 2024) + `01` (mês de competência janeiro). Arquivos de 1992–2007 seguem o mesmo padrão, p.ex. `RDAC9201.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/sih-rd/<AAAAMM>/sih-rd_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sih-rd/202401/sih-rd_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/IT_SIHSUS_1603.pdf` (Informe Técnico do SIHSUS, 57 KB, 2016) é o dicionário oficial de variáveis; `Auxiliar/TAB_SIH.zip` (~6,1 MB, tabelas e conversores `.cnv`/`.def` atuais) e as versões históricas `TAB_SIH_199201-199712.zip`, `TAB_SIH_199801-200307.zip` e `TAB_SIH_200308-200712.zip` trazem as tabelas de procedimentos, CID e códigos usadas em cada fase.

## Conteúdo

O Sistema de Informações Hospitalares do SUS (SIH/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES), com processamento e disseminação a cargo do DATASUS — e tem como finalidade operacionalizar o pagamento das internações realizadas em hospitais públicos e privados conveniados ao SUS. Por ser um sistema de faturamento, cobre apenas a assistência financiada pelo SUS (não inclui saúde suplementar nem internações particulares) e é a principal fonte nacional para estudar morbidade hospitalar, perfil assistencial e gasto hospitalar.

O evento gerador é a **internação hospitalar** formalizada pela Autorização de Internação Hospitalar (AIH). A unidade de análise do RD é a **AIH aprovada** (e não o paciente: o SIH não possui identificador único de pessoa, de modo que reinternações do mesmo indivíduo aparecem como AIH distintas). Cada hospital preenche a Autorização de Internação Hospitalar (AIH) e a remete mensalmente ao gestor municipal/estadual, que a valida e a envia ao DATASUS para processamento na competência (`ANO_CMPT`/`MES_CMPT`). O processamento classifica cada AIH como aprovada (arquivo RD), rejeitada (RJ/ER) e detalha os atos profissionais (SP). O campo `IDENT` distingue a AIH normal (tipo 1) da AIH de continuação/longa permanência (tipo 5), que reaparece em competências sucessivas com o mesmo paciente e deve ser tratada para evitar dupla contagem de internações.

O FTP mantém duas séries contínuas: 1992-01 a 2007-12 (diretório `199201_200712`, antes da Tabela Unificada) e 2008-01 em diante (`200801_`). Marcos relevantes: adoção da CID-10 em substituição à CID-9 (a partir de 1998 no SIH), a implantação da Tabela Unificada de Procedimentos, Medicamentos e OPM do SUS (SIGTAP) a partir de 2008, que alterou os códigos de procedimento (10 dígitos) e o leiaute, e a inclusão de campos de diagnósticos secundários (`DIAGSEC1`–`DIAGSEC9`) e de repasse federal/gestor (`VAL_*_FED`/`VAL_*_GES`) nos leiautes recentes. O mês do arquivo é a **competência de processamento**, não a data da internação: use `DT_INTER`/`DT_SAIDA` para análises temporais clínicas.

Indicadores típicos: taxa de internação por 10.000 habitantes por causa (CID-10 do `DIAG_PRINC`) e por município de residência; internações por condições sensíveis à atenção primária (ICSAP); tempo médio de permanência (`DIAS_PERM`); letalidade hospitalar (`MORTE`); taxa de ocupação de UTI (`UTI_MES_TO`); custo médio por internação e por procedimento (`VAL_TOT`, `VAL_SH`, `VAL_SP`); fluxos de pacientes entre município de residência (`MUNIC_RES`) e de internação (`MUNIC_MOV`); e partos, cesarianas e mortalidade materna/neonatal hospitalar.

### Cobertura observada

- Índice do FTP (2026-10): 11237 arquivos, de 1992-01 a 2026-09, 27 UF(s) com arquivos, última atualização em 2026-11-10.
- Conversão local de amostras (5 arquivo(s) Parquet, de 1992-10 a 2026-08), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Eras

- **1998-01**: a CID-10 passa a ser usada no SIH (informação da documentação do DATASUS; antes, CID-9)
- **2008-01**: Tabela Unificada de Procedimentos (SIGTAP): códigos de 10 dígitos e novo diretório/leiaute (`200801_`)
- **2015-01**: `DIAG_SECUN` passa a vir preenchido com zeros, conforme o informe técnico

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Colunas do leiaute atual (114 campos no arquivo de 2024-01, `RDAC2401.dbc`); o leiaute antes de 2008 é mais enxuto.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `UF_ZI` | String (6) | Código IBGE da UF/município de gestão (zona de informação) do estabelecimento; na prática o código do gestor, p.ex. `120000` para o Acre. |
| `ANO_CMPT / MES_CMPT` | String (4 / 2) | Ano e mês da competência de processamento da AIH (não é a data da internação). |
| `N_AIH` | String (13) | Número da AIH; chave do registro dentro da competência. Mantido como texto. |
| `IDENT` | String (1) | Tipo da AIH: `1` normal; `5` continuação/longa permanência. |
| `CNES` | String (7) | Código CNES do estabelecimento de saúde que realizou a internação. |
| `MUNIC_RES / MUNIC_MOV` | String (6) | Município de residência do paciente / município do estabelecimento (movimento), código IBGE de 6 dígitos. |
| `NASC / IDADE / COD_IDADE` | String AAAAMMDD / Int / String | Data de nascimento; idade; unidade da idade (`2` dias, `3` meses, `4` anos, `5` > 100 anos). |
| `SEXO` | Inteiro | Sexo do paciente (`1` masculino, `3` feminino, `0`/`9` ignorado). |
| `RACA_COR / ETNIA` | String | Raça/cor (`01` branca, `02` preta, `03` parda, `04` amarela, `05` indígena, `99` sem informação) e etnia indígena. |
| `DT_INTER / DT_SAIDA` | String AAAAMMDD → `pl.Date` | Datas de internação e de saída (alta, transferência ou óbito). |
| `PROC_SOLIC / PROC_REA` | String (10) | Procedimento SIGTAP solicitado e efetivamente realizado (principal da internação). |
| `DIAG_PRINC / DIAG_SECUN / DIAGSEC1–9` | String (CID-10) | Diagnóstico principal, secundário e diagnósticos secundários adicionais; `CID_NOTIF`, `CID_ASSO` e `CID_MORTE` completam as causas. |
| `DIAS_PERM / QT_DIARIAS` | Inteiro | Dias de permanência e quantidade de diárias. |
| `UTI_MES_TO / UTI_INT_TO / MARCA_UTI` | Inteiro / String | Total de diárias de UTI no mês e na internação; tipo de leito de UTI utilizado. |
| `VAL_SH / VAL_SP / VAL_SADT / VAL_UTI / VAL_TOT` | Float | Valores (R$) de serviços hospitalares, profissionais, SADT, UTI e total da AIH. |
| `MORTE` | Inteiro | Indicador de óbito durante a internação (`1` sim, `0` não). |
| `CAR_INT / COBRANCA` | String | Caráter da internação (`01` eletiva, `02` urgência …) e motivo de saída/cobrança (`11` alta curado, `41` óbito etc.). |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `uf_zi` | `UF_ZI` | texto | Município Gestor. | — | todos |
| `ano_cmpt` | `ANO_CMPT` | texto | Ano de processamento da AIH, no formato aaaa. | — | todos |
| `mes_cmpt` | `MES_CMPT` | texto | Mês de processamento da AIH, no formato mm. | — | todos |
| `espec` | `ESPEC` | texto | Especialidade do Leito | — | todos |
| `cgc_hosp` | `CGC_HOSP` | texto | CNPJ do Estabelecimento. | — | todos |
| `n_aih` | `N_AIH` | texto | Número da AIH. | — | todos |
| `ident` | `IDENT` | texto | Identificação do tipo da AIH. | — | todos |
| `nasc` | `NASC` | texto | Data de nascimento do paciente (aaaammdd). | — | todos |
| `sexo` | `SEXO` | texto | Sexo do paciente. | — | todos |
| `uti_total` | `UTI_TOTAL` | inteiro | Total de dias de UTI (leiaute antigo, anterior à separação por tipo de UTI) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1992-10 |
| `proc_rea` | `PROC_REA` | texto | Procedimento realizado. | — | todos |
| `val_sh` | `VAL_SH` | decimal(13,2) | Valor de serviços hospitalares. | — | todos |
| `val_sp` | `VAL_SP` | decimal(13,2) | Valor de serviços profissionais. | — | todos |
| `val_sadt` | `VAL_SADT` | decimal(13,2) | Zerado | — | todos |
| `val_ortp` | `VAL_ORTP` | decimal(13,2) | Zerado | — | todos |
| `val_sangue` | `VAL_SANGUE` | decimal(13,2) | Zerado | — | todos |
| `val_tot` | `VAL_TOT` | decimal(14,2) | Valor total da AIH. | — | todos |
| `us_sh` | `US_SH` | decimal(9,2) | Valor de serviços hospitalares em dólar (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1992-10 |
| `us_sp` | `US_SP` | decimal(9,2) | Valor de serviços profissionais em dólar (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1992-10 |
| `us_sadt` | `US_SADT` | decimal(9,2) | Valor de SADT (serviços auxiliares de diagnóstico e terapia) em dólar (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1992-10 |
| `us_ortp` | `US_ORTP` | decimal(9,2) | Valor de órteses e próteses em dólar (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1992-10 |
| `us_sangue` | `US_SANGUE` | decimal(9,2) | Valor de sangue em dólar (leiaute antigo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 1992-10 |
| `us_tot` | `US_TOT` | decimal(10,2) | Valor total, em dólar. | — | todos |
| `dt_inter` | `DT_INTER` | data | Data de internação (AAAAMMDD, convertida para data); o informe técnico a grafa `DI_INTER` | — | todos |
| `dt_saida` | `DT_SAIDA` | data | Data de saída, no formato aaaammdd. | — | todos |
| `diag_princ` | `DIAG_PRINC` | texto | Código do diagnóstico principal (CID10). | — | todos |
| `cobranca` | `COBRANCA` | texto | Motivo de Saída/Permanência | — | todos |
| `natureza` | `NATUREZA` | texto | Natureza jurídica do hospital (com conteúdo até maio/12). Era utilizada a classificação de Regime e Natureza. | — | todos |
| `munic_mov` | `MUNIC_MOV` | texto | Município do Estabelecimento. | — | todos |
| `cod_idade` | `COD_IDADE` | texto | Unidade de medida da idade. | — | todos |
| `idade` | `IDADE` | inteiro | Idade. | — | todos |
| `dias_perm` | `DIAS_PERM` | inteiro | Dias de Permanência. | — | todos |
| `morte` | `MORTE` | texto | Indica Óbito | — | todos |
| `cod_arq` | `COD_ARQ` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 1992-10 a 2002-03 |
| `cont` | `CONT` | inteiro | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 1992-10 a 2002-03 |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `cep` | `CEP` | texto | CEP do paciente. | — | 2002-03 a 2026-08 |
| `munic_res` | `MUNIC_RES` | texto | Município de Residência do Paciente | — | 2002-03 a 2026-08 |
| `uti_mes_in` | `UTI_MES_IN` | inteiro | Zerado | — | 2002-03 a 2026-08 |
| `uti_mes_an` | `UTI_MES_AN` | inteiro | Zerado | — | 2002-03 a 2026-08 |
| `uti_mes_al` | `UTI_MES_AL` | inteiro | Zerado | — | 2002-03 a 2026-08 |
| `uti_mes_to` | `UTI_MES_TO` | inteiro | Quantidade de dias de UTI no mês. | — | 2002-03 a 2026-08 |
| `marca_uti` | `MARCA_UTI` | texto | Indica qual o tipo de UTI utilizada pelo paciente. | — | 2002-03 a 2026-08 |
| `uti_int_in` | `UTI_INT_IN` | inteiro | Zerado | — | 2002-03 a 2026-08 |
| `uti_int_an` | `UTI_INT_AN` | inteiro | Zerado | — | 2002-03 a 2026-08 |
| `uti_int_al` | `UTI_INT_AL` | inteiro | Zerado | — | 2002-03 a 2026-08 |
| `uti_int_to` | `UTI_INT_TO` | inteiro | Quantidade de diárias em unidade intermediaria. | — | 2002-03 a 2026-08 |
| `val_rn` | `VAL_RN` | decimal(13,2) | Zerado | — | 2002-03 a 2026-08 |
| `val_sadtsr` | `VAL_SADTSR` | decimal(11,2) | Zerado | — | 2002-03 a 2026-08 |
| `val_transp` | `VAL_TRANSP` | decimal(13,2) | Zerado | — | 2002-03 a 2026-08 |
| `val_obsang` | `VAL_OBSANG` | decimal(11,2) | Zerado | — | 2002-03 a 2026-08 |
| `val_ped1ac` | `VAL_PED1AC` | decimal(11,2) | Zerado | — | 2002-03 a 2026-08 |
| `val_uti` | `VAL_UTI` | decimal(8,2) | Valor de UTI. | — | 2002-03 a 2026-08 |
| `diag_secun` | `DIAG_SECUN` | texto | Código do diagnostico secundário (CID10). Preenchido com zeros a partir de 201501. | — | 2002-03 a 2026-08 |
| `gestao` | `GESTAO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2002-03 a 2026-08 |
| `nacional` | `NACIONAL` | texto | Código da nacionalidade do paciente. | — | 2002-03 a 2026-08 |
| `num_proc` | `NUM_PROC` | texto | Zerado | — | 2002-03 a 2026-08 |
| `car_int` | `CAR_INT` | texto | Caráter da internação. | — | 2002-03 a 2026-08 |
| `tot_pt_sp` | `TOT_PT_SP` | inteiro | Zerado | — | 2002-03 a 2026-08 |
| `cpf_aut` | `CPF_AUT` | texto | Zerado | — | 2002-03 a 2026-08 |
| `homonimo` | `HOMONIMO` | texto | Indicador se o paciente da AIH é homônimo do paciente de outra AIH. | — | 2002-03 a 2026-08 |
| `num_filhos` | `NUM_FILHOS` | inteiro | Número de filhos do paciente. | — | 2002-03 a 2026-08 |
| `instru` | `INSTRU` | texto | Grau de instrução do paciente. | — | 2002-03 a 2026-08 |
| `cid_notif` | `CID_NOTIF` | texto | CID de Notificação. | — | 2002-03 a 2026-08 |
| `contracep1` | `CONTRACEP1` | texto | Tipo de contraceptivo utilizado. | — | 2002-03 a 2026-08 |
| `contracep2` | `CONTRACEP2` | texto | Segundo tipo de contraceptivo utilizado. | — | 2002-03 a 2026-08 |
| `gestrisco` | `GESTRISCO` | texto | Indicador se é gestante de risco. | — | 2002-03 a 2026-08 |
| `insc_pn` | `INSC_PN` | texto | Número da gestante no pré-natal. | — | 2002-03 a 2026-08 |
| `seq_aih5` | `SEQ_AIH5` | texto | Sequencial de longa permanência (AIH tipo 5). | — | 2002-03 a 2026-08 |
| `cbor` | `CBOR` | texto | Ocupação do paciente, segundo a Classificação Brasileira de Ocupações – CBO. | — | 2002-03 a 2026-08 |
| `cnaer` | `CNAER` | texto | Código de acidente de trabalho. | — | 2002-03 a 2026-08 |
| `vincprev` | `VINCPREV` | texto | Vínculo com a Previdência. | — | 2002-03 a 2026-08 |
| `diar_acom` | `DIAR_ACOM` | inteiro | Quantidade de diárias de acompanhante. | — | 2009-02 a 2026-08 |
| `qt_diarias` | `QT_DIARIAS` | inteiro | Quantidade de diárias. | — | 2009-02 a 2026-08 |
| `proc_solic` | `PROC_SOLIC` | texto | Procedimento solicitado. | — | 2009-02 a 2026-08 |
| `val_acomp` | `VAL_ACOMP` | decimal(13,2) | Zerado | — | 2009-02 a 2026-08 |
| `rubrica` | `RUBRICA` | inteiro | Zerado | — | 2009-02 a 2026-08 |
| `ind_vdrl` | `IND_VDRL` | texto | Indica exame VDRL. | — | 2009-02 a 2026-08 |
| `gestor_cod` | `GESTOR_COD` | texto | Motivo de autorização da AIH pelo Gestor. | — | 2009-02 a 2026-08 |
| `gestor_tp` | `GESTOR_TP` | texto | Tipo de gestor. | — | 2009-02 a 2026-08 |
| `gestor_cpf` | `GESTOR_CPF` | texto | Número do CPF do Gestor. | — | 2009-02 a 2026-08 |
| `gestor_dt` | `GESTOR_DT` | texto | Data da autorização dada pelo Gestor (aaaammdd). | — | 2009-02 a 2026-08 |
| `cnes` | `CNES` | texto | Código CNES do hospital. | — | 2009-02 a 2026-08 |
| `cnpj_mant` | `CNPJ_MANT` | texto | CNPJ da mantenedora. | — | 2009-02 a 2026-08 |
| `infehosp` | `INFEHOSP` | texto | Status de infecção hospitalar. | — | 2009-02 a 2026-08 |
| `cid_asso` | `CID_ASSO` | texto | CID causa. | — | 2009-02 a 2026-08 |
| `cid_morte` | `CID_MORTE` | texto | CID da morte. | — | 2009-02 a 2026-08 |
| `complex` | `COMPLEX` | texto | Complexidade. | — | 2009-02 a 2026-08 |
| `financ` | `FINANC` | texto | Tipo de financiamento. | — | 2009-02 a 2026-08 |
| `faec_tp` | `FAEC_TP` | texto | Subtipo de financiamento FAEC. | — | 2009-02 a 2026-08 |
| `regct` | `REGCT` | texto | Regra contratual. | — | 2009-02 a 2026-08 |
| `raca_cor` | `RACA_COR` | texto | Raça/Cor do paciente. | — | 2009-02 a 2026-08 |
| `etnia` | `ETNIA` | texto | Etnia do paciente, se raça cor for indígena. | — | 2009-02 a 2026-08 |
| `sequencia` | `SEQUENCIA` | inteiro | Sequencial da AIH na remessa. | — | 2009-02 a 2026-08 |
| `remessa` | `REMESSA` | texto | Número da remessa. | — | 2009-02 a 2026-08 |
| `nat_jur` | `NAT_JUR` | texto | Natureza jurídica do Estabelecimento, conforme a Comissão Nacional de Classificação - CONCLA | — | 2016-03 a 2026-08 |
| `aud_just` | `AUD_JUST` | texto | Justificativa do auditor para aceitação da AIH sem o número do Cartão Nacional de Saúde. | — | 2016-03 a 2026-08 |
| `sis_just` | `SIS_JUST` | texto | Justificativa do estabelecimento para aceitação da AIH sem o número do Cartão Nacional de Saúde. | — | 2016-03 a 2026-08 |
| `val_sh_fed` | `VAL_SH_FED` | decimal(10,2) | Valor do complemento federal de serviços hospitalares. Está incluído no valor total da AIH. | — | 2016-03 a 2026-08 |
| `val_sp_fed` | `VAL_SP_FED` | decimal(10,2) | Valor do complemento federal de serviços profissionais. Está incluído no valor total da AIH. | — | 2016-03 a 2026-08 |
| `val_sh_ges` | `VAL_SH_GES` | decimal(10,2) | Valor do complemento do gestor (estadual ou municipal) de serviços hospitalares. Está incluído no valor total da AIH. | — | 2016-03 a 2026-08 |
| `val_sp_ges` | `VAL_SP_GES` | decimal(10,2) | Valor do complemento do gestor (estadual ou municipal) de serviços profissionais. Está incluído no valor total da AIH. | — | 2016-03 a 2026-08 |
| `val_uci` | `VAL_UCI` | decimal(10,2) | Valor de UCI. | — | 2016-03 a 2026-08 |
| `marca_uci` | `MARCA_UCI` | texto | Tipo de UCI utilizada pelo paciente. | — | 2016-03 a 2026-08 |
| `diagsec1` | `DIAGSEC1` | texto | Diagnóstico secundário1. | — | 2016-03 a 2026-08 |
| `diagsec2` | `DIAGSEC2` | texto | Diagnóstico secundário 2. | — | 2016-03 a 2026-08 |
| `diagsec3` | `DIAGSEC3` | texto | Diagnóstico secundário 3. | — | 2016-03 a 2026-08 |
| `diagsec4` | `DIAGSEC4` | texto | Diagnóstico secundário 4. | — | 2016-03 a 2026-08 |
| `diagsec5` | `DIAGSEC5` | texto | Diagnóstico secundário 5. | — | 2016-03 a 2026-08 |
| `diagsec6` | `DIAGSEC6` | texto | Diagnóstico secundário 6. | — | 2016-03 a 2026-08 |
| `diagsec7` | `DIAGSEC7` | texto | Diagnóstico secundário 7. | — | 2016-03 a 2026-08 |
| `diagsec8` | `DIAGSEC8` | texto | Diagnóstico secundário 8. | — | 2016-03 a 2026-08 |
| `diagsec9` | `DIAGSEC9` | texto | Diagnóstico secundário 9. | — | 2016-03 a 2026-08 |
| `tpdisec1` | `TPDISEC1` | texto | Tipo de diagnóstico secundário 1. | — | 2016-03 a 2026-08 |
| `tpdisec2` | `TPDISEC2` | texto | Tipo de diagnóstico secundário 2. | — | 2016-03 a 2026-08 |
| `tpdisec3` | `TPDISEC3` | texto | Tipo de diagnóstico secundário 3. | — | 2016-03 a 2026-08 |
| `tpdisec4` | `TPDISEC4` | texto | Tipo de diagnóstico secundário 4. | — | 2016-03 a 2026-08 |
| `tpdisec5` | `TPDISEC5` | texto | Tipo de diagnóstico secundário 5. | — | 2016-03 a 2026-08 |
| `tpdisec6` | `TPDISEC6` | texto | Tipo de diagnóstico secundário 6. | — | 2016-03 a 2026-08 |
| `tpdisec7` | `TPDISEC7` | texto | Tipo de diagnóstico secundário 7. | — | 2016-03 a 2026-08 |
| `tpdisec8` | `TPDISEC8` | texto | Tipo de diagnóstico secundário 8. | — | 2016-03 a 2026-08 |
| `tpdisec9` | `TPDISEC9` | texto | Tipo de diagnóstico secundário 9. | — | 2016-03 a 2026-08 |
| `fonte_orc` | `FONTE_ORC` | texto | Fonte orçamentária do pagamento (campo presente só nas partições mais recentes) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2026-08 |

## No lake

- **Dataset no lake:** `datasus/sih-rd`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 2, decimal(10,2): 6, decimal(11,2): 3, decimal(13,2): 8, decimal(14,2): 1, decimal(8,2): 1, decimal(9,2): 5, inteiro: 18, texto: 80.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sih-rd.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) o RD contém apenas AIH **aprovadas**; AIH rejeitadas estão em `sih-rj`/`sih-er` e podem ser reapresentadas e aprovadas em competência posterior, portanto não some RD+RJ sem deduplicar `N_AIH`; (ii) AIH tipo 5 (`IDENT = 5`) repete-se por competência — exclua-as ao contar admissões; (iii) `MUNIC_RES` `999999`/ignorado vira `null`; (iv) UF do arquivo = UF de gestão (`UF_ZI`), não necessariamente a UF de residência — pacientes de outras UFs aparecem em `MUNIC_RES`; (v) valores monetários são nominais da época (não deflacionados) e mudam de regra com a SIGTAP. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 95 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas internações aprovadas (AIH normais, sem as de continuação) houve por UF e ano, e qual o valor total pago?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sih-rd").glob("**/*.parquet"))
dados = pl.concat(  # períodos diferentes têm colunas e tipos diferentes
    [pl.scan_parquet(a, hive_partitioning=True) for a in arquivos],
    how="diagonal_relaxed",
)

(
    dados.filter(
        pl.col("ident") == "1"
    )  # exclui AIH de continuação (tipo 5), que repetem a internação
    .group_by("ano", "uf")
    .agg(pl.len().alias("internacoes"), pl.col("val_tot").sum().alias("valor_total"))
    .sort("ano", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Pela linha de comando (`datasus-fetcher`)

```bash
# o que o FTP publica para o dataset (arquivos e tamanho)
datasus-fetcher list sih-rd

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sih-rd -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sih-rd
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIHSUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/IT_SIHSUS_1603.pdf`
- **Manual Técnico Operacional do SIH/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **PCDaS/Fiocruz** (SIH/SUS para pesquisa): https://pcdas.icict.fiocruz.br/
- **Portal DATASUS — SIH/SUS (TabNet)**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/ (Assistência à Saúde → Morbidade Hospitalar do SUS).
