---
dataset:
  id: sinan-ltan
  fonte: datasus
  titulo: Leishmaniose Tegumentar Americana
  resumo: 'Leishmaniose Tegumentar Americana do DATASUS: uma ficha de notificação/investigação de leishmaniose Tegumentar Americana.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2000'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de leishmaniose Tegumentar Americana
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 116
  unidades_de_medida:
    tra_peso: 'número inteiro: contagem ou código numérico (ver Descrição)'
    tra_ampola: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    dt_transrm: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_lote_v: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_lote_h: 'número inteiro: contagem ou código numérico (ver Descrição)'
    pa_des1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    pa_des2: 'número inteiro: contagem ou código numérico (ver Descrição)'
    pa_des3: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Leishmaniose Tegumentar Americana (`sinan-ltan`)

## Resumo

O `sinan-ltan` contém os microdados das notificações e investigações de casos de Leishmaniose Tegumentar Americana (LTA, CID-10 B55.1) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de LTA — formas cutânea, mucocutânea e disseminada — digitado no SINAN Net/Sinan Online pelos serviços de saúde. A LTA é de notificação compulsória em todo o país e constitui a base oficial para monitorar a incidência, a distribuição e o desfecho dos casos humanos.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `LTAN` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `LTAN` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `LTANBR00.dbc` — prefixo `LTAN`, `BR` (consolidação nacional) e `00` (ano 2000, início da série disponível), até `LTANBR25.dbc` (2025). Não há arquivo em `PRELIM` para o `sinan-ltan` no inventário atual.
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-ltan/<AAAA>/sinan-ltan_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-ltan/2024/sinan-ltan_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## Conteúdo

A leishmaniose tegumentar americana é uma zoonose parasitária causada por espécies do complexo *Leishmania (Viannia) braziliensis* e afins, transmitida por flebotomíneos (popularmente "mosquito palha") com ampla gama de reservatórios silvestres. A vigilância é coordenada pela SVSA/MS, por meio do Programa de Vigilância e Controle da Leishmaniose Tegumentar, cuja ficha de investigação é revisada periodicamente. A notificação é compulsória de acordo com a Portaria SVS/MS nº 104/2011 (consolidação da Portaria GM/MS nº 204/2016), de forma individual para casos humanos confirmados e suspeitos.

O evento gerador é a **Ficha de Investigação da Leishmaniose Tegumentar Americana** do SINAN (ficha `LTA_v5`, com dicionário próprio), preenchida no caso suspeito — lesão cutânea ulcerada ou mucosa com tempo de evolução compatível e exposição em áreas de transmissão — e completada com exames parasitológicos (raspado/escarificação para amastigotas), intradermorreação de Montenegro e diagnóstico sorológico/molecular conforme disponibilidade. A unidade de análise é o caso notificado individual.

Marcos normativos e de leiaute: a ficha vigente data da revisão de 2006 e flui pelo SINAN Net (2007+) e Sinan Online (2014+), com dicionário de dados LTA próprio. A classificação final variou ao longo do tempo entre formas clínicas (cutânea, mucocutânea, cutânea difusa/disseminada). O registro histórico concentra-se em áreas rurais endêmicas (Amazônia Legal, Centro-Oeste e Nordeste), mas a expansão periurbana, os ecoturismos e o lazer em áreas endêmicas prescrevem vigilância permanente, particularmente em trabalhadores rurais (floresta, agropecuária, extrativismo).

Aplicações analíticas: coeficiente de detecção anual por 100 mil habitantes, distribuição por forma clínica, proporção de casos com comprometimento mucoso (maior gravidade), perfil ocupacional via CBO, acompanhamento de abandono de tratamento (possível dado da coluna `evolucao`) e mapeamento de recrudescentes endêmicos.

### Cobertura observada

