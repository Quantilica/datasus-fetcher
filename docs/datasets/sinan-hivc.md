---
dataset:
  id: sinan-hivc
  fonte: datasus
  titulo: HIV em crianças
  resumo: 'HIV em crianças do DATASUS: uma ficha de notificação/investigação de hIV em crianças.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: '2024'
  unidade: uma ficha de notificação/investigação de hIV em crianças
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 105
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    idade_mae: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# HIV em crianças (`sinan-hivc`)

## Resumo

Notificações de infecção pelo HIV em crianças (menores de 13 anos), registradas no SINAN. Cada linha representa uma ficha de notificação/investigação de uma criança com infecção confirmada pelo HIV.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `HIVC` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `HIVC` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `HIVCBR24.dbc`, em que `HIVC` é o prefixo do agravo, `BR` indica a base nacional (o SINAN publica um único arquivo por ano para o Brasil) e `24` é o ano com 2 dígitos (2024).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-hivc/<AAAA>/sinan-hivc_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-hivc/2024/sinan-hivc_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
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
  - O dicionário de dados desta base (`Ficha de Investigação HIV Criança`) está contido em `Docs_TAB_SINAN.zip`; os dicionários por agravo não são publicados como arquivos separados.

## Conteúdo

Faz parte do conjunto de fichas de HIV do SINAN, de notificação compulsória desde 2013-2014 (Portaria SVS/MS nº 29/2013), sob responsabilidade do DATHI/SVSA. Distingue-se de `sinan-hive`, que reúne crianças apenas expostas ao HIV, e de `sinan-aidc`, que registra os casos que atingiram critério de AIDS.

O evento gerador é o diagnóstico de infecção pelo HIV em criança, segundo os algoritmos pediátricos (testes de carga viral/DNA pró-viral em menores de 18 meses). A unidade de análise é o caso notificado, com campos de exposição (em geral transmissão vertical), dados da mãe, profilaxias recebidas e evolução.

O FTP traz arquivos nacionais anuais de 2007 a 2024, com volume mínimo (cerca de 150 KB no total). Séries confiáveis dependem da implantação da notificação a partir de 2014.

Usos: monitoramento da transmissão vertical, taxa de detecção em menores de 5 anos, tempo até o diagnóstico e avaliação do cuidado pediátrico, em conjunto com `sinan-hive` e `sinan-hivg`.

### Cobertura observada

