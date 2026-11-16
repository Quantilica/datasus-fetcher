---
dataset:
  id: sinan-teta
  fonte: datasus
  titulo: Tétano Acidental
  resumo: 'Tétano Acidental do DATASUS: uma ficha de notificação/investigação de tétano Acidental.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de tétano Acidental
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 67
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Tétano Acidental (`sinan-teta`)

## Resumo

O `sinan-teta` contém os microdados das notificações e investigações epidemiológicas de casos de Tétano Acidental (CID-10 A35) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de tétano acidental, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. É uma base de baixa incidência (a doença é evitável por vacinação) mas com leiaute detalhado (66 colunas na v5.0) que documenta a possível porta de entrada do agente (ferimento, queimadura, abortamento séptico, cirurgia), o estado vacinal do paciente, as manifestações clínicas (trismo, riso sardônico, opistótono, rigidez), a profilaxia pós-exposição e o desfecho do caso.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `TETA` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `TETA` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `TETABR25.dbc` — `TETA` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As consolidações até 2023 estão em `FINAIS` e os anos de 2024 a 2026 estão apenas em `PRELIM` (ex.: `TETABR26.dbc`, atualização de 07/10/2026).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-teta/<AAAA>/sinan-teta_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-teta/2024/sinan-teta_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

O tétano acidental é agravo de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, constando hoje da Lista Nacional de Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) em articulação com o GT-SINAN e o Programa Nacional de Imunizações (vacinas DTP/DT/dT/TD e imunização antitetânica). O agravo é distinto do tétano neonatal (dataset `sinan-tetn`), pois monitora casos em qualquer idade com porta de entrada por lesão (excluído o período neonatal e o cordão umbilical); os indicadores oficiais incluem incidência, letalidade e a proporção de casos com esquema vacinal incompleto, bem como a identificação de municípios com falhas de cobertura vacinal — em especial nos grupos vulneráveis (gestantes e idosos).

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Tétano Acidental** do SINAN. A notificação nasce com a suspeição clínica (trismo, riso sardônico, opistótono, rigidez de nuca ou abdômen "em prancha" associada a ferimento nos 21 dias anteriores) e é completada ao longo da investigação com o registro da possível porta de entrada (`TP_CAUSA`, com descrição quando "outros"), o local da lesão (`TP_LOCALLE`), o estado vacinal (`NU_DOSE` e `DT_ULT_DOS`, incluindo "nunca vacinado"), a profilaxia/tratamento específico utilizados (`TP_PROFILA`: soro antitetânico, imunoglobulina, vacina ou antibiótico), as manifestações clínicas e o desfecho do caso (cura, óbito, e o local provável da fonte de infecção). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. Revisões do dicionário datam de fevereiro/2012 e organizaram as opções de dose aplicada, profilaxia e medidas de análise (imunização de pessoas vulneráveis), além dos campos de fonte de infecção (domicílio, trabalho, via pública, escola, campo, unidade de saúde ou outro local: `CS_LOCAL`) e do caso ser autóctone de residência (`TPAUTOCTO`), o que permite estudar o território de exposição.

