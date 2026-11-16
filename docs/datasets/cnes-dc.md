---
dataset:
  id: cnes-dc
  fonte: datasus
  titulo: Dados Complementares
  resumo: 'Dados Complementares do DATASUS: um estabelecimento de saúde (dados complementares), em uma competência.'
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2005-08
    fim: em-curso
  unidade: um estabelecimento de saúde (dados complementares), em uma competência
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
    colunas: 173
  unidades_de_medida:
    s_hbsagp: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_hbsagn: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_dpi: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_dpac: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_reagp: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_reagn: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_rehcv: 'número inteiro: contagem ou código numérico (ver Descrição)'
    maq_prop: 'número inteiro: contagem ou código numérico (ver Descrição)'
    maq_outr: 'número inteiro: contagem ou código numérico (ver Descrição)'
    simul_rd: 'número inteiro: contagem ou código numérico (ver Descrição)'
    planj_rd: 'número inteiro: contagem ou código numérico (ver Descrição)'
    armaz_ft: 'número inteiro: contagem ou código numérico (ver Descrição)'
    conf_mas: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sala_mol: 'número inteiro: contagem ou código numérico (ver Descrição)'
    blocoper: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_armaze: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_prepar: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_qcdura: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_qldura: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_cpflux: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_simula: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_acell6: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_alseme: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_alcome: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ortv1050: 'número inteiro: contagem ou código numérico (ver Descrição)'
    orv50150: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ov150500: 'número inteiro: contagem ou código numérico (ver Descrição)'
    un_cobal: 'número inteiro: contagem ou código numérico (ver Descrição)'
    eqbrbaix: 'número inteiro: contagem ou código numérico (ver Descrição)'
    eqbrmedi: 'número inteiro: contagem ou código numérico (ver Descrição)'
    eqbralta: 'número inteiro: contagem ou código numérico (ver Descrição)'
    eq_marea: 'número inteiro: contagem ou código numérico (ver Descrição)'
    eq_mindi: 'número inteiro: contagem ou código numérico (ver Descrição)'
    eqsispln: 'número inteiro: contagem ou código numérico (ver Descrição)'
    eqdoscli: 'número inteiro: contagem ou código numérico (ver Descrição)'
    eqfonsel: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_recepc: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_trihmt: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_tricli: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_coleta: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_aferes: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_preest: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_proces: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_estoqu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_distri: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_sorolo: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_imunoh: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_pretra: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_hemost: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_contrq: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_biomol: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_imunfe: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_transf: 'número inteiro: contagem ou código numérico (ver Descrição)'
    s_sgdoad: 'número inteiro: contagem ou código numérico (ver Descrição)'
    qt_cadre: quantidade
    qt_cenre: quantidade
    qt_refsa: quantidade
    qt_conra: quantidade
    qt_extpl: quantidade
    qt_fre18: quantidade
    qt_fre30: quantidade
    qt_agipl: quantidade
    qt_selad: quantidade
    qt_irrhe: quantidade
    qt_agltn: quantidade
    qt_maqaf: quantidade
    qt_refre: quantidade
    qt_refas: quantidade
    qt_capfl: quantidade
  dados_pessoais:
  - coluna: cpf_cnpj
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  - coluna: cns_oped
    categoria: Cartão Nacional de Saúde (CNS)
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Dados Complementares (`cnes-dc`)

## Resumo

O `cnes-dc` contém os microdados do arquivo de **Dados Complementares** do Cadastro Nacional de Estabelecimentos de Saúde (CNES). Cada registro (linha) representa um estabelecimento de saúde em uma competência mensal, com os atributos cadastrais complementares ao arquivo de Estabelecimentos (`ST`) — gestão, natureza jurídica e, sobretudo, a infraestrutura especializada declarada (hemoterapia, diálise, radioterapia, quimioterapia e perfusionistas) e os tipos de atendimento/conveniados prestados (`AP*CV*`). É a tabela que detalha a capacidade de alta complexidade e o perfil de atendimento do estabelecimento.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/DC` | `DC` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `DCSP2401.dbc` — `DC` é o prefixo de Dados Complementares, `SP` a UF, `24` o ano e `01` o mês de competência. Existem também arquivos `DCBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-dc/<AAAAMM>/cnes-dc_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/cnes-dc/202401/cnes-dc_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Dados Complementares — DC*.dbf") e o pacote de domínios `TAB_CNES.zip`.