- Índice do FTP (2026-10): 18 arquivos, de 2007 a 2024, 1 UF(s) com arquivos, última atualização em 2025-02-24.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2024), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo real `HIVCBR24.dbc` do FTP (campos da ficha do SINAN Net; o leiaute pode variar entre anos). Os microdados públicos não trazem número de notificação nem data de nascimento completa, apenas campos não identificáveis. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

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
| `IDADE_MAE` | Inteiro | Idade da mãe (anos). |
| `ESC_MAE_N` | String | Escolaridade da mãe. |
| `RACA_MAE` | String | Raça/cor da mãe. |
| `ID_OCUP_MA` | String | Ocupação da mãe (CBO, 6 dígitos). |
| `TIPO_INVES` | String | Tipo de investigação (criança exposta/infectada). |
| `ANT_PERINA` | String | Antecedente de transmissão perinatal. |
| `LAB_TRIAGE` | String | Realização de teste de triagem laboratorial. |
| `CONFIRMA` | String | Realização de teste confirmatório. |
| `DTCONFIRMA` | Data (AAAAMMDD) | Data do teste confirmatório. |
| `LAB_PCR_1` | String | Realização da 1ª carga viral/PCR. |
| `DT_PCR_1` | Data (AAAAMMDD) | Data da 1ª PCR. |
| `CLI_TUBERC` | String | Manifestação clínica: tuberculose. |
| `CRI_1500` | String | Critério laboratorial de contagem de linfócitos (limiar 1500). |
| `EVO_DIAG` | String | Evolução do diagnóstico (criança). |
| `EVOLUCAO` | String | Evolução do caso. |
| `EVO_DT_OBI` | Data (AAAAMMDD) | Data do óbito. |
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
| `idade_mae` | `IDADE_MAE` | inteiro | Idade da mãe. Idade da mãe no momento do diagnóstico | — | todos |
| `esc_mae_n` | `ESC_MAE_N` | texto | Escolaridade da mãe. Escolaridade da mãe no momento da notificação do caso | 0 – Analfabeto 1 –Até 4ª série incompleta do EF 2 – Até 4ª série completa do EF 3 – 5 a 8ª série incompleta do EF 4 – Ensino fundamental completo 5 – Ensino médio incompleto 6 – Ensino médio completo 7 – Educação supe... | todos |
| `raca_mae` | `RACA_MAE` | texto | Raça/cor da mãe. Considera-se na seleção das categorias a cor ou raça declarada pela mãe. 1 – Branca 2 – Preta 3 – Amarela (pessoa que se declarou de raça amarela) 4 – Parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5 – Indígena (pessoa que se declarou indígena ou índia) | 1 – Branca 2 – Preta 3 – Amarela 4 – Parda 5 – Indígena 9 – Ignorado | todos |
| `id_ocup_ma` | `ID_OCUP_MA` | texto | Ocupação da mãe. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo de atividade econômica do paciente refere-se as atividades econômicas desenvolvidas nos processos de produção do setor primário (agricultura e extrativismo); secundário (indústria) ou terciário (serviços e comércio) | — | todos |
| `tipo_inves` | `TIPO_INVES` | texto | Tipo de investigação. Caso de aids em menores de 13 anos de idade | 2 – Aids em menores de 13 anos | todos |
| `ant_perina` | `ANT_PERINA` | texto | Transmissão vertical. Registra se o provável modo de transmissão foi por transmissão vertical | 1 – Sim 2 – Não foi transmissão vertical 9 – Ignorado | todos |
| `ant_rel_n` | `ANT_REL_N` | texto | Transmissão sexual. Registra se o provável modo de transmissão foi sexual | 1 – Relações sexuais só com homens 2 – Relações sexuais só com mulheres | todos |
| `ant_droga` | `ANT_DROGA` | texto | Transmissão sanguínea Uso de drogas injetáveis. Registra se o provável modo de transmissão foi o uso de drogas injetáveis | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_t_hemo` | `ANT_T_HEMO` | texto | Transmissão sanguínea Tratamento para hemofilia. Registra se o provável modo de transmissão foi tratamento/hemotransfusão para hemofilia | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_trans_` | `ANT_TRANS_` | texto | Transmissão sanguínea Transfusão sanguínea. Registra se o provável modo de transmissão foi transfusão sanguínea | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_aciden` | `ANT_ACIDEN` | texto | Transmissão sanguínea Acidente com material biológico com posterior soroconversão até 6 meses | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `antdttrans` | `ANTDTTRANS` | nulo (vazio nas amostras) | Data da transfusão / acidente. Data em que ocorreu a transfusão sanguínea ou acidente com material biológico | — | todos |
| `antuftrans` | `ANTUFTRANS` | texto | UF. Unidade Federada em que ocorreu a transfusão sanguínea ou acidente com material biológico | — | todos |
| `antmuntran` | `ANTMUNTRAN` | texto | Município onde ocorreu transfusão / acidente. Município onde ocorreu a transfusão sanguínea ou acidente com material biológico | — | todos |
| `ant_invest` | `ANT_INVEST` | texto | Após investigação realizada conforme algoritmo do PN DST/AIDS, a transfusão/acidente com material biológico foi considerada causa da infecção pelo HIV?. Registrar, após investigação realizada conforme normas técnicas do Ministério da Saúde, se a transfusão ou acidente com material biológico foi a causa da infecção pelo HIV | 1 – Sim 2 – Não 3 – Não se aplica | todos |
| `lab_triage` | `LAB_TRIAGE` | texto | Evidência laboratorial de infecção pelo HIV Teste de triagem. Resultado do teste de triagem Anti-HIV após os 18 meses de vida | 1 – Positivo/reagente 2 – Negativo/não reagente 3 – Inconclusivo 4 – Não realizado | todos |
| `dt_tria_11` | `DT_TRIA_11` | data | Data da coleta do Teste de triagem. Informar a data da coleta do Teste de triagem | — | todos |
| `confirma` | `CONFIRMA` | texto | Evidência laboratorial de infecção pelo HIV (Teste confirmatório anti- HIV após 18 meses de vida). Resultado do teste confirmatório anti-HIV após 18 meses de vida | 1 – Positivo/reagente 2 – Negativo/não reagente 3 – Inconclusivo 4 – Não realizado 9 – Ignorado | todos |
| `dtconfirma` | `DTCONFIRMA` | data | Data da coleta do Teste Confirmatório. Informar a data da coleta do Teste Confirmatório | — | todos |
| `tprapido1` | `TPRAPIDO1` | texto | Teste rápido 1. Registrar o resultado dos testes rápidos que foram realizados segundo algoritmo de testes validado pelo Ministério da Saúde de acordo com a Portaria nº. 34/SVS/MS, de julho de 2005 | 1 – Positivo/reagente 2 – Negativo/não reagente 3 – Inconclusivo 4 – Não realizado 9 – Ignorado | todos |
| `tprapido2` | `TPRAPIDO2` | texto | Teste rápido 2 | 1 – Positivo/reagente 2 – Negativo/não reagente 3 – Inconclusivo 4 – Não realizado 9 – Ignorado | todos |
| `tprapido3` | `TPRAPIDO3` | texto | Teste rápido 3 | 1 – Positivo/reagente 2 – Negativo/não reagente 3 – Inconclusivo 4 – Não realizado 9 – Ignorado | todos |
| `dtrapido1` | `DTRAPIDO1` | data | Data de realização dos exames. Informar a data de realização do exame | — | todos |
| `lab_pcr_1` | `LAB_PCR_1` | texto | Evidência laboratorial de infecção pelo HIV (1º teste de detecção de ácido nucléico) | 6 – Detectável 7 – Indetectável 4 – Não realizado 9 – Ignorado | todos |
| `dt_pcr_1` | `DT_PCR_1` | data | Data da coleta do 1° Teste de detecção de ácido nucléico. Informar a data da coleta do 1° Teste de detecção de ácido nucléico | — | todos |
| `lab_pcr_2` | `LAB_PCR_2` | texto | Evidência laboratorial de | 6 – Detectável | todos |
| `dt_pcr_2` | `DT_PCR_2` | data | Data da coleta do 2° Teste de detecção de ácido nucléico. Informar a data da coleta do 2° Teste de detecção de ácido nucléico | — | todos |
| `lab_pcr_3` | `LAB_PCR_3` | texto | Evidência laboratorial de infecção pelo HIV (3º teste de detecção de ácido nucléico) | 6 – Detectável 7 – Indetectável 4 – Não realizado 9 – Ignorado | todos |
| `dt_pcr_3` | `DT_PCR_3` | data | Data da coleta do 3° Teste de detecção de ácido nucléico. Informar a data da coleta do 3° Teste de detecção de ácido nucléico | — | todos |
| `cli_paroti` | `CLI_PAROTI` | texto | Aumento crônico de parótida | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_derma` | `CLI_DERMA` | texto | Dermatite persistente | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_esplen` | `CLI_ESPLEN` | texto | Esplenomegalia | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_hepato` | `CLI_HEPATO` | texto | Hepatomegalia | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_otite` | `CLI_OTITE` | texto | Infecções persistentes ou recorrentes de VAS (Otite ou Sinusite) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_linfa` | `CLI_LINFA` | texto | Linfadenopatia >= 0.5 cm em mais de 2 sítios | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_anemia` | `CLI_ANEMIA` | texto | Anemia por mais de 30 dias | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `clicdcca_n` | `CLICDCCA_N` | texto | Candidose de esôfago | 1 – Sim | todos |
| `cli_pulmao` | `CLI_PULMAO` | texto | Candidose de traquéia, brônquios ou pulmões | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_candia` | `CLI_CANDIA` | texto | Candidose oral resistente ao tratamento | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_ci` | `CLI_CDC_CI` | texto | Citomegalovirose (qualquer outro local que não fígado, baço ou linfonodo > 1 mês de idade). Citomegalovirose | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdccre` | `CLI_CDCCRE` | texto | Criptococose (extra- pulmonar). Criptococose (extrapulmonar) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_cr` | `CLI_CDC_CR` | texto | Criptosporidiose com diarréia. Criptosporidíase | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cronic` | `CLI_CRONIC` | texto | Diarréia recorrente ou crônica | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_en` | `CLI_CDC_EN` | texto | Encefalopatia pelo HIV | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_febre` | `CLI_FEBRE` | texto | Febre persistente > 1 mes | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_ge` | `CLI_CDC_GE` | texto | Gengivo-Estomatite Herpética Recorrente (mais de dois episódios em um ano) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_hepati` | `CLI_HEPATI` | texto | Hepatite por HIV | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_herpeg` | `CLI_HERPEG` | texto | Herpes zoster (ao menos 2 episódios distintos ou em mais de um dermátomo) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_he` | `CLI_CDC_HE` | texto | Herpes Simples muco- cutâneo > 1 mês em crianças > 1 mês | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_herpes` | `CLI_HERPES` | texto | Herpes Simples em brônquios, pulmões ou trato gastrintestinal | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_hi` | `CLI_CDC_HI` | texto | Histoplasmose Disseminada | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_in` | `CLI_CDC_IN` | texto | Infecções Bacterianas de Repetição/Múltiplas (pneumonia, abcessos em órgãos internos, infecções osteoarticulares). Infecções bacterianas de repetição/múltiplas (pneumonia, abcessos em orgãos internos, infecções ósteo-articulares) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_infcit` | `CLI_INFCIT` | texto | Infecção por citomegalovírus < 1 mês de idade | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_is` | `CLI_CDC_IS` | texto | Isosporidiose intestinal crônica, por um período superior a 1 mês. Isosporídiose intestinal crônica, por um período superior a 1 mês | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_leiomi` | `CLI_LEIOMI` | texto | Leiomiossarcoma | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_le` | `CLI_CDC_LE` | texto | Leucoencefalopatia Multifocal Progressiva | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_linfo` | `CLI_LINFO` | texto | Linfopenia por mais de 30 dias | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdclih` | `CLI_CDCLIH` | texto | Linfoma não Hodgkin e | 1 – Sim | todos |
| `cli_cdc_li` | `CLI_CDC_LI` | texto | Linfoma Primário de Cérebro. Linfoma Primário de cerébro | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_miocar` | `CLI_MIOCAR` | texto | Miocardiopatia | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_mi` | `CLI_CDC_MI` | texto | Micobacteriose Disseminada (exceto tuberculose e hanseníase) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_me` | `CLI_CDC_ME` | texto | Meningite Bacteriana, pneumonia ou Sepse (único episódio). Meningite bacteriana ou sepse (único episódio) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_nefro` | `CLI_NEFRO` | texto | Nefropatia | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_nocar` | `CLI_NOCAR` | texto | Norcardiose. Norcadiose | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_pn` | `CLI_CDC_PN` | texto | Pneumonia Linfóide Intersticial | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_pc` | `CLI_CDC_PC` | texto | Pneumonia por P.carinii. Pneumonia por P. Carinii | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_sa` | `CLI_CDC_SA` | texto | Salmonelose (sepse ou septicemia recorrente não-tifóide). Salmonelose (Sepse ou septicemia recorrente não- tifóide) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_sk` | `CLI_CDC_SK` | texto | Sarcoma de Kaposi | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_cdc_si` | `CLI_CDC_SI` | texto | Síndrome da Emaciação (AIDS Wasting. Síndrome da Emaciação (Aids Wasting Syndrome) | 1 – Sim 2 – Não | todos |
| `cli_cdc_to` | `CLI_CDC_TO` | texto | Toxoplasmose Cerebral em crianças com mais de 1 mês de idade. Toxoplasmose Cerebral | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_tox1m` | `CLI_TOX1M` | texto | Toxoplasmose iniciada antes de 1 mês de idade | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_tupulm` | `CLI_TUPULM` | texto | Trombocitopenia por mais de 30 dias | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_tuberc` | `CLI_TUBERC` | texto | Tuberculose pulmonar | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_dissem` | `CLI_DISSEM` | texto | Tuberculose Disseminada ou Extrapulmonar | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cli_varice` | `CLI_VARICE` | texto | Varicela disseminada | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cri_1500` | `CRI_1500` | texto | Achados laboratoriais (contagem de linfócitos T DC4 + definidora de imunodeficiência de acordo com a idade) < 1500 células por mm3 (<25%). < 1500 células por mm3 (<25%) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cri_1000` | `CRI_1000` | texto | Achados laboratoriais (contagem de linfócitos T DC4 + definidora de imunodeficiência de acordo com a idade) < 1000 células por mm3 (<25%). Critério CDC < 1000 células por mm3 (<25% | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `cri_500` | `CRI_500` | texto | Achados laboratoriais (contagem de linfócitos T. Critério CDC < 500 células por mm3 (<25%) | 1 – Sim 2 – Não | todos |
| `evo_diag` | `EVO_DIAG` | texto | Critério óbito Declaração de óbito com menção de aids, ou HIV e causa de morte associada a imunodeficiência, sem classificação por outro critério após investigação | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `tra_uf` | `TRA_UF` | texto | UF. Nome da unidade federada onde se realiza o tratamento | — | todos |
| `tra_munici` | `TRA_MUNICI` | texto | Município onde se Realiza o Tratamento. Nome do município onde se realiza o tratamento | — | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso | 1 – Vivo 2 – Óbito por Aids 3 – Óbito por outras causas 9 – Ignorado | todos |
| `evo_dt_obi` | `EVO_DT_OBI` | data | Data do óbito. Data do óbito do paciente | — | todos |
| `criterio` | `CRITERIO` | texto | Critério de definição de caso | 100 – CDC adaptado 600 – Critério óbito 900 – Descartado 901 – HIV+ | todos |
| `ant_cat_ex` | `ANT_CAT_EX` | texto | Categoria de exposição | 10 – Homossexual 11 – Homo/Drogas 12 – Homo/Hemofilico 13 – Homo/transfusão 14 – Homo/Droga/Hemof 15 – Homo/Droga/Transf 20 – Bissexual 21 – Bi/Drogas | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-hivc`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 9, inteiro: 2, nulo (vazio nas amostras): 9, texto: 93.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-hivc.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- Poucos registros por ano; evitar recortes municipais sem agregação. Verificar duplicidade com `sinan-aidc` ao somar casos (uma criança pode aparecer como HIV e depois como AIDS). Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (UF de notificação) ou `SG_UF`/`ID_MN_RESI` (residência) conforme a pergunta, pois os dois podem diferir. Arquivos do diretório PRELIM são preliminares e substituídos pelos finais; prefira sempre os arquivos finais quando o mesmo ano existir nas duas fontes, evitando somar PRELIM e FINAIS. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas vazias nas amostras:** `antdttrans` (tipo nulo: todas as linhas amostradas vieram vazias). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-hivc").glob("**/*.parquet"))
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
datasus-fetcher list sinan-hivc

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-hivc -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-hivc
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS): https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Boletim Epidemiológico de HIV/Aids: https://www.gov.br/aids/pt-br/centrais-de-conteudo/boletins-epidemiologicos
