---
dataset:
  id: sinan-hant
  fonte: datasus
  titulo: Hantavirose
  resumo: O sinan-hant contém os microdados das notificações e investigações de casos de Hantavirose (principalmente a síndrome cardiopulmonar por hantavírus, CID-10 B33.4) registrados no Sistema de Informação de Agravos de Notificação (SINAN).
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '1999'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de hantavirose
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 172
  unidades_de_medida:
    id_municip: 'número inteiro: contagem ou código numérico (ver Descrição)'
    id_unidade: 'número inteiro: contagem ou código numérico (ver Descrição)'
    dt_notific: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cs_raca: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cs_escolar: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ano: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sem_not: 'número inteiro: contagem ou código numérico (ver Descrição)'
    id_regiona: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sem_pri: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ano_nasc: 'número inteiro: contagem ou código numérico (ver Descrição)'
    id_pais: 'número inteiro: contagem ou código numérico (ver Descrição)'
    id_dg_not: 'número inteiro: contagem ou código numérico (ver Descrição)'
    id_ev_not: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_dt_inv: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_desmat: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_arrumo: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_colhei: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_corte: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_moagem: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_planti: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_aragem: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_lazer: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_roedor: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_limpez: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_contat: 'número inteiro: contagem ou código numérico (ver Descrição)'
    ant_exposi: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_dt_ate: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_rinorr: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_vomito: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_renal: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_dispne: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_abdomi: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_cefale: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_tontur: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_h: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_febre: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_neurol: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_gargan: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_mialgi: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_tosse: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_angust: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_toraci: 'número inteiro: contagem ou código numérico (ver Descrição)'
    cli_outros: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_realiz: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_igm_r: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_igg_r: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_outro: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_igm: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_igg: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_l_out: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_bilate: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_hemato: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_leuc_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_micron: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_trombo: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_l_c_de: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_histop: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_ureia: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_l_s_de: 'número inteiro: contagem ou código numérico (ver Descrição)'
    lab_atipic: 'número inteiro: contagem ou código numérico (ver Descrição)'
    tra_hosp: 'número inteiro: contagem ou código numérico (ver Descrição)'
    tra_dt_int: 'número inteiro: contagem ou código numérico (ver Descrição)'
    tra_munici: 'número inteiro: contagem ou código numérico (ver Descrição)'
    tra_mecani: 'número inteiro: contagem ou código numérico (ver Descrição)'
    tra_antivi: 'número inteiro: contagem ou código numérico (ver Descrição)'
    tra_tratam: 'número inteiro: contagem ou código numérico (ver Descrição)'
    con_inf_pa: 'número inteiro: contagem ou código numérico (ver Descrição)'
    conf_inf_m: 'número inteiro: contagem ou código numérico (ver Descrição)'
    con_area: 'número inteiro: contagem ou código numérico (ver Descrição)'
    con_ambien: 'número inteiro: contagem ou código numérico (ver Descrição)'
    con_diagno: 'número inteiro: contagem ou código numérico (ver Descrição)'
    con_criter: 'número inteiro: contagem ou código numérico (ver Descrição)'
    con_evoluc: 'número inteiro: contagem ou código numérico (ver Descrição)'
    con_dt_obi: 'número inteiro: contagem ou código numérico (ver Descrição)'
    con_autops: 'número inteiro: contagem ou código numérico (ver Descrição)'
    con_doenca: 'número inteiro: contagem ou código numérico (ver Descrição)'
    con_dt_enc: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Hantavirose (`sinan-hant`)

## Resumo

