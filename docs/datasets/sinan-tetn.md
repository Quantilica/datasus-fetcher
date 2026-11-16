---
dataset:
  id: sinan-tetn
  fonte: datasus
  titulo: Tétano Neonatal
  resumo: 'Tétano Neonatal do DATASUS: uma ficha de notificação/investigação de tétano Neonatal.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de tétano Neonatal
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 86
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    idade_mae: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  - coluna: dt_nasc
    categoria: data de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Tétano Neonatal (`sinan-tetn`)

## Resumo

Notificações de casos de tétano neonatal registradas no SINAN. Cada linha representa uma ficha de investigação de um caso suspeito ou confirmado de tétano em recém-nascido (até 28 dias de vida).

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `TETN` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `TETN` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `TETNBR26.dbc`, em que `TETN` é o prefixo do agravo, `BR` indica a base nacional (o SINAN publica um único arquivo por ano para o Brasil) e `26` é o ano com 2 dígitos (2026).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-tetn/<AAAA>/sinan-tetn_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-tetn/2024/sinan-tetn_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
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
  - O dicionário de dados desta base (`Ficha de Investigação Tétano Neonatal`) está contido em `Docs_TAB_SINAN.zip`; os dicionários por agravo não são publicados como arquivos separados.

## Conteúdo

O tétano neonatal é de notificação compulsória e imediata, e acompanhado pela SVSA/MS (Coordenação-Geral de Vigilância das Doenças Imunopreveníveis). O Brasil eliminou o tétano neonatal como problema de saúde pública (menos de 1 caso por 1.000 nascidos vivos por município), e cada caso é tratado como evento sentinela de falha na vacinação da gestante ou no cuidado do parto e do coto umbilical.

O evento gerador é o adoecimento de recém-nascido com sinais compatíveis (incapacidade de sucção, rigidez, espasmos) nos primeiros 28 dias de vida. A ficha investiga história vacinal da mãe, local e condições do parto, manejo do coto umbilical, evolução e classificação final. A unidade de análise é o caso notificado.

O FTP traz 13 arquivos nacionais anuais, de 2014 a 2026, de volume mínimo (cerca de 35 KB no total), pois os casos confirmados são muito raros. O número de registros é dominado por suspeitas que foram descartadas.

