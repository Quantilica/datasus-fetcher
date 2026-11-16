---
dataset:
  id: sinan-dift
  fonte: datasus
  titulo: Difteria
  resumo: 'Difteria do DATASUS: uma ficha de notificação/investigação de difteria.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de difteria
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 93
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_temper: 'número inteiro: contagem ou código numérico (ver Descrição)'
    med_quan_c: 'número inteiro: contagem ou código numérico (ver Descrição)'
    med_quan_m: 'número inteiro: contagem ou código numérico (ver Descrição)'
    med_quan_p: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Difteria (`sinan-dift`)

## Resumo

O `sinan-dift` contém os microdados das notificações e investigações epidemiológicas de casos de Difteria (CID-10 A36) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de difteria, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. É uma base de baixa incidência (difteria é agravo raro no Brasil, com registros individuais habitualmente associados a inquéritos e surtos), mas com leiaute detalhado (92 colunas na v5.0) que registra a pseudo-membrana, complicações (faringe, laringe, cordae, miocardite, nefrite, paralisias), o tratamento com soro antitoxina e antibiótico, a síntese de contato e a investigação vacinal.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `DIFT` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `DIFT` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `DIFTBR25.dbc` — `DIFT` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As consolidações até 2023 estão em `FINAIS` e os anos de 2024 a 2026 estão apenas em `PRELIM` (ex.: `DIFTBR26.dbc`, atualização de 07/10/2026).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-dift/<AAAA>/sinan-dift_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-dift/2024/sinan-dift_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

A difteria é agravo de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, atualmente constando da Lista Nacional de Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) em articulação com o GT-SINAN, a rede laboratorial de referência para o diagnóstico de *Corynebacterium diphtheriae* e o Programa Nacional de Imunizações, cuja cobertura vacinal (vacina tríplice bacteriana/D3 e D3a) é decisiva para manter a doença em níveis raros. Com poucos casos esperados por ano, a base serve à investigação de casos individualizados, à identificação de bolsões de cobertura vacinal insuficiente e à resposta rápida a surtos localizados.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Difteria** do SINAN. A notificação nasce com a suspeição clínica (pseudo-membrana sogra nos pilares, amígdalas, palato, faringe ou laringe, acompanhada de edema cervical, prostração e febre) e é completada ao longo da investigação com o registro detalhado da topografia da pseudo-membrana, das complicações (miocardite, nefrite, paralisias bulbar/palatina/de membros e arritmias), do material clínico coletado e do tratamento (soro antitoxina e antibiótico, com datas `TRA_DATA_S`/`TRA_DATA_A`). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. Mudanças incrementais no dicionário (versão revisada em julho/2010) refletiram a organização das opções do critério de confirmação (cultura com provas de toxigenicidade, cultura sem prova de toxigenicidade, vínculo epidemiológico, morte pós-clínica compatível, clínico e necrópsia) e o registro do antibiótico terapêutico em rodapé (data de início com uso de responsabilidade clínica).

