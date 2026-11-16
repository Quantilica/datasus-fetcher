---
dataset:
  id: sinan-sifc
  fonte: datasus
  titulo: Sífilis Congênita
  resumo: 'Sífilis Congênita do DATASUS: uma ficha de notificação/investigação de sífilis Congênita.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de sífilis Congênita
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 66
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_idade: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_titu_2: 'número inteiro: contagem ou código numérico (ver Descrição)'
    labc_tit_1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    labc_tit_2: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Sífilis Congênita (`sinan-sifc`)

## Resumo

Notificações de sífilis congênita registradas no SINAN. Cada linha representa uma ficha de notificação de um caso de sífilis congênita, incluindo natimortos e abortos por sífilis, com dados da criança e da mãe.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `SIFC` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `SIFC` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `SIFCBR25.dbc`, em que `SIFC` é o prefixo do agravo, `BR` indica a base nacional (o SINAN publica um único arquivo por ano para o Brasil) e `25` é o ano com 2 dígitos (2025).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-sifc/<AAAA>/sinan-sifc_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-sifc/2024/sinan-sifc_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
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
  - O dicionário de dados desta base (`Ficha de Investigação Sífilis Congênita`) está contido em `Docs_TAB_SINAN.zip`; os dicionários por agravo não são publicados como arquivos separados.

## Conteúdo

A sífilis congênita é de notificação compulsória desde 1986 (Portaria nº 542/1986), sob coordenação do DATHI/SVSA, e é indicador de falha na assistência pré-natal. No SINAN, a ficha reúne dados do recém-nascido e da mãe.

O evento gerador é o nascimento (ou aborto/natimorto) de criança de mãe com sífilis não tratada ou inadequadamente tratada. A unidade de análise é o caso notificado, com campos sobre pré-natal (realização, momento do diagnóstico, esquema de tratamento da mãe e do parceiro), exames da criança, classificação final (sífilis congênita recente, tardia, natimorto, aborto) e evolução.

O FTP traz arquivos nacionais anuais de 2007 a 2025. O aumento da taxa de incidência na década de 2010 foi acompanhado de mudança do critério de definição de caso em 2017, e esse marco deve ser considerado em análises de tendência.

Usos: incidência de sífilis congênita por mil nascidos vivos (denominador do `sinasc`), mortalidade por sífilis congênita, cobertura e adequação do pré-natal e tratamento do parceiro, no Boletim Epidemiológico de Sífilis.

### Cobertura observada