Usos: monitoramento da manutenção da eliminação, investigação de falhas na vacinação antitetânica (dT/dTpa) em gestantes, na assistência ao parto e na atenção ao recém-nascido.

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-11-12.
- Conversão local de amostras (4 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo real `TETNBR26.dbc` do FTP (campos da ficha do SINAN Net; o leiaute pode variar entre anos).

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
| `DT_SIN_PRI` | Data (AAAAMMDD) | Data dos primeiros sintomas. |
| `ANO_NASC` | String | Ano de nascimento. |
| `NU_IDADE_N` | Inteiro codificado | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `SG_UF` | String | UF de residência. |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `DT_INVEST` | Data (AAAAMMDD) | Data da investigação. |
| `ID_OCUPA_N` | String | Ocupação (CBO, 6 dígitos). |
| `CS_VACTETA` | String | Situação de vacinação antitetânica. |
| `DT_1_DOSE` | Data (AAAAMMDD) | Data da 1ª dose da vacina. |
| `DT_REFORCO` | Data (AAAAMMDD) | Data do reforço. |
| `IDADE_MAE` | Inteiro | Idade da mãe (tétano neonatal). |
| `CS_TRISMO` | String | Sinal clínico: trismo. |
| `CS_CRISE` | String | Sinal clínico: crises. |
| `DT_TRISMO` | Data (AAAAMMDD) | Data do trismo. |
| `CS_ORIGEM` | String | Origem da infecção/porta de entrada. |
| `CS_HOSPITA` | String | Internação hospitalar. |
| `CLASSI_FIN` | String | Classificação final do caso. |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito. |
| `DT_ENCERRA` | Data (AAAAMMDD) | Data de encerramento da investigação. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
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
| `dt_invest` | `DT_INVEST` | data | Data de Investigação. Data completa do início da investigação (data da primeira ação desenvolvida após o conhecimento do caso) dd/mm/aaaa | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/ Ramo de Atividade Econômica. Informar a atividade exercida pela mãe do recém nascido no setor formal, informal ou autônomo ou sua última atividade exercida quando a mãe do recém | — | todos |
| `num_con_n` | `NUM_CON_N` | texto | Número de consultas de pré-natal. Informar número de consultas de pré-natal realizadas durante a última gestação | 1- Uma 2- Duas 3- De 3 a 5 4- 6 e mais 5- Nenhuma 9- Ignorado | todos |
| `cs_vacteta` | `CS_VACTETA` | texto | Antecedentes vacinais contra tétano (mãe) | 1. Vacinada (comprovado pelo cartão) 2. Não Vacinada 9. ignorado | todos |
| `dt_1_dose` | `DT_1_DOSE` | data | Data da 1ª dose. Data da 1ª dose de vacina contra tétano (DPT, DT, dT ou TT) | — | todos |
| `dt_2_dose` | `DT_2_DOSE` | data | Data da 2ª dose. Data da 2ª dose de vacina contra tétano (DPT, DT, dT ou TT) | — | todos |
| `dt_3_dose` | `DT_3_DOSE` | data | Data da 3ª dose. Data da 3ª dose de vacina contra tétano (DPT, DT, dT ou TT) | — | todos |
| `dt_reforco` | `DT_REFORCO` | data | Data do último reforço. Data do último reforço da vacina contra tétano (DPT, DT, dT ou TT) | — | todos |
| `idade_mae` | `IDADE_MAE` | inteiro | Idade da mãe. Idade da mãe por ocasião do nascimento do último recém-nascido | — | todos |
| `nu_gesta` | `NU_GESTA` | texto | Número de gestações (incluindo a atual). Informar o número de gestações ocorridas inclusive aborto caso tenha ocorrido | 1- Uma 2- Duas 3- Três 4- Quatro 5- Cinco e mais 9- Ignorado | todos |
| `escolmae_n` | `ESCOLMAE_N` | texto | Escolaridade da mãe do recém-nascido (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `cs_nascido` | `CS_NASCIDO` | texto | Local de ocorrência do parto | 1. hospital 2. domicílio 3. casa de parto 4.outro 9. ignorado | todos |
| `no_ouparto` | `NO_OUPARTO` | texto | Local de ocorrência do parto Se outro, especificar | — | todos |
| `cs_atend_n` | `CS_ATEND_N` | texto | Parto atendido por. quem realizou o parto | 1. médico 2. enfermeiro | todos |
| `no_atenout` | `NO_ATENOUT` | texto | Parto atendido por Se Outro, especificar | — | todos |
| `cs_sugou` | `CS_SUGOU` | texto | Sugou normalmente após o nascimento. se o recém nascido sugou (mamou) normalmente após o nascimento | 1. sim 2. não 9. ignorado | todos |
| `cs_mamar` | `CS_MAMAR` | texto | Sinais e sintomas Dificuldade de mamar. Se o recém-nascido apresentou dificuldade para mamar igual a um | 1. sim 2. não 9. ignorado | todos |
| `cs_trismo` | `CS_TRISMO` | texto | Sinais e sintomas Trismo. Se o recém-nascido apresentou dificuldade em abrir a boca | 1. sim 2. não 9. ignorado | todos |
| `cs_nuca` | `CS_NUCA` | texto | Sinais e sintomas Rigidez de nuca. Se o recém-nascido apresentou dificuldade em movimentar o pescoço | 1. sim 2. não 9. ignorado | todos |
| `cs_choro` | `CS_CHORO` | texto | Sinais e sintomas Choro excessivo. Se o recém-nascido apresentou choro imotivado além do normal | 1. sim 2. não 9. ignorado | todos |
| `cs_riso` | `CS_RISO` | texto | Sinais e sintomas Contratura labial. Se o recém-nascido apresentou contratura muscular labial | 1. sim 2. não 9. ignorado | todos |
| `cs_abdomen` | `CS_ABDOMEN` | texto | Sinais e sintomas Rigidez abdominal. Se o recém-nascido apresentou endurecimento da | 1. sim 2. não 9. ignorado | todos |
| `cs_inf_cot` | `CS_INF_COT` | texto | Sinais e sintomas Processo inflamatório no coto umbilical. Se a ferida umbilical apresentou anormalidade Presença de pus mal cheiro, vermelhidão ou outros sinais | 1. sim 2. não 9. ignorado | todos |
| `cs_opistot` | `CS_OPISTOT` | texto | Sinais e sintomas Opistótono. Se o recém-nascido apresentou contratura da musculatura dorsal em formato de um arco | 1. sim 2. não 9. ignorado | todos |
| `cs_membros` | `CS_MEMBROS` | texto | Sinais e sintomas Rigidez de membros. Se o recém-nascido apresentou contratura da musculatura das pernas e/ou braços | 1. sim 2. não 9. ignorado | todos |
| `cs_crise` | `CS_CRISE` | texto | Sinais e sintomas Crises de contraturas. Se o recém-nascido apresentou crises de contraturas musculares generalizadas inicialmente pelo simples toque, ou estímulos sonoros ou luminosos e, posteriormente espontaneamente | 1. sim 2. não 9. ignorado | todos |
| `cs_outros` | `CS_OUTROS` | texto | Sinais e sintomas outros. Se outros sinais e sintomas apresentados pelo recém-nascido, além dos mencionados acima | 1. sim 2. não 9. ignorado | todos |
| `nm_out_sin` | `NM_OUT_SIN` | texto | Se outros, especificar. Se o recém-nascido apresentou outros sinais e sintomas além dos mencionados acima cite- os | — | todos |
| `dt_trismo` | `DT_TRISMO` | data | Data do trismo. Data da ocorrência do início do trismo | — | todos |
| `cs_origem` | `CS_ORIGEM` | texto | Origem do caso. Origem da fonte de identificação do caso | 1. notificação 2. busca ativa 3. declaração de óbito | todos |
| `cs_hospita` | `CS_HOSPITA` | texto | Ocorreu hospitalização? | 1- sim 2- não 9 - ignorado | todos |
| `cs_cobertu` | `CS_COBERTU` | texto | Local de residência coberto pelo:. Se o local de residência da mãe está coberto pelo Programa da Atenção Básica | 1. PACS 2. PSF 3. PACS/PSF 4. Nenhum 5 – Outro 9 – Ignorado | todos |
| `no_coboutr` | `NO_COBOUTR` | texto | Local de residência coberto pelo: Se Outros especificar. Se o local de residência da mãe está coberto por Outro Programa de Atenção Básica, além dos mencionados anteriormente especificar | — | todos |
| `cs_vacinac` | `CS_VACINAC` | texto | Medidas adotadas (Atualização do Esquema Vacinal da Mãe). o | 1. sim 2. não 9. ignorado | todos |
| `cs_cadastr` | `CS_CADASTR` | texto | Medidas adotadas (Cadastro e Capacitação de parteiras atuantes). Se foi realizado cadastro e capacitação de parteiras atuantes na área | 1- sim 2- não 9- ignorado | todos |
| `cs_divulga` | `CS_DIVULGA` | texto | Medidas adotadas. Se foi realizada a | 1- sim | todos |
| `cs_buscaat` | `CS_BUSCAAT` | texto | Medidas adotadas (Busca ativa de outros casos de TNN). Se foi realizada busca ativa de outros casos de Tétano Neonatal (TNN) na comunidade, em unidades de internação, em registros de óbitos para avaliar subnotificação | 1- sim 2- não 9- ignorado | todos |
| `cs_orienta` | `CS_ORIENTA` | texto | Medidas adotadas (Orientação às parturientes quanto aos cuidados com o coto umbilical). Se a parturiente foi orientada como cuidar do coto umbilical | 1- sim 2- não 9- ignorado | todos |
| `cs_analise` | `CS_ANALISE` | texto | Medidas adotadas (Análise da Cobertura Vacinal (CV) da área e vacinação discriminada em Mulheres em Idade Fértil-(MIF) contra o tétano). Se foi realizada a análise da CV de MIF e vacinação discriminada em MIF contra o tétano | 1- sim 2- não 9- ignorado | todos |
| `cs_outras` | `CS_OUTRAS` | texto | Medidas adotadas (outras). Se foram adotadas outras medidas além das citadas | — | todos |
| `no_outras` | `NO_OUTRAS` | texto | Medidas adotadas Se Outras, especificar | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final. Conclusão do caso | 1. confirmado 2. descartado | todos |
| `ds_inf_loc` | `DS_INF_LOC` | texto | Local provável da fonte de infecção. Local onde provavelmente ocorreu a infecção | 1- Hospital 2- Domicílio 3- Casa de Parto 4- Outro Local 9- IGN | todos |
| `ds_inf_out` | `DS_INF_OUT` | texto | Local provável da fonte de infecção Se Outros especificar | — | todos |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência? | 1 – Sim 2 – Não 3 – Indeterminado | todos |
| `coufinf` | `COUFINF` | texto | UF (provável da. Sigla da unidade | — | todos |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente infectado | — | todos |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). o | — | todos |
| `counidinf` | `COUNIDINF` | texto | Unidade. Unidade de Saúde onde provalvel mente ocorreu a | — | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso | 1. cura 2. óbito por TNN 3. óbito por outras causas 9-ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito. Data por ocasião do óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Data do encerramento da investigação | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `dt_nasc` | `DT_NASC` | data | Data de nascimento. Data de nascimento do paciente | — | só em 2017 |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | 2017 a 2026 |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | só em 2026 |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | só em 2026 |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | só em 2026 |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | só em 2026 |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | só em 2026 |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | só em 2026 |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | só em 2026 |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | só em 2026 |

## No lake

- **Dataset no lake:** `datasus/sinan-tetn`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 18, inteiro: 2, texto: 66.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-tetn.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- Volumes ínfimos: cada linha tem alto valor epidemiológico, e a análise é em geral caso a caso. Filtrar por `CLASSI_FIN` para separar casos confirmados de descartados. Dados do ano corrente são preliminares. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (UF de notificação) ou `SG_UF`/`ID_MN_RESI` (residência) conforme a pergunta, pois os dois podem diferir. Arquivos do diretório PRELIM são preliminares e substituídos pelos finais; prefira sempre os arquivos finais quando o mesmo ano existir nas duas fontes, evitando somar PRELIM e FINAIS. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 10 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** nas amostras, 1 arquivo(s) sem nenhuma linha escaparam da limpeza do conversor e gravaram as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre os arquivos de zero linha antes de empilhar partições. Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0. Achado do conversor, não corrigido aqui.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-tetn").glob("**/*.parquet"))
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
datasus-fetcher list sinan-tetn

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-tetn -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-tetn
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Tétano Neonatal: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Programa Nacional de Imunizações (SVSA/MS): https://www.gov.br/saude/pt-br/vacinacao
