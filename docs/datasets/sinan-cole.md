---
dataset:
  id: sinan-cole
  fonte: datasus
  titulo: Cólera
  resumo: O sinan-cole contém os microdados das notificações e investigações epidemiológicas de casos de Cólera (CID-10 A00) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde.
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de cólera
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 83
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    pa_des1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    pa_des2: 'número inteiro: contagem ou código numérico (ver Descrição)'
    pa_des3: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: dt_nasc
    categoria: data de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Cólera (`sinan-cole`)

## Resumo

O `sinan-cole` contém os microdados das notificações e investigações epidemiológicas de casos de Cólera (CID-10 A00) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de cólera, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. É uma base de incidência muito baixa no país atual (desde a introdução do *Vibrio cholerae* em 1991 os casos se concentraram em episódios isolados), com leiaute detalhado de investigação (91 colunas na ficha v5.0): quadro diarréico agudo, desidratação, coleta de fezes/vômito para cultura e sorotipagem, antibióticos, tipo de reidratação (oral/venosa) e fonte provável de infecção.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2007 a 2025, com o ano de 2023 ausente no FTP (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 18 arquivos (~49 KB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim (diretório `PRELIM`)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `COLE` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `COLE` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `COLEBR24.dbc` — `COLE` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `24` é o ano de notificação (2024). As consolidações até 2022 estão em `FINAIS` e os anos de 2024 a 2025 estão apenas em `PRELIM` (ex.: `COLEBR25.dbc`); **o arquivo de 2023 não consta no FTP** (lacuna verificável no inventário `index.json`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-cole/<ano>/sinan-cole_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-cole/2025/sinan-cole_preliminar_2025-br@20260120.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

O cólera é agravo de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, integrando hoje a Lista Nacional de Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), com apoio da rede de laboratórios de referência (Fiocruz/IOC), sob o alerta precoce para reintrodução do agente na região das Américas — onde a doença permanece recorrente em países próximos (Haiti, Peru e outras transmissões recentes). Com transmissão endêmica extinta no Brasil, a base serve principalmente ao registro de casos isolados/importados, à vigilância de surtos episódicos e ao monitoramento da qualidade da rede de diagnóstico de *Vibrio cholerae*.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Cólera** do SINAN. A notificação nasce com a suspeição clínica (diarreia aguda profusa — "água de arroz" — com ou sem desidratação e choque) e é completada ao longo da investigação com sintomas (diarreia, câimbras, vômitos, presença de sangue e muco nas fezes), o grau de desidratação/choque (`CS_CHOQUE`), a coleta de material para cultura (`CS_MATERIA`/`CS_VOMITO`, `DT_COLETA`), resultado da cultura e sorotipagem (`CS_RESULTA`/`CS_POSITIV`/`CS_NEG_ESP`), antibiótico e reidratação (`CS_REIDRAT`: via oral ou venosa), e a fonte provável de infecção (contatos e vínculos de surto: `FC_CONTATO`, `VINCULO`). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo, e as consolidações até 2022 foram publicadas em `FINAIS`, com os anos de 2024 e 2025 apenas em `PRELIM`. Há uma lacuna no FTP: **o arquivo referente a 2023 não está disponível** (nem em `FINAIS` nem em `PRELIM`) — a série anual tem uma quebra que deve ser tratada em agregações. Revisões do dicionário datam de fevereiro/2012 (incluindo o bloco de desdobrams com fontes de água/alimentos e contatos).

Aplicações analíticas típicas: vigilância de casos isolados/importados (com fonte provável de infecção em `COUFINF`/`COPAISINF`/`COMUNINF`); investigação de surtos de diarreia aguda por vínculo epidemiológico (`FC_CONTATO`, `VINCULO`); percentual de casos hospitalizados e letalidade; e o registro de casos confirmados laboratorialmente (cultura e sorotipagem O1/O139), indicador da capacidade da rede de laboratórios de referência.

### Cobertura observada

- Índice do FTP (2026-10): 18 arquivos, de 2007 a 2025, 1 UF(s) com arquivos, última atualização em 2026-01-20.
- Conversão local de amostras (1 arquivo(s) Parquet, de 2016 a 2016), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `COLEBR24.dbc` (91 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `FC_CONTATO` | Inteiro | Se sim, tipo de contato com caso de cólera (domiciliar, vizinho, outro, sem contato) |
| `FC_CONT_DE` / `OUT_VINCUL` | Inteiro/String | Tipo de contato detalhado e/outro vínculo (escola, trabalho, mar) |
| `VINCULO` | Inteiro | Vínculo entre os casos notificados (coorte de surto) |
| `CS_ASSINTO` | Inteiro | Assintomático (1 - Sim, 2 - Não, 9 - Ignorado) |
| `CS_DIARRE`/`CS_CAIMBRA`/`CS_FEBRE`/`CS_VOMITOS`/`CS_DOR` | Inteiro | Sintomas: diarreia, câimbras, febre, vômitos e dor abdominal |
| `CS_CHOQUE` / `CS_DESIT` | Inteiro | Choque e desidratação/estado de hidratação |
| `TIP_DIARRE`/`CS_FREQUEN`/`CS_SANGUE`/`CS_MUCO`/`CS_TIPO` | Inteiro | Aspecto da diarreia: tipo (aguada — "água de arroz"), frequência, presença de sangue e muco |
| `DT_ATENDIM` / `DT_INTERNA` / `UF_HOSPITA` / `NM_MUNIC_H` | Data/String | Atendimento, internação hospitalar e local |
| `CS_MATERIA` / `CS_VOMITO` | Inteiro | Material colhido para exame: fezes e vômito (1 - Sim, 2 - Não, 9 - Ignorado) |
| `DT_COLETA` | Data (`AAAAMMDD`) | Data da coleta do material para exame |
| `CS_ANTIB` / `NM_ANTIBIO` / `CS_RESULTA` | Inteiro/String | Antibioticoterapia instituída, nome dos antibióticos e resultado da cultura |
| `CS_POSITIV` / `CS_NEG_ESP` | Inteiro | Resultado positivo da cultura e espécimes negativados (sorotipagem O1/O139) |
| `CS_REIDRAT` | Inteiro | Tipo de reidratação recebida: via oral, venosa |
| `CS_ANTIB_T` / `ANTIB_DES` | Inteiro/String | Antibiótico profilático e descrição |
| `CLASSI_FIN` | Inteiro | Classificação final do caso: 1 - Confirmado, 2 - Descartado |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte: 1 - Laboratorial, 2 - Clínico-epidemiológico |
| `TPAUTOCTO` | Inteiro | O caso é autóctone do município de residência (1 - Sim, 2 - Não, 3 - Indeterminado) |
| `COUFINF`/`COPAISINF`/`COMUNINF`/`CODISINF` | String/Data | UF, país, distrito e município prováveis da fonte de infecção |
| `DOENCA_TRA` | Inteiro | Doença relacionada ao trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito por cólera, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` / `DT_ENCERRA` | Data (`AAAAMMDD`) | Data do óbito e de encerramento do caso |
| `DT_DESC1`/`DT_DESC2`/`DT_DESC3` | Data | Campos repetidos (1 a 3) de descarte/administração de registros — data (co UF / município / país correspondentes em `CO_UF_DES*`, `MUN_DES*`, `PA_DES*` e descrição `DS_TRANS*`)

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno). ds_semana_notifi cacao | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação. co_municipio_not ificacao | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico. dt_diagnostico_si ntoma | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno). ds_semana_sinto ma | — | todos |
| `dt_nasc` | `DT_NASC` | data | Data de nascimento. Data de nascimento do paciente | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência. co_municipio_res idencia | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil). co_pais_residenc ia | — | todos |
| `dt_invest` | `DT_INVEST` | data | Data da investigação. data de início da investigação do caso | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Ocupação do indivíduo que sofreu o agravo | — | todos |
| `fc_contato` | `FC_CONTATO` | texto | Contato com caso suspeito ou confirmado de cólera (até 10 dias antes do início dos sinais e sintomas). Local em que o paciente teve contato com caso semelhante nos últimos 10 dias, anteriores ao início dos sinais e sintomas | 1. Domicílio 2. Vizinhança 3. Trabalho 4. Creche/escola 5. Posto de saúde/hospital 6. Outro estado/município 7. Outros 8. Sem história de contato 9. Ignorado | todos |
| `fc_cont_de` | `FC_CONT_DE` | texto | No caso de outros (especificar). Habilitar se campo 33- Contato com caso suspeito ou confirmado de cólera (até 10 dias antes do início dos sinais e sintomas) for = 7-outros | — | todos |
| `vinculo` | `VINCULO` | texto | Sugestão de vínculo com. varchar(1), | 1- Consumo de água não tratada 2- Exposição à esgoto 3- Alimento 4- Deslocamento 5- Outros 9- Ignorado | todos |
| `out_vincul` | `OUT_VINCUL` | texto | Se outros especificar. Informar se outras sugestões de vínculo que não as de cima especificadas | — | todos |
| `cs_assinto` | `CS_ASSINTO` | texto | Outros Sinais e Sintomas Assintomático. O paciente não apresentou sintomas da doença | 1-sim 2-não 9-ignorado | todos |
| `cs_diarre` | `CS_DIARRE` | texto | Sinais e Sintomas Diarréia. O paciente apresentou diarréia | 1-sim 2-não 9-ignorado | todos |
| `cs_caimbra` | `CS_CAIMBRA` | texto | Sinais e Sintomas Câimbras. O paciente apresentou câimbras | 1-sim 2-não 9-ignorado | todos |
| `cs_febre` | `CS_FEBRE` | texto | Sinais e Sintomas Febre. O paciente teve febre | 1-sim 2-não 9-ignorado | todos |
| `cs_vomitos` | `CS_VOMITOS` | texto | Sinais e Sintomas Vômitos. O paciente teve vômitos | 1-sim 2-não 9-ignorado | todos |
| `cs_dor` | `CS_DOR` | texto | Sinais e Sintomas Dor Abdominal. O paciente apresentou dor abdominal | 1-sim 2-não 9-ignorado | todos |
| `cs_choque` | `CS_CHOQUE` | texto | Sinais e Sintomas Choque. O paciente entrou em estado de choque | 1-sim 2-não 9-ignorado | todos |
| `cs_desit` | `CS_DESIT` | texto | Desidratação. Grau de desidratação do paciente | 1. Não 2. Algum grau 3. Grave 9. Ignorado | todos |
| `tip_diarre` | `TIP_DIARRE` | texto | Característica da Diarréia. Como apresentava- se a diarréia | 1-aquosa/ amarelada 2- aquosa/ água de arroz 3- pastosa 9- ignorado | todos |
| `cs_frequen` | `CS_FREQUEN` | texto | Freqüência/ Dia. Quantas evacuações o paciente teve durante 24 horas | 1. até 5 evacuações 2. de 6 a 10 evacuações 3. de 11 a 20 evacuações 4. acima de 20 evacuações | todos |
| `cs_sangue` | `CS_SANGUE` | texto | Presença de sangue. Se há presença de sangue nas fezes do paciente | 1. Sim 2. Não 9. Ignorado | todos |
| `cs_muco` | `CS_MUCO` | texto | Presença de muco. Se há presença de muco nas fezes do paciente | 1. Sim 2. Não 9. Ignorado | todos |
| `cs_tipo` | `CS_TIPO` | texto | Tipo de atendimento. Tipo de atendimento recebido pelo paciente em decorrência da suspeita de cólera | 1. Hospitalar 2. Ambulatorial 3. Domiciliar 4. Nenhum 9. Ignorado | todos |
| `dt_atendim` | `DT_ATENDIM` | data | Data do atendimento. Data em que o paciente foi atendido | — | todos |
| `dt_interna` | `DT_INTERNA` | data | Data da internação. Se hospitalar, Data da internação | — | todos |
| `uf_hospita` | `UF_HOSPITA` | texto | UF. Sigla da UF onde o paciente foi internado | — | todos |
| `nm_munic_h` | `NM_MUNIC_H` | texto | Município do hospital. Nome completo do município onde o paciente foi internado | — | todos |
| `cs_materia` | `CS_MATERIA` | texto | Material colhido - Fezes. Colheu-se fezes para o exame | 1-sim 2-não 9-ignorado | todos |
| `cs_vomito` | `CS_VOMITO` | texto | Material colhido - Vômito. st_materia_colhido_vomit o | 1-sim 2-não 9-ignorado | todos |
| `dt_coleta` | `DT_COLETA` | data | Data da coleta. Data da coleta do material para exame | — | todos |
| `cs_antib` | `CS_ANTIB` | texto | Uso de antibiótico antes da coleta do material. Se o paciente fez uso de antibiótico antes da coleta para exame | 1-sim 2-não 9-ignorado | todos |
| `nm_antibio` | `NM_ANTIBIO` | texto | Caso afirmativo, qual. Especificar o nome do antibiótico | — | todos |
| `cs_resulta` | `CS_RESULTA` | texto | Resultado. Informar se o exame foi positivo ou negativo | 1. Positivo 2. Negativo | todos |
| `cs_positiv` | `CS_POSITIV` | texto | Caso positivo. Informar o sorotipo | 1. Ogawa 2. Inaba 3. Hikojima 4. Outro sorotipo 5. Não vibrio | todos |
| `cs_neg_esp` | `CS_NEG_ESP` | texto | Caso negativo, especificar. Acrescentar a opção outro agente etiologico | — | todos |
| `cs_reidrat` | `CS_REIDRAT` | texto | Reidratação. Informar o tipo de tratamento recebido pelo paciente | 1-via oral 2-venosa 3-oral - venosa | todos |
| `cs_antib_t` | `CS_ANTIB_T` | texto | Utilizou antibióticos. se o paciente foi tratado com antibióticos | 1. Sim 2. Não 9. Ignorado | todos |
| `antib_des` | `ANTIB_DES` | texto | Caso afirmativo, qual. Em caso afirmativo, | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final. Classificação final do caso | 1. Confirmado 2. Descartado | todos |
| `criterio` | `CRITERIO` | texto | Critério de confirmação/descarte. Define se o caso foi confirmado por laboratório ou clínico - epidemiológico | 1. Laboratorial 2. Clínico- epidemiológico | todos |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência?. Indica se o caso é autóctone do município de residência | 1 – Sim 2 – Não 3 – Indeterminado | todos |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o paciente foi provavelmente infectado | — | todos |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente infectado | — | todos |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). Código do município onde o paciente foi provavelmente infectado. O nome está associado ao código na tabela de municípios | — | todos |
| `codisinf` | `CODISINF` | texto | Distrito (provável de infecção). co_distrito_infeccão | — | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho. Se o paciente adquiriu a doença | 1. sim 2. não | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso | 1- cura 2- óbito por cólera 3- óbito por outras causas 9- ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Data do encerramento do caso | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_desc1` | `DT_DESC1` | data | Informações complementares e observações Data de deslocamento 1. informar data de deslocamento 1 | — | todos |
| `dt_desc2` | `DT_DESC2` | data | Informações complementares e observações Data de deslocamento 2. informar data de deslocamento 2 | — | todos |
| `dt_desc3` | `DT_DESC3` | data | Informações complementares e observações Data de deslocamento 3. informar data de deslocamento 3 | — | todos |
| `co_uf_des1` | `CO_UF_DES1` | texto | Informações complementares e observações UF deslocamento 1. co_uf_deslocamento_ 1 | — | todos |
| `co_uf_des2` | `CO_UF_DES2` | texto | Informações complementares e observações UF deslocamento 2. co_uf_deslocamento_ 2 | — | todos |
| `co_uf_des3` | `CO_UF_DES3` | texto | Informações complementares e. co_uf_deslocamento_ 3 | — | todos |
| `mun_des1` | `MUN_DES1` | texto | Informações complementares e observações Município deslocamento 1. co_municipio_desloca mento_1 | — | todos |
| `mun_des2` | `MUN_DES2` | texto | Informações complementares e observações Município deslocamento 2. co_municipio_desloca mento_2 | — | todos |
| `mun_des3` | `MUN_DES3` | texto | Informações complementares e observações Município deslocamento 3. co_municipio_desloca mento_3 | — | todos |
| `pa_des1` | `PA_DES1` | inteiro | Informações complementares e observações País deslocamento 1. co_pais_deslocament o_1 | — | todos |
| `pa_des2` | `PA_DES2` | inteiro | Informações complementares e observações País deslocamento 2. co_pais_deslocament o_2 | — | todos |
| `pa_des3` | `PA_DES3` | inteiro | Informações complementares e observações País deslocamento. co_pais_deslocament o_3 | — | todos |
| `ds_trans1` | `DS_TRANS1` | texto | Informações complementares e observações Meio de transporte 1. informar o meio de transporte de deslocamento 1 | — | todos |
| `ds_trans2` | `DS_TRANS2` | texto | Informações complementares e observações Meio de transporte 2. informar o meio de transporte de deslocamento 2 | — | todos |
| `ds_trans3` | `DS_TRANS3` | texto | Informações complementares e observações Meio de transporte 3. informar o meio de transporte de deslocamento 3 | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-cole`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 13, inteiro: 4, texto: 66.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-cole.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- o volume anual de casos é mínimo (série com pouquíssimos registros); a **lacuna do ano 2023 no FTP** exige cuidado na consolidação da série anual em agregações; e os campos coleta/cultura (`CS_MATERIA`, `CS_VOMITO`, `CS_POSITIV`) devem ser lidos conforme a ficha revisada de fevereiro/2012 (definição de caso e amostragem obrigatória). (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-cole/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-cole
quantilica datasus list sinan-cole

# 2. Baixar microdados de sinan-cole com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-cole -o ./data --start 2007 --end 2025 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-cole -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-cole -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc(
    "data/sinan-cole/2024/sinan-cole_preliminar_2024-br@20260120.dbc", clean=True
)

# Casos confirmados por ano e critério de confirmação
conf = (
    qdf.filter(pl.col("CLASSI_FIN") == 1)
    .group_by(["NU_ANO", "CRITERIO"])
    .len()
    .sort("NU_ANO")
)
print(conf)

# Evolução dos casos confirmados (incluindo letalidade)
print(conf.filter(pl.col("EVOLUCAO") == 2))
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Cólera (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de cólera e doenças diarréicas agudas (DDA)
