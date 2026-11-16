---
dataset:
  id: sinan-hans
  fonte: datasus
  titulo: Hanseníase
  resumo: 'Hanseníase do DATASUS: uma ficha de notificação/investigação de hanseníase.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2001'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de hanseníase
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 65
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_lesoes: 'número inteiro: contagem ou código numérico (ver Descrição)'
    contreg: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nervosafet: 'número inteiro: contagem ou código numérico (ver Descrição)'
    dose_receb: 'número inteiro: contagem ou código numérico (ver Descrição)'
    contexam: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Hanseníase (`sinan-hans`)

## Resumo

O `sinan-hans` contém os microdados das notificações e investigações epidemiológicas de casos de Hanseníase/Doença de Hansen (CID-10 A30) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha de notificação/investigação (ou boletim de acompanhamento) de um caso de hanseníase, preenchida pelas unidades de saúde do SUS em todo o país a partir da avaliação dermatoneurológica do paciente. É a base oficial para dimensionamento da morbidade da hanseníase no país, com 64 campos da rotina v5.0 cobrindo desde forma clínica e classificação operacional até desfecho de alta (cura, transferência, óbito, abandono, erro diagnóstico) e contatos examinados.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `HANS` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `HANS` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `HANSBR23.dbc` — `HANS` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `23` é o ano de notificação (2023). As consolidações até 2023 estão em `FINAIS` e os anos de 2024 a 2026 estão apenas em `PRELIM` (ex.: `HANSBR26.dbc`, atualização de 29/09/2026).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-hans/<AAAA>/sinan-hans_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-hans/2024/sinan-hans_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

Hanseníase é doença infecciosa crônica de notificação compulsória desde o início da vigilância nacional brasileira (Lei nº 6.259/1975 e Decreto nº 78.231/1976) e, hoje, consta na Lista Nacional de Doenças e Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). O programa de controle é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), por meio do Departamento de Doenças de Condições Crônicas e Infecções Sexualmente Transmissíveis (DCCI), em articulação com o GT-SINAN. O Brasil concentra um dos maiores contingentes de casos novos do mundo; a base alimenta os indicadores oficiais de incidência por 100 mil habitantes, de prevalência (casos em tratamento), detecção em menores de 15 anos, grau de incapacidade física no diagnóstico e atuação dos serviços de referência em dermatologia sanitária.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Hanseníase** (ficha v5.0; o acompanhamento de casos já notificados ocorre por meio do boletim individual, o mesmo instrumento do Sinan Net). Cada notificação nasce quando o paciente é diagnosticado por exame dermatoneurológico (lesão ou placa cutânea com perda de sensibilidade, nervo periférico acometido e, quando indicado, baciloscopia intradérmica) e é completada ao longo da investigação e do acompanhamento com dados de classificação operacional (paucibacilar/multibacilar), esquema antileprótico (PQT/6 e PQT/MB/12 doses), doses supervisionadas, episódios reacionais, notificação do grau de incapacidade física no diagnóstico e no acompanhamento e desfecho da alta. A unidade de análise é o caso (paciente) registrado no SINAN — cada ficha é a unidade de notificação individual do agravo.

A série histórica registra três fases do sistema de informação: de **2001 a 2006** os dados provêm do Sinan-Windows (com campo `MIGRADO_W` distinguindo registros migrados); de **2007 em diante**, as bases provêm do Sinan Net com o Sinan Online (mesma base disseminada). Mudanças importantes do instrumento incluem a separação da notificação em **ficha de notificação** (diagnóstico) e o **boletim/transferência vertical** de acompanhamento em anos subsequentes, e a inclusão de campos administrativos das transferências (`UFATUAL`, `ID_MUNI_AT`, `DT_NOTI_AT`, `UFRESAT` para registrar a unidade responsável pelo acompanhamento atual do caso) e controles de vinculação de registros (`IN_VINCULA`, `NU_LOTE_IA`).

Aplicações analíticas típicas: incidência de casos novos e densidade de pacientes multibacilares; detecção de casos em menores de 15 anos (idade e fonte de infecção); distribuição de formas clínicas (indeterminada, tuberculóide, dimorfa, virchowiana) e da classificação operacional (PB/MB); percentual de casos com grau de incapacidade física (0, I, II) no diagnóstico e no acompanhamento; doses de poliquimioterapia supervisionada (`DOSE_RECEB`); frequência de episódios reacionais (`EPIS_RACIO`); proporções de cura, abandono e óbito (tipo de saída `TPALTA_N`); e cobertura de contatos registrados e examinados (`CONTREG`/`CONTEXAM`).

### Cobertura observada

