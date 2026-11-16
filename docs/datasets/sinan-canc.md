---
dataset:
  id: sinan-canc
  fonte: datasus
  titulo: Câncer relacionado ao trabalho
  resumo: 'Câncer relacionado ao trabalho do DATASUS: uma ficha de notificação/investigação de câncer relacionado ao trabalho.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de câncer relacionado ao trabalho
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 68
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Câncer relacionado ao trabalho (`sinan-canc`)

## Resumo

Notificações de casos de câncer cuja causalidade inclui exposição a fatores, agentes ou situações de risco presentes no ambiente e no processo de trabalho, registradas no SINAN. Cada linha representa uma ficha de investigação de um caso confirmado de câncer relacionado ao trabalho (CART).

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM, 2023–2026; Finais até 2022)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `CANC` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `CANC` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `CANCBR24.dbc`, em que `CANC` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024, preliminar).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-canc/<AAAA>/sinan-canc_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-canc/2024/sinan-canc_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`DRT Câncer Relacionado ao Trabalho`) é distribuído no Portal SINAN; não há PDF por agravo no FTP.

## Conteúdo

O Câncer Relacionado ao Trabalho (CART) integra a lista de Doenças e Agravos Relacionados ao Trabalho (DART) de notificação compulsória no SUS, sob a coordenação da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) e operacionalização da RENAST/CEREST. A notificação compulsória decorre da Portaria MS nº 777/2004 e da Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V; Portaria GM/MS nº 217/2023).

O evento gerador é todo caso de câncer que tem entre seus elementos causais a exposição a agentes carcinogênicos ocupacionais (ex.: asbesto, benzeno, sílica, radiação ionizante, agrotóxicos), mesmo após a cessação da exposição. A definição é ampla e a comprovação do nexo é frequentemente difícil, o que torna a base pequena em relação ao universo de neoplasias. A unidade de análise é o caso notificado (um registro por ficha), com CID-10 da neoplasia, ocupação (CBO), situação no mercado de trabalho e dados da empresa contratante (CNAE, CNPJ/CPF).

O instrumento é a *Ficha de Investigação — Câncer Relacionado ao Trabalho*. A notificação exige investigação de história ocupacional pregressa, agentes de exposição e tempo de latência, e o encerramento registra a evolução em categorias próprias (remissão completa/parcial, doença estável/em progressão, fora de possibilidade terapêutica, óbito pelo câncer, óbito por outras causas). A série no FTP inicia em 2007 e os dados de 2023 em diante estão em PRELIM, sujeitos a revisão.

