---
dataset:
  id: cnes-st
  fonte: datasus
  titulo: Estabelecimentos
  resumo: 'Estabelecimentos do DATASUS: um estabelecimento de saúde, em uma competência.'
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2005-08
    fim: em-curso
  unidade: um estabelecimento de saúde, em uma competência
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
    colunas: 210
  unidades_de_medida:
    qtleitp1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleitp2: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleitp3: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst01: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst02: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst03: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst04: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst05: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst06: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst07: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst08: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst09: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst10: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst11: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst12: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst13: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst14: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst15: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst16: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst17: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst18: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst19: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst20: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst21: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst22: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst23: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst24: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst25: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst26: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst27: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst28: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst29: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst30: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst31: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst32: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst33: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst34: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst35: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst36: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtinst37: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit05: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit06: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit07: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit08: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit09: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit19: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit20: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit21: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit22: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit23: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit32: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit34: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit38: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit39: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qtleit40: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: cod_cep
    categoria: CEP
  - coluna: cpf_cnpj
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  eras:
  - desde: 2005-08
    mudanca: início da série do CNES no FTP (base `200508_`)
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Estabelecimentos (`cnes-st`)

## Resumo

O `cnes-st` contém os microdados do arquivo de **Estabelecimentos** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), o cadastro oficial e obrigatório de todos os estabelecimentos de saúde — públicos, privados e conveniados — que realizam ações e serviços de saúde no território nacional. Cada registro (linha) representa um estabelecimento de saúde identificado pelo número nacional CNES, em uma determinada competência (mês/ano) e UF. É a tabela-raiz do CNES: todas as demais tabelas (profissionais, leitos, equipamentos, serviços, equipes) referenciam o `CNES` nela cadastrado.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/ST` | `ST` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `STSP2401.dbc` — `ST` identifica o arquivo de Estabelecimentos, `SP` a Unidade da Federação, `24` o ano e `01` o mês da competência. Também existem arquivos `STBR<AA><MM>.dbc` (consolidação nacional).
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-st/<AAAAMM>/cnes-st_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/cnes-st/202401/cnes-st_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: no diretório `CNES/200508_/doc` está a Nota Técnica de layout `IT_CNES_1706.pdf` (dicionário oficial de todos os arquivos CNES); em `CNES/200508_/Auxiliar` está `TAB_CNES.zip`, pacote com as tabelas de domínio (tipos de unidade, natureza jurídica, esfera administrativa, habilitações, serviços/classificações, CBO, etc.) usadas na tabulação.

## Conteúdo

O CNES é gerido pelo Ministério da Saúde por intermédio da Secretaria Executiva/DATASUS (Divisão de Disseminação de Informações em Saúde — DIDIS) e da Coordenação-Geral de Sistemas de Informação da então SAS. O cadastro foi criado pela Portaria SAS/MS nº 403/2000, teve a Ficha Cadastral dos Estabelecimentos de Saúde (FCES) aprovada pela Portaria SAS/MS nº 511/2000 e foi reinstituído como sistema de informação oficial pela Portaria GM/MS nº 1.646/2015. Sua manutenção é responsabilidade compartilhada dos gestores estaduais e municipais de saúde, com alimentação continuada pelos próprios estabelecimentos no SCNES (Sistema do Cadastro Nacional de Estabelecimentos de Saúde). O CNES é o vértice de integração dos sistemas de informação do SUS: seus códigos alimentam SIH, SIA, SINAN, SINASC, RNDS e os demais cadastros nacionais.

O **evento gerador** deste dataset é o cadastro/atualização mensal do estabelecimento na FCES, por meio do aplicativo SCNES ou de *webservices*. A **unidade de análise é o estabelecimento de saúde em uma competência** (`CNES` + `COMPETEN`). Um mesmo CNES pode aparecer em várias competências (série histórica de sua situação cadastral) e a extração mensal funciona como um retrato da rede assistencial naquele mês. O arquivo `ST` concentra os atributos de identificação, localização, natureza jurídica, esfera administrativa, tipo de unidade, vínculo com o SUS, habilitações de gestão e capacidade física básica (instalações e leitos) do estabelecimento.

A série histórica do FTP começa em agosto de 2005 (base `200508_`). Ao longo do tempo houve incorporação de campos e mudanças de leiaute documentadas na `IT_CNES` — por exemplo a introdução do campo `NAT_JUR` (natureza jurídica padronizada) e indicadores de gestão (`GESPRG*`), da `DT_ATUA` (competência da última atualização informada pelo estabelecimento) e de blocos de requisitos de hemoterapia, radioterapia e quimioterapia nos arquivos complementares. Não há diretório preliminar: os arquivos são publicados já consolidados por competência.

Aplicações analíticas típicas: dimensionamento da rede assistencial (número de estabelecimentos por tipo, esfera e natureza jurídica), cobertura de atenção básica e de serviços especializados, distribuição territorial da oferta de leitos e equipamentos, identificação de estabelecimentos com/sem vínculo SUS, base para cálculo de cobertura de equipes de atenção básica e para vinculação de profissionais, internações (SIH) e procedimentos ambulatoriais (SIA).

### Cobertura observada

- Índice do FTP (2026-10): 6858 arquivos, de 2005-08 a 2026-09, 27 UF(s) com arquivos, última atualização em 2026-10-15.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2005-10 a 2026-01), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Eras

- **2005-08**: início da série do CNES no FTP (base `200508_`)

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde (chave primária) |
| `CODUFMUN` | String (7) | Código do município do estabelecimento: UF + MUNIC (sem dígito verificador) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `CPF_CNPJ` | String (14) | CPF (pessoa física) ou CNPJ (pessoa jurídica) do estabelecimento |
| `PF_PJ` | String (1) | Indicador de pessoa: 1 - Física, 3 - Jurídica |
| `NIV_DEP` | String (1) | Grau de dependência: 1 - Individual, 3 - Mantida |
| `TP_UNID` | String (2) | Código do tipo de unidade/estabelecimento |
| `ESFERA_A` | String (2) | Código da esfera administrativa (federal, estadual, municipal, privada) |
| `NATUREZA` | String (2) | Código da natureza da organização |
| `NAT_JUR` | String (4) | Natureza jurídica padronizada do estabelecimento |
| `VINC_SUS` | String (1) | Vínculo com o SUS: 1 - Sim, 0 - Não |
| `TPGESTAO` | String (1) | Tipo de gestão de saúde do estabelecimento |
| `REGSAUDE` / `MICR_REG` | String (4/6) | Código da região e da microrregião de saúde (NOAS) |
| `TP_PREST` | String (2) | Tipo de prestador |
| `DT_ATUA` | String (`AAAAMM`) | Competência da última atualização informada pelo estabelecimento |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `cnes` | `CNES` | texto | Número nacional do estabelecimento de saúde | — | todos |
| `codufmun` | `CODUFMUN` | texto | Código do município do estabelecimento: UF + MUNIC (sem dígito) | — | todos |
| `cod_cep` | `COD_CEP` | texto | Código do CEP do estabelecimento | — | todos |
| `cpf_cnpj` | `CPF_CNPJ` | texto | CPF do estabelecimento, caso pessoa física ou CNPJ, caso pessoa jurídica | — | todos |
| `pf_pj` | `PF_PJ` | texto | Indicador de pessoa: 1-Física 3-Jurídica | — | todos |
| `niv_dep` | `NIV_DEP` | texto | Grau de dependência, onde: 1-Individual 3-Mantida | — | todos |
| `cnpj_man` | `CNPJ_MAN` | texto | CNPJ da mantenedora do estabelecimento. | — | todos |
| `cod_ir` | `COD_IR` | texto | Indica o tipo de retenção de tributos da mantenedora | — | todos |
| `regsaude` | `REGSAUDE` | texto | Código da região de saúde NOAS | — | todos |
| `micr_reg` | `MICR_REG` | texto | Código da micro-região de saúde NOAS | — | todos |
| `distrsan` | `DISTRSAN` | texto | Código do distrito sanitário | — | todos |
| `distradm` | `DISTRADM` | texto | Inicialmente chamado Distrito Administrativo, atualmente Código do Módulo Assistencial conforme tabela local, em conformidade com o Plano Diretor de Regionalização do Estado/Município. | — | todos |
| `vinc_sus` | `VINC_SUS` | texto | Vínculo com SUS: 1-Sim 0-Não | — | todos |
| `tpgestao` | `TPGESTAO` | texto | Gestão de saúde | — | todos |
| `esfera_a` | `ESFERA_A` | texto | Código da esfera administrativa | — | todos |
| `retencao` | `RETENCAO` | texto | Código de retenção de tributos | — | todos |
| `atividad` | `ATIVIDAD` | texto | Código da atividade de ensino/pesquisa | — | todos |
| `natureza` | `NATUREZA` | texto | Código da natureza da organização | — | todos |
| `clientel` | `CLIENTEL` | texto | Código de FLUXO da clientela | — | todos |
| `tp_unid` | `TP_UNID` | texto | Tipo de unidade (estabelecimento) | — | todos |
| `turno_at` | `TURNO_AT` | texto | Código de turno de atendimento | — | todos |
| `niv_hier` | `NIV_HIER` | texto | Código do nível de hierarquia | — | todos |
| `tp_prest` | `TP_PREST` | texto | Tipo de Prestador | — | todos |
| `co_banco` | `CO_BANCO` | texto | Código do Banco do Estabelecimento | — | todos |
| `co_agenc` | `CO_AGENC` | texto | Código da Agência do Estabelecimento | — | todos |
| `c_corren` | `C_CORREN` | texto | Código da Conta Corrente do Estabelecimento | — | todos |
| `contratm` | `CONTRATM` | texto | Número do contrato/convênio MUNICIPAL do vínculo com o SUS | — | todos |
| `dt_publm` | `DT_PUBLM` | texto | Ano e Mês de publicação do contrato /convênio MUNICIPAL (AAAAMM) | — | todos |
| `contrate` | `CONTRATE` | texto | Número do contrato/convênio ESTADUAL do vínculo com o SUS | — | todos |
| `dt_puble` | `DT_PUBLE` | texto | Ano e Mês de publicação do contrato /convênio ESTADUAL (AAAAMM) | — | todos |
| `alvara` | `ALVARA` | texto | Número do alvará | — | todos |
| `dt_exped` | `DT_EXPED` | texto | Ano e Mês de da expedição do alvará (AAAAMM) | — | todos |
| `orgexped` | `ORGEXPED` | texto | Órgão expedidor do alvará, onde: 1-SES 2-SMS | — | todos |
| `av_acred` | `AV_ACRED` | texto | Indica se o estabelecimento foi avaliado segundo o Manual de Acreditação Hospitalar do MS, onde: 1-Sim 2-Não | — | todos |
| `clasaval` | `CLASAVAL` | texto | Classificação da avaliação do estabelecimento segundo o Manual de Acreditação Hospitalar do MS | — | todos |
| `dt_acred` | `DT_ACRED` | texto | Ano e Mês da Acreditação (AAAAMM) | — | todos |
| `av_pnass` | `AV_PNASS` | texto | Indica se o estabelecimento foi avaliado segundo o Programa Nacional de Serviços de Saúde - PNASS, onde: 1-Sim 2-Não | — | todos |
| `dt_pnass` | `DT_PNASS` | texto | Ano e Mês da Avaliação PNASS (AAAAMM) | — | todos |
| `gesprg1e` | `GESPRG1E` | texto | Indicador se a gestão da atividade ATENÇÃO BÁSICA do Nível de Atenção AMBULATORIAL é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg1m` | `GESPRG1M` | texto | Indicador se a gestão da atividade ATENÇÃO BÁSICA do Nível de Atenção AMBULATORIAL é MUNICIPAL, onde: 1-sim 0-não | — | todos |
| `gesprg2e` | `GESPRG2E` | texto | Indicador se a gestão da atividade MÉDIA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg2m` | `GESPRG2M` | texto | Indicador se a gestão da atividade MÉDIA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é MUNICIPAL, onde: 1-sim 0-não | — | todos |
| `gesprg4e` | `GESPRG4E` | texto | Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg4m` | `GESPRG4M` | texto | Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é MUNICIPAL, onde: 1-sim 0-não | — | todos |
| `nivate_a` | `NIVATE_A` | texto | Indica a existência de Nível de Atenção AMBULATORIAL, de gestão Municipal/Estadual, para este CNES, onde: 1-sim 0-não | — | todos |
| `gesprg3e` | `GESPRG3E` | texto | Indicador se a gestão do programa cód. 03 é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg3m` | `GESPRG3M` | texto | Indicador se a gestão do programa cód. 03 é MUNICIPAL, onde: 1-sim 0-não | — | todos |
| `gesprg5e` | `GESPRG5E` | texto | Indicador se a gestão da atividade MÉDIA COMPLEXIDADE do Nível de Atenção HOSPITALAR é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg5m` | `GESPRG5M` | texto | Indicador se a gestão da atividade MÉDIA COMPLEXIDADE do Nível de Atenção HOSPITALAR é MUNICIPAL, onde: 1-sim 0-não | — | todos |
| `gesprg6e` | `GESPRG6E` | texto | Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção HOSPITALAR é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg6m` | `GESPRG6M` | texto | Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção HOSPITALAR é MUNICIPAL, onde: 1-sim 0-não | — | todos |
| `nivate_h` | `NIVATE_H` | texto | Indica a existência de Nível de Atenção HOSPITALAR, de gestão Municipal/Estadual, para este CNES, onde: 1-sim 0-não | — | todos |
| `qtleitp1` | `QTLEITP1` | inteiro | Quantidade de leitos tipo 1 (cirúrgico) existentes | — | todos |
| `qtleitp2` | `QTLEITP2` | inteiro | Quantidade de leitos tipo 2 (clínico) existentes | — | todos |
| `qtleitp3` | `QTLEITP3` | inteiro | Quantidade de leitos tipo 3 (complem.) existentes | — | todos |
| `leithosp` | `LEITHOSP` | texto | Indica a existência de LEITOS HOSPITALARES-CIRPURGICOS, CLÍNICOS E COMPLEMENTARES para este CNES, onde: 1-sim 0-não | — | todos |
| `qtinst01` | `QTINST01` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst02` | `QTINST02` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst03` | `QTINST03` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst04` | `QTINST04` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst05` | `QTINST05` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst06` | `QTINST06` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst07` | `QTINST07` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst08` | `QTINST08` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst09` | `QTINST09` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst10` | `QTINST10` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst11` | `QTINST11` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst12` | `QTINST12` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst13` | `QTINST13` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst14` | `QTINST14` | inteiro | Quantidade de salas/consultórios | — | todos |
| `urgemerg` | `URGEMERG` | texto | Indica a existência de INSTALAÇÃO FÍSICA de URGÊNCIA/EMERGÊNCIA para este CNES, onde: 1-sim 0-não | — | todos |
| `qtinst15` | `QTINST15` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst16` | `QTINST16` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst17` | `QTINST17` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst18` | `QTINST18` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst19` | `QTINST19` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst20` | `QTINST20` | inteiro | Quantidade de salas/consultórios (instalação 20) | — | todos |
| `qtinst21` | `QTINST21` | inteiro | Quantidade de salas/consultórios (instalação 21) | — | todos |
| `qtinst22` | `QTINST22` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst23` | `QTINST23` | inteiro | Quantidade de salas/consultórios (instalação 23) | — | todos |
| `qtinst24` | `QTINST24` | inteiro | Quantidade de salas/consultórios (instalação 24) | — | todos |
| `qtinst25` | `QTINST25` | inteiro | Quantidade de salas/consultórios (instalação 25) | — | todos |
| `qtinst26` | `QTINST26` | inteiro | Quantidade de salas/consultórios (instalação 26) | — | todos |
| `qtinst27` | `QTINST27` | inteiro | Quantidade de salas/consultórios (instalação 27) | — | todos |
| `qtinst28` | `QTINST28` | inteiro | Quantidade de salas/consultórios (instalação 28) | — | todos |
| `qtinst29` | `QTINST29` | inteiro | Quantidade de salas/consultórios (instalação 29) | — | todos |
| `qtinst30` | `QTINST30` | inteiro | Quantidade de salas/consultórios (instalação 30) | — | todos |
| `atendamb` | `ATENDAMB` | texto | Indica a existência de INSTALAÇÃO FÍSICA de ATENDIMENTO AMBULATORIAL para este CNES, onde: 1-sim 0-não | — | todos |
| `qtinst31` | `QTINST31` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst32` | `QTINST32` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst33` | `QTINST33` | inteiro | Quantidade de salas/consultórios | — | todos |
| `centrcir` | `CENTRCIR` | texto | Indica a existência de INSTALAÇÃO FÍSICA de ATENDIMENTO HOSPITALAR- CENTRO CIRÚRGICO para este CNES, onde: 1-sim 0-não | — | todos |
| `qtinst34` | `QTINST34` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst35` | `QTINST35` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst36` | `QTINST36` | inteiro | Quantidade de salas/consultórios | — | todos |
| `qtinst37` | `QTINST37` | inteiro | Quantidade de salas/consultórios | — | todos |
| `centrobs` | `CENTROBS` | texto | Indica a existência de INSTALAÇÃO FÍSICA de ATENDIMENTO HOSPITALAR- CENTRO OBSTÉTRICO para este CNES, onde: 1-sim 0-não | — | todos |
| `qtleit05` | `QTLEIT05` | inteiro | Quantidade de leitos/equipos | — | todos |
| `qtleit06` | `QTLEIT06` | inteiro | Quantidade de leitos/equipos | — | todos |
| `qtleit07` | `QTLEIT07` | inteiro | Quantidade de leitos/equipos | — | todos |
| `qtleit08` | `QTLEIT08` | inteiro | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `qtleit09` | `QTLEIT09` | inteiro | Quantidade de leitos/equipos | — | todos |
| `qtleit19` | `QTLEIT19` | inteiro | Quantidade de leitos/equipos | — | todos |
| `qtleit20` | `QTLEIT20` | inteiro | Quantidade de leitos/equipos | — | todos |
| `qtleit21` | `QTLEIT21` | inteiro | Quantidade de leitos/equipos | — | todos |
| `qtleit22` | `QTLEIT22` | inteiro | Quantidade de leitos/equipos | — | todos |
| `qtleit23` | `QTLEIT23` | inteiro | Quantidade de leitos/equipos | — | todos |
| `qtleit32` | `QTLEIT32` | inteiro | Quantidade de leitos/equipos | — | todos |
| `qtleit34` | `QTLEIT34` | inteiro | Quantidade de leitos/equipos | — | todos |
| `qtleit38` | `QTLEIT38` | inteiro | Quantidade de leitos/equipos | — | todos |
| `qtleit39` | `QTLEIT39` | inteiro | Quantidade de leitos/equipos | — | todos |
| `qtleit40` | `QTLEIT40` | inteiro | Quantidade de leitos/equipos | — | todos |
| `centrneo` | `CENTRNEO` | texto | Indica a existência de INSTALAÇÃO FÍSICA de ATENDIMENTO HOSPITALAR- UNIDADE NEONATAL para este CNES, onde: 1-sim 0-não | — | todos |
| `atendhos` | `ATENDHOS` | texto | Indica a existência de INSTALAÇÃO FÍSICA de ATENDIMENTO HOSPITALAR para este CNES, onde: 1-sim 0-não | — | todos |
| `serap01p` | `SERAP01P` | texto | Serviço de apoio S.A.M.E. ou S.P.P. próprio, onde: 1-sim 0-não | — | todos |
| `serap01t` | `SERAP01T` | texto | Serviço de apoio S.A.M.E. ou S.P.P. terceirizado, onde: 1-sim 0-não | — | todos |
| `serap02p` | `SERAP02P` | texto | Serviço de apoio Serviço Social próprio, onde: 1-sim 0-não | — | todos |
| `serap02t` | `SERAP02T` | texto | Serviço de apoio Serviço Social terceirizado, onde: 1-sim 0-não | — | todos |
| `serap03p` | `SERAP03P` | texto | Serviço de apoio Farmácia próprio, onde: 1-sim 0-não | — | todos |
| `serap03t` | `SERAP03T` | texto | Serviço de apoio Farmácia terceirizado, onde: 1-sim 0-não | — | todos |
| `serap04p` | `SERAP04P` | texto | Serviço de apoio Esterilização de Materiais próprio, onde: 1-sim 0-não | — | todos |
| `serap04t` | `SERAP04T` | texto | Serviço de apoio Esterilização de Materiais terceirizado, onde: 1-sim 0-não | — | todos |
| `serap05p` | `SERAP05P` | texto | Serviço de apoio Nutrição/Dietética (S.N.D.) próprio, onde: 1-sim 0-não | — | todos |
| `serap05t` | `SERAP05T` | texto | Serviço de apoio Nutrição/Dietética (S.N.D.) terceirizado, onde: 1-sim 0-não | — | todos |
| `serap06p` | `SERAP06P` | texto | Serviço de apoio Lactário próprio, onde: 1-sim 0-não | — | todos |
| `serap06t` | `SERAP06T` | texto | Serviço de apoio Lactário terceirizado, onde: 1-sim 0-não | — | todos |
| `serap07p` | `SERAP07P` | texto | Serviço de apoio Banco De Leite próprio, onde: 1-sim 0-não | — | todos |
| `serap07t` | `SERAP07T` | texto | Serviço de apoio Banco De Leite terceirizado, onde: 1-sim 0-não | — | todos |
| `serap08p` | `SERAP08P` | texto | Serviço de apoio Lavanderia próprio, onde: 1-sim 0-não | — | todos |
| `serap08t` | `SERAP08T` | texto | Serviço de apoio Lavanderia terceirizado, onde: 1-sim 0-não | — | todos |
| `serap09p` | `SERAP09P` | texto | Serviço de apoio Manutenção de Equipamento próprio, onde: 1-sim 0-não | — | todos |
| `serap09t` | `SERAP09T` | texto | Serviço de apoio Manutenção de Equipamento terceirizado, onde: 1-sim 0-não | — | todos |
| `serap10p` | `SERAP10P` | texto | Serviço de apoio Ambulância próprio, onde: 1-sim 0-não | — | todos |
| `serap10t` | `SERAP10T` | texto | Serviço de apoio Ambulância terceirizado, onde: 1-sim 0-não | — | todos |
| `serap11p` | `SERAP11P` | texto | Serviço de apoio Necrotério próprio, onde: 1-sim 0-não | — | todos |
| `serap11t` | `SERAP11T` | texto | Serviço de apoio Necrotério terceirizado, onde: 1-sim 0-não | — | todos |
| `serapoio` | `SERAPOIO` | texto | Indica a existência de algum serviço de apoio para este CNES, onde: 1-sim 0-não | — | todos |
| `res_biol` | `RES_BIOL` | texto | Existe coleta de resíduo biológico, onde: 1-sim 0-não | — | todos |
| `res_quim` | `RES_QUIM` | texto | Existe coleta de resíduo químico, onde: 1-sim 0-não | — | todos |
| `res_radi` | `RES_RADI` | texto | Existe coleta de rejeitos radioativos, onde: 1-sim 0-não | — | todos |
| `res_comu` | `RES_COMU` | texto | Existe coleta de resíduos comuns, onde: 1-sim 0-não | — | todos |
| `coletres` | `COLETRES` | texto | Indica a existência de alguma coleta de resíduo para este CNES, onde: 1-sim 0-não | — | todos |
| `comiss01` | `COMISS01` | texto | Existe comissão de ETICA MEDICA, onde: 1-sim 0-não | — | todos |
| `comiss02` | `COMISS02` | texto | Existe comissão de ETICA DE ENFERMAGEM, onde: 1-sim 0-não | — | todos |
| `comiss03` | `COMISS03` | texto | Existe comissão de FARMÁCIA E TERAPÊUTICA, onde: 1-sim 0-não | — | todos |
| `comiss04` | `COMISS04` | texto | Existe comissão de CONTROLE DE INFECÇÃO HOSPITALAR, onde: 1-sim 0-não | — | todos |
| `comiss05` | `COMISS05` | texto | Existe comissão de APROPRIAÇÃO DE CUSTOS, onde: 1-sim 0-não | — | todos |
| `comiss06` | `COMISS06` | texto | Existe comissão de CIPA, onde: 1-sim 0-não | — | todos |
| `comiss07` | `COMISS07` | texto | Existe comissão de REVISÃO DE PRONTUÁRIOS, onde: 1-sim 0-não | — | todos |
| `comiss08` | `COMISS08` | texto | Existe comissão de REVISAO DE DOCUMENTACAO MEDICA E ESTATISTICA, onde: 1-sim 0-não | — | todos |
| `comiss09` | `COMISS09` | texto | Existe comissão de ANALISE DE OBITOS E BIOPISIAS, onde: 1-sim 0-não | — | todos |
| `comiss10` | `COMISS10` | texto | Existe comissão de INVESTIGACAO EPIDEMIOLOGICA, onde: 1-sim 0-não | — | todos |
| `comiss11` | `COMISS11` | texto | Existe comissão de NOTIFICACAO DE DOENCAS, onde: | — | todos |
| `comiss12` | `COMISS12` | texto | 1-sim 0-não Existe comissão de CONTROLE DE ZOONOSES E VETORES, onde: 1-sim 0-não | — | todos |
| `comissao` | `COMISSAO` | texto | Indica a existência de alguma comissão para este CNES, onde: 1-sim 0-não | — | todos |
| `ap01cv01` | `AP01CV01` | texto | Atendimento prestado INTERNAÇÃO/Convenio SUS, onde: 1-sim 0-não | — | todos |
| `ap01cv02` | `AP01CV02` | texto | Atendimento prestado INTERNAÇÃO/Convenio PARTICULAR, onde: 1-sim 0-não | — | todos |
| `ap01cv05` | `AP01CV05` | texto | Atendimento prestado INTERNAÇÃO/ Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap01cv06` | `AP01CV06` | texto | Atendimento prestado INTERNAÇÃO/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap01cv03` | `AP01CV03` | texto | Atendimento prestado INTERNAÇÃO/Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap01cv04` | `AP01CV04` | texto | Atendimento prestado INTERNAÇÃO/Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `ap02cv01` | `AP02CV01` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio SUS, onde: 1-sim 0-não | — | todos |
| `ap02cv02` | `AP02CV02` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PARTICULAR, onde: 1-sim 0-não | — | todos |
| `ap02cv05` | `AP02CV05` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap02cv06` | `AP02CV06` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap02cv03` | `AP02CV03` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO- SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap02cv04` | `AP02CV04` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO- SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `ap03cv01` | `AP03CV01` | texto | Atendimento prestado SADT/ Convenio SUS, onde: 1-sim 0-não | — | todos |
| `ap03cv02` | `AP03CV02` | texto | Atendimento prestado SADT/ Convenio PARTICULAR, onde: 1-sim 0-não | — | todos |
| `ap03cv05` | `AP03CV05` | texto | Atendimento prestado SADT/ Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap03cv06` | `AP03CV06` | texto | Atendimento prestado SADT/ Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap03cv03` | `AP03CV03` | texto | Atendimento prestado SADT/ Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap03cv04` | `AP03CV04` | texto | Atendimento prestado SADT/ Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `ap04cv01` | `AP04CV01` | texto | Atendimento prestado URGENCIA/ Convenio SUS, onde: 1-sim 0-não | — | todos |
| `ap04cv02` | `AP04CV02` | texto | Atendimento prestado URGENCIA/ Convenio PARTICULAR, onde: 1-sim 0-não | — | todos |
| `ap04cv05` | `AP04CV05` | texto | Atendimento prestado URGENCIA/ Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap04cv06` | `AP04CV06` | texto | Atendimento prestado URGENCIA/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap04cv03` | `AP04CV03` | texto | Atendimento prestado URGENCIA/ Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap04cv04` | `AP04CV04` | texto | Atendimento prestado URGENCIA/ Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `ap05cv01` | `AP05CV01` | texto | Atendimento prestado OUTROS/ Convenio SUS,onde: 1-sim 0-não | — | todos |
| `ap05cv02` | `AP05CV02` | texto | Atendimento prestado OUTROS/Convenio PARTICULAR, onde: 1-sim 0-não | — | todos |
| `ap05cv05` | `AP05CV05` | texto | Atendimento prestado OUTROS/Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap05cv06` | `AP05CV06` | texto | Atendimento prestado OUTROS/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap05cv03` | `AP05CV03` | texto | Atendimento prestado OUTROS/Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap05cv04` | `AP05CV04` | texto | Atendimento prestado OUTROS/Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `ap06cv01` | `AP06CV01` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio SUS, onde: 1-sim 0-não Atendimento prestado VIGILANCIA EM SAUDE/Convenio PARTICULAR, onde: | — | todos |
| `ap06cv02` | `AP06CV02` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio PARTICULAR, onde: 1-Sim 0-Não | — | todos |
| `ap06cv05` | `AP06CV05` | texto | 1-sim 0-não Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap06cv06` | `AP06CV06` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap06cv03` | `AP06CV03` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap06cv04` | `AP06CV04` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `ap07cv01` | `AP07CV01` | texto | Atendimento prestado REGULACAO/Convenio SUS, onde: 1-sim 0-não | — | todos |
| `ap07cv02` | `AP07CV02` | texto | Atendimento prestado REGULACAO/Convenio PARTICULAR, onde: 1-sim 0-não | — | todos |
| `ap07cv05` | `AP07CV05` | texto | Atendimento prestado REGULACAO/Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap07cv06` | `AP07CV06` | texto | Atendimento prestado REGULACAO/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap07cv03` | `AP07CV03` | texto | Atendimento prestado REGULACAO/Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap07cv04` | `AP07CV04` | texto | Atendimento prestado REGULACAO/Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `atend_pr` | `ATEND_PR` | texto | Indica a existência de algum atendimento prestado para este CNES, onde: 1-sim / 0-não | — | todos |
| `dt_atual` | `DT_ATUAL` | texto | Competência da última atualização informada pelo estabelecimento (AAAAMM) | — | todos |
| `competen` | `COMPETEN` | texto | Ano e Mês de competência da informação (AAAAMM) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `nat_jur` | `NAT_JUR` | texto | Natureza Jurídica | — | 2016-01 a 2026-01 |
| `ap01cv07` | `AP01CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-01 |
| `ap02cv07` | `AP02CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-01 |
| `ap03cv07` | `AP03CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-01 |
| `ap04cv07` | `AP04CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-01 |
| `ap05cv07` | `AP05CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-01 |
| `ap06cv07` | `AP06CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-01 |
| `ap07cv07` | `AP07CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-01 |

## No lake

- **Dataset no lake:** `datasus/cnes-st`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): inteiro: 55, texto: 155.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `cnes-st.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- a extração é um *snapshot* mensal, portanto para uma foto vigente use a competência mais recente e para séries históricas conte CNES distintos por competência; o campo `CODUFMUN` tem 7 caracteres (UF+6) mas o município é frequentemente referenciado com 6 dígitos + dígito verificador em outras bases, exigindo padronização; existe tanto arquivo por UF quanto `BR` consolidado, o que pode gerar duplicidade se ambos forem baixados; e campos de capacidade física (`QTLEITP1..3`, `QTINST*`) refletem o autocadastro do estabelecimento e exigem validação cruzada com os arquivos `LT` e `EQ`. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 8 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/cnes-st").glob("**/*.parquet"))
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
datasus-fetcher list cnes-st

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync cnes-st -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset cnes-st
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/ST`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica de layout `IT_CNES_1706.pdf`** e pacote `TAB_CNES.zip` (tabelas de domínio) no FTP DATASUS
- **Portaria GM/MS nº 1.646/2015** (institui o CNES) e Portaria SAS/MS nº 511/2000 (aprova a FCES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
