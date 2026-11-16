---
dataset:
  id: sinan-lerd
  fonte: datasus
  titulo: LER/Dort
  resumo: 'LER/Dort do DATASUS: uma ficha de notificação/investigação de lER/Dort.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2006'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de lER/Dort
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 74
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# LER/Dort (`sinan-lerd`)

## Resumo

Notificações de Lesões por Esforços Repetitivos / Distúrbios Osteomusculares Relacionados ao Trabalho (LER/DORT), registradas no SINAN. Cada linha representa uma ficha de investigação de um caso de doença do sistema musculoesquelético causada, mantida ou agravada pelo trabalho.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM, 2023–2026; Finais até 2022)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `LERD` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `LERD` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `LERDBR24.dbc`, em que `LERD` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024, preliminar).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-lerd/<AAAA>/sinan-lerd_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-lerd/2024/sinan-lerd_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`DRT LER/DORT`) é distribuído no Portal SINAN; não há PDF por agravo no FTP.

## Conteúdo

A LER/DORT integra a lista de Doenças e Agravos Relacionados ao Trabalho (DART) de notificação compulsória no SUS, sob a coordenação da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) e operacionalização da RENAST/CEREST. A notificação compulsória decorre da Portaria MS nº 777/2004 e da Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V; Portaria GM/MS nº 217/2023).

O evento gerador é toda doença, lesão ou síndrome que afeta o sistema musculoesquelético (CID-10 G50–G59, G90–G99, M00–M99), causada, mantida ou agravada pelo trabalho, caracterizada por sintomas como dor crônica, parestesia e fadiga muscular, principalmente em pescoço, coluna vertebral, cintura escapular e membros. A unidade de análise é o caso notificado (um registro por ficha), com ocupação (CBO), situação no mercado de trabalho, tempo de exposição ao agente de risco e dados da empresa contratante (CNAE, CNPJ/CPF).

O instrumento é a *Ficha de Investigação — LER/DORT*, que registra agravos associados (hipertensão, transtorno mental, diabetes, tuberculose, hanseníase, asma, outras), regime de tratamento, sinais e sintomas, limitação/incapacidade, exposição no trabalho (jornada > 6 horas, pausas) e conduta. A série no FTP inicia em 2006; os dados de 2023 em diante estão em PRELIM e sujeitos a revisão.

Principais usos: incidência de LER/DORT por ramo (CNAE) e ocupação (CBO), avaliação de afastamentos e incapacidades, vigilância de setores com processos de trabalho repetitivos (bancários, frigoríficos, teleatendimento, indústria) e base para ações de VISAT e de reabilitação profissional.

### Cobertura observada

