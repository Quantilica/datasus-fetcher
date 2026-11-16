---
dataset:
  id: sinan-iexo
  fonte: datasus
  titulo: Intoxicação Exógena
  resumo: 'Intoxicação Exógena do DATASUS: uma ficha de notificação/investigação de intoxicação Exógena.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2006'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de intoxicação Exógena
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 85
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    coagtoxma1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    coagtoxma2: 'número inteiro: contagem ou código numérico (ver Descrição)'
    coagtoxma3: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: dt_nasc
    categoria: data de nascimento
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Intoxicação Exógena (`sinan-iexo`)

## Resumo

Notificações de intoxicações exógenas por agentes químicos, medicamentos, drogas de abuso, metais, agrotóxicos e outros, registradas no SINAN. Cada linha representa uma ficha de investigação de um caso de intoxicação por substância exógena, incluindo exposições ocupacionais, acidentais e intencionais.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM, 2023–2026; Finais até 2022)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `IEXO` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `IEXO` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `IEXOBR24.dbc`, em que `IEXO` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024, preliminar).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-iexo/<AAAA>/sinan-iexo_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-iexo/2024/sinan-iexo_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`, `Nota_Tecnica_Intoxicacao_Exogena.pdf` (nota técnica específica do agravo).
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`DRT Intoxicação Exógena` / IEXO) é distribuído no Portal SINAN; a nota técnica no FTP complementa as orientações de preenchimento.

## Conteúdo

A intoxicação exógena é agravo de notificação compulsória na Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V; Portaria GM/MS nº 217/2023), sob a coordenação da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS). Quando relacionada ao trabalho, integra também a lista de Doenças e Agravos Relacionados ao Trabalho (DART), sendo de investigação obrigatória pelos CEREST/RENAST; a notificação ocupacional decorre da Portaria MS nº 777/2004.

O evento gerador é todo quadro de intoxicação resultante da exposição a substâncias químicas (medicamentos, agrotóxicos, metais, solventes, produtos de limpeza, drogas de abuso, substâncias usadas como arma química e outras), com CID-10 T36–T65 (destacando-se T65.9). A exposição pode ser aguda ou crônica e ocupacional ou não ocupacional. A unidade de análise é o caso notificado (um registro por ficha), com ocupação (CBO) e identificação da fonte de exposição.

O instrumento é a *Ficha de Investigação — Intoxicação Exógena*, que registra o grupo do agente tóxico, o princípio ativo, a via de exposição, a circunstância (habitual, ocupacional, acidental, intencional/suicida, uso de medicamento, abuso de drogas, ignorada), a classificação final (intoxicação confirmada, só exposição, reação adversa, surto), o critério de confirmação e a evolução (cura, óbito por intoxicação, óbito por outras causas, sequela). A série no FTP inicia em 2006; os dados de 2023 em diante estão em PRELIM e sujeitos a revisão.

Principais usos: vigilância de intoxicações ocupacionais por ramo (CNAE) e ocupação (CBO), monitoramento de agrotóxicos e de acidentes com produtos químicos, análise de tentativas de autoextermínio, vigilância de surtos e embasamento de ações de VISAT e de regulação de produtos.

### Cobertura observada

- Índice do FTP (2026-10): 21 arquivos, de 2006 a 2026, 1 UF(s) com arquivos, última atualização em 2026-10-29.
- Conversão local de amostras (4 arquivo(s) Parquet, de 2006 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo `IEXOBR07.dbc` (leiaute do SINAN Net; fichas e leiautes podem variar entre anos, por isso a lista reflete esse arquivo). Os arquivos públicos não trazem identificadores individuais como número da notificação (`NU_NOTIFIC`) nem data de nascimento completa. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (registro da ficha de notificação individual). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado. |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | String | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE). |
| `ID_UNIDADE` | String | Código CNES da unidade de saúde notificadora (7 dígitos). |
| `DT_SIN_PRI` | Data (AAAAMMDD) | Data dos primeiros sintomas. |
| `SEM_PRI` | String | Semana epidemiológica dos primeiros sintomas (AAAASS). |
| `ANO_NASC` | String | Ano de nascimento (o arquivo público não traz a data de nascimento completa). |
| `NU_IDADE_N` | Inteiro | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade. |
| `SG_UF` | String | UF de residência (código IBGE de 2 dígitos). |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `DT_INVEST` | Data (AAAAMMDD) | Data da investigação. |
| `ID_OCUPA_N` | String | Ocupação do trabalhador (CBO 2002, 6 dígitos). |
| `SIT_TRAB` | String | Situação no mercado de trabalho. |
| `LOC_EXPO` | String | Local de ocorrência da exposição (descrição de outros em `LOC_EXP_DE`). |
| `CNAE` | String | Atividade econômica da empresa contratante (CNAE). |
| `PAIS_EXP` | String | País de ocorrência da exposição. |
| `AGENTE_TOX` | String | Classificação do agente tóxico (grupo). |
| `COAGTOXMA1` | Inteiro | Código do agente tóxico (1º) segundo a tabela de agentes tóxicos. |
| `COAGTOXMA2` | Inteiro | Código do agente tóxico (2º). |
| `COAGTOXMA3` | Inteiro | Código do agente tóxico (3º). |
| `AGENTE_1` | String | Nome do agente tóxico (1º; texto livre). |
| `AGENTE_2` | String | Nome do agente tóxico (2º; texto livre). |
| `AGENTE_3` | String | Nome do agente tóxico (3º; texto livre). |
| `P_ATIVO_1` | String | Princípio ativo (1º; texto livre). |
| `P_ATIVO_2` | String | Princípio ativo (2º; texto livre). |
| `P_ATIVO_3` | String | Princípio ativo (3º; texto livre). |
| `UTILIZACAO` | String | Utilização do agente (descrição em `UTIL_DESC`). |
| `ATIVIDA_1` | String | Atividade relacionada à exposição (1ª). |
| `ATIVIDA_2` | String | Atividade relacionada à exposição (2ª). |
| `ATIVIDA_3` | String | Atividade relacionada à exposição (3ª). |
| `VIA_1` | String | Via de exposição (1ª). |
| `VIA_2` | String | Via de exposição (2ª). |
| `VIA_3` | String | Via de exposição (3ª). |
| `CIRCUNSTAN` | String | Circunstância da exposição/intoxicação (descrição de outras em `CIRCUN_DES`). |
| `DOENCA_TRA` | String | Doença relacionada ao trabalho. |
| `TPEXP` | String | Tipo de exposição (aguda, crônica etc.). |
| `TPATENDE` | String | Tipo de atendimento. |
| `HOSPITAL` | String | Hospitalização (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `DTINTERNA` | Data (AAAAMMDD) | Data da internação. |
| `UF_HOSP` | String | UF do hospital. |
| `MUN_HOSP` | String | Município do hospital. |
| `CLASSI_FIN` | String | Classificação final do caso. |
| `DIAG_CONF` | String | Diagnóstico confirmado (CID-10). |
| `CRITERIO` | String | Critério de confirmação. |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito, quando aplicável. |
| `CAT` | String | Foi emitida a Comunicação de Acidente do Trabalho (CAT)? |
| `DT_ENCERRA` | Data (AAAAMMDD) | Data de encerramento da investigação. |
| `LAVOURA` | String | Tipo de lavoura (texto livre). |
| `INTOX_CHUM` | String | Intoxicação por chumbo (marcação). |
| `INTOX_MERC` | String | Intoxicação por mercúrio (marcação). |
| `INTOX_META` | String | Intoxicação por outro metal (marcação). |

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
| `dt_nasc` | `DT_NASC` | data | Data de nascimento. Data de nascimento do paciente | — | só em 2006 |
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
| `dt_invest` | `DT_INVEST` | data | Data da investigação. Informar a data de investigação do caso | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação (c.b.o) | — | todos |
| `sit_trab` | `SIT_TRAB` | texto | trabalho. carteira assinada 02.Empregado não registrado 03.Autonomo/conta própria 04. Servidor público estatutário 05. Servidor públlico celetista 06. Aposentado 07. Desempregado 08. Trabalho temporário 09. Cooperativado 10. Trabalhador avulso 11. Empregador 12 Outro 99. Ignorado | — | todos |
| `loc_expo` | `LOC_EXPO` | texto | Local de ocorrência da exposição. Informar o local de ocorrência da exposição | 1. Residência 2. Ambiente de Trabalho 3. Trajeto do trabalho 4. Serviços de saúde 5. Escola/creche 6. Ambiente Externo 7. Outro 9 Ignorado | todos |
| `cnae` | `CNAE` | texto | Código da atividade econômica (cnae). Informar o nome do local/estabelecimento de ocorrência do acidente/exposição | — | todos |
| `uf_emp` | `UF_EMP` | texto | UF. Informar a UF de ocorrência o acidente/exposição | — | todos |
| `mun_emp` | `MUN_EMP` | texto | Município do estabelecimento | — | todos |
| `pais_exp` | `PAIS_EXP` | texto | País (se estabelecimento fora do Brasil). Informar o País se estabelecimento fora do Brasil | — | todos |
| `agente_tox` | `AGENTE_TOX` | texto | Grupo do agente tóxico / classificação geral. 01 Medicamento 02 Agrotóxico/uso agrícola 03 Agrotóxico/uso doméstico 04 Agrotóxico/uso saúde pública 05 Raticida 06 Produto Veterinário 07 Produto de uso domiciliar 08 Cosmético / higiene pessoal 09 Produto químico de uso industrial 10 Metal 11 Drogas de abuso 12 Planta tóxica 13 Alimento e bebida 14 Outro 99 Ignorado | — | todos |
| `coagtoxma1` | `COAGTOXMA1` | inteiro | Agente tóxico (código) 1. _1 | — | todos |
| `coagtoxma2` | `COAGTOXMA2` | inteiro | Agente tóxico (código) 2. _1 | — | todos |
| `coagtoxma3` | `COAGTOXMA3` | inteiro | Agente tóxico (código) 3. _1 | — | todos |
| `agente_1` | `AGENTE_1` | texto | Agente tóxico (nome comercial / popular) 1. _1 | — | todos |
| `agente_2` | `AGENTE_2` | texto | Agente tóxico (nome comercial / popular) 2. _2 | — | todos |
| `agente_3` | `AGENTE_3` | texto | Agente tóxico (nome comercial / popular) 3. _3 | — | todos |
| `p_ativo_1` | `P_ATIVO_1` | texto | Agente tóxico (princípio ativo) 1. _1 | — | todos |
| `p_ativo_2` | `P_ATIVO_2` | texto | Agente tóxico (princípio ativo) 2. _2 | — | todos |
| `p_ativo_3` | `P_ATIVO_3` | texto | Agente tóxico (princípio ativo) 3. _3 | — | todos |
| `utilizacao` | `UTILIZACAO` | texto | Se agrotóxico, qual a finalidade da utilização. 1 Inseticida 2 Herbicida 3 Carrapaticida 4 Raticida 5 Fungicida 6 Preservante para madeira 7 Outro 8 Não se aplica 9 Ignorado | — | todos |
| `ativida_1` | `ATIVIDA_1` | texto | Se agrotóxico, quais as atividades exercidas na exposição atual (1ª opção). 01 Diluição 02 Pulverização 03 Tratamento de sementes 04 Armazenagem 05 Colheita 06 Transporte 07 Desinsetização 08 Produção / formulação 09 Outros 10 Não se aplica 99 Ignorado | — | todos |
| `ativida_2` | `ATIVIDA_2` | texto | Se agrotóxico, quais as atividades exercidas na exposição atual (2ª opção). 01 Diluição 02 Pulverização 03 Tratamento de sementes 04 Armazenagem 05 Colheita 06 Transporte 07 Desinsetização 08 Produção / formulação 09 Outros 10 Não se aplica | — | todos |
| `ativida_3` | `ATIVIDA_3` | texto | Se agrotóxico, quais as atividades exercidas na exposição atual (3ª opção). 01 Diluição 02 Pulverização 03 Tratamento de sementes 04 Armazenagem 05 Colheita 06 Transporte 07 Desinsetização 08 Produção / formulação 09 Outros 10 Não se aplica 99 Ignorado | — | todos |
| `via_1` | `VIA_1` | texto | Via de exposição / contaminação (1ª opção). cao_1 | — | todos |
| `via_2` | `VIA_2` | texto | Via de exposição / contaminação (2ª opção). cao_2 | — | todos |
| `via_3` | `VIA_3` | texto | Via de exposição / contaminação (3ª opção). cao_3 | — | todos |
| `circunstan` | `CIRCUNSTAN` | texto | Circunstância da exposição / contaminação. 01 Uso habitual 02 Acidental 03 Ambiental 04 Uso terapêutico 05 Prescrição médica inadequada 06 Erro de administração 07 Automedicação 08 Abuso 09 Ingestão de alimento ou bebida 10 Tentativa de suicídio 11 Tentativa de aborto 12 Violência / homicídio 13 Outra 99 Ignorado | — | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | A exposição/contaminação pode ser considerado acidente de trabalho/ocupacional | — | todos |
| `tpexp` | `TPEXP` | texto | Tipo de exposição. 1 Aguda – única 2 Aguda – repetida 3 Crônica 4 Aguda sobre crônica | — | todos |
| `nutempo` | `NUTEMPO` | texto | Número que compõe o tempo (de exposição ou de ocorrência); a unidade está em `tptempo` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tptempo` | `TPTEMPO` | texto | Unidade do tempo informado em `nutempo` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tpatende` | `TPATENDE` | texto | Tipo de atendimento. 1 Hospitalar 2 Ambulatorial 3 Domiciliar 4 Nenhum 9 Ignorado | — | todos |
| `hospital` | `HOSPITAL` | texto | Houve hospitalização | 1-Sim 2-Não 9-Ignorado | todos |
| `dtinterna` | `DTINTERNA` | data | Data da internação. Data da internação deve ser >= a Data de primeiros sintomas | — | todos |
| `uf_hosp` | `UF_HOSP` | texto | UF. Informar a UF do hospital | — | todos |
| `mun_hosp` | `MUN_HOSP` | texto | Município de hospitalização | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final | — | todos |
| `diag_conf` | `DIAG_CONF` | texto | Se intoxicação confirmada, qual o diagnóstico (cid – 10). o | — | todos |
| `criterio` | `CRITERIO` | texto | Critério de confirmação | — | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. 1 Cura sem sequela 2 Cura com sequela 3 Óbito por intoxicação exógena 4 Óbito por outra causa 5 Perda do seguimento 9 Ignorada | — | todos |
| `dt_obito` | `DT_OBITO` | data | Data óbito. Informar data do óbito | — | todos |
| `cat` | `CAT` | texto | Comunicação de acidente de trabalho (cat). acidente_trab | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Informar a data do encerramento do caso | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | todos |
| `trab_desc` | `TRAB_DESC` | texto | Se outro especificar. alho_outro | — | todos |
| `loc_exp_de` | `LOC_EXP_DE` | texto | Local de ocorrência da exposição (outro) especificar | — | todos |
| `out_agente` | `OUT_AGENTE` | texto | Grupo do agente tóxico / classificação geral Outro (especificar). _outro | — | todos |
| `util_desc` | `UTIL_DESC` | texto | Se agrotóxico, qual a finalidade da utilização Outro (especificar). o | — | todos |
| `lavoura` | `LAVOURA` | texto | Se agrotóxico de uso agrícola, qual a cultura / lavoura. a | — | todos |
| `circun_des` | `CIRCUN_DES` | texto | Circunstância da exposição / contaminação Outro (especificar). _outro | — | todos |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `intox_chum` | `INTOX_CHUM` | texto | Intoxicação exógena por chumbo**. Informar se o produto químico foi classificado como chumbo | 1 – Sim Vazio – Não ou Ignorado/Branco | 2012 a 2026 |
| `intox_merc` | `INTOX_MERC` | texto | Intoxicação exógena por mercúrio**. nformar se o produto químico foi classificado como mercúrio | 1 – Sim Vazio – Não ou Ignorado/Branco | 2012 a 2026 |
| `intox_meta` | `INTOX_META` | texto | Intoxicação exógena por metanol**. nformar se o produto químico foi classificado como metanol | 1 – Sim Vazio – Não ou Ignorado/Branco | 2012 a 2026 |

## No lake

- **Dataset no lake:** `datasus/sinan-iexo`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 14, inteiro: 4, texto: 67.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-iexo.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- é uma das maiores bases do SINAN e inclui grande volume de casos não ocupacionais (medicamentos, tentativas de autoextermínio, acidentes domésticos); filtre por `CIRCUNSTAN`/`SIT_TRAB`/`CNAE` para análises ocupacionais. Os agentes tóxicos podem ser registrados com granularidade variável (nome do princípio ativo é texto livre, sujeito a inconsistências) e há múltiplos campos de agente. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. Arquivos do diretório PRELIM (2023+) são preliminares; como `NU_NOTIFIC` não consta dos arquivos públicos, deduplique por combinação de campos (ex.: `ID_UNIDADE`, `DT_NOTIFIC`, `ID_MN_RESI`, `ANO_NASC`, `CS_SEXO`) ao combinar as duas fontes. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 4 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-iexo").glob("**/*.parquet"))
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
datasus-fetcher list sinan-iexo

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-iexo -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-iexo
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (Intoxicação Exógena): https://portalsinan.saude.gov.br/
- Nota Técnica sobre Intoxicação Exógena (FTP DATASUS, `/SINAN/DOCS`): `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DOCS/Nota_Tecnica_Intoxicacao_Exogena.pdf`
- Guia de Vigilância em Saúde (SVSA/MS): https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- RENAST — Rede Nacional de Atenção Integral à Saúde do Trabalhador: https://www.gov.br/saude/pt-br/composicao/svsa/saude-do-trabalhador/renast
