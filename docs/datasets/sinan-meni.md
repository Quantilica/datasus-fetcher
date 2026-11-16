---
dataset:
  id: sinan-meni
  fonte: datasus
  titulo: Meningite
  resumo: 'Meningite do DATASUS: uma ficha de notificação/investigação de meningite.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de meningite
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 133
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_doses_: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_dose_c: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_dose_4: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_dose_5: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_dose_t: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_dose_7: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cla_sorogr: 'número inteiro: contagem ou código numérico (ver Descrição)'
    med_nucomu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_hema: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_neutro: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_glico: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_leuco: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_eosi: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_prot: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_mono: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_linfo: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_clor: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Meningite (`sinan-meni`)

## Resumo

O `sinan-meni` contém os microdados das notificações e investigações epidemiológicas de casos de Meningite (CID-10 A39, G00, G01, A87, G03 e correlatos) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de meningite, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. Com 132 colunas no leiaute v5.0 é uma das fichas mais extensas do SINAN, cobrindo detalhadamente sinais e sintomas, o extenso bloco laboratorial (punção liquórica, culturas, contraimunoeletroforese/CIE, aglutinação em látex, isolamento viral e PCR) e a classificação final da etiologia — meningocócica, tuberculosa, asséptica, por outras bactérias ou por outra etiologia.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `MENI` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `MENI` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `MENIBR25.dbc` — `MENI` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As consolidações até 2022 estão em `FINAIS` e os anos de 2023 a 2026 estão apenas em `PRELIM` (ex.: `MENIBR26.dbc`, atualização de 21/09/2026).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-meni/<AAAA>/sinan-meni_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-meni/2024/sinan-meni_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

A meningite é agravo de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, e atualmente consta da Lista Nacional de Agravos de Notificação Compulsória consolidada na Portaria GM/MS nº 204/2016. O seguimento da vigilância é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), em articulação com o GT-SINAN e a rede de laboratórios centrais (LACEN e laboratórios de referência nacional, como o Instituto Adolfo Lutz e o FioCruz/RJ), dando suporte à vigilância laboratorial integrada e à avaliação das estratégias de vacinação do PNI (meningocócica C/ACWY/B, pneumocócica e Hib). Como a síndrome pode ser causada por múltiplos agentes (bactérias, vírus, fungos e o bacilo da tuberculose), o SINAN exige o encerramento do caso com a etiologia confirmada por meio do bloco laboratorial — daí a extensão da ficha.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Meningite** do SINAN. A notificação nasce com a suspeição clínica (cefaléia, febre, vômitos, convulsões, rigidez de nuca, sinal de Kernig/Brudzinski, abaulamento de fontanela, coma, petéquias) e é completada com resultados do líquido cefalorraquidiano (aspecto, células, bioquímica) e dos exames microbiológicos por amostra biológica (coprocultura, LATEX aglutinação, CIE, isolamento viral e PCR). A unidade de análise é o caso notificado, com a etiologia definida no encerramento quando aplicável — a investigação orienta ainda a quimioprofilaxia de comunicantes nos casos de doença meningocócica.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. O leiaute manteve-se estável ao longo da série, com revisões pontuais do dicionário (versão revisada em julho/2010) e mudanças de instrumento menos frequentes do que em outras fichas do SINAN, o que facilita a comparabilidade longitudinal. Os campos de antecedentes de vacinação (`ANT_BCG`, `ANT_CONJ_C`, `ANT_TRIPLI`, `ANT_HEMO_T`, `ANT_PNEUMO`) registram dose, lote e data da última dose, permitindo a avaliação de falhas vacinais no suporte das doenças penetrante dos eventos à admissão das fichas de eventos adversos das vacinas de PNI.