Principais usos: vigilância de casos sentinela em setores de alta exposição, caracterização de nexo ocupacional por ramo (CNAE) e ocupação (CBO), apoio à Notificação Compulsória e ao estabelecimento de nexo para fins previdenciários, além de embasar ações de VISAT e de interdição de ambientes de trabalho.

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-09-03.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo `CANCBR26.dbc` (leiaute do SINAN Net; fichas e leiautes podem variar entre anos, por isso a lista reflete esse arquivo). Os arquivos públicos não trazem identificadores individuais como número da notificação (`NU_NOTIFIC`) nem data de nascimento completa. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (registro da ficha de notificação individual). |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | String | Ano da notificação. |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE). |
| `ID_UNIDADE` | String | Código CNES da unidade de saúde notificadora (7 dígitos). |
| `DT_DIAG` | Data (AAAAMMDD) | Data do diagnóstico. |
| `SEM_DIAG` | String | Semana epidemiológica do diagnóstico (AAAASS). |
| `ANO_NASC` | String | Ano de nascimento (o arquivo público não traz a data de nascimento completa). |
| `NU_IDADE_N` | String | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade. |
| `SG_UF` | String | UF de residência (código IBGE de 2 dígitos). |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `ID_OCUPA_N` | String | Ocupação do trabalhador (CBO 2002, 6 dígitos). |
| `SIT_TRAB` | String | Situação no mercado de trabalho. |
| `CNAE` | String | Atividade econômica da empresa contratante (CNAE). |
| `DIAG_ESP` | String | Diagnóstico específico (CID-10). |
| `ASBESTO` | String | Exposição a asbesto/amianto. |
| `SILICA` | String | Exposição a sílica. |
| `AMINA` | String | Exposição a aminas aromáticas. |
| `BENZENO` | String | Exposição a benzeno. |
| `ALCATRAO` | String | Exposição a alcatrão. |
| `HIDROCARBO` | String | Exposição a hidrocarbonetos. |
| `OLEOS` | String | Exposição a óleos minerais. |
| `BERILIO` | String | Exposição a berílio. |
| `CADMIO` | String | Exposição a cádmio. |
| `CROMO` | String | Exposição a cromo. |
| `NIQUEL` | String | Exposição a níquel. |
| `IONIZANTES` | String | Exposição a radiações ionizantes. |
| `NAO_IONIZA` | String | Exposição a radiações não ionizantes. |
| `HORMONIO` | String | Exposição a hormônios. |
| `NEOPLASICO` | String | Exposição a agentes antineoplásicos. |
| `OUTRO_EXP` | String | Outra exposição (descrição em `OUT_EXP_DE`). |
| `FUMA` | String | Hábito de fumar (marcação da ficha). |
| `TEMPO_FUMA` | String | Tempo de tabagismo (valor; unidade em `TP_TEMP_FU`). |
| `TP_TEMP_FU` | String | Unidade do tempo de tabagismo. |
| `TRAB_DOE` | String | Outros trabalhadores com a mesma doença no local de trabalho. |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito, quando aplicável. |
| `CAT` | String | Foi emitida a Comunicação de Acidente do Trabalho (CAT)? |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno) | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_diag` | `DT_DIAG` | data | Data dos primeiros sintomas / Diagnóstico. Data dos primeiros sintomas do caso de agravo agudo. Data do diagnóstico do caso de agravo crônico e DRTs Data do acidente nos acidentes da saúde do trabalhador | — | todos |
| `sem_diag` | `SEM_DIAG` | texto | Semana epidemiológica dos primeiros sintomas/ diagnósticos. (campo interno). Semanas do calendário epidemiológico padronizado | — | todos |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | texto | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil) | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. o | — | todos |
| `sit_trab` | `SIT_TRAB` | texto | Situação no mercado de trabalho. Situação de trabalho do indivíduo que sofreu o agravo | 01. Empregado registrado com carteira assinada 02. Empregado não registrado 03. Autônomo/conta | todos |
| `nutempo` | `NUTEMPO` | texto | Número que compõe o tempo (de exposição ou de ocorrência); a unidade está em `tptempo` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tptempo` | `TPTEMPO` | texto | Unidade do tempo informado em `nutempo` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `cnae` | `CNAE` | texto | Código da atividade Econômica(CNAE). Classificação Nacional da Atividade Econômica do Contratante | — | todos |
| `uf_emp` | `UF_EMP` | texto | UF. Unidade da Federação da empresa contratante | — | todos |
| `mun_emp` | `MUN_EMP` | texto | Município. a | — | todos |
| `terceiriza` | `TERCEIRIZA` | texto | O empregador é empresa Terceirizada | 01- Sim 02- Não 03- Não se aplica 09- Ignorado | todos |
| `nutemporis` | `NUTEMPORIS` | texto | Número que compõe o tempo de exposição ao agente de risco; a unidade está em `tptemporis` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tptemporis` | `TPTEMPORIS` | texto | Unidade do tempo informado em `nutemporis` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `regime` | `REGIME` | texto | Regime de tratamento. O tratamento ocorreu em regime hospitalar ou ambulatorial | 1 – hospitalar 2 - ambulatorial | todos |
| `diag_esp` | `DIAG_ESP` | texto | Diagnóstico específico. co_cid_diagnóstico | — | todos |
| `asbesto` | `ASBESTO` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Asbesto ou Amianto | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `silica` | `SILICA` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Sílica livre, arsênico e seus compostos arsenicais. Ocorreu exposição nos locais de trabalho, durante toda a sua vida profissional Sílica livre, arsênico e seus compostos arsenicais | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `amina` | `AMINA` | texto | Houve exposição nos locais de trabalho, | 1 – Sim 2 – Não | todos |
| `benzeno` | `BENZENO` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Benzeno ou seus homólogos tóxicos. Ocorreu exposição nos locais de trabalho, durante toda a sua vida profissional Benzeno ou seus homólogos tóxicos | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `alcatrao` | `ALCATRAO` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Alcatrão, breu, betume, hulha mineral, parafina e produtos ou resíduos dessas substâncias. Ocorreu exposição nos locais de trabalho, durante toda a sua vida profissional Alcatrão, breu, betume, hulha mineral, parafina e produtos ou resíduos dessas substâncias | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `hidrocarbo` | `HIDROCARBO` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Hidrocarbonetos alifáticos ou aromáticos (seus derivados halogenados). Ocorreu exposição nos locais de trabalho, durante toda a sua vida profissional Hidrocarbonetos alifáticos ou aromáticos (seus derivados halogenados) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `oleos` | `OLEOS` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Óleos Minerais. Ocorreu exposição nos locais de trabalho, durante toda a sua vida profissional Óleos Minerais | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `berilio` | `BERILIO` | texto | Houve exposição nos. Ocorreu exposição | 1 – Sim | todos |
| `cadmio` | `CADMIO` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Cádmio ou seus compostos. Ocorreu exposição nos locais de trabalho, durante toda a sua vida profissional Cádmio ou seus compostos | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cromo` | `CROMO` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Cromo ou seus compostos tóxicos. Ocorreu exposição nos locais de trabalho, durante toda a sua vida profissional Cromo ou seus compostos tóxicos | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `niquel` | `NIQUEL` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Composto de Níquel | — | todos |
| `ionizantes` | `IONIZANTES` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Radiações Ionizantes | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `nao_ioniza` | `NAO_IONIZA` | texto | Houve exposição nos. Ocorreu exposição | 1 – Sim | todos |
| `hormonio` | `HORMONIO` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Hormônios. Ocorreu exposição nos locais de trabalho, durante toda a sua vida profissional Hormônios | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `neoplasico` | `NEOPLASICO` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Antineoplásicos. Ocorreu exposição nos locais de trabalho, durante toda a sua vida profissional Antineoplásicos | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `outro_exp` | `OUTRO_EXP` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Outros. Ocorreu exposição nos locais de trabalho, durante toda a sua vida profissional Outros | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `fuma` | `FUMA` | texto | Hábito de fumar | 1 – Sim 2 – Não 3 – Ex-fumante 9 – Ignorado | todos |
| `tempo_fuma` | `TEMPO_FUMA` | texto | Tempo de tabagismo (número); a unidade está em `tp_temp_fu` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tp_temp_fu` | `TP_TEMP_FU` | texto | Unidade do tempo de tabagismo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `trab_doe` | `TRAB_DOE` | texto | Há ou houve outros. Campo | 1 – Sim | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. Como evoluiu a situação do paciente | 1- Sem evidência da doença (remissão completa) 2- Remissão parcial 3- Doença estável 4- Doença em Progressão 5- Fora de possibilidade terapêutica 6- Óbito por câncer relacionado ao trabalho 7- Óbito por outras causas ... | todos |
| `dt_obito` | `DT_OBITO` | data | Se, óbito data. Se, óbito colocar data | — | todos |
| `cat` | `CAT` | texto | Foi emitida a comunicação de Acidente de Trabalho. Informar se foi emitida a comunicação de acidente do trabalho | 1- Sim 2- Não 3- Não se aplica 9- Ignorado | todos |
| `out_exp_de` | `OUT_EXP_DE` | texto | Houve exposição nos locais de trabalho, durante toda a sua vida profissional, a algum dos itens abaixo relacionados? Outros (especificar). Ocorreu exposição nos locais de trabalho, durante toda a sua vida profissional Outros (Especificar) | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_trnasrm` | `DT_TRNASRM` | data | Data de transmissão do registro (nome gravado com erro de grafia na fonte) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-canc`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 10, nulo (vazio nas amostras): 3, texto: 58.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-canc.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- é uma base pequena e sensível à subnotificação; o CID-10 (`ID_AGRAVO`) pode não corresponder ao tipo histológico real, e o nexo ocupacional depende da qualidade da história ocupacional registrada. Não há separação por UF nos arquivos (`BR`); use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. Arquivos do diretório PRELIM (2023+) são preliminares; como `NU_NOTIFIC` não consta dos arquivos públicos, deduplique por combinação de campos (ex.: `ID_UNIDADE`, `DT_NOTIFIC`, `ID_MN_RESI`, `ANO_NASC`, `CS_SEXO`) ao combinar as duas fontes. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-canc").glob("**/*.parquet"))
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
datasus-fetcher list sinan-canc

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-canc -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-canc
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (DRT Câncer Relacionado ao Trabalho): https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Saúde do Trabalhador: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- RENAST — Rede Nacional de Atenção Integral à Saúde do Trabalhador: https://www.gov.br/saude/pt-br/composicao/svsa/saude-do-trabalhador/renast
