---
dataset:
  id: sinan-sdta
  fonte: datasus
  titulo: Surto Doenças Transmitidas por Alimentos
  resumo: O sinan-sdta contém os microdados dos inquéritos e planilhas de acompanhamento de surtos de Doenças Transmitidas por Alimentos (DTA — CID-10 A04–A09, inclusive Rotavírus/Norovírus/Adenovírus por veículo comum) registrados no Sistema de Informação de Agravos de
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação de surto de doença transmitida por alimentos
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 106
  unidades_de_medida:
    sem_pri: 'número inteiro: contagem ou código numérico (ver Descrição)'
    dttransrm: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_entr: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ent_doe: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_tot: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_tot_hos: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_obito: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_1_m_nu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_1_4_nu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_5_9_nu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_10_19_m: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_20_49_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_50_m_nu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_igra_nu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_f_tot_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_1_f_nu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu1_4_f_nu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu5_9_f_nu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu10_19_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_20_49_f: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_50_f_nu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ig_f_nu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_to_f_nu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_1_ign: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_1_4_ign: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_5_9_ign: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_10_19ig: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_20_49ig: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_50_ign: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ig_ign: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_tot_ign: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_1_tot_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_1_4_tot: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_5_9_tot: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_10_19: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_20_49: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_50_tot: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ign_nu: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_f_tot: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_nause_p: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_vomto_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_diarr_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_cefal_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_abdom_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_neuro_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_outro_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_febre_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_incub_m: 'número inteiro: contagem ou código numérico (ver Descrição)'
    max_inc: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_inc_me: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_num_3: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_a_num_3: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_a_clini: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_cli_num: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_num_2: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_a_alim: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_a_num_1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_a_num_2: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Surto Doenças Transmitidas por Alimentos (`sinan-sdta`)

## Resumo

