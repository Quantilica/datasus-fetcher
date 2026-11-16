---
dataset:
  id: sinan-lept
  fonte: datasus
  titulo: Leptospirose
  resumo: 'Leptospirose do DATASUS: uma ficha de notificação/investigação de leptospirose.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2000'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de leptospirose
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 176
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Leptospirose (`sinan-lept`)

## Resumo

O `sinan-lept` contém os microdados das notificações e investigações de casos de Leptospirose (CID-10 A27) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de leptospirose, digitado no SINAN Net/Sinan Online. A doença é de notificação compulsória e a base concentra grande parte dos registros do ciclo de enchentes e desastres climáticos, ao lado dos casos ocupacionais em ambientes com água e inundações.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `LEPT` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `LEPT` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `LEPTBR00.dbc` — prefixo `LEPT`, `BR` (consolidação nacional) e `00` (ano 2000), até `LEPTBR24.dbc` (2024); arquivos preliminares em `PRELIM` (ex.: `LEPTBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-lept/<AAAA>/sinan-lept_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-lept/2024/sinan-lept_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## Conteúdo

A leptospirose é uma zoonose causada por espiroquetas do gênero *Leptospira* (principalmente *L. interrogans*), transmitida ao homem por contato direto ou indireto com urina de animais infectados — sobretudo roedores urbanos —, bem como por inundações e água contaminada na época das chuvas. No âmbito ocupacional, a exposição é relevante para trabalhadores de saneamento e limpeza urbana, coleta de resíduos, esgoto, agricultura e pesca. A vigilância é da SVSA/MS, com o agravo na Lista de Notificação Compulsória desde a Portaria de Consolidação (GM/MS nº 204/2016) e anteriormente desde a Portaria SVS/MS nº 5/2006; a notificação imediata é mandatória para os casos graves.

O instrumento é a **Ficha de Investigação de Leptospirose** do SINAN (ficha `Leptospirose_v5`), que registra a notificação do caso suspeito e, ao longo da investigação, os exames laboratoriais empregados (MAT — teste de aglutinação microscópica, ELISA, macroaglutinação e PCR) e o desfecho clínico. A unidade de análise é o caso suspeito/confirmado notificado individualmente, com atenção ao contexto de exposição (transporte, ambiente ocupacional, inundação).

O número anual de casos é compatível com um padrão sazonal marcado por chuvas intensas e desastres climáticos — por exemplo, as grandes inundações de 2008 em Santa Catarina e de 2011 no Rio de Janeiro produziram picos de notificação. A capacidade do SINAN de registrar casos pós-desastre facilita a articulação entre vigilância epidemiológica e gestão de riscos ambientais.

Aplicações analíticas: coeficiente de incidência por 100 mil, letalidade (a leptospirose grave tem letalidade elevada), distribuição por sexo/idade/ocupação, análise de fatores de exposição (inundações, ambientes urbanos deteriorados), associação climática por semana epidemiológica e respostas posteriormente a desastres.

### Cobertura observada

- Índice do FTP (2026-10): 27 arquivos, de 2000 a 2026, 1 UF(s) com arquivos, última atualização em 2026-11-03.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2000 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Leptospirose — CID-10 A27) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave; notificação imediata nos casos graves) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data do início dos sintomas |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_RACA` | Inteiro | Raça/cor (1-Branca ... 5-Indígena, 9-Ignorado) |
| `ID_OCUPA_C` | String (6) | Ocupação do paciente, em código CBO (limpeza urbana, saneamento etc.) |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DOENCA_TRA` | Inteiro | Relação do caso com o trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `CLASSI_FIN` | Inteiro | Classificação final (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação | — | todos |
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno) | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `cs_escolar` | `CS_ESCOLAR` | texto | Escolaridade do paciente (formato do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2000 |
| `nu_idade` | `NU_IDADE` | texto | Idade do paciente (formato do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2000 |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno) | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_ev_not` | `ID_EV_NOT` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Leptospirose (`ID_EV_NOT`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `id_dg_not` | `ID_DG_NOT` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Leptospirose (`ID_DG_NOT`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil) | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `ant_cb_lim` | `ANT_CB_LIM` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Leptospirose (`ANT_CB_LIM`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `ant_cb_car` | `ANT_CB_CAR` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Leptospirose (`ANT_CB_CAR`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `ant_cb_cri` | `ANT_CB_CRI` | texto | Situações de risco ocorrida nos 30 dias que antecederam os primeiros sintomas Criação de animais | 1-Sim; 2-Não; 9- Ignorado | todos |
| `ant_cb_cor` | `ANT_CB_COR` | texto | Situações de risco ocorrida nos 30 dias que antecederam os primeiros sintomas Rio, córrego, lagoa ou represa | 1-Sim; 2-Não; 9- Ignorado | todos |
| `ant_cb_fos` | `ANT_CB_FOS` | texto | Situações de risco ocorrida nos 30 dias que antecederam os primeiros sintomas Fossa, caixa de gordura ou esgoto | 1-Sim; 2-Não; 9- Ignorado | todos |
| `ant_cb_lix` | `ANT_CB_LIX` | texto | Situações de risco ocorrida nos 30 dias que antecederam os primeiros sintomas Lixo/Entulho | 1-Sim; 2-Não; 9- Ignorado | todos |
| `ant_cb_lam` | `ANT_CB_LAM` | texto | Situações de risco ocorrida nos 30 dias que antecederam os primeiros sintomas Água ou lama de enchente | 1-Sim; 2-Não; 9- Ignorado | todos |
| `ant_cb_lav` | `ANT_CB_LAV` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Leptospirose (`ANT_CB_LAV`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `ant_ocupac` | `ANT_OCUPAC` | texto | Ocupação do paciente (antecedente epidemiológico) | — | só em 2000 |
| `ant_dt_inv` | `ANT_DT_INV` | data | Data da investigação | — | só em 2000 |
| `cli_icteri` | `CLI_ICTERI` | texto | Sinais e sintomas – Icterícia | 1-Sim; 2-Não; 9- Ignorado | todos |
| `cli_outras` | `CLI_OUTRAS` | texto | Complicações Existiram (Outras). Informa se a complicação foram outras que não as especificadas acima | 1. Sim 2. Não 9. Ignorado | só em 2000 |
| `cli_mening` | `CLI_MENING` | texto | Sinais e sintomas – Meningismo | 1-Sim; 2-Não; 9- Ignorado | todos |
| `cli_hemorr` | `CLI_HEMORR` | texto | Sinais e sintomas – Outras Hemorragias | 1-Sim; 2-Não; 9- Ignorado | todos |
| `cli_cardia` | `CLI_CARDIA` | texto | Sinais e sintomas – Alterações cardíacas | 1-Sim; 2-Não; 9- Ignorado | todos |
| `cli_respir` | `CLI_RESPIR` | texto | Sinais e sintomas – Alterações respiratórias | 1-Sim; 2-Não; 9- Ignorado | todos |
| `cli_dt_ate` | `CLI_DT_ATE` | data | Data de Atendimento | — | todos |
| `ant_animai` | `ANT_ANIMAI` | texto | Casos anteriores de leptospirose no local provável de infecção nos últimos 2 meses Casos Animais | 1-Sim; 2-Não; 9- Ignorado | todos |
| `ant_humano` | `ANT_HUMANO` | texto | Casos anteriores de leptospirose no local provável de infecção nos últimos 2 meses Casos Humanos | 1-Sim; 2-Não; 9- Ignorado | todos |
| `ant_cb_out` | `ANT_CB_OUT` | texto | Situações de risco ocorrida nos 30 dias que antecederam os primeiros sintomas Outras | 1-Sim; 2-Não; 9- Ignorado | todos |
| `ant_cb_roe` | `ANT_CB_ROE` | texto | Situações de risco ocorrida nos 30 dias que antecederam os primeiros sintomas Roedores diretamente | 1-Sim; 2-Não; 9- Ignorado | todos |
| `ate_munici` | `ATE_MUNICI` | texto | Município do Hospital. Nome completo do município onde o paciente foi internado | — | todos |
| `ate_uf` | `ATE_UF` | texto | UF. Sigla da UF onde o | — | todos |
| `ate_dt_alt` | `ATE_DT_ALT` | data | Data de Alta. Data alta > ou = Data de internação | — | todos |
| `ate_hosp` | `ATE_HOSP` | texto | Ocorreu Hospitalização. o | 1-Sim; 2-Não; 9- Ignorado | todos |
| `ate_dt_int` | `ATE_DT_INT` | data | Data da Internação. Data de internação, caso tenha ocorrido | — | todos |
| `cli_desc_o` | `CLI_DESC_O` | texto | Manifestação clínica registrada na ficha de Leptospirose (`CLI_DESC_O`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `cli_conges` | `CLI_CONGES` | texto | Sinais e sintomas – Congestão conjuntival | 1-Sim; 2-Não; 9- Ignorado | todos |
| `cli_vomito` | `CLI_VOMITO` | texto | Sinais e sintomas – Vômito | 1-Sim; 2-Não; 9- Ignorado | todos |
| `cli_renal` | `CLI_RENAL` | texto | Sinais e sintomas – | 1-Sim; 2-Não; 9- | todos |
| `cli_diarre` | `CLI_DIARRE` | texto | Sinais e sintomas – Diarréia | 1-Sim; 2-Não; 9- Ignorado | todos |
| `cli_mialgi` | `CLI_MIALGI` | texto | Sinais e sintomas – Mialgia | 1-Sim; 2-Não; 9- Ignorado | todos |
| `cli_cefale` | `CLI_CEFALE` | texto | Sinais e sintomas – Cefaléia | 1-Sim; 2-Não; 9- Ignorado | todos |
| `cli_febre` | `CLI_FEBRE` | texto | Sinais e sintomas – Febre | 1-Sim; 2-Não; 9- Ignorado | todos |
| `lab_s_2` | `LAB_S_2` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_S_2`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_s_1` | `LAB_S_1` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_S_1`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_dt_2` | `LAB_DT_2` | data | Data da Coleta – Sorologia IgM – Elisa – 2ª amostra. Deve ser maior que a data da 1ª amostra | — | todos |
| `lab_micro` | `LAB_MICRO` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_MICRO`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_dt_1` | `LAB_DT_1` | data | Data da Coleta – Sorologia IgM – Elisa – 1ª amostra | — | todos |
| `lab_macro` | `LAB_MACRO` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_MACRO`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_uf` | `LAB_UF` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_UF`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_soroag` | `LAB_SOROAG` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_SOROAG`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `con_clas_e` | `CON_CLAS_E` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_CLAS_E`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_classi` | `CON_CLASSI` | texto | Classificação da forma clínica | 1. Forma bubônica 2. Forma pneumônica 3. Forma septicêmica 4 outra | só em 2000 |
| `lab_potass` | `LAB_POTASS` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_POTASS`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_plaque` | `LAB_PLAQUE` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_PLAQUE`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_tgo` | `LAB_TGO` | texto | Resultado A TGO. a_tgo | 1-Sim 2-Não 3- Não realizado 9-Ignorado | só em 2000 |
| `lab_tgp` | `LAB_TGP` | texto | Resultado A TGP. a_tgp | 1-Sim 2-Não 3-Não | só em 2000 |
| `lab_bt` | `LAB_BT` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_BT`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_bd` | `LAB_BD` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_BD`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_bi` | `LAB_BI` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_BI`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_creati` | `LAB_CREATI` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_CREATI`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_ureia` | `LAB_UREIA` | texto | Resultado A Aumento de Uréia e Creatinina. a_aumento | 1-Sim 2-Não 3-Não realizado 9-Ignorado | só em 2000 |
| `lab_met_d` | `LAB_MET_D` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_MET_D`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_metodo` | `LAB_METODO` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_METODO`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_r_2` | `LAB_R_2` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_R_2`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_r_1` | `LAB_R_1` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_R_1`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_dt_3` | `LAB_DT_3` | data | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_DT_3`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_s_5` | `LAB_S_5` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_S_5`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_s_4` | `LAB_S_4` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_S_4`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `lab_s_3` | `LAB_S_3` | texto | Dado de exame laboratorial registrado na ficha de Leptospirose (`LAB_S_3`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `con_criter` | `CON_CRITER` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_CRITER`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_ambien` | `CON_AMBIEN` | texto | Característica do local Provável da fonte de infecção Ambiente da infecção | 1-Domiciliar 2-Trabalho 3-Lazer 4-Outro 9-Ignorado | todos |
| `con_inf_pa` | `CON_INF_PA` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_INF_PA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_inf_uf` | `CON_INF_UF` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_INF_UF`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_inf_mu` | `CON_INF_MU` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_INF_MU`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_evoluc` | `CON_EVOLUC` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_EVOLUC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_doenca` | `CON_DOENCA` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_DOENCA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_esgoto` | `CON_ESGOTO` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_ESGOTO`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_alimen` | `CON_ALIMEN` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_ALIMEN`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_animai` | `CON_ANIMAI` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_ANIMAI`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_rio` | `CON_RIO` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_RIO`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_entulh` | `CON_ENTULH` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_ENTULH`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_terren` | `CON_TERREN` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_TERREN`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_enchen` | `CON_ENCHEN` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_ENCHEN`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_roedor` | `CON_ROEDOR` | texto | Dado de conclusão do caso na ficha de Leptospirose (`CON_ROEDOR`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_dt_enc` | `CON_DT_ENC` | data | Dado de conclusão do caso na ficha de Leptospirose (`CON_DT_ENC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_dt_obi` | `CON_DT_OBI` | data | Dado de conclusão do caso na ficha de Leptospirose (`CON_DT_OBI`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `nduplic` | `NDUPLIC` | texto | Indicador de duplicidade do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2000 |
| `in_vincula` | `IN_VINCULA` | texto | Vinculação. 0 ou branco – Não Vinculado 1 – Vinculado | — | só em 2000 |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | 2008 a 2026 |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | 2008 a 2026 |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | 2008 a 2026 |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | 2008 a 2026 |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | 2008 a 2026 |
| `nduplic_n` | `NDUPLIC_N` | texto | Não Listar/ Não Contar. 0 ou branco – Não identificado 1 – Não é duplicidade (não listar) 2 – Duplicidade (não contar) | — | 2008 a 2026 |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | 2008 a 2026 |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | 2008 a 2026 |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | 2008 a 2026 |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | 2008 a 2026 |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | 2008 a 2026 |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | 2008 a 2026 |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | 2008 a 2026 |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | 2008 a 2026 |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | 2008 a 2026 |
| `cs_flxret` | `CS_FLXRET` | texto | Fluxo de retorno. Identifica se o registro está habilitado ou foi enviado pelo fluxo de retorno para o município de residência | 0 - Não 1 - habilitado para envio. 2 - enviado | 2008 a 2026 |
| `flxrecebi` | `FLXRECEBI` | texto | Recebida por fluxo de retorno (campo interno). Colocar a estrutura do nº atribuído pelo sistema | — | 2008 a 2026 |
| `migrado_w` | `MIGRADO_W` | texto | Identifica migração (campo interno). Identifica se o registro é oriundo da rotina de migração da base Windows | 1- migrado do Sinan Windows | 2008 a 2026 |
| `dt_invest` | `DT_INVEST` | data | Data da Investigação. Data em que ocorreu a investigação – informar a data da 1ª visita ao paciente | — | 2008 a 2026 |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/Ramo de Atividade Econômica. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O | — | 2008 a 2026 |
| `ant_cb_cai` | `ANT_CB_CAI` | texto | Situações de risco ocorrida nos 30 dias que antecederam os primeiros sintomas Caixa d´água | 1-Sim; 2-Não; 9- Ignorado | 2008 a 2026 |
| `ant_cb_sin` | `ANT_CB_SIN` | texto | Situações de risco ocorrida nos 30 dias que antecederam os primeiros sintomas | 1-Sim; 2-Não; 9- Ignorado | 2008 a 2026 |
| `ant_cb_pla` | `ANT_CB_PLA` | texto | Situações de risco ocorrida nos 30 dias que antecederam os primeiros sintomas Plantio/colheita (lavoura) | 1-Sim; 2-Não; 9- Ignorado | 2008 a 2026 |
| `ant_cb_gra` | `ANT_CB_GRA` | texto | Situações de risco ocorrida nos 30 dias que antecederam os primeiros sintomas Armazenamento de grãos/alimentos | 1-Sim; 2-Não; 9- Ignorado | 2008 a 2026 |
| `ant_cb_ter` | `ANT_CB_TER` | texto | Situações de risco ocorrida nos 30 dias que antecederam os primeiros sintomas Terreno baldio | 1-Sim; 2-Não; 9- Ignorado | 2008 a 2026 |
| `ant_ou_des` | `ANT_OU_DES` | texto | Situações de risco. Habilitar se campo | 1-Sim; 2-Não; 9- | 2008 a 2026 |
| `cli_prost` | `CLI_PROST` | texto | Sinais e sintomas – Prostração | 1-Sim; 2-Não; 9- Ignorado | 2008 a 2026 |
| `cli_pantur` | `CLI_PANTUR` | texto | Sinais e sintomas – Dor na panturrilha | 1-Sim; 2-Não; 9- Ignorado | 2008 a 2026 |
| `cli_hemopu` | `CLI_HEMOPU` | texto | Sinais e sintomas – Hemorragia Pulmonar | 1-Sim; 2-Não; 9- Ignorado | 2008 a 2026 |
| `cli_outros` | `CLI_OUTROS` | texto | Sinais e sintomas – Outros | 1-Sim; 2-Não; 9- Ignorado | 2008 a 2026 |
| `cli_otrdes` | `CLI_OTRDES` | texto | Sinais e sintomas – Outros Se Outras especificar. VARCHAR2(30 ) | — | 2008 a 2026 |
| `lab_elis_1` | `LAB_ELIS_1` | texto | Resultado 1ª Amostra | 1-Reagente 2-Não Reagente 3-Inconclusivo 4-Não realizado | 2008 a 2026 |
| `lab_elis_2` | `LAB_ELIS_2` | texto | Resultado 2ª Amostra | 1-Reagente 2-Não Reagente 3-Inconclusivo 4-Não realizado | 2008 a 2026 |
| `dtmicro1` | `DTMICRO1` | data | Data da Coleta – Micro 1ª amostra. Deve ser maior ou igual à data de Primeiros Sintomas | — | 2008 a 2026 |
| `micro1_s1` | `MICRO1_S1` | texto | Micro 1ª Amostra 1º Sorovar | — | 2008 a 2026 |
| `micro1_t_1` | `MICRO1_T_1` | texto | Micro 1ª Amostra título | — | 2008 a 2026 |
| `micro1_s_2` | `MICRO1_S_2` | texto | Micro 1ª Amostra 2º Sorovar | — | 2008 a 2026 |
| `micro1_t_2` | `MICRO1_T_2` | texto | Micro 1ª Amostra título | — | 2008 a 2026 |
| `lab_micr_1` | `LAB_MICR_1` | texto | Resultado MICRO aglutinação 1ª amostra | 1-Reagente 2-Não Reagente 3-Não Realizada 9-Ignorado | 2008 a 2026 |
| `dtmicro2` | `DTMICRO2` | data | Data da Coleta – Micro 2ª amostra. Deve ser maior que a data de coleta – Micro 1ª amostra | — | 2008 a 2026 |
| `micro2_s1` | `MICRO2_S1` | texto | Resultado 2ª Amostra 1º Sorovar | — | 2008 a 2026 |
| `micro2_t_1` | `MICRO2_T_1` | texto | Micro 2ª Amostra título | — | 2008 a 2026 |
| `micro2_s_2` | `MICRO2_S_2` | texto | Resultado 2ª Amostra 2º Sorovar | — | 2008 a 2026 |
| `micro2_t_2` | `MICRO2_T_2` | texto | Micro 2ª Amostra título | — | 2008 a 2026 |
| `lab_micr_2` | `LAB_MICR_2` | texto | Resultado MICRO aglutinação 2ª amostra | 1-Reagente 2-Não Reagente 3-Não Realizada 9-Ignorado | 2008 a 2026 |
| `dtisola` | `DTISOLA` | data | Isolamento – Data da Coleta. Data da Coleta deverá ser maior ou igual à Data dos Primeiros Sintomas | — | 2008 a 2026 |
| `res_isol` | `RES_ISOL` | texto | Isolamento – Resultado | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | 2008 a 2026 |
| `dtimuno` | `DTIMUNO` | data | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2008 a 2026 |
| `res_imuno` | `RES_IMUNO` | texto | Imunohistoquímica – Resultado | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | 2008 a 2026 |
| `dt_pcr` | `DT_PCR` | data | RT-PCR – Data da Coleta. Data da Coleta deverá ser maior ou igual à Data dos Primeiros Sintomas | — | 2008 a 2026 |
| `res_pcr` | `RES_PCR` | texto | RT-PCR – Resultado | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | 2008 a 2026 |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação Final | 1- Confirmado 2- Descartado | 2008 a 2026 |
| `criterio` | `CRITERIO` | texto | Critério de confirmação ou Descarte | 1-Clínico Laboratorial 2-Clínico Epidemiológico | 2008 a 2026 |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência?. Indica se o caso é autóctone do município de residência | 1 – Sim 2 – Não 3 – Indeterminado | 2008 a 2026 |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o paciente foi provavelmente | — | 2008 a 2026 |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente infectado | — | 2008 a 2026 |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). Código do município onde o paciente foi provavelmente infectado. O nome está associado ao código na tabela de municípios | — | 2008 a 2026 |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho | 1 – Sim 2 – Não 9 – Ignorado | 2008 a 2026 |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso | 1-Cura; 2-Óbito por leptospirose 3 Óbito por outras causas 9-Ignorado | 2008 a 2026 |
| `dt_obito` | `DT_OBITO` | data | Data do Óbito. Data da ocorrência do óbito | — | 2008 a 2026 |
| `dt_encerra` | `DT_ENCERRA` | data | Data do Encerramento. Data do encerramento da investigação | — | 2008 a 2026 |
| `dt_risco1` | `DT_RISCO1` | data | Informações complementares Data 1. Data e endereço se esteve em situação de risco ocorrida nos 30 dias que antecederam os primeiros sintomas | — | 2008 a 2026 |
| `dt_risco2` | `DT_RISCO2` | data | Informações complementares Data 2. Data e endereço se esteve em situação de risco ocorrida nos 30 dias que antecederam os primeiros sintomas | — | 2008 a 2026 |
| `dt_risco3` | `DT_RISCO3` | data | Informações complementares Data 3. Data e endereço se esteve em situação de risco ocorrida nos 30 dias que antecederam os primeiros sintomas | — | 2008 a 2026 |
| `dt_risco4` | `DT_RISCO4` | data | Informações complementares Data 4. Data e endereço se esteve em situação de risco ocorrida nos 30 dias que | — | 2008 a 2026 |
| `co_mun_r1` | `CO_MUN_R1` | texto | Informações complementares Município 1. Data e endereço se esteve em situação de risco ocorrida nos 30 dias que antecederam os primeiros sintomas | — | 2008 a 2026 |
| `co_mun_r2` | `CO_MUN_R2` | texto | Informações complementares Município 2. Data e endereço se esteve em situação de risco ocorrida nos 30 dias que antecederam os primeiros sintomas | — | 2008 a 2026 |
| `co_mun_r3` | `CO_MUN_R3` | texto | Informações complementares Município 3. Data e endereço se esteve em situação de risco ocorrida nos 30 dias que antecederam os primeiros sintomas | — | 2008 a 2026 |
| `co_mun_r4` | `CO_MUN_R4` | texto | Informações complementares Município 4. Data e endereço se esteve em situação de risco ocorrida nos 30 dias que antecederam os primeiros sintomas | — | 2008 a 2026 |
| `co_uf_r1` | `CO_UF_R1` | texto | Informações complementares UF 1. Data e endereço se esteve em situação de risco ocorrida nos 30 dias que antecederam os primeiros sintomas | — | 2008 a 2026 |
| `co_uf_r2` | `CO_UF_R2` | texto | Informações complementares UF 2. Data e endereço se esteve em situação de risco ocorrida nos 30 dias que antecederam os primeiros sintomas | — | 2008 a 2026 |
| `co_uf_r3` | `CO_UF_R3` | texto | Informações complementares. Data e endereço se esteve em situação | — | 2008 a 2026 |
| `co_uf_r4` | `CO_UF_R4` | texto | Informações complementares UF 4. Data e endereço se esteve em situação de risco ocorrida nos 30 dias que antecederam os primeiros sintomas | — | 2008 a 2026 |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | 2008 a 2026 |

## No lake

- **Dataset no lake:** `datasus/sinan-lept`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 30, inteiro: 1, nulo (vazio nas amostras): 2, texto: 145.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-lept.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- forte sazonalidade com picos de chuvas e enchentes; atenção à separação entre incidência e subnotificação de casos laboratoriais não confirmados em surtos; cuidado com o grande número de notificações descartadas (diagnósticos diferenciais de outras febres agudas); parte dos casos ocupacionais também aparece em bases de vigilância de acidentes de trabalho, o que exige deduplicação; e o arquivo do ano em curso em `PRELIM` é sujeito a revisão. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 128 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-lept").glob("**/*.parquet"))
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
datasus-fetcher list sinan-lept

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-lept -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-lept
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Leptospirose (ficha e dicionário)**: https://portalsinan.saude.gov.br/leptospirose
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo Leptospirose
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
