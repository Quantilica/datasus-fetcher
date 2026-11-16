---
dataset:
  id: sinan-chag
  fonte: datasus
  titulo: Doença de Chagas Aguda
  resumo: 'Doença de Chagas Aguda do DATASUS: uma ficha de notificação/investigação de doença de Chagas Aguda.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2000'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de doença de Chagas Aguda
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 153
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    tempo: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Doença de Chagas Aguda (`sinan-chag`)

## Resumo

O `sinan-chag` contém os microdados das notificações e investigações de casos de Doença de Chagas em fase aguda (CID-10 B57.0/B57.1/B57.2) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de Chagas agudo, digitada no SINAN Net/Sinan Online pelas unidades de saúde. Embora a cardiopatia crônica do Chagas não seja notificada no SINAN, a fase aguda da doença — especialmente via transmissão oral em surtos familiares — é de notificação compulsória imediata.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `CHAG` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `CHAG` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `CHAGBR00.dbc` — prefixo `CHAG`, `BR` (consolidação nacional) e `00` (ano 2000, primeira série do FTP); os arquivos finais vão até `CHAGBR22.dbc` (2022), com os anos recentes em `PRELIM` (ex.: `CHAGBR25.dbc`).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-chag/<AAAA>/sinan-chag_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-chag/2024/sinan-chag_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## Conteúdo

A doença de Chagas aguda (infecção pelo *Trypanosoma cruzi* com fase aguda sintomática) é de notificação compulsória imediata — em até 24 horas — conforme a lista nacional (Portaria SVS/MS nº 104/2011; consolidada na Portaria GM/MS nº 204/2016). A vigilância é gerida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), com foco na detecção de casos de transmissão vetorial (triatomíneos domiciliados e peridomiciliados), transmissão oral (consumo de açaí, caldo de cana e outros alimentos contaminados por fezes de triatomíneos — principal mecanismo atual de surtos no país), transmissão congênita e acidental (laboratorial). A base dimensiona a persistência da morbidade chagásica em áreas rurais e a emergência de transmissões por via alimentar em contexto urbano.

O evento gerador é a **Ficha de Investigação da Doença de Chagas Aguda** do SINAN (ficha `Chagas_agudo_v5`), preenchida na suspeição do caso (febre com sinais como chagoma de inoculação, sinal de Romaña, hepatoesplenomegalia) e completada com dados da investigação, exames parasitológicos/sorológicos (gota espessa, hemocultura, anticorpos IgM e IgG), identificação da via de transmissão e sorovigilância de comunicantes. A unidade de análise é o caso suspeito/confirmado individual.

Marcos históricos: a notificação compulsória da fase aguda constava já da lista da Portaria SVS/MS nº 5/2006; a expansão da transmissão oral nos anos 2000 (grandes surtos detectados a partir de 2005-2006) recalibrou os protocolos de investigação na ficha mais recente, com enfoque na investigação alimentar de surtos, e a vigilância passou a integrar o registro de insetos triatomíneos capturados; surtos de maiores dimensões podem ser registrados também no módulo de surto do SINAN.

Aplicações analíticas: coeficiente de incidência de Chagas agudo por 100 mil habitantes, distribuição por via de transmissão (vetorial, oral, congênita, acidental, transfusional), letalidade da fase aguda, mapeamento de municípios com transmissão ativa, monitoramento de surtos alimentares (ação conjunta entre vigilância epidemiológica e vigilância sanitária) e vigilância de comunicantes/famíliares infectados.

### Cobertura observada