## Conteúdo

O arquivo `DC` é parte do mesmo sistema CNES (ver `cnes-st`), gerido pelo Ministério da Saúde via Secretaria Executiva/DATASUS e mantido pelos gestores estaduais e municipais. O CNES foi criado pela Portaria SAS/MS nº 403/2000, teve a FCES aprovada pela Portaria SAS/MS nº 511/2000 e foi reinstituído pela Portaria GM/MS nº 1.646/2015. Enquanto o `ST` traz a identidade, localização e classificação geral do estabelecimento, o `DC` aprofunda os requisitos de habilitação sanitária para procedimentos de alta complexidade e a caracterização dos atendimentos.

O **evento gerador** é o preenchimento/atualização da FCES no SCNES, na qual o estabelecimento declara se possui os requisitos físicos e de recursos humanos exigidos para determinadas políticas (por exemplo, diálise e hemoterapia, com campos como `DIALISE`, `HEMOTERA`, `QUIMRADI` e as quantidades de salas). A **unidade de análise é o estabelecimento na competência** (`CNES` + `COMPETEN`). Os campos `AP01CV*` a `AP07CV*` indicam, para sete grandes grupos de atendimento (internação, ambulatorial, SADT, urgência, outros, vigilância em saúde e regulação), se o estabelecimento atende aos convênios SUS, particular, plano de saúde público, plano de saúde privado, plano-seguro próprio e plano-seguro de terceiros.

Historicamente o arquivo `DC` acumulou colunas de diferentes ciclos do CNES — do cadastro de salas de hemodiálise, hemoterapia e dos requisitos de oncologia (radioterapia/quimioterapia) — e inclui os CNS dos responsáveis técnicos dessas áreas. Não há diretório preliminar; as bases são publicadas consolidadas por competência.

Aplicações analíticas típicas: identificação de serviços habilitados em alta complexidade (diálise, hemoterapia, oncologia), análise da oferta de atendimento por tipo de convênio (SUS vs. saúde suplementar), cálculo de capacidade de salas de procedimentos e apoio à regulação assistencial e à programação de políticas de alta complexidade.

### Cobertura observada