- Índice do FTP (2026-10): 26 arquivos, de 2000 a 2025, 1 UF(s) com arquivos, última atualização em 2026-09-14.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2000 a 2025), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (LTA — CID-10 B55.1) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (lesão cutânea/mucosa) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) — forte predominância de homens em áreas ocupacionais |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_RACA` | Inteiro | Raça/cor (1-Branca ... 5-Indígena, 9-Ignorado) |
| `ID_OCUPA_C` | String (6) | Ocupação do paciente, código CBO (trabalhadores rurais predominantes) |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `CLASSI_FIN` | Inteiro | Classificação final (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Abandono, 3 - Óbito por LTA, 4 - Óbito por outras causas, 5 - Transferência, 6 - Mudança de diagnóstico) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
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
| `dt_diag` | `DT_DIAG` | data | Data dos primeiros sintomas / Diagnóstico. Data dos primeiros sintomas do caso de agravo agudo. Data do diagnóstico do caso de agravo crônico e DRTs Data do acidente nos acidentes da saúde do trabalhador | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno) | — | só em 2000 |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2000 a 2018 |
| `nu_idade` | `NU_IDADE` | texto | Idade do paciente (formato do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2000 |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil) | — | todos |
| `id_dg_not` | `ID_DG_NOT` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Leishmaniose Tegumentar Americana (`ID_DG_NOT`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `id_ev_not` | `ID_EV_NOT` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Leishmaniose Tegumentar Americana (`ID_EV_NOT`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `ant_dt_inv` | `ANT_DT_INV` | data | Data da investigação | — | só em 2000 |
| `id_ocupaca` | `ID_OCUPACA` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Leishmaniose Tegumentar Americana (`ID_OCUPACA`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `cli_cutane` | `CLI_CUTANE` | texto | Presença de lesão Cutânea. Informar o tipo de lesão que o paciente apresenta | 1 – Sim 2 – Não | todos |
| `cli_mucosa` | `CLI_MUCOSA` | texto | Presença de lesão mucosa. Informar o tipo de lesão que o paciente apresenta | 1 – Sim 2 – Não | todos |
| `cli_cut_di` | `CLI_CUT_DI` | texto | Manifestação clínica registrada na ficha de Leishmaniose Tegumentar Americana (`CLI_CUT_DI`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `cli_cicatr` | `CLI_CICATR` | texto | Em caso de presença de lesão Mucosa, há presença de cicatrizes cutâneas. Informar se há presença de cicatriz cutânea em casos de presença de lesão mucosa | 1 – Sim 2 – Não | todos |
| `lab_parasi` | `LAB_PARASI` | texto | Parasitológico Direto. Informar o resultado do exame do parasitológico direto | 1 – Positivo 2 – Negativo 3 – Não realizado | todos |
| `lab_irm` | `LAB_IRM` | texto | IRM. Informar o resultado do IRM (Intradermoreação de Montenegro) | 1 – Positivo 2 – Negativo 3 – Não Realizado | todos |
| `lab_histop` | `LAB_HISTOP` | texto | Histopatologia. Informar o resultado do exame histopatológico | 1 – Encontro do Parasita 2 – Compatível 3 – Não Compatível 4 – Não Realizado | todos |
| `clas_tipo_` | `CLAS_TIPO_` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `clas_forma` | `CLAS_FORMA` | texto | Forma Clínica. Informar a forma clínica | 1 – Cutânea 2 – Mucosa 9 - Ignorada | todos |
| `dt_inic_tr` | `DT_INIC_TR` | data | Data do Início do Tratamento. Informar a data do início do tratamento | — | todos |
| `tra_droga_` | `TRA_DROGA_` | texto | Droga Inicial Administrada. Informar o medicamento prescrito para o tratamento inicial | 1 – Antimonial Pentavalente 2 – Anfotericina B 3 – Pentamidina 4 – Outras 5 – Não Utilizada | todos |
| `tra_peso` | `TRA_PESO` | inteiro ou texto | Peso. Informar o peso do paciente em Kg | — | todos |
| `tra_dose` | `TRA_DOSE` | texto | Dose Prescrita em mg/kg/dia Sb+5. Informar a dose prescrita para o tratamento do paciente | 1 - Menor que 10 2 - Maior ou igual a 10 e menor que 15 3 - Igual a 15 4 - Maior ou igual a 15 e menor que 20 5 Maior ou igual a 20 | todos |
| `tra_ampola` | `TRA_AMPOLA` | inteiro ou texto | Nº Total de Ampolas Prescritas. Informar o número total de ampolas prescritas no tratamento inicial | — | todos |
| `tra_outra_` | `TRA_OUTRA_` | texto | Dado do inquérito/tratamento de tracoma (`TRA_OUTRA_`) | — | só em 2000 |
| `ento_local` | `ENTO_LOCAL` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_LOCAL`) | — | só em 2000 |
| `ento_exist` | `ENTO_EXIST` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_EXIST`) | — | só em 2000 |
| `ento_exi_1` | `ENTO_EXI_1` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_EXI_1`) | — | só em 2000 |
| `ento_exi_2` | `ENTO_EXI_2` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_EXI_2`) | — | só em 2000 |
| `ento_exi_3` | `ENTO_EXI_3` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_EXI_3`) | — | só em 2000 |
| `ento_exi_4` | `ENTO_EXI_4` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_EXI_4`) | — | só em 2000 |
| `ento_proxi` | `ENTO_PROXI` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_PROXI`) | — | só em 2000 |
| `ento_flebo` | `ENTO_FLEBO` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_FLEBO`) | — | só em 2000 |
| `ento_intra` | `ENTO_INTRA` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_INTRA`) | — | só em 2000 |
| `ento_perid` | `ENTO_PERID` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_PERID`) | — | só em 2000 |
| `ento_extra` | `ENTO_EXTRA` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_EXTRA`) | — | só em 2000 |
| `ento_cao` | `ENTO_CAO` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_CAO`) | — | só em 2000 |
| `ento_equin` | `ENTO_EQUIN` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_EQUIN`) | — | só em 2000 |
| `ento_outro` | `ENTO_OUTRO` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_OUTRO`) | — | só em 2000 |
| `ento_anima` | `ENTO_ANIMA` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_ANIMA`) | — | só em 2000 |
| `ento_captu` | `ENTO_CAPTU` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_CAPTU`) | — | só em 2000 |
| `ento_trans` | `ENTO_TRANS` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_TRANS`) | — | só em 2000 |
| `ento_inset` | `ENTO_INSET` | texto | Dado da investigação entomológica ou ambiental na ficha de Leishmaniose Tegumentar Americana (`ENTO_INSET`) | — | só em 2000 |
| `con_classi` | `CON_CLASSI` | texto | Classificação da forma clínica | 1. Forma bubônica 2. Forma pneumônica 3. Forma septicêmica 4 outra | só em 2000 |
| `con_criter` | `CON_CRITER` | texto | Dado de conclusão do caso na ficha de Leishmaniose Tegumentar Americana (`CON_CRITER`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_auto_u` | `CON_AUTO_U` | texto | Dado de conclusão do caso na ficha de Leishmaniose Tegumentar Americana (`CON_AUTO_U`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_auto_m` | `CON_AUTO_M` | texto | Dado de conclusão do caso na ficha de Leishmaniose Tegumentar Americana (`CON_AUTO_M`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_import` | `CON_IMPORT` | texto | Dado de conclusão do caso na ficha de Leishmaniose Tegumentar Americana (`CON_IMPORT`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_uf` | `CON_UF` | texto | Dado de conclusão do caso na ficha de Leishmaniose Tegumentar Americana (`CON_UF`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_pais` | `CON_PAIS` | texto | Dado de conclusão do caso na ficha de Leishmaniose Tegumentar Americana (`CON_PAIS`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_munici` | `CON_MUNICI` | texto | Dado de conclusão do caso na ficha de Leishmaniose Tegumentar Americana (`CON_MUNICI`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_doenca` | `CON_DOENCA` | texto | Dado de conclusão do caso na ficha de Leishmaniose Tegumentar Americana (`CON_DOENCA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_evoluc` | `CON_EVOLUC` | texto | Dado de conclusão do caso na ficha de Leishmaniose Tegumentar Americana (`CON_EVOLUC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_dt_obi` | `CON_DT_OBI` | texto | Dado de conclusão do caso na ficha de Leishmaniose Tegumentar Americana (`CON_DT_OBI`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_dt_enc` | `CON_DT_ENC` | data | Dado de conclusão do caso na ficha de Leishmaniose Tegumentar Americana (`CON_DT_ENC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | 2007 a 2025 |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | 2007 a 2025 |
| `sem_diag` | `SEM_DIAG` | texto | Semana epidemiológica dos primeiros sintomas/ diagnósticos. (campo interno). Semanas do calendário epidemiológico padronizado | — | 2007 a 2025 |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | 2007 a 2025 |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | 2007 a 2025 |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | 2007 a 2025 |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | 2007 a 2025 |
| `nduplic_n` | `NDUPLIC_N` | texto | Não Listar/ Não Contar. 0 ou branco – Não identificado 1 – Não é duplicidade (não listar) 2 – Duplicidade (não contar) | — | 2007 a 2025 |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | 2007 a 2025 |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | 2007 a 2025 |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | 2007 a 2025 |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | 2007 a 2025 |
| `dt_transrm` | `DT_TRANSRM` | data ou inteiro | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | 2007 a 2025 |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | 2007 a 2025 |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | 2007 a 2025 |
| `nu_lote_v` | `NU_LOTE_V` | inteiro ou texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | 2007 a 2025 |
| `nu_lote_h` | `NU_LOTE_H` | inteiro ou texto | Número do lote horizontal | — | 2007 a 2025 |
| `cs_flxret` | `CS_FLXRET` | texto | Fluxo de retorno. Identifica se o registro está habilitado ou foi enviado pelo fluxo de retorno para o município de residência | 0 - Não 1 - habilitado para envio. 2 - enviado | 2007 a 2025 |
| `flxrecebi` | `FLXRECEBI` | texto | Recebida por fluxo de retorno (campo interno). Colocar a estrutura do nº atribuído pelo sistema | — | 2007 a 2025 |
| `migrado_w` | `MIGRADO_W` | texto | Identifica migração (campo interno). Identifica se o registro é oriundo da rotina de migração da base Windows | 1- migrado do Sinan Windows | 2007 a 2025 |
| `dt_invest` | `DT_INVEST` | data | Data da Investigação. Informe a Data de início da investigação do caso | — | 2007 a 2025 |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Nomes e códigos das ocupações e ramos de atividades da tabela correspondente | — | 2007 a 2025 |
| `cli_co_hiv` | `CLI_CO_HIV` | texto | Co-infecção HIV. Informar se o paciente apresenta co-infecção LTA/HIV | 1 – Sim 2 – Não 9 - ignorado | 2007 a 2025 |
| `cla_tipo_n` | `CLA_TIPO_N` | texto | Tipo de Entrada. Informar o tipo de entrada do caso | 1 – Caso Novo 2 – Recidiva 3 – Transferência 9 – Ignorado | 2007 a 2025 |
| `tra_outr_n` | `TRA_OUTR_N` | texto | Outra Droga Utilizada, na Falência do Tratamento Inicial. Informar qual droga foi utilizada na falência do tratamento inicial | 1 – Anfotericina B 2 – Pentamidina 3 – Outros 4 – Não se aplica | 2007 a 2025 |
| `criterio` | `CRITERIO` | texto | Critério de confirmação. Informar o critério de confirmação | 1 – Laboratorial 2 – Clínico Epidemiológico | 2007 a 2025 |
| `con_class_` | `CON_CLASS_` | texto | Classificação epidemiológica | 1 – autóctone 2 – importado 3 - indeterminado | 2007 a 2025 |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência?. Indica se o caso é autóctone do município de residência | 1 – Sim 2 – Não 3 – Indeterminado | 2007 a 2025 |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o paciente foi provavelment e infectado | — | 2007 a 2025 |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente infectado | — | 2007 a 2025 |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). Código do município onde o paciente foi provavelmente infectado. O nome está associado ao código na tabela de municípios | — | 2007 a 2025 |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao Trabalho. Informar se a doença está relacionada ao ambiente de trabalho do paciente | 1 – Sim 2 – Não 9 – Ignorado | 2007 a 2025 |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. Informar a evolução do caso | 1 – Alta por cura 2 – Abandono 3 – Óbito por LTA 4- Óbito por outras causas 5 Transferência 6 – Mudança de diagnóstico | 2007 a 2025 |
| `dt_obito` | `DT_OBITO` | data | Data do Óbito. Informar a data do óbito | — | 2007 a 2025 |
| `dt_encerra` | `DT_ENCERRA` | data | Data do Encerramento. Informar a data do encerramento do caso | — | 2007 a 2025 |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | 2007 a 2025 |
| `dt_desc1` | `DT_DESC1` | data | Informações complementares e observações Data de deslocamento 1. informar data de deslocamento 1 | — | 2007 a 2025 |
| `dt_desc2` | `DT_DESC2` | data | Informações complementares e observações Data de deslocamento 2. informar data de deslocamento 2 | — | 2007 a 2025 |
| `dt_desc3` | `DT_DESC3` | data | Informações complementares e observações Data de deslocamento 3. informar data de deslocamento 3 | — | 2007 a 2025 |
| `co_uf_des1` | `CO_UF_DES1` | texto | Informações complementares e observações UF deslocamento 1. 1 | — | 2007 a 2025 |
| `co_uf_des2` | `CO_UF_DES2` | texto | Informações complementares e observações UF deslocamento 2. 2 | — | 2007 a 2025 |
| `co_uf_des3` | `CO_UF_DES3` | texto | Informações complementares e. 3 | — | 2007 a 2025 |
| `mun_des1` | `MUN_DES1` | texto | Informações complementares e observações Município deslocamento 1. mento_1 | — | 2007 a 2025 |
| `mun_des2` | `MUN_DES2` | texto | Informações complementares e observações Município deslocamento 2. mento_2 | — | 2007 a 2025 |
| `mun_des3` | `MUN_DES3` | texto | Informações complementares e observações Município deslocamento 3. mento_3 | — | 2007 a 2025 |
| `pa_des1` | `PA_DES1` | inteiro | Informações complementares e observações País deslocamento 1. o_1 | — | 2007 a 2025 |
| `pa_des2` | `PA_DES2` | inteiro | Informações complementares e observações País deslocamento 2. o_2 | — | 2007 a 2025 |
| `pa_des3` | `PA_DES3` | inteiro | Informações complementares e observações País deslocamento. o_3 | — | 2007 a 2025 |

## No lake

- **Dataset no lake:** `datasus/sinan-ltan`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 18, inteiro: 9, texto: 94.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-ltan.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- a completude dos resultados laboratoriais é frequentemente insuficiente — boa parte dos casos é confirmado por critério clínico-epidemiológico (`CRITERIO = 2`); volume considerável por ano (~38,8 MB em 26 consolidações), pois a LTA é endêmica em dezenas de países municipais, sobretudo no Norte e Centro-Oeste; a ausência de arquivos `PRELIM` no inventário atual para este agravo (ver `quantilica datasus list sinan-ltan`) recomenda o uso dos FINAIS como fonte principal. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Tipo que varia entre períodos:** `tra_peso`, `tra_ampola`, `dt_transrm`, `nu_lote_v`, `nu_lote_h` aparecem com mais de um tipo nas amostras (por exemplo, inteiro em alguns períodos e texto em outros); leia a coluna `Tipo` do dicionário e converta explicitamente antes de empilhar períodos. Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Colunas que não existem em todo o período:** 89 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-ltan").glob("**/*.parquet"))
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
datasus-fetcher list sinan-ltan

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-ltan -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-ltan
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Leishmaniose Tegumentar Americana**: https://portalsinan.saude.gov.br/leishmaniose-tegumentar-americana
- **Dicionário de Dados LTA v5 (SINAN NET)**: http://portalsinan.saude.gov.br/images/documentos/Agravos/Leishmaniose%20Tegumentar%20Americana/DIC_DADOS_LTA_v5.pdf
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo Leishmanioses
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