Aplicações analíticas típicas: incidência e letalidade por faixa etária (adultos idosos concentram os casos); percentual de casos "nunca vacinados" ou com esquema incompleto (`NU_DOSE`); distribuição das portas de entrada e locais de infecção (`TP_CAUSA`, `TP_LOCALLE`, `CS_LOCAL`); uso de profilaxia pós-exposição `SAT/IG`/vacina/antibiótico (`TP_PROFILA`) e estudo da brecha entre ferimento recente (checklist de 21/30 dias) e admissão tardia na rede; e comparativo com o tétano neonatal (`sinan-tetn`) e o tétano por outras causais de outros grupos.

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-10-29.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `TETABR25.dbc` (66 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE do município de notificação e de residência |
| `NU_IDADE_N` | Inteiro composto | Idade (o primeiro dígito indica a unidade: dia/mês/ano) |
| `TP_CAUSA` | Inteiro | Possível causa (porta de entrada): 1 - Injeção, 2 - Laceração, 3 - Queimadura, 4 - Cirúrgico, 5 - Perfuração, 6 - Escoriação, 7 - Abortamento Séptico, 8 - Outros, 9 - Ignorado |
| `TP_CAUSOUT` | String (30) | Descrição da outra possível causa (habilitado se `TP_CAUSA` = 8) |
| `TP_LOCALLE` | Inteiro | Local da lesão: 1 - Membros Inferiores, 2 - Membros Superiores, 3 - Tronco, 4 - Cabeça/Pescoço, 5 - Cavidade Oral, 9 - Ignorado |
| `NU_DOSE` | Inteiro | Nº de doses de vacina (DTP, DT, dT, TT ou tetravalente) recebidas antes da lesão: 1 a 3, 4/5 com reforços, 6 - Nunca vacinado, 9 - Ignorado |
| `DT_ULT_DOS` | Data (`AAAAMMDD`) | Data da última dose da vacina contra tétano |
| `TP_PROFILA` | Inteiro | Tratamento específico/profilaxia utilizada após ferimento: 1 - Soro Antitetânico, 2 - Imunoglobulina, 3 - Vacina, 4 - Antibiótico, 5 - Nenhum |
| `CS_TRISMO`/`CS_RISO`/`CS_OPISTOT`/`CS_NUCA`/`CS_ABDOMIN`/`CS_MEMBROS`/`CS_CRISES`/`CS_SIN_OUT` | Inteiro | Manifestações clínicas: trismo, riso sardônico, opistótono, rigidez de nuca, abdômen em prancha, rigidez de membros, crises, outros sintomas (com descrição em `NM_SIN_OUT`) |
| `TP_ORIGEM` | Inteiro | Origem do caso (notificação por estabelecimento de saúde ou inquérito) |
| `CS_HOSPITA` / `DT_INTERNA` | Inteiro / Data | Internação hospitalar e data de internação |
| `TP_IDENTFI` / `TP_VACINA` / `TP_ANALISE` | Inteiro | Identificação do caso, esquemas vacinais aplicados e imunização/medidas adotadas na população suscetível |
| `CLASSI_FIN` | Inteiro | Classificação final do caso: 1 - Confirmado, 2 - Descartado |
| `CS_LOCAL` | Inteiro | Local provável da fonte de infecção: 1 - Domicílio, 2 - Trabalho, 3 - Via pública, 4 - Escola, 5 - Campo, 6 - Unidade de saúde, 7 - Outro local, 9 - Ignorado |
| `TPAUTOCTO` | Inteiro | O caso é autóctone do município de residência (1 - Sim, 2 - Não, 3 - Indeterminado) |
| `COUFINF`/`COPAISINF`/`COMUNINF` | String/Data | UF, país e municpio prováveis da fonte de infecção (autoctonia) |
| `EVOLUCAO` | Inteiro | Evolução do caso: 1 - Cura, 2 - Óbito por tétano, 3 - Óbito por outras causas, 9 - Ignorado |
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
| `dt_invest` | `DT_INVEST` | data | Data de investigação. Data completa do inicio da investigação iniciada (Data da primeira ação desenvolvida após o conhecimento do caso) | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/ Ramo de Atividade Econômica. Atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última | — | todos |
| `tp_causa` | `TP_CAUSA` | texto | Possível Causa. varcha r2(1) | 1-Injeção 2-Laceração 3-Queimadura 4-Cirúrgico 5-Perfuração 6-Escoriação 7-Abortamento Séptico 8-Outros 9-Ignorado | todos |
| `tp_causout` | `TP_CAUSOUT` | texto | Possível causa Outros (Descrição) | — | todos |
| `tp_localle` | `TP_LOCALLE` | texto | Local da lesão. Local da lesão que provavelmente foi a porta de entrada para o agente etiológico | 1- Membros Inferiores 2- Membros Superiores 3- Tronco 4- Cabeça/ Pescoço 5- Cavidade Oral 9- Ignorado | todos |
| `nu_dose` | `NU_DOSE` | texto | Registro de vacinação (`NU_DOSE`) | — | todos |
| `dt_ult_dos` | `DT_ULT_DOS` | data | Data da última dose. Data da última dose da vacina contra tétano (DPT,DT,dT,TT Tetra) | — | todos |
| `tp_profila` | `TP_PROFILA` | texto | Tratamento específico e outras medidas | 1- Soro Antitetânico 2- Imunoglobulina 3- Vacina 4- Antibiótico 5- Nenhum | todos |
| `cs_trismo` | `CS_TRISMO` | texto | Manifestações clínicas Trismo | 1-Sim 2-Não 9-Ignorado | todos |
| `cs_riso` | `CS_RISO` | texto | Manifestações clínicas Riso sardônico. Se o paciente apresentou riso sarcástico | 1-Sim 2-Não 9-Ignorado | todos |
| `cs_opistot` | `CS_OPISTOT` | texto | Manifestações clínicas Opistótono | 1-Sim 2-Não 9-Ignorado | todos |
| `cs_nuca` | `CS_NUCA` | texto | Manifestações clínicas Rigidez de nuca. a | 1-Sim 2-Não 9-Ignorado | todos |
| `cs_abdomin` | `CS_ABDOMIN` | texto | Manifestações clínicas Rigidez abdominal | 1-Sim 2-Não 9-Ignorado | todos |
| `cs_membros` | `CS_MEMBROS` | texto | Sinais e sintomas Rigidez de membros. Se o recém-nascido apresentou contratura da musculatura das pernas e/ou braços | 1. sim 2. não 9. ignorado | todos |
| `cs_crises` | `CS_CRISES` | texto | Manifestações clínicas Crises de contraturas. e | 1-Sim 2-Não 9-Ignorado | todos |
| `cs_sin_out` | `CS_SIN_OUT` | texto | Manifestações clínicas Outros. o | 1-Sim 2-Não 9-Ignorado | todos |
| `nm_sin_out` | `NM_SIN_OUT` | texto | Manifestações clínicas Outros (Especificar). o | — | todos |
| `tp_origem` | `TP_ORIGEM` | texto | Origem do caso. Identificar se o conhecimento do caso se deu por notificação possível ou por ocasião da busca ativa, ou pela declaração de óbito | 1-Notificação 2-Busca ativa 3-Declaração de óbito | todos |
| `cs_hospita` | `CS_HOSPITA` | texto | Ocorreu hospitalização | 1-Sim 2-Não 9-Ignorado | todos |
| `dt_interna` | `DT_INTERNA` | data | Data da internação. Data de internação, caso tenha ocorrido | — | todos |
| `sg_uf_inte` | `SG_UF_INTE` | texto | UF de hospitalização. Sigla da UF onde o paciente foi internado | — | todos |
| `nm_munic_h` | `NM_MUNIC_H` | texto | Município de hospitalização. Nome do município onde o paciente foi internado | — | todos |
| `tp_identfi` | `TP_IDENTFI` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Tétano Acidental (`TP_IDENTFI`); o dicionário consultado não define o campo isoladamente | — | todos |
| `tp_vacina` | `TP_VACINA` | texto | Medidas de controle Análise de cobertura vacinal por faixa etária. Se foi analisada a cobertura vacinal da população do município em que reside o caso | 1. Sim 2. Não 9. Ignorado | todos |
| `tp_analise` | `TP_ANALISE` | texto | Medidas de controle Vacinação da população suscetível. Se foi realizada vacinação nas pessoas vulneráveis | 1. Sim 2. Não 9. Ignorado | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final. Confirmação do caso ou descarte do suspeito que não atende aos critérios de confirmação após a investigação | 1. Confirmado 2. Descartado | todos |
| `cs_local` | `CS_LOCAL` | texto | Local provável da fonte de infecção. Local onde provavelmente ocorreu a infecção | 1- Domicílio 2- Trabalho 3- Via pública 4- Escola 5- Campo 6- Unidade de saúde 7- Outro local 9- Ignorado | todos |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência? | 1 – Sim 2 – Não 3 – Indeterminado | todos |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o paciente foi provavelmente infectado | — | todos |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente infectado | — | todos |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). o | — | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. Informar como o paciente evoluiu | 1. Cura 2. Óbito por tétano acidental 3. Óbito por outras causas 9. Ignorado | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Data do encerramento da investigação | — | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito. Data de óbito | — | todos |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-teta`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 14, inteiro: 1, nulo (vazio nas amostras): 6, texto: 52.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-teta.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- o código 6 de `NU_DOSE` ("nunca vacinado") deve ser tratado como valor explícito, não nulo; `TP_CAUSOUT`/`NM_SIN_OUT` são campos de texto livre com descrições que demandam revisão ortográfica antes de agregar; o baixo número de casos anuais recomenda tabulações por agregações de anos; e o corte das janelas de 21/30 dias pós-ferimento (história de injeção nas últimas 3 semanas e demais causas nas últimas 4) deve ser replicado manualmente a partir das datas do caso. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-teta").glob("**/*.parquet"))
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
datasus-fetcher list sinan-teta

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-teta -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-teta
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Tétano Acidental (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de tétano acidental e tétano neonatal (eliminação do tétano materno e neonatal)