- Índice do FTP (2026-10): 6858 arquivos, de 2005-08 a 2026-09, 27 UF(s) com arquivos, última atualização em 2026-10-15.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2005-10 a 2026-07), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (7) | Código do município do estabelecimento: UF + MUNIC (sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `PF_PJ` | String (1) | Indicador de pessoa: 1 - Física, 3 - Jurídica |
| `NIV_DEP` | String (1) | Grau de dependência: 1 - Individual, 3 - Mantida |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `NAT_JUR` | String (4) | Natureza jurídica |
| `DIALISE` | String (1) | Indica requisito de diálise para o CNES: 1 - Sim, 0 - Não |
| `HEMOTERA` | String (1) | Indica requisito de hemoterapia: 1 - Sim, 0 - Não |
| `QUIMRADI` | String (1) | Indica requisito de quimio/radioterapia: 1 - Sim, 0 - Não |
| `CNS_NEFR` | String (15) | CNS do médico nefrologista responsável |
| `S_HBSAGP` / `S_DPI` | Inteiro | Quantidade de salas HBsAG+ / de diálise peritoneal (DPI) |
| `AP01CV01` .. `AP07CV04` | String (1) | Tipos de atendimento prestado por grupo e convênio (1 - Sim, 0 - Não) |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `cnes` | `CNES` | texto | de Dados Complementares - Nomenclatura (DC*.dbf) DESCRIÇÃO Número nacional do estabelecimento de saúde | — | todos |
| `codufmun` | `CODUFMUN` | texto | Código do município do estabelecimento: UF + MUNIC (sem dígito) | — | todos |
| `cpf_cnpj` | `CPF_CNPJ` | texto | CPF do estabelecimento, caso pessoa física ou CNPJ, caso pessoa jurídica | — | todos |
| `pf_pj` | `PF_PJ` | texto | Indicador de pessoa: 1-Física 3-Jurídica | — | todos |
| `niv_dep` | `NIV_DEP` | texto | Grau de dependência, onde: 1-Individual 3-Mantida | — | todos |
| `cnpj_man` | `CNPJ_MAN` | texto | CNPJ da mantenedora do estabelecimento. | — | todos |
| `cod_ir` | `COD_IR` | texto | Indica o tipo de retenção de tributos da mantenedora | — | todos |
| `regsaude` | `REGSAUDE` | texto | Código da região de saúde NOAS | — | todos |
| `micr_reg` | `MICR_REG` | texto | Código da micro-região de saúde NOAS | — | todos |
| `distrsan` | `DISTRSAN` | texto | Código do distrito sanitário | — | todos |
| `vinc_sus` | `VINC_SUS` | texto | Vínculo com SUS: 1-Sim 0-Não | — | todos |
| `distradm` | `DISTRADM` | texto | Inicialmente chamado Distrito Administrativo, atualmente Código do Módulo Assistencial conforme tabela local, em conformidade com o Plano Diretor de Regionalização do Estado/Município. | — | todos |
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
| `s_hbsagp` | `S_HBSAGP` | inteiro | Quantidade de salas HBsAg+ (de hemodiálise) | — | todos |
| `s_hbsagn` | `S_HBSAGN` | inteiro | Quantidade de salas HBsAG- | — | todos |
| `s_dpi` | `S_DPI` | inteiro | Quantidade de salas DPI | — | todos |
| `s_dpac` | `S_DPAC` | inteiro | Quantidade de salas DPAC | — | todos |
| `s_reagp` | `S_REAGP` | inteiro | Quantidade de salas de reuso de HBsAG+ | — | todos |
| `s_reagn` | `S_REAGN` | inteiro | Quantidade de salas de reuso de HBsAG- Quantidade de Salas de reuso de HCV+ | — | todos |
| `s_rehcv` | `S_REHCV` | inteiro | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `maq_prop` | `MAQ_PROP` | inteiro | Quantidade de máquinas de proporção | — | todos |
| `maq_outr` | `MAQ_OUTR` | inteiro | Quantidade de outras máquinas | — | todos |
| `f_areia` | `F_AREIA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `f_carvao` | `F_CARVAO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `abrandad` | `ABRANDAD` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `deioniza` | `DEIONIZA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `osmose_r` | `OSMOSE_R` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `out_trat` | `OUT_TRAT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `cns_nefr` | `CNS_NEFR` | texto | CNS do MÉDICO NEFROLOGISTA RESPONSÀVEL | — | todos |
| `dialise` | `DIALISE` | texto | Indica a existência de algum REQUISITO DE DIÁLISE para este CNES, onde: 1-Sim 0-Não | — | todos |
| `simul_rd` | `SIMUL_RD` | inteiro | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `planj_rd` | `PLANJ_RD` | inteiro | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `armaz_ft` | `ARMAZ_FT` | inteiro | Número de salas de armazenamento de fontes - (Radioterapia) | — | todos |
| `conf_mas` | `CONF_MAS` | inteiro | Número de salas confecção masc. - (Radioterapia) | — | todos |
| `sala_mol` | `SALA_MOL` | inteiro | Número de salas de salas de molde - (Radioterapia) | — | todos |
| `blocoper` | `BLOCOPER` | inteiro | Número de salas de bloco personalizado - (Radioterapia) | — | todos |
| `s_armaze` | `S_ARMAZE` | inteiro | Número de salas de armazenagem | — | todos |
| `s_prepar` | `S_PREPAR` | inteiro | Número de salas de preparo | — | todos |
| `s_qcdura` | `S_QCDURA` | inteiro | Salas/Equipamentos de Quimio Curta duração | — | todos |
| `s_qldura` | `S_QLDURA` | inteiro | Salas/Equipamentos de Quimio de Longa Duração | — | todos |
| `s_cpflux` | `S_CPFLUX` | inteiro | Salas/Equipamentos de Capela Fluxo Laminar | — | todos |
| `s_simula` | `S_SIMULA` | inteiro | Quantidade de Simuladores | — | todos |
| `s_acell6` | `S_ACELL6` | inteiro | Quantidade de Acelerador Linear até 6 MeV | — | todos |
| `s_alseme` | `S_ALSEME` | inteiro | Quantidade de Acelerador Linear maior 6 MeV sem elétrons | — | todos |
| `s_alcome` | `S_ALCOME` | inteiro | Quantidade de acelerador linear maior 6 MeV com elétrons | — | todos |
| `ortv1050` | `ORTV1050` | inteiro | Quantidade de Equipamentos de Ortovoltagem 10-50 KV | — | todos |
| `orv50150` | `ORV50150` | inteiro | Quantidade de Equipamentos de Ortovoltagem 50-150 KV | — | todos |
| `ov150500` | `OV150500` | inteiro | Quantidade de Equipamentos de Ortovoltagem 150-500 KV | — | todos |
| `un_cobal` | `UN_COBAL` | inteiro | Quantidade de Unidade de Cobalto | — | todos |
| `eqbrbaix` | `EQBRBAIX` | inteiro | Quantidade de Equipamentos de Braquiterapia Baixa | — | todos |
| `eqbrmedi` | `EQBRMEDI` | inteiro | Quantidade de Equipamentos de Braquiterapia Média | — | todos |
| `eqbralta` | `EQBRALTA` | inteiro | Quantidade de Equipamentos de Braquiterapia Alta | — | todos |
| `eq_marea` | `EQ_MAREA` | inteiro | Quantidade de Monitor de Área | — | todos |
| `eq_mindi` | `EQ_MINDI` | inteiro | Quantidade de Monitor Individual | — | todos |
| `eqsispln` | `EQSISPLN` | inteiro | Quantidade de sistema de Computação para Planejamento | — | todos |
| `eqdoscli` | `EQDOSCLI` | inteiro | Quantidade de dosímetro clínico | — | todos |
| `eqfonsel` | `EQFONSEL` | inteiro | Quantidade de fontes seladas | — | todos |
| `cns_adm` | `CNS_ADM` | texto | CNS do médico responsável – ADMINISTRADOR OU RESPONSÁVEL TÉCNICO | — | todos |
| `cns_oped` | `CNS_OPED` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `cns_conc` | `CNS_CONC` | texto | CNS do médico responsável - por CIRURGIA ONCOLÓGICA | — | todos |
| `cns_oclin` | `CNS_OCLIN` | texto | CNS do médico responsável - ONCOLOGISTA CLÍNICO | — | todos |
| `cns_mrad` | `CNS_MRAD` | texto | CNS do médico responsável - RADIOTERAPEUTA | — | todos |
| `cns_fnuc` | `CNS_FNUC` | texto | CNS do médico responsável - FÍSICO NUCLEAR Indica a existência de algum REQUISITO DE QUÍMIO/RÁDIO para este CNES, onde: | — | todos |
| `quimradi` | `QUIMRADI` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `s_recepc` | `S_RECEPC` | inteiro | 1-Sim 0-Não Número de salas de recepção | — | todos |
| `s_trihmt` | `S_TRIHMT` | inteiro | Número de salas de triagem hematológica | — | todos |
| `s_tricli` | `S_TRICLI` | inteiro | Número de salas de triagem clínica | — | todos |
| `s_coleta` | `S_COLETA` | inteiro | Número de salas de coleta | — | todos |
| `s_aferes` | `S_AFERES` | inteiro | Número de salas de aférese | — | todos |
| `s_preest` | `S_PREEST` | inteiro | Número de salas de pré-estoque | — | todos |
| `s_proces` | `S_PROCES` | inteiro | Número de salas de processamento | — | todos |
| `s_estoqu` | `S_ESTOQU` | inteiro | Número de salas de estoque | — | todos |
| `s_distri` | `S_DISTRI` | inteiro | Número de salas de distribuição | — | todos |
| `s_sorolo` | `S_SOROLO` | inteiro | Número de salas de sorologia | — | todos |
| `s_imunoh` | `S_IMUNOH` | inteiro | Número de salas de imunohematologia | — | todos |
| `s_pretra` | `S_PRETRA` | inteiro | Número de salas pré-transfusionais | — | todos |
| `s_hemost` | `S_HEMOST` | inteiro | Número de salas hemostasia | — | todos |
| `s_contrq` | `S_CONTRQ` | inteiro | Número de salas de controle de qualidade | — | todos |
| `s_biomol` | `S_BIOMOL` | inteiro | Número de salas de biologia molecular | — | todos |
| `s_imunfe` | `S_IMUNFE` | inteiro | Número de salas de imunofenotipágem | — | todos |
| `s_transf` | `S_TRANSF` | inteiro | Número de salas de transfusão | — | todos |
| `s_sgdoad` | `S_SGDOAD` | inteiro | Número de salas seguimento doador | — | todos |
| `qt_cadre` | `QT_CADRE` | inteiro | Quantidade de cadeiras reclináveis | — | todos |
| `qt_cenre` | `QT_CENRE` | inteiro | Quantidade de centrífugas refrigeradas | — | todos |
| `qt_refsa` | `QT_REFSA` | inteiro | Quantidade de refrigeradores para guarda de sangue | — | todos |
| `qt_conra` | `QT_CONRA` | inteiro | Quantidade de congeladores rápidos | — | todos |
| `qt_extpl` | `QT_EXTPL` | inteiro | Quantidade de extratores automáticos de plasma | — | todos |
| `qt_fre18` | `QT_FRE18` | inteiro | Quantidade de freezers –18ºC | — | todos |
| `qt_fre30` | `QT_FRE30` | inteiro | Quantidade de freezers -30ºC | — | todos |
| `qt_agipl` | `QT_AGIPL` | inteiro | Quantidade de agitadores de plaquetas | — | todos |
| `qt_selad` | `QT_SELAD` | inteiro | Quantidade de seladoras | — | todos |
| `qt_irrhe` | `QT_IRRHE` | inteiro | Quantidade de irradiadores de hemocomponentes | — | todos |
| `qt_agltn` | `QT_AGLTN` | inteiro | Quantidade de aglutinoscópio | — | todos |
| `qt_maqaf` | `QT_MAQAF` | inteiro | Quantidade de máquinas de aférese | — | todos |
| `qt_refre` | `QT_REFRE` | inteiro | Quantidade de refrigeradores para guarda de reagentes | — | todos |
| `qt_refas` | `QT_REFAS` | inteiro | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `qt_capfl` | `QT_CAPFL` | inteiro | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `cns_hmtr` | `CNS_HMTR` | texto | CNS do médico responsável - HEMOTERAPEUTA | — | todos |
| `cns_hmtl` | `CNS_HMTL` | texto | CNS do médico responsável - HEMATOLOGISTA | — | todos |
| `cns_cres` | `CNS_CRES` | texto | CNS do médico capacitado RESPONSÀVEL | — | todos |
| `cns_rtec` | `CNS_RTEC` | texto | CNS do responsável TÉCNICO / SOROLOGIA | — | todos |
| `hemotera` | `HEMOTERA` | texto | Indica a existência de algum REQUISITO DE HEMOTERAPIA para este CNES, onde: 1-Sim 0-Não | — | todos |
| `ap01cv01` | `AP01CV01` | texto | Atendimento prestado INTERNAÇÃO/Convenio SUS, onde: 1-Sim 0-Não | — | todos |
| `ap01cv02` | `AP01CV02` | texto | Atendimento prestado INTERNAÇÃO/Convenio PARTICULAR, onde: 1-Sim 0-Não | — | todos |
| `ap01cv05` | `AP01CV05` | texto | Atendimento prestado INTERNAÇÃO/Convenio PLANO de SAUDE PUBLICO, onde: 1-Sim 0-Não | — | todos |
| `ap01cv06` | `AP01CV06` | texto | Atendimento prestado INTERNAÇÃO/Convenio PLANO de SAUDE PRIVADO, onde: 1-Sim 0-Não | — | todos |
| `ap01cv03` | `AP01CV03` | texto | Atendimento prestado INTERNAÇÃO/Convenio PLANO-SEGURO PROPRIO, onde: 1-Sim 0-Não | — | todos |
| `ap01cv04` | `AP01CV04` | texto | Atendimento prestado INTERNAÇÃO/Convenio PLANO-SEGURO TERCEIRO, onde: 1-Sim 0-Não | — | todos |
| `ap02cv01` | `AP02CV01` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio SUS, onde: 1-Sim 0-Não | — | todos |
| `ap02cv02` | `AP02CV02` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PARTICULAR, onde: 1-Sim 0-Não | — | todos |
| `ap02cv05` | `AP02CV05` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO de SAUDE PUBLICO, onde: 1-Sim 0-Não | — | todos |
| `ap02cv06` | `AP02CV06` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO de SAUDE PRIVADO, onde: 1-Sim 0-Não | — | todos |
| `ap02cv03` | `AP02CV03` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO- SEGURO PROPRIO, onde: 1-Sim 0-Não | — | todos |
| `ap02cv04` | `AP02CV04` | texto | Atendimento prestado ATENDIMENTO AMBULATORIAL/Convenio PLANO- SEGURO TERCEIRO, onde: 1-Sim 0-Não | — | todos |
| `ap03cv01` | `AP03CV01` | texto | Atendimento prestado SADT/Convenio SUS, onde: 1-Sim 0-Não | — | todos |
| `ap03cv02` | `AP03CV02` | texto | Atendimento prestado SADT/Convenio PARTICULAR, onde: 1-Sim 0-Não | — | todos |
| `ap03cv05` | `AP03CV05` | texto | Atendimento prestado SADT/Convenio PLANO de SAUDE PUBLICO, onde: 1-Sim 0-Não | — | todos |
| `ap03cv06` | `AP03CV06` | texto | Atendimento prestado SADT/Convenio PLANO de SAUDE PRIVADO, onde: 1-Sim 0-Não | — | todos |
| `ap03cv03` | `AP03CV03` | texto | Atendimento prestado SADT/Convenio PLANO-SEGURO PROPRIO, onde: 1-Sim 0-Não | — | todos |
| `ap03cv04` | `AP03CV04` | texto | Atendimento prestado SADT/Convenio PLANO-SEGURO TERCEIRO, onde: 1-Sim 0-Não | — | todos |
| `ap04cv01` | `AP04CV01` | texto | Atendimento prestado URGENCIA/Convenio SUS, onde: 1-Sim 0-Não | — | todos |
| `ap04cv02` | `AP04CV02` | texto | Atendimento prestado URGENCIA/Convenio PARTICULAR, onde: 1-Sim 0-Não | — | todos |
| `ap04cv05` | `AP04CV05` | texto | Atendimento prestado URGENCIA/Convenio PLANO de SAUDE PUBLICO, onde: 1-Sim 0-Não | — | todos |
| `ap04cv06` | `AP04CV06` | texto | Atendimento prestado URGENCIA/Convenio PLANO de SAUDE PRIVADO, onde: 1-Sim 0-Não | — | todos |
| `ap04cv03` | `AP04CV03` | texto | Atendimento prestado URGENCIA/Convenio PLANO-SEGURO PROPRIO, onde: 1-Sim 0-Não | — | todos |
| `ap04cv04` | `AP04CV04` | texto | Atendimento prestado URGENCIA/Convenio PLANO-SEGURO TERCEIRO, onde: 1-Sim 0-Não | — | todos |
| `ap05cv01` | `AP05CV01` | texto | Atendimento prestado OUTROS/Convenio SUS, onde: 1-Sim 0-Não | — | todos |
| `ap05cv02` | `AP05CV02` | texto | Atendimento prestado OUTROS/Convenio PARTICULAR, onde: 1-Sim 0-Não | — | todos |
| `ap05cv05` | `AP05CV05` | texto | Atendimento prestado OUTROS/Convenio PLANO de SAUDE PUBLICO, onde: 1-Sim 0-Não | — | todos |
| `ap05cv06` | `AP05CV06` | texto | Atendimento prestado OUTROS/Convenio PLANO de SAUDE PRIVADO, onde: 1-Sim 0-Não | — | todos |
| `ap05cv03` | `AP05CV03` | texto | Atendimento prestado OUTROS/Convenio PLANO-SEGURO PROPRIO, onde: 1-Sim 0-Não | — | todos |
| `ap05cv04` | `AP05CV04` | texto | Atendimento prestado OUTROS/Convenio PLANO-SEGURO TERCEIRO, onde: 1-Sim 0-Não | — | todos |
| `ap06cv01` | `AP06CV01` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio SUS, onde: 1-Sim 0-Não | — | todos |
| `ap06cv02` | `AP06CV02` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio PARTICULAR, onde: 1-Sim 0-Não | — | todos |
| `ap06cv05` | `AP06CV05` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO de SAUDE PUBLICO, onde: 1-Sim 0-Não | — | todos |
| `ap06cv06` | `AP06CV06` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO de SAUDE PRIVADO, onde: 1-Sim 0-Não | — | todos |
| `ap06cv03` | `AP06CV03` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO-SEGURO PROPRIO, onde: 1-Sim 0-Não | — | todos |
| `ap06cv04` | `AP06CV04` | texto | Atendimento prestado VIGILANCIA EM SAUDE/Convenio PLANO-SEGURO TERCEIRO, onde: 1-Sim 0-Não | — | todos |
| `ap07cv01` | `AP07CV01` | texto | Atendimento prestado REGULACAO/Convenio SUS, onde: 1-Sim 0-Não | — | todos |
| `ap07cv02` | `AP07CV02` | texto | Atendimento prestado REGULACAO/Convenio PARTICULAR, onde: 1-Sim 0-Não | — | todos |
| `ap07cv05` | `AP07CV05` | texto | Atendimento prestado REGULACAO/Convenio PLANO de SAUDE PUBLICO, onde: 1-Sim 0-Não | — | todos |
| `ap07cv06` | `AP07CV06` | texto | Atendimento prestado REGULACAO/Convenio PLANO de SAUDE PRIVADO, onde: 1-Sim 0-Não | — | todos |
| `ap07cv03` | `AP07CV03` | texto | Atendimento prestado REGULACAO/Convenio PLANO-SEGURO PROPRIO, onde: 1-Sim 0-Não | — | todos |
| `ap07cv04` | `AP07CV04` | texto | Atendimento prestado REGULACAO/Convenio PLANO-SEGURO TERCEIRO, onde: 1-Sim 0-Não | — | todos |
| `atend_pr` | `ATEND_PR` | texto | Indica a existência de algum atendimento prestado para este CNES, onde: 1-sim / 0-não | — | todos |
| `gesprg3e` | `GESPRG3E` | texto | Indicador se a gestão do programa é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg3m` | `GESPRG3M` | texto | Indicador se a gestão do programa é MUNICIPAL, onde: 1-sim 0-não | — | todos |
| `gesprg4e` | `GESPRG4E` | texto | Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é ESTADUAL, onde: 1-Sim 0-Não | — | todos |
| `gesprg4m` | `GESPRG4M` | texto | Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção AMBULATORIAL é MUNICIPAL, onde: 1-Sim 0-Não | — | todos |
| `gesprg6e` | `GESPRG6E` | texto | Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção HOSPITALAR é ESTADUAL, onde: 1-sim 0-não | — | todos |
| `gesprg6m` | `GESPRG6M` | texto | Indicador se a gestão da atividade ALTA COMPLEXIDADE do Nível de Atenção HOSPITALAR é MUNICIPAL, onde: 1-Sim 0-Não | — | todos |
| `nivate_a` | `NIVATE_A` | texto | Indica a existência de Nível de Atenção AMBULATORIAL, de gestão Municipal/Estadual, para este CNES, onde: 1-sim 0-não | — | todos |
| `nivate_h` | `NIVATE_H` | texto | Indica a existência de Nível de Atenção HOSPITALAR, de gestão Municipal/Estadual, para este CNES, onde: 1-sim 0-não | — | todos |
| `competen` | `COMPETEN` | texto | Ano e Mês de competência da informação (AAAAMM) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `nat_jur` | `NAT_JUR` | texto | Natureza Jurídica de Profissionais - Nomenclatura (PF*.dbf) | — | 2016-08 a 2026-07 |
| `ap01cv07` | `AP01CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-07 |
| `ap02cv07` | `AP02CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-07 |
| `ap03cv07` | `AP03CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-07 |
| `ap04cv07` | `AP04CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-07 |
| `ap05cv07` | `AP05CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-07 |
| `ap06cv07` | `AP06CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-07 |
| `ap07cv07` | `AP07CV07` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026-07 |

## No lake

- **Dataset no lake:** `datasus/cnes-dc`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): inteiro: 69, texto: 104.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `cnes-dc.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- o leiaute do `DC` mudou bastante ao longo dos anos (blocos de salas de radioterapia, hemoterapia e diálise foram acrescentados em competências distintas), de modo que nem todas as colunas existem em todas as competências — a leitura deve tolerar schema variável; os muitos campos `AP*CV*` exigem dicionário para decodificar grupo de atendimento + convênio; e o `DC` só cobre estabelecimentos que declaram essas características, devendo ser sempre lido em conjunto com o `ST`. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 8 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/cnes-dc").glob("**/*.parquet"))
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
datasus-fetcher list cnes-dc

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync cnes-dc -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset cnes-dc
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/DC`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout DC) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
