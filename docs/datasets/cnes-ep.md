---
dataset:
  id: cnes-ep
  fonte: datasus
  titulo: Equipes
  resumo: O cnes-ep contém os microdados do arquivo de Equipes do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra as equipes de atenção básica e outras equipes vinculadas aos estabelecimentos.
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2007-04
    fim: em-curso
  unidade: uma equipe de saúde vinculada a um estabelecimento, em uma competência
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
    colunas: 110
  dados_pessoais:
  - coluna: cod_cep
    categoria: CEP
  - coluna: cpf_cnpj
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Equipes (`cnes-ep`)

## Resumo

O `cnes-ep` contém os microdados do arquivo de **Equipes** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra as equipes de atenção básica e outras equipes vinculadas aos estabelecimentos. Cada registro (linha) representa uma **equipe** (`ID_EQUIPE`) de um estabelecimento, em uma competência mensal, com o tipo de equipe, área de atuação, segmento populacional atendido e datas de ativação/desativação. É a base oficial para monitorar a Estratégia Saúde da Família (ESF) e a cobertura da atenção primária.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2007-04 a 2026-09 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 6318 arquivos (~583 MB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Não
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`)
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/EP` | `EP` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `EPSP2401.dbc` — `EP` (Equipes), `SP` (UF), `24` (ano), `01` (mês). Há também `EPBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-ep/2024-01/cnes-ep_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Equipes — EP*.dbf") e `TAB_CNES.zip` (domínios de tipo de equipe, área, motivo de desativação).

## Conteúdo

O arquivo `EP` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS e alimentado pelos gestores municipais/estaduais no SCNES. As equipes cadastradas (Equipe de Saúde da Família, Equipe de Atenção Primária, equipes de saúde bucal, NASF/eMulti, equipes ribeirinhas, fluviais, entre outras) são o elemento operacional da Política Nacional de Atenção Básica (PNAB), e seu cadastro no CNES é condição para o repasse de recursos federais de custeio da atenção primária.

O **evento gerador** é a declaração das equipes na FCES/SCNES a cada competência. A **unidade de análise é a equipe de um estabelecimento na competência** (`CNES` + `ID_EQUIPE` + `COMPETEN`), identificada por município + código de área + sequencial. O campo `TIPO_EQP` classifica o tipo de equipe, `AREA_EQP`/`NOMEAREA` identificam a área de atuação, `TIPOSEGM` distingue segmento urbano/rural e as flags `QUILOMBO`, `ASSENTAD`, `POPGERAL`, `ESCOLA`, `INDIGENA` e `PRONASCI` indicam as populações assistidas. `DT_ATIVA` e `DT_DESAT` registram a ativação e a desativação da equipe, e `MOTDESAT`/`TP_DESAT` o motivo e o tipo de desativação.

A série histórica no FTP começa em abril de 2007, período de consolidação do cadastro de equipes após a implantação do CNES. Não há diretório preliminar.

Aplicações analíticas típicas: cobertura populacional estimada da atenção básica, número de equipes de saúde da família e de saúde bucal por município, evolução das equipes ativas ao longo do tempo, identificação de equipes desativadas e motivos, distribuição de equipes por segmento (urbano/rural, quilombola, indígena) e apoio ao cálculo de indicadores de financiamento da atenção primária.

### Cobertura observada

- Índice do FTP (2026-10): 6318 arquivos, de 2007-04 a 2026-09, 27 UF(s) com arquivos, última atualização em 2026-10-15.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007-07 a 2026-02), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (7) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `ID_EQUIPE` | String (18) | Código do município + código da área + sequencial da equipe |
| `TIPO_EQP` | String (2) | Tipo de equipe |
| `NOME_EQP` | String (60) | Nome da equipe |
| `AREA_EQP` | String (10) | Código da área da equipe |
| `NOMEAREA` | String (60) | Nome da área |
| `TIPOSEGM` | String (1) | Tipo do segmento: 1 - Urbano, 2 - Rural |
| `DT_ATIVA` / `DT_DESAT` | String (`AAAAMM`) | Competência de ativação / desativação da equipe |
| `QUILOMBO` / `ASSENTAD` | String (1) | Atende população quilombola / assentada: 1 - Sim, 0 - Não |
| `POPGERAL` / `ESCOLA` / `INDIGENA` / `PRONASCI` | String (1) | Populações assistidas: geral / escolares / indígena / PRONASCI |
| `MOTDESAT` | String (2) | Código do motivo de desativação da equipe |
| `TP_DESAT` | String (1) | Tipo de desativação: 1 - Temporário, 2 - Definitivo |
| `NAT_JUR` | String (4) | Natureza jurídica |

## Variáveis

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
| `terceiro` | `TERCEIRO` | texto | O estabelecimento é terceiro: 1-Sim 0-Não | — | todos |
| `tp_prest` | `TP_PREST` | texto | Tipo de Prestador | — | todos |
| `gesprg1e` | `GESPRG1E` | texto | Indicador se a gestão da atividade ATENÇÃO BÁSICA do Nível de Atenção AMBULATORIAL é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg1m` | `GESPRG1M` | texto | Indicador se a gestão da atividade ATENÇÃO BÁSICA do Nível de Atenção AMBULATORIAL é MUNICIPAL, onde: 1-sim 0-não | — | todos |
| `gesprg2e` | `GESPRG2E` | texto | Indicador se a gestão da atividade MÉDIA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg2m` | `GESPRG2M` | texto | Indicador se a gestão da atividade MÉDIA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é MUNICIPAL, onde: 1-sim 0-não | — | todos |
| `gesprg4e` | `GESPRG4E` | texto | Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg4m` | `GESPRG4M` | texto | Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é MUNICIPAL, onde: 1-sim 0-não | — | todos |
| `nivate_a` | `NIVATE_A` | texto | Indica a existência de Nível de Atenção AMBULATORIAL, de gestão Municipal/Estadual, para este CNES, onde: 1-sim 0-não | — | todos |
| `gesprg3e` | `GESPRG3E` | texto | Indicador se a gestão do programa é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg3m` | `GESPRG3M` | texto | Indicador se a gestão do programa é MUNICIPAL, onde: 1-sim 0-não | — | todos |
| `gesprg5e` | `GESPRG5E` | texto | Indicador se a gestão da atividade MÉDIA COMPLEXIDADE do Nível de Atenção HOSPITALAR é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg5m` | `GESPRG5M` | texto | Indicador se a gestão da atividade MÉDIA COMPLEXIDADE do Nível de Atenção HOSPITALAR é MUNICIPAL, onde: 1-sim 0-não | — | todos |
| `gesprg6e` | `GESPRG6E` | texto | Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção HOSPITALAR é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg6m` | `GESPRG6M` | texto | Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção HOSPITALAR é MUNICIPAL, onde: 1-sim 0-não | — | todos |
| `nivate_h` | `NIVATE_H` | texto | Indica a existência de Nível de Atenção HOSPITALAR, de gestão Municipal/Estadual, para este CNES, onde: 1-sim 0-não | — | todos |
| `ap01cv01` | `AP01CV01` | texto | Atendimento prestado INTERNAÇÃO/ Convenio SUS, onde: 1-sim 0-não | — | todos |
| `ap01cv02` | `AP01CV02` | texto | Atendimento prestado INTERNAÇÃO/Convenio PARTICULAR, onde: 1-sim 0-não | — | todos |
| `ap01cv05` | `AP01CV05` | texto | Atendimento prestado INTERNAÇÃO/Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap01cv06` | `AP01CV06` | texto | Atendimento prestado INTERNAÇÃO/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap01cv03` | `AP01CV03` | texto | Atendimento prestado INTERNAÇÃO/Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap01cv04` | `AP01CV04` | texto | Atendimento prestado INTERNAÇÃO/Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `ap02cv01` | `AP02CV01` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio SUS, onde: 1-sim 0-não | — | todos |
| `ap02cv02` | `AP02CV02` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PARTICULAR, onde: 1-sim 0-não | — | todos |
| `ap02cv05` | `AP02CV05` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap02cv06` | `AP02CV06` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap02cv03` | `AP02CV03` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO- SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap02cv04` | `AP02CV04` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO- SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `ap03cv01` | `AP03CV01` | texto | Atendimento prestado SADT/Convenio SUS, onde: 1-sim 0-não | — | todos |
| `ap03cv02` | `AP03CV02` | texto | Atendimento prestado SADT/Convenio PARTICULAR, onde: 1-sim 0-não | — | todos |
| `ap03cv05` | `AP03CV05` | texto | Atendimento prestado SADT/Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap03cv06` | `AP03CV06` | texto | Atendimento prestado SADT/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap03cv03` | `AP03CV03` | texto | Atendimento prestado SADT/Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap03cv04` | `AP03CV04` | texto | Atendimento prestado SADT/Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `ap04cv01` | `AP04CV01` | texto | Atendimento prestado URGENCIA/Convenio SUS, onde: 1-sim 0-não | — | todos |
| `ap04cv02` | `AP04CV02` | texto | Atendimento prestado URGENCIA/Convenio PARTICULAR, onde: 1-sim 0-não | — | todos |
| `ap04cv05` | `AP04CV05` | texto | Atendimento prestado URGENCIA/Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap04cv06` | `AP04CV06` | texto | Atendimento prestado URGENCIA/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap04cv03` | `AP04CV03` | texto | Atendimento prestado URGENCIA/Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap04cv04` | `AP04CV04` | texto | Atendimento prestado URGENCIA/Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `ap05cv01` | `AP05CV01` | texto | Atendimento prestado OUTROS/Convenio SUS,onde: 1-sim 0-não | — | todos |
| `ap05cv02` | `AP05CV02` | texto | Atendimento prestado OUTROS/Convenio PARTICULAR, onde: 1-sim 0-não | — | todos |
| `ap05cv05` | `AP05CV05` | texto | Atendimento prestado OUTROS/Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap05cv06` | `AP05CV06` | texto | Atendimento prestado OUTROS/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap05cv03` | `AP05CV03` | texto | Atendimento prestado OUTROS/Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap05cv04` | `AP05CV04` | texto | Atendimento prestado OUTROS/Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `ap06cv01` | `AP06CV01` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio SUS, onde: 1-sim 0-não | — | todos |
| `ap06cv02` | `AP06CV02` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio PARTICULAR, onde: 1-sim 0-não | — | todos |
| `ap06cv05` | `AP06CV05` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap06cv06` | `AP06CV06` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap06cv03` | `AP06CV03` | texto | Atendimento prestado VIGILANCIA EM SAUDE/ Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap06cv04` | `AP06CV04` | texto | Atendimento prestado VIGILANCIA EM SAUDE/ Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `ap07cv01` | `AP07CV01` | texto | Atendimento prestado REGULACAO/Convenio SUS, onde: 1-sim 0-não | — | todos |
| `ap07cv02` | `AP07CV02` | texto | Atendimento prestado REGULACAO/Convenio PARTICULAR, onde: 1-sim 0-não | — | todos |
| `ap07cv05` | `AP07CV05` | texto | Atendimento prestado REGULACAO/Convenio PLANO de SAUDE PUBLICO, onde: 1-sim 0-não | — | todos |
| `ap07cv06` | `AP07CV06` | texto | Atendimento prestado REGULACAO/Convenio PLANO de SAUDE PRIVADO, onde: 1-sim 0-não | — | todos |
| `ap07cv03` | `AP07CV03` | texto | Atendimento prestado REGULACAO/Convenio PLANO-SEGURO PROPRIO, onde: 1-sim 0-não | — | todos |
| `ap07cv04` | `AP07CV04` | texto | Atendimento prestado REGULACAO/Convenio PLANO-SEGURO TERCEIRO, onde: 1-sim 0-não | — | todos |
| `atend_pr` | `ATEND_PR` | texto | Indica a existência de algum atendimento prestado para este CNES, onde: 1-sim / 0-não | — | todos |
| `idequipe` | `IDEQUIPE` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `tipo_eqp` | `TIPO_EQP` | texto | Tipo de Equipe | — | todos |
| `nome_eqp` | `NOME_EQP` | texto | Nome da Equipe | — | todos |
| `id_area` | `ID_AREA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `nomearea` | `NOMEAREA` | texto | Nome da Área | — | todos |
| `id_segm` | `ID_SEGM` | texto | Código do Segmento | — | todos |
| `descsegm` | `DESCSEGM` | texto | Descrição do Segmento | — | todos |
| `tiposegm` | `TIPOSEGM` | texto | Tipo do Segmento: 1–Urbano 2–Rural | — | todos |
| `dt_ativa` | `DT_ATIVA` | texto | Ano e Mês da Data de ATIVAÇÃO da Equipe | — | todos |
| `dt_desat` | `DT_DESAT` | texto | Ano e Mês da Data de DESATIVAÇÃO da Equipe | — | todos |
| `quilombo` | `QUILOMBO` | texto | Atende População Assistida Quilombolas: 1-Sim 0-Não | — | todos |
| `assentad` | `ASSENTAD` | texto | Atende População Assistida Assentados: 1– Sim 0-Não | — | todos |
| `popgeral` | `POPGERAL` | texto | Atende População Assistida Geral: 1-Sim 0-Não | — | todos |
| `escola` | `ESCOLA` | texto | Atende População Assistida Escolares: 1-Sim 0-Não | — | todos |
| `indigena` | `INDIGENA` | texto | Atende População Assistida PRONASCI: 1-Sim 0-Não | — | todos |
| `pronasci` | `PRONASCI` | texto | Atende População Assistida Geral: 1-Sim 0-Não | — | todos |
| `motdesat` | `MOTDESAT` | texto | Código do Motivo de Desativação da Equipe Código do Tipo de Desativação da Equipe | — | todos |
| `tp_desat` | `TP_DESAT` | texto | Código do Tipo de Desativação da Equipe | — | todos |
| `competen` | `COMPETEN` | texto | 1 – Temporário 2 - Definitivo Ano e Mês de competência da informação (AAAAMM) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `nat_jur` | `NAT_JUR` | texto | Natureza Jurídica de Habilitações - Nomenclatura (HB*.dbf ) | — | 2013-12 a 2026-02 |
| `ap01cv07` | `AP01CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2021-02 a 2026-02 |
| `ap02cv07` | `AP02CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2021-02 a 2026-02 |
| `ap03cv07` | `AP03CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2021-02 a 2026-02 |
| `ap04cv07` | `AP04CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2021-02 a 2026-02 |
| `ap05cv07` | `AP05CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2021-02 a 2026-02 |
| `ap06cv07` | `AP06CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2021-02 a 2026-02 |
| `ap07cv07` | `AP07CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2021-02 a 2026-02 |

## No lake

- **Dataset no lake:** `datasus/cnes-ep`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): texto: 110.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `cnes-ep.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- para medir "equipes ativas" em uma competência é preciso filtrar as equipes vigentes (considerando `DT_ATIVA` ≤ competência e `DT_DESAT` vazio/posterior); uma mesma equipe pode mudar de tipo ou área ao longo do tempo; a cobertura da atenção básica exige combinar o `EP` com estimativas populacionais (IBGE/TAB_POP) e com as regras de ponderação da PNAB; e o mesmo estabelecimento pode ter mais de uma equipe, exigindo deduplicação por `ID_EQUIPE`. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 8 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/cnes-ep/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "mes", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "mes", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-ep
quantilica datasus list cnes-ep

# 2. Baixar microdados de cnes-ep (uf+yearmonth)
quantilica datasus sync cnes-ep -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-ep -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-ep -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-ep/2024-01/cnes-ep_202401-sp@20261015.dbc", clean=True)

# Equipes ativas por tipo
ativas = (
    qdf.filter(pl.col("dt_desat").is_null())
    .group_by("tipo_eqp")
    .agg(pl.col("id_equipe").n_unique().alias("equipes_ativas"))
    .sort("equipes_ativas", descending=True)
)
print(ativas)
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EP`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout EP) e `TAB_CNES.zip`
- **Política Nacional de Atenção Básica (PNAB)** e **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
