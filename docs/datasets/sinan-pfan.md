---
dataset:
  id: sinan-pfan
  fonte: datasus
  titulo: Paralisia Flácida Aguda
  resumo: 'Paralisia Flácida Aguda do DATASUS: uma ficha de notificação/investigação de paralisia Flácida Aguda.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de paralisia Flácida Aguda
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 179
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_doses: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_l_cel1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_l_lin1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_l_pro1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_l_gli1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_l_cl1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_l_cel2: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_l_lin2: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_l_pro2: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_l_gli2: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_l_cl2: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Paralisia Flácida Aguda (`sinan-pfan`)

## Resumo

O `sinan-pfan` contém os microdados das notificações e investigações epidemiológicas de casos de Paralisia Flácida Aguda (PFA, CID-10 A80, G99.8 e correlatos) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha de notificação/investigação de um caso suspeito de PFA, em todos os menores de 15 anos com paralisia flácida aguda ou pessoas de qualquer idade com suspeita de poliomielite. É a base central da vigilância de poliomielite no Brasil, com o leiaute mais extenso do lote (178 colunas na ficha v5.0, revisão abril/2012): investigação clínica detalhada (força muscular e tônus por membro, sensibilidade por região, reflexos), amostras de fezes/liquor, diagnóstico laboratorial (isolamento de poliovírus e diferenciação intraespecífica para vírus selvagem e vírus derivado de cepa vacinal — PVDV) e a avaliação de sequelas a 60 dias.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `PFAN` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `PFAN` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `PFANBR25.dbc` — `PFAN` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As consolidações até 2022 estão em `FINAIS` e os anos de 2023 a 2026 estão apenas em `PRELIM` (ex.: `PFANBR26.dbc`, atualização de 21/09/2026).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-pfan/<AAAA>/sinan-pfan_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-pfan/2024/sinan-pfan_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

A paralisia flácida aguda é agravo de notificação compulsória universal para menores de 15 anos (e qualquer idade com suspeita de poliomielite, A80) desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, com regulamentação hoje consolidada na Portaria GM/MS nº 204/2016. A vigilância é operada pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) em articulação com o GT-SINAN, os Comitês Regionais e o laboratório nacional de referência da OMS (Fiocruz/RJ), com o objetivo de certificar a interrupção da transmissão do poliovírus selvagem e do vírus derivado de cepa vacinal (VDPV). A base alimenta os indicadores oficiais acordados com a OMS: taxa de notificação mínima de 1 caso de PFA por 100 mil menores de 15 anos, percentual de casos com investigação completa, percentual de casos com coleta adequada de amostras (2 amostras de fezes em até 14 dias), investigação de sequelas a 60 dias e resposta rápida na eventual hipótese de reintrodução do poliovírus (alerta máximo da saúde global).

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Paralisia Flácida Aguda** do SINAN. A notificação nasce com o caso suspeito (paralisia flácida aguda de início súbito em menores de 15 anos, ou pessoa de qualquer idade com suspeita de poliomielite) e é completada com a investigação clínica pormenorizada (força muscular e tônus por membro, sensibilidade, reflexos e raio X), as duas coletas de fezes e liquor para cultura/estudos laboratoriais (`LAB_*`), o antecedente de vacinação (VOP/IPV, doses e datas), o seguimento ao 60º dia da evolução (força muscular e revisão das sequelas: `EVOR_*`, `EVOR1_DT_R`) e a classificação final (confirmado, compatível, associado à vacina, descartado ou confirmado PVDV). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. O instrumento é revisado periodicamente (rev. abril/2012) e acompanhou as mudanças das estratégias da OPAS/OMS para a verificação da interrupção da transmissão do poliovírus — inclusive a diferenciação entre vírus selvagem, vírus derivado de cepa vacinal (PVDV) e outros agentes diagnosticados como síndrome de Guillain-Barré (o CID do caso descartado `CON_DESCAR`), com blocos clínicos, laboratoriais, de seguimento e de diagnóstico distribuídos ao longo da ficha estruturada.