- Índice do FTP (2026-10): 19 arquivos, de 2007 a 2025, 1 UF(s) com arquivos, última atualização em 2026-06-30.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2025), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo real `SIFCBR25.dbc` do FTP (campos da ficha do SINAN Net; o leiaute pode variar entre anos). Os microdados públicos não trazem número de notificação nem data de nascimento completa, apenas campos não identificáveis. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (individual ou negativa). |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
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
| `ANT_IDADE` | Inteiro | Idade da mãe (anos). |
| `ANT_RACA` | String | Raça/cor da mãe. |
| `ID_OCUPA_N` | String | Ocupação da mãe (CBO, 6 dígitos). |
| `ESCOLMAE` | String | Escolaridade da mãe. |
| `ANT_PRE_NA` | String | Realização de pré-natal na gestação atual. |
| `UF_PRE_NAT` | String | UF de realização do pré-natal. |
| `MUN_PRE_NA` | String | Município de realização do pré-natal (código IBGE). |
| `ANTSIFIL_N` | String | Diagnóstico de sífilis materna. |
| `LAB_PARTO` | String | Teste não treponêmico no momento do parto/curetagem. |
| `LAB_TITU_2` | Inteiro | Titulação do teste não treponêmico materno. |
| `LAB_DT3` | Data (AAAAMMDD) | Data do teste não treponêmico materno. |
| `LAB_CONF` | String | Teste treponêmico confirmatório materno. |
| `TRA_ESQUEM` | String | Esquema de tratamento da mãe. |
| `TRA_DT` | Data (AAAAMMDD) | Data do tratamento da mãe. |
| `ANT_TRATAD` | String | Parceiro tratado concomitantemente. |
| `LABC_SANGU` | String | Teste não treponêmico no sangue periférico da criança. |
| `LABC_TIT_1` | Inteiro | Titulação do teste não treponêmico da criança. |
| `LABC_LIQUO` | String | Exame do líquor da criança. |
| `DS_ESQUEMA` | String | Descrição do esquema de tratamento (texto livre). |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito. |
| `EVO_DIAG_N` | String | Diagnóstico final / evolução da criança. |
| `TRA_DIAG_C` | String | Tratamento da criança. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno) | — | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_diag` | `DT_DIAG` | data | Data dos primeiros sintomas / Diagnóstico. Data dos primeiros sintomas do caso de agravo agudo. Data do diagnóstico do caso de agravo crônico e DRTs Data do acidente nos acidentes da saúde do trabalhador | — | todos |
| `sem_diag` | `SEM_DIAG` | texto | Semana epidemiológica dos primeiros sintomas/ diagnósticos. (campo interno). Semanas do calendário epidemiológico padronizado | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil) | — | todos |
| `ant_idade` | `ANT_IDADE` | inteiro | Idade da mãe. Idade da mãe, por ocasião da notificação do caso. Permite digitação | — | todos |
| `ant_raca` | `ANT_RACA` | texto | Raça/cor da mãe. Considera-se na seleção das categorias a cor ou raça declarada pela mãe. 1- branca 2- preta 3- amarela ( pessoa que se declarou de raça amarela) 4- parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) | 1 – branca 2 – preta 3 – amarela 4 – parda 5 – indígena 9 – ignorado | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/ Ramo de Atividade Econômica. e | — | todos |
| `escolmae` | `ESCOLMAE` | texto | Escolaridade da Mãe | 0 – analfabeto 1 – 1ª a 4ª série incompleta do ef 2 – até 4ª série completa do ef 3 – 5 a 8ª série incompleta do ef. 4 – ensino fundamental completo. 5 – ensino médio incompleto. 6 – ensino médio completo. 7 – educaçã... | todos |
| `ant_pre_na` | `ANT_PRE_NA` | texto | Realizou pré-natal na gestação. Informa se a mãe realizou pré-natal durante a gravidez do caso notificado | 1 – sim 2 – não 9 – ignorado | todos |
| `uf_pre_nat` | `UF_PRE_NAT` | texto | UF do Local da realização do Pré-Natal. Informa a UF do local de realização do pré- natal | — | todos |
| `mun_pre_na` | `MUN_PRE_NA` | texto | Município do Local da realização do Pré-Natal | — | todos |
| `antsifil_n` | `ANTSIFIL_N` | texto | Diagnóstico de sífilis materna | 1. durante o pré-natal 2. no momento do parto/curetagem 3. após o parto 4. não realizado 9. ignorado. | todos |
| `lab_parto` | `LAB_PARTO` | texto | Teste não treponêmico no parto/cureta gem. Resultado qualitativo do VDRL materno recomendado na admissão de todas as gestantes para a realização do parto/curetagem | 1 – reagente 2 – não reagente 3 – não realizado 9 – ignorado | todos |
| `lab_titu_2` | `LAB_TITU_2` | inteiro | Resultado teste não treponêmi co no parto/cure tagem – Título. Resultado quantitativo do VDRL materno recomendado na admissão de todas as gestantes para a realização do parto/curetagem | — | todos |
| `lab_dt3` | `LAB_DT3` | data | Data da coleta teste não treponêmi co no parto/cure tagem. Data da coleta do VDRL realizado no momento do parto/curetagem | — | todos |
| `lab_conf` | `LAB_CONF` | texto | Teste confirmatóri o treponêmico no parto /curetagem | 1 – reagente 2 – não reagente 3 – não realizado 9 – ignorado | todos |
| `tra_esquem` | `TRA_ESQUEM` | texto | Esquema de tratamento materno | 1. adequado 2. inadequado 3. não realizado 9. Ignorado | todos |
| `tra_dt` | `TRA_DT` | data | Data do início do tratamento | — | todos |
| `ant_tratad` | `ANT_TRATAD` | texto | Parceiro (s) tratado(s) concomitant. o | 1. sim 2. não 9. ignorado | todos |
| `ant_uf_cri` | `ANT_UF_CRI` | texto | UF. UF de localização da ocorrência do nascimento, aborto ou óbito da criança | — | todos |
| `ant_muni_c` | `ANT_MUNI_C` | texto | Município do Nascimento/ Aborto/Nati morto | — | todos |
| `labc_sangu` | `LABC_SANGU` | texto | Teste não treponêmi co – Sangue Periférico | 1. reagente 2. não reagente 3. não realizado 9. ignorado | todos |
| `labc_tit_1` | `LABC_TIT_1` | inteiro | Título | — | todos |
| `labc_dt_1` | `LABC_DT_1` | data | Data | — | todos |
| `labc_igg` | `LABC_IGG` | texto | Teste treponêmi co após 18 meses | 1. reagente 2. não reagente 3. não realizado 4. não se aplica 9. ignorado | todos |
| `labc_dt` | `LABC_DT` | data | Data | — | todos |
| `labc_liquo` | `LABC_LIQUO` | texto | Teste não treponemi co – Líquor. Resultado qualitativo do teste não treponêmico realizado em amostra de líquor do caso notificado | 1. reagente 2. não reagente 3. não realizado 9. ignorado | todos |
| `labc_tit_2` | `LABC_TIT_2` | inteiro | Título. Resultado quantitativo do teste treponêmico realizado em amostra de líquor do caso notificado | — | todos |
| `labc_dt_2` | `LABC_DT_2` | data | Data. Data da coleta do Teste não treponêmico – Líquor | — | todos |
| `labc_titul` | `LABC_TITUL` | texto | Titulação ascendent e. Titulação ascendente – Refere-se à comparação dos títulos da sorologia não treponêmica da criança após cada teste realizado durante o esquema de seguimento ( VDRL com 1mes, 3, 6 ,12 e 18 meses) | 1. sim 2. não 3. não realizado 9. ignorado | todos |
| `labc_evide` | `LABC_EVIDE` | texto | Evidência de T. pallidum | 1. sim 2. não 3. não realizado 9. ignorado | todos |
| `labc_liq_1` | `LABC_LIQ_1` | texto | Alteração liquórica | 1. sim 2. não 3. não realizado 9. ignorado | todos |
| `tra_diag_t` | `TRA_DIAG_T` | texto | Diagnóstic o radiológic o da criança: Alteração no Exame dos Ossos Longos | 1. sim 2. não 3. não realizado 9. ignorado | todos |
| `tra_esqu_1` | `TRA_ESQU_1` | texto | Esquema de Tratament o. Esquema terapêutico utilizado para o tratamento da sífilis congênita do caso notificado, ao nível hospitalar ou ambulatorial. A Penicilina Cristalina é administrada por via intravenosa, e as Penicilinas Procaína e Benzatina administradas por via intramuscular | 1. penicilina g cristalina 100.000 a 150.000 ui kg / dia / 10 dias 2. penicilina g procaína 50.000 ui kg / dia / 10 dias 3. penicilina g benzatina 50.000 ui kg / dia / dose única 4. outro esquema 5. não realizado 6. n... | todos |
| `ds_esquema` | `DS_ESQUEMA` | texto | Esquema de Tratament o – Outro Esquema | — | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso | 1. vivo 2. óbito por sífilis congênita 3. óbito por outras causas 4. aborto 5. natimorto 9. ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito. Data do óbito da criança | — | todos |
| `evo_diag_n` | `EVO_DIAG_N` | texto | Diagnóstic o Final Campo Interno. Diagnóstico definitivo do caso notificado, segundo o estadiamento do caso.  Sífilis congênita recente: diagnóstico em criança < de 2 anos de idade.  Sífilis congênita tardia: diagnóstico em criança > de 2 anos de idade.  Natimorto com sífilis: perda fetal com mais de 22 semanas de gestação ou >500g de peso;  Aborto por sífilis: perda fetal com <22 semanas de gestação;  Descar... | 1. sífilis congênita recente 2. sífilis congênita tardia 3. aborto 4. natimorto 5. descartado | todos |
| `tra_diag_c` | `TRA_DIAG_C` | texto | Dado do inquérito/tratamento de tracoma (`TRA_DIAG_C`) | — | todos |
| `cli_icteri` | `CLI_ICTERI` | texto | Sinais e sintomas – Icterícia | 1-Sim; 2-Não; 9- Ignorado | todos |
| `cli_rinite` | `CLI_RINITE` | texto | Manifestação clínica registrada na ficha de Sífilis Congênita (`CLI_RINITE`); o dicionário consultado não define o campo isoladamente | — | todos |
| `cli_anemia` | `CLI_ANEMIA` | texto | Anemia por mais de 30 dias | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_esplen` | `CLI_ESPLEN` | texto | Esplenomegalia | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `hepato` | `HEPATO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `cli_osteo` | `CLI_OSTEO` | texto | Manifestação clínica registrada na ficha de Sífilis Congênita (`CLI_OSTEO`); o dicionário consultado não define o campo isoladamente | — | todos |
| `lesoes` | `LESOES` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `cli_outro` | `CLI_OUTRO` | texto | Manifestação clínica registrada na ficha de Sífilis Congênita (`CLI_OUTRO`); o dicionário consultado não define o campo isoladamente | — | todos |
| `sin_outr_e` | `SIN_OUTR_E` | texto | Presença de sinais e sintomas Outro Especificar. a_outro | — | todos |
| `cli_pseudo` | `CLI_PSEUDO` | texto | Sinais e Sintomas (Pseudomembrana) | 1. Sim 2. Não 9. Ignorado | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-sifc`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 8, inteiro: 5, texto: 53.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-sifc.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- A UF/município de residência é da criança (ou da mãe, conforme preenchimento). Usar `sinasc` como denominador pela UF de residência da mãe. Os campos específicos da ficha mudaram com a revisão de 2017. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (UF de notificação) ou `SG_UF`/`ID_MN_RESI` (residência) conforme a pergunta, pois os dois podem diferir. Arquivos do diretório PRELIM são preliminares e substituídos pelos finais; prefira sempre os arquivos finais quando o mesmo ano existir nas duas fontes, evitando somar PRELIM e FINAIS. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-sifc").glob("**/*.parquet"))
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
datasus-fetcher list sinan-sifc

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-sifc -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-sifc
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Boletim Epidemiológico de Sífilis (SVSA/MS): https://www.gov.br/aids/pt-br/centrais-de-conteudo/boletins-epidemiologicos
- Guia de Vigilância em Saúde (SVSA/MS): https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Protocolo Clínico e Diretrizes Terapêuticas para Atenção Integral às Pessoas com IST (MS)