Aplicações analíticas típicas: incidência de meningite meningocócica e meningococcemia por faixa etária e UF (base dos dossiês de vacinação ACWY e B); distribuição de etiologias confirmadas (`CON_DIAGES`, `CLA_ME_BAC`/`CLA_ME_ASS`/`CLA_ME_ETI`); formas assépticas virais e tuberculosa; letalidade e hospitalização; percentual de casos com critério laboratorial de confirmação (culturas, LATEX e PCR por líquor e sangue); cobertura de quimioprofilaxia de comunicantes (`MED_NUCOMU`, `MED_QUIMIO`) e curvas epidêmicas por semana de início dos sintomas (`SEM_PRI`).

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-10-29.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `MENIBR25.dbc` (132 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CS_MENING` | Inteiro | Tipo de meningite notificada/investigada conforme Quadro I do dicionário (meningococcemia, meningite meningocócica, tuberculosa asséptica, por outras bactérias etc.) |
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas (base das curvas epidêmicas com `SEM_NOT`/`SEM_PRI`) |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `ID_UNIDADE` | String (7) | Código CNES da unidade notificadora |
| `ANT_AC`/`ANT_CONJ_C`/`ANT_TRIPLI`/`ANT_HEMO_T`/`ANT_PNEUMO` | Inteiro | Antecedentes de vacinação: meningocócica C, conjugada, tríplice bacteriana, Hib (Hemófilo tipo B), pneumocócica (com doses, lote e datas `ANT_DOSE_*`/`ANT_DTUL_*`) |
| `ANT_AIDS`/`ANT_IMUNO`/`ANT_TUBE`/`ANT_TRAUMA`/`ANT_INF_HO` | Inteiro | Antecedentes associados: AIDS, imunodepressão, tuberculose, trauma/extracção, infecção hospitalar, cirurgia prévia, uso de drogas imunossupressoras |
| `CLI_CEFALE`/`CLI_FEBRE`/`CLI_VOMITO`/`CLI_CONVUL`/`CLI_RIGIDE`/`CLI_KERNIG`/`CLI_ABAULA`/`CLI_COMA`/`CLI_PETEQU` | Inteiro | Sinais e sintomas: cefaléia, febre, vômitos, convulsões, rigidez de nuca, Kernig, abaulamento de fontanela, coma e outras manifestações clínicas |
| `ATE_HOSPIT`/`ATE_INTERN` | Inteiro | Hospitalização (local e se houve internação) |
| `LAB_PUNCAO` / `LAB_DTPUNC` | Inteiro / Data | Punção liquórica realizada e data da coleta do líquor |
| `LAB_ASPECT` | Inteiro | Aspecto do líquor (hábito e da investigação: normal, turbido, hemorrágico, coleções fibrinosas) |
| `LAB_CTLIQU`/`LAB_CTLESA`/`LAB_CTSANG`/`LAB_CTESCA` | Inteiro | Culturas (líquor, lesão, sangue, escarro): amostra coletada, em processamento, resultado ou não realizado |
| `LAB_BCLIQU`/`LAB_BCSANG` | Inteiro | Bacterioscopia: 1 = Positiva, 2 = Negativa, 3 = Em processamento, 4 = Não realizado |
| `LAB_AGLIQU`/`LAB_AGSANG` | Inteiro | Aglutinação ou LATEX (líquor, sangue): agente etiológico identificado segundo Quadro X |
| `LAB_ISLIQU`/`LAB_ISFEZE` | Inteiro | Isolamento viral (líquor, fezes): agente etiológico segundo Quadro XI |
| `LAB_PCLIQU`/`LAB_PCLESA`/`LAB_PCSANG`/`LAB_PCESCA` | Inteiro | PCR (líquor, lesão petequial, sangue, escarro): agente etiológico segundo Quadro XII |
| `LAB_HEMA`/`LAB_NEUTRO`/`LAB_GLICO`/`LAB_PROT`/`LAB_CLOR` | Inteiro | Exame do líquor: hemácias/mm3, neutrófilos (%), glicorraquia, proteinorraquia, clororraquia |
| `CLASSI_FIN` | Inteiro | Classificação do caso: 1 - Confirmado, 2 - Descartado |
| `CON_DIAGES` | Inteiro | Se confirmado, especifique a etiologia: 1 - Meningococcemia, 2 - Meningite Meningocócica, 3 - Meningite Meningocócica com Meningococcemia, 4 - Meningite Tuberculosa, 5 - Meningite por outras bactérias, 6 - Meningite não especificada, 7 - Meningite Asséptica, 8 - Meningite por outra etiologia |
| `CLA_ME_BAC`/`CLA_ME_ASS`/`CLA_ME_ETI` | String (4) | Detalhamento da etiologia nos casos 5 (outras bactérias — Quadro II), 7 (asséptica — Quadro III) e 8 (outra etiologia) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial; 2 - Clínico; 3 - Clínico laboratorial aplicado em inquéritos epidemiológicos) |
| `MED_NUCOMU`/`MED_QUIMIO`/`MED_DT_QUI` | Inteiro/Data | Comunicantes identificados, quimioprofilaxia realizada e data do esquema DIM/QP |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito, 3 - Óbito atribuído a outra causa, 9 - Ignorado) |
| `DT_OBITO` / `DT_ENCERRA` | Data (`AAAAMMDD`) | Data do óbito e de encerramento do caso |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
| `cs_mening` | `CS_MENING` | texto | Tipo de meningite (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
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
| `dt_invest` | `DT_INVEST` | data | Data da investigação. data de ínicio da investigação do caso | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo de atividade econômica do paciente refere-se as | — | todos |
| `ant_ac` | `ANT_AC` | texto | Vacinação (Polissacarídica A/C). caridica_ac | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_dose_3` | `ANT_DOSE_3` | texto | Numero de Doses (Polissacarídica A/C). aridica_ac | — | todos |
| `ant_dtul_3` | `ANT_DTUL_3` | data | Data da Ultima Dose (Polissacarídica A/C). aridica_ac | — | todos |
| `ant_bc` | `ANT_BC` | texto | Vacinação (Polissacarídica B/C). caridica_bc | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_doses_` | `ANT_DOSES_` | inteiro | Numero de Doses (Polissacarídica B/C). aridica_bc | — | todos |
| `ant_dtult_` | `ANT_DTULT_` | data | Data da Ultima Dose (Polissacarídica B/C). aridica_bc | — | todos |
| `ant_conj_c` | `ANT_CONJ_C` | texto | Vacinação (Conjugada Meningo C). ada_meningo | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_dose_c` | `ANT_DOSE_C` | inteiro | Numero de Doses (Conjugada Meningo C). da_meningo_c | — | todos |
| `ant_dtul_c` | `ANT_DTUL_C` | data | Data da Ultima Dose (Conjugada Meningo C). a_meningo_c | — | todos |
| `ant_bcg` | `ANT_BCG` | texto | Vacinação (Bcg). informa se o paciente tem história vacinal de BCG | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_dose_4` | `ANT_DOSE_4` | inteiro | Numero de Doses (Contra Bcg). Nº de doses | — | todos |
| `ant_dtul_4` | `ANT_DTUL_4` | data | Data da Ultima Dose (Contra Bcg). data da ultima dose da vacinação BCG | — | todos |
| `ant_tripli` | `ANT_TRIPLI` | texto | Vacinação (Tríplice Viral). informa se o paciente tem história vacinal de Triplice Viral | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_dose_5` | `ANT_DOSE_5` | inteiro | Numero de Doses (Tríplice Viral). Nº de doses da vacina Triplice Viral | — | todos |
| `ant_dtul_5` | `ANT_DTUL_5` | data | Data da Ultima Dose (Tríplice Viral). data da ultima dose da vacinação Tríplice Viral | — | todos |
| `ant_hemo_t` | `ANT_HEMO_T` | texto | Vacinação (Hemófilo – Tetravalente Ou Hib). o | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_dose_t` | `ANT_DOSE_T` | inteiro | Numero de Doses (Hemófilo). Nº de doses da vacina Hemófilos (Tetravalente ou Hib) | — | todos |
| `ant_dtul_t` | `ANT_DTUL_T` | data | Data da Ultima Dose (Hemófilo). data da ultima dose da vacinação Hemófilos (Tetravalente ou Hib) | — | todos |
| `ant_pneumo` | `ANT_PNEUMO` | texto | Vacinação (Pneumococo) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_dose_7` | `ANT_DOSE_7` | inteiro | Numero de Doses (Pneumococo) | — | todos |
| `ant_dtul_7` | `ANT_DTUL_7` | data | Data da Ultima Dose (Pneumococo) | — | todos |
| `ant_outra` | `ANT_OUTRA` | texto | Vacinação (Outra). informa se o paciente tem história vacinal de Outras Vacinas | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ant_ou_de` | `ANT_OU_DE` | texto | Vacinação (Outra) Se outra especificar. informa se o paciente tem história vacinal de Outras Vacinas especificar | — | todos |
| `ant_dtul_8` | `ANT_DTUL_8` | data | Data da Ultima Dose (Outra). data da última dose da vacinação Outra | — | todos |
| `ant_aids` | `ANT_AIDS` | texto | Doenças Pré-Existentes - AIDS/HIV | 1. Sim 2. Não 9.Ignorado | todos |
| `ant_imuno` | `ANT_IMUNO` | texto | Doenças Pré-Existentes – Outras Doenças Imunodepressoras. utra_doenca | 1. Sim 2. Não 9.Ignorado | todos |
| `ant_ira` | `ANT_IRA` | texto | Doenças Pré-Existentes – IRA. a | 1. Sim 2.Não 9.Ignorado | todos |
| `ant_tube` | `ANT_TUBE` | texto | Doenças Pré-Existentes - Tuberculose | 1. Sim 2.Não 9.Ignorado | todos |
| `ant_trauma` | `ANT_TRAUMA` | texto | Doenças Pré-Existentes - Traumatismo | 1. Sim 3. Não 9.Ignorado | todos |
| `ant_inf_ho` | `ANT_INF_HO` | texto | Doenças Pré-Existentes – Infecção Hospitalar | 1. Sim 2.Não 9.Ignorado | todos |
| `ant_outro` | `ANT_OUTRO` | texto | Doenças Pré-Existentes - Outro | 1. Sim 2.Não 9.Ignorado | todos |
| `ant_outr_d` | `ANT_OUTR_D` | texto | Doenças Pré-Existentes (Outro) Especificar. xistente_outro | — | todos |
| `ant_cont_n` | `ANT_CONT_N` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Meningite (`ANT_CONT_N`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_secund` | `ANT_SECUND` | texto | Caso Secundário | 1-sim 2-não 9-Ignorado | todos |
| `cli_cefale` | `CLI_CEFALE` | texto | Sinais e Sintomas (Cefaléia). informa se esta manifestação clínica ocorreu com o paciente | 1-sim 2-não 9-Ignorado | todos |
| `cli_febre` | `CLI_FEBRE` | texto | Sinais e Sintomas (Febre). informa se esta manifestação clínica ocorreu com o paciente | 1-sim 2-não 9-Ignorado | todos |
| `cli_vomito` | `CLI_VOMITO` | texto | Sinais e Sintomas (Vômitos). informa se esta manifestação clínica ocorreu com o paciente | 1-sim 2-não 9-Ignorado | todos |
| `cli_convul` | `CLI_CONVUL` | texto | Sinais e Sintomas (Convulsões) | 1-sim 2-não 9-Ignorado | todos |
| `cli_rigide` | `CLI_RIGIDE` | texto | Sinais e Sintomas (Rigidez de Nuca) | 1-sim 2-não 9-Ignorado | todos |
| `cli_kernig` | `CLI_KERNIG` | texto | Sinais e Sintomas (Kernig/ Brudzinski). informa se esta manifestação clínica ocorreu com o paciente | 1-sim 2-não 9-Ignorado | todos |
| `cli_abaula` | `CLI_ABAULA` | texto | Sinais e Sintomas (Abaulamento de Fontanela) | 1-sim 2-não 9-Ignorado | todos |
| `cli_coma` | `CLI_COMA` | texto | Sinais E Sintomas (Coma). informa se esta manifestação clínica ocorreu com o paciente | 1-sim 2-não 9-Ignorado | todos |
| `cli_petequ` | `CLI_PETEQU` | texto | Sinais e Sintomas (Petéquias/ Sufusões Hemorrágicas) | 1-sim 2-não 9-Ignorado | todos |
| `cli_outras` | `CLI_OUTRAS` | texto | Sinais e Sintomas (Outras). informa se ocorreram outras manifestações clínicas | 1-sim 2-não 9-Ignorado | todos |
| `cli_especi` | `CLI_ESPECI` | texto | Sinais e Sintomas (Outras: Especificar). Especificação de outros sinais e/ou sintomas não listados na ficha | — | todos |
| `ate_hospit` | `ATE_HOSPIT` | texto | Ocorreu Hospitalização | 1-sim 2-não 9-Ignorado | todos |
| `ate_intern` | `ATE_INTERN` | data | Data da Internação | — | todos |
| `ate_uf_hos` | `ATE_UF_HOS` | texto | UF Hospital. Sigla da UF do hospital onde o paciente foi internado | — | todos |
| `ate_munici` | `ATE_MUNICI` | texto | Nome do Município do Hospital | — | todos |
| `lab_puncao` | `LAB_PUNCAO` | texto | Punção Lombar. Informa se foi realizada punção lombar no paciente | 1-sim 2-não 9-ignorado | todos |
| `lab_dtpunc` | `LAB_DTPUNC` | data | Data da Punção. Data da realização da punção lombar | — | todos |
| `lab_aspect` | `LAB_ASPECT` | texto | Aspecto do Líquor. Aspecto do líquor recolhido na punção | 1- Límpido 2- Purulento 3- Hemorrágico 4- Turvo 5- Xantocrômico 6- Outro 9. Ignorado | todos |
| `lab_ctliqu` | `LAB_CTLIQU` | texto | Dado de exame laboratorial registrado na ficha de Meningite (`LAB_CTLIQU`); o dicionário consultado não define o campo isoladamente | — | todos |
| `lab_ctlesa` | `LAB_CTLESA` | texto | Cultura lesão petequial | — | todos |
| `lab_ctsang` | `LAB_CTSANG` | texto | Cultura Sangue/soro. e_soro | — | todos |
| `lab_ctesca` | `LAB_CTESCA` | texto | Cultura escarro. o | — | todos |
| `lab_bcliqu` | `LAB_BCLIQU` | texto | Bacterioscopia líquor | — | todos |
| `lab_bclesa` | `LAB_BCLESA` | texto | Bacterioscopia lesão petequial. ao_petequial | — | todos |
| `lab_bcsang` | `LAB_BCSANG` | texto | Bacterioscopia Sangue/soro. ngue_soro | — | todos |
| `lab_bcesca` | `LAB_BCESCA` | texto | Bacterioscopia escarro | — | todos |
| `lab_ciliqu` | `LAB_CILIQU` | texto | CIE líquor. Colocar o número da etiologia Segundo Quadro IX (anexo) | — | todos |
| `lab_cisang` | `LAB_CISANG` | texto | CIE Sangue/soro | — | todos |
| `lab_agliqu` | `LAB_AGLIQU` | texto | LATEX líquor | — | todos |
| `lab_agsang` | `LAB_AGSANG` | texto | LATEX Sangue/soro. angue_soro | — | todos |
| `lab_isliqu` | `LAB_ISLIQU` | texto | Isolamento viral líquor. al_liquor | — | todos |
| `lab_isfeze` | `LAB_ISFEZE` | texto | Isolamento viral fezes. al_fezes | — | todos |
| `lab_pcliqu` | `LAB_PCLIQU` | texto | PCR líquor. Colocar o número da | — | todos |
| `lab_pclesa` | `LAB_PCLESA` | texto | PCR lesão petequial. torio_lesao | — | todos |
| `lab_pcsang` | `LAB_PCSANG` | texto | PCR Sangue/soro. torio_sangue | — | todos |
| `lab_pcesca` | `LAB_PCESCA` | texto | PCR escarro. torio_escarro | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação do Caso | 1-confirmado 2-descartado | todos |
| `con_diages` | `CON_DIAGES` | texto | Se Confirmado, Especifique | 1-Meningococcemia 2-Meningite Meningocócic a 3-Meningite Meningocócica com Meningococcemia 4-Meningite Tuberculosa 5-Meningite por outras bactérias 6-Meningite não especificada 7-Meningite Asséptica 8-Meningite por ou... | todos |
| `cla_me_bac` | `CLA_ME_BAC` | texto | Se Confirmado, Especifique (5 - Meningite Por Outras Bactérias). varchar (4) | — | todos |
| `cla_me_ass` | `CLA_ME_ASS` | texto | Se Confirmado, Especifique (7 - Meningite Asséptica). varchar (4) | — | todos |
| `cla_me_eti` | `CLA_ME_ETI` | texto | Se Confirmado, Especifique (8 - Meningite de Outra Etiologia). Conforme quadro IV | — | todos |
| `criterio` | `CRITERIO` | texto | Critério de Confirmação | — | todos |
| `cla_sorogr` | `CLA_SOROGR` | inteiro | Se N. Meningiditis Especificar Sorogrupo. Colocar categoria segundo Quadro VI | — | todos |
| `med_nucomu` | `MED_NUCOMU` | inteiro | Número de Comunicantes. número de comunicantes identificados | — | todos |
| `med_quimio` | `MED_QUIMIO` | texto | Realizada Quimioprofilaxia dos Comunicantes. a | 1-sim 2-não 9-ignorado | todos |
| `med_dt_qui` | `MED_DT_QUI` | data | Se sim, data. Data em que foi realizada quimioprofiaxia dos comunicantes | — | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença Relacionada ao Trabalho. o | 1-sim 2-não 9-ignorado | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do Caso | 1-alta 2-óbito por meningite 3-óbito por outra | todos |
| `med_dt_evo` | `MED_DT_EVO` | data | Data da Evolução | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do Encerramento. Data do encerramento do caso | — | todos |
| `lab_hema` | `LAB_HEMA` | inteiro | Exame Quimiocitológico Hemácias | — | todos |
| `lab_neutro` | `LAB_NEUTRO` | inteiro | Exame Quimiocitológico Neutrófilos | — | todos |
| `lab_glico` | `LAB_GLICO` | inteiro | Exame Quimiocitológico Glicose | — | todos |
| `lab_leuco` | `LAB_LEUCO` | inteiro | Exame Quimiocitológico Leucócitos | — | todos |
| `lab_eosi` | `LAB_EOSI` | inteiro | Exame Quimiocitológico Eosinófilos | — | todos |
| `lab_prot` | `LAB_PROT` | inteiro | Exame Quimiocitológico Proteínas | — | todos |
| `lab_mono` | `LAB_MONO` | inteiro | Exame Quimiocitológico Monócitos | — | todos |
| `lab_linfo` | `LAB_LINFO` | inteiro | Exame Quimiocitológico Linfócitos | — | todos |
| `lab_clor` | `LAB_CLOR` | inteiro | Exame Quimiocitológico Cloreto | — | todos |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-meni`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 23, inteiro: 18, nulo (vazio nas amostras): 1, texto: 92.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-meni.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- os campos de etiologia detalhada (`CLA_ME_*`) usam códigos dos Quadros anexos ao dicionário (Quadro II para bactérias, Quadro III para meningite asséptica e Quadros de agentes para isolamento/LATEX/CIE/PCR) e devem ser interpretados em conjunto com `CON_DIAGES`; os campos `LAB_*` registram tanto a coleta da amostra quanto o resultado do exame, o que exige leitura cuidadosa por material biológico; a série inicia em 2007 (não há bases do Sinan-Windows para esse agravo no FTP), facilitando a comparabilidade; e nos registros com `MIGRADO_W` há possíveis informações parciais. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-meni").glob("**/*.parquet"))
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
datasus-fetcher list sinan-meni

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-meni -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-meni
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`

- Portal de Transferência de Arquivos do DATASUS: https://datasus.saude.gov.br/transferencia-de-arquivos/
- TabNet DATASUS: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- Portal SINAN — Meningite (ficha e dicionário de dados v5.0 e REV. julho/2010): https://portalsinan.saude.gov.br
- Portaria GM/MS nº 204/2016 (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- PCDaS/Fiocruz — SINAN: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- Guia de Vigilância em Saúde (SVSA/MS, Ed. atual) — capítulo de doença meningocócica e meningites; Manual dos Serviços de Saúde (MS) sobre manejo e vigilância de meningites
