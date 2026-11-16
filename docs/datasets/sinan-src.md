---
dataset:
  id: sinan-src
  fonte: datasus
  titulo: Síndrome da Rubéola Congênita
  resumo: Notificações de casos suspeitos de síndrome da rubéola congênita (SRC) registradas no SINAN.
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de síndrome da Rubéola Congênita
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 79
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    peso: valor decimal (ver Descrição)
    idademae: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Síndrome da Rubéola Congênita (`sinan-src`)

## Resumo

Notificações de casos suspeitos de síndrome da rubéola congênita (SRC) registradas no SINAN. Cada linha representa uma ficha de investigação de um caso suspeito, confirmado ou descartado de SRC em criança.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (dBASE comprimido)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2007 a 2026 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 20 arquivos (~194 KB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim (diretório PRELIM)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `SRC` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `SRC` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `SRCBR26.dbc`, em que `SRC` é o prefixo do agravo, `BR` indica a base nacional (o SINAN publica um único arquivo por ano para o Brasil) e `26` é o ano com 2 dígitos (2026).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-src/<partição>/sinan-src_br_2026_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
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
  - O dicionário de dados desta base (`Ficha de Investigação Síndrome da Rubéola Congênita`) está contido em `Docs_TAB_SINAN.zip`; os dicionários por agravo não são publicados como arquivos separados.

## Conteúdo

A SRC é de notificação compulsória e imediata, e integra a vigilância de doenças exantemáticas e a estratégia de eliminação da rubéola e da SRC, coordenada pela SVSA/MS (Coordenação-Geral de Vigilância das Doenças Imunopreveníveis). O Brasil recebeu a certificação de eliminação da rubéola em 2015.

O evento gerador é o nascimento ou a identificação de criança com suspeita de infecção congênita pelo vírus da rubéola (malformações cardíacas, catarata, surdez) ou de mãe com rubéola ou exposição na gestação. A ficha registra dados clínicos, laboratoriais (IgM, IgG) e a classificação final; a unidade de análise é o caso suspeito notificado.

O FTP traz arquivos nacionais anuais de 2007 a 2026, de volume muito pequeno (cerca de 190 KB no total), pois o número de casos suspeitos é baixo. Poucos casos são confirmados em anos recentes.

Usos: vigilância pós-eliminação, taxa de notificação de casos suspeitos, proporção de casos investigados e laboratorialmente classificados, e avaliação de risco de reintrodução do vírus.

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-09-25.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo real `SRCBR26.dbc` do FTP (campos da ficha do SINAN Net; o leiaute pode variar entre anos).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (individual ou negativa). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado. |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | Inteiro | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE). |
| `ID_UNIDADE` | String | Código CNES da unidade de saúde notificadora (7 dígitos). |
| `DT_DIAG` | Data (AAAAMMDD) | Data do diagnóstico. |
| `SEM_DIAG` | String | Semana epidemiológica do diagnóstico (AAAASS). |
| `NU_IDADE_N` | Inteiro codificado | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `SG_UF` | String | UF de residência. |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `DT_INVEST` | Data (AAAAMMDD) | Data da investigação. |
| `RECEM_NASC` | String | Indicador de recém-nascido. |
| `PESO` | String | Peso ao nascer. |
| `CATARATA` | String | Alteração: catarata. |
| `RETINOPA` | String | Alteração: retinopatia. |
| `GLAUCOMA` | String | Alteração: glaucoma. |
| `AUDITIVA` | String | Alteração auditiva. |
| `CARDIOPATI` | String | Alteração: cardiopatia. |
| `RETAR_PM` | String | Retardo psicomotor. |
| `MICROCEFA` | String | Microcefalia. |
| `ICTERICIA` | String | Icterícia. |
| `PURPURA` | String | Púrpura. |
| `DT_COL1` | Data (AAAAMMDD) | Data da 1ª coleta de amostra. |
| `S1_IGM` | String | Resultado IgM da 1ª amostra. |
| `S1_IGG` | String | Resultado IgG da 1ª amostra. |
| `CS_RESULTA` | String | Resultado final do exame. |
| `IDADEMAE` | Inteiro | Idade da mãe (anos). |
| `VACINACAO` | String | Situação de vacinação da mãe. |
| `DT_VACINA` | Data (AAAAMMDD) | Data da vacinação. |
| `CLASSI_FIN` | String | Classificação final do caso. |
| `CRITERIO` | String | Critério de confirmação/descarte. |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito. |
| `DT_ENCERRA` | Data (AAAAMMDD) | Data de encerramento da investigação. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno). ds_semana_notifi cacao | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação. co_municipio_not ificacao | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora. co_unidade_notifi cacao | — | todos |
| `dt_diag` | `DT_DIAG` | data | Data dos primeiros sintomas / Diagnóstico. Data dos primeiros sintomas do caso de agravo agudo. Data do diagnóstico do caso de agravo crônico e DRTs Data do acidente nos acidentes da saúde do trabalhador | — | todos |
| `sem_diag` | `SEM_DIAG` | texto | Semana epidemiológica dos primeiros sintomas/ diagnósticos. (campo interno). Semanas do calendário epidemiológico padronizado | — | todos |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2007 a 2017 |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência. co_municipio_res idencia | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil). co_pais_residenc ia | — | todos |
| `dt_invest` | `DT_INVEST` | data | Data da investigação. Data do início da investigação | — | todos |
| `recem_nasc` | `RECEM_NASC` | texto | Recém nascido. Refere-se à idade gestacional | 1- A termo 2- Prematuro (< 37 semanas) 9- Ignorado | todos |
| `peso` | `PESO` | decimal(38,3) | Peso ao nascer (em gramas) | — | todos |
| `catarata` | `CATARATA` | texto | Sinais Maiores – Grupo I Catarata. Se a criança apresentar (ou) Catarata | 1- Sim 2- Não 9- Ignorado | todos |
| `retinopa` | `RETINOPA` | texto | Sinais Maiores – Grupo I– Retinopatia pigmentar. st_sinais_retinopati a | 1- Sim 2- Não 9- Ignorado | todos |
| `glaucoma` | `GLAUCOMA` | texto | Sinais Maiores – Grupo I – Glaucoma congênito. Se a criança apresentar (ou) Glaucoma congênito | 1- Sim 2- Não 9- Ignorado | todos |
| `auditiva` | `AUDITIVA` | texto | Sinais Maiores – Grupo I–Deficiência auditiva. st_sinais_deficienci a | 1- Sim 2- Não 9- Ignorado | todos |
| `cardiopati` | `CARDIOPATI` | texto | Sinais Maiores – Grupo I – Cardiopatia congênita. st_sinais_cardiopati a | 1- Sim 2- Não 9- Ignorado | todos |
| `dscardiop` | `DSCARDIOP` | texto | Especificar Cardiopatia. ds_sinais_cardiopat ia | — | todos |
| `retar_pm` | `RETAR_PM` | texto | Sinais Menores - Grupo II – Retardo Psico-Motor. Se a criança apresentar (ou) Retardo Psico - Motor | 1- Sim 2- Não 9- Ignorado | todos |
| `microcefa` | `MICROCEFA` | texto | Sinais Menores - Grupo II – Microcefalia. st_sinais_microcefal ia | 1- Sim 2- Não 9- Ignorado | todos |
| `meningo` | `MENINGO` | texto | Sinais Menores - Grupo II – Meningoencefalite. st_sinais_meningoe ncefalite | 1- Sim 2- Não 9- Ignorado | todos |
| `hepa_esp` | `HEPA_ESP` | texto | Sinais Menores -Grupo II – Hepatoesplenomegalia. st_sinais_hepatoes plenomeg | 1- Sim 2- Não 9- Ignorado | todos |
| `ictericia` | `ICTERICIA` | texto | Sinais Menores - Grupo II – Icterícia. Se a criança apresentar (ou) Icterícia | 1- Sim 2- Não 9- Ignorado | todos |
| `purpura` | `PURPURA` | texto | Sinais Menores - Grupo II – Púrpura. Se a criança apresentar (ou) Púrpura | 1- Sim 2- Não 9- Ignorado | todos |
| `ossea` | `OSSEA` | texto | Sinais Menores - Grupo II – Alterações Ósseas. st_sinais_alteracao _ossea | 1- Sim 2- Não 9- Ignorado | todos |
| `dt_col1` | `DT_COL1` | data | Data da coleta da 1ª amostra. dt_coleta_amostra_ 1 | — | todos |
| `dt_col2` | `DT_COL2` | data | Data da coleta da 2ª amostra. dt_coleta_amostra_ 2 | — | todos |
| `dt_col3` | `DT_COL3` | data | Data da coleta da 3ª amostra. dt_coleta_amostra_ 3 | — | todos |
| `s1_igm` | `S1_IGM` | texto | Resultado dos Exames Sorológicos - criança IgM S1. Resultado da 1ª sorologia – IgM - S1 | 1- Reagente 2- Não reagente 3- Inconclusivo 4- Não realizado | todos |
| `s1_igg` | `S1_IGG` | texto | Resultado dos Exames Sorológicos IgG – S1. Resultado da 3ª sorologia - IgG - S1 | 1- Reagente 2- Não reagente 3- Inconclusivo 4- Não realizado | todos |
| `s2_igm` | `S2_IGM` | texto | Resultado dos Exames Sorológicos - criança IgM S2. Resultado da 2ª sorologia - IgM - S2 | 1- Reagente 2- Não reagente 3- Inconclusivo 4- Não realizado | todos |
| `s2_igg` | `S2_IGG` | texto | Resultado dos Exames Sorológicos IgG – S2. Resultado da 3ª sorologia - IgG - S2 | 1- Reagente 2- Não reagente 3- Inconclusivo 4- Não realizado | todos |
| `s3_igm` | `S3_IGM` | texto | Resultado dos Exames Sorológicos - criança IgM S3. Resultado da 3ª sorologia - IgM - S3 | 1- Reagente 2- Não reagente 3- Inconclusivo 4- Não realizado | todos |
| `s3_igg` | `S3_IGG` | texto | Resultado dos Exames Sorológicos IgG – S3. Resultado da 3ª sorologia - IgG - S3 | 1- Reagente 2- Não reagente 3- Inconclusivo 4- Não realizado | todos |
| `cs_sangue` | `CS_SANGUE` | texto | Detecção Viral Amostra Clínica - Sangue total. st_amostra_sangue _total | 1- Sim 2- Não 9- Ignorado | todos |
| `cs_secreca` | `CS_SECRECA` | texto | Detecção Viral Amostra Clínica - Secreção Nasofaríngea. st_amostra_nasofar ingea | 1- Sim 2- Não 9- Ignorado | todos |
| `cs_urina` | `CS_URINA` | texto | Detecção Viral Amostra Clínica - Urina. Se todos os campos da amostra clínica (sangue total, secreção nasofaríngea, urina, e liquor) = 2, 9 ou null pular para o campo 42 (Bloqueio vacinal de contatos) | 1- Sim 2- Não 9- Ignorado | todos |
| `cs_liquor` | `CS_LIQUOR` | texto | Detecção Viral Amostra Clínica - Líquor. Se todos os campos da amostra clínica (sangue total, secreção nasofaríngea, urina, e liquor) = 2, 9 ou null pular para o campo 42 (Bloqueio vacinal de contatos) | 1- Sim 2- Não 9- Ignorado | todos |
| `cs_resulta` | `CS_RESULTA` | texto | Resultado. Habilitar se algum dos campos da amostra clínica (sangue total, secreção nasofaríngea, urina, e liquor) = 1 | 1- Vírus rubéola selvagem 2 - Vírus rubéola vacinal 3 - Outros vírus 4 - Não detectado | todos |
| `ds_resu_ou` | `DS_RESU_OU` | texto | Resultado Outros Vírus especificar. Informar resultado se, outros vírus especificar | — | todos |
| `bloqueio` | `BLOQUEIO` | texto | Bloqueio Vacinal de Contatos. st_bloqueio_vacinal _contato | 1- Sim 2- Não 9- Ignorado | todos |
| `isolamento` | `ISOLAMENTO` | texto | Isolamento de Recém - Nascido na Maternidade. st_isolamento_rece m_nascido | 1- Sim 2- Não 9- Ignorado | todos |
| `idademae` | `IDADEMAE` | inteiro | Idade da mãe. Informar idade da mãe | — | todos |
| `vacinacao` | `VACINACAO` | texto | Vacinação tríplice viral (sarampo, rubéola, cachumba). st_vacinacao_triplic e_viral | 1- Sim 2- Não 9- Ignorado | todos |
| `vacinarube` | `VACINARUBE` | texto | Vacinação rubéola (monovalente). st_vacinacao_rubeo la | 1- Sim 2- Não 9- Ignorado | todos |
| `vacinadupl` | `VACINADUPL` | texto | Vacinação dupla viral (sarampo e rubéola). st_vacinacao_dupla _viral | 1- Sim 2- Não 9- Ignorado | todos |
| `dt_vacina` | `DT_VACINA` | data | Data da última dose da vacina. Informar a data da última dose da vacina caso tenha vacinado recentemente | — | todos |
| `sinais` | `SINAIS` | texto | Sinais e Sintomas. Informar se apresentou ou não sinais e sintomas de rubéola | 1- Apresentou Sintomas de Rubéola 2 - Não Apresentou Sintomas de Rubéola 9 - Ignorado | todos |
| `periodo` | `PERIODO` | texto | Período da gestação em que foi acometida/exposta. tp_periodo_gestaca o | 1- 1º trimestre 2- 2º trimestre 3- 3º trimestre 9- Ignorado | todos |
| `diag_mae` | `DIAG_MAE` | texto | Critério de confirmação de diagnóstico da mãe. tp_confirmacao_dia gnostico | 1- Laboratório 2- Vínculo - Epidemiológico 3- Clínico | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final. tp_classificacao_fin al | 1- Confirmado 2- Infecção congênita 3- Descartado | todos |
| `criterio` | `CRITERIO` | texto | Critério de Confirmação/Descarte. tp_criterio_confirma cao | 1- Laboratorial 2- Clínico 9- Ignorado | todos |
| `id_dg_des` | `ID_DG_DES` | texto | Diagnóstico de descarte | 1- Toxoplamas mose 2- Citomegaloví rus 3- Sífilis congênita 4- Outras | todos |
| `dg_out_n` | `DG_OUT_N` | texto | Diagnóstico de descarte Outras (Especificar). ds_diag_descarte_o utro | — | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução. Evolução do caso | 1- Alta 2- Óbito por SRC 3- Óbito por outras causas 9- Ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Data do encerramento do caso | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal. nu_lote_horizont al | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-src`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 15, decimal(38,3): 1, inteiro: 2, texto: 61.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-src.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- Os registros incluem muitos casos descartados; filtrar por `CLASSI_FIN` ao contar casos confirmados. Contagens por UF/ano são pequenas e sujeitas a grande variação. Dados do ano corrente são preliminares. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (UF de notificação) ou `SG_UF`/`ID_MN_RESI` (residência) conforme a pergunta, pois os dois podem diferir. Arquivos do diretório PRELIM são preliminares e substituídos pelos finais; prefira sempre os arquivos finais quando o mesmo ano existir nas duas fontes, evitando somar PRELIM e FINAIS. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 1 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-src/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-src
quantilica datasus list sinan-src

# 2. Baixar microdados de sinan-src (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-src -o ./data --start 2024 --end 2026 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-src -o ./data --docs --aux --start 2024 --end 2026 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-src -o ./data/raw --parquet-dir ./data/parquet --start 2024 --end 2026 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/SRCBR26.dbc", dataset="sinan-src")

# Contagem de notificações por UF de notificação e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Distribuição por cs_sexo, nu_ano
print(frame.group_by("cs_sexo").agg(pl.len().alias("n")).sort("n", descending=True))
print(resumo.head())
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Rubéola e SRC: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Programa Nacional de Imunizações (SVSA/MS): https://www.gov.br/saude/pt-br/vacinacao