Aplicações analíticas típicas: manutenção da vigilância caso a caso (o volume é baixo); letalidade da difteria (`EVOLUCAO` 3/4 com `DT_OBITO`); proporção de casos com cobertura vacinal incompleta (`ANT_DOS_N`, `ANT_ULTI_D`) e tipo de contato do caso (`ANT_TIPOCO`); confirmação pela cultura com prova de toxigenicidade (`CRITERIO` = 1), o padrão-ouro laboratorial; e registro de sequelas (`EVOLUCAO` 1/2) e do manejo terapêutico (antitoxina/antibiótico).

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-10-29.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `DIFTBR25.dbc` (92 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE do município de notificação e de residência |
| `NU_LOTE_V`/`NU_LOTE_H` | String | Lote da transferência vertical (hierárquica) da investigação|
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `ID_OCUPA_N` | String (6) | Código CBO da ocupação do paciente |
| `ANT_TIPOCO` | Inteiro | Tipo de contato com caso de difteria (domiciliar, escolar, colega de trabalho, ignorado) |
| `ANT_DOS_N` / `ANT_ULTI_D` | Inteiro / Data | Nº de doses do esquema vacinal (D3/TD) e data da última dose |
| `CLI_EDEMAG`/`CLI_PESCOC`/`CLI_FEBRE`/`CLI_PROSTR`/`CLI_PSEUDO`/`CLI_PALIDE`/`CLI_TEMPER` | Inteiro | Sinais e sintomas: edema de pescoço ("pescoço de touro"), feb­re, prostração, pseudo-membrana, palidez e temperatura elevada |
| `CLI_CAVIDA`/`CLI_AMIGDA`/`CLI_CORDAO`/`CLI_FARING`/`CLI_LARING`/`CLI_ORGAOS`/`CLI_PALATO` | Inteiro | Localização da pseudomembrana: cavidade nasal, amigdalas, cordas vocais, faringe, laringe, outros órgãos, palato |
| `CLI_MIOCAR`/`CLI_NEFRIT`/`CLI_PARALB`/`CLI_PARALP`/`CLI_ARRITM`/`CLI_PARALM` | Inteiro | Complicações: miocardite, nefrite, paralisia bulbar, paralisia palatina, arritmias, paralisia de membros |
| `ATE_HOSPIT`/`ATE_INTERN` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |
| `LAB_MATE_N`/`LAB_DATA_C`/`LAB_CULTUR`/`LAB_PROVAS` | Inteiro/Data | Material coletado (swab), data da coleta, resultado da cultura e provas de toxigenicidade |
| `TRA_DATA_S` | Data | Data da aplicação de soro antitoxina difiteria |
| `TRA_ANTIBI`/`TRA_DATA_A` | Inteiro/Data | Antibiótico instituído e data da administração |
| `CLASSI_FIN` | Inteiro | Classificação final do caso: 1 - Confirmado, 2 - Descartado |
| `CRITERIO` | Inteiro | Critério de confirmação: 1 - Cultura com prova de toxigenicidade, 2 - Cultura sem prova de toxigenicidade, 3 - Vínculo epidemiológico, 4 - Morte pós clínica compatível, 5 - Clínico, 6 - Necrópsia |
| `EVOLUCAO` | Inteiro | Evolução do caso: 1 - Cura com sequela, 2 - Cura sem sequela, 3 - Óbito por difteria, 4 - Óbito por outras causas, 9 - Ignorado |
| `DT_OBITO` / `DT_ENCERRA` | Data (`AAAAMMDD`) | Data do óbito e de encerramento do caso |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

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
| `dt_invest` | `DT_INVEST` | data | Data da Investigação. Data em que ocorreu a investigação – informar a Data da 1ª ação desenvolvida após a notificação | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/ Ramo de Atividade Econômica. Atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O | — | todos |
| `ant_tipoco` | `ANT_TIPOCO` | texto | Contato Com Caso Suspeito ou Confirmado de Difteria (Até 14 Dias Antes do Início dos Sinais E Sintomas). Local em que o paciente teve contato com caso semelhante nas últimas 2 semanas, anterior ao início dos sinais e sintomas | 1. Domicílio 2. Vizinhança 3. Trabalho 4. Creche/escola 5. Posto de saúde/hospital 6. Outro Estado/Município 7. Outro 8. Sem história de contato 9. Ignorado | todos |
| `ant_outros` | `ANT_OUTROS` | texto | Se Outro contato (Especificar). Identificação de outro local em que o paciente teve contato não referido acima | — | todos |
| `ant_dos_n` | `ANT_DOS_N` | texto | N.º de Doses da Vacina Tríplice (DTP) ou Tetravalente (DTP+Hib). Número de doses da vacina tríplice (DPT) ou tetravalente | 1. Uma 2. Duas 3. Três | todos |
| `ant_ulti_d` | `ANT_ULTI_D` | data | Data da última dose. Informe a Data da última dose da vacina tríplice (DTP) ou dupla (DT ou dT) que o paciente recebeu | — | todos |
| `cli_edemag` | `CLI_EDEMAG` | texto | Sinais e Sintomas (Edema Ganglionar) | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_pescoc` | `CLI_PESCOC` | texto | Sinais e Sintomas (Edema de Pescoço). o | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_febre` | `CLI_FEBRE` | texto | Sinais e Sintomas (Febre). 1 Sim 2 Não 9. Ignorado | — | todos |
| `cli_prostr` | `CLI_PROSTR` | texto | Sinais e Sintomas (Prostração). Informa se o paciente apresentou prostração | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_pseudo` | `CLI_PSEUDO` | texto | Sinais e Sintomas (Pseudomembrana) | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_palide` | `CLI_PALIDE` | texto | Sinais e Sintomas (Palidez). Informa se o paciente apresentou palidez | 1. Sim 2. Não | todos |
| `cli_temper` | `CLI_TEMPER` | inteiro | Temperatura Corporal. Informa a temperatura corporal apresentada pelo paciente durante a fase inicial da doença, em graus centígrados | — | todos |
| `cli_cavida` | `CLI_CAVIDA` | texto | Localização da Pseudomembrana (Placas) (Cavidade Nasal) | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_amigda` | `CLI_AMIGDA` | texto | Localização da Pseudomembrana (Placas) (Amígdalas) | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_cordao` | `CLI_CORDAO` | texto | Localização da Pseudomembrana (Placas) Cordão Umbilical) | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_faring` | `CLI_FARING` | texto | Localização da Pseudomembrana (Placas) (Faringe) | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_laring` | `CLI_LARING` | texto | Localização da Pseudomembrana (Placas) (Laringe) | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_orgaos` | `CLI_ORGAOS` | texto | Localização da Pseudomembrana (Placas) (Órgãos Genitais) | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_palato` | `CLI_PALATO` | texto | Localização da. Informa se a | 1. Sim | todos |
| `cli_condut` | `CLI_CONDUT` | texto | Localização da Pseudomembrana (Placas) (Conduto Auditivo) | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_traque` | `CLI_TRAQUE` | texto | Localização da Pseudomembrana (Placas) (Traquéia) | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_pele` | `CLI_PELE` | texto | Localização da Pseudomembrana (Placas) (Pele). e | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_conjun` | `CLI_CONJUN` | texto | Localização da Pseudomembrana (Placas) (Conjuntiva) | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_miocar` | `CLI_MIOCAR` | texto | Complicações Existiram (Miocardite). e | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_nefrit` | `CLI_NEFRIT` | texto | Complicações Existiram (Nefrite). Informa se a complicação foi nefrite | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_paralb` | `CLI_PARALB` | texto | Complicações Existiram (Paralisia Bilateral e Simetrica das Extremidades). ) | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_paralp` | `CLI_PARALP` | texto | Complicações Existiram Paralisia do Palato. Informa se a complicação foi paralisia do palato | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_arritm` | `CLI_ARRITM` | texto | Complicações Existiram (Arritmias Cardíacas). Informa se a complicação foram arritmias cardíacas | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_paralm` | `CLI_PARALM` | texto | Complicações Existiram (Paralisia dos Músculos Intercostais e Diafragma). Informa se a complicação foi paralisia dos músculos intercostais e diafragma | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_outras` | `CLI_OUTRAS` | texto | Complicações Existiram (Outras). Informa se a complicação foram outras que não as especificadas acima | 1. Sim 2. Não 9. Ignorado | todos |
| `cli_especi` | `CLI_ESPECI` | texto | Outras Complicações Especificar. Especifica outro tipo de complicação além das referidas acima | — | todos |
| `ate_hospit` | `ATE_HOSPIT` | texto | Ocorreu Hospitalização. Informa se o paciente foi internado devido ao agravo que está sendo notificado | 1- Sim 2- Não 9 Ignorado | todos |
| `ate_intern` | `ATE_INTERN` | data | Data da Internação. Data de internação, caso tenha ocorrido | — | todos |
| `ate_uf_int` | `ATE_UF_INT` | texto | UF. Sigla da UF onde o paciente foi internado | — | todos |
| `ate_munici` | `ATE_MUNICI` | texto | Município do Hospital. Código e nome completo do município onde o paciente foi internado | — | todos |
| `lab_mate_n` | `LAB_MATE_N` | texto | Material Coletado. Informa se foi realizada coleta de material da orofaringe, nasofaringe e/ ou lesão de pele ou mucosa | 1-Orofaringe 2-Nasofaringe 3-Orofaringe e nasofaringe 4-Não coletado 9-Ignorado | todos |
| `lab_data_c` | `LAB_DATA_C` | data | Data da Coleta. Data em que foi colhido o material | — | todos |
| `lab_cultur` | `LAB_CULTUR` | texto | Cultura para Difteria. Resultado da cultura para C. diphteriae | 1. Positiva para C. diphteriae 2. Negativa para C. diphteriae 3. Não realizada 9. Ignorado | todos |
| `lab_provas` | `LAB_PROVAS` | texto | Provas de Toxigenicidade. resultado das provas de toxigenicidade | 1. Positiva 2. Negativa 3. Não realizada 9. Ignorado | todos |
| `tra_data_s` | `TRA_DATA_S` | data | Data da Aplicação do Soro. data de aplicação do soro | — | todos |
| `tra_antibi` | `TRA_ANTIBI` | texto | Antibiótico. Informa se o paciente foi tratado com antibiótico | 1. Sim 2. Não 9. Ignorado | todos |
| `tra_data_a` | `TRA_DATA_A` | data | Data da Adm. do Antibiótico. Data de início da administração do antibiótico utilizado no tratamento | — | todos |
| `med_iden_c` | `MED_IDEN_C` | texto | Realizada Identificação dos Comunicantes Íntimos. Informa se foi realizada identificação dos comunicantes íntimos(os comunicantes podem ser identificados na residência, creche, escola, orfanatos, quartéis e outros locais que possibilitam o contato íntimo com o caso) | 1. Sim 2. Não 9. Ignorado | todos |
| `med_quan_c` | `MED_QUAN_C` | inteiro | Se Sim, Quantos?. número de comunicantes íntimos identificados | — | todos |
| `med_caso_s` | `MED_CASO_S` | texto | Quantos casos secundários foram confirmados entre os comunicantes | 1. Nenhum 2. Um 3. Dois ou mais 9. Ignorado | todos |
| `med_materi` | `MED_MATERI` | texto | Realizada Coleta de Material dos Comunicantes. Informa se foi realizada coleta de material de comunicantes | 1-Sim 2-Não 9.Ignorado | todos |
| `med_quan_m` | `MED_QUAN_M` | inteiro | Se Sim, Em Quantos?. ) | — | todos |
| `med_quan_p` | `MED_QUAN_P` | inteiro | Quantos portadores foram Identificados entre os comunicantes?. Nº de portadores identificados entre os comunicantes | — | todos |
| `med_preven` | `MED_PREVEN` | texto | Medidas de Prevenção/ Controle. Informa o tipo de bloqueio realizado | 1. Bloqueio vacinal 2. Quimioprofilaxia 3. Ambos 4. Não 9. Ignorado | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação Final. Classificação final da notificação | 1. Confirmado 2. Descartado | todos |
| `criterio` | `CRITERIO` | texto | Critério de Confirmação/Descarte. Critérios de confirmação do caso | 1. Cultura com prova de toxigenicidade 2. Cultura sem prova de toxigenicidade 3. Vínculo epidemiológico 4. Morte pós clínica compatível 5. Clínico 6. Necrópsia | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença Relacionada ao Trabalho. Informa se o paciente adquiriu a doença em decorrência das condições/situação de trabalho | 1. Sim 2. Não 9. Ignorado | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução. Evolução do paciente | 1. Cura c/ sequela | todos |
| `dt_obito` | `DT_OBITO` | data | Data do Óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do Encerramento. Data do encerramento da investigação do caso | — | todos |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-dift`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 17, inteiro: 5, texto: 71.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-dift.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- a base tem poucos casos por ano (doença rara na era pós-vacinal), de modo que tabelas agregadas simples tendem a ser esparsas; os dois critérios de cultura (com/sem prova de toxigenicidade) marcam a diferença entre confirmação definitiva (`CRITERIO` = 1) e isolamento sem prova da toxigenicidade (`CRITERIO` = 2); a evolução com/sem sequela (`EVOLUCAO` = 1/2) requer mapeamento antes de qualquer tabulação; e a série de 2024 a 2026 está apenas em `PRELIM`, com casos ainda passíveis de revisão. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-dift").glob("**/*.parquet"))
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
datasus-fetcher list sinan-dift

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-dift -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-dift
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Difteria (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de difteria; Norma de Manejo e tratamento da difteria (MS)