O `sinan-sdta` contém os microdados dos **inquéritos e planilhas de acompanhamento de surtos** de Doenças Transmitidas por Alimentos (DTA — CID-10 A04–A09, inclusive Rotavírus/Norovírus/Adenovírus por veículo comum) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a **planilha consolidada de um surto** — caso típico em que o modo de transmissão provável é indireto/veículo comum — preenchida pela Vigilância Epidemiológica municipal/estadual ao longo da investigação do surto e digitada no SINAN Net/Sinan Online. É a base de agregados epidemiológicos da vigilância de surtos por veículo comum (água e alimentos), com leiaute de 102 colunas: modo e veículo provável de transmissão, contagens de doentes/hospitalizados/óbitos por faixa etária e sexo, sinais e sintomas agregados, tempo de incubação, fatores causais, amostras (clínicas e bromatológicas) e agentes etiológicos/ alimentos implicados — campos agregados voltados à vigilância de surtos.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2007 a 2018 em `FINAIS` (com lacuna em 2014) e 2019 a 2024 em `PRELIM` (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 17 arquivos (~1,2 MB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim (diretório `PRELIM`, sem arquivo em 2014)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `SDTA` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `SDTA` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `SDTABR24.dbc` — `SDTA` é o prefixo do agravo (Surto DTA), `BR` indica a consolidação nacional de todo o país e `24` é o ano de notificação (2024). A série em `FINAIS` vai de 2007 a 2018 (com lacuna em 2014) e os anos de 2019 a 2024 estão apenas em `PRELIM` (ex.: `SDTABR24.dbc`, atualização de 24/07/2025).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-sdta/<ano>/sinan-sdta_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-sdta/2024/sinan-sdta_preliminar_2024-br@20250724.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip`, as instruções POP_I/II/III de acesso, descompactação e tabulação e os manuais de vigilância de surtos de DTA; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

O componente de vigilância de surtos é operado pela Vigilância Epidemiológica/GVE — municípios, estados e a Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) — nos termos da Lista Nacional de Agravos de Notificação (Portaria GM/MS nº 204/2016) e do Guia de Vigilância em Saúde, com suporte do CIEVS (Centros de Informações Estratégicas em Vigilância em Saúde) para o alerta e o acompanhamento dos eventos de grande porte. No SINAN, surtos por veículo comum (água, alimentos e outros veículos indiretos) são acompanhados por meio das planilhas de investigação de surto — o módulo abre automaticamente a planilha de DTA quando o veículo é alimento/água. Esses registros complementam a vigilância de casos individuais e alimentam os alertas e fichamentos do CIEVS, tornando a base peça central da vigilância epidemiológica de doenças transmitidas por água e alimentos no país.

O evento gerador deste dataset é a **Planilha de Acompanhamento de Surto** do SINAN (ficha de surto de DTA e agravos por veículo comum). A notificação nasce quando o modo provável de transmissão é registrado como indireto/veículo comum (`CS_TRANS` = 2 ou veículo de transmissão provável entre 2 e 9 em `TP_INDIRET`) — inclusive surtos por Rotavírus, Norovírus e Adenovírus por água/alimentos, caso em que a Planilha de DTA é aberta automaticamente pelo sistema. A investigação é completada com: local de produção/preparação (`TP_LOCAL` — domicílio, restaurantes, comemorações, creche/escola, hospital/unidade de saúde); número de entrevistados, doentes, total de doentes e hospitalizações/óbitos (`NU_ENTR`, `NU_ENT_DOE`, `NU_TOT`, `NU_TOT_HOS`, `NU_OBITO`); distribuição de doentes por faixa etária e sexo; sinais e sintomas agregados (náuseas, vômitos, diarreia, cefaleia, abdominais, neurológicos e outros: `NU_NAUSE_P`, `NU_VOMTO_N`, `NU_DIARR_N`, `NU_CEFAL_N`, `NU_ABDOM_N`, `NU_NEURO_N`, `NU_OUTRO_N`, `NU_FEBRE_N`); tempo de incubação (mediana e média, mínimo e máximo); fatores causais (matéria-prima imprópria, conservação inadequada, manipulação incorreta: `ST_IMPRO`, `ST_INAD`, `ST_MANIP`); amostras clínicas e bromatológicas coletadas e resultados (`ST_A_CLINI`, `ST_ALIMEN`, `NU_A_ALIM`); agentes etiológicos etiologia por extenso (`AGENTE_ET1..3`) e alimento suspeito/causal (`ALIMENTO_C`). A unidade de análise é o Surto.

A série histórica de bases `FINAIS` no FTP inicia em **2007** e vai até **2018**, com **lacuna em 2014** (não há arquivo desse ano no FTP); os anos de 2019 a 2024 estão apenas em `PRELIM`. O dicionário de dados do agravo (revisado em fevereiro/2012) remete à planilha de acompanhamento de surto e às regras de abertura automática da Planilha de DTA.

Aplicações analíticas típicas: frequência de surtos por ano e região (UF/least `ID_MUNICIP`); distribuição do local de produção (`TP_LOCAL`) e do veículo (`TP_INDIRET`); atingimento/letalidade do surto (hospitalizações e óbitos `NU_TOT_HOS`, `NU_OBITO` sobre `NU_TOT`); distribuição agregada por doentes (`NU_TOT`) e por sintoma (`NU_*`); tempo de incubação (mediana/média/min/max) por agente (`AGENTE_ET1..3`) e por alimento (`ALIMENTO_C`) e amostras coletadas (`ST_A_CLINI`, `ST_ALIMEN`, `NU_A_ALIM`).

### Cobertura observada

- Índice do FTP (2026-10): 19 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-11-10.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `SDTABR24.dbc` (102 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `SEM_NOT` / `NU_ANO` | Data (`AAAAMMDD`)/Inteiro | Data e semana epidemiológica e ano da notificação do surto |
| `ID_MUNICIP` / `SG_UF` / `ID_MUNI_RE` | String (6/7) | Códigos IBGE de município e UF de notificação e residência |
| `ID_UNIDADE` / `ID_REGIONA` | String 7 | Código CNES da unidade notificante e região de saúde |
| `DT_SIN_PRI` / `SEM_PRI` | Data/Inteiro | Data e semana epidemiológica de início do surto |
| `QT_TOTAL_C` | Inteiro | Total de casos do surto |
| `DT_INVEST` / `DT_DIGITA` | Data (`AAAAMMDD`) | Data da investigação e de digitação |
| `CS_TRANS` | Inteiro | Modo provável de transmissão: 1 - Direta (pessoa a pessoa), 2 - Indireta (veículo comum ou vetor), 9 - Ignorado |
| `TP_INDIRET` | Inteiro | Veículo provável da transmissão indireta: alimento/água (2–3), vetor (3–4), produto (medicamentos, agrotóxicos, imunobiológicos, sangue), fômite (4–5); a Planilha de DTA é aberta quando veículo entre 2 e 9 |
| `TP_LOCAL` | Inteiro | Local de produção/preparação: 01 - Domicílio, 02 - Comemorações, 03 - Creche/Escola, 04 - Hospital/Unidade de Saúde, restaurantes, entre outros |
| `NU_ENTR` / `NU_ENT_DOE` | Inteiro | Número de entrevistados e de doentes pela Vigilância Epidemiológica (doentes ≤ entrevistados) |
| `NU_TOT` / `NU_TOT_HOS` / `NU_OBITO` | Inteiro | Número total de doentes, de hospitalizados e de óbitos |
| `NU_1_M_NU` a `NU_TOT_IGN` / `NU_F_TOT_N` | Inteiro | Distribuição de doentes por faixa etária e sexo (masculino, feminino e sexo ignorado) |
| `NU_NAUSE_P` / `NU_VOMTO_N` / `NU_DIARR_N` / `NU_CEFAL_N` / `NU_ABDOM_N` / `NU_NEURO_N` / `NU_FEBRE_N` / `NU_OUTRO_N` | Inteiro | Número de doentes com cada sinal/sintoma (nauseas, vômitos, diarreia, cefaleia, dores abdominais, sintomas neurológicos, febre, outros) |
| `NU_INCUB_M` / `MAX_INC` / `NU_INC_ME` | Inteiro | Tempo de incubação: mediana máximo, máximo do período e média |
| `ST_INCUB_M` / `ST_INC_ME` | Inteiro | Unidade do tempo de incubação (horas/dias) |
| `TP_PRO_PRE` | Inteiro | Local principal de produção/preparação do alimento implicado no surto |
| `ST_IMPRO` / `ST_INAD` / `ST_MANIP` / `ST_F_OUTRO`/`DS_F_OUTRO` | Inteiro/String | Fatores causais: matéria-prima imprópria, conservação inadequada, manipulação incorreta e outros fator |
| `ST_A_CLINI` / `NU_A_CLINI` / `NU_CLI_NUM` / `NU_NUM_2` / `NU_RESU_3` | Inteiro | Amostras clínicas coletadas, número de amostras e resultados |
| `ST_ALIMEN` / `NU_A_ALIM` / `NU_A_NUM_1..3` | Inteiro | Amostras de alimentos coletadas (bromatológicas), número e resultados |
| `AGENTE_ET1` / `AGENTE_ET2` / `AGENTE_ET3` | String | Agente etiológico identificado (por extenso), até 3 por surto |
| `ALIMENTO_C` | String | Alimento suspeito/causal (por extenso) |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte: 2 - Clínico, 3 - Laboratorial, 4 - Laboratorial Clínico-Bromatológico, 5 - Inconclusivo |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do surto |
| `DTTRANSUS`/`DTTRANS*` / `DT_TRANS*` | Data (`AAAAMMDD`) | Datas de tramitação e trânsito entre níveis do sistema |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `id_agravo` | `ID_AGRAVO` | texto | Agravo | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação. co_municipio_no tificacao | — | todos |
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. 3 | 3 – Notificação de Surto | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno). ds_semana_noti ficacao | — | todos |
| `nu_ano` | `NU_ANO` | texto | Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de. Sigla da Unidade | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | Campo com código da regional de saúde da tabela de município do sistema (campo interno). tb_regional_svs _.co_seq_region al | — | todos |
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora. co_unidade_noti ficacao | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos 1ºs sintomas do 1º caso suspeito. dt_diagnostico_s intoma | — | todos |
| `sem_pri` | `SEM_PRI` | inteiro | Semana epidemiológic a dos primeiros sintomas do caso índice (campo interno). ds_semana_noti ficacao | — | todos |
| `qt_total_c` | `QT_TOTAL_C` | texto | N° de casos Suspeitos / Expostos até a data de notificação. nu_caso_suspeit o | — | todos |
| `cs_local` | `CS_LOCAL` | texto | Local inicial de Ocorrência do Surto | 1- Residência 2- Hospital / Unidade de saúde 3- Creche / | todos |
| `sg_uf` | `SG_UF` | texto | UF de Ocorrência. co_uf_residênci a | — | todos |
| `id_muni_re` | `ID_MUNI_RE` | texto | Município. Código do | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | Campo com código da regional de saúde da tabela de município do sistema (campo interno). tb_regional_svs. co_seq_regional | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil. co_pais_residen cia | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dttransus` | `DTTRANSUS` | data | Data de transferência da unidade de saúde (campo interno). Data de Transferência da Unidade de Saúde | — | todos |
| `dttransdm` | `DTTRANSDM` | data | Data de transferência do distrito municipal (campo interno). Data de Transferência do Distrito Municipal | — | todos |
| `dttransrm` | `DTTRANSRM` | inteiro | Data de transferência da regional municipal (campo interno). Data de Transferência da Regional Municipal | — | todos |
| `dttranssm` | `DTTRANSSM` | data | Data de transferência da secretaria municipal de saúde (campo interno). Data de Transferência da Secretaria Municipal de Saúde | — | todos |
| `dttransrs` | `DTTRANSRS` | data | Data de transferência da regional de. Data de Transferência da Regional de Saúde | — | todos |
| `dttransse` | `DTTRANSSE` | data | Data de transferência da secretaria (campo interno). Data de Transferência da Secretaria Estadual | — | todos |
| `dt_invest` | `DT_INVEST` | data | Data da investigação | — | todos |
| `cs_trans` | `CS_TRANS` | texto | Modo provável da transmissão. st_modo_transm issao | 1-Direta(pessoa a pessoa) 2-Indireta(veículo comum ou vetor) 9-Ignorado | todos |
| `tp_indiret` | `TP_INDIRET` | texto | Se indireta, qual o veículo de transmissão provável. tp_veiculo_trans missao | 1-Alimento//água 2-Recursos hídricos contaminados(poço, rio, reservatório de água) 3-Vetor 4- Produto(medicament os, agrotóxico, imunobiológicos, sangue, etc) 5-Fômite(faca, lençóis,etc) | todos |
| `tp_local` | `TP_LOCAL` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Surto Doenças Transmitidas por Alimentos (`TP_LOCAL`); o dicionário consultado não define o campo isoladamente | — | todos |
| `nu_entr` | `NU_ENTR` | inteiro | Número de Entrevistados. Registrar o total de pessoas entrevistadas (total de doentes e não doentes) pela Vigilância Epidemiológica | — | todos |
| `nu_ent_doe` | `NU_ENT_DOE` | inteiro | Número de Doentes Entrevistados. nu_entrevistado_ doente | — | todos |
| `nu_tot` | `NU_TOT` | inteiro | Número Total de Doentes | — | todos |
| `nu_tot_hos` | `NU_TOT_HOS` | inteiro | Número Total de. nu_total_hospitali zado | — | todos |
| `nu_obito` | `NU_OBITO` | inteiro | Número de Óbitos | — | todos |
| `nu_1_m_nu` | `NU_1_M_NU` | inteiro | Número de Doentes por Faixa Etária e Sexo Masculino < 1 Número. nu_faixa_menor_ 1_m_nu | — | todos |
| `nu_1_4_nu` | `NU_1_4_NU` | inteiro | Número de Doentes por Faixa Etária e Sexo Masculino 1 a 4 Número. nu_faixa_1_a_4_ m_nu | — | todos |
| `nu_5_9_nu` | `NU_5_9_NU` | inteiro | Número de Doentes por Faixa Etária e Sexo Masculino 5 a 9 Número. nu_faixa_5_a_9_ m_nu | — | todos |
| `nu_10_19_m` | `NU_10_19_M` | inteiro | Número de Doentes por Faixa Etária e Sexo Masculino 10 a 19 Número. nu_faixa_10_a_1 9_m_nu | — | todos |
| `nu_20_49_n` | `NU_20_49_N` | inteiro | Número de Doentes por Faixa Etária e Sexo Masculino 20 a 49 Número. nu_faixa_20_a_4 9_m_nu | — | todos |
| `nu_50_m_nu` | `NU_50_M_NU` | inteiro | Número de. O número total de doentes por | — | todos |
| `nu_igra_nu` | `NU_IGRA_NU` | inteiro | Número de Doentes por Faixa Etária e Sexo Masculino Ignorada - Número. nu_faixa_ignorad a_m_nu | — | todos |
| `nu_f_tot_n` | `NU_F_TOT_N` | inteiro | Número de Doentes por Faixa Etária e Sexo Masculino- Total Número. nu_faixa_total_m _nu | — | todos |
| `nu_1_f_nu` | `NU_1_F_NU` | inteiro | Número de Doentes por Faixa Etária e Sexo Feminino < 1 Número. nu_faixa_menor_ 1_f_nu | — | todos |
| `nu1_4_f_nu` | `NU1_4_F_NU` | inteiro | Número de Doentes por Faixa Etária e Sexo Feminino 1 a 4 Número. nu_faixa_1_a_4_ f_nu | — | todos |
| `nu5_9_f_nu` | `NU5_9_F_NU` | inteiro | Número de Doentes por Faixa Etária e Sexo Feminino 5 a. nu_faixa_5_a_9_ f_nu | — | todos |
| `nu10_19_n` | `NU10_19_N` | inteiro | Número de Doentes por Faixa Etária e Sexo Feminino 10 a 19 Número. nu_faixa_10_a_1 9_f_nu | — | todos |
| `nu_20_49_f` | `NU_20_49_F` | inteiro | Número de Doentes por Faixa Etária e Sexo Feminino 20 a 49 Número. nu_faixa_20_a_4 9_f_nu | — | todos |
| `nu_50_f_nu` | `NU_50_F_NU` | inteiro | Número de Doentes por Faixa Etária e Sexo Feminino 50 e + Número. nu_faixa_50_e_ mais_f_nu | — | todos |
| `nu_ig_f_nu` | `NU_IG_F_NU` | inteiro | Número de Doentes por Faixa Etária e Sexo Feminino Ignorada- Número. nu_faixa_ignorad a_f_nu | — | todos |
| `nu_to_f_nu` | `NU_TO_F_NU` | inteiro | Número de Doentes por Faixa Etária e Sexo Feminino Total- Número. nu_faixa_total_f_ nu | — | todos |
| `nu_1_ign` | `NU_1_IGN` | inteiro | Número de Doentes por. nu_faixa_menor_ 1_ign | — | todos |
| `nu_1_4_ign` | `NU_1_4_IGN` | inteiro | Número de Doentes por Faixa Etária e Sexo Ignorado 1 a 4. nu_faixa_1_a_4_ ign | — | todos |
| `nu_5_9_ign` | `NU_5_9_IGN` | inteiro | Número de Doentes por Faixa Etária e Sexo Ignorado 5 a 9. nu_faixa_5_a_9_ ign | — | todos |
| `nu_10_19ig` | `NU_10_19IG` | inteiro | Número de Doentes por Faixa Etária e Sexo Ignorado10 a 19. nu_faixa_10_a_1 9_ign | — | todos |
| `nu_20_49ig` | `NU_20_49IG` | inteiro | Número de Doentes por Faixa Etária e Sexo Ignorado 20 a 49. nu_faixa_20_a_4 9_ign | — | todos |
| `nu_50_ign` | `NU_50_IGN` | inteiro | Número de Doentes por Faixa Etária e Sexo Ignorado 50 e +. nu_faixa_50_e_ mais_ign | — | todos |
| `nu_ig_ign` | `NU_IG_IGN` | inteiro | Número de Doentes por Faixa Etária e Sexo Ignorado Ignorada. nu_faixa_ignorad a_ign | — | todos |
| `nu_tot_ign` | `NU_TOT_IGN` | inteiro | Número de Doentes por Faixa Etária e Sexo Ignorado Total. nu_faixa_total_ig n | — | todos |
| `nu_1_tot_n` | `NU_1_TOT_N` | inteiro | Número de Doentes por Faixa Etária e Sexo Total <1 Número. nu_faixa_menor_ 1_tot_nu | — | todos |
| `nu_1_4_tot` | `NU_1_4_TOT` | inteiro | Número de Doentes por Faixa Etária e Sexo Total 1 a 4 Número. nu_faixa_1_a_4_ tot_nu | — | todos |
| `nu_5_9_tot` | `NU_5_9_TOT` | inteiro | Número de Doentes por Faixa Etária e Sexo Total 5 a 9 Número. nu_faixa_5_a_9_ tot_nu | — | todos |
| `nu_10_19` | `NU_10_19` | inteiro | Número de Doentes por Faixa Etária e Sexo Total 10 a 19 Número. nu_faixa_10_a_1 9_tot_nu | — | todos |
| `nu_20_49` | `NU_20_49` | inteiro | Número de Doentes por Faixa Etária e Sexo Total 20 a 49 Número. nu_faixa_20_a_4 9_tot_nu | — | todos |
| `nu_50_tot` | `NU_50_TOT` | inteiro | Número de Doentes por Faixa Etária e Sexo Total 50. nu_faixa_50_e_ mais_tot_nu | — | todos |
| `nu_ign_nu` | `NU_IGN_NU` | inteiro | Número de Doentes por Faixa Etária e Sexo Total Ignorada Número. nu_faixa_ignorad a_tot_nu | — | todos |
| `nu_f_tot` | `NU_F_TOT` | inteiro | Número de Doentes por Faixa Etária e Sexo Total – Total Número. nu_faixa_total_to t_nu | — | todos |
| `nu_nause_p` | `NU_NAUSE_P` | inteiro | Sinais e sintomas Doentes Náuseas Número. nu_sinais_nause a_nu | — | todos |
| `nu_vomto_n` | `NU_VOMTO_N` | inteiro | Sinais e sintomas Doentes Vômitos Número. nu_sinais_vomito _nu | — | todos |
| `nu_diarr_n` | `NU_DIARR_N` | inteiro | Sinais e sintomas Doentes Diarréia Número. nu_sinais_diarrei a_nu | — | todos |
| `nu_cefal_n` | `NU_CEFAL_N` | inteiro | Sinais e sintomas Doentes Cefaléia Número. nu_sinais_cefalei a_nu | — | todos |
| `nu_abdom_n` | `NU_ABDOM_N` | inteiro | Sinais e sintomas Doentes Dor Abdominal Número. nu_sinais_dor_a bdominal_nu | — | todos |
| `nu_neuro_n` | `NU_NEURO_N` | inteiro | Sinais e sintomas Doentes Neurológicos Percentual. nu_sinais_neurol ogico_nu | — | todos |
| `nu_outro_n` | `NU_OUTRO_N` | inteiro | Sinais e sintomas Doentes Outros Número. nu_sinais_outro_ nu | — | todos |
| `nu_febre_n` | `NU_FEBRE_N` | inteiro | Sinais e sintomas Doentes Febre Número | — | todos |
| `nu_incub_m` | `NU_INCUB_M` | inteiro | Período de Incubação Mínimo (em horas ou dias) – Período. nu_incubacao_m inino | — | todos |
| `st_incub_m` | `ST_INCUB_M` | texto | Período de Incubação Mínimo (em horas ou dias) – Horas/Dias. st_incubacao_mi nino | — | todos |
| `max_inc` | `MAX_INC` | inteiro | Período de. Quando o período | — | todos |
| `max_st_inc` | `MAX_ST_INC` | texto | Período de Incubação Máximo (em horas ou dias) – Horas/Dias. st_incubacao_m aximo | — | todos |
| `nu_inc_me` | `NU_INC_ME` | inteiro | Mediana do Período de Incubação (em horas ou dias) – Período. nu_incubacao_m edia | — | todos |
| `st_inc_me` | `ST_INC_ME` | texto | Mediana do Período de Incubação (em horas ou dias) – Horas/Dias. st_incubacao_m edia | — | todos |
| `tp_pro_pre` | `TP_PRO_PRE` | texto | Local de Produção / Preparação | 01- Ambulantes 02- Comemoraçõ es 03- Creche / | todos |
| `st_impro` | `ST_IMPRO` | texto | Fatores Causais Matéria – prima Imprópria. st_fator_mat_pri ma_impropria | 1- Sim 2- Não 9- Ignorado | todos |
| `st_inad` | `ST_INAD` | texto | Fatores Causais Conservação Inadequada. st_fator_conserv a_inadequada | 1- Sim 2- Não 9- Ignorado | todos |
| `st_manip` | `ST_MANIP` | texto | Fatores Causais Manipulação / Preparação Inadequada. st_fator_manipul a_inadequada | 1- Sim 2- Não 9- Ignorado | todos |
| `st_f_outro` | `ST_F_OUTRO` | texto | Fatores Causais Outros | 1- Sim 2- Não 9- Ignorado | todos |
| `ds_f_outro` | `DS_F_OUTRO` | texto | Fatores Causais Outros Especificar | — | todos |
| `st_a_clini` | `ST_A_CLINI` | texto | Coletadas amostras Clínicas. st_amostra_clinic a | 1- Sim 2- Não 9- Ignorado | todos |
| `nu_num_3` | `NU_NUM_3` | inteiro | N° de. Se o agente for | — | todos |
| `st_alimen` | `ST_ALIMEN` | texto | Coletadas Amostras de Alimentos. st_amostra_alim ento | 1- Sim 2- Não 9- Ignorado | todos |
| `nu_a_num_3` | `NU_A_NUM_3` | inteiro | N° de Positivas. nu_amostra_alim ento_num_3 | — | todos |
| `agente_eti` | `AGENTE_ETI` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2007 a 2021 |
| `agente_et0` | `AGENTE_ET0` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2007 a 2021 |
| `agente_et1` | `AGENTE_ET1` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `alimento_c` | `ALIMENTO_C` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `criterio` | `CRITERIO` | texto | Critério confirmação. tp_criterio_confir macao | 1 - Clínico- Epidemiológico 2 - Laboratorial Clínico 3 - Laboratorial Bromatológico 4 - Laboratorial Clínico - Bromatológico 5 - Inconclusivo | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data de encerramento do surto DTA. Data do encerramento | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `nu_a_clini` | `NU_A_CLINI` | inteiro | Se SIM, n° de Amostras. nu_amostra_clini ca | — | 2026 a 2026 |
| `nu_cli_num` | `NU_CLI_NUM` | inteiro | N° de Positivas. nu_amostra_clini ca_num_1 | — | 2026 a 2026 |
| `nu_num_2` | `NU_NUM_2` | inteiro | N° de Positivas. nu_amostra_clini ca_num_2 | — | 2026 a 2026 |
| `nu_resu_3` | `NU_RESU_3` | texto | Resultado 3 (Outro Achado). ds_amostra_clini ca_result_3 | — | 2026 a 2026 |
| `nu_a_alim` | `NU_A_ALIM` | inteiro | Se SIM, n° de Amostras. nu_amostra_alim ento | — | 2026 a 2026 |
| `nu_a_num_1` | `NU_A_NUM_1` | inteiro | N° de Positivas. nu_amostra_alim ento_num_1 | — | 2026 a 2026 |
| `nu_a_num_2` | `NU_A_NUM_2` | inteiro | N° de Positivas. nu_amostra_alim ento_num_2 | — | 2026 a 2026 |
| `agente_et2` | `AGENTE_ET2` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2026 a 2026 |
| `agente_et3` | `AGENTE_ET3` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2026 a 2026 |

## No lake

- **Dataset no lake:** `datasus/sinan-sdta`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 10, inteiro: 58, nulo (vazio nas amostras): 3, texto: 38.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-sdta.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- a base é de **registros agregados por surto** — o cálculo de taxas deve sempre ser feito com as constantes de doentes (`NU_TOT`), hospitalizados (`NU_TOT_HOS`) e óbitos (`NU_OBITO`); a abertura da planilha condiciona-se ao modo de transmissão (`CS_TRANS` = 2 ou veículo indireto 2–9); "agentes etiológicos" (`AGENTE_ET1..3`) e "alimento causal" (`ALIMENTO_C`) são texto longo, *não* códigos de dicionário; e há lacunas no FTP (ausência do arquivo de 2014 em `FINAIS`). (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 11 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-sdta/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-sdta
quantilica datasus list sinan-sdta

# 2. Baixar microdados de sinan-sdta com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-sdta -o ./data --start 2007 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-sdta -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-sdta -o ./data/raw --parquet-dir ./data/parquet --start 2007
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc(
    "data/sinan-sdta/2024/sinan-sdta_preliminar_2024-br@20250724.dbc", clean=True
)

# Surtos por modo provável de transmissão (direta x indireta/veículo comum)
trans = qdf.group_by("cs_trans").len().sort("cs_trans")
print(trans)

# Letalidade hospitalar nos surtos registrados
letal = qdf.select(
    [
        pl.col("nu_tot").sum().alias("doentes"),
        pl.col("nu_tot_hos").sum().alias("hospitalizados"),
        pl.col("nu_obito").sum().alias("obitos"),
    ]
)
print(letal)

# Agentes etiológicos mais frequentes (texto livre)
agentes = qdf.group_by("agente_et1").len().sort("len", descending=True)
print(agentes.head(15))
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Surtos de DTA (planilha de acompanhamento de surto e dicionário de dados)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de Doenças Transmitidas por Alimentos (DTA) e procedimentos de vigilância epidemiológica de surtos (CIEVS)
