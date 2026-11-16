---
dataset:
  id: sinan-chik
  fonte: datasus
  titulo: Febre de Chikungunya
  resumo: 'Febre de Chikungunya do DATASUS: uma ficha de notificação/investigação de febre de Chikungunya.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2014'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de febre de Chikungunya
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 124
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras:
  - desde: 2016-01
    mudanca: ficha de investigação unificada para dengue e chikungunya
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Febre de Chikungunya (`sinan-chik`)

## Resumo

O `sinan-chik` contém os microdados das notificações e investigações epidemiológicas de casos de Febre de Chikungunya (CID-10 A92.0) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de chikungunya, digitada no SINAN Net/Sinan Online pelas unidades notificadoras. A base cobre a experiência brasileira completa da doença, pois os primeiros casos autóctones do país foram detectados em 2014, marco inicial da série no FTP.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `CHIK` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `CHIK` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `CHIKBR14.dbc` — prefixo `CHIK`, `BR` (consolidação nacional) e `14` (ano 2014, primeiro da série) até `CHIKBR25.dbc` (2025); o ano corrente fica em `PRELIM` (ex.: `CHIKBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-chik/<AAAA>/sinan-chik_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-chik/2024/sinan-chik_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (dicionários e tabulações do Sinan Net/Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominador populacional).

## Conteúdo

A febre de Chikungunya é transmitida pelos mosquitos `Aedes aegypti` e `Aedes albopictus`, causada pelo arbovírus CHIKV (família Togaviridae, gênero Alphavirus). A vigilância do agravo é gerida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), que coordena a resposta a epidemias com picos massivos nas regiões Nordeste e Sudeste. O agravo passou a ser de notificação compulsória a partir da introdução no país em 2014 e está consolidado na Portaria GM/MS nº 204/2016. O dataset é o insumo oficial para coeficientes de incidência, letalidade e monitoramento da fase crônica da doença.

O evento gerador é a **Ficha de Notificação de Conclusão de Febre de Chikungunya do SINAN**, implantada em 2014 e, desde 2016, unificada com a ficha de dengue (`Ficha_DENGCHIK`, SVS 14/03/2016) e a possibilidade de registro do campo `ID_AGRAVO` com "2-Chikungunya" (A92.0). Com isso, um mesmo leiaute DBF abriga dengue e chikungunya, sendo nécessaire filtrar o agravo para isolar os casos de chikungunya. A unidade de análise é o caso suspeito/confirmado notificado individualmente (a definição de caso suspeito envolve febre e artralgia intensa de início agudo em área com transmissão).

A série histórica registra as fases do SINAN: notificação inicial pela ficha específica de 2014 e, de 2016 em diante, o mesmo instrumento unificado do Sinan Online (fases do sistema: 2000-2006 SINAN-Windows, 2007-2013 SINAN Net, 2014+ SINAN Net/Online). A introdução do vírus ocorreu em 2014 (primeiros casos autóctones na região Norte/Nordeste) e as regiões tropicais rapidamente concentraram os maiores números; episódios epidêmicos posteriores ressaltaram a carga de artralgia crônica incapacitante e seus impactos sobre a produtividade e a rede assistencial.

Aplicações analíticas: coeficiente de incidência anual por 100 mil habitantes, proporção de casos com artralgias crónicas, letalidade da fase aguda, distribuição por faixa de idade/sexo, monitoramento de coinfecções com dengue e zika no mesmo território, e avaliação da incorporação da vacina contra chikungunya em territórios prioritários.

### Cobertura observada

- Índice do FTP (2026-10): 13 arquivos, de 2014 a 2026, 1 UF(s) com arquivos, última atualização em 2026-11-10.
- Conversão local de amostras (4 arquivo(s) Parquet, de 2014 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Eras

- **2016-01**: ficha de investigação unificada para dengue e chikungunya

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual para casos de chikungunya) |
| `ID_AGRAVO` | String | Agravo na ficha unificada — identifica a suspeição de chikungunya (A92.0) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade de saúde notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (febre de início súbito + artralgia intensa) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação (obrigatório, >= data de notificação) |
| `CLASSI_FIN` | Inteiro | Classificação final: 5 - Descartado, 13 - Chikungunya (ficha unificada) |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte (1 - Laboratório, 2 - Clínico Epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 4 - Óbito em investigação, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo/doença. Especifica a suspeição do agravo | 1-Dengue 2-Chikungunya | todos |
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
| `dt_invest` | `DT_INVEST` | data | Data da Investigação. Informar a data da investigação | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/ramo de atividade econômica. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo de atividade econômica do paciente refere-se as atividades econômicas desenvolvidas nos processos de produção do setor primário (agricultura e extrativismo); secundário (indústria) ou terciário (serviços e comércio) | — | todos |
| `febre` | `FEBRE` | texto | Sinais clínicos (Febre). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `mialgia` | `MIALGIA` | texto | Sinais clínicos (Mialgia). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `cefaleia` | `CEFALEIA` | texto | Sinais clínicos (Cefaleia). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `exantema` | `EXANTEMA` | texto | Sinais clínicos (Exantema). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `vomito` | `VOMITO` | texto | Sinais clínicos (Vômito). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `nausea` | `NAUSEA` | texto | Sinais clínicos (Náusea). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `dor_costas` | `DOR_COSTAS` | texto | Sinais clínicos (Dor nas costas). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `conjuntvit` | `CONJUNTVIT` | texto | Sinais clínicos (Conjuntivite). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `artrite` | `ARTRITE` | texto | Sinais clínicos (Artrite). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `artralgia` | `ARTRALGIA` | texto | Sinais clínicos (Artralgia intensa). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `petequia_n` | `PETEQUIA_N` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `leucopenia` | `LEUCOPENIA` | texto | Sinais clínicos (Leucopenia). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `laco` | `LACO` | texto | Sinais clínicos (Prova do laço). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `dor_retro` | `DOR_RETRO` | texto | Sinais clínicos (Dor retroorbital). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `diabetes` | `DIABETES` | texto | Doenças pré- existentes (Diabetes). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `hematolog` | `HEMATOLOG` | texto | Doenças pré- existentes (Doenças hematológicas). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `hepatopat` | `HEPATOPAT` | texto | Doenças pré- existentes (Hepatopatias). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `renal` | `RENAL` | texto | Doenças pré- existentes (Doença renal crônica). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `hipertensa` | `HIPERTENSA` | texto | Doenças pré- existentes (Hipertensão arterial). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `acido_pept` | `ACIDO_PEPT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `auto_imune` | `AUTO_IMUNE` | texto | Doenças pré- existentes (Doenças auto-imunes). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `dt_chik_s1` | `DT_CHIK_S1` | data | Exame sorológico (IgM) Chikungunya Soro 1 Data da Coleta. Data da Coleta Exame Sorológico (IgM) Chikungunya soro 1 | — | todos |
| `dt_chik_s2` | `DT_CHIK_S2` | data | Exame sorológico (IgM) Chikungunya Soro 2 Data da Coleta. Data da Coleta Exame Sorológico (IgM) Chikungunya soro 2 | — | todos |
| `dt_prnt` | `DT_PRNT` | data | Exame PRNT Data da Coleta. Data da Coleta Exame PRNT | — | todos |
| `res_chiks1` | `RES_CHIKS1` | texto | Exame sorológico (IgM) Chikungunya Soro 1 Resultado. Resultado do Exame Sorológico (IgM) soro 1 para Chikunugnya | 1-Reagente 2-Não Reagente 3-Inconclusivo 4-Não realizado | todos |
| `res_chiks2` | `RES_CHIKS2` | texto | Exame sorológico (IgM) Chikungunya Soro 2 Resultado. Resultado do Exame Sorológico (IgM) soro 2 para Chikunugnya | 1-Reagente 2-Não Reagente 3-Inconclusivo 4-Não realizado | todos |
| `resul_prnt` | `RESUL_PRNT` | texto | Exame PRNT Resultado. Resultado do Exame Sorológico (IgM) PRNT | 1-Reagente 2-Não Reagente 3-Inconclusivo 4-Não realizado | todos |
| `dt_soro` | `DT_SORO` | data | Exame sorológico (IgM) Dengue Data da Coleta. Data da Coleta Exame Sorológico (IgM) Dengue | — | todos |
| `resul_soro` | `RESUL_SORO` | texto | Exame sorológico (IgM) Dengue Resultado. Resultado do Exame Sorológico (IgM) Dengue | 1-Reagente 2-Não Reagente 3-Inconclusivo 4-Não realizado | todos |
| `dt_ns1` | `DT_NS1` | data | Exame NS1 Data da Coleta. dt_coleta_NS1 | — | todos |
| `resul_ns1` | `RESUL_NS1` | texto | Exame NS1 Resultado. Tp_result_NS1 | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | todos |
| `dt_viral` | `DT_VIRAL` | data | Isolamento Viral Data da Coleta. Data da Coleta Isolamento Viral | — | todos |
| `resul_vi_n` | `RESUL_VI_N` | texto | Isolamento Viral Resultado. Resultado Exame de Isolamento Viral | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | todos |
| `dt_pcr` | `DT_PCR` | data | RT-PCR Data da Coleta. Data de Coleta do Exame de RT-PCR | — | todos |
| `resul_pcr_` | `RESUL_PCR_` | texto | RT-PCR Resultado. Resultado do Exame de RT-PCR | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | todos |
| `sorotipo` | `SOROTIPO` | texto | Sorotipo | 1-DEN 1 2-DEN 2 3 DEN 3 4-DEN 4 | todos |
| `histopa_n` | `HISTOPA_N` | texto | Histopatologia Resultado | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | todos |
| `imunoh_n` | `IMUNOH_N` | texto | Imunohistoquímica Resultado | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | todos |
| `hospitaliz` | `HOSPITALIZ` | texto | Ocorreu Hospitalização? | 1-Sim 2-Não 9-Ignorado | todos |
| `dt_interna` | `DT_INTERNA` | data | Data Da Internação. Informar a data de internação do paciente | — | todos |
| `uf_hospital` | `UF` | texto | UF do hospital de internação (coluna `UF` da fonte, renomeada pelo conversor porque `uf` é coluna do lake) | — | todos |
| `municipio` | `MUNICIPIO` | texto | Municipio Do Hospital. VARCHAR (6) | — | todos |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência? | 1 – Sim 2 – Não 3 – Indeterminado | todos |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o paciente foi provavelmente infectado | — | todos |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente infectado | — | todos |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). o | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação. VARCHAR (1) | 5-Descartado 10-Dengue 11-Dengue com sinais de alarme 12-Dengue grave 13-Chikungunya | todos |
| `criterio` | `CRITERIO` | texto | Critério De Confirmação/Descarte. o | 1-Laboratório 2-Clínico Epidemiológico 3-Em investigação | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `clinc_chik` | `CLINC_CHIK` | texto | Manifestação clínica registrada na ficha de Febre de Chikungunya (`CLINC_CHIK`); o dicionário consultado não define o campo isoladamente | — | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução Do Caso. VARCHAR (1) | 1- cura 2- óbito pelo agravo 3- óbito por outras causas 4- óbito em investigação 9- ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do Óbito. Informar a data do óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data Do Encerramento. Informar a data do encerramento do caso | — | todos |
| `alrm_hipot` | `ALRM_HIPOT` | texto | Dengue com sinais de alarme (Hipotensão). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | todos |
| `alrm_plaq` | `ALRM_PLAQ` | texto | Dengue com sinais de alarme (Queda abrupta de plaquetas). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | todos |
| `alrm_vom` | `ALRM_VOM` | texto | Dengue com sinais de alarme (Vômitos persistentes). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | todos |
| `alrm_sang` | `ALRM_SANG` | texto | Dengue com sinais de alarme (Sangramento de mucosa/outras hemorragias). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | todos |
| `alrm_hemat` | `ALRM_HEMAT` | texto | Dengue com sinais de alarme (Aumento hematócrito). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | todos |
| `alrm_abdom` | `ALRM_ABDOM` | texto | Dengue com sinais de alarme. Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | todos |
| `alrm_letar` | `ALRM_LETAR` | texto | Dengue com sinais de alarme (Letargia ou irritabilidade). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | todos |
| `alrm_hepat` | `ALRM_HEPAT` | texto | Dengue com sinais de alarme (Hepatomegalia). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | todos |
| `alrm_liq` | `ALRM_LIQ` | texto | Dengue com sinais de alarme (Acúmulo de líquidos). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | todos |
| `dt_alrm` | `DT_ALRM` | data | Dengue com sinais de alarme Data de início dos sintomas. Informar data de início dos sinais de alarme. Considerar a data do primeiro sinal de alarme manifestado | — | todos |
| `grav_pulso` | `GRAV_PULSO` | texto | Dengue grave (Pulso débil ou indectável). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_conv` | `GRAV_CONV` | texto | Dengue grave (PA convergente). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_ench` | `GRAV_ENCH` | texto | Dengue grave (Tempo de enchimento capilar). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_insuf` | `GRAV_INSUF` | texto | Dengue grave (Acúmulo de líquidos com insuficiência respiratória). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_taqui` | `GRAV_TAQUI` | texto | Dengue grave (Taquicardia). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_extre` | `GRAV_EXTRE` | texto | Dengue grave (Extremidade frias). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_hipot` | `GRAV_HIPOT` | texto | Dengue grave (Hipotensão arterial em fase tardia). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_hemat` | `GRAV_HEMAT` | texto | Dengue grave (Hematêmese). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_melen` | `GRAV_MELEN` | texto | Dengue grave (Melena). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_metro` | `GRAV_METRO` | texto | Dengue grave (Metrorragia volumosa). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_sang` | `GRAV_SANG` | texto | Dengue grave (Sangramento do SNC). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_ast` | `GRAV_AST` | texto | Dengue grave (AST/ALT >1.000). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_mioc` | `GRAV_MIOC` | texto | Dengue grave (Miocardite). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_consc` | `GRAV_CONSC` | texto | Dengue grave (Alteração da consciência). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | todos |
| `grav_orgao` | `GRAV_ORGAO` | texto | Dengue grave (Outros órgãos). Informar qual sinal de gravidade foi encontrado | — | todos |
| `dt_grav` | `DT_GRAV` | data | Dengue grave Data de início dos sintomas. Informar data de início dos sinais de alarme. Considerar a data do primeiro sinal de alarme manifestado | — | todos |
| `mani_hemor` | `MANI_HEMOR` | texto | Manifestação clínica registrada na ficha de Febre de Chikungunya (`MANI_HEMOR`); o dicionário consultado não define o campo isoladamente | — | todos |
| `epistaxe` | `EPISTAXE` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `gengivo` | `GENGIVO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `metro` | `METRO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `petequias` | `PETEQUIAS` | texto | Sinais e Sintomas Petéquias. Informar se o paciente teve sinais/sintomas de Petéquias | 1- Sim 2- Não 9- Ignorado | todos |
| `hematura` | `HEMATURA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `sangram` | `SANGRAM` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `laco_n` | `LACO_N` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `plasmatico` | `PLASMATICO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `evidencia` | `EVIDENCIA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `plaq_menor` | `PLAQ_MENOR` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `con_fhd` | `CON_FHD` | texto | Dado de conclusão do caso na ficha de Febre de Chikungunya (`CON_FHD`): classificação, critério de confirmação, local provável de infecção ou evolução | — | todos |
| `complica` | `COMPLICA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `tp_sistema` | `TP_SISTEMA` | texto | Sistema de origem do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nduplic_n` | `NDUPLIC_N` | texto | Não Listar/ Não Contar. 0 ou branco – Não identificado 1 – Não é duplicidade (não listar) 2 – Duplicidade (não contar) | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `cs_flxret` | `CS_FLXRET` | texto | Fluxo de retorno. Identifica se o registro está habilitado ou foi enviado pelo fluxo de retorno para o município de residência | 0 - Não 1 - habilitado para envio. 2 - enviado | todos |
| `flxrecebi` | `FLXRECEBI` | texto | Recebida por fluxo de retorno (campo interno). Colocar a estrutura do nº atribuído pelo sistema | — | todos |
| `migrado_w` | `MIGRADO_W` | texto | Identifica migração (campo interno). Identifica se o registro é oriundo da rotina de migração da base Windows | 1- migrado do Sinan Windows | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-chik`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 16, inteiro: 1, texto: 107.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-chik.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- há transição de leiaute de ficha — entre 2014 e 2015 a notificação usa a ficha específica de chikungunya e, a partir de 2016, a ficha unificada Dengue/Chikungunya (casos notificados pelo instrumento antigo têm os campos novos de investigação preenchidos com categorias padrão, como 2 - Não); o volume é alto e concentrado em 13 consolidações `BR` anuais, com o arquivo do ano corrente em `PRELIM` ainda sujeito a revisão; a filtragem por `ID_AGRAVO`/`CLASSI_FIN` é obrigatória para separar chikungunya de dengue no mesmo leiaute. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-chik").glob("**/*.parquet"))
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
datasus-fetcher list sinan-chik

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-chik -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-chik
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Dengue/Chikungunya**: https://portalsinan.saude.gov.br/sinan-dengue-chikungunya
- **Ficha e dicionário de dados da ficha unificada**: https://portalsinan.saude.gov.br/images/documentos/Agravos/Dengue/Ficha_DENGCHIK_FINAL.pdf
- **Portaria GM/MS nº 204/2016** (notificação compulsória) e **Guia de Vigilância em Saúde** (SVSA/MS, capítulo de chikungunya)
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
