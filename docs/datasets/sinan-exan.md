---
dataset:
  id: sinan-exan
  fonte: datasus
  titulo: Doenças exantemáticas
  resumo: 'Doenças exantemáticas do DATASUS: uma ficha de notificação/investigação de doenças exantemáticas.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de doenças exantemáticas
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 109
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    menor_5ano: 'número inteiro: contagem ou código numérico (ver Descrição)'
    de5a14anos: 'número inteiro: contagem ou código numérico (ver Descrição)'
    de15a39ano: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Doenças exantemáticas (`sinan-exan`)

## Resumo

O `sinan-exan` contém os microdados das notificações e investigações epidemiológicas de casos suspeitos de doenças exantemáticas (sarampo, CID-10 B05, e rubéola, CID-10 B06) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de sarampo ou rubéola, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. Com 108 colunas no leiaute da ficha v5.0 (revisão março/2012), a ficha unificada cobre o quadro clínico (febre, exantema, tosse, coriza, conjuntivite, artralgia, linfadenopatia retroauricular), o histórico vacinal, o esquema de bloqueio vacinal e as coletas seriadas de sorologias (IgM/IgG em amostras 1 e 2 e repetição), sustentando os programas de eliminação do sarampo e da vigilância da síndrome da rubéola congênita (SRC).

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim — todos os arquivos estão em `PRELIM`; `meta.py` também consulta `FINAIS`, que hoje não contém arquivos do agravo
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `EXAN` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `EXAN` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `EXANBR25.dbc` — `EXAN` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). Não há arquivos em `FINAIS` para o agravo: toda a série (2007 a 2026) está em `PRELIM` (ex.: `EXANBR26.dbc`, atualização de 23/09/2026).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-exan/<AAAA>/sinan-exan_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-exan/2024/sinan-exan_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

Sarampo e rubéola são agravos de notificação compulsória universal (Lei nº 6.259/1975 e Decreto nº 78.231/1976, hoje na Portaria GM/MS nº 204/2016), monitorados pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) por meio da vigilância de doenças exantemáticas — instrumento central dos programas de eliminação do sarampo e da vigilância da síndrome da rubéola congênita (SRC), com suporte dos laboratórios de referência (Fiocruz/RJ e Adolfo Lutz). Toda pessoa com febre + exantema + tosse/coriza/conjuntivite deve ser notificada e investigada dentro de 48 horas, com bloqueio vacinal dos contatos e coletas laboratoriais, para que o Brasil demonstre manutenção da eliminação do sarampo certificada — a base detecta casos importados, cadenas de transmissão endêmica e surtos.

