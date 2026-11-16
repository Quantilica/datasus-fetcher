---
dataset:
  id: sinan-anim
  fonte: datasus
  titulo: Acidente por Animais Peçonhentos
  resumo: 'Acidente por Animais Peçonhentos do DATASUS: uma ficha de notificação/investigação de acidente por Animais Peçonhentos.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de acidente por Animais Peçonhentos
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 77
  unidades_de_medida:
    ano_nasc: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ampolas: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ampol_1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ampol_8: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ampol_6: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ampol_4: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ampo_7: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ampo_5: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ampol_9: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ampol_3: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Acidente por Animais Peçonhentos (`sinan-anim`)

## Resumo

O `sinan-anim` contém os microdados das notificações de acidentes por animais peçonhentos (CID-10 X20-X29) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação de um acidente por serpente (botrópico, crotálico, elapídico, laquético), aranha (foneutrismo/loxoscelismo/latrodectismo), escorpião, lagarta (lonomia), abelha ou outro animal peçonhento, digitada no SINAN Net/Sinan Online. O agravo é de notificação compulsória e é um dos maiores volumes do SINAN, pois os acidentes escorpiônicos no Brasil superam 150 mil casos por ano na atualidade.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ANIM` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ANIM` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `ANIMBR07.dbc` — prefixo `ANIM`, `BR` (consolidação nacional) e `07` (ano 2007), até `ANIMBR22.dbc` (2022); os anos recentes ficam em `PRELIM` (ex.: `ANIMBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-anim/<AAAA>/sinan-anim_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-anim/2024/sinan-anim_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## Conteúdo

A vigilância dos acidentes por animais peçonhentos é gerida pela SVSA/MS com o programa de saneamento e controle de peçonhentos: serpentes (*Bothrops*, *Crotalus durissus*, *Micrurus*, *Lachesis*), aranhas (*Phoneutria*, *Loxosceles*, *Latrodectus*), escorpiões (sobretudo o *Tityus serrulatus* em expansão urbana), lagartas (*Lonomia obliqua*), abelhas e outros artrópodes. As notificações humanas — de grande impacto sanitário, sobretudo na população urbana em expansão do escorpionismo — são compulsórias desde a Portaria SVS/MS nº 5/2006 e permanecem na lista nacional consolidada (Portaria GM/MS nº 204/2016). A notificação usa ficha própria, notificação individual de acidente por animal peçonhento (ficha `Animais_Peconhentos_v5`), de interesse nacional.

O evento gerador é a ficha de acidente por animais peçonhentos, que registra o tipo de animal (1-Serpente, 2-Aranha, 3-Escorpião, 4-Lagarta, 5-Abelha, 6-Outros), tipo de serpente (botrópico, crotálico, elapídico, laquético e não peçonhenta); aranha (foneutrismo, loxoscelismo, latrodectismo, outra); manifestações locais e sistêmicas, tempo de coagulação e soroterapia — o caso confirmado é definido por evidências clínicas de envenenamento, independentemente da identificação do animal. A unidade de análise é o acidente notificado individualmente (não o atendimento de soroterapia em si, registrado na internação).

A série de 2007 em diante coincide com a expansão da notificação obrigatória e do conhecimento (decada 2007 unluvutitlus): os acidentes explosivos nos anos 2010-2020 em zoneamento urbano — escorpões (*Tityus serrulatus* sinte e tipo presente) — são mais notados emuther Télba-água municípios das regiões Sudeste e Norte; no ambiente rural, as serpentes ainda predominam em trabalhador rural (CBO grandes grupos agropastoris). O OGMB/SINAN foi crescentamente e a base espaço-temporal é sólida para séries de acidentes.

Aplicações analíticas: coeficiente de incidência por 100 mil habitantes, letalidade específica por tipo de acidente (escorpionismo, ofidismo, araneismo e lonomismo), distribuição por parte do corpo picada (local da picada), tempo decorrido picada/atendimento (qualidade da assistência), uso de soroterapia (soro antibotrópico/anticrotálico/antielapídico/antilonômico) e vigilância ocupacional (fichas com campo de relação com trabalho).

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-10-29.
- Conversão local de amostras (4 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Acidente por animais peçonhentos — CID-10 X20-X29) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_ACID` | Data (`AAAAMMDD`) | Data do acidente (campo específico da ficha) |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_RACA` | Inteiro | Raça/cor (1-Branca ... 5-Indígena, 9-Ignorado) |
| `ID_OCUPA_C` | String (6) | Ocupação do paciente, código CBO (trabalhador rural predominante) |
| `DOENCA_TRA` | Inteiro | Relação do acidente com o trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `CLASSI_FIN` | Inteiro | Classificação final do caso (conforme dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (conforme dicionário; acidente é estruturalmente clínico) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito por acidente, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno) | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno) | — | todos |
| `ano_nasc` | `ANO_NASC` | inteiro ou texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil) | — | todos |
| `dt_invest` | `DT_INVEST` | data | Data da investigação. data de início da investigação do caso | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Ocupação do indivíduo que sofreu o agravo | — | todos |
| `ant_dt_aci` | `ANT_DT_ACI` | data | Data do acidente. Informar o nome do município onde ocorreu o acidente | — | todos |
| `ant_uf` | `ANT_UF` | texto | UF. co_uf_ocorrência | — | todos |
| `ant_munic_` | `ANT_MUNIC_` | texto | Município de Ocorrência do Acidente. Informar o nome do município onde ocorreu o acidente | — | todos |
| `ant_tempo_` | `ANT_TEMPO_` | texto | Tempo Decorrido Picada/Atendimento. Informar o tempo decorrido entre o acidente e o atendimento | 1- 0 - 1h 2- 1 - 3h 3- 3 - 6h 4- 6 - 12h 5- 12 e 24h 6- 24 e +h 9- Ignorado | todos |
| `ant_loca_1` | `ANT_LOCA_1` | texto | Local da Picada. Informar a localização da picada | 01 – Cabeça 02 – Braço 03 – Ante-Braço 04 – Mão 05 – Dedo da Mão 06 – tronco 07 – Coxa 08 – Perna 09 – Pé 10 – Dedo do Pé 99 – Ignorado | todos |
| `mcli_local` | `MCLI_LOCAL` | texto | Manifestações locais. Informar se houve manifestações locais | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_dor` | `CLI_DOR` | texto | Se Manifestações. Se manifestações locais | 1 – Sim | todos |
| `cli_edema` | `CLI_EDEMA` | texto | Se Manifestações locais sim, especificar (Edema). Se manifestações locais sim, informar se houve (edema) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_equimo` | `CLI_EQUIMO` | texto | Se Manifestações locais sim, especificar (Equimose). Se manifestações locais sim, informar se houve (equimose) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_necros` | `CLI_NECROS` | texto | Se Manifestações locais sim, especificar (Necrose). Se manifestações locais sim, informar se houve (necrose) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_local_` | `CLI_LOCAL_` | texto | Se Manifestações locais sim, especificar (Outras). Se manifestações locais sim, informar se houve (outras) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_loca_1` | `CLI_LOCA_1` | texto | No caso de Outras(especificar). Especificar outras manifestações locais | — | todos |
| `mcli_sist` | `MCLI_SIST` | texto | Manifestações sistêmicas. Informar se houve manifestações sistêmicas | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_neuro` | `CLI_NEURO` | texto | Se manifestações sistêmicas sim, especificar neuroparalíticas (ptose palpebral, turvação visual) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_hemorr` | `CLI_HEMORR` | texto | Se manifestações sistêmicas sim, especificar Hemorrágicas (gengivorragia, outros sangramentos) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_vagais` | `CLI_VAGAIS` | texto | Se manifestações sistêmicas sim, especificar vagais (vômitos/ diarréia). Se manifestações sistêmicas sim, informar se houve manifestações vagais (vômitos/ diarréia) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_miolit` | `CLI_MIOLIT` | texto | Se manifestações sistêmicas sim, especificar miolíticas/ hemolíticas (mialgia, anemia, urina escura). a | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_renal` | `CLI_RENAL` | texto | Se manifestações sistêmicas sim, especificar renais (oligúria/ anúria). Se manifestações sistêmicas sim, informar se houve manifestações renais (oligúria/ anúria) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_outr_2` | `CLI_OUTR_2` | texto | Se manifestações sistêmicas sim, especificar (Outras). Se manifestações sistêmicas sim informar se houve outras | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_outr_3` | `CLI_OUTR_3` | texto | No caso de Outras(especificar). Especificar outras manifestações sistêmicas | — | todos |
| `cli_tempo_` | `CLI_TEMPO_` | texto | Tempo de Coagulação. Informar o tempo de coagulação | 1 – Normal 2 – Alterado 9 – Não realizado | todos |
| `tp_acident` | `TP_ACIDENT` | texto | Tipo de Acidente. Informar o tipo de acidente segundo o animal responsável pela agressão | 1 – Serpente 2 – Aranha 3 – Escorpião 4 – Lagarta 5 – Abelha 6 – Outros 9 – Ignorado | todos |
| `ani_tipo_1` | `ANI_TIPO_1` | texto | No caso de Outros especificar. Especificar outro animal responsável pela agressão | — | todos |
| `ani_serpen` | `ANI_SERPEN` | texto | Serpente – Tipo de acidente. Informar o tipo de acidente ofídico conforme as manifestações clinicas do envenenamento | 1 – Botrópico 2 – Crotálico 3 – Elapídico 4 – Laquético 5 –Serpente não peçonhenta 9 – Ignorado | todos |
| `ani_aranha` | `ANI_ARANHA` | texto | Aranha – Tipo de acidente. Informar o tipo de acidente araneídico conforme as manifestações clinicas do envenenamento | 1 – Foneutrismo 2 – Loxoscelismo 3 – Latrodectismo 4 – Outra aranha 9 – Ignorado | todos |
| `ani_lagart` | `ANI_LAGART` | texto | Lagarta – Tipo de acidente. Informar o tipo de acidente conforme as manifestações clinicas do envenenamento | 1 – Lonomia 2 – Outra lagarta 9 – Ignorado | todos |
| `tra_classi` | `TRA_CLASSI` | texto | Classificação do Caso. Informar a classificação do caso segundo a gravidade do envenenamento | 1 – Leve 2 – Moderado 3 – Grave 9 – Ignorado | todos |
| `con_sorote` | `CON_SOROTE` | texto | Soroterapia. Informar se foi feita Soroterapia | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `nu_ampolas` | `NU_AMPOLAS` | inteiro | Se soroterapia sim, especificar, número. Informar o número de ampolas aplicadas (soro | — | todos |
| `nu_ampol_1` | `NU_AMPOL_1` | inteiro | Se soroterapia sim, especificar, número de ampolas de soro: anticrotálico (SAC). Informar o número de ampolas aplicadas (soro anticrotálico) | — | todos |
| `nu_ampol_8` | `NU_AMPOL_8` | inteiro | Se soroterapia sim, especificar, número de ampolas de soro: antiaracnídico (SAAr). Informar o número de ampolas aplicadas (soro antiaracnídico) | — | todos |
| `nu_ampol_6` | `NU_AMPOL_6` | inteiro | Se soroterapia sim, especificar, número de ampolas de soro: antibrotópico- laquético (SABL). Informar o número de ampolas aplicadas (soro antibrotópico-crotálico) | — | todos |
| `nu_ampol_4` | `NU_AMPOL_4` | inteiro | Se soroterapia sim, especificar, número de ampolas de soro: antielapídico (SAEL). Informar o número de ampolas aplicadas (soro antielapídico) | — | todos |
| `nu_ampo_7` | `NU_AMPO_7` | inteiro | Número ou quantidade registrado na ficha de Acidente por Animais Peçonhentos (`NU_AMPO_7`); o dicionário consultado não define o campo isoladamente | — | todos |
| `nu_ampo_5` | `NU_AMPO_5` | inteiro | Número ou quantidade registrado na ficha de Acidente por Animais Peçonhentos (`NU_AMPO_5`); o dicionário consultado não define o campo isoladamente | — | todos |
| `nu_ampol_9` | `NU_AMPOL_9` | inteiro | Se soroterapia sim, especificar, número de ampolas de soro: antiescorpiônico (SAEsc). Informar o número de ampolas aplicadas (soro antiescorpiônico) | — | todos |
| `nu_ampol_3` | `NU_AMPOL_3` | inteiro | Se soroterapia sim, especificar, número. Informar o número de ampolas aplicadas (soro | — | todos |
| `com_loc` | `COM_LOC` | texto | complicações Locais. Informar se houve complicações locais | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `com_secund` | `COM_SECUND` | texto | Se complicações locais Sim, especificar - Infecção Secundária. o | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `com_necros` | `COM_NECROS` | texto | Se complicações locais Sim, especificar - Necrose Extensa. e | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `com_compor` | `COM_COMPOR` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `com_defict` | `COM_DEFICT` | texto | Se complicações locais Sim, especificar - Déficit Funcional. Se complicações locais sim, informar se houve Déficit Funcional | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `com_aputac` | `COM_APUTAC` | texto | Se complicações locais Sim, especificar - Amputação | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `com_sistem` | `COM_SISTEM` | texto | Complicações Sistêmicas. Informar se houve complicações sistêmicas | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `com_renal` | `COM_RENAL` | texto | Se complicações sistêmicas, especificar -. Se complicações sistemicas sim, informar se houve Insuficiência | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `com_edema` | `COM_EDEMA` | texto | Se complicações sistêmicas, especificar - Insuficiência Respiratória/ Edema Pulmonar Agudo | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `com_septic` | `COM_SEPTIC` | texto | Se complicações sistêmicas, especificar - Septicemia | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `com_choque` | `COM_CHOQUE` | texto | Se complicações sistêmicas, especificar - Choque. Se complicações sistêmicas sim, Informar se houve Choque | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Acidente relacionada ao trabalho. Informar se a doença é relacionada ao trabalho | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do Caso | 1 – Cura 2 – óbito por acidente por animais peçonhentos 3 – Óbito por outras causas 9 – Ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-anim`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 7, inteiro: 11, texto: 60.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-anim.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- volume enorme (20 consolidações anuais com ~207 MB) e sazonalidade de pico em estações quentes; o tipo de acidente e o gênero da serpente/aranha podem ficar em branco quando o animal não é identificado — não tratar blank como "outros"; município de residência vs. município de ocorrência do acidente podem divergir (campos específicos da ficha registram UF/localidade de ocorrência); acidentes de trabalho exigem o cruzamento de `DOENCA_TRA` com `ID_OCUPA_C`, como fazem as análises oficiais do Boletim Epidemiológico da SVSA. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Tipo que varia entre períodos:** `ano_nasc` aparecem com mais de um tipo nas amostras (por exemplo, inteiro em alguns períodos e texto em outros); leia a coluna `Tipo` do dicionário e converta explicitamente antes de empilhar períodos. Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-anim").glob("**/*.parquet"))
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
datasus-fetcher list sinan-anim

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-anim -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-anim
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Acidente por Animais Peçonhentos (ficha e instrucional)**: https://portalsinan.saude.gov.br/acidente-por-animais-peconhentos
- **Ficha de Investigação Acidentes por Animais Peçonhentos (Animais_Peconhentos_v5)**: http://portalsinan.saude.gov.br/images/documentos/Agravos/AAP/Animais_Peconhentos_v5.pdf
- **Boletim Epidemiológico SVSA — acidentes por animais peçonhentos**: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/a/animais-peconhentos
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo peçonhentos
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
