---
dataset:
  id: sinan-rota
  fonte: datasus
  titulo: Rotavírus
  resumo: O sinan-rota contém os microdados das notificações e investigações epidemiológicas de casos de Rotavírus (Ficha de Vigilância de Rotavírus, CID-10 A08.0) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde.
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2009'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de rotavírus
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
    cs_suspeit: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cs_mening: 'número inteiro: contagem ou código numérico (ver Descrição)'
    id_unidade: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    dt_transrm: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_lote_h: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Rotavírus (`sinan-rota`)

## Resumo

O `sinan-rota` contém os microdados das notificações e investigações epidemiológicas de casos de Rotavírus (Ficha de Vigilância de Rotavírus, CID-10 A08.0) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de rotavirose — fezes coletadas para pesquisa do rotavírus — preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. É a base de vigilância sentinela da doença diarréica por rotavírus, com 73 colunas na série atual: quadro clínico diarreico/vomitivo (com contagem de episódios e duração), alimentação do lactente (leite materno/formula), a vacinação (VOP/VORH, rotavírus — doses, lotes e fabricante), genotipagem de rotavírus (sorotipos G e P), outros enterovírus/bactérias/parasitas e identificação de surtos.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2009 a 2026 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 18 arquivos (~1,4 MB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim (diretório `PRELIM`)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ROTA` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ROTA` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `ROTABR25.dbc` — `ROTA` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). A série em `FINAIS` começa em 2009 e vai até 2024; os anos de 2025 e 2026 estão apenas em `PRELIM` (ex.: `ROTABR26.dbc`, atualização de 30/04/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-rota/<ano>/sinan-rota_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-rota/2026/sinan-rota_preliminar_2026-br@20260430.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip`, as instruções POP_I/II/III de acesso/descompactação e a **`Nota_Tecnica_Rotavirus.pdf`** (nota técnica específica do agravo); em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

A vigilância do rotavírus é operada pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) por meio da vigilância sentinela de gastroenterites (unidades sentinelas de vigilância de rotavírus e laboratórios de referência da Fiocruz), com registro no SINAN desde 2009, em ligação com a rede de vigilância sentinela de rotavírus criada em apoio à introdução da vacina oral de rotavírus humano (VORH) no PNI, em 2006. A base é instrumento central para monitoramento da carga de doença, da circulação de genotipos (G/P) e da efetividade da vacina nos serviços sentinelas. Cada caso é um registro de vigilância sentinela (coleta de fezes de gastroenterites agudas em unidades hospitalares e ambulatórios selecionados) — os totais não representam a incidência endêmica nacional.

O evento gerador deste dataset é a **Ficha de Vigilância de Rotavírus** do SINAN (ficha de rotavírus, integrada ao PNI e com Nota Técnica própria do DATASUS/SVSA). A notificação nasce com a suspeição clínica de gastroenterite aguda em criança (diarreia com sangue, frequência de episódios, febre, vômitos) e a coleta de fezes para pesquisa de rotavírus. A investigação é completada com os dados de alimentação do lactente (`LEITE`, `TIPO_LEITE`), o histórico de vacinação contra rotavírus (doses com lote e fabricante: `VACINA`, `DT_1VAC`, `LOTE1`, `LAB_PROD1`, `DT_2VAC`), o resultado da pesquisa de antígeno/Ac nas fezes (`ROTA_R`, `DT_FEZES`), a genotipagem do vírus (G/P: `GENOT_G`, `GENOT_P`), a pesquisa de co-infecções (`OUT_VIRUS`, `BACTERIA`, `PARASITA`) e o vínculo a surto (`CASO_ISOLA`, `SURTO`).

A série histórica inicia em **2009**: o FTP contém a primeira consolidação em `FINAIS` (2009 a 2024) e os anos de 2025 a 2026 apenas em `PRELIM`. O instrumento é complementado na documentação do FTP pela **Nota Técnica do Rotavírus** (`Nota_Tecnica_Rotavirus.pdf`, no diretório `SINAN/DOCS`), que detalha a definição de caso, as coletas e o encerramento — vigilância sentinela com o rotavírus como causa principal de diarreia em menores de 5 anos, com a vacinação introduzida em 2006 no calendário do PNI.

Aplicações analíticas típicas: percentual de casos positivos para rotavírus nas unidades sentinelas (`ROTA_R`); distribuição de genotipos G/P (`GENOT_G`, `GENOT_P`) e co-infecções com outros vírus/bactérias (`OUT_VIRUS`, `BACTERIA`, `PARASITA`); efetividade vacinal (comparar casos vacinados/não vacinados e doses/lotes `DT_1VAC`/`DT_2VAC`); análise de surtos (`SURTO`) e a casuística por faixa etária (`NU_IDADE_N`) e tipo de alimentação (`LEITE`, `TIPO_LEITE`); o monitoramento da circulação viral e da emergência de novos genotipos — informação central do comitê de vigilância de rotavírus e opções vacinais no calendário.

### Cobertura observada

- Índice do FTP (2026-10): 18 arquivos, de 2009 a 2026, 1 UF(s) com arquivos, última atualização em 2026-04-30.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2009 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `ROTABR25.dbc` (73 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CS_SUSPEIT` / `CS_MENING` | Inteiro | Caso suspeito de rotavirose e manifestações associadas (síndromes agudas) |
| `DT_NOTIFIC` / `SEM_NOT` / `NU_ANO` | Data / Inteiro | Data, semana epidemiológica e ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `DT_SIN_PRI` / `SEM_PRI` | Data / Inteiro | Data e semana de início dos sintomas |
| `NU_IDADE_N` / `CS_SEXO` | Inteiro/String | Idade decomposta por unidade e sexo (casos concentrados em menores de 5 anos) |
| `VOMITO` / `N_VOMITO` / `D_VOMITO` | Inteiro | Vômito presente, número de episódios e duração (dias) |
| `FEBRE` / `T_FEBRE` | Inteiro | Febre presente e duração |
| `DIARREIA` / `N_DIAR` / `D_DIAR` | Inteiro | Diarreia presente, número de episódios e duração (dias) |
| `SANG` | Inteiro | Diarreia com sangue |
| `LEITE` / `TIPO_LEITE` | Inteiro | Tipo de alimentação: leite materno, fórmula (tipo registrado) |
| `VACINA` / `DT_1VAC` / `LOTE1` / `LAB_PROD1` | Inteiro/Data/String | Histórico de vacinação contra rotavírus (VOP/VORH): doses, data da 1ª dose, lote e fabricante |
| `DT_2VAC` / `LOTE2` / `LAB_PROD2` | Data/String | Data, lote e fabricante da 2ª dose |
| `VOP_VORH` / `DT_VOP` | Inteiro/Data | Dose de rotavírus VOP/VORH aplicada e data |
| `DT_FEZES` | Data (`AAAAMMDD`) | Data de coleta de fezes para laboratório |
| `ROTA_R` | Inteiro | Pesquisa de rotavírus nas fezes: resultado (positivo/negativo/em processamento/não realizado) |
| `GENOT_G` / `GENOT_P` | String | Genotipo G e P do rotavírus identificado (tipagem molecular) |
| `OUT_VIRUS` / `NOME_VIRUS` | Inteiro/String | Concomitância de outros vírus e nome do vírus |
| `BACTERIA` / `NOME_BACT` | Inteiro/String | Co-infecção bacteriana e nome |
| `PARASITA` / `NOME_PARAS` | Inteiro/String | Co-infecção parasitária e nome |
| `MEDICAMENT` / `OUT_MEDIC` / `DT_ENVIO` / `ACONDIC` | Inteiro/Data | Medicação prévia, outra medicação, data de envio da amostra e condições de acondicionamento |
| `CLASSI_FIN` | Inteiro | Classificação final do caso |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte |
| `CASO_ISOLA` / `SURTO` | Inteiro | O caso é isolado ou vinculado a surto (1 - Sim, 2 - Não) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito por rotavirose, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` / `DT_ENCERRA` / `DT_DIGITA` | Data (`AAAAMMDD`) | Data do óbito, de encerramento e de digitação |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
| `cs_suspeit` | `CS_SUSPEIT` | inteiro | Suspeita do Agravo. a) Doenças Exantemáticas 1 – Sarampo 2 – Rubéola b) Meningite 1 – Doenças Meningocócicas 2 – Outras Meningites c) AIDS (banco genérico) 1- Criança (<13) 2- Adulto (≥ 13 anos) AIDS (banco DBF) C- Criança (<13) A- Adulto (≥ 13 anos) | — | todos |
| `cs_mening` | `CS_MENING` | inteiro | Tipo de meningite (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno). ds_semana_notifi cacao | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação. co_municipio_not ificacao | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `id_unidade` | `ID_UNIDADE` | inteiro | Unidade de saúde ou outra fonte notificadora. co_unidade_notifi cacao | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico. dt_diagnostico_si ntoma | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno). ds_semana_sinto ma | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência. co_municipio_res idencia | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil). co_pais_residenc ia | — | todos |
| `vomito` | `VOMITO` | texto | Sinais e sintomas Vômito. st_sintoma_vomit o | 1. Sim 2. Não 9. Ignorado | todos |
| `n_vomito` | `N_VOMITO` | texto | Sinais e sintomas Vômito / Número de episódios de vômito. qt_episodio_vomit o | — | todos |
| `d_vomito` | `D_VOMITO` | texto | Sinais e sintomas Vômito / Duração de dias com vômito. Duração de dias com vômito | — | todos |
| `febre` | `FEBRE` | texto | Sinais e sintomas Febre. O paciente teve febre | 1. Sim 2. Não 9. Ignorado | todos |
| `t_febre` | `T_FEBRE` | texto | Tipo ou duração da febre (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `diarreia` | `DIARREIA` | texto | Sinais e sintomas. O paciente teve diarreia | 1. Sim | todos |
| `n_diar` | `N_DIAR` | texto | Sinais e sintomas Diarreia / Número de episódios de diarreia. qt_episodio_diarr eia | — | todos |
| `d_diar` | `D_DIAR` | texto | Sinais e sintomas Diarreia / Duração de dias com diarreia. Duração de dias com diarreia | — | todos |
| `sang` | `SANG` | texto | Presença de sangue nas fezes. st_presenca_san gue | 1. Sim 2. Não 9. Ignorado | todos |
| `leite` | `LEITE` | texto | Aleitamento Materno. st_aleitamento_m aterno | 1. Sim 2. Não | todos |
| `tipo_leite` | `TIPO_LEITE` | texto | Tipo de leite consumido pela criança (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `vacina` | `VACINA` | texto | Vacina contra Rotavírus. st_vacina_rotavir us | 1. Sim 2. Não 9. Ignorado | todos |
| `dt_1vac` | `DT_1VAC` | data | Data da aplicação 1ª dose. dt_aplicacao_dos e_1 | — | todos |
| `lote1` | `LOTE1` | texto | Lote da vacina 1ª dose. Número do lote da vacina 1ª dose | — | todos |
| `lab_prod1` | `LAB_PROD1` | texto | Laboratório produtor 1ª dose. ds_laboratorio_do se_1 | — | todos |
| `dt_2vac` | `DT_2VAC` | data | Data da aplicação 2ª dose. dt_aplicacao_dos e_2 | — | todos |
| `lote2` | `LOTE2` | texto | Lote da vacina 2ª dose. Número do lote da vacina 2ª dose | — | todos |
| `lab_prod2` | `LAB_PROD2` | texto | Laboratório produtor 2ª dose. ds_laboratorio_do se_2 | — | todos |
| `vop_vorh` | `VOP_VORH` | texto | Vacina oral contra poliomielite/rotavírus humano: registro de doses (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_vop` | `DT_VOP` | data | Data da última dose de VOP. dt_ultima_dose_v op | — | todos |
| `dt_fezes` | `DT_FEZES` | data | Data da coleta da amostra de fezes. Data da coleta de Fezes | — | todos |
| `rota_r` | `ROTA_R` | texto | Resultado do teste para rotavírus (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `genot_g` | `GENOT_G` | texto | Qual o genótipo G:. Nome do genótipo G | — | todos |
| `genot_p` | `GENOT_P` | texto | Qual o genótipo P:. Nome do genótipo P | — | todos |
| `out_virus` | `OUT_VIRUS` | texto | Outros vírus identificados na amostra. Se outros vírus identificados na amostra | 1. Sim 2. Não 9. Ignorado | todos |
| `nome_virus` | `NOME_VIRUS` | texto | Se sim, qual. Nome do vírus identificado na amostra | — | todos |
| `bacteria` | `BACTERIA` | texto | Bactéria identificada na amostra. st_bacteria_identi ficada | 1. Sim 2. Não 9. Ignorado | todos |
| `nome_bact` | `NOME_BACT` | texto | Se sim, qual bactéria. ds_bacteria_ident ificada | — | todos |
| `parasita` | `PARASITA` | texto | Parasita identificado na amostra. st_parasita_identi ficado | 1. Sim 2. Não 9. Ignorado | todos |
| `nome_paras` | `NOME_PARAS` | texto | Se sim, qual parasita. ds_parasita_ident ificado | — | todos |
| `medicament` | `MEDICAMENT` | texto | Uso de medicamento antes da coleta. st_uso_medicam ento | 1. Sim 2. Não 9. Ignorado | todos |
| `out_medic` | `OUT_MEDIC` | texto | Se sim, qual?. Nome de outro medicamento antes da coleta | — | todos |
| `dt_envio` | `DT_ENVIO` | data | Data de envio da amostra ao LACEN. dt_envio_amostra _lacen | — | todos |
| `acondic` | `ACONDIC` | texto | Acondicionamento da amostra. st_acondicioname nto_amostra | 1. Sim 2. Não 9. Ignorado | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final. tp_classificacao_f inal | 1. Confirmado 2. Descartado | todos |
| `criterio` | `CRITERIO` | texto | Critério de Confirmação/ Descarte. tp_criterio_confir macao | 1-Laboratorial 2-Clínico Epidemiológico 3- Clínico | todos |
| `caso_isola` | `CASO_ISOLA` | texto | Diarreia por Rotavírus/ Caso isolado. st_diarreia_isolad o | 1. Sim 2. Não | todos |
| `surto` | `SURTO` | texto | Diarreia por Rotavírus/ Surto. Define se o caso faz parte de um surto | 1. Sim 2. Não | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução. Evolução do caso | 1. Cura 2. Óbito por Rotavírus 3. Óbito por outras causas 9. Ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Data do encerramento da investigação | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_transrm` | `DT_TRANSRM` | inteiro | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `nu_lote_h` | `NU_LOTE_H` | inteiro | Número do lote horizontal. nu_lote_horizont al | — | todos |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-rota`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 15, inteiro: 6, nulo (vazio nas amostras): 5, texto: 53.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-rota.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- a base é de **vigilância sentinela** (unidades selecionadas), não universal — os totais não representam a incidência nacional; a genotipagem (`GENOT_G`/`GENOT_P`) é registrada em poucos casos (requer vínculo a laboratório de referência), com frequentes resultados "não realizado"; a efetividade vacinal exige a lógica de doses/lotes e fabricante por dose (`LOTE1`/`LOTE2`, `LAB_PROD1/2`); e há casos com "outros vírus" (`OUT_VIRUS`) investigados como outras etiologias de diarreia. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-rota/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-rota
quantilica datasus list sinan-rota

# 2. Baixar microdados de sinan-rota com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-rota -o ./data --start 2009 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-rota -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-rota -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc(
    "data/sinan-rota/2025/sinan-rota_preliminar_2025-br@20260430.dbc", clean=True
)

# Positividade de rotavírus nas fezes coletadas (vigilância sentinela)
posit = qdf.filter(pl.col("rota_r") == 1).group_by("nu_ano").len().sort("nu_ano")
print(posit)

# Genotipos identificados nas amostras positivas
geno = (
    qdf.filter(pl.col("rota_r") == 1)
    .group_by(["genot_g", "genot_p"])
    .len()
    .sort("genot_g")
)
print(geno)
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Rotavírus (ficha e dicionário de dados)**: https://portalsinan.saude.gov.br
- **Nota Técnica do DATASUS/SVSA sobre Rotavírus** (`Nota_Tecnica_Rotavirus.pdf`, disponível em `SINAN/DOCS`)
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de gastroenterites por rotavírus e vigilância sentinela de doença diarréica aguda