- Índice do FTP (2026-10): 26 arquivos, de 2000 a 2025, 1 UF(s) com arquivos, última atualização em 2026-09-28.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2000 a 2025), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Doença de Chagas aguda — CID-10 B57.x) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave, compulsória em até 24h) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (febre, chagoma, sinal de Romaña etc.) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_RACA` | Inteiro | Raça/cor (1-Branca, 2-Preta, 3-Amarela, 4-Parda, 5-Indígena, 9-Ignorado) |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `CLASSI_FIN` | Inteiro | Classificação final (1 - Confirmado, 5 - Descartado ou equivalente agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento (cierre) do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação | — | todos |
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escolar` | `CS_ESCOLAR` | texto | Escolaridade do paciente (formato do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2000 |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno) | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno) | — | todos |
| `nu_idade` | `NU_IDADE` | texto | Idade do paciente (formato do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2000 |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil) | — | todos |
| `id_dg_not` | `ID_DG_NOT` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Doença de Chagas Aguda (`ID_DG_NOT`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `id_ev_not` | `ID_EV_NOT` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Doença de Chagas Aguda (`ID_EV_NOT`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `ant_dt_inv` | `ANT_DT_INV` | data | Data da investigação | — | só em 2000 |
| `ocupacao` | `OCUPACAO` | texto | Ocupação do paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2000 |
| `presenca` | `PRESENCA` | texto | Presença de vestígios de triatomídeos Intra- Domicílio | 1-sim; 2-não; 3-não | todos |
| `suspeitos` | `SUSPEITOS` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `afirmativo` | `AFIRMATIVO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `confirmad` | `CONFIRMAD` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `quantos` | `QUANTOS` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `historia` | `HISTORIA` | texto | História de uso de sangue ou hemoderivados nos últimos 120 dias | 1-sim; 2-não; 9-ignorado | todos |
| `controle` | `CONTROLE` | texto | Existência de controle sorológico na Unidade de Hemoterapia. varchar (1) | 1-sim; 2-não; 3- não se aplica 9- ignorado | todos |
| `manipula` | `MANIPULA` | texto | Manipulação de Material com T. Cruzi. varchar (1) | 1-sim; 2-não; 3-não se aplica; 9- ignorado | todos |
| `recemnasc` | `RECEMNASC` | texto | Indica se o paciente é recém-nascido (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2000 |
| `assintoma` | `ASSINTOMA` | texto | Sinais e sintomas ASSINTOMÁTICO. varchar (1) | 1-sim; 2-não; 9-ignorado | todos |
| `febre` | `FEBRE` | texto | Sinais e sintomas FEBRE PERSISTENTE | 1-sim; 2-não; 9-ignorado | todos |
| `cefaleia` | `CEFALEIA` | texto | Sinais clínicos (Cefaleia). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | só em 2000 |
| `arritmias` | `ARRITMIAS` | texto | Sinais e sintomas TAQUICARDIA PERSISTENTE. varchar (1) | 1-sim; 2-não; 9-ignorado | todos |
| `astenia` | `ASTENIA` | texto | Sinais e sintomas ASTENIA. varchar (1) | 1-sim; 2-não; 9-ignorado | todos |
| `anorexia` | `ANOREXIA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `hiporexia` | `HIPOREXIA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `sinais` | `SINAIS` | texto | Sinais e Sintomas. Informar se apresentou ou não sinais e sintomas de rubéola | 1- Apresentou Sintomas de Rubéola 2 - Não Apresentou Sintomas de Rubéola 9 - Ignorado | só em 2000 |
| `edema` | `EDEMA` | texto | Sinais e sintomas EDEMA. varchar (1) | 1-sim; 2-não; 9-ignorado | todos |
| `hepatome` | `HEPATOME` | texto | Sinais e sintomas HEPATOMEGALIA. a | 1-sim; 2-não; 9-ignorado | todos |
| `esplenom` | `ESPLENOM` | texto | Sinais e sintomas ESPLENOMEGALIA | 1-sim; 2-não; 9-ignorado | todos |
| `meningoe` | `MENINGOE` | texto | Sinais e sintomas SINAIS DE MENINGOENCEFALITE | 1-sim; 2-não; 9-ignorado | todos |
| `hepaesple` | `HEPAESPLE` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `chagoma` | `CHAGOMA` | texto | Sinais e sintomas CHAGOMA DE INOCULAÇÂO (sinal de Romana ou outro). varchar (1) | 1-sim; 2-não; 9-ignorado | todos |
| `ganglios` | `GANGLIOS` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `aumento` | `AUMENTO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `exame` | `EXAME` | texto | EXAMES REALIZADOS Parasitológico Direto Exame a Fresco. o | 1-positivo; 2-negativo; 3-não realizado; | todos |
| `xenodiag` | `XENODIAG` | texto | EXAMES REALIZADOS Parasitológico Indireto Xenodiagnóstico. varchar (1) | 1-positivo; 2-negativo; 3-não realizado; | todos |
| `hemo` | `HEMO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `imuno` | `IMUNO` | texto | Dado de exame laboratorial registrado na ficha de Doença de Chagas Aguda (`IMUNO`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `elisa` | `ELISA` | texto | Dado de exame laboratorial registrado na ficha de Doença de Chagas Aguda (`ELISA`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `ecg` | `ECG` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `ecg_result` | `ECG_RESULT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `raiox` | `RAIOX` | texto | Confirmação Diagnóstica Radiografia de tórax. Confirmação de Diagnóstico através de Radiografia de Tórax | 1 – Sim 2 – Não 9 – Ignorado | só em 2000 |
| `rai_result` | `RAI_RESULT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `especifico` | `ESPECIFICO` | texto | Tipo de Tratamento Específico. o | 1-sim; 2-não; 9-ignorado | todos |
| `inespecif` | `INESPECIF` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `droga` | `DROGA` | texto | Droga Utilizada no Tratamento Específico. varchar (1) | 1- benznidazol 2-outro | todos |
| `dosagem` | `DOSAGEM` | texto | Dado de exame laboratorial registrado na ficha de Doença de Chagas Aguda (`DOSAGEM`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `duracao` | `DURACAO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `med_contr` | `MED_CONTR` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `fiscaliza` | `FISCALIZA` | texto | Ocorreu ou Medidas Tomadas Fiscalização Sanitária em Unidade de Hemoterapia. varchar (1) | 1-sim; 2-não; 3-não se aplica; 9- ignorado | todos |
| `implanta` | `IMPLANTA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `med_outro` | `MED_OUTRO` | texto | Ocorreu ou Medidas Tomadas Outros. varchar (1) | 1-sim; 2-não; 3-não se aplica; 9- ignorado | todos |
| `con_classi` | `CON_CLASSI` | texto | Classificação da forma clínica | 1. Forma bubônica 2. Forma pneumônica 3. Forma septicêmica 4 outra | só em 2000 |
| `con_criter` | `CON_CRITER` | texto | Dado de conclusão do caso na ficha de Doença de Chagas Aguda (`CON_CRITER`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_provav` | `CON_PROVAV` | texto | Modo Provável da Infecção. varchar (1) | 1- transfusional 2-vetorial 3- transplacentá ria 4-acidental 5-oral 6-outra 9-ignorada | todos |
| `con_infecc` | `CON_INFECC` | texto | Dado de conclusão do caso na ficha de Doença de Chagas Aguda (`CON_INFECC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_inf_ou` | `CON_INF_OU` | texto | Dado de conclusão do caso na ficha de Doença de Chagas Aguda (`CON_INF_OU`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_inf_mu` | `CON_INF_MU` | texto | Dado de conclusão do caso na ficha de Doença de Chagas Aguda (`CON_INF_MU`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_inf_uf` | `CON_INF_UF` | texto | Dado de conclusão do caso na ficha de Doença de Chagas Aguda (`CON_INF_UF`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_inf_pa` | `CON_INF_PA` | texto | Dado de conclusão do caso na ficha de Doença de Chagas Aguda (`CON_INF_PA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_doenca` | `CON_DOENCA` | texto | Dado de conclusão do caso na ficha de Doença de Chagas Aguda (`CON_DOENCA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_evoluc` | `CON_EVOLUC` | texto | Dado de conclusão do caso na ficha de Doença de Chagas Aguda (`CON_EVOLUC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_dt_obi` | `CON_DT_OBI` | data | Dado de conclusão do caso na ficha de Doença de Chagas Aguda (`CON_DT_OBI`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_dt_enc` | `CON_DT_ENC` | data | Dado de conclusão do caso na ficha de Doença de Chagas Aguda (`CON_DT_ENC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `in_vincula` | `IN_VINCULA` | texto | Vinculação. 0 ou branco – Não Vinculado 1 – Vinculado | — | só em 2000 |
| `nduplic` | `NDUPLIC` | texto | Indicador de duplicidade do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2000 |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | 2007 a 2025 |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | 2007 a 2025 |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2007 a 2025 |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | 2007 a 2025 |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | 2007 a 2025 |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | 2007 a 2025 |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | 2007 a 2025 |
| `nduplic_n` | `NDUPLIC_N` | texto | Não Listar/ Não Contar. 0 ou branco – Não identificado 1 – Não é duplicidade (não listar) 2 – Duplicidade (não contar) | — | 2007 a 2025 |
| `dt_invest` | `DT_INVEST` | data | Data da investigação. Data em que ocorreu a investigação – informar a Data da 1ª visita ao paciente | — | 2007 a 2025 |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo de atividade econômica do paciente refere-se as atividades econômicas desenvolvidas nos processos de produção do setor primário (agricultura e extrativismo); secundário (indústria) ou terciário (serviços e comércio) | — | 2007 a 2025 |
| `ant_uf_1` | `ANT_UF_1` | texto | Deslocamento UF 1. varchar (2) | — | 2007 a 2025 |
| `mun_1` | `MUN_1` | texto | Deslocamento Município 1. 1 | — | 2007 a 2025 |
| `ant_uf_2` | `ANT_UF_2` | texto | Deslocamento UF 2. varchar (2) | — | 2007 a 2025 |
| `mun_2` | `MUN_2` | texto | Deslocamento Município 2. 2 | — | 2007 a 2025 |
| `ant_uf_3` | `ANT_UF_3` | texto | Deslocamento UF 3. varchar (2) | — | 2007 a 2025 |
| `mun_3` | `MUN_3` | texto | Deslocamento Município 3. 3 | — | 2007 a 2025 |
| `parasito` | `PARASITO` | data | Data do encontro dos vestígios. Data do encontro do parasito | — | 2007 a 2025 |
| `maechaga` | `MAECHAGA` | texto | Menor ou igual a 9 meses de idade: Mãe com infecção chagásica. varchar (1) | 1-sim; 2-não; 3-não se aplica; 9- ignorado | 2007 a 2025 |
| `oral` | `ORAL` | texto | Possibilidade de transmissão por via oral. varchar (1) | 1-sim; 2-não; 9-ignorado | 2007 a 2025 |
| `poliadeno` | `POLIADENO` | texto | Sinais e sintomas POLIADENOPATIA. a | 1-sim; 2-não; 9-ignorado | 2007 a 2025 |
| `sinais_icc` | `SINAIS_ICC` | texto | Sinais e sintomas SINAIS DE ICC. varchar (1) | 1-sim; 2-não; 9-ignorado | 2007 a 2025 |
| `outro_sin` | `OUTRO_SIN` | texto | Sinais e sintomas OUTROS. varchar (1) | 1-sim; 2-não; 9-ignorado | 2007 a 2025 |
| `outro_esp` | `OUTRO_ESP` | texto | Sinais e sintomas OUTROS especificar. ds-sinal_outro | — | 2007 a 2025 |
| `dt_col_dir` | `DT_COL_DIR` | data | EXAMES REALIZADOS Parasitológico Direto | — | 2007 a 2025 |
| `micro_hema` | `MICRO_HEMA` | texto | EXAMES REALIZADOS Parasitológico Direto Strout/Microhematócrito/ QBC | 1-positivo; 2-negativo 3-não realizado | 2007 a 2025 |
| `outro` | `OUTRO` | texto | EXAMES REALIZADOS Outro. ttp_parasotologico_outr o | 1-positivo; 2-negativo 3-não realizado | 2007 a 2025 |
| `dt_col_ind` | `DT_COL_IND` | data | EXAMES REALIZADOS Parasitológico Indireto Data da Coleta | — | 2007 a 2025 |
| `hemocult` | `HEMOCULT` | texto | EXAMES REALIZADOS Parasitológico Indireto Hemocultivo. varchar (1) | 1-positivo; 2-negativo; 3-não realizado; | 2007 a 2025 |
| `dt_col_s1` | `DT_COL_S1` | data | EXAMES REALIZADOS Data da Coleta S1. Data de coleta do material para realização do exame parasitológico | — | 2007 a 2025 |
| `dt_col_s2` | `DT_COL_S2` | data | EXAMES REALIZADOS Data da Coleta S2. Data de coleta do material para realização do exame parasitológico | — | 2007 a 2025 |
| `eli_igm_s1` | `ELI_IGM_S1` | texto | EXAMES REALIZADOS Resultado da Sorologia para ELISA IgM S1. varchar (1) | 1-reagente; 2-não- reagente; 3- inconclusivo | 2007 a 2025 |
| `eli_igg_s1` | `ELI_IGG_S1` | texto | EXAMES REALIZADOS Resultado da Sorologia para ELISA IgG S1. varchar (1) | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `eli_igm_s2` | `ELI_IGM_S2` | texto | EXAMES REALIZADOS Resultado da Sorologia para ELISA IgM S2. varchar (1) | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `eli_igg_s2` | `ELI_IGG_S2` | texto | EXAMES REALIZADOS Resultado da Sorologia para ELISA IgG S2. varchar (1) | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `hem_igm_s1` | `HEM_IGM_S1` | texto | EXAMES REALIZADOS Resultado da Sorologia para Hemoaglutinação IgM S1. m_s1 | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `hem_igg_s1` | `HEM_IGG_S1` | texto | EXAMES REALIZADOS Resultado da Sorologia para Hemoaglutinação IgG S1. g_s1 | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não | 2007 a 2025 |
| `hem_igm_s2` | `HEM_IGM_S2` | texto | EXAMES REALIZADOS Resultado da Sorologia para Hemoaglutinação IgM S2. m_s2 | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `hem_igg_s2` | `HEM_IGG_S2` | texto | EXAMES REALIZADOS Resultado da Sorologia para Hemoaglutinação IgG S2. g_s2 | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `imu_igm_s1` | `IMU_IGM_S1` | texto | EXAMES REALIZADOS Resultado da Imunofluorescência Indireta - IFI IgM S1. varchar (1) | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `tit_igm_s1` | `TIT_IGM_S1` | texto | EXAMES REALIZADOS Resultado da Imunofluorescência Indireta - IFI Título IgM S1. _s1 | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `imu_igm_s2` | `IMU_IGM_S2` | texto | EXAMES REALIZADOS Resultado da Imunofluorescência Indireta - IFI IgM S2. varchar (1) | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `tit_igm_s2` | `TIT_IGM_S2` | texto | EXAMES REALIZADOS Resultado da Imunofluorescência Indireta - IFI Título IgM Laboratório produtor do soro anti- rábico S2. _s2 | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `imu_igg_s1` | `IMU_IGG_S1` | texto | EXAMES REALIZADOS Resultado da Imunofluorescência Indireta - IFI IgG S1. varchar (1) | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `tit_igg_s1` | `TIT_IGG_S1` | texto | EXAMES REALIZADOS Resultado da Imunofluorescência Indireta - IFI Título IgG S1. varchar (5) | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `imu_igg_s2` | `IMU_IGG_S2` | texto | EXAMES REALIZADOS Resultado da Imunofluorescência Indireta - IFI IgG S2. varchar (1) | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `tit_igg_s2` | `TIT_IGG_S2` | texto | EXAMES REALIZADOS Resultado da Imunofluorescência Indireta - IFI Título IgG S2. _s2 | 1-reagente; 2-não- reagente; 3- inconclusivo 4-não realizado | 2007 a 2025 |
| `resul_his` | `RESUL_HIS` | data | EXAMES. Data da Coleta do exame | — | 2007 a 2025 |
| `res_hist` | `RES_HIST` | texto | EXAMES REALIZADOS Resultado do Histopatológico. varchar (1) | 1. positivo 2. negativo 3. não realizado 9. ignorado | 2007 a 2025 |
| `sintomatic` | `SINTOMATIC` | texto | Tipo de Tratamento Sintomático | 1-sim; 2-não; 9-ignorado | 2007 a 2025 |
| `tempo` | `TEMPO` | inteiro | Tempo de Tratamento | — | 2007 a 2025 |
| `con_triat` | `CON_TRIAT` | texto | Ocorreu ou Medidas Tomadas Controle de Triatomídeos. varchar (1) | 1-sim; 2-não; 3-não se aplica; 9- ignorado | 2007 a 2025 |
| `biosseg` | `BIOSSEG` | texto | Ocorreu ou Medidas. varchar (1) | 1-sim; 2-não; | 2007 a 2025 |
| `outro_des` | `OUTRO_DES` | texto | Ocorreu ou Medidas Tomadas Outros, especifique. varchar (30) | — | 2007 a 2025 |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação Final. varchar (1) | 1-confirmado 2-descartado | 2007 a 2025 |
| `criterio` | `CRITERIO` | texto | Critério de Confirmação/Descart e. varchar (1) | 1-laboratório 2-clínico- epidemiológic o 3-clínico | 2007 a 2025 |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. varchar (1) | 1 – vivo 2- óbito por chagas 3- óbito por outras causas 9- ignorado | 2007 a 2025 |
| `dt_obito` | `DT_OBITO` | data | Data do Óbito. Informar a data do óbito | — | 2007 a 2025 |
| `con_outra` | `CON_OUTRA` | texto | Modo Provável da Infecção Outra especificar | — | 2007 a 2025 |
| `con_local` | `CON_LOCAL` | texto | Local Provável de Infecção (no período de 90 dias). varchar (1) | 1-unidade de hemoterapia; 2-domicílio; | 2007 a 2025 |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência?. a | 1 – sim 2 – não 3 – indeterminad o | 2007 a 2025 |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o paciente foi provavelmente infectado | — | 2007 a 2025 |
| `copaisinf` | `COPAISINF` | texto | País (provável da. País onde o paciente foi | — | 2007 a 2025 |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). Código do município onde o paciente foi provavelmente infectado. O nome está associado ao código na tabela de municípios | — | 2007 a 2025 |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao Trabalho. varchar (1) | 1 – sim 2 – não 9 – ignorado | 2007 a 2025 |
| `dt_encerra` | `DT_ENCERRA` | data | Data do Encerramento. Informar a data do encerramento do caso | — | 2007 a 2025 |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | 2007 a 2025 |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | 2007 a 2025 |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | 2007 a 2025 |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | 2007 a 2025 |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | 2007 a 2025 |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | 2007 a 2025 |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | 2007 a 2025 |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | 2007 a 2025 |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | 2007 a 2025 |

## No lake

- **Dataset no lake:** `datasus/sinan-chag`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 21, inteiro: 2, nulo (vazio nas amostras): 10, texto: 130.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-chag.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- o volume é baixo e disperso (26 consolidações `BR` anuais de ~5 MB), com poucos casos por ano — o cálculo de coeficientes por 100 mil habitantes exige denominadores precisos; os arquivos finais vão até 2022 e os anos recentes aparecem apenas em `PRELIM`, sinalizando que os dados mais recentes podem ser revisados; surtos alimentares e vetoriais são caracterizados apenas nos campos de investigação específicos da ficha, que frequentemente ficam incompletos. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 117 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-chag").glob("**/*.parquet"))
dados = pl.concat(  # períodos diferentes têm colunas e tipos diferentes
    [pl.scan_parquet(a, hive_partitioning=True) for a in arquivos],
    how="diagonal_relaxed",
)

(
    dados.group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Pela linha de comando (`datasus-fetcher`)

```bash
# o que o FTP publica para o dataset (arquivos e tamanho)
datasus-fetcher list sinan-chag

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-chag -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-chag
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Doença de Chagas Aguda**: https://portalsinan.saude.gov.br/doenca-de-chagas-aguda
- **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo Doença de Chagas aguda; **Portaria GM/MS nº 204/2016**
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
