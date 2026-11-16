---
dataset:
  id: sinan-fmac
  fonte: datasus
  titulo: Febre Maculosa
  resumo: 'Febre Maculosa do DATASUS: uma ficha de notificação/investigação de febre Maculosa.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de febre Maculosa
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 98
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    tit_igm_s1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    tit_igg_s1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    tit_igm_s2: 'número inteiro: contagem ou código numérico (ver Descrição)'
    tit_igg_s2: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Febre Maculosa (`sinan-fmac`)

## Resumo

O `sinan-fmac` contém os microdados das notificações e investigações de casos de Febre Maculosa (FM Brasileira, CID-10 A77.0) e outras riquetsioses registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de febre maculosa, digitado no SINAN Net/Sinan Online. O agravo é de notificação compulsória imediata (até 24 horas) e a base tem elevada relevância clínica porque a doença tem alta letalidade quando não tratada rapidamente.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `FMAC` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `FMAC` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `FMACBR07.dbc` — prefixo `FMAC`, `BR` (consolidação nacional) e `07` (ano 2007), até `FMACBR21.dbc` (2021); os anos recentes ficam em `PRELIM` (ex.: `FMACBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-fmac/<AAAA>/sinan-fmac_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-fmac/2024/sinan-fmac_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## Conteúdo

A Febre Maculosa Brasileira é causada pela bactéria *Rickettsia rickettsii*, transmitida pela picada de carrapatos (sobretudo o carrapato-estrela *Amblyomma cajennense sensu lato*, com reservatórios silvestres como capivaras e roedores), e é a riquetsiose mais grave do continente. A vigilância é gerida pela SVSA/MS; o caso suspeito é de notificação compulsória imediata e a investigação inclui indicadores de letalidade historicamente altos (podendo ser superiores a 30-40% em áreas urbanas, pacientes geralmente internados em UTI). Casos de FM e de outras riquetsioses de interesse são fluxos mantidos em regiões endêmicas da Sudeste (Vale do Anhembi em SP, entre outros) e há ocorrência pontual no Sul e no Nordeste.

O evento gerador é a **Ficha de Investigação de Febre Maculosa** do SINAN (ficha `Febre_Maculosa_v5`, com dicionário de dados revisto em 2012), preenchida na suspeição — indivíduo com febre, cefaléia, mialgia e história de picada de carrapatos e/ou contato com animais domésticos/silvestres e/ou permanência em área sabidamente de transmissão nos últimos 15 dias e/ou exantema máculo-papular ou manifestações hemorrágicas — e completada ao longo da investigação com dados clínicos, laboratoriais (imunofluorescência indireta, reação em cadeia, PCR), hospitalização e desfecho. A unidade de análise é o caso suspeito/confirmado notificado individualmente.

Na lista de notificação compulsória inicial (Portaria SVS/MS nº 5/2006), o agravo constava já na versão SINAN de 2006, mas no FTP o primeiro arquivo final aceito é o de 2007; a partir de então, casos são recorrentes em épocas quentes. O SINAN posteriormente incorporou o registro da notificação de febre maculosa e de outras riquetsioses de interesse, com a vigência de notificação imediata estabelecida pela Portaria de Consolidação (GM/MS nº 204/2016) e atualizações recentes.

Aplicações analíticas: coeficiente de incidência, taxa de letalidade e mortalidade (a FM tem letalidade entre as mais altas dos agravos notificados no SINAN), distribuição por município provável de infecção, faixa etária e exposições (trabalhos em áreas de mata, capivaras urbanas), oportunidade de notificação (intervalo entre inicio de sintomas e notificação é decisivo para o desfecho) e vigilância de áreas com transmissão ativa.

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-08-25.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Febre Maculosa — CID-10 A77.0) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data de preenchimento da ficha de notificação (campo-chave; notificação imediata) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (febre, cefaléia, mialgia) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação (campo obrigatório da ficha de FM) |
| `ID_OCUPA_C` | String (6) | Ocupação/ramo de atividade econômica do paciente (CBO 6 dígitos) |
| `CLASSI_FIN` | Inteiro | Classificação final do caso (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
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
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno) | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil) | — | todos |
| `dt_invest` | `DT_INVEST` | data | Data da Investigação (Vig. Epidemiológica). Data de investigação do caso | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/Ramo de atividade Econômica. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo | — | todos |
| `febre` | `FEBRE` | texto | Sinais e Sintomas Febre. Informar se o paciente teve sinais/sintomas de febre | 1- Sim 2- Não 9- Ignorado | todos |
| `cefaleia` | `CEFALEIA` | texto | Sinais e Sintomas Cefaféia. Informar se o paciente teve sinais/sintomas de Cefaféia | 1- Sim 2- Não 9- Ignorado | todos |
| `abdominal` | `ABDOMINAL` | texto | Sinais e Sintomas Dor Abdominal. Informar se o paciente teve sinais/sintomas de Dor Abdominal | 1- Sim 2- Não 9- Ignorado | todos |
| `mialgia` | `MIALGIA` | texto | Sinais e Sintomas Mialgia. Informar se o paciente teve sinais/sintomas de Mialgia | 1- Sim 2- Não 9- Ignorado | todos |
| `nausea` | `NAUSEA` | texto | Sinais e sintomas Náusea/vômito. Informar se o paciente teve sinais/sintomas de Náusea/vômito | 1- Sim 2- Não 9- Ignorado | todos |
| `exantema` | `EXANTEMA` | texto | Sinais e Sintomas Exantema. Informar se o paciente teve sinais/sintomas de Exantema | 1- Sim 2- Não 9- Ignorado | todos |
| `diarreia` | `DIARREIA` | texto | Sinais e Sintomas Diarréia. Informar se o paciente teve sinais/sintomas de Diarréia | 1- Sim 2- Não 9- Ignorado | todos |
| `ictericia` | `ICTERICIA` | texto | Sinais e Sintomas Icterícia. Informar se o paciente teve sinais/sintomas de Icterícia | 1- Sim 2- Não 9- Ignorado | todos |
| `hiperemia` | `HIPEREMIA` | texto | Sinais e Sintomas Hiperemia Conjuntival. Informar se o paciente teve sinais/sintomas de Hiperemia Conjuntival | 1- Sim 2- Não 9- Ignorado | todos |
| `hepatome` | `HEPATOME` | texto | Sinais e Sintomas Hepatomegalia/Esplenomeg. a | 1- Sim 2- Não | todos |
| `petequias` | `PETEQUIAS` | texto | Sinais e Sintomas Petéquias. Informar se o paciente teve sinais/sintomas de Petéquias | 1- Sim 2- Não 9- Ignorado | todos |
| `hemorrag` | `HEMORRAG` | texto | Sinais e Sintomas Manifestações Hemorrágicas. s | 1- Sim 2- Não 9- Ignorado | todos |
| `linfadeno` | `LINFADENO` | texto | Sinais e sintomas Linfadenopatia. a | 1- Sim 2- Não 9- Ignorado | todos |
| `convulsao` | `CONVULSAO` | texto | Sinais e Sintomas Convulsão. Informar se o paciente teve sinais/sintomas de Convulsão | 1- Sim 2- Não 9- Ignorado | todos |
| `necrose` | `NECROSE` | texto | Sinais e Sintomas Necrose de extremidades. Informar se o paciente teve sinais/sintomas de Necrose de extremidades | 1- Sim 2- Não 9- Ignorado | todos |
| `prostacao` | `PROSTACAO` | texto | Sinais e Sintomas Prostração. Informar se o paciente teve sinais/sintomas de Prostração | 1- Sim 2- Não 9- Ignorado | todos |
| `choque` | `CHOQUE` | texto | Sinais e Sintomas Choque/Hipotensão. Informar se o paciente teve sinais/sintomas de Choque/Hipotensão | 1- Sim 2- Não 9- Ignorado | todos |
| `coma` | `COMA` | texto | Sinais e Sintomas Estupor/Coma. Informar se o paciente teve sinais/sintomas de Estupor/Coma | 1- Sim 2- Não 9- Ignorado | todos |
| `hemorragi` | `HEMORRAGI` | texto | Sinais e Sintomas Sufusão hemorrágica. Informar se o paciente teve sinais/sintomas de Sufusão Hemorrágica | 1- Sim 2- Não 9- Ignorado | todos |
| `respirato` | `RESPIRATO` | texto | Sinais e Sintomas Alterações Respiratórias. Informar se o paciente teve sinais/sintomas de Alterações Respiratórias | 1- Sim 2- Não 9- Ignorado | todos |
| `oliguria` | `OLIGURIA` | texto | Sinais e Sintomas Oligúria/Anúria. Informar se o paciente teve sinais/sintomas de Oligúria/Anúria | 1- Sim 2- Não 9- Ignorado | todos |
| `outros` | `OUTROS` | texto | Sinais e Sintomas Outros. Informar se o paciente teve outros sinais/sintomas | 1- Sim 2- Não 9- Ignorado | todos |
| `outro_esp` | `OUTRO_ESP` | texto | Sinais e Sintomas Outros Especificar. varchar2(30) | — | todos |
| `carrapato` | `CARRAPATO` | texto | Teve contato com animais? Carrapato | 1- Sim 2- Não 9- Ignorado | todos |
| `capivara` | `CAPIVARA` | texto | Teve contato com animais? Capivara | 1- Sim 2- Não 9- Ignorado | todos |
| `cao_gato` | `CAO_GATO` | texto | Teve contato com animais? Cão/Gato | 1- Sim 2- Não 9- Ignorado | todos |
| `bovino` | `BOVINO` | texto | Teve contato com animais? Bovinos | 1- Sim 2- Não 9- Ignorado | todos |
| `equinos` | `EQUINOS` | texto | Teve contato com animais? Eqüinos | 1- Sim 2- Não 9- Ignorado | todos |
| `outroani` | `OUTROANI` | texto | Teve contato com animais? Outros. o | 1- Sim 2- Não 9- Ignorado | todos |
| `anim_esp` | `ANIM_ESP` | texto | Teve contato com animais? Outros (especificar) | — | todos |
| `foi_mata` | `FOI_MATA` | texto | Freqüentou ambientes com vegetação(mata, floresta, rios, cachoeiras, etc) | 1- Sim 2- Não 9- Ignorado | todos |
| `hospital` | `HOSPITAL` | texto | Ocorreu Hospitalização | 1- Sim 2- Não 9- Ignorado | todos |
| `dtinterna` | `DTINTERNA` | data | Data da Internação. Informar a Data da Hospitalização | — | todos |
| `dtalta` | `DTALTA` | data | Data da alta. Informar a Data da alta | — | todos |
| `coufhosp` | `COUFHOSP` | texto | UF. UF do hospital onde ocorreu o tratamento | — | todos |
| `comunhosp` | `COMUNHOSP` | texto | Município do Hospital. Município do hospital onde ocorreu o tratamento | — | 2007 a 2017 |
| `diagno_lab` | `DIAGNO_LAB` | texto | Diagnóstico Laboratorial | 1 – Sim 2 – Não 9- Ignorado | todos |
| `dts1` | `DTS1` | data | Data da Coleta S1. Informar data da amostra S1 | — | todos |
| `dts2` | `DTS2` | data | Data da Coleta S 2. Informar data da amostra S2 | — | todos |
| `igm_s1` | `IGM_S1` | texto | Resultados sorologia S1 IgM. Informar o resultado da amostra S1 IgM | 1 – Positivo 2 – Negativo 3 – Inconclusivo 4 – Não realizado | todos |
| `tit_igm_s1` | `TIT_IGM_S1` | inteiro | Resultados sorologia S1 IGM títulos. os1 | — | todos |
| `igg_s1` | `IGG_S1` | texto | Resultados sorologia S1 IgG. Informar o resultado da amostra S1 IgG | 1 – Positivo 2 – Negativo 3 – Inconclusivo 4 – Não realizado | todos |
| `tit_igg_s1` | `TIT_IGG_S1` | inteiro | Resultados sorologia S1 IgG títulos. s1 | — | todos |
| `igm_s2` | `IGM_S2` | texto | Resultados sorologia S2 IgM. Informar o resultado da amostra S2IgM | 1 – Positivo 2 – Negativo 3 – Inconclusivo 4 – Não realizado | todos |
| `tit_igm_s2` | `TIT_IGM_S2` | inteiro | Resultados sorologia IgM S2 títulos. os2 | — | todos |
| `igg_s2` | `IGG_S2` | texto | Resultados sorologia S2 IgG. Informar o resultado da amostra S2 IgG | 1 – Positivo 2 – Negativo 3 – Inconclusivo 4 – Não realizado | todos |
| `tit_igg_s2` | `TIT_IGG_S2` | inteiro | Resultados sorologia IGG S2 títulos. s2 | — | todos |
| `dt_coleta` | `DT_COLETA` | data | Data da coleta. Informar a data da coleta | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `isolamento` | `ISOLAMENTO` | texto | Resultado Isolamento | 1– Detectado 2- Não Detectado 3- Não realizado | todos |
| `agente` | `AGENTE` | texto | Agente. Informar o remetente | — | todos |
| `histopato` | `HISTOPATO` | texto | Resultado Histopatologia. Informar o resultado Histopatologia | 1 – Positivo 2 – Negativo 3 – Inconclusivo 4 – Não realizado | todos |
| `imunohist` | `IMUNOHIST` | texto | Resultado Imunohistoquímica | 1 – Positivo 2 – Negativo 3 – Inconclusivo 4 – Não realizado | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação Final. Informar o diagnóstico definitivo | 1- Confirmado 2- Descartado | todos |
| `criterio` | `CRITERIO` | texto | Critério Confirmação/Descarte | 1 – Laboratório 2 – Clínico- Epidemiológico 3 – Clínico | todos |
| `diag_desca` | `DIAG_DESCA` | texto | Se descartado, Especificar diagnóstico | — | todos |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência?. a | 1 – Sim 2 – Não 3 – Indeterminado | todos |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o | — | todos |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente infectado | — | todos |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). Código do município onde o paciente foi provavelmente infectado. O nome está associado ao código na tabela de municípios | — | todos |
| `ambiente` | `AMBIENTE` | texto | Característica do Local Provável de Infecção Ambiente. Informar a Característica do Local Provável de Infecção - Ambiente | 1- Domiciliar 2- Trabalho 3- Lazer 4- Outro 9- Ignorado | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao Trabalho. Informar se a doença está relacionada ao ambiente de trabalho do paciente | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução. Informar a evolução do caso | 1- Cura 2- Óbito por febre maculosa 3- Óbito por outra causa 9- Ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do Óbito. Informar a data do óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Informar a data do encerramento | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2021 a 2026 |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | 2021 a 2026 |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | 2021 a 2026 |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | 2021 a 2026 |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | 2021 a 2026 |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | 2021 a 2026 |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | 2021 a 2026 |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | 2021 a 2026 |
| `ident_micr` | `IDENT_MICR` | texto | Identificação do micro (campo interno) | — | 2021 a 2026 |

## No lake

- **Dataset no lake:** `datasus/sinan-fmac`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 16, inteiro: 5, nulo (vazio nas amostras): 1, texto: 77.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-fmac.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- volume pequeno (20 consolidações `BR` anuais, ~6 MB), mas com concentrados de grande gravidade — a letalidade da FM é realçada; parte da investigação específica da ficha (exposição a carrapato, exames serológicos) fica em branco (as campos exigem pré-preenchimento apenas em unidades investigadoras); casos podem ser notificados em UF diferente da exposição (casos importados), refletidos nos campos de local provável de infecção; o arquivo do ano corrente em `PRELIM` é sujeito a revisão. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 10 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-fmac").glob("**/*.parquet"))
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
datasus-fetcher list sinan-fmac

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-fmac -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-fmac
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Febre Maculosa (ficha, instrucional, dicionário)**: http://portalsinan.saude.gov.br/febre-maculosa
- **Dicionário de Dados Febre Maculosa v5**: http://www.portalsinan.saude.gov.br/images/documentos/Agravos/Febre%20Maculosa/DIC_DADOS_Febre_Maculosa_v5.pdf
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo Febre Maculosa
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