- Índice do FTP (2026-10): 26 arquivos, de 2001 a 2026, 1 UF(s) com arquivos, última atualização em 2026-09-29.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2001 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `HANSBR23.dbc` (64 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_DIAG` | Data (`AAAAMMDD`) | Data do diagnóstico (base da abertura da ficha epidemiológica) |
| `SEM_DIAG` | Inteiro (`AAAASS`) | Semana epidemiológica do diagnóstico |
| `NU_IDADE_N` | Inteiro composto | Idade (o primeiro dígito indica a unidade: dia/mês/ano) |
| `CS_SEXO` | String (1) | Sexo do paciente (M/F/I - Ignorado) |
| `ID_MN_RESI` | String (6/7) | Código IBGE do município de residência (base de contagem) |
| `NU_LESOES` | Inteiro | Número de lesões cutâneas identificadas no exame dermatoneurológico |
| `FORMACLINI` | Inteiro | Forma clínica pela classificação de Madrid: 1 - Indeterminada, 2 - Tuberculóide, 3 - Dimorfa, 4 - Virchowiana, 5 - Não classificado |
| `AVALIA_N` | Inteiro | Grau de incapacidade física no diagnóstico: 0 - Grau zero, 1 - Grau I, 2 - Grau II, 3 - Não avaliado |
| `CLASSOPERA` | Inteiro | Classificação operacional: 1 - PB (Paucibacilar), 2 - MB (Multibacilar) |
| `MODOENTR` | Inteiro | Modo de entrada: caso novo, recorrentes/recidiva ou transferências entre unidades, municípios, estados e países |
| `MODODETECT` | Inteiro | Modo de detecção do caso (espontâneo, por encaminhamento, exame de contato/coletividade) |
| `BACILOSCOP` | Inteiro | Resultado da baciloscopia (positiva/negativa/não realizada) |
| `DTINICTRAT` | Data (`AAAAMMDD`) | Data de início do tratamento RS/PQT (base do indicador de cumprimento do esquema) |
| `ESQ_INI_N` / `ESQ_ATU_N` | Inteiro | Esquema terapêutico inicial e atual: PQT/PB (6 doses), PQT/MB (12 doses) ou outros esquemas substitutivos |
| `CONTREG` | Inteiro | Nº de contatos domiciliares registrados (residiram nos últimos 5 anos com o paciente) |
| `NERVOSAFET` | Inteiro | Número de nervos afetados no exame dermatoneurológico |
| `UFATUAL`/`ID_MUNI_AT`/`ID_UNID_AT` | String | Unidade federativa atual, município e unidade de saúde (CNES) responsáveis pelo acompanhamento atual do caso |
| `DT_NOTI_AT` | Data (`AAAAMMDD`) | Data da atualização da notificação (boletim de acompanhamento/transferência) |
| `DTULTCOMP` | Data (`AAAAMMDD`) | Data da última consulta/atendimento de acompanhamento |
| `CLASSATUAL` | Inteiro | Classificação operacional atual (PB/MB) no acompanhamento |
| `AVAL_ATU_N` | Inteiro | Avaliação do grau de incapacidade física no acompanhamento (0/I/II/não avaliado) |
| `DOSE_RECEB` | Inteiro | Número de doses supervisionadas já recebidas pelo paciente |
| `EPIS_RACIO` | Inteiro | Ocorrência de episódios reacionais durante o acompanhamento |
| `DTMUDESQ` | Data (`AAAAMMDD`) | Data de mudança do esquema terapêutico (se pertinente) |
| `CONTEXAM` | Inteiro | Número de contatos examinados (sempre ≤ contatos registrados) |
| `DTALTA_N` | Data (`AAAAMMDD`) | Data da alta (encerramento do caso) |
| `TPALTA_N` | Inteiro | Tipo de saída/alta: 1 - Cura, 2 - Transferência para o mesmo município, 3 - Transferência para outro município, 4 - Transferência para outro estado, 5 - Transferência para outro país, 6 - Óbito, 7 - Abandono, 8 - Erro diagnóstico |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_diag` | `DT_DIAG` | data | Data dos primeiros sintomas / Diagnóstico. Data dos primeiros sintomas do caso de agravo agudo. Data do diagnóstico do caso de agravo crônico e DRTs Data do acidente nos acidentes da saúde do trabalhador | — | todos |
| `sem_diag` | `SEM_DIAG` | texto | Semana epidemiológica dos primeiros sintomas/ diagnósticos. (campo interno). Semanas do calendário epidemiológico padronizado | — | todos |
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
| `migrado_w` | `MIGRADO_W` | texto | Identifica migração (campo interno). Identifica se o registro é oriundo da rotina de migração da base Windows | 11- migrado do Sinan Windows | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Categorias da classificação brasileira de ocupações (CBO) | — | todos |
| `nu_lesoes` | `NU_LESOES` | inteiro | Nº de lesões cutâneas. Número de lesões dermatológicas apresentadas pelo paciente por ocasião do diagnóstico | — | todos |
| `formaclini` | `FORMACLINI` | texto | Forma Clínica. Forma clínica inicial por ocasião do diagnóstico, segundo classificação de Madrid | 1- I -Indeterminada 2- T - Tuberculóide 3- D - Dimorfa 4- V - Virchowiana 5- Não classificado | todos |
| `avalia_n` | `AVALIA_N` | texto | Avaliação do Grau de Incapacidade Física no Diagnóstico | — | todos |
| `classopera` | `CLASSOPERA` | texto | Classificação Operacional | 1- PB - Paucibacilar 2- MB - Multibacilar | todos |
| `modoentr` | `MODOENTR` | texto | Modo de entrada. Modo de entrada do paciente no sistema | 1- Caso novo 2- Transferencia do mesmo município (outra unidade) 3- Transferência de outro município (mesma UF) 4- Transferência de outro estado 5- Transferencia de outro país 6- Recidiva 7- Outros reingressos 9- Igno... | todos |
| `mododetect` | `MODODETECT` | texto | Modo de detecção de caso novo. Modo de detecção do caso novo | 1- Encaminhamento 2- Demanda espontânea 3- Exame de coletividade 4- Exame de contatos 5- Outros modos 9- Ignorado | todos |
| `baciloscop` | `BACILOSCOP` | texto | Resultado da baciloscopia (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dtinictrat` | `DTINICTRAT` | data | Data do início do tratamento. Data do inicio do tratamento | — | todos |
| `esq_ini_n` | `ESQ_INI_N` | texto | Esquema terapêutico inicial | 1. PQT/ PB/ 6 doses 2. PQT/ MB/ 12 doses 3. Outros Esquemas Substitutos | todos |
| `contreg` | `CONTREG` | inteiro | Nº de contatos registrados | — | todos |
| `nervosafet` | `NERVOSAFET` | inteiro | Nº de nervos afetados. Número de nervos afetados | — | todos |
| `ufatual` | `UFATUAL` | texto | UF de atendimento atual. Código da UF do cadastro do IBGE | — | todos |
| `id_muni_at` | `ID_MUNI_AT` | texto | Município de atendimento atual. Código e nome dos municípios do cadastro do IBGE | — | todos |
| `dt_noti_at` | `DT_NOTI_AT` | data | Data de notificação atual. Data de notificação do caso pela unidade de saúde responsável pelo tratamento atual do caso | — | todos |
| `id_unid_at` | `ID_UNID_AT` | texto | Unidade de atendimento atual. Códigos e nomes de estabelecimentos de saúde (CNES) | — | todos |
| `ufresat` | `UFRESAT` | texto | UF de residência atual (*) | — | todos |
| `muniresat` | `MUNIRESAT` | texto | Município de residência atual (*). encia_atual | — | todos |
| `dtultcomp` | `DTULTCOMP` | data | Data do último comparecimento | — | todos |
| `classatual` | `CLASSATUAL` | texto | Classificação operacional atual. ao_atual | 1. PB (Paucibacilar) 2. MB (Multibacilar) | todos |
| `aval_atu_n` | `AVAL_ATU_N` | texto | Avaliação de incapacidade física no momento da cura. ica_cura | 0. grau zero 1. grau I 2. grau II 3. Não avaliado 9- Ignorado | todos |
| `esq_atu_n` | `ESQ_ATU_N` | texto | Esquema terapêutico atual. utico_atual | 1- PQT/PB/06 doses 2- PQT/MB/12 doses 3- Outros Esquemas Substitutivos | todos |
| `dose_receb` | `DOSE_RECEB` | inteiro | Número de doses supervisionadas. Número de doses supervisionadas recebidas sob supervisão | — | todos |
| `epis_racio` | `EPIS_RACIO` | texto | Episódio Reacional Durante o Tratamento | 1- Reação tipo 1 2- Reação tipo 2 3- Reação tipo 1 e 2 | todos |
| `dtmudesq` | `DTMUDESQ` | data | Data de mudança do Esquema | — | todos |
| `contexam` | `CONTEXAM` | inteiro | Número de contatos examinados | — | todos |
| `dtalta_n` | `DTALTA_N` | data | Data da alta | — | todos |
| `tpalta_n` | `TPALTA_N` | texto | Tipo de alta (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `in_vincula` | `IN_VINCULA` | texto | Vinculação. Indica se a notificação foi vinculada | 0 - Não Vinculada 1 - Vinculada | todos |
| `nu_lote_ia` | `NU_LOTE_IA` | texto | Transferência vertical da investigação e do acompanhamento. Identifica o Lote da transferência da investigação e do acompanhamento de um nível do sistema para outro (transferência vertical) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-hans`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 14, inteiro: 6, texto: 45.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-hans.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- a hanseníase cobre tanto **fichas de notificação** quanto **boletins de acompanhamento** de casos transferidos entre municípios/unidades — um caso pode aparecer mais de uma vez seguido de atualizações (`UFATUAL`, `DT_NOTI_AT`), exigindo deduplicação por caso antes de indicadores agregados; contar casos novos exige filtrar `MODOENTR` = 1 (Caso novo); o inventário de bases muda entre `FINAIS` (2001 a 2023) e `PRELIM` (2024 a 2026); a idade em `NU_IDADE_N` requer decomposição do primeiro dígito; e o campo `IN_VINCULA` marca notificações vinculadas pelo sistema a outras fichas (hanseníase/tuberculose). (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-hans").glob("**/*.parquet"))
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
datasus-fetcher list sinan-hans

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-hans -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-hans
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Hanseníase (ficha, dicionário e boletim de acompanhamento v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de hanseníase e Diretrizes para vigilância, atenção e eliminação da hanseníase