O `sinan-hant` contém os microdados das notificações e investigações de casos de Hantavirose (principalmente a síndrome cardiopulmonar por hantavírus, CID-10 B33.4) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de hantavirose, digitado no SINAN Net/Sinan Online. O agravo é de notificação compulsória imediata (até 24 horas) por tratar-se de zoonose grave, de alta letalidade e com potencial de surto, por exemplo em roedores silvestres.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 1999 a 2026 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 28 arquivos (~2,3 MB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim (diretório `PRELIM`)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `HANT` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `HANT` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `HANTBR99.dbc` — prefixo `HANT`, `BR` (consolidação nacional) e `99` (ano 1999), até `HANTBR24.dbc` (2024); os anos recentes aparecem em `PRELIM` (ex.: `HANTBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-hant/<ano>/sinan-hant_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-hant/2024/sinan-hant_2024-br@20260515.dbc`; arquivos preliminares recebem o sufixo `-preliminar`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## Conteúdo

A hantavirose brasileira é causada por hantavirus (Orthohantavirus da família Hantaviridae) mantidos por roedores silvestres das famílias Cricetidae (ex.: *Oligoryzomys nigripes*, *O. flavescens*, *Necromys lasiurus* — principais, com variantes regionais Araraquara, Juquitiba, Castelo dos Sonhos e Laguna Negra). A transmissão humana dá-se por inalação de aerossóis de urina, fezes e saliva de roedores infectados, tipicamente em ambientes rurais e florestais. A vigilância é da SVSA/MS; a doença é de notificação compulsória imediata desde a Portaria SVS/MS nº 5/2006 e está na LNC consolidada (Portaria GM/MS nº 204/2016). A forma mais comum no Brasil é a síndrome cardiopulmonar por hantavírus (SCPH), grave, em pacientes jovens, com letalidade historicamente em torno de 40%.

O evento gerador é a **Ficha de Investigação de Hantavirose** do SINAN (ficha `Hantavirose_v5`, de 19/05/2006, com instrucional e dicionário de dados próprios), preenchida no caso suspeito e completada com exames sorológicos — IgM (imunofluorescência), imunohistoquímica (em material de necropsia) e RT-PCR — e com a investigação do local provável de infecção (LPI). A unidade de análise é o caso suspeito/confirmado individual.

A literatura documenta três versões de ficha na série histórica (1996-2000 SINAN-DOS, 2001-2006 SINAN-Windows, 2007+ SINAN NET), o que introduz quebras de leiaute nos campos específicos. No FTP, a série de arquivos finais disponíveis inicia em 1999 e casos notificados concentram-se em biomas de Cerrado, Mata Atlântica e Pampa (Minas Gerais, São Paulo, Mato Grosso, Paraná, Santa Catarina, Rio Grande do Sul e oeste do Espírito Santo).

Aplicações analíticas: coeficiente de incidência e letalidade anual, distribuição geográfica pelo local provável de infecção (campo LPI), proporção de casos confirmados entre notificados (a maior parte descartada — relevância da qualidade de triagem), resultados de métodos laboratoriais (IgM, imunohistoquímica, RT-PCR), e vigilância de trabalhadores rurais e atividades de risco (colheitas, desmatamento, armazenamento de grãos).

### Cobertura observada

- Índice do FTP (2026-10): 28 arquivos, de 1999 a 2026, 1 UF(s) com arquivos, última atualização em 2026-05-15.
- Conversão local de amostras (5 arquivo(s) Parquet, de 1999 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Hantavirose — CID-10 B33.4) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave; notificação imediata) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data do início dos sintomas (síndrome febril, mialgia, dispnéia) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `LPI` | String | Local provável de infecção (município/UF onde ocorreu a exposição) — campo essencial da ficha de hantavirose |
| `CLASSI_FIN` | Inteiro | Classificação final (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `id_municip` | `ID_MUNICIP` | inteiro ou texto | Município de Notificação. co_municipio_not ificacao | — | todos |
| `id_unidade` | `ID_UNIDADE` | inteiro ou texto | Unidade de saúde ou outra fonte notificadora. co_unidade_notifi cacao | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data ou inteiro | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `cs_raca` | `CS_RACA` | inteiro ou texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escolar` | `CS_ESCOLAR` | inteiro | Escolaridade do paciente (formato do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 1999 a 1999 |
| `nu_ano` | `NU_ANO` | inteiro ou texto | (campo interno). Ano da notificação | — | todos |
| `sem_not` | `SEM_NOT` | inteiro ou texto | Semana epidemiológic a da notificação (campo interno). ds_semana_notifi cacao | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_regiona` | `ID_REGIONA` | inteiro ou texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico. dt_diagnostico_si ntoma | — | todos |
| `sem_pri` | `SEM_PRI` | inteiro ou texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno). ds_semana_sinto ma | — | todos |
| `ano_nasc` | `ANO_NASC` | inteiro ou texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_idade` | `NU_IDADE` | texto | Idade do paciente (formato do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 1999 a 1999 |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_pais` | `ID_PAIS` | inteiro ou texto | País (se residente fora do Brasil). co_pais_residenc ia | — | todos |
| `id_dg_not` | `ID_DG_NOT` | inteiro | Código (tipo, identificação ou classificação) registrado na ficha de Hantavirose (`ID_DG_NOT`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `id_ev_not` | `ID_EV_NOT` | inteiro | Código (tipo, identificação ou classificação) registrado na ficha de Hantavirose (`ID_EV_NOT`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `ant_dt_inv` | `ANT_DT_INV` | inteiro | Data da investigação | — | 1999 a 1999 |
| `ant_ocupac` | `ANT_OCUPAC` | texto | Ocupação do paciente (antecedente epidemiológico) | — | 1999 a 1999 |
| `ant_desmat` | `ANT_DESMAT` | inteiro | Antecedente epidemiológico ou exposição registrado na ficha de Hantavirose (`ANT_DESMAT`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `ant_arrumo` | `ANT_ARRUMO` | inteiro | Antecedente epidemiológico ou exposição registrado na ficha de Hantavirose (`ANT_ARRUMO`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `ant_colhei` | `ANT_COLHEI` | inteiro | Antecedente epidemiológico ou exposição registrado na ficha de Hantavirose (`ANT_COLHEI`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `ant_corte` | `ANT_CORTE` | inteiro | Antecedente epidemiológico ou exposição registrado na ficha de Hantavirose (`ANT_CORTE`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `ant_moagem` | `ANT_MOAGEM` | inteiro | Antecedente epidemiológico ou exposição registrado na ficha de Hantavirose (`ANT_MOAGEM`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `ant_planti` | `ANT_PLANTI` | inteiro | Antecedente epidemiológico ou exposição registrado na ficha de Hantavirose (`ANT_PLANTI`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `ant_aragem` | `ANT_ARAGEM` | inteiro | Antecedente epidemiológico ou exposição registrado na ficha de Hantavirose (`ANT_ARAGEM`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `ant_lazer` | `ANT_LAZER` | inteiro | Antecedente epidemiológico ou exposição registrado na ficha de Hantavirose (`ANT_LAZER`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `ant_roedor` | `ANT_ROEDOR` | inteiro | Antecedente epidemiológico ou exposição registrado na ficha de Hantavirose (`ANT_ROEDOR`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `ant_limpez` | `ANT_LIMPEZ` | inteiro | Antecedente epidemiológico ou exposição registrado na ficha de Hantavirose (`ANT_LIMPEZ`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `ant_contat` | `ANT_CONTAT` | inteiro | Antecedente epidemiológico ou exposição registrado na ficha de Hantavirose (`ANT_CONTAT`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `ant_exposi` | `ANT_EXPOSI` | inteiro | Antecedente epidemiológico ou exposição registrado na ficha de Hantavirose (`ANT_EXPOSI`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `cli_dt_ate` | `CLI_DT_ATE` | data ou inteiro | Data do 1º atendimento. dt_atendiment o_1 | — | todos |
| `cli_munici` | `CLI_MUNICI` | texto | Manifestação clínica registrada na ficha de Hantavirose (`CLI_MUNICI`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `cli_rinorr` | `CLI_RINORR` | inteiro | Manifestação clínica registrada na ficha de Hantavirose (`CLI_RINORR`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `cli_vomito` | `CLI_VOMITO` | inteiro ou texto | Manifestações clínicas (sinais e sintomas) Náusea/vômito. st_manifestac ao_nausea | 1-Sim 2-Não 9-Ignorado | todos |
| `cli_renal` | `CLI_RENAL` | inteiro ou texto | Manifestações clínicas (sinais e sintomas) Insuficiência renal. st_manifestac ao_insuf_rena l | 1-Sim 2-Não 9-Ignorado | todos |
| `cli_dispne` | `CLI_DISPNE` | inteiro ou texto | Manifestações clínicas (sinais e sintomas) Dispnéia ( alteração na respiração, dificuldade para respirar). st_manifestac ao_dispneia | 1-Sim 2-Não 9-Ignorado | todos |
| `cli_abdomi` | `CLI_ABDOMI` | inteiro ou texto | Manifestações clínicas (sinais e sintomas) Dor Abdominal. St_ manifestacao _dor_abdomin a | 1-Sim 2-Não 9-Ignorado | todos |
| `cli_cefale` | `CLI_CEFALE` | inteiro ou texto | Manifestações clínicas (sinais e sintomas). st_manifestac ao_cefaleia | 1-Sim 2-Não | todos |
| `cli_tontur` | `CLI_TONTUR` | inteiro ou texto | Manifestações clínicas (sinais e sintomas) Tontura/Vertigem. st_manifestac ao_tontura | 1-Sim 2-Não 9-Ignorado | todos |
| `cli_h` | `CLI_H` | inteiro | Manifestação clínica registrada na ficha de Hantavirose (`CLI_H`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `cli_h_desc` | `CLI_H_DESC` | texto | Manifestações clínicas (sinais e sintomas), Outras manifestações Hemorrágicas (especificar). ds_ manifestacao _hemor_outro | — | todos |
| `cli_febre` | `CLI_FEBRE` | inteiro ou texto | Manifestações clínicas (sinais e sintomas) Febre. st_manifestac ao_febre | 1-Sim 2-Não 9-Ignorado | todos |
| `cli_neurol` | `CLI_NEUROL` | inteiro ou texto | Manifestações clínicas (sinais e sintomas) Sintomas Neurológicos. st_manifestac ao_sintoma_n euro | 1-Sim 2-Não 9-Ignorado | todos |
| `cli_gargan` | `CLI_GARGAN` | inteiro | Manifestação clínica registrada na ficha de Hantavirose (`CLI_GARGAN`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `cli_mialgi` | `CLI_MIALGI` | inteiro | Sinais e sintomas – Mialgia | 1-Sim; 2-Não; 9- Ignorado | 1999 a 1999 |
| `cli_mial_d` | `CLI_MIAL_D` | texto | Manifestação clínica registrada na ficha de Hantavirose (`CLI_MIAL_D`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `cli_tosse` | `CLI_TOSSE` | inteiro ou texto | Manifestações clínicas (sinais e sintomas) Tosse Seca. st_manifestac ao_tosse_sec a | 1-Sim 2-Não 9-Ignorado | todos |
| `cli_angust` | `CLI_ANGUST` | inteiro | Manifestação clínica registrada na ficha de Hantavirose (`CLI_ANGUST`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `cli_toraci` | `CLI_TORACI` | inteiro ou texto | Manifestações clínicas (sinais e sintomas) Dor Torácica. st_manifestac ao_dor_toraci ca | 1-Sim 2-Não 9-Ignorado | todos |
| `cli_outros` | `CLI_OUTROS` | inteiro ou texto | Manifestações clínicas (sinais e sintomas) /Outros. st_manifestac ao_outro | 1-Sim 2-Não 9-Ignorado | todos |
| `cli_out_d` | `CLI_OUT_D` | texto | Manifestações clínicas (sinais e sintomas)/ Outros (especificar). ds_manifesta cao_outro | — | todos |
| `lab_realiz` | `LAB_REALIZ` | inteiro | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_REALIZ`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_igm_r` | `LAB_IGM_R` | inteiro ou texto | Resultado IgM. tp_resultado_i gm | 1- reagente 2- não reagente 3- inconclusivo 4- não realizado | todos |
| `lab_igg_r` | `LAB_IGG_R` | inteiro | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_IGG_R`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_outro` | `LAB_OUTRO` | inteiro | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_OUTRO`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_out_d` | `LAB_OUT_D` | texto | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_OUT_D`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_igm` | `LAB_IGM` | inteiro | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_IGM`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_igg` | `LAB_IGG` | inteiro | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_IGG`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_l_out` | `LAB_L_OUT` | inteiro | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_L_OUT`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_out_e` | `LAB_OUT_E` | texto | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_OUT_E`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_bilate` | `LAB_BILATE` | inteiro | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_BILATE`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_hemato` | `LAB_HEMATO` | inteiro | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_HEMATO`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_leuc_n` | `LAB_LEUC_N` | inteiro | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_LEUC_N`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_micron` | `LAB_MICRON` | inteiro | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_MICRON`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_trombo` | `LAB_TROMBO` | inteiro ou texto | Resultado A Trombocitopenia. st_resultado_ a_trombocitop enia | 1-Sim 2-Não 3-Não realizado 9-Ignorado | todos |
| `lab_l_c_de` | `LAB_L_C_DE` | inteiro | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_L_C_DE`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_histop` | `LAB_HISTOP` | inteiro | Histopatologia. Informar o resultado do exame histopatológico | 1 – Encontro do Parasita 2 – Compatível 3 – Não Compatível 4 – Não Realizado | 1999 a 1999 |
| `lab_ureia` | `LAB_UREIA` | inteiro ou texto | Resultado A Aumento de Uréia e Creatinina. st_resultado_ a_aumento | 1-Sim 2-Não 3-Não realizado 9-Ignorado | todos |
| `lab_l_s_de` | `LAB_L_S_DE` | inteiro | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_L_S_DE`); o dicionário consultado não define o campo isoladamente | — | 1999 a 1999 |
| `lab_atipic` | `LAB_ATIPIC` | inteiro ou texto | Resultado A Linfócitos Atípicos. st_resultado_ a_linfocito | 1-Sim 2-Não 3- Não realizado 9-Ignorado | todos |
| `tra_hosp` | `TRA_HOSP` | inteiro ou texto | Ocorreu Hospitalização. st_ocorreu_ho spitalizacao | 1-Sim 2-Não 9-Ignorado | todos |
| `tra_dt_int` | `TRA_DT_INT` | data ou inteiro | Data da internação. Dia, mês e ano da internação, caso tenha ocorrido | — | todos |
| `tra_dt_alt` | `TRA_DT_ALT` | texto | Dado do inquérito/tratamento de tracoma (`TRA_DT_ALT`) | — | 1999 a 1999 |
| `tra_uf` | `TRA_UF` | texto | UF. co_uf_hospita l | — | todos |
| `tra_munici` | `TRA_MUNICI` | inteiro ou texto | Município do hospital. co_municipio_ hospital | — | todos |
| `tra_mecani` | `TRA_MECANI` | inteiro ou texto | Suporte Terapêutico Ficou no Respirador mecânico. st_terapeutico _respirador | 1-Sim 2-Não 9-Ignorado | todos |
| `tra_antivi` | `TRA_ANTIVI` | inteiro ou texto | Suporte Terapêutico Usou | 1-Sim | todos |
| `tra_tratam` | `TRA_TRATAM` | inteiro ou texto | Suporte Terapêutico Outro tipo de tratamento. st_terapeutico _outro | 1-Sim 2-Não 9-Ignorado | todos |
| `tra_especi` | `TRA_ESPECI` | texto | Suporte Terapêutico Outro Tipo de Tratamento (Especificar). ds_terapeutic o_outro | — | todos |
| `conf_inf_u` | `CONF_INF_U` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 1999 a 1999 |
| `con_inf_pa` | `CON_INF_PA` | inteiro | Dado de conclusão do caso na ficha de Hantavirose (`CON_INF_PA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 1999 a 1999 |
| `conf_inf_m` | `CONF_INF_M` | inteiro | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 1999 a 1999 |
| `con_area` | `CON_AREA` | inteiro | Característica do local Provável da fonte de infecção Área provável de infecção | 1-Urbana 2-Rural 3-Peri-Urbana 9-Ignorado | 1999 a 1999 |
| `con_ambien` | `CON_AMBIEN` | inteiro ou texto | Tipo de Ambiente onde provavelmente ocorreu a infecção. tp_ambiente_i nfeccao | 1-Domiciliar 2-Trabalho 3-Lazer 4-Outro 9-Ignorado | todos |
| `con_diagno` | `CON_DIAGNO` | inteiro | Dado de conclusão do caso na ficha de Hantavirose (`CON_DIAGNO`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 1999 a 1999 |
| `con_diag_d` | `CON_DIAG_D` | texto | Dado de conclusão do caso na ficha de Hantavirose (`CON_DIAG_D`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 1999 a 1999 |
| `con_criter` | `CON_CRITER` | inteiro | Dado de conclusão do caso na ficha de Hantavirose (`CON_CRITER`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 1999 a 1999 |
| `con_evoluc` | `CON_EVOLUC` | inteiro | Dado de conclusão do caso na ficha de Hantavirose (`CON_EVOLUC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 1999 a 1999 |
| `con_dt_obi` | `CON_DT_OBI` | inteiro | Dado de conclusão do caso na ficha de Hantavirose (`CON_DT_OBI`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 1999 a 1999 |
| `con_autops` | `CON_AUTOPS` | inteiro ou texto | Se óbito, realizou autopsia. st_realizou_a utopsia | 1-Sim 2-Não 9-Ignorado | todos |
| `con_doenca` | `CON_DOENCA` | inteiro | Dado de conclusão do caso na ficha de Hantavirose (`CON_DOENCA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 1999 a 1999 |
| `con_dt_enc` | `CON_DT_ENC` | inteiro | Dado de conclusão do caso na ficha de Hantavirose (`CON_DT_ENC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 1999 a 1999 |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | 2007 a 2026 |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | 2007 a 2026 |
| `cs_suspeit` | `CS_SUSPEIT` | texto | Suspeita do Agravo. a) Doenças Exantemáticas 1 – Sarampo 2 – Rubéola b) Meningite 1 – Doenças Meningocócicas 2 – Outras Meningites c) AIDS (banco genérico) 1- Criança (<13) 2- Adulto (≥ 13 anos) AIDS (banco DBF) C- Criança (<13) A- Adulto (≥ 13 anos) | — | 2007 a 2026 |
| `in_aids` | `IN_AIDS` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Hantavirose (`IN_AIDS`); o dicionário consultado não define o campo isoladamente | — | 2007 a 2026 |
| `cs_mening` | `CS_MENING` | texto | Tipo de meningite (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2007 a 2026 |
| `dtdiasinac` | `DTDIASINAC` | data | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2007 a 2026 |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | 2007 a 2026 |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | 2007 a 2026 |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | 2007 a 2026 |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência. co_municipio_res idencia | — | 2007 a 2026 |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | 2007 a 2026 |
| `dt_invest` | `DT_INVEST` | data | Data da investigação. dt_investigaca o | — | 2007 a 2026 |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/Ramo de atividade econômica. co_cbo_ocup acao | — | 2007 a 2026 |
| `treina_mil` | `TREINA_MIL` | texto | Nas últimas 8 semanas (60 dias antes do inicio dos sintomas) desenvolveu e/ ou expôs-se atividades ligada a: Treinamento militar em parques, área rural ou silvestre.. st_atividade_t reinamento | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `desmata_n` | `DESMATA_N` | texto | Nas últimas 8 semanas (60 dias antes do inicio dos sintomas) desenvolveu e/ ou expôs-se atividades ligada a: Desmatamento, aragem de terra, plantio agrícola, e outros semelhantes.. st_atividade_ desmatament o | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `expo_n` | `EXPO_N` | texto | Nas últimas 8 semanas (60 dias antes do inicio dos sintomas) desenvolveu e/ ou expôs-se atividades ligada a : Exposição e/ou Limpeza de casa abandonada, despensa, galpão, depósitos, sótão, porão, e outros semelhantes. st_atividade_ exposicao | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `moagem_n` | `MOAGEM_N` | texto | Nas últimas 8 semanas (60 dias antes do inicio dos sintomas) desenvolveu e/ ou expôs-se atividades ligada a : Moagem e/ou Armazenamento de grãos, arrumou ou moveu fardos de lenha, capim, ou outros semelhantes.. st_atividade_ moagem | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `dormiu_n` | `DORMIU_N` | texto | Nas últimas 8 semanas (60 dias antes do inicio dos sintomas) desenvolveu e/ ou expôs-se atividades ligada a : Dormiu em barraca, galpão, paiol, e outros locais semelhantes.. st_atividade_ barraca | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `transpo_n` | `TRANSPO_N` | texto | Nas últimas 8 semanas (60 dias antes do inicio dos sintomas) desenvolveu e/ ou expôs-se atividades ligada a: Transporte e/ou carregamento (em veículos motorizados) de cargas em geral. st_atividade_t ransporte | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `pescou_n` | `PESCOU_N` | texto | Nas últimas 8 semanas (60 dias antes do inicio dos sintomas) desenvolveu e/ ou expôs-se atividades ligada a: Pescou, caçou ou participou de atividades de eco turismo ou similares.. st_atividade_ pesca | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `roedor_n` | `ROEDOR_N` | texto | Nas últimas 8 semanas (60 dias antes do inicio dos sintomas) desenvolveu e/ ou expôs-se atividades ligada a: Teve contato direto e/ou viu rato vivo ou morto ou suas excretas/vestígios (fezes, urina e/ou cheiro de urina, sangue, saliva, roeduras,pegadas,trilhas, manchas e outros sinais de rato). st_atividade_c ontato_rato | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `outra_ativ` | `OUTRA_ATIV` | texto | Nas últimas 8 semanas ( 60 dias antes do inicio dos sintomas) desenvolveu e/ ou expôs-se atividades ligada a : Outras atividades/ exposições. st_atividade_ outro | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `outr_ati_d` | `OUTR_ATI_D` | texto | Nas últimas 8 semanas (60 dias antes do inicio dos sintomas) desenvolveu e/ ou expôs-se atividades ligada a : Outras atividades/ exposições (outros animais ou suas instalações / outros casos humanos de hantavírus ou outras), se Outras especificar. ds_atividade_ outro | — | 2007 a 2026 |
| `cli_respi` | `CLI_RESPI` | texto | Manifestações clínicas (sinais e sintomas) Insuficiência Respiratória Aguda. st_manifestac ao_insuf_resp ira | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `cli_mial_g` | `CLI_MIAL_G` | texto | Manifestações clínicas (sinais e sintomas) Mialgia generalizada (dor em todo o corpo). st_manifestac ao_mialgia | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `cli_lombar` | `CLI_LOMBAR` | texto | Manifestações clínicas (sinais e sintomas) Dor Lombar ( dor na região dos rins). st_manifestac ao_dor_lomba r | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `cli_hipote` | `CLI_HIPOTE` | texto | Manifestações clínicas (sinais e sintomas) Hipotensão. st_manifestac ao_hipotensa o | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `cli_choque` | `CLI_CHOQUE` | texto | Manifestações clínicas (sinais e sintomas) Choque. st_manifestac ao_choque | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `cli_diarre` | `CLI_DIARRE` | texto | Manifestações clínicas (sinais e sintomas) Diarréia. st_manifestac ao_diarreia | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `cli_cardia` | `CLI_CARDIA` | texto | Manifestações clínicas (sinais e sintomas) Insuficiência Cardíaca. st_manifestac ao_insuf_card iaca | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `cli_asteni` | `CLI_ASTENI` | texto | Manifestações clínicas (sinais e sintomas) Astenia. st_manifestac ao_astenia | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `cli_petequ` | `CLI_PETEQU` | texto | Manifestações clínicas (sinais e sintomas) Petéquias (manchas de sangue sob a pele). st_manifestac ao_petequias | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `cli_hemo` | `CLI_HEMO` | texto | Manifestações clínicas (sinais e sintomas), Outras manifestações Hemorrágicas. st_ manifestacao _hemor_outro | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `am_sangue` | `AM_SANGUE` | texto | Colheu amostra de sangue para exames cllínicos/ bioquímicos. st_amostra_s angue | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `lab_hema_n` | `LAB_HEMA_N` | texto | Resultado A Hematócrito > 45%. st_resultado_ a_hematocrito | 1-Sim 2-Não 3-Não realizado 9-Ignorado | 2007 a 2026 |
| `lab_tgo` | `LAB_TGO` | texto | Resultado A TGO. st_resultado_ a_tgo | 1-Sim 2-Não 3- Não realizado 9-Ignorado | 2007 a 2026 |
| `lab_tgo_d` | `LAB_TGO_D` | texto | Especifique TGO. ds_resultado_ a_tgo | — | 2007 a 2026 |
| `lab_tgp` | `LAB_TGP` | texto | Resultado A TGP. st_resultado_ a_tgp | 1-Sim 2-Não 3-Não | 2007 a 2026 |
| `lab_tgp_d` | `LAB_TGP_D` | texto | Especifique TGP. ds_resultado_ a_tgp | — | 2007 a 2026 |
| `lab_res_b` | `LAB_RES_B` | texto | Resultado B Leucócitos. tp_resultado_ b | 1- Normais 2- Aumenta dos COM desvio a esquerda 3- Diminuíd os (Leucope nia) 4- Aumenta dos SEM desvio à esquerda 5. Não realizado 9 - Ignorado | 2007 a 2026 |
| `lab_radiol` | `LAB_RADIOL` | texto | Realizou radiografia do Tórax. st_radiografia _torax | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `lab_difuso` | `LAB_DIFUSO` | texto | Se sim, apresentou alguma destas alterações? Infiltrado Pulmonar Difuso. st_alguma_alt eracao_difuso | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `lab_local` | `LAB_LOCAL` | texto | Se sim, apresentou alguma. Se o exame radiológico | 1-Sim | 2007 a 2026 |
| `lab_derram` | `LAB_DERRAM` | texto | Se sim, apresentou alguma destas alterações? Derrame Pleural. st_alguma_alt eracao_pleura l | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `lab_colheu` | `LAB_COLHEU` | texto | Dado de exame laboratorial registrado na ficha de Hantavirose (`LAB_COLHEU`); o dicionário consultado não define o campo isoladamente | — | 2007 a 2026 |
| `dt_col_igm` | `DT_COL_IGM` | data | Data da coleta do IgM. dt_coleta_sor ologia | — | 2007 a 2026 |
| `lab_imuno` | `LAB_IMUNO` | texto | Resultado Imunohistoquimica. tp_resultado_i munohistoqui mica | 1- positivo 2- negativo 3- inconclusivo 4-não realizado | 2007 a 2026 |
| `dt_rtpcr` | `DT_RTPCR` | data | Data registrada na ficha de Hantavirose (`DT_RTPCR`); o dicionário consultado não define o campo isoladamente | — | 2007 a 2026 |
| `lab_rtpcr` | `LAB_RTPCR` | texto | Resultado RT-PCR. tp_resultado_ amostra_rt_pc r | 1- positivo 2- negativo 3- inconclusivo | 2007 a 2026 |
| `tra_cortic` | `TRA_CORTIC` | texto | Suporte Terapêutico Usou corticóide. st_terapeutico _corticoide | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `tra_cpap` | `TRA_CPAP` | texto | Suporte Terapêutico CPAP/BIPAP. st_terapeutico _cpap | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `tra_vasoat` | `TRA_VASOAT` | texto | Suporte Terapêutico Usou Drogas Vasoativas (dopamina, dobutamina ou similares). st_terapeutico _droga | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `tra_antibi` | `TRA_ANTIBI` | texto | Suporte Terapêutico Usou Antibióticos. st_terapeutico _antibiotico | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final. tp_classificac ao_final | 1-Confirmado 2-Descartado | 2007 a 2026 |
| `con_forma` | `CON_FORMA` | texto | Forma clínica. st_forma_clini ca | 1-Prodrômica ou inespecífica 2-Síndrome cardiopulmon ar por hantavirus | 2007 a 2026 |
| `criterio` | `CRITERIO` | texto | Critério Diagnóstico. st_criterio_dia gnostico | 1- Laboratorial 2-Clínico- Epidemiológi co | 2007 a 2026 |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência?. tp_autoctone_ residencia | 1 – Sim 2 – Não 3 – Indeterminad o | 2007 a 2026 |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). co_uf_infecca o | — | 2007 a 2026 |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). co_pais_infec cao | — | 2007 a 2026 |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). co_municipio_ infeccao | — | 2007 a 2026 |
| `con_amb_de` | `CON_AMB_DE` | texto | Tipo de Ambiente onde provavelmente ocorreu a infecção Outro (Especificar). ds_ambiente_ infeccao_outr o | — | 2007 a 2026 |
| `con_locali` | `CON_LOCALI` | texto | Localização do LPI em relação à Sede do Município - Km. nu_localizaca o_lpi | — | 2007 a 2026 |
| `con_local2` | `CON_LOCAL2` | texto | Localização do LPI em relação à Sede do Município - Direção. tp_localizacao _lpi | 1-Sul 2-Norte 3-Leste 4-Oeste | 2007 a 2026 |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. tp_evolucao_ caso | 1-Cura 2-Óbito por hantavirose 3Óbito por outra causa 9-Ignorado | 2007 a 2026 |
| `dt_evoluc` | `DT_EVOLUC` | data | Data do óbito ou da alta hospitalar | — | 2007 a 2026 |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao Trabalho. st_doenca_tra balho | 1-Sim 2-Não 9-Ignorado | 2007 a 2026 |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. dt_encerramn to | — | 2007 a 2026 |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | 2007 a 2026 |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | 2007 a 2026 |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | 2007 a 2026 |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | 2007 a 2026 |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | 2007 a 2026 |
| `dt_trnasrs` | `DT_TRNASRS` | data | Data de transmissão do registro (nome gravado com erro de grafia na fonte) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2007 a 2026 |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | 2007 a 2026 |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | 2007 a 2026 |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal. nu_lote_horizont al | — | 2007 a 2026 |

## No lake

- **Dataset no lake:** `datasus/sinan-hant`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 17, inteiro: 78, nulo (vazio nas amostras): 3, texto: 111.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-hant.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- grande proporção de notificações descartadas (o agravo exige exclusão de outras causas de insuficiência respiratória aguda); o campo do local provável de infecção (LPI) tem alto índice de incompletude, e as vigilâncias estaduais costumam reconstruir a LPI para assegurar a distinção entre residência e exposição; há três versões de ficha históricas (leiautes distintos por período) e os casos anuais em consolidações `BR` são poucos (total ~2,3 MB em 28 arquivos), exigindo cautela no cálculo de coeficientes. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Tipo que varia entre períodos:** `id_municip`, `id_unidade`, `dt_notific`, `cs_raca`, `nu_ano`, `sem_not`, `id_regiona`, `sem_pri`, `ano_nasc`, `id_pais`, `cli_dt_ate`, `cli_vomito`, `cli_renal`, `cli_dispne`, `cli_abdomi`, `cli_cefale`, `cli_tontur`, `cli_febre`, `cli_neurol`, `cli_tosse`, `cli_toraci`, `cli_outros`, `lab_igm_r`, `lab_trombo`, `lab_ureia` e outras aparecem com mais de um tipo nas amostras (por exemplo, inteiro em alguns períodos e texto em outros); leia a coluna `Tipo` do dicionário e converta explicitamente antes de empilhar períodos. Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Colunas que não existem em todo o período:** 128 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-hant/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-hant
quantilica datasus list sinan-hant

# 2. Baixar microdados de sinan-hant com recorte adequado à partição do dataset
quantilica datasus sync sinan-hant -o ./data --start 2007 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-hant -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-hant -o ./data/raw --parquet-dir ./data/parquet --start 2007
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de hantavirose já tratado
qdf = read_dbc("data/sinan-hant/2024/sinan-hant_2024-br@20260515.dbc", clean=True)

# Proporção de casos confirmados entre notificados, por ano
print(
    qdf.group_by("nu_ano")
    .agg(
        notificados=pl.len(),
        confirmados=(pl.col("classi_fin") == 1).sum(),
    )
    .sort("nu_ano")
    .with_columns((pl.col("confirmados") / pl.col("notificados")).alias("prop_confirm"))
)

# Letalidade entre casos confirmados
confirmados = qdf.filter(pl.col("classi_fin") == 1)
print(
    confirmados.group_by("nu_ano")
    .agg(
        casos=pl.len(),
        obitos=(pl.col("evolucao") == 2).sum(),
    )
    .sort("nu_ano")
)
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Hantavirose (ficha, instrucional e dicionário)**: https://portalsinan.saude.gov.br/hantavirose
- **Instrucional da ficha de hantavirose SINAN NET**: http://portalsinan.saude.gov.br/images/documentos/Agravos/Hantavirose/Hantavirose_v5_instr.pdf
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo Hantavirose
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