- Índice do FTP (2026-10): 21 arquivos, de 2006 a 2026, 1 UF(s) com arquivos, última atualização em 2026-09-02.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2006 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo `LERDBR26.dbc` (leiaute do SINAN Net; fichas e leiautes podem variar entre anos, por isso a lista reflete esse arquivo). Os arquivos públicos não trazem identificadores individuais como número da notificação (`NU_NOTIFIC`) nem data de nascimento completa. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

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
| `DT_DIAG` | Data (AAAAMMDD) | Data do diagnóstico. |
| `SEM_DIAG` | String | Semana epidemiológica do diagnóstico (AAAASS). |
| `ANO_NASC` | String | Ano de nascimento (o arquivo público não traz a data de nascimento completa). |
| `NU_IDADE_N` | Inteiro | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade. |
| `SG_UF` | String | UF de residência (código IBGE de 2 dígitos). |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `ID_OCUPA_N` | String | Ocupação do trabalhador (CBO 2002, 6 dígitos). |
| `SIT_TRAB` | String | Situação no mercado de trabalho. |
| `CNAE` | String | Atividade econômica da empresa contratante (CNAE). |
| `HIPERTEN` | String | Doença preexistente: hipertensão. |
| `TUBE` | String | Doença preexistente: tuberculose. |
| `DIABETES` | String | Doença preexistente: diabetes. |
| `ASMA` | String | Doença preexistente: asma. |
| `HANSENIASE` | String | Doença preexistente: hanseníase. |
| `MENTAL` | String | Doença preexistente: transtorno mental. |
| `OUT_AGRAVO` | String | Doença preexistente: outro agravo (descrição em `AGRAVO_DES`). |
| `SENSIBILI` | String | Sintoma: alteração de sensibilidade. |
| `LIMITA_MOV` | String | Sintoma: limitação de movimento. |
| `MUSCULAR` | String | Sintoma: alteração de força muscular. |
| `FLOGISTICO` | String | Sinal flogístico (inflamatório). |
| `MENOS_MOV` | String | Sintoma: diminuição de movimentos. |
| `DOR` | String | Sintoma: dor. |
| `OUTRO_SIN` | String | Outro sintoma. |
| `TAREFAS` | String | Fator organizacional: tarefas com metas/ritmo. |
| `PREMIOS` | String | Fator organizacional: sistema de prêmios/produtividade. |
| `HA_PAUSA` | String | Existência de pausas. |
| `REPETITIVO` | String | Movimentos repetitivos. |
| `MAIS_6HS` | String | Jornada superior a 6 horas. |
| `STRESS` | String | Estresse/pressão no trabalho. |
| `DIAG_ESP` | String | Diagnóstico específico (CID-10). |
| `AFASTAMENT` | String | Houve afastamento do trabalho. |
| `TRAB_DOE` | String | Outros trabalhadores com a mesma doença no local de trabalho. |
| `AFAST_RISC` | String | Conduta: afastamento do local de risco. |
| `INDIVIDUAL` | String | Conduta: ação individual. |
| `MUDA_TRAB` | String | Conduta: mudança de função/posto de trabalho. |
| `NENHUM` | String | Conduta: nenhuma ação. |
| `COLETIVA` | String | Conduta: ação coletiva. |
| `AFAST_TRAB` | String | Conduta: afastamento do trabalho. |
| `CONDUTA` | String | Conduta adotada (marcação geral da ficha). |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito, quando aplicável. |
| `CAT` | String | Foi emitida a Comunicação de Acidente do Trabalho (CAT)? |
| `AGRAVO_DES` | String | Descrição textual de outro agravo preexistente. |
| `SINTO_DES` | String | Descrição textual de outro sintoma. |
| `CONDUT_DES` | String | Descrição textual de outra conduta. |

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
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Ocupação do indivíduo que sofreu o agravo | — | todos |
| `sit_trab` | `SIT_TRAB` | texto | Situação no mercado de trabalho. o | 01. Empregado registrado com carteira assinada 02. Empregado não registrado 03. Autônomo/conta própria 04. Servidor público estatuário 05. Servidor público celetista 06. Aposentado 07. Desempregado 08. Trabalho tempor... | todos |
| `nutempo` | `NUTEMPO` | texto | Número que compõe o tempo (de exposição ou de ocorrência); a unidade está em `tptempo` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tptempo` | `TPTEMPO` | texto | Unidade do tempo informado em `nutempo` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `cnae` | `CNAE` | texto | Atividade Econômica(CNAE). Classificação Nacional da Atividade Econômica do Contratante | — | todos |
| `uf_emp` | `UF_EMP` | texto | UF. Unidade federativa da empresa contratante | — | todos |
| `mun_emp` | `MUN_EMP` | texto | Município | — | todos |
| `terceiriza` | `TERCEIRIZA` | texto | O empregador é empresa Terceirizada | 01- sim 02- não 03- não se aplica 09- ignorado | todos |
| `hiperten` | `HIPERTEN` | texto | Agravos associados Hipertensão arterial | 1. sim 2. não 9. Ignorado | todos |
| `tube` | `TUBE` | texto | Agravos associados Tuberculose | 1. sim 2. não 9. Ignorado | todos |
| `diabetes` | `DIABETES` | texto | Agravos associados Diabetes Mellitus. s | 1. sim 2. não 9. Ignorado | todos |
| `asma` | `ASMA` | texto | Agravos associados Asma. Condição associada ao agravo – Asma | 1. sim 2. não 9. Ignorado | todos |
| `hanseniase` | `HANSENIASE` | texto | Agravos associados Hanseníase | 1. sim 2. não 9. Ignorado | todos |
| `mental` | `MENTAL` | texto | Agravos associados transtorno mental | 1. sim 2. não 9. Ignorado | todos |
| `out_agravo` | `OUT_AGRAVO` | texto | Agravos associados outras. Condição associada ao agravo – outra doença | 1. sim 2. não 9. Ignorado | todos |
| `nutemporis` | `NUTEMPORIS` | texto | Número que compõe o tempo de exposição ao agente de risco; a unidade está em `tptemporis` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tptemporis` | `TPTEMPORIS` | texto | Unidade do tempo informado em `nutemporis` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `regime` | `REGIME` | texto | Regime de tratamento | 1. hospitalar 2. ambulatorial | todos |
| `sensibili` | `SENSIBILI` | texto | Sinais e Sintomas Alteração de sensibilidade | 1. sim 2. não 9. Ignorado | todos |
| `limita_mov` | `LIMITA_MOV` | texto | Sinais e Sintomas Limitação de movimentos | 1. sim 2. não 9. Ignorado | todos |
| `muscular` | `MUSCULAR` | texto | Sinais e Sintomas Diminuição de força muscular | 1. sim 2. não 9. Ignorado | todos |
| `flogistico` | `FLOGISTICO` | texto | Sinais e Sintomas Sinais Flogísticos | 1. sim 2. não 9. Ignorado | todos |
| `menos_mov` | `MENOS_MOV` | texto | Sinais e Sintomas Diminuição do movimento. o | 1. sim 2. não 9. Ignorado | todos |
| `dor` | `DOR` | texto | Sinais e Sintomas Dor | 1. sim 2. não 9. Ignorado | todos |
| `outro_sin` | `OUTRO_SIN` | texto | Sinais e Sintomas Outro. Outros Sinais e Sintomas | 1. sim 2. não 9. Ignorado | todos |
| `tarefas` | `TAREFAS` | texto | Limitação e incapacidade para o exercício de tarefas. O paciente ficou incapacitado ou limitado para o exercício de tarefas | 1. sim 2. não 9. Ignorado | todos |
| `premios` | `PREMIOS` | texto | O paciente está exposto em seu local de trabalho a Prêmios de produção. O paciente tem incentivos/prêmios se atingir ou superar determinados níveis de produção | 1. sim 2. não 9. Ignorado | todos |
| `ha_pausa` | `HA_PAUSA` | texto | O paciente está exposto em seu local de trabalho à tempo de pausas. O paciente tem intervalo para descanso durante sua jornada de trabalho | 1. sim 2. não 9. Ignorado | todos |
| `repetitivo` | `REPETITIVO` | texto | O paciente está exposto em seu local de trabalho à Movimentos repetitivos. o | 1. sim 2. não 9. Ignorado | todos |
| `mais_6hs` | `MAIS_6HS` | texto | O paciente está exposto em seu local de trabalho à Jornada de trabalho de mais de 6 horas. O paciente tem uma jornada de trabalho diária superior a seis horas | 1. sim 2. não 9. Ignorado | todos |
| `stress` | `STRESS` | texto | O paciente está exposto em seu local de trabalho à ambiente estressante | 1. sim 2. não 9. Ignorado | todos |
| `diag_esp` | `DIAG_ESP` | texto | Diagnostico Específico CID 10. Diagnóstico específico - CID 10 | — | todos |
| `afastament` | `AFASTAMENT` | texto | Houve afastamento do Trabalho para tratamento | 1. sim 2. não 9. Ignorado | todos |
| `nu_afast` | `NU_AFAST` | texto | Tempo de afastamento do trabalho (número); a unidade está em `tp_afast` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tp_afast` | `TP_AFAST` | texto | Unidade do tempo de afastamento do trabalho (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `evol_afast` | `EVOL_AFAST` | texto | Com afastamento do trabalho | — | todos |
| `trab_doe` | `TRAB_DOE` | texto | Há ou houve outros trabalhadores com a mesma doença no local de trabalho. ma_doenca | — | todos |
| `afast_risc` | `AFAST_RISC` | texto | Conduta geral afastamento do agente do risco com mudança de função e/ ou posto de trabalho. mento_risco | 1. Sim 2. Não | todos |
| `individual` | `INDIVIDUAL` | texto | Conduta geral adoção de proteção individual. o_individual | 1. Sim 2. Não | todos |
| `muda_trab` | `MUDA_TRAB` | texto | Conduta geral adoção de mudança na organização do trabalho. ca_trabalho | 1. Sim 2. Não | todos |
| `nenhum` | `NENHUM` | texto | Conduta geral nenhum. m | 1. Sim 2. Não | todos |
| `coletiva` | `COLETIVA` | texto | Conduta geral adoção de proteção coletiva. o_coletiva | 1. Sim 2. Não | todos |
| `afast_trab` | `AFAST_TRAB` | texto | Conduta geral Afastamento do local de trabalho. o_coletiva | 1. Sim 2. Não | todos |
| `conduta` | `CONDUTA` | texto | Conduta geral outros. Atitude tomada em relação ao agravo – outros | 1. Sim 2. Não | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. Como evoluiu a situação do paciente | 1. Cura 2. Cura não confirmada 3. Incapacidade temporária 4. Incapacidade permanente parcial 5. Incapacidade permanente total 6. Óbito por doença relacionada ao trabalho 7. Óbito por outra causa 8. Outro 9. Ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito | — | todos |
| `cat` | `CAT` | texto | Foi emitida a comunicação de acidente do trabalho. Foi feita comunicação de acidente do trabalho | 1. Sim 2. Não 3. Não se aplica 9. Ignorado | todos |
| `agravo_des` | `AGRAVO_DES` | texto | Agravos associados se outros especificar | — | todos |
| `sinto_des` | `SINTO_DES` | texto | Sinais e Sintomas Se Outro especificar. Sinais e sintomas se outros especificar | — | todos |
| `condut_des` | `CONDUT_DES` | texto | Conduta geral Se Outro especificar. Atitude tomada em relação ao agravo – se outros especificar | — | todos |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-lerd`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 3, inteiro: 1, texto: 70.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-lerd.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- o `ID_AGRAVO` costuma ser o código genérico da LER/DORT e não identifica o diagnóstico específico (M-codes); a análise por CID exige campos adicionais ou o relacionamento com a AIH/atestado. Os agravos associados são modelados como múltiplas colunas booleanas, (`HIPERTEN`, `TUBE`, `DIABETES`, `ASMA`, `HANSENIASE`, `MENTAL`, `OUT_AGRAVO`). Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. Arquivos do diretório PRELIM (2023+) são preliminares; como `NU_NOTIFIC` não consta dos arquivos públicos, deduplique por combinação de campos (ex.: `ID_UNIDADE`, `DT_NOTIFIC`, `ID_MN_RESI`, `ANO_NASC`, `CS_SEXO`) ao combinar as duas fontes. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-lerd").glob("**/*.parquet"))
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
datasus-fetcher list sinan-lerd

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-lerd -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-lerd
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (DRT LER/DORT): https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Saúde do Trabalhador: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- RENAST — Rede Nacional de Atenção Integral à Saúde do Trabalhador: https://www.gov.br/saude/pt-br/composicao/svsa/saude-do-trabalhador/renast
