---
dataset:
  id: sinan-leiv
  fonte: datasus
  titulo: Leishmaniose Visceral
  resumo: 'Leishmaniose Visceral do DATASUS: uma ficha de notificação/investigação de leishmaniose Visceral.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2000'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de leishmaniose Visceral
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 114
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    peso: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ampolas: 'número inteiro: contagem ou código numérico (ver Descrição)'
    co_pais_1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    co_pais_2: 'número inteiro: contagem ou código numérico (ver Descrição)'
    co_pais_3: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Leishmaniose Visceral (`sinan-leiv`)

## Resumo

O `sinan-leiv` contém os microdados das notificações e investigações de casos de Leishmaniose Visceral (LV, ou calazar; CID-10 B55.0) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de leishmaniose visceral humana, digitada no SINAN Net/Sinan Online. A LV é de notificação compulsória em todo o território nacional e a base é o insumo central da vigilância da leishmaniose visceral humana no país.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `LEIV` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `LEIV` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `LEIVBR00.dbc` — prefixo `LEIV`, `BR` (consolidação nacional) e `00` (ano 2000, início da série disponível); a série vai até `LEIVBR25.dbc` (2025). Conforme o inventário atual do FTP não há arquivo em `PRELIM` para este agravo no momento.
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-leiv/<AAAA>/sinan-leiv_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-leiv/2024/sinan-leiv_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/descompactação/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## Conteúdo

A leishmaniose visceral é uma zoonose parasitária grave (letalidade elevada quando não tratada) causada no Brasil pela *Leishmania infantum* (sin. *L. chagasi*), transmitida por flebotomíneos — sobretudo *Lutzomyia longipalpis* — com o cão doméstico como principal reservatório urbano. A vigilância é gerida pela SVSA/MS por meio do Programa de Vigilância e Controle da Leishmaniose Visceral (que inclui o componente canino com recolhimento de animais sororreativos). A notificação dos casos humanos é compulsória (Portaria SVS/MS nº 104/2011; hoje na Portaria GM/MS nº 204/2016 e atualizações).

O evento gerador é a **Ficha de Investigação da Leishmaniose Visceral** do SINAN (revisada em 2006/2007 como ficha LV_v5), preenchida diante do caso suspeito — febre longa acompanhada de hepatoesplenomegalia, palidez, anemia, emaciação e/ou emagrecimento — e completada ao longo da investigação com parasitológico de medula óssea ou sorologia (ELISA, IFI), classificação de evolução clínica e desfecho. A unidade de análise é o caso individual notificado, em residentes de áreas com ou sem transmissão documentada.

Marcos normativos e de leiaute: a ficha foi revisada a partir de 2006 e a notificação passou a fluir pelo SINAN Net (2007+) e pelo Sinan Online (2014+). A LV transicionou de perfil rural para periurbano/urbano ao longo de 2000-2010 (grandes surtos metropolitanos em Teresina, Belo Horizonte, São Luís e Fortaleza), com confirmação de casos em áreas demonstrativamente de transmissão intensa.

Aplicações analíticas: coeficiente de detecção anual (casos/100 mil), letalidade específica (alta em pediatria), distribuição por faixa etária, sexo, raça/cor e escolaridade, oportuna vigilância de internações e desfecho (cura, óbito, abandono), e mapeamento de municípios prioritários para controle vetorial e vigilância canina.

### Cobertura observada