O evento gerador deste dataset é a **Ficha de Notificação Individual das Doenças Exantemáticas** (sarampo/rubéola; ficha v5.0). A notificação nasce com a suspeição clínica (febre + exantema maculopapular + tosse, coriza ou conjuntivite) e é completada com o contato com caso suspeito até 23 dias antes (`CS_FONTE`), o bloqueio vacinal (`CS_VACINAL`), as coletas de amostras ('1ª e 2ª sorologias: `DT_COL_1`, `DT_COL_2`, resultantes `ID_S1_IGM/ID_S1_IGG`, `ID_S2_*`, repetição `ID_RE_*`) e, quando encerrado, a etiologia final (sarampo/rubéola/descartado). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. A base é publicada em consolidações revisadas periodicamente — todas estão em `PRELIM`. O instrumento unificou as fichas antigas de sarampo e rubéola em uma única ficha de doenças exantemáticas, no contexto da eliminação formal da rubéola nas Américas (2009) e da manutenção do certificado de eliminação do sarampo — a base é essencial para detectar casos importados e surtos de sarampo, como as grandes ondas registradas em 2018 e posteriormente.

Aplicações analíticas típicas: monitoramento de casos suspeitos e confirmados de sarampo por classificação (`CLASSI_FIN` 1/2 vs descartados), percentual de casos com IgM reagente (`ID_S1_IGM`), cumprimento do prazo de investigação em 48 horas (diferença entre `DT_NOTIFIC` e `DT_INVEST`) e realização de bloqueio vacinal dos contos dientes (`CS_VACINAL`); vigilância da rubéola de mulheres em idade fértil e das SRC gestantes pelo árvore de investigação do grupo de casos compatíveis; e análise de casos importados pela fonte de infecção (`COUFINF`/`COPAISINF`).

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-11-09.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `EXANBR25.dbc` (108 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CS_SUSPEIT` | Inteiro | Tipo de caso: suspeito de sarampo, rubéola ou caso compatível com doença exantemática |
| `DT_NOTIFIC` / `SEM_NOT` / `NU_ANO` | Data / Inteiro | Data, semana epidemiológica e ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `ID_UNIDADE` | String (7) | Código CNES da unidade notificadora |
| `DT_SIN_PRI` / `SEM_PRI` | Data / Inteiro | Data e semana de início dos sintomas |
| `NU_IDADE_N` / `CS_SEXO` / `CS_RACA` / `CS_ESCOL_N` | Inteiro/String | Idade decomposta por unidade, sexo, raça/cor e escolaridade |
| `CS_VACINA` / `DT_DOSE_N` | Inteiro / Data | Tomou vacina dupla ou triviral (1 - Sim, 2 - Não, 9 - Ignorado) e data da última dose |
| `CS_FONTE` | Inteiro | Contato com caso suspeito/confirmado de sarampo ou rubéola até 23 dias antes do início dos sintomas (domicílio, creche/escola, posto de saúde/hospital, outro Estado/Município) |
| `DT_FEBRE` / `DT_INICIO_` | Data (`AAAAMMDD`) | Data do início da febre e do exantema |
| `ID_TOSSE`/`ID_CORIZA`/`ID_CONJUNT`/`ID_ARTRALG`/`ID_GANGLIO`/`ID_RETRO` | Inteiro | Sinais e sintomas: tosse, coriza, conjuntivite, artralgia, linfadenopatias gerais e retroauriculares |
| `ID_HOSPIT` / `DT_INTERNA` / `UF_H` / `NM_MUN_HOS` | Inteiro/Data/String | Hospitalização, data da internação e local |
| `DT_COL_1` / `DT_COL_2` | Data | Datas das coletas de sangue (1ª e 2ª amostras para sorologia) |
| `ID_S1_IGM`/`ID_S1_IGG`/`ID_S2_IGM`/`ID_S2_IGG` | Inteiro | Resultados de IgM e IgG na 1ª e 2ª amostras (positivo/negativo/inconclusivo/não realizado) |
| `ID_S1_IGM_`/`ID_S1_IGG_`/`ID_S2_*`/`ID_RE_*` | Inteiro | Resultados complementares/repetidos das sorologias (menciona o laboratório de referência) |
| `TPEXANTE` | Inteiro | Situação da investigação de doença exantemática |
| `ID_SANGUE`/`ID_URINA`/`ID_SECRECA`/`ID_LIQUOR` | Inteiro | Coleta de outros materiais (sangue, urina, secreção, líquor) |
| `ID_ETIOLOG` / `ETIOL_OUTR` | Inteiro/String | Outra etiologia investigada e descrição (ex.: dengue, parvovírus B19, enterovírus) |
| `CS_VACINAL` | Inteiro | Bloqueio vacinal realizado (todos vacinados, parte vacinados, sem história de contato, não realizado) |
| `MENOR_5ANO`/`DE5A14ANOS`/`DE15A39ANO`/`INT_TEMPO` | Inteiro | Bloqueios vacinais por grupos etários e intervalo entre início dos sintomas e notificação |
| `CLASSI_FIN` | Inteiro | Classificação final: 1 - Sarampo, 2 - Rubéola, 3 - Descartado |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte: 1 - Laboratorial, 2 - Vínculo Epidemiológico, 3 - Clínico, 4 - Data da última dose da vacina |
| `CS_DESCART` | Inteiro | Motivo do descarte (ex.: exame IgM negativo, vacinados sem exame, conf. exantemático com outra etiologia) |
| `COUFINF`/`COPAISINF`/`COMUNINF` | String | UF, país e município prováveis da fonte de infecção (autoctonia/importação) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito por doença exantemática, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` / `DT_ENCERRA` / `DT_DESC*` | Data (`AAAAMMDD`) | Datas do óbito, de encerramento e das despesas relacionadas à comunicação de surtos |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
| `cs_suspeit` | `CS_SUSPEIT` | texto | Tipo suspeito 1 - Sarampo / 2 - Rubéola. Identifica se a suspeita na notificação foi de sarampo ou rubéola | — | todos |
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
| `cs_flxret` | `CS_FLXRET` | texto | Fluxo de retorno. Identifica se o registro está habilitado ou foi enviado pelo fluxo de retorno para o município de residência | 0 - Não 1 - habilitado para envio. 2 - enviado | todos |
| `flxrecebi` | `FLXRECEBI` | texto | Recebida por fluxo de retorno (campo interno). Colocar a estrutura do nº atribuído pelo sistema | — | todos |
| `migrado_w` | `MIGRADO_W` | texto | Identifica migração (campo interno). Identifica se o registro é oriundo da rotina de migração da base Windows | 1- migrado do Sinan Windows | todos |
| `dt_invest` | `DT_INVEST` | data | Data da investigação. Data em que ocorreu a investigação – informar a Data da 1ª visita ao paciente | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo de atividade econômica do paciente refere-se as atividades econômicas desenvolvidas nos processos de produção do setor primário (agricultura e extrativismo); secundário (indústria) ou terciário (serviços e comércio) | — | todos |
| `cs_vacina` | `CS_VACINA` | texto | Tomou vacina contra sarampo e rubéola (dupla ou triviral). Informa se o paciente já foi vacinado ou não, contra sarampo e rubéola (vacina dupla ou tríplice viral), após verificar documentação/caderneta | 1 - sim 2 - não 9 - ignorado | todos |
| `dt_dose_n` | `DT_DOSE_N` | data | Data da ultima dose. data da última dose da vacina contra tríplice viral ou dupla viral que o paciente tomou | — | todos |
| `cs_fonte` | `CS_FONTE` | texto | Contato com caso suspeito ou confirmado de sarampo ou rubéola (até 23 dias antes do início dos sinais e sintomas). local em que o paciente teve contato c/ suspeito ou confirmado de sarampo ou rubéola (até 23 dias antes do início dos sinais e sintomas) | 1-Domicílio 2-Vizinhança 3-Trabalho 4- Creche/escol a 5-Posto de saúde/hospit al 6-Outro Estado /Município 7-Sem história de | todos |
| `dt_inicio_` | `DT_INICIO_` | data | Data do inicio do exantema (manchas vermelhas no corpo). Data do início do exantema | — | todos |
| `dt_febre` | `DT_FEBRE` | data | Data do inicio da febre. Data do início da febre | — | todos |
| `id_tosse` | `ID_TOSSE` | texto | Outros sinais e sintomas (tosse). Informa se o paciente apresentou tosse | 1-sim 2-não 9-ignorado | todos |
| `id_coriza` | `ID_CORIZA` | texto | Outros sinais e sintomas (coriza, nariz escorrendo). Informa se o paciente apresentou coriza | 1-sim 2-não 9-ignorado | todos |
| `id_conjunt` | `ID_CONJUNT` | texto | Outros sinais e sintomas (conjuntivite, olhos avermelhados). Informa se o paciente apresentou conjuntivite | 1-sim 2-não 9-ignorado | todos |
| `id_artralg` | `ID_ARTRALG` | texto | Outros sinais e sintomas (artralgia/artrite, dores nas juntas). Informa se o paciente apresentou artralgia/artrite | 1-sim 2-não 9-ignorado | todos |
| `id_ganglio` | `ID_GANGLIO` | texto | Outros sinais e sintomas (presença de gânglios retroauriculares/occ ipitais, caroço atrás da orelha). Informa se o paciente apresentou presença de gânglios retroauriculares/occipitais | 1-sim 2-não 9-ignorado | todos |
| `id_retro` | `ID_RETRO` | texto | Outros sinais e sintomas (dor retro- auricular, dor acima dos olhos). Informa se o paciente apresentou dor retro auricular | 1-sim 2-não 9-ignorado | todos |
| `id_hospit` | `ID_HOSPIT` | texto | Ocorreu hospitalização | 1-sim 2-não 9-ignorado | todos |
| `dt_interna` | `DT_INTERNA` | data | Data da internação. Informa a data de internação, caso tenha ocorrido | — | todos |
| `uf_h` | `UF_H` | texto | UF. Informe a sigla da UF onde o paciente foi internado | — | todos |
| `nm_mun_hos` | `NM_MUN_HOS` | texto | Nome do município do hospital (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_col_1` | `DT_COL_1` | data | Exame sorológico (data da coleta da 1ª amostra s1). Data coleta da 1ª sorologia | — | todos |
| `dt_col_2` | `DT_COL_2` | data | Exame sorológico (data da coleta da 2ª amostra – s2). Data da coleta da 2ª amostra para sorologia | — | todos |
| `id_s1_igm` | `ID_S1_IGM` | texto | Resultado do exame IgM s1 para sarampo. Resultado da 1ª amostra para sorologia para sarampo – IgM | 1-Reagente 2-Não Reagente 3- Inconclusivo | todos |
| `id_s1_igg` | `ID_S1_IGG` | texto | Resultado do exame IgG s1 para sarampo. Resultado da 1ª sorologia para sarampo – IgG | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `id_s1_igm_` | `ID_S1_IGM_` | texto | Resultado do exame IgM s1 para rubéola. Resultado da 1ª sorologia para rubéola - IgM | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `id_s1_igg_` | `ID_S1_IGG_` | texto | Resultado do exame IgG s1 para rubéola. Resultado da 1ª sorologia para rubéola – IgG | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `id_s1_ig_1` | `ID_S1_IG_1` | texto | Resultado do exame IgM s1 para outras exantemáticas. Resultado da 1ª sorologia para outras exantemáticas - IgM | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `id_s1_ig_2` | `ID_S1_IG_2` | texto | Resultado do exame IgG s1 para outras exantemáticas. Resultado da 1ª sorologia para outras exantemáticas - IgG | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `id_s2_igm` | `ID_S2_IGM` | texto | Resultado do exame IgM s2 para sarampo. Resultado da 2ª sorologia para sarampo – IgM | 1-Reagente 2-Não Reagente | todos |
| `id_s2_igg` | `ID_S2_IGG` | texto | Resultado do exame IgG s2 para sarampo. Resultado da 2ª sorologia para sarampo - IgG | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `id_s2_igm_` | `ID_S2_IGM_` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Doenças exantemáticas (`ID_S2_IGM_`); o dicionário consultado não define o campo isoladamente | — | todos |
| `id_s2_igg_` | `ID_S2_IGG_` | texto | Resultado do exame IgG s2 para rubéola. Resultado da 2ª sorologia para rubéola - IgG | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `id_s2_ig_1` | `ID_S2_IG_1` | texto | Resultado do exame IgM s2 para outras exantemáticas. Resultado da 2ª sorologia para outras exantemáticas - IgM | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `id_s2_ig_2` | `ID_S2_IG_2` | texto | Resultado do exame IgG s2 para outras exantemáticas. Resultado da 2ª sorologia para outras exantemáticas – IgG | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `id_re_igm` | `ID_RE_IGM` | texto | Resultado do exame IgM re-teste. e | 1-Reagente 2-Não | todos |
| `id_re_igg` | `ID_RE_IGG` | texto | Resultado do exame IgG re-teste para sarampo. e | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `id_re_igm_` | `ID_RE_IGM_` | texto | Resultado do exame IgM re-teste para rubéola. Resultado do re-teste de sorologia para rubéola - IgM | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `id_re_igg_` | `ID_RE_IGG_` | texto | Resultado do exame IgG re-teste para rubéola. Resultado do re-teste de sorologia para rubéola - IgG | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `id_re_ig_1` | `ID_RE_IG_1` | texto | Resultado do exame IgM re-teste para outras exantemáticas. Resultado do re-teste de sorologia para outras exantemáticas - IgM | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `id_re_ig_2` | `ID_RE_IG_2` | texto | Resultado do exame IgG re-teste outras exantemáticas. Resultado do re-teste de sorologia para outras exantemáticas - IgG | 1-Reagente 2-Não Reagente 3- Inconclusivo 4-Não realizado | todos |
| `tpexante` | `TPEXANTE` | texto | Outras. Identificação da outra | 1-Dengue | todos |
| `id_sangue` | `ID_SANGUE` | texto | Isolamento viral Amostra clínica coletada Sangue total. Informa se foi colhido sangue para realização de isolamento viral | 1-sim 2-não 9-Ignorado | todos |
| `id_urina` | `ID_URINA` | texto | Amostra clínica coletada Urina. Informa se foi colhido urina para realização de isolamento viral | 1-sim 2-não 9-Ignorado | todos |
| `id_secreca` | `ID_SECRECA` | texto | Amostra clínica coletada Secreção nasofaríngea | 1-sim 2-não 9-Ignorado | todos |
| `id_liquor` | `ID_LIQUOR` | texto | Amostra clínica coletada Liquor. Informa se foi colhido LIQUOR para realização de isol. viral | 1-sim 2-não 9-Ignorado | todos |
| `id_etiolog` | `ID_ETIOLOG` | texto | Etiologia viral. Etiologia do vírus detectado | 1-Vírus Sarampo Selvagem 2-Vírus Sarampo Vacinal 3-Vírus Rubéola Selvagem 4-Vírus Rubéola Vacinal 5-Dengue 6-Herpes Vírus Tipo 6 | todos |
| `etiol_outr` | `ETIOL_OUTR` | texto | Etiologia Viral se Outras especificar. Habilitar se campo 50 - Etiologia Viral = 9 | — | todos |
| `cs_vacinal` | `CS_VACINAL` | texto | Realizou bloqueio vacinal. Informa se foi realizado bloqueio vacinal | 1-Sim 2-Não 3-Não, todos vacinados 4-Não, sem história de contato 9-Ignorado | todos |
| `menor_5ano` | `MENOR_5ANO` | inteiro | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `de5a14anos` | `DE5A14ANOS` | inteiro | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `de15a39ano` | `DE15A39ANO` | inteiro | Em caso afirmativo, indique a quantidade de suscetíveis vacinados De 15 a 39 anos. nº de pessoas vacinadas na faixa etária | — | todos |
| `int_tempo` | `INT_TEMPO` | texto | Em caso afirmativo, especifique intervalo de tempo | 1-Em até 72 horas 2-Após 72 horas 9-Ignorado | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação. Classificação final do | 1-Sarampo | todos |
| `criterio` | `CRITERIO` | texto | Critério de confirmação / descarte. critério utilizado para confirmação ou descarte da suspeita de sarampo ou de rubéola | 1- Laboratorial 2-Vínculo Epidemiológi co 3-Clínico 4-Data da última dose da vacina | todos |
| `cs_descart` | `CS_DESCART` | texto | Motivo do descarte do caso (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de. a | 1 – Sim 2 – Não | todos |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o paciente foi provavelmente infectado | — | todos |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente infectado | — | todos |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). Código do município onde o paciente foi provavelmente infectado. O nome está associado ao código na tabela de municípios | — | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. evolução do caso confirmado | 1. cura 2. óbito por doença exantemátic a 3.óbito por outras causas 9. ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito. Data em que ocorreu o óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Data do encerramento do caso | — | todos |
| `dt_desc1` | `DT_DESC1` | data | Informações complementares e observações Data de deslocamento 1. informar data de deslocamento 1 | — | todos |
| `dt_desc2` | `DT_DESC2` | data | Informações complementares e observações Data de deslocamento 2. informar data de deslocamento 2 | — | todos |
| `dt_desc3` | `DT_DESC3` | data | Informações complementares e observações Data de deslocamento 3. informar data de deslocamento 3 | — | todos |
| `co_uf_des1` | `CO_UF_DES1` | texto | Informações complementares e observações UF deslocamento 1. 1 | — | todos |
| `co_uf_des2` | `CO_UF_DES2` | texto | Informações complementares e observações UF deslocamento 2. 2 | — | todos |
| `co_uf_des3` | `CO_UF_DES3` | texto | Informações complementares e. 3 | — | todos |
| `mun_des1` | `MUN_DES1` | texto | Informações complementares e observações Município deslocamento 1. mento_1 | — | todos |
| `mun_des2` | `MUN_DES2` | texto | Informações complementares e observações Município deslocamento 2. mento_2 | — | todos |
| `mun_des3` | `MUN_DES3` | texto | Informações complementares e observações Município deslocamento 3. mento_3 | — | todos |
| `pa_des1` | `PA_DES1` | texto | Informações complementares e observações País deslocamento 1. o_1 | — | todos |
| `pa_des2` | `PA_DES2` | texto | Informações complementares e observações País deslocamento 2. o_2 | — | todos |
| `pa_des3` | `PA_DES3` | texto | Informações complementares e observações País deslocamento. o_3 | — | todos |
| `ds_trans1` | `DS_TRANS1` | texto | Informações complementares e observações Meio de transporte 1. informar o meio de transporte de deslocamento 1 | — | todos |
| `ds_trans2` | `DS_TRANS2` | texto | Informações complementares e observações Meio de transporte 2. informar o meio de transporte de deslocamento 2 | — | todos |
| `ds_trans3` | `DS_TRANS3` | texto | Informações complementares e observações Meio de transporte 3. informar o meio de transporte de deslocamento 3 | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-exan`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 21, inteiro: 4, nulo (vazio nas amostras): 2, texto: 84.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-exan.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- os fluxos de sorologia em cadeia (1ª amostra, 2ª amostra e repetida) devem ser interpretados por amostra no cálculo de confirmados; o descarte tem motivo codificado (`CS_DESCART`) e datas específicas (`DT_DESC*`); toda a série está em `PRELIM`, com dados sujeitos a revisão; e, diferentemente das demais fichas do SINAN, `CLASSI_FIN` = 1 significa Sarampo e 2 significa Rubéola (a opção de descartado é 3). (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-exan").glob("**/*.parquet"))
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
datasus-fetcher list sinan-exan

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-exan -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-exan
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Doenças Exantemáticas (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulos de sarampo, rubéola e síndrome da rubéola congênita; Plano Nacional de Solução de Surtos do MS (manual do sistema de notificação e vigilância do sarampo)