Aplicações analíticas típicas: monitoramento da incidência de PFA (casos notificados por 100 mil menores de 15 anos, comparado às metas da OMS); distribuição das classificações finais (confirmado, compatível, associado à vacina, descartado e confirmado PVDV); percentual de casos com coletas exitosas (2 amostras de fezes coletadas em até 14 dias, `LAB_DT_F1`/`LAB_DT_F2`); percentual de casos com seguimento ao 60º dia (`EVOR1_DT_R`) e sequelas classificadas; diagnóstico dos CID-10 dos casos descartados (`CON_DESCAR`, com predomínio da síndrome de Guillain-Barré — G61.0); e vigilância de eventual reintrodução do poliovírus selvagem ou vírus derivado de cepa vacinal (VDPV).

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-09-21.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `PFANBR25.dbc` (178 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `NU_IDADE_N` / `CS_SEXO` | Inteiro/String | Idade decomposta por unidade e sexo (casos de menores de 15 anos e outras idades com suspeita de pólio) |
| `DTPRICONS` | Data (`AAAAMMDD`) | Data da primeira consulta pelo serviço de saúde por motivo da paralisia |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `ANT_VACINA` / `ANT_DOSES` / `ANT_DT_VAC` / `ANT_30_DIA` | Inteiro/Data | Antecedentes de vacinação contra poliomielite (dose aplicada, nº de doses, data e vacinação nos 30 dias anteriores) |
| `CLI_FEBRE`/`CLI_DIARRE`/`CLI_DORES`/`CLI_VOMITO`/`CLI_CEFALE`/`CLI_OUTROS` | Inteiro | Sintomas prodrômicos: febre, diarreia, dores, vômitos, cefaléia e outros |
| `CLI_AGUDA`/`CLI_FLACID`/`CLI_ASSIME`/`CLI_PROGRE`/`CLI_ASCEND`/`CLI_DESCEN` | Inteiro | Características da paralisia: início agudo, flacidez, assimetria, progressão ascendente/descendente |
| `CLI_F_MIE`/`CLI_F_MSE`/`CLI_F_MID`/`CLI_F_MSD` | Inteiro | Força muscular por membro (membro inferior esquerdo/direito, superior esquerdo/direito) |
| `LOCA_MIE_N`/`LOCA_MSE_N`/`LOCA_MID_N`/`LOCA_MSD_N` | Inteiro | Localização da fraqueza por membro (nº do segmento acometido) |
| `CLI_RESPIR`/`CLI_CERVIC`/`CLI_FACE`/`CLI_KERNIG`/`CLI_NUCA`/`CLI_BRUDZ`/`CLI_CONTAT` | Inteiro | Comprometimento respiratório, cervical, facial; sinal de Kernig/Brudzinski; rigidez de nuca; contato com casos de PFA |
| `CLI_INJECA`/`CLI_LOCAL` | Inteiro | Piora após injeção aplicada no membro paralisado |
| `CLI_A_*` | Inteiro | Bloco de avaliação clínico-neuromuscular por membro: força, tônus, sensibilidade e reflexos (campos `CLI_A_F*`, `CLI_A_T*`, `CLI_A_S*`, `CLI_AQ_*`, `CLI_PAT*`, `CLI_BIC*`, `CLI_TRIE*` etc.) |
| `ATE_HIPOTE`/`ATE_HOSP`/`ATE_DT_INT`/`ATE_UF`/`ATE_MUNICI` | Inteiro/Data/String | Hospitalização, data, UF e município da internação |
| `LAB_DT_F1`/`LAB_DT_F2` | Data | Datas de coleta das amostras de fezes |
| `LAB_RES_F1`/`LAB_RES_F2`/`LAB_RES_F3` | Inteiro | Resultados do isolamento de poliovírus nas amostras de fezes |
| `LAB_DT_L_1`/`LAB_L_CEL1`/`LAB_L_LIN1`/`LAB_L_PRO1`/`LAB_L_GLI1`/`LAB_L_CL1` | Data/Inteiro | Liquor: data da coleta, células, linfócitos, proteínas, glicose e cloro |
| `LAB_E_D_1`/`LAB_CELEBR`/`LAB_MEDULA`/`LAB_INTEST` | Data/Inteiro | Exames complementares: eletromiografia, biópsia cerebral, medula espinal e intestino |
| `LAB_DT_R1`/`LAB_DT_C1`/`LAB_RESULT` | Data/Inteiro | Revisão das amostras não-coletadas/exames e resultado conclusivo |
| `EVOR_*`/`EVOR1_DT_R` | Inteiro/Data | Acompanhamento da 60ª dia: força muscular por membro (`EVOR_F_*`), tônus (`EVOR_A_*`), sensibilidade por região (`EVOR_S_*`/`REFR_*`) e data da revisão |
| `CLASSI_FIN` | Inteiro | Classificação final: 1 - Confirmado, 2 - Compatível, 3 - Associado à vacina, 4 - Descartado, 5 - Confirmado PVDV |
| `CRITERIO` | Inteiro | Critério de classificação: 1 - Laboratorial, 2 - Clínico Epidemiológico, 3 - Perda de Seguimento, 4 - Óbito, 5 - Evolução |
| `CON_DESCAR` | String (5) | CID-10 do caso descartado (ex.: síndrome de Guillain-Barré — G61.0) |
| `EVOLUCAO` | Inteiro | Evolução do caso: 1 - Cura com sequela, 2 - Cura sem sequela, 3 - Óbito por PFA/Pólio, 4 - Óbito por outras causas, 9 - Ignorado |
| `DT_OBITO` / `DT_ENCERRA` | Data (`AAAAMMDD`) | Data do óbito e de encerramento da investigação |

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
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno) | — | todos |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil) | — | todos |
| `nduplic_n` | `NDUPLIC_N` | texto | Não Listar/ Não Contar. 0 ou branco – Não identificado 1 – Não é duplicidade (não listar) 2 – Duplicidade (não contar) | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | todos |
| `cs_flxret` | `CS_FLXRET` | texto | Fluxo de retorno. Identifica se o registro está habilitado ou foi enviado pelo fluxo de retorno para o município de residência | 0 - Não 1 - habilitado para envio. 2 - enviado | todos |
| `flxrecebi` | `FLXRECEBI` | texto | Recebida por fluxo de retorno (campo interno). Colocar a estrutura do nº atribuído pelo sistema | — | todos |
| `migrado_w` | `MIGRADO_W` | texto | Identifica migração (campo interno). Identifica se o registro é oriundo da rotina de migração da base Windows | 1- migrado do Sinan Windows | todos |
| `dtpricons` | `DTPRICONS` | data | Data da 1º Consulta. Data da primeira consulta | — | todos |
| `dt_invest` | `DT_INVEST` | data | Data da Investigação. Informe a data do início da investigação | — | todos |
| `ant_vacina` | `ANT_VACINA` | texto | Tomou Vacina Contra Poliomielite. Informar se tomou ou não vacina contra Pólio | 1 – Sim 2 – Não 9 - Ignorado | todos |
| `ant_doses` | `ANT_DOSES` | inteiro | Número de doses válidas. Informar o nº de doses de vacina Sabin/anti-pólio recebidas | — | todos |
| `ant_dt_vac` | `ANT_DT_VAC` | data | Data da Última Dose da Vacina. Informar a data da última dose de vacina Sabin/anti- pólio oral recebida | — | todos |
| `ant_30_dia` | `ANT_30_DIA` | texto | Viajou ou recebeu visitas provenientes de áreas endêmicas de poliomielite nos 30 dias Anteriores ao início da Deficiência motora?. Informar se viajou nos 30 dias anteriores a deficiência motora | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_pais` | `ANT_PAIS` | texto | Se sim, País origem. Informar o país para onde viajou | — | todos |
| `cli_febre` | `CLI_FEBRE` | texto | Sinais e sintomas Febre. Se o paciente apresentou febre | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_diarre` | `CLI_DIARRE` | texto | Sinais e sintomas Diarréia. Se o paciente apresentou diarréia | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_dores` | `CLI_DORES` | texto | Sinais e sintomas Dores Musculares. Se o paciente apresentou dores musculares | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_sintom` | `CLI_SINTOM` | texto | Sinais e sintomas Sint. Respiratórios. Se o paciente apresentou sintomas respiratórios | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_vomito` | `CLI_VOMITO` | texto | Sinais e sintomas Vômito. Se o paciente apresentou vômitos | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_obstip` | `CLI_OBSTIP` | texto | Sinais e sintomas Obstipação. Se o paciente apresentou obstipação | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cefale` | `CLI_CEFALE` | texto | Sinais e sintomas Cefaléia. Se o paciente apresentou cefaléia | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_outros` | `CLI_OUTROS` | texto | Sinais e sintomas Se outros especificar. Se o paciente apresentou outros sintomas | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `outros_des` | `OUTROS_DES` | texto | Sinais e sintomas outros Especificar. Se o paciente apresentou outros sinais e sintomas especificar | — | todos |
| `cli_dt` | `CLI_DT` | data | Data de início da Def. Motora. Informar a data de inicio da deficiência motora | — | todos |
| `cli_aguda` | `CLI_AGUDA` | texto | Deficiência motora Aguda. Informar se o paciente apresentou deficiência motora aguda | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_flacid` | `CLI_FLACID` | texto | Deficiência motora Flácida. Informar se o paciente apresentou deficiência motora flácida | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_assime` | `CLI_ASSIME` | texto | Deficiência motora Assimétrica | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_progre` | `CLI_PROGRE` | texto | Deficiência motora Progressão após 3 Dias | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_ascend` | `CLI_ASCEND` | texto | Deficiência motora Ascendente | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_descen` | `CLI_DESCEN` | texto | Deficiência motora Descendente | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_f_mie` | `CLI_F_MIE` | texto | Força Muscular MIE. e | 1. Diminuída 2. Ausente 3. Normal 9. Ignorado | todos |
| `cli_f_mse` | `CLI_F_MSE` | texto | Força Muscular MSE. e | 1. Diminuída 2. Ausente 3. Normal 9. Ignorado | todos |
| `cli_f_mid` | `CLI_F_MID` | texto | Força Muscular MSD. d | 1. Diminuída 2. Ausente 3. Normal 9. Ignorado | todos |
| `cli_f_msd` | `CLI_F_MSD` | texto | Manifestação clínica registrada na ficha de Paralisia Flácida Aguda (`CLI_F_MSD`); o dicionário consultado não define o campo isoladamente | — | todos |
| `loca_mie_n` | `LOCA_MIE_N` | texto | Localização MIE. Informar a localização da deficiência no membro inferior esquerdo | 1. Distal 2. Proximal 3. Todo o membro 9. Ignorado | todos |
| `loca_mse_n` | `LOCA_MSE_N` | texto | Localização MSE. Informar a localização da deficiência no membro superior esquerdo | 1. Distal 2. Proximal 3. Todo o membro 9. Ignorado | todos |
| `loca_mid_n` | `LOCA_MID_N` | texto | Localização MID. Informar a localização da deficiência no membro inferior direito | 1. Distal 2. Proximal 3. Todo o membro 9. Ignorado | todos |
| `loca_msd_n` | `LOCA_MSD_N` | texto | Localização MSD. Informar a localização da deficiência no membro superior direito | 1- Distal 2- Proximal 3- Todo o membro 9- Ignorado | todos |
| `cli_respir` | `CLI_RESPIR` | texto | Comprometimen to de Musculatura Respiratória | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cervic` | `CLI_CERVIC` | texto | Comprometimen to de Musculatura Cervical | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_face` | `CLI_FACE` | texto | Comprometimento de Face | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_dt_exa` | `CLI_DT_EXA` | data | Data do exame. Informar data de realização do exame na fase aguda | — | todos |
| `cli_a_fmie` | `CLI_A_FMIE` | texto | Força Muscular MIE. ular_mie | 1- Diminuída 2- Ausente 3- Normal 9- Ignorado | todos |
| `cli_a_fmse` | `CLI_A_FMSE` | texto | Força Muscular MSE. ular_mse | 1- Diminuída 2- Ausente 3- Normal 9- Ignorado | todos |
| `cli_a_fmid` | `CLI_A_FMID` | texto | Força Muscular MID. ular_mid | 1- Diminuída 2- Ausente 3- Normal 9- Ignorado | todos |
| `cli_a_fmsd` | `CLI_A_FMSD` | texto | Força Muscular MSD. ular_msd | 1- Diminuída 2- Ausente 3- Normal 9- Ignorado | todos |
| `cli_a_tmie` | `CLI_A_TMIE` | texto | Tônus Muscular MIE. Informar situação doTônus muscular no MIE | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `cli_a_tmse` | `CLI_A_TMSE` | texto | Tônus Muscular MSE. Informar a situação do Tônus muscular No MSE | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `cli_a_tmid` | `CLI_A_TMID` | texto | Tônus Muscular MID. Informar a situação do Tônus muscular No MID | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `cli_a_tmsd` | `CLI_A_TMSD` | texto | Tônus Muscular MSD. Informar a situação do Tônus muscular no MSD | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `cli_a_t_ce` | `CLI_A_T_CE` | texto | Tônus Muscular Musculatura Cervical. Informar a situação do Tônus muscular Na Musculatura cervical | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `cli_a_t_fa` | `CLI_A_T_FA` | texto | Tônus Muscular Face. Informar a situação doTônus muscular Na Face | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `cli_a_smie` | `CLI_A_SMIE` | texto | Sensibilidade MIE. Informar a situação da Sensibilidade no MIE | 1- Diminuída 2- Ausente 3- Normal 4- Parestesia 5- Prejudicado 9- Ignorado | todos |
| `cli_a_smse` | `CLI_A_SMSE` | texto | Sensibilidade MSE. Informar a situação da Sensibilidade no MSE | 1- Diminuída 2- Ausente 3- Normal 4- Parestesia 5- Prejudicado 9- Ignorado | todos |
| `cli_a_smid` | `CLI_A_SMID` | texto | Sensibilidade MID. Informar a situação da Sensibilidade no MID | 1- Diminuída 2- Ausente 3- Normal 4- Parestesia 5- Prejudicado 9- Ignorado | todos |
| `cli_a_smsd` | `CLI_A_SMSD` | texto | Sensibilidade MSD. Informar a situação do da Sensibilidade MSD | 1- Diminuída 2- Ausente 3- Normal 4- Parestesia 5- Prejudicado 9- Ignorado | todos |
| `cli_a_s_fa` | `CLI_A_S_FA` | texto | Sensibilidade Face. varcha2r(1) | 1-Diminuída 2.Ausente 3.Normal 4.Parestesia 5.Prejudicado 9-gnorado | todos |
| `cli_aq_e_n` | `CLI_AQ_E_N` | texto | Reflexos Aquileu E. Informar a situação do Reflexo Aquileu Esquerdo | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `cli_aq_d_n` | `CLI_AQ_D_N` | texto | Reflexos Aquileu D. Informar a situação do Reflexo Aquileu Direito | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `cli_pate_n` | `CLI_PATE_N` | texto | Reflexos Patelar E. Informar a situação do Reflexo Patelar Esquerdo | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `cli_patd_n` | `CLI_PATD_N` | texto | Reflexos Patelar D. Informar a situação do Reflexo Patelar Direito | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `cli_bice_n` | `CLI_BICE_N` | texto | Reflexos Bicipital E. Informar a situação do Reflexo Bicipital Esquerdo | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `cli_bicd_n` | `CLI_BICD_N` | texto | Reflexos Bicipital D. Informar a situação do Reflexo Bicipital Direito | 1- Diminuído 1. Ausente 2. Normal 3. Aumentado 9- Ignorado | todos |
| `cli_trie_n` | `CLI_TRIE_N` | texto | Reflexos Tricipital E. Informar a situação do Reflexo Tricipital Esquerdo | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `cli_trid_n` | `CLI_TRID_N` | texto | Reflexos Tricipital D. Informar a situação do Reflexo Tricipital Direito | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `cli_fle_e` | `CLI_FLE_E` | texto | Reflexo Cutâneo Plantar Flexão E. Reflexo Cutâneo Plantar Flexão Esquerdo | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_fle_d` | `CLI_FLE_D` | texto | Manifestação clínica registrada na ficha de Paralisia Flácida Aguda (`CLI_FLE_D`); o dicionário consultado não define o campo isoladamente | — | todos |
| `cli_ext_e` | `CLI_EXT_E` | texto | Manifestação clínica registrada na ficha de Paralisia Flácida Aguda (`CLI_EXT_E`); o dicionário consultado não define o campo isoladamente | — | todos |
| `cli_ext_d` | `CLI_EXT_D` | texto | Reflexo Cutâneo Plantar Extensão D. Reflexo Cutâneo Plantar Extensão Direito | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_kernig` | `CLI_KERNIG` | texto | Sinais de irritação meníngea Kernig | 1. Ausente 2. Presente 9- Ignorado | todos |
| `cli_nuca` | `CLI_NUCA` | texto | Sinais de irritação meníngea Rigidez de nuca | 1- Ausente 2- Presente 9- Ignorado | todos |
| `cli_brudz` | `CLI_BRUDZ` | texto | Sinais de irritação meníngea Brudzinski | 1- Ausente 2- Presente 9- Ignorado | todos |
| `cli_contat` | `CLI_CONTAT` | texto | Contato ou Ingestão de Substâncias Tóxicas (Agrotóxicos, Chumbo, Mercúrio, Medicamentos). Contato ou ingestão de substâncias tóxicas | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_con_es` | `CLI_CON_ES` | texto | Caso afirmativo, especifique. Informar o nome da substância que teve contato ou ingeriu | — | todos |
| `cli_injeca` | `CLI_INJECA` | texto | História de Injeção Intramuscular | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_local` | `CLI_LOCAL` | texto | Local de Aplicação. Informar o lugar que foi aplicada (Glúteo/Braço/coxa) | 1 – MIE 2 – MSE 3 – MID 4 – MSD 5 – Glúteo E 6 – Glúteo D | todos |
| `ate_hipote` | `ATE_HIPOTE` | texto | Hipótese diagnóstica (vide tabela anexa) | — | todos |
| `ate_hosp` | `ATE_HOSP` | texto | Ocorreu hospitalização | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ate_dt_int` | `ATE_DT_INT` | data | Data de internação. Data de internação, caso tenha ocorrido | — | todos |
| `ate_uf` | `ATE_UF` | texto | UF. Sigla da UF onde o paciente foi internado | — | todos |
| `ate_munici` | `ATE_MUNICI` | texto | Município do Hospital. Nome completo do município onde o paciente foi internado | — | todos |
| `lab_dt_f1` | `LAB_DT_F1` | data | Data da Coleta. Informar a data que foi coletada a amostra de fezes | — | todos |
| `lab_dt_nle` | `LAB_DT_NLE` | data | Data do envio do Nível local para Estadual. Data do envio da amostra pelo Nível Local para o Estadual | — | todos |
| `lab_dt_cen` | `LAB_DT_CEN` | data | Data do envio do Nível estadual para LRR.. o | — | todos |
| `lab_dt_r1` | `LAB_DT_R1` | data | Data do recebimento no LRR. Data do recebimento da amostra de fezes no Laboratório | — | todos |
| `lab_q_f` | `LAB_Q_F` | texto | Quantidade. Informar se quantidade amostra de frezes coletada foi suficiente ou insuficiente | 1 – Suficiente 2 – Insuficiente | todos |
| `lab_con_f` | `LAB_CON_F` | texto | Condições. Informar se as condições da temperatura da amostra | 1 – Temperatura Adequada 2 – Temperatura Alterada | todos |
| `lab_dt_re1` | `LAB_DT_RE1` | data | Data do resultado. Data do resultado da amostra | — | todos |
| `lab_res_f1` | `LAB_RES_F1` | texto | Resultado. Informar o resultado liberado pelo LRR | 01 – P1 Vacinal 02 – P2 Vacinal 03 – P3 Vacinal 04 – P1 Selvagem 05 – P2 Selvagem 06 – P3 Selvagem 07 – Negativo 08 – Não Pólio 09 – Outros 10 – Inconclusivo 11 – PVDV 1 12 – PVDV 2 13 – PVDV 3 | todos |
| `lab_res_f2` | `LAB_RES_F2` | texto | Dado de exame laboratorial registrado na ficha de Paralisia Flácida Aguda (`LAB_RES_F2`); o dicionário consultado não define o campo isoladamente | — | todos |
| `lab_res_f3` | `LAB_RES_F3` | texto | Dado de exame laboratorial registrado na ficha de Paralisia Flácida Aguda (`LAB_RES_F3`); o dicionário consultado não define o campo isoladamente | — | todos |
| `lab_dt_l_1` | `LAB_DT_L_1` | data | Exame complementar 1 Líquor - Data da Coleta. Informar data da coleta do líquor e o resultado | — | todos |
| `lab_l_cel1` | `LAB_L_CEL1` | inteiro | Exame complementar 1 Líquor - Nº de Células/mm³. Informar número de células/mm 3 do Líquor | — | todos |
| `lab_l_lin1` | `LAB_L_LIN1` | inteiro | Exame complementar 1 Líquor - Linfócitos %. Informar número percentual de linfócitos do Líquor | — | todos |
| `lab_l_pro1` | `LAB_L_PRO1` | inteiro | Exame complementar 1 Líquor - Proteínas MG%. Informar número percentual de proteínas do Líquor | — | todos |
| `lab_l_gli1` | `LAB_L_GLI1` | inteiro | Exame complementar 1 Líquor - Glicose mg%. Informar número percentual de glicose do Líquor | — | todos |
| `lab_l_cl1` | `LAB_L_CL1` | inteiro | Exame complementar 1 Líquor - Cloreto MG%. Informar número percentual de cloreto do Líquor | — | todos |
| `lab_dt_l_2` | `LAB_DT_L_2` | data | Exame complementar 2 Líquor - Data da Coleta. Informar data da coleta do Líquor e o resultado | — | todos |
| `lab_l_cel2` | `LAB_L_CEL2` | inteiro | Exame complementar 2 Líquor - Nº de Células/mm³. Informar número de células/mm 3 do Líquor | — | todos |
| `lab_l_lin2` | `LAB_L_LIN2` | inteiro | Exame complementar 2 Líquor - Linfócitos %. Informar número percentual de linfócitos do Líquor | — | todos |
| `lab_l_pro2` | `LAB_L_PRO2` | inteiro | Exame complementar 2 Líquor - Proteínas MG%. Informar número percentual de proteínas do Líquor | — | todos |
| `lab_l_gli2` | `LAB_L_GLI2` | inteiro | Exame complementar 2 Líquor- Glicose MG%. Informar número percentual de glicose do Líquor | — | todos |
| `lab_l_cl2` | `LAB_L_CL2` | inteiro | Exame complementar 2 Líquor - Cloreto MG%. Informar número de cloreto do Líquor | — | todos |
| `lab_dt_e_1` | `LAB_DT_E_1` | data | Eletroneuromiograf ia Data da realização. Informar data de realização da 1ª Eletroneuromiografi a | — | todos |
| `lab_e_d_1` | `LAB_E_D_1` | texto | Diagnóstico Sugestivo de (tabela anexa). Ver tabela anexa | — | todos |
| `lab_celebr` | `LAB_CELEBR` | texto | Dado de exame laboratorial registrado na ficha de Paralisia Flácida Aguda (`LAB_CELEBR`); o dicionário consultado não define o campo isoladamente | — | todos |
| `lab_medula` | `LAB_MEDULA` | texto | Coletado material Anatomopatológi- co ? Médula. Informar se foi coletado material para exame Anatomopatológico da Médula | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `lab_intest` | `LAB_INTEST` | texto | Coletado material Anatomopatológi- co ? Intestino. Informar se foi coletado material para exame Anatomopatológico do Intestino | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `lab_dt_c1` | `LAB_DT_C1` | data | Data da Coleta. Informar da data de coleta de material Anatomopatológico | — | todos |
| `lab_result` | `LAB_RESULT` | texto | Resultado. Informar o resultado do exame Anatomopatológico | 1 – Compatível com poliomielite 2 – Não compatível com poliomielite | todos |
| `evor_dt_re` | `EVOR_DT_RE` | data | Data da Revisita. Informar a data que foi realizada a revisita | — | todos |
| `evor_f_mie` | `EVOR_F_MIE` | texto | Força Muscular MIE. c_mie | 1. Diminuída 2. Ausente 3. Normal 9- Ignorado | todos |
| `evor_f_mse` | `EVOR_F_MSE` | texto | Força Muscular MSE. c_mse | 1- Diminuída 2- Ausente 3- Normal 9- Ignorado | todos |
| `evor_f_mid` | `EVOR_F_MID` | texto | Força Muscular MID. c_mid | 1- Diminuída 2-Ausente 3-Normal 9- Ignorado | todos |
| `evor_f_msd` | `EVOR_F_MSD` | texto | Força Muscular MSD. c_msd | 1- Diminuída 2.Ausente 3.Normal 9- Ignorado | todos |
| `tonr_mie_n` | `TONR_MIE_N` | texto | Tônus Muscular MIE. Informar situação do Tônus muscular MIE | 1- Diminuída 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `tonr_mse_n` | `TONR_MSE_N` | texto | Tônus Muscular MSE. Informar situação doTônus muscular MSE | 1- Diminuída 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `tonr_mid_n` | `TONR_MID_N` | texto | Tônus Muscular MID. Informar situação doTônus muscular MID | 1- Diminuída 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `tonr_msd_n` | `TONR_MSD_N` | texto | Tônus Muscular MSD. Informar situação do Tônus muscular MSD | 1- Diminuída 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `tonr_cer_n` | `TONR_CER_N` | texto | Tônus Muscular Musculatura Cervical. Tônus muscular da Musculatura Cervical | 1- Diminuída 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `tonr_fac_n` | `TONR_FAC_N` | texto | Tônus Muscular Face. Informar situação doTônus muscular Face | 1- Diminuída 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `refr_aqe_n` | `REFR_AQE_N` | texto | Reflexos Aquileu E. Informar situação do Reflexo Aquileu E | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `refr_aqd_n` | `REFR_AQD_N` | texto | Reflexos Aquileu D. Informar situação do Reflexo Aquileu D | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `refr_pae_n` | `REFR_PAE_N` | texto | Reflexos Patelar E. Informar situação do Reflexo Patelar E | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `refr_pad_n` | `REFR_PAD_N` | texto | Reflexos Patelar D. Informar situação do Reflexo Patelar D | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `refr_bie_n` | `REFR_BIE_N` | texto | Reflexos Bicipital E. Informar situação do Reflexo Bicipital E | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `refr_bid_n` | `REFR_BID_N` | texto | Reflexos Bicipital D. Informar situação do Reflexo Bicipital D | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `refr_tre_n` | `REFR_TRE_N` | texto | Reflexos Tricipital E. Informar situação do Reflexo Tricipital E | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `refr_trd_n` | `REFR_TRD_N` | texto | Reflexos Tricipital D. Informar situação do ReflexoTricipital D | 1- Diminuído 2- Ausente 3- Normal 4- Aumentado 9- Ignorado | todos |
| `evor_rc_fe` | `EVOR_RC_FE` | texto | Reflexo Cutâneo Plantar Flexão E. Informar situação do Reflexo Cutâneo Plantar Flexão E | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `evor_rc_fd` | `EVOR_RC_FD` | texto | Reflexo Cutâneo Plantar Flexão D. Informar situação do Reflexo Cutâneo Plantar Flexão D | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `evor_rc_ee` | `EVOR_RC_EE` | texto | Reflexo Cutâneo Plantar Extensão E. e | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `evor_rc_ed` | `EVOR_RC_ED` | texto | Reflexo Cutâneo Plantar Extensão D. d | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `evor_a_mie` | `EVOR_A_MIE` | texto | Atrofia MIE. Informar a presença ou ausência Atrofia MIE | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `evor_a_mse` | `EVOR_A_MSE` | texto | Atrofia MSE. e | 1- Presente 2- Ausente 9- Ignorado | todos |
| `evor_a_mid` | `EVOR_A_MID` | texto | Atrofia MID. Informar a presença ou ausência Atrofia MID | 1- Presente 2- Ausente 9- Ignorado | todos |
| `evor_a_msd` | `EVOR_A_MSD` | texto | Atrofia MSD. d | 1- Presente 2- Ausente 9- Ignorado | todos |
| `evor_s_mie` | `EVOR_S_MIE` | texto | Sensibilidade MIE. de_mie | 1- Diminuída 2- Ausente 1- Normal 2- Parestesia 3- Prejudicado 9- Ignorado | todos |
| `evor_s_mse` | `EVOR_S_MSE` | texto | Sensibilidade MSE. de_mse | 1- Diminuída 2- Ausente 3- Normal 4- Parestesia 5- Prejudicado 9- Ignorado | todos |
| `evor_s_mid` | `EVOR_S_MID` | texto | Sensibilidade MID. de_mid | 1- Diminuída 2- Ausente 3- Normal 4- Parestesia 5- Prejudicado 9- Ignorado | todos |
| `evor_s_msd` | `EVOR_S_MSD` | texto | Sensibilidade MSD. de_msd | 1- Diminuída 2- Ausente 3- Normal 4- Parestesia 5- Prejudicado 9- Ignorado | todos |
| `evor_s_fac` | `EVOR_S_FAC` | texto | Sensibilidade Face. de_face | 1- Diminuída 2- Ausente 3- Normal 4- Parestesia 5- Prejudicado 9- Ignorado | todos |
| `evor1_dt_r` | `EVOR1_DT_R` | data | Data da Revisão. Informar a data de realização da revisão | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final. Informar a conclusão da investigação | 1- Confirmado 2- Compatível 3- Associado à vacina 4- Descartado 5- Confirmado PVDV | todos |
| `criterio` | `CRITERIO` | texto | Critério de Classificação. Informa o critério de classificação | 1- Laboratorial 2- Clinico Epidemiológico 3- Perda de Seguimento 4- Óbito 5- Evolução | todos |
| `con_descar` | `CON_DESCAR` | texto | Diagnóstico do Caso Descartado (vide tabela em anexo) | — | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução. Evolução do caso | 1- Cura com sequela 2- Cura sem sequela 3- Óbito por PFA/Pólio 4- Óbito por outras causas 9- Ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do Óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do Encerramento. Data do encerramento da investigação | — | todos |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-pfan`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 28, inteiro: 12, nulo (vazio nas amostras): 1, texto: 139.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-pfan.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- o caso confirmado exige 2 amostras de fezes (data de coleta até 14 dias do início da paralisia, `LAB_DT_F1`/`LAB_DT_F2`); os campos de evolução a 60 dias (`EVOR_*`) sustentam o critério "perda de seguimento" (`CRITERIO` = 3); o CID do caso descartado (`CON_DESCAR`) segue a tabela anexa da ficha (dentre elas, a síndrome de Guillain-Barré); e a força/sensibilidade é registrada por membro em blocos separados (`CLI_*` no diagnóstico e `EVOR_*`/`REFR_*` no seguimento), o que exige agregação cuidadosa para indicadores de paralisia residual. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-pfan").glob("**/*.parquet"))
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
datasus-fetcher list sinan-pfan

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-pfan -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-pfan
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Paralisia Flácida Aguda/Poliomielite (ficha e dicionário v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de paralisia flácida aguda/poliomielite; Diretrizes da OPAS/OMS para a vigilância e resposta rápida a HVDPV