- Índice do FTP (2026-10): 26 arquivos, de 2000 a 2025, 1 UF(s) com arquivos, última atualização em 2026-09-03.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2000 a 2025), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Leishmaniose Visceral — CID-10 B55.0) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_RACA` | Inteiro | Raça/cor (1-Branca ... 5-Indígena, 9-Ignorado) |
| `ID_MN_RESI` | String (6/7) | Município de residência do caso (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `CLASSI_FIN` | Inteiro | Classificação final do caso (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Abandono, 3 - Óbito por LV, 4 - Óbito por outras causas, 5 - Transferência, 6 - Mudança de diagnóstico) |
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
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno) | — | todos |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_idade` | `NU_IDADE` | texto | Idade do paciente (formato do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2000 |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil) | — | todos |
| `id_dg_not` | `ID_DG_NOT` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Leishmaniose Visceral (`ID_DG_NOT`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `id_ev_not` | `ID_EV_NOT` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Leishmaniose Visceral (`ID_EV_NOT`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `ant_dt_inv` | `ANT_DT_INV` | data | Data da investigação | — | só em 2000 |
| `ocupacao` | `OCUPACAO` | texto | Ocupação do paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2000 |
| `caso` | `CASO` | texto | Indica caso (confirmado ou não) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2000 |
| `endemico` | `ENDEMICO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `febre` | `FEBRE` | texto | Sinais e Sintomas Febre. Informar se o paciente apresenta febre | 1- Sim 2- Não 9 -Ignorado | todos |
| `fraqueza` | `FRAQUEZA` | texto | Sinais e Sintomas Fraqueza | 1-Sim 2 Não 9 Ignorado | todos |
| `emagra` | `EMAGRA` | texto | Sinais e Sintomas Emagrecimento | 1- Sim 2-Não 9- Ignorado | todos |
| `tosse` | `TOSSE` | texto | Sinais e Sintomas Tosse e/ou diarréia. Informar se o paciente apresenta tosse e/ou diarréia | 1- Sim 2- Não 9-Ignorado | todos |
| `baco` | `BACO` | texto | Sinais e Sintomas Aumento do Baço. to_baco | 1- Sim 2 - Não 9 - Ignorado | todos |
| `figado` | `FIGADO` | texto | Sinais e Sintomas Aumento do Fígado. Informar se o paciente apresenta aumento do fígado | 1-Sim 2-Não 9-Ignorado | todos |
| `hiv` | `HIV` | texto | Co-infecção HIV. Informar se o paciente apresenta infecções intercorrentes – HIV | 1-Sim 2-Não 9-Ignorado | todos |
| `tube` | `TUBE` | texto | Agravos associados Tuberculose. Condição associada ao agravo – Tuberculose | 1- Sim 2- Não 9- Ignorado | só em 2000 |
| `outras` | `OUTRAS` | texto | O paciente foi submetido ou exposto à: Outras. Informar se o paciente submeteu-se outras situações de risco diferentes das existentes no campo, há quanto tempo. Se sim, especificar a situação. (considerar a data da investigação como parâmetro) | 1. Sim há menos de 6 meses 2. Sim há mais de seis meses 3. Não 9- Ignorado | só em 2000 |
| `ifi` | `IFI` | texto | Diagnóstico Imunológico IFI | 1. Positivo 2. Negativo 3. Não realizado | todos |
| `elisa` | `ELISA` | texto | Dado de exame laboratorial registrado na ficha de Leishmaniose Visceral (`ELISA`); o dicionário consultado não define o campo isoladamente | — | só em 2000 |
| `outro` | `OUTRO` | texto | Diagnóstico Imunológico Outro | 1. Positivo 2. Negativo 3. Não realizado | todos |
| `diag_para` | `DIAG_PARA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `droga` | `DROGA` | texto | Droga Inicial Administrada. Informar o medicamento prescrito para o tratamento inicial | 1. Antimonial Pentavalente 2. anfotericina b 3. Pentamidina 4. anfotericina b lipossomal 5. outras 6. Não utilizada | todos |
| `doses` | `DOSES` | texto | Registro de vacinação (`DOSES`) | — | só em 2000 |
| `duracao` | `DURACAO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2000 |
| `falencia` | `FALENCIA` | texto | Outra droga utilizada, na falência do tratamento inicial. a | 1 – Anfotericina B 2 – Anfotericina B lipossomal 3 – Outras 4 – Não se aplica | todos |
| `con_classi` | `CON_CLASSI` | texto | Classificação da forma clínica | 1. Forma bubônica 2. Forma pneumônica 3. Forma septicêmica 4 outra | só em 2000 |
| `con_inf_ou` | `CON_INF_OU` | texto | Dado de conclusão do caso na ficha de Leishmaniose Visceral (`CON_INF_OU`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_inf_ba` | `CON_INF_BA` | texto | Dado de conclusão do caso na ficha de Leishmaniose Visceral (`CON_INF_BA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_inf_di` | `CON_INF_DI` | texto | Dado de conclusão do caso na ficha de Leishmaniose Visceral (`CON_INF_DI`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_inf_mu` | `CON_INF_MU` | texto | Dado de conclusão do caso na ficha de Leishmaniose Visceral (`CON_INF_MU`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_inf_uf` | `CON_INF_UF` | texto | Dado de conclusão do caso na ficha de Leishmaniose Visceral (`CON_INF_UF`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_inf_pa` | `CON_INF_PA` | texto | Dado de conclusão do caso na ficha de Leishmaniose Visceral (`CON_INF_PA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_doenca` | `CON_DOENCA` | texto | Dado de conclusão do caso na ficha de Leishmaniose Visceral (`CON_DOENCA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_evoluc` | `CON_EVOLUC` | texto | Dado de conclusão do caso na ficha de Leishmaniose Visceral (`CON_EVOLUC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_dt_obi` | `CON_DT_OBI` | texto | Dado de conclusão do caso na ficha de Leishmaniose Visceral (`CON_DT_OBI`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `con_dt_enc` | `CON_DT_ENC` | data | Dado de conclusão do caso na ficha de Leishmaniose Visceral (`CON_DT_ENC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | só em 2000 |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | 2007 a 2025 |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | 2007 a 2025 |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | 2007 a 2025 |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | 2007 a 2025 |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | 2007 a 2025 |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | 2007 a 2025 |
| `nduplic_n` | `NDUPLIC_N` | texto | Não Listar/ Não Contar. 0 ou branco – Não identificado 1 – Não é duplicidade (não listar) 2 – Duplicidade (não contar) | — | 2007 a 2025 |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | 2007 a 2025 |
| `cs_flxret` | `CS_FLXRET` | texto | Fluxo de retorno. Identifica se o registro está habilitado ou foi enviado pelo fluxo de retorno para o município de residência | 0 - Não 1 - habilitado para envio. 2 - enviado | 2007 a 2025 |
| `flxrecebi` | `FLXRECEBI` | texto | Recebida por fluxo de retorno (campo interno). Colocar a estrutura do nº atribuído pelo sistema | — | 2007 a 2025 |
| `migrado_w` | `MIGRADO_W` | texto | Identifica migração (campo interno). Identifica se o registro é oriundo da rotina de migração da base Windows | 1- migrado do Sinan Windows | 2007 a 2025 |
| `dt_invest` | `DT_INVEST` | data | Data de investigação. Data em que ocorreu a investigação – informar a data da 1ª visita ao paciente | — | 2007 a 2025 |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/ Ramo de Atividade Econômica. o | — | 2007 a 2025 |
| `edema` | `EDEMA` | texto | Sinais e Sintomas Edema. Informar se o paciente apresenta edema | 1- Sim 2- Não 9- Ignorado | 2007 a 2025 |
| `palidez` | `PALIDEZ` | texto | Sinais e Sintomas Palidez. Informar se o paciente apresenta palidez | 1- Sim 2- Não 9- Ignorado | 2007 a 2025 |
| `infeccioso` | `INFECCIOSO` | texto | Sinais e Sintomas Quadro infeccioso | 1-Sim 2-Não 9- Ignorado | 2007 a 2025 |
| `fen_hemorr` | `FEN_HEMORR` | texto | Sinais e Sintomas Fenômenos hemorrágicos | 1- Sim 2 -Não 9 -Ignorado | 2007 a 2025 |
| `ictericia` | `ICTERICIA` | texto | Sinais e Sintomas Icterícia. a | 1-Sim 2-Não 9 -Ignorado | 2007 a 2025 |
| `outros` | `OUTROS` | texto | Sinais e Sintomas Outros. Informar se o paciente apresenta outros sinais e sintomas | 1-Sim 2-Não 9-Ignorado | 2007 a 2025 |
| `outros_esp` | `OUTROS_ESP` | texto | Sinais e Sintomas Outros (especificação). _outro | — | 2007 a 2025 |
| `diag_par_n` | `DIAG_PAR_N` | texto | Diagnóstico Parasitológico. arasitologico | 1. Positivo 2. Negativo 3. Não realizado | 2007 a 2025 |
| `entrada` | `ENTRADA` | texto | Tipo de entrada | 1. Caso novo 2. Recidiva 3. Transferência 9. Ignorado | 2007 a 2025 |
| `tratamento` | `TRATAMENTO` | data | Data do início do tratamento | — | 2007 a 2025 |
| `peso` | `PESO` | inteiro | Peso. Informar o peso do paciente em Kg | — | 2007 a 2025 |
| `dose` | `DOSE` | texto | Dose Prescrita em mg/kg/dia Sb+5. a | 1. Maior ou igual a 10 e menor que 15 2. Maior ou igual a 15 e menor que 20 3. Maior ou igual a 20 | 2007 a 2025 |
| `ampolas` | `AMPOLAS` | inteiro | Nº total de ampolas prescritas. _pescrita | — | 2007 a 2025 |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final | 1. Confirmado 2. Descartado | 2007 a 2025 |
| `criterio` | `CRITERIO` | texto | Critério de confirmação | — | 2007 a 2025 |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é. Tp_autoctone_re | 1 – Sim | 2007 a 2025 |
| `coufinf` | `COUFINF` | texto | Local provável da fonte de infecção UF. o | — | 2007 a 2025 |
| `copaisinf` | `COPAISINF` | texto | Local provável da fonte de infecção País | — | 2007 a 2025 |
| `comuninf` | `COMUNINF` | texto | Local provável da fonte de infecção Município | — | 2007 a 2025 |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho | 1. Sim 2. Não 9. Ignorado | 2007 a 2025 |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso | 1. Cura 2. Abandono 3. Óbito por LV 4. Óbito por outras causas 5. Transferênci a | 2007 a 2025 |
| `dt_obito` | `DT_OBITO` | data | Data do óbito. Informar a data do óbito | — | 2007 a 2025 |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento | — | 2007 a 2025 |
| `dt_deslc1` | `DT_DESLC1` | data | Informações complementares Data 1. Informações complementares e observações Deslocamento(datas e locais freqüentados nos últimos seis meses anterior ao início dos sinais e sintomas) Data | — | 2007 a 2025 |
| `ds_mun_1` | `DS_MUN_1` | texto | Informações complementares Local/Município 1. cal_municipio _1 | — | 2007 a 2025 |
| `co_uf_1` | `CO_UF_1` | texto | Informações complementares UF 1. _1 | — | 2007 a 2025 |
| `co_pais_1` | `CO_PAIS_1` | inteiro | Informações complementares País 1. ca_1 | — | 2007 a 2025 |
| `ds_trans_1` | `DS_TRANS_1` | texto | Informações complementares Meio de transporte 1. porte_1 | — | 2007 a 2025 |
| `dt_deslc2` | `DT_DESLC2` | data | Informações complementares Data 2. Informações complementares e observações Deslocamento(datas e locais freqüentados nos últimos seis meses anterior ao início dos sinais e sintomas) Data | — | 2007 a 2025 |
| `ds_mun_2` | `DS_MUN_2` | texto | Informações complementares Local/Município 2. cal_municipio _2 | — | 2007 a 2025 |
| `co_uf_2` | `CO_UF_2` | texto | Informações complementares UF 2. _2 | — | 2007 a 2025 |
| `co_pais_2` | `CO_PAIS_2` | inteiro | Informações complementares País 2. ca_2 | — | 2007 a 2025 |
| `ds_trans_2` | `DS_TRANS_2` | texto | Informações complementares Meio de transporte 2. porte_2 | — | 2007 a 2025 |
| `dt_deslc3` | `DT_DESLC3` | data | Informações complementares Data 3. Informações complementares e observações Deslocamento (datas e locais freqüentados nos últimos seis meses anterior ao início dos sinais e sintomas) Data | — | 2007 a 2025 |
| `ds_mun_3` | `DS_MUN_3` | texto | Informações complementares Local/Município 3. cal_municipio _3 | — | 2007 a 2025 |
| `co_uf_3` | `CO_UF_3` | texto | Informações complementares UF 3. _3 | — | 2007 a 2025 |
| `co_pais_3` | `CO_PAIS_3` | inteiro | Informações complementares País 3. ca_3 | — | 2007 a 2025 |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | só em 2025 |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | só em 2025 |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | só em 2025 |
| `dt_transrm` | `DT_TRANSRM` | nulo (vazio nas amostras) | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | só em 2025 |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | só em 2025 |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | só em 2025 |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | só em 2025 |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | só em 2025 |
| `ident_micr` | `IDENT_MICR` | texto | Identificação do micro (campo interno) | — | só em 2025 |
| `ds_trans_3` | `DS_TRANS_3` | texto | Informações complementares Meio de transporte 3. porte_3 | — | só em 2025 |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | só em 2025 |

## No lake

- **Dataset no lake:** `datasus/sinan-leiv`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 17, inteiro: 6, nulo (vazio nas amostras): 7, texto: 90.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-leiv.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- casos de LV podem ter demora de encerramento de vários anos (tratamento prolongado e revisão), de modo que consolidações antigas podem ser corrigidas em republicações; por fim, o agravo não tem arquivo anual em `PRELIM` no inventário atual — recomenda-se sempre verificar com `quantilica datasus list sinan-leiv`; códigos de evolução de LV incluem abandono e mudança de diagnóstico, invisíveis nos agravos agudos. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas vazias nas amostras:** `dt_transrm` (tipo nulo: todas as linhas amostradas vieram vazias). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Colunas que não existem em todo o período:** 86 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-leiv").glob("**/*.parquet"))
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
datasus-fetcher list sinan-leiv

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-leiv -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-leiv
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Leishmaniose Visceral (ficha/dicionário unidades de saúde)**: https://portalsinan.saude.gov.br/leishmaniose-visceral
- **Nota técnica e Manual de Vigilância e Controle da Leishmaniose Visceral (SVSA/MS)**
- **Portaria GM/MS nº 204/2016** (notificação compulsória)
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
