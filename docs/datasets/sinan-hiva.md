---
dataset:
  id: sinan-hiva
  fonte: datasus
  titulo: HIV em adultos
  resumo: Notificações de infecção pelo HIV em indivíduos com 13 anos ou mais, registradas no SINAN.
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: '2024'
  unidade: uma ficha de notificação/investigação de hIV em adultos
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 78
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# HIV em adultos (`sinan-hiva`)

## Resumo

Notificações de infecção pelo HIV em indivíduos com 13 anos ou mais, registradas no SINAN. Cada linha representa uma ficha de notificação/investigação de infecção pelo HIV em adulto, independentemente da presença de AIDS.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (dBASE comprimido)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2007 a 2024 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 18 arquivos (~17,6 MB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim (diretório PRELIM)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `HIVA` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `HIVA` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `HIVABR24.dbc`, em que `HIVA` é o prefixo do agravo, `BR` indica a base nacional (o SINAN publica um único arquivo por ano para o Brasil) e `24` é o ano com 2 dígitos (2024).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-hiva/<partição>/sinan-hiva_br_2024_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`):
  - `Docs_TAB_SINAN.zip` — pacote de documentação e dicionários para tabulação (~65 MB)
  - `Nota_Tecnica_Toxoplasmose.pdf` — nota técnica sobre toxoplasmose
  - `POP_I_Acesso_a_Microdados_5.pdf` — POP I: acesso a microdados
  - `POP_II_Descompactacao_expansao_conversao_3.pdf` — POP II: descompactação, expansão e conversão (.dbc → .dbf)
  - `POP_III_Instalacao_do_tabulador_TabWin_3.pdf` — POP III: instalação do TabWin
  - `Nota_Tecnica_Intoxicacao_Exogena.pdf` — nota técnica de intoxicação exógena (agravo de outro dataset do mesmo grupo)
  - Tabelas auxiliares (`/SINAN/AUXILIAR`):
  - `TAB_SINANNET.zip` — tabelas de conversão/tabulação (.cnv, .def) do SINAN Net (~44 MB)
  - `TAB_SINANONLINE.zip` — tabelas do SINAN Online (~240 KB)
  - `POPT_Estimativa_TCU_2019_Sinan.zip` — estimativas populacionais TCU 2019 para uso no SINAN
  - O dicionário de dados desta base (`Ficha de Investigação HIV Adulto`) está contido em `Docs_TAB_SINAN.zip`; os dicionários por agravo não são publicados como arquivos separados.

## Conteúdo

A infecção pelo HIV em adultos, gestantes e crianças expostas passou a ser de notificação compulsória em 2013-2014 (Portaria SVS/MS nº 29/2013), consolidada depois na Portaria de Consolidação GM/MS nº 4/2017 e na lista nacional vigente. A vigilância é conduzida pelo DATHI/SVSA e permite identificar a infecção antes do estágio de AIDS.

O evento gerador é o diagnóstico laboratorial de infecção pelo HIV, notificado em ficha de investigação própria no SINAN. A unidade de análise é a notificação do caso, e os campos incluem dados sociodemográficos, categoria de exposição, resultado de exames, classificação e encerramento. Notificações de gestantes (`sinan-hivg`), crianças expostas (`sinan-hive`) e crianças infectadas (`sinan-hivc`) têm bases separadas.

O arquivo no FTP cobre 2007 a 2024, mas a notificação nacional efetiva só se consolida a partir de 2014. Os anos anteriores trazem registros esparsos, vindos de estados que notificavam antes da obrigatoriedade, e não podem ser lidos como série de incidência.

Usos: taxa de detecção de HIV, perfil sociodemográfico e de exposição, diagnóstico tardio, linkagem com sistemas laboratoriais (SISCEL) e de medicamentos (SICLOM) e planejamento da resposta ao HIV.

### Cobertura observada

- Índice do FTP (2026-10): 18 arquivos, de 2007 a 2024, 1 UF(s) com arquivos, última atualização em 2025-02-24.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2024), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo real `HIVABR24.dbc` do FTP (campos da ficha do SINAN Net; o leiaute pode variar entre anos). Os microdados públicos não trazem número de notificação nem data de nascimento completa, apenas campos não identificáveis. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (individual ou negativa). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado. |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `NU_ANO` | Inteiro | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE). |
| `ID_REGIONA` | String | Regional de saúde de notificação. |
| `DT_DIAG` | Data (AAAAMMDD) | Data do diagnóstico. |
| `SEM_DIAG` | String | Semana epidemiológica do diagnóstico (AAAASS). |
| `NU_IDADE_N` | Inteiro codificado | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_GESTANT` | String | Gestante (trimestre de gestação ou não gestante, conforme a ficha). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade (código da ficha do SINAN). |
| `SG_UF` | String | UF de residência. |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `ID_RG_RESI` | String | Regional de saúde de residência. |
| `ID_PAIS` | String | País de residência. |
| `ID_OCUPA_N` | String | Ocupação (CBO, 6 dígitos). |
| `ANT_TRASMI` | String | Antecedente epidemiológico: categoria de transmissão informada. |
| `ANT_DROGA` | String | Antecedente de uso de drogas injetáveis. |
| `ANTTRANS_M` | String | Antecedente de transmissão: transfusão/hemoderivados. |
| `ANT_ACIDEN` | String | Antecedente de acidente com material biológico. |
| `LAB_TRIAGE` | String | Realização de teste de triagem laboratorial. |
| `DTTRIAGEM` | Data (AAAAMMDD) | Data do teste de triagem. |
| `LAB_CONFIR` | String | Realização de teste confirmatório. |
| `DT_CONFIRM` | Data (AAAAMMDD) | Data do teste confirmatório. |
| `TPRAPIDO1` | String | Resultado do 1º teste rápido. |
| `ANT_TUBERC` | String | Sinal/sintoma ou doença indicativa: tuberculose. |
| `DEF_DIAGNO` | String | Doença definidora diagnosticada. |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito. |
| `CRITERIO` | String | Critério de definição de caso (código de 3 caracteres). |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças – CID 10) e nomes dos agravos classificados como notificação compulsória (nacional, estadual ou municipal) e as síndromes (febre hemorragia aguda; respiratória aguda; diarréia aguda; sanguinolenta; neurológica aguda; insuficiência renal aguda; outras síndromes | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação. Código do município onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. O nome está associado ao código na tabela de municípios | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_diag` | `DT_DIAG` | data | Data dos primeiros sintomas / Diagnóstico. Data dos primeiros sintomas do caso de agravo agudo. Data do diagnóstico do caso de agravo crônico e DRTs Data do acidente nos acidentes da saúde do trabalhador | — | todos |
| `sem_diag` | `SEM_DIAG` | texto | Semana epidemiológica dos primeiros sintomas/ diagnósticos. (campo interno). Semanas do calendário epidemiológico padronizado | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece ao seguinte critério: 1o dígito: 1 – Hora 2 – Dia 3 – Mês 4 – Ano Ex: 3009 – nove meses, 4018 – dezoito anos | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M – Masculino F – Feminino I – Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1 – 1º Trimestre 2 – 2º Trimestre 3 – 3º Trimestre 4 – Idade gestacional ignorada 5 – Não 6 – Não se aplica 9 – Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1 – Branca 2 – Preta 3 – Amarela (pessoa que se declarou de raça amarela) 4 – Parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5 – Indígena (pessoa que se declarou indígena ou índia) | 1 – Branca 2 – Preta 3 – Amarela 4 – Parda 5 – Indígena 9 – Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. Série e grau que a pessoa está frequentando ou frequentou considerando a última série concluída com aprovação ou grau de instrução do paciente por ocasião da notificação | 0 – Analfabeto 1 – 1ª a 4ª série incompleta do EF 2 – 4ª série completa do EF (antigo 1° grau) 3 – 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4 – Ensino fundamental completo (antigo ginásio ou 1° grau)... | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência. Código do município de residência do caso notificado. O nome está associado ao código na tabela de municípios | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil). País onde residia o paciente por ocasião da notificação | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/Ramo de Atividade Econômica. varchar (6) | — | todos |
| `ant_trasmi` | `ANT_TRASMI` | texto | Transmissão Vertical. varchar (1) | 1 – Sim 2 – Não foi transmissão vertical 9 – Ignorado | todos |
| `antrelse_n` | `ANTRELSE_N` | texto | Sexual. Provável modo de transmissão do HIV: sexual | 1 – Relações sexuais com Homens 2 – Relações sexuais com Mulheres 3 – Relações sexuais com homens e mulheres 4 – Não foi transmissão sexual 9 – Ignorado | todos |
| `ant_droga` | `ANT_DROGA` | texto | Sanguínea Uso de Droga injetável. Provável modo de transmissão do HIV: uso de drogas injetáveis | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_hemolf` | `ANT_HEMOLF` | texto | Sanguínea Tratamento/hemotransfusão para hemofilia. Provável modo de transmissão do HIV: tratamento para hemofilia/hemotransfusão | 1 – Sim 2 – Não 3 – Ignorado | todos |
| `anttrans_m` | `ANTTRANS_M` | texto | Sanguínea Transfusão sanguínea. Provável modo de transmissão: transfusão sanguínea | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_aciden` | `ANT_ACIDEN` | texto | Sanguínea Acidente com material biológico com | 1 – Sim 2 – Não | todos |
| `antdttrans` | `ANTDTTRANS` | data | Data da transfusão/acidente | — | todos |
| `antuftrans` | `ANTUFTRANS` | texto | UF | — | todos |
| `antmuntran` | `ANTMUNTRAN` | texto | Município onde foi realizada a transfusão/acidente. Município onde foi realizada a transfusão sanguínea/acidente com material biológico do paciente (código IBGE) | — | todos |
| `ant_invest` | `ANT_INVEST` | texto | Após investigação realizada conforme algoritmo do PN DST/AIDS, a transfusão / acidente com material biológico foi considerada causa da infecção pelo HIV. Registrar, após investigação realizada conforme normas técnicas do Ministério da Saúde, se a transfusão ou acidente com material biológico foi a causa da infecção pelo HIV | 1 – Sim 2 – Não 3 – Não se aplica | todos |
| `lab_triage` | `LAB_TRIAGE` | texto | Evidência laboratorial de infecção pelo HIV (Teste de triagem) | 1 – Positivo / Reagente 2 – Negativo / Não reagente 3 – Inconclusivo 4 – Não realizado 9 – Ignorado | todos |
| `dttriagem` | `DTTRIAGEM` | data | Data da coleta. Informar a data da coleta do teste de triagem | — | todos |
| `lab_confir` | `LAB_CONFIR` | texto | Evidência laboratorial de infecção pelo HIV (Teste confirmatório) | 1 – Positivo / Reagente 2 – Negativo / Não reagente 3 – Inconclusivo 4 – Não realizado 5 – Indeterminado 9 – Ignorado | todos |
| `dt_confirm` | `DT_CONFIRM` | data | Data de coleta. Informar data de coleta do teste confirmatório | — | todos |
| `tprapido1` | `TPRAPIDO1` | texto | Teste rápido 1 | 1 – Positivo / Reagente 2 – Negativo / Não reagente 3 – Inconclusivo | todos |
| `tprapido2` | `TPRAPIDO2` | texto | Teste rápido 2 | 1 – Positivo / Reagente 2 – Negativo / Não reagente 3 – Inconclusivo 4 – Não realizado 9 – Ignorado | todos |
| `tprapido3` | `TPRAPIDO3` | texto | Teste rápido 3 | 1 – Positivo / Reagente 2 – Negativo / Não reagente 3 – Inconclusivo 4 – Não realizado 9 – Ignorado | todos |
| `dt_rapido` | `DT_RAPIDO` | data | Data da coleta dos exames. Informar data de realização dos testes rápidos | — | todos |
| `ant_sarcom` | `ANT_SARCOM` | texto | Critério Rio de Janeiro/Caracas Sarcoma de Kaposi (10). Sarcoma de Kaposi - Pontuação (10) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_tuberc` | `ANT_TUBERC` | texto | Critério Rio de Janeiro/Caracas Tuberculose disseminada/ extra-pulmonar/ não cavitária (10). Tuberculose disseminada/extrapulmonar/ não cavitária - Pontuação (10) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_candid` | `ANT_CANDID` | texto | Critério Rio de Janeiro/Caracas Candidose oral ou leucoplasia pilosa (5). Candidíase Oral ou Leucoplasia Pilosa - Pontuação (5) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_pulmon` | `ANT_PULMON` | texto | Critério Rio de Janeiro/Caracas Tuberculose pulmonar cavitária ou não especificada (5). Tuberculose pulmonar cavitaria ou não especificada - Pontuação (5) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_herpes` | `ANT_HERPES` | texto | Critério Rio de Janeiro/Caracas Herpes Zoster em indivíduo. Herpes Zoster em indivíduo menor ou igual a 60 anos - Pontuação (5) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_disfun` | `ANT_DISFUN` | texto | Critério Rio de Janeiro/Caracas Disfunção do sistema nervoso central (5). Disfunção do sistema nervoso central - Pontuação (5) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_diarre` | `ANT_DIARRE` | texto | Critério Rio de Janeiro/Caracas Diarréia igual ou maior a 1 mês (2). Diarreia igual ou maior que um 1 mês - Pontuação (2) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_febre` | `ANT_FEBRE` | texto | Critério Rio de Janeiro/Caracas Febre maior ou igual a 38ºC por tempo maior ou igual a 1 mês (2). Febre maior ou igual 38º C, por tempo maior ou igual a 1 mês - Pontuação (2) Excluída a tuberculose como causa” | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_caquex` | `ANT_CAQUEX` | texto | Critério Rio de Janeiro/Caracas Caquexia ou perda de peso maior que 10% (2). Caquexia ou pedra de peso maior que 10% - Pontuação (2) Excluída a tuberculose como causa” | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_asteri` | `ANT_ASTERI` | texto | Critério Rio de Janeiro/Caracas Astenia maior ou igual a 1 mês (2). Astenia maior ou igual a 1 mês - Pontuação (2) Excluída a tuberculose como causa” | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_dermat` | `ANT_DERMAT` | texto | Critério Rio de Janeiro/Caracas Dermatite persistente (2). Astenia maior ou igual a 1 mês - Pontuação (2) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_anemia` | `ANT_ANEMIA` | texto | Critério Rio de Janeiro/Caracas Anemia e/ou linfopenia e/ou trombocitopenia (2). Anemia e/ou linfopenia e/ou trombocitopenia - Pontuação (2) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_tosse` | `ANT_TOSSE` | texto | Critério Rio de Janeiro/Caracas Tosse persistente ou. Tosse persistente ou qualquer pneumonia - Pontuação (2) Excluída a tuberculose como causa” | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_linfo` | `ANT_LINFO` | texto | Critério Rio de Janeiro/Caracas Linfadenopatia Maior ou Igual a 1 cm, Maior ou Igual a 2 sítios extra-inquinais por tempo maior ou igual a 1 mês (2). Linfadenopatia maior ou igual a 1 cm, maior ou igual a 2 sítios extra-inquinais por tempo maior ou igual a 1 mês - Pontuação (2) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_cancer` | `ANT_CANCER` | texto | Critério CDC adaptado Câncer cervical invasivo. Câncer cervical invasivo | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_esof_n` | `ANT_ESOF_N` | texto | Critério CDC/ adaptado Candidose Esôfago. Candidose (esôfago, traquéia, brônquios,pulmão) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_pulm_n` | `ANT_PULM_N` | texto | Critério CDC/ adaptado Candidose Traquéia, Brônquio, Pulmão. Candidose (esôfago, traquéia, brônquios,pulmão) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_cito` | `ANT_CITO` | texto | Critério CDC/ adaptado Citomegalovirose (exceto fígado, baço ou linfonodos). Citomegalovirose | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_cripto` | `ANT_CRIPTO` | texto | Critério CDC/ adaptado Criptococose extrapulmonar. Criptococose (Extra-Pulmonar) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_crip_1` | `ANT_CRIP_1` | texto | Critério CDC/ adaptado Criptosporidiose intestinal crônica >1 mês. Criptosporidíase | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_h_simp` | `ANT_H_SIMP` | texto | Critério CDC/ adaptado Herpes Simples mucocutâneo > 1 Mês. Herpes Simples (Muco-Cutâneo > 1 mês, esôfago, brônquios, pulmão) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_histo` | `ANT_HISTO` | texto | Critério CDC/ adaptado Histoplasmose Disseminada. Histoplasmose disseminada | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_isopor` | `ANT_ISOPOR` | texto | Critério CDC/ adaptado. Isosporíase | 1 – Sim | todos |
| `ant_leuco` | `ANT_LEUCO` | texto | Critério CDC/ adaptado Leucoencefalopatia Multifocal Progressiva. Leucoencefalopatia Multifocal Progressiva | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_linfom` | `ANT_LINFOM` | texto | Critério CDC/ adaptado Linfoma Não Hodgkin e outros linfomas. Linfoma não Hodgkin | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_linfo_` | `ANT_LINFO_` | texto | Critério CDC/ adaptado Linfoma Primário do Cérebro. Linfoma Primário do Cérebro | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_micro` | `ANT_MICRO` | texto | Critério CDC/ adaptado Microbacteriose disseminada exceto tuberculose e hanseníase. Micobacteriose Disseminada | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_pneumo` | `ANT_PNEUMO` | texto | Critério CDC/ adaptado Pneumonia por Pneumocystis carinii. Pneumonia por P. Carinii | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_chagas` | `ANT_CHAGAS` | texto | Critério CDC/ adaptado Reativação de doença de Chagas (meningoencefalite e/ou miocardite) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_salmo` | `ANT_SALMO` | texto | Critério CDC/ adaptado Salmonelose (Septicemia Recorrente não-tifóide). Salmonelose (sepcemia recorrente) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_toxo` | `ANT_TOXO` | texto | Critério CDC/ adaptado Toxoplasmose Cerebral. Toxoplasmose cerebral | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_contag` | `ANT_CONTAG` | texto | Critério CDC/ adaptado Contagem de linfócitos T CD4+ menor que 350 cel/mm3 | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `def_diagno` | `DEF_DIAGNO` | texto | Critério óbito. Critério de definição de caso para fins de | 1 – Sim | todos |
| `tra_uf` | `TRA_UF` | texto | UF. Nome da unidade federada onde se realiza o tratamento | — | todos |
| `tra_munici` | `TRA_MUNICI` | texto | Município Onde se Realiza o Tratamento. Nome do município onde se realiza o tratamento | — | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso | 1 – Vivo 2 – Óbito por Aids 3 – Óbito por outras causas 9 – Ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do Óbito. Data do óbito do paciente | — | todos |
| `criterio` | `CRITERIO` | texto | Critério de definição de caso (Campo interno) | 100 – CDC adaptado 300 – Rio de Janeiro/Caracas 600 – Critério óbito 900 – Descartado 901 – HIV+ | todos |
| `ant_rel_ca` | `ANT_REL_CA` | texto | Categoria de exposição (Campo interno). O sistema atribui à categoria de acordo com dados e hierarquia de outros campos relacionados | 10 – Homossexual 11 – Homo/Drogas 12 – Homo/Hemofilico 13 – Homo/transfusão 14 – Homo/Droga/Hemof 15 – Homo/Droga/Transf 20 – Bissexual 21 – Bi/Drogas 22 – Bi/Hemofílico 23 – Bi/Transfusão 24 – Bi/Droga/Hemofílico 25 ... | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-hiva`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 7, inteiro: 1, texto: 70.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-hiva.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- Registros anteriores a 2014 não representam a incidência real, pois a notificação ainda não era obrigatória. Pessoas menores de 13 anos estão em `sinan-hivc`; gestantes vivendo com HIV em `sinan-hivg`. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (UF de notificação) ou `SG_UF`/`ID_MN_RESI` (residência) conforme a pergunta, pois os dois podem diferir. Arquivos do diretório PRELIM são preliminares e substituídos pelos finais; prefira sempre os arquivos finais quando o mesmo ano existir nas duas fontes, evitando somar PRELIM e FINAIS. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-hiva/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-hiva
quantilica datasus list sinan-hiva

# 2. Baixar microdados de sinan-hiva (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-hiva -o ./data --start 2022 --end 2024 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-hiva -o ./data --docs --aux --start 2022 --end 2024 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-hiva -o ./data/raw --parquet-dir ./data/parquet --start 2022 --end 2024 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/HIVABR24.dbc", dataset="sinan-hiva")

# Contagem de notificações por UF de notificação e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Distribuição por cs_sexo, cs_raca
print(frame.group_by("cs_sexo").agg(pl.len().alias("n")).sort("n", descending=True))
print(resumo.head())
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS): https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Boletim Epidemiológico de HIV/Aids: https://www.gov.br/aids/pt-br/centrais-de-conteudo/boletins-epidemiologicos
- Indicadores e dados básicos de HIV/aids: http://indicadores.aids.gov.br/
