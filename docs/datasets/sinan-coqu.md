---
dataset:
  id: sinan-coqu
  fonte: datasus
  titulo: Coqueluche
  resumo: O sinan-coqu contém os microdados das notificações e investigações epidemiológicas de casos de Coqueluche/Pertússis (CID-10 A37) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde.
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de coqueluche
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 84
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    med_quan_c: 'número inteiro: contagem ou código numérico (ver Descrição)'
    quan_comun: 'número inteiro: contagem ou código numérico (ver Descrição)'
    quan_posit: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Coqueluche (`sinan-coqu`)

## Resumo

O `sinan-coqu` contém os microdados das notificações e investigações epidemiológicas de casos de Coqueluche/Pertússis (CID-10 A37) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de coqueluche, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. Com 83 colunas no leiaute v5.0, cobre o detalhamento clínico do período paroxístico (crises, cianose, apneia, vomitos), o histórico vacinal do paciente (doses de cómic DPT ou tetravalente), a situação da investigação de contatos e quimioprofilaxia (bloqueio) — instrumento central para a vigilância da coqueluche em menores de 1 ano e das ondas epidemicas registradas em intervalos de três a cinco anos no Brasil.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2007 a 2026 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 20 arquivos (~10,8 MB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim (diretório `PRELIM`)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `COQU` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `COQU` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `COQUBR25.dbc` — `COQU` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As consolidações até 2022 estão em `FINAIS` e os anos de 2023 a 2026 estão apenas em `PRELIM` (ex.: `COQUBR26.dbc`, atualização de 07/10/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-coqu/<ano>/sinan-coqu_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-coqu/2026/sinan-coqu_preliminar_2026-br@20261007.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

A coqueluche é doença de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, integrando hoje a Lista Nacional de Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) em articulação com o GT-SINAN, o Programa Nacional de Imunizações (DTP e dTpa, incluindo a vacinação de gestantes) e a rede de laboratórios de referência. A dinâmica epidemiológica da doença é cíclica (ondas epidêmicas a cada 3 a 5 anos) e a letalidade se concentra em lactentes menores de 6 meses — a base alimenta a detecção de situações de recrudescimento da pertússis e as análises de cobertura vacinal do PNI.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Coqueluche** do SINAN. A notificação nasce com a suspeição clínica (condição de tosse paroxística de mais de 15 dias, crises de tosse seguidas de vômitos ou cianose, tosse com tosso convulsivo) já na fase catarral (`DT_CATARRA`), e é completada ao longo da investigação com o registro clínico do período paroxístico (crises, cianose, apneia, vômitos, hospitalização), o histórico vacinal (`CS_VAC_N`, doses de DPT ou tetravalente e `DT_ULT_DOS`), a confirmação laboratorial por coleta de material de nasofaringe (`CS_COLETA`, `CS_CULTURA`) e a investigação de contatos com bloqueio (bloqueio vacinal, quimioprofilaxia ou ambos: `MED_BLOQUE`). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. Importantes revisões do instrumento e do vocabulário do dicionário datam de fevereiro/2012, período que acompanhou a vigência da vigilância intensificada de coqueluche, com a definição de casos clínicos para menores de 4 meses e casos confirmados por critério laboratorial ou vínculo epidemiológico — o histórico de doses reforçadas do PNI permanece registrado no instrumento.

Aplicações analíticas típicas: incidência anual de casos confirmados e taxa de letalidade; curva epidêmica por semana do início da tosse (`SEM_PRI`); desfechos de hospitalização (`CS_HOSPITA`, `DT_INTERNA`) e óbito (`EVOLUCAO`); percentual de casos com esquema vacinal conforme o PNI (análise de falhas de cobertura); investigação de comunicantes e bloqueios realizados (`QUAN_COMUN`, `QUAN_POSIT`, `MED_BLOQUE`); e análise específica de menores de 1 ano, grupo prioritário da vigilância.

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-10-29.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `COQUBR25.dbc` (83 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE do município de notificação e de residência |
| `NU_IDADE_N` | Inteiro composto | Idade (o primeiro dígito indica a unidade: dia/mês/ano) — grupo etário prioritário são os menores de 1 ano |
| `ANT_SENTIN` | Inteiro | Unidade sentinela de vigilância da coqueluche |
| `FC_CONTATO` | Inteiro | Contato com caso de coqueluche até 14 dias antes do início dos sintomas (domiciliar, vizinho, outro município/Estado, sem história de contato, ignorado) |
| `CS_VAC_N` | Inteiro | Nº de doses de vacina tríplice (DPT) ou tetravalente (DTP+Hib): 1 a 2 doses, 3 doses, 3 doses + reforços (opção 4/5), 6 - Nunca vacinado, 9 - Ignorado |
| `DT_ULT_DOS` | Data (`AAAAMMDD`) | Data da última dose da vacina DPT/tetravalente |
| `DT_CATARRA` | Data (`AAAAMMDD`) | Data de início do período catarral (referência epidemiológica para investigação de contatos) |
| `CS_TOSSE_E`/`CS_TOSSE_P` | Inteiro | Tosse com mais de 15 dias e tosse paroxística (1 - Sim, 2 - Não) |
| `CS_CRISE`/`CS_CIANOSE`/`CS_VOMITOS`/`CS_APNEIA` | Inteiro | Manifestações do período paroxístico: crises de tosse, cianose, vômitos e apneia |
| `CS_TEMP37`/`CS_TEMP_38` | Inteiro | Resposta térmica do paciente (temperatura ≥37,5 ºC e ≥38 ºC) |
| `CS_PNEUMON`/`CS_ENCEFAL`/`CS_DESITRA`/`CS_OTITE` | Inteiro | Complicações: pneumonia, encefalopatia, fissura/lesão do aspareza desidratação e otite média |
| `CS_HOSPITA` / `DT_INTERNA` | Inteiro / Data | Internação hospitalar e data de internação |
| `CS_COLETA`/`DT_COLETA`/`CS_CULTURA` | Inteiro/Data | Coleta de material (swab nasofaríngeo para cultura), data e resultado da cultura |
| `MED_IDEN_C`/`MED_QUAN_C`/`MED_CASO_S` | Inteiro | Contatos identificadas e suspeitos com eventos de caso índice, para orientar o bloqueio |
| `COLET_COMU`/`QUAN_COMUN`/`QUAN_POSIT` | Inteiro | Comunicantes com coleta de cultura, nº de comunicantes com resultado e nº de resultados positivos |
| `MED_BLOQUE` | Inteiro | Medidas de prevenção/controle: 1 - Bloqueio vacinal, 2 - Quimioprofilaxia, 3 - Ambos, 4 - Não, 9 - Ignorado |
| `CLASSI_FIN` | Inteiro | Classificação final do caso: 1 - Confirmado, 2 - Descartado |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte: 1 - Laboratorial, 2 - Vínculo Epidemiológico, 3 - Clínico |
| `DOENCA_TRA` | Inteiro | Doença relacionada ao trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `EVOLUCAO` | Inteiro | Evolução do caso: 1 - Cura, 2 - Óbito por coqueluche, 3 - Óbito por outras causas, 9 - Ignorado |
| `DT_OBITO` / `DT_ENCERRA` | Data (`AAAAMMDD`) | Data do óbito e de encerramento do caso |

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
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora. co_unidade_notifi cacao | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico. dt_diagnostico_si ntoma | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno). ds_semana_sinto ma | — | todos |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência. co_municipio_res idencia | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil). co_pais_residenc ia | — | todos |
| `nduplic_n` | `NDUPLIC_N` | texto | Não Listar/ Não Contar. 0 ou branco – Não identificado 1 – Não é duplicidade (não listar) 2 – Duplicidade (não contar) | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal. nu_lote_horizont al | — | todos |
| `cs_flxret` | `CS_FLXRET` | texto | Fluxo de retorno. Identifica se o registro está habilitado ou foi enviado pelo fluxo de retorno para o município de residência | 0 - Não 1 - habilitado para envio. 2 - enviado | todos |
| `flxrecebi` | `FLXRECEBI` | texto | Recebida por fluxo de retorno (campo interno). Colocar a estrutura do nº atribuído pelo sistema | — | todos |
| `migrado_w` | `MIGRADO_W` | texto | Identifica migração (campo interno). Identifica se o registro é oriundo da rotina de migração da base Windows | 1- migrado do Sinan Windows | todos |
| `dt_invest` | `DT_INVEST` | data | Data da investigação. Data completa do inicio da investigação iniciada (Data da primeira ação desenvolvida após o conhecimento do caso) | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Exportar o código da CBO e não o código sequencial | — | todos |
| `ant_sentin` | `ANT_SENTIN` | texto | A Unidade Notificante É Sentinela?. Informa se a unidade de saúde que notificou o caso é considerada sentinela | 1- Sim 2- Não 9 - Ignorado | todos |
| `fc_contato` | `FC_CONTATO` | texto | Contato Com Caso Suspeito Ou Confirmado De Coqueluche (Até 14 Dias Antes Do Início Dos Sinais E Sintomas). Local em que o paciente teve contato com caso semelhante nos últimos 14 dias, anterior ao início dos Sintomas | 1. Domicílio 2. Vizinhança 3. Trabalho 4. Creche/escola 5. Posto de saúde/hospital 6. Outro Estado/ Município 7. Outro 8. Sem história de contato 9. Ignorado | todos |
| `out_contat` | `OUT_CONTAT` | texto | Se Outro Contato, Especificar. Outro local de contato além dos referidos no campo LO_CONTATO | — | todos |
| `cs_vac_n` | `CS_VAC_N` | texto | N º de doses de vacina tríplice (dpt) ou tetravalente (dtp + hib). Número de doses da vacina que o paciente recebeu. (informação em cartão de vacina) | 1. Uma 2. Duas 3. Três 4. Três + 1 Reforço 5. Três + 2 Reforços 6. Nunca Vacinado 9. Ignorado | todos |
| `dt_ult_dos` | `DT_ULT_DOS` | data | Data Da Ultima Dose. Data da última dose da vacina tríplice (DTP) que o paciente recebeu. Não deve ser menor ou igual a data de nascimento | — | todos |
| `dt_catarra` | `DT_CATARRA` | data | Data do Inicio da Tosse. Data do início da tosse. Essa data deverá ser inferior a 14 dias a data de notificação | — | todos |
| `cs_tosse_e` | `CS_TOSSE_E` | texto | Sinais e Sintomas (Tosse). Informa se o paciente apresentou tosse | 1- Sim 2- Não 9 - Ignorado | todos |
| `cs_tosse_p` | `CS_TOSSE_P` | texto | Sinais e Sintomas (Tosse Paroxística). Informa se o paciente apresentou tosse paroxísitica(tosse súbita incontrolável com tossidas rápidas e curtas(5 a 10) em uma única expiração | 1- Sim 2- Não 9 - Ignorado | todos |
| `cs_crise` | `CS_CRISE` | texto | Sinais e Sintomas Respiração Ruidosa Ao Final Da Crise De Tosse (Guincho). Informa se o paciente apresentou respiração ruidosa ao final da crise de tosse (guincho) | 1- Sim 2- Não 9 - Ignorado | todos |
| `cs_cianose` | `CS_CIANOSE` | texto | Sinais e Sintomas (Cianose). Informa se o paciente apresentou Cianose | 1- Sim 2- Não 9 - Ignorado | todos |
| `cs_vomitos` | `CS_VOMITOS` | texto | SinaiseE Sintomas (Vômitos). Informa se o paciente apresentou vômitos pós- tosse | 1- Sim 2- Não 9 - Ignorado | todos |
| `cs_apneia` | `CS_APNEIA` | texto | Sinais e Sintomas (Apnéia). Informa se o paciente apresentou Apnéia | 1- Sim 2- Não 9 - Ignorado | todos |
| `cs_temp37` | `CS_TEMP37` | texto | Sinais e Sintomas (Temperatura < 38ºc). st_sinais_temperatura_menor _38 | 1- Sim 2- Não 9 - Ignorado | todos |
| `cs_temp_38` | `CS_TEMP_38` | texto | Sinais e Sintomas (Temperatura > Ou = 38ºc). st_sinais_temperatura_maior_ 38 | 1- Sim 2- Não 9 - Ignorado | todos |
| `cs_out_sin` | `CS_OUT_SIN` | texto | Sinais e Sintomas (Outros). Informa se o paciente apresentou outros sintomas que não os descritos anteriormente | 1- Sim 2- Não 9 - Ignorado | todos |
| `nm_out_sin` | `NM_OUT_SIN` | texto | Outros Sinais e Sintomas (Especificar). descreve outro sinal ou sintoma não referido nos campos anteriores | — | todos |
| `cs_pneumon` | `CS_PNEUMON` | texto | Complicações (penumonia ou broncopneumonia). Informa se o paciente apresentou Pneumonia ou Broncopneumonia | 1. Sim 2. Não 9. Ignorado | todos |
| `cs_encefal` | `CS_ENCEFAL` | texto | Complicações (Encefalopatia (Convulsões)). Informa se o paciente apresentou Encefalopatia (convulsões) | 1. Sim 2. Não 9. Ignorado | todos |
| `cs_desitra` | `CS_DESITRA` | texto | Complicações (Desidratação). Informa se o paciente apresentou Desidratação | 1. Sim 2. Não 9. Ignorado | todos |
| `cs_otite` | `CS_OTITE` | texto | Complicações (Otite). Informa se o paciente apresentou Otite | 1. Sim 2. Não 9. Ignorado | todos |
| `cs_desnutr` | `CS_DESNUTR` | texto | Complicações (Desnutrição). Informa se o paciente apresentou Desnutrição | 1. Sim 2. Não 9. Ignorado | todos |
| `cs_out_com` | `CS_OUT_COM` | texto | Complicações (Outras). Informa se o paciente apresentou outras complicações que não as listadas anteriormente | 1. Sim 2. Não 9. Ignorado | todos |
| `nm_out_com` | `NM_OUT_COM` | texto | Outras Complicações (Especificar). Especifica outras complicações, além das referidas | — | todos |
| `cs_hospita` | `CS_HOSPITA` | texto | Ocorreu Hospitalização. Informa se o paciente foi hospitalizado | 1- Sim 2- Não 9 - Ignorado | todos |
| `dt_interna` | `DT_INTERNA` | data | Data Da Internação. data de internação, caso tenha ocorrido | — | todos |
| `cod_uf_hos` | `COD_UF_HOS` | texto | Uf. sigla da UF onde o paciente foi internado | — | todos |
| `cod_mun_ho` | `COD_MUN_HO` | texto | Município Do Hospital. Códigos dos municípios do IBGE | — | todos |
| `cs_antibio` | `CS_ANTIBIO` | texto | Utilizou Antibiótico. Informa se o paciente fez uso de Antibióticos/antimicrobian os no tratamento | 1. Sim 2. Não 9. Ignorado | todos |
| `dt_adm_ant` | `DT_ADM_ANT` | data | Data De Adm. Do Antibiótico. Data da administração do antibiótico/antimicrobiano | — | todos |
| `cs_coleta` | `CS_COLETA` | texto | Coleta De Material Da Nasofaringe. Informa se foi realizada a coleta de material da nasofaringe | 1. Sim 2. Não 9. Ignorado | todos |
| `dt_coleta` | `DT_COLETA` | data | Data Da Coleta Do Material. Data da coleta do material da nasofaringe | — | todos |
| `cs_cultura` | `CS_CULTURA` | texto | Resultado Da Cultura. resultado da cultura do material da nasofaringe(Bordetella pertussis) | 1. Positiva 2. Negativa 3. Não realizada 9. Ignorado | todos |
| `med_iden_c` | `MED_IDEN_C` | texto | Realizada Identificação Dos Comunicantes Íntimos. Informar se foram identificados comunicantes íntimos (os comunicantes podem ser identificados na residência, creche, escola, orfanatos, quartéis e outros locais que possibilitam o contato íntimo com o caso) | 1- Sim 2- Não 9. Ignorado | todos |
| `med_quan_c` | `MED_QUAN_C` | inteiro | Se Sim, Quantos?. Número de comunicantes íntimos | — | todos |
| `med_caso_s` | `MED_CASO_S` | texto | Quantos Casos Secundários Foram Confirmados Entre Os. Nº de casos secundários identificados entre os comunicantes | 0. Nenhum 1. Um 2. Dois ou mais | todos |
| `colet_comu` | `COLET_COMU` | texto | Realizada Coleta de Material da Nasofaringe dos Comunicantes. st_coleta_material_comunican te | 1. Sim 2. Não 9. Ignorado | todos |
| `quan_comun` | `QUAN_COMUN` | inteiro | Se Sim, em Quantos?. número de comunicantes em que foi coletado o material | — | todos |
| `quan_posit` | `QUAN_POSIT` | inteiro | Em Quantos Comunicantes o Resultado da Cultura Foi Positivo?. número de comunicantes com resultado da cultura positivo | — | todos |
| `med_bloque` | `MED_BLOQUE` | texto | Medidas de Prevenção/ Controle. Informa se foi realizado bloqueio e qual tipo do bloqueio | 1. Bloqueio vacinal 2. Quimioprofilaxi a 3. Ambos 4. Não 9. Ignorado | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação Final. Classificação final do caso | 1. Confirmado 2. Descartado | todos |
| `criterio` | `CRITERIO` | texto | Critério de Confirmação/Descarte. critério utilizado para confirmação do caso ou descarte do suspeito | 1. Laboratorial 2. Vínculo Epidemiológico | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença Relacionada ao Trabalho. varchar(1) st_doenca_tra balho TB_NOTIFIC ACAO | 1. Sim 2. Não 9. Ignorado | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução. Evolução do caso | 1. Cura 2. Óbito por coqueluche 3. Óbito por outras causas 9.Ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do Óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do Encerramento. Data do encerramento do caso | — | todos |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-coqu`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 17, inteiro: 4, nulo (vazio nas amostras): 1, texto: 63.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-coqu.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- a classificação final segue o vocabulário do dicionário revisado em fevereiro/2012 (confirmado/descartado, com critérios laboratorial, vínculo epidemiológico e clínico); o período catarral (`DT_CATARRA`) pode anteceder `DT_SIN_PRI` e sustenta a janela de 14 dias usada na investigação de contatos; o histórico vacinal (`CS_VAC_N`) exige cuidado com os códigos de reforços (três doses + um ou dois reforços) e nunca vacinado; e o campo `ANT_SENTIN` identifica casos notificados em unidades-sentinela do agravo, com as bases de 2023 a 2026 disponibilizadas apenas em `PRELIM`. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-coqu/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-coqu
quantilica datasus list sinan-coqu

# 2. Baixar microdados de sinan-coqu com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-coqu -o ./data --start 2007 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-coqu -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-coqu -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc(
    "data/sinan-coqu/2025/sinan-coqu_preliminar_2025-br@20261007.dbc", clean=True
)

# Casos confirmados por critério de confirmação e evolução do caso
conf = qdf.filter(pl.col("classi_fin") == 1).group_by("criterio").len().sort("criterio")
print(conf)

# Hospitalização e complicações (pneumonia) nos casos confirmados
hosp = (
    qdf.filter((pl.col("classi_fin") == 1) & (pl.col("cs_hospita") == 1))
    .group_by("cs_pneumon")
    .len()
    .sort("cs_pneumon")
)
print(hosp)
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Coqueluche (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de coqueluche e situações de óbitos em lactentes (vigilância intensificada)
