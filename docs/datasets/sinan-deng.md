---
dataset:
  id: sinan-deng
  fonte: datasus
  titulo: Dengue
  resumo: O sinan-deng contém os microdados das notificações e investigações epidemiológicas de casos de Dengue (CID-10 A90) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde.
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2000'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de dengue
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 197
  unidades_de_medida:
    ano_dengue_anterior: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras:
  - desde: 2007-01
    mudanca: SINAN Net substitui o SINAN-Windows (2000 a 2006 vêm do SINAN-Windows)
  - desde: 2014-01
    mudanca: Sinan Online passa a alimentar a mesma base, além do SINAN Net
  - desde: 2016-01
    mudanca: ficha de investigação unificada para dengue e chikungunya; `ID_AGRAVO` distingue os dois agravos
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Dengue (`sinan-deng`)

## Resumo

O `sinan-deng` contém os microdados das notificações e investigações epidemiológicas de casos de Dengue (CID-10 A90) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de dengue, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. É uma das maiores bases de dados de morbidade do sistema de saúde brasileiro e centraliza o monitoramento das arboviroses urbanas transmitidas pelo *Aedes aegypti*.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2000 a 2026 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 27 arquivos (~1,02 GB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim (diretório `PRELIM`)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `DENG` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `DENG` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `DENGBR25.dbc` — `DENG` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). Em anos recentes apenas o arquivo nacional `BR` é publicado; o equivalente preliminar do ano corrente aparece em `PRELIM` (ex.: `DENGBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-deng/<ano>/sinan-deng_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-deng/2025/sinan-deng_2025-br@20260721.dbc`; arquivos preliminares recebem o sufixo do dataset `-preliminar` no nome.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` (pacote de documentação/tabulações do SINAN) e as instruções de acesso e conversão (`POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`); em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (dicionários/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

A dengue é a arbovirose de maior impacto no Brasil e o SINAN que a monitora é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), por meio da respectiva área da vigilância de arboviroses e do GT-SINAN. A doença integra a Lista Nacional de Doenças e Agravos de Notificação Compulsória (hoje consolidada na Portaria GM/MS nº 204/2016, atualizada por normas posteriores, como a Portaria GM/MS nº 10.175/2026). A base alimenta o diagnóstico dinâmico da situação epidemiológica municipal, estadual e nacional, orienta a mobilização de planos de contingência durante epidemias sazonais e dimensiona a carga de doença anual — o Brasil é um dos países com maior número de casos de dengue do mundo.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Dengue** do SINAN. Cada notificação individual nasce no momento da suspeição (febre de 2 a 7 dias acompanhada de, pelo menos, mais dois sintomas definidores (náuseas/vômitos, exantema, mialgias, cefaléia, dor retroorbital, petéquias ou leucopenia)) e é completada ao longo da investigação com dados clínicos, laboratoriais, de internação e de conclusão (classificação final, critério de confirmação, evolução e desfecho). A unidade de análise é o caso suspeito/confirmado notificado, não o óbito nem a internação (que ficam no SIM e no SIH/SIA).

A série histórica registra três fases do sistema de informação, conforme notas técnicas oficiais: de **2000 a 2006** os dados provêm do SINAN-Windows; de **2007 a 2013**, do SINAN Net; e **de 2014 em diante**, do SINAN Net e do **Sinan Online** (notificação em tempo real, mesma base disseminada). Houve também mudanças relevantes do instrumento de coleta: a ficha revisada de dengue incorporou a nova classificação da OMS (separando "Dengue", "Dengue com sinais de alarme" e "Dengue grave" no lugar de "Febre Hemorrágica do Dengue"/"Síndrome do Choque do Dengue") e, a partir de 2016, a ficha de investigação tornou-se unificada para Dengue e Febre de Chikungunya (`Ficha_DENGCHIK`, SVS 14/03/2016), com o campo `ID_AGRAVO` distinguindo os dois agravos na mesma estrutura.

Aplicações analíticas típicas: incidência anual de casos confirmados (por 100 mil habitantes, contra a estimativa populacional TCU), distribuição por faixa etária, sexo, raça/cor e gestação, incidência específica de dengue com sinais de alarme e dengue grave, taxa de letalidade (óbitos por casos confirmados), curvas epidémicas por semana de início dos sintomas (`DT_SIN_PRI`/`SEM_PRI`), desempenho da vigilância (proporção de usados com critério laboratorial, oportunidade de encerramento) e mapeamento de municípios prioritários para controle vetorial.

### Cobertura observada

- Índice do FTP (2026-10): 27 arquivos, de 2000 a 2026, 1 UF(s) com arquivos, última atualização em 2026-11-10.
- Conversão local de amostras (4 arquivo(s) Parquet, de 2000 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Eras

- **2007-01**: SINAN Net substitui o SINAN-Windows (2000 a 2006 vêm do SINAN-Windows)
- **2014-01**: Sinan Online passa a alimentar a mesma base, além do SINAN Net
- **2016-01**: ficha de investigação unificada para dengue e chikungunya; `ID_AGRAVO` distingue os dois agravos

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (1 - Negativa, 2 - Individual, 3 - Surto e outros) |
| `ID_AGRAVO` | String | Código do agravo conforme CID-10 (A90 - Dengue; distinguindo Chikungunya na ficha unificada) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data de preenchimento da ficha de notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação, derivada de `DT_NOTIF` |
| `NU_ANO` | Inteiro | Ano da notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | Código CNES da unidade de saúde (ou fonte) notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data dos primeiros sintomas da doença (usada nas curvas epidémicas) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `NU_NOTIFIC` | String (7) | Número da notificação (identificador do registro no terminal digitador) |
| `CS_SEXO` | String (1) | Sexo do paciente (M/F/I - Ignorado) |
| `NU_IDADE_N` | Inteiro composto | Idade (o primeiro dígito indica a unidade: dia/mês/ano; ex.: `4` + idade em anos) |
| `CS_GESTANTE` | Inteiro | Estado gestacional (1 a 4 conforme grupo gestacional; 9 - Ignorado) |
| `ID_MN_RESI` | String (6/7) | Código IBGE do município de residência (vs. município de notificação) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `ANT_VAC` | Inteiro | Antecedente de vacinação contra dengue (ficha unificada recente) |
| `CLASSI_FIN` | Inteiro | Classificação final: 5 - Descartado, 10 - Dengue, 11 - Dengue com sinais de alarme, 12 - Dengue grave, 13 - Chikungunya (ficha unificada) |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte (1 - Laboratório, 2 - Clínico Epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito por dengue, 3 - Óbito por outras causas, 4 - Óbito em investigação, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação. co_municipio_not ificacao | — | todos |
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora. co_unidade_notifi cacao | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escolar` | `CS_ESCOLAR` | texto | Escolaridade do paciente (formato do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2000 a 2004 |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno). ds_semana_notifi cacao | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico. dt_diagnostico_si ntoma | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno). ds_semana_sinto ma | — | todos |
| `nu_idade` | `NU_IDADE` | texto | Idade do paciente (formato do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2000 a 2004 |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência. co_municipio_res idencia | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil). co_pais_residenc ia | — | todos |
| `id_dg_not` | `ID_DG_NOT` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Dengue (`ID_DG_NOT`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `id_ev_not` | `ID_EV_NOT` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Dengue (`ID_EV_NOT`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `ant_dt_inv` | `ANT_DT_INV` | data | Data da investigação | — | 2000 a 2004 |
| `ocupacao` | `OCUPACAO` | texto | Ocupação do paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2000 a 2004 |
| `dengue` | `DENGUE` | texto | Indica caso de dengue (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2000 a 2004 |
| `ano_dengue_anterior` | `ANO` | inteiro | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `vacinado` | `VACINADO` | texto | Vacinado contra Febre Amarela. st_vacinado_feb re_amarela | 1. Sim 2. Não 9. Ignorado | 2000 a 2004 |
| `dt_dose` | `DT_DOSE` | data | Registro de vacinação (`DT_DOSE`) | — | 2000 a 2004 |
| `febre` | `FEBRE` | texto | Sinais clínicos (Febre). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `dt_febre` | `DT_FEBRE` | data | Data do inicio da febre. Data do início da febre | — | 2000 a 2004 |
| `duracao` | `DURACAO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `laco` | `LACO` | texto | Sinais clínicos (Prova do laço). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `cefaleia` | `CEFALEIA` | texto | Sinais clínicos (Cefaleia). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `exantema` | `EXANTEMA` | texto | Sinais clínicos (Exantema). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `dor` | `DOR` | texto | Sinais e sintomas Dor abdominal. st_sinais_abdom inal | 1. Sim 2. Não 9. Ignorado | 2000 a 2004 |
| `prostacao` | `PROSTACAO` | texto | Sinais e Sintomas Prostração. Informar se o paciente teve sinais/sintomas de Prostração | 1- Sim 2- Não 9- Ignorado | 2000 a 2004 |
| `mialgia` | `MIALGIA` | texto | Sinais clínicos (Mialgia). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `nauseas` | `NAUSEAS` | texto | Sinais e sintomas Náuseas. st_sinais_nause a | 1. Sim 2. Não 9. Ignorado | 2000 a 2004 |
| `artralgia` | `ARTRALGIA` | texto | Sinais clínicos (Artralgia intensa). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | todos |
| `diarreia` | `DIARREIA` | texto | Sinais e sintomas. O paciente teve diarreia | 1. Sim | 2000 a 2004 |
| `outros` | `OUTROS` | texto | Outros. Anotar o CÓDIGO 3 se outro exame não foi realizado e 1 ou 2 , respectivamente, conforme o resultado tenha sido positivo ou | 1. Positivo 2. Negativo 3. Não realizado | 2000 a 2004 |
| `sin_out` | `SIN_OUT` | texto | Manifestação clínica registrada na ficha de Dengue (`SIN_OUT`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `epistaxe` | `EPISTAXE` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `petequias` | `PETEQUIAS` | texto | Sinais e Sintomas Petéquias. Informar se o paciente teve sinais/sintomas de Petéquias | 1- Sim 2- Não 9- Ignorado | todos |
| `gengivo` | `GENGIVO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `metro` | `METRO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `hematura` | `HEMATURA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `sangram` | `SANGRAM` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `outros_m` | `OUTROS_M` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `outros_m_d` | `OUTROS_M_D` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `ascite` | `ASCITE` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `pleural` | `PLEURAL` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `pericardi` | `PERICARDI` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `abdominal` | `ABDOMINAL` | texto | Sinais e Sintomas Dor Abdominal. Informar se o paciente teve sinais/sintomas de Dor Abdominal | 1- Sim 2- Não 9- Ignorado | 2000 a 2004 |
| `hepato` | `HEPATO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `miocardi` | `MIOCARDI` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `hipotensao` | `HIPOTENSAO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `choque` | `CHOQUE` | texto | Sinais e Sintomas Choque/Hipotensão. Informar se o paciente teve sinais/sintomas de Choque/Hipotensão | 1- Sim 2- Não 9- Ignorado | 2000 a 2004 |
| `manifesta` | `MANIFESTA` | texto | Manifestação clínica registrada na ficha de Dengue (`MANIFESTA`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `insuficien` | `INSUFICIEN` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `outro_s` | `OUTRO_S` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `outro_s_d` | `OUTRO_S_D` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `dt_choque` | `DT_CHOQUE` | data | Data registrada na ficha de Dengue (`DT_CHOQUE`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `hospitaliz` | `HOSPITALIZ` | texto | Ocorreu Hospitalização?. st_ocorreu_hospitaliz acao | 1-Sim 2-Não 9-Ignorado | todos |
| `dt_interna` | `DT_INTERNA` | data | Data Da Internação. Informar a data de internação do paciente | — | todos |
| `uf_hospital` | `UF` | texto | UF do hospital de internação (coluna `UF` da fonte, renomeada pelo conversor porque `uf` é coluna do lake) | — | todos |
| `municipio` | `MUNICIPIO` | texto | Municipio Do Hospital. VARCHAR (6) | — | todos |
| `dt_col_hem` | `DT_COL_HEM` | data | Dado de exame laboratorial registrado na ficha de Dengue (`DT_COL_HEM`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `hema_maior` | `HEMA_MAIOR` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `dt_col_plq` | `DT_COL_PLQ` | data | Dado de exame laboratorial registrado na ficha de Dengue (`DT_COL_PLQ`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `palq_maior` | `PALQ_MAIOR` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `dt_col_he2` | `DT_COL_HE2` | data | Dado de exame laboratorial registrado na ficha de Dengue (`DT_COL_HE2`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `hema_menor` | `HEMA_MENOR` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `dt_col_pl2` | `DT_COL_PL2` | data | Dado de exame laboratorial registrado na ficha de Dengue (`DT_COL_PL2`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `plaq_menor` | `PLAQ_MENOR` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `dt_soro1` | `DT_SORO1` | data | Dado de exame laboratorial registrado na ficha de Dengue (`DT_SORO1`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `dt_soro2` | `DT_SORO2` | data | Dado de exame laboratorial registrado na ficha de Dengue (`DT_SORO2`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `dt_soror1` | `DT_SOROR1` | data | Dado de exame laboratorial registrado na ficha de Dengue (`DT_SOROR1`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `dt_soror2` | `DT_SOROR2` | data | Dado de exame laboratorial registrado na ficha de Dengue (`DT_SOROR2`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `s1_igm` | `S1_IGM` | texto | Exame sorológico: Resultado 1ª amostra. tp_sorologico_re sultado_1 | 1-Reagente 2-Não reagente 3-Inconclusivo 4-Não realizado | 2000 a 2004 |
| `s1_igg` | `S1_IGG` | texto | Resultado dos Exames Sorológicos IgG – S1. Resultado da 3ª sorologia - IgG - S1 | 1- Reagente 2- Não reagente 3- Inconclusivo 4- Não realizado | 2000 a 2004 |
| `s2_igm` | `S2_IGM` | texto | Exame sorológico: Resultado 2ª amostra. tp_sorologico_re sultado_2 | 1 -Reagente 2- Não reagente 3- Inconclusivo 4 -Não realizado | 2000 a 2004 |
| `s2_igg` | `S2_IGG` | texto | Resultado dos Exames Sorológicos IgG – S2. Resultado da 3ª sorologia - IgG - S2 | 1- Reagente 2- Não reagente 3- Inconclusivo 4- Não realizado | 2000 a 2004 |
| `s1_tit1` | `S1_TIT1` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `s2_tit1` | `S2_TIT1` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `material` | `MATERIAL` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `soro1` | `SORO1` | texto | Dado de exame laboratorial registrado na ficha de Dengue (`SORO1`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `soro2` | `SORO2` | texto | Dado de exame laboratorial registrado na ficha de Dengue (`SORO2`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `tecidos` | `TECIDOS` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `resul_vira` | `RESUL_VIRA` | texto | Dado de exame laboratorial registrado na ficha de Dengue (`RESUL_VIRA`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `histopa` | `HISTOPA` | texto | Histopatologia - Resultado | 1- Reagente 2- Não Reagente 3- Inconclusivo 4- Não Realizado | 2000 a 2004 |
| `imunoh` | `IMUNOH` | texto | Imunohistoquímica - Resultado. tp_imunohitoqui mica | 1- Reagente 2- Não Reagente 3- Inconclusivo 4- Não Realizado | 2000 a 2004 |
| `amos_pcr` | `AMOS_PCR` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `resul_pcr` | `RESUL_PCR` | texto | Dado de exame laboratorial registrado na ficha de Dengue (`RESUL_PCR`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `amos_out` | `AMOS_OUT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `tecnica` | `TECNICA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2000 a 2004 |
| `resul_out` | `RESUL_OUT` | texto | Dado de exame laboratorial registrado na ficha de Dengue (`RESUL_OUT`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `con_classi` | `CON_CLASSI` | texto | Classificação da forma clínica | 1. Forma bubônica 2. Forma pneumônica 3. Forma septicêmica 4 outra | 2000 a 2004 |
| `con_criter` | `CON_CRITER` | texto | Dado de conclusão do caso na ficha de Dengue (`CON_CRITER`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2000 a 2004 |
| `con_fhd` | `CON_FHD` | texto | Dado de conclusão do caso na ficha de Dengue (`CON_FHD`): classificação, critério de confirmação, local provável de infecção ou evolução | — | todos |
| `con_inf_mu` | `CON_INF_MU` | texto | Dado de conclusão do caso na ficha de Dengue (`CON_INF_MU`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2000 a 2004 |
| `con_inf_uf` | `CON_INF_UF` | texto | Dado de conclusão do caso na ficha de Dengue (`CON_INF_UF`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2000 a 2004 |
| `con_inf_pa` | `CON_INF_PA` | texto | Dado de conclusão do caso na ficha de Dengue (`CON_INF_PA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2000 a 2004 |
| `con_doenca` | `CON_DOENCA` | texto | Dado de conclusão do caso na ficha de Dengue (`CON_DOENCA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2000 a 2004 |
| `con_evoluc` | `CON_EVOLUC` | texto | Dado de conclusão do caso na ficha de Dengue (`CON_EVOLUC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2000 a 2004 |
| `con_dt_obi` | `CON_DT_OBI` | data | Dado de conclusão do caso na ficha de Dengue (`CON_DT_OBI`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2000 a 2004 |
| `con_dt_enc` | `CON_DT_ENC` | data | Dado de conclusão do caso na ficha de Dengue (`CON_DT_ENC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2000 a 2004 |
| `in_vincula` | `IN_VINCULA` | texto | Vinculação. 0 ou branco – Não Vinculado 1 – Vinculado | — | 2000 a 2004 |
| `nduplic` | `NDUPLIC` | texto | Indicador de duplicidade do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2000 a 2004 |
| `in_aids` | `IN_AIDS` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Dengue (`IN_AIDS`); o dicionário consultado não define o campo isoladamente | — | 2000 a 2004 |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | 2017 a 2026 |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo/doença. Especifica a suspeição do agravo | 1-Dengue 2-Chikungunya | 2017 a 2026 |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2017 a 2026 |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | 2017 a 2026 |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | 2017 a 2026 |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | 2017 a 2026 |
| `dt_invest` | `DT_INVEST` | data | Data da Investigação. Informar a data da investigação | — | 2017 a 2026 |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/ramo de atividade econômica. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo de atividade econômica do paciente refere-se as atividades econômicas desenvolvidas nos processos de produção do setor primário (agricultura e extrativismo); secundário (indústria) ou terciário (serviços e comércio) | — | 2017 a 2026 |
| `vomito` | `VOMITO` | texto | Sinais clínicos (Vômito). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | 2017 a 2026 |
| `nausea` | `NAUSEA` | texto | Sinais clínicos (Náusea). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | 2017 a 2026 |
| `dor_costas` | `DOR_COSTAS` | texto | Sinais clínicos (Dor nas costas). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | 2017 a 2026 |
| `conjuntvit` | `CONJUNTVIT` | texto | Sinais clínicos (Conjuntivite). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | 2017 a 2026 |
| `artrite` | `ARTRITE` | texto | Sinais clínicos (Artrite). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | 2017 a 2026 |
| `petequia_n` | `PETEQUIA_N` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2017 a 2026 |
| `leucopenia` | `LEUCOPENIA` | texto | Sinais clínicos (Leucopenia). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | 2017 a 2026 |
| `dor_retro` | `DOR_RETRO` | texto | Sinais clínicos (Dor retroorbital). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | 2017 a 2026 |
| `diabetes` | `DIABETES` | texto | Doenças pré- existentes (Diabetes). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | 2017 a 2026 |
| `hematolog` | `HEMATOLOG` | texto | Doenças pré- existentes (Doenças hematológicas). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | 2017 a 2026 |
| `hepatopat` | `HEPATOPAT` | texto | Doenças pré- existentes (Hepatopatias). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | 2017 a 2026 |
| `renal` | `RENAL` | texto | Doenças pré- existentes (Doença renal crônica). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | 2017 a 2026 |
| `hipertensa` | `HIPERTENSA` | texto | Doenças pré- existentes (Hipertensão arterial). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | 2017 a 2026 |
| `acido_pept` | `ACIDO_PEPT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2017 a 2026 |
| `auto_imune` | `AUTO_IMUNE` | texto | Doenças pré- existentes (Doenças auto-imunes). Informar qual sinal clínico ou achados laboratoriais inespecíficos | 1 – Sim 2 – Não | 2017 a 2026 |
| `dt_chik_s1` | `DT_CHIK_S1` | data | Exame sorológico (IgM) Chikungunya Soro 1 Data da Coleta. Data da Coleta Exame Sorológico (IgM) Chikungunya soro 1 | — | 2017 a 2026 |
| `dt_chik_s2` | `DT_CHIK_S2` | data | Exame sorológico (IgM) Chikungunya Soro 2 Data da Coleta. Data da Coleta Exame Sorológico (IgM) Chikungunya soro 2 | — | 2017 a 2026 |
| `dt_prnt` | `DT_PRNT` | data | Exame PRNT Data da Coleta. Data da Coleta Exame PRNT | — | 2017 a 2026 |
| `res_chiks1` | `RES_CHIKS1` | texto | Exame sorológico (IgM) Chikungunya Soro 1 Resultado. Resultado do Exame Sorológico (IgM) soro 1 para Chikunugnya | 1-Reagente 2-Não Reagente 3-Inconclusivo 4-Não realizado | 2017 a 2026 |
| `res_chiks2` | `RES_CHIKS2` | texto | Exame sorológico (IgM) Chikungunya Soro 2 Resultado. Resultado do Exame Sorológico (IgM) soro 2 para Chikunugnya | 1-Reagente 2-Não Reagente 3-Inconclusivo 4-Não realizado | 2017 a 2026 |
| `resul_prnt` | `RESUL_PRNT` | texto | Exame PRNT Resultado. Resultado do Exame Sorológico (IgM) PRNT | 1-Reagente 2-Não Reagente 3-Inconclusivo 4-Não realizado | 2017 a 2026 |
| `dt_soro` | `DT_SORO` | data | Exame sorológico (IgM) Dengue Data da Coleta. Data da Coleta Exame Sorológico (IgM) Dengue | — | 2017 a 2026 |
| `resul_soro` | `RESUL_SORO` | texto | Exame sorológico (IgM) Dengue Resultado. Resultado do Exame Sorológico (IgM) Dengue | 1-Reagente 2-Não Reagente 3-Inconclusivo 4-Não realizado | 2017 a 2026 |
| `dt_ns1` | `DT_NS1` | data | Exame NS1 Data da Coleta. dt_coleta_NS1 | — | 2017 a 2026 |
| `resul_ns1` | `RESUL_NS1` | texto | Exame NS1 Resultado. Tp_result_NS1 | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | 2017 a 2026 |
| `dt_viral` | `DT_VIRAL` | data | Isolamento Viral Data da Coleta. Data da Coleta Isolamento Viral | — | 2017 a 2026 |
| `resul_vi_n` | `RESUL_VI_N` | texto | Isolamento Viral Resultado. Resultado Exame de Isolamento Viral | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | 2017 a 2026 |
| `dt_pcr` | `DT_PCR` | data | RT-PCR Data da Coleta. Data de Coleta do Exame de RT-PCR | — | 2017 a 2026 |
| `resul_pcr_` | `RESUL_PCR_` | texto | RT-PCR Resultado. Resultado do Exame de RT-PCR | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | 2017 a 2026 |
| `sorotipo` | `SOROTIPO` | texto | Sorotipo | 1-DEN 1 2-DEN 2 3 DEN 3 4-DEN 4 | 2017 a 2026 |
| `histopa_n` | `HISTOPA_N` | texto | Histopatologia Resultado. tp_result_histopatolog ia | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | 2017 a 2026 |
| `imunoh_n` | `IMUNOH_N` | texto | Imunohistoquímica Resultado. tp_result_imunohistoq uimica | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | 2017 a 2026 |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência?. tp_autoctone_residen cia | 1 – Sim 2 – Não 3 – Indeterminado | 2017 a 2026 |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o paciente foi provavelmente infectado | — | 2017 a 2026 |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente infectado | — | 2017 a 2026 |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). co_municipio_infecca o | — | 2017 a 2026 |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação. VARCHAR (1) | 5-Descartado 10-Dengue 11-Dengue com sinais de alarme 12-Dengue grave 13-Chikungunya | 2017 a 2026 |
| `criterio` | `CRITERIO` | texto | Critério De Confirmação/Descarte. tp_criterio_confirmaca o | 1-Laboratório 2-Clínico Epidemiológico 3-Em investigação | 2017 a 2026 |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho. st_doenca_trabal ho | 1 – Sim 2 – Não 9 – Ignorado | 2017 a 2026 |
| `clinc_chik` | `CLINC_CHIK` | texto | Manifestação clínica registrada na ficha de Dengue (`CLINC_CHIK`); o dicionário consultado não define o campo isoladamente | — | 2017 a 2026 |
| `evolucao` | `EVOLUCAO` | texto | Evolução Do Caso. VARCHAR (1) | 1- cura 2- óbito pelo agravo 3- óbito por outras causas 4- óbito em investigação 9- ignorado | 2017 a 2026 |
| `dt_obito` | `DT_OBITO` | data | Data do Óbito. Informar a data do óbito | — | 2017 a 2026 |
| `dt_encerra` | `DT_ENCERRA` | data | Data Do Encerramento. Informar a data do encerramento do caso | — | 2017 a 2026 |
| `alrm_hipot` | `ALRM_HIPOT` | texto | Dengue com sinais de alarme (Hipotensão). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `alrm_plaq` | `ALRM_PLAQ` | texto | Dengue com sinais de alarme (Queda abrupta de plaquetas). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `alrm_vom` | `ALRM_VOM` | texto | Dengue com sinais de alarme (Vômitos persistentes). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `alrm_sang` | `ALRM_SANG` | texto | Dengue com sinais de alarme (Sangramento de mucosa/outras hemorragias). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `alrm_hemat` | `ALRM_HEMAT` | texto | Dengue com sinais de alarme (Aumento hematócrito). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `alrm_abdom` | `ALRM_ABDOM` | texto | Dengue com sinais de alarme. Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `alrm_letar` | `ALRM_LETAR` | texto | Dengue com sinais de alarme (Letargia ou irritabilidade). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `alrm_hepat` | `ALRM_HEPAT` | texto | Dengue com sinais de alarme (Hepatomegalia). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `alrm_liq` | `ALRM_LIQ` | texto | Dengue com sinais de alarme (Acúmulo de líquidos). Informar qual sinal de alarme foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `dt_alrm` | `DT_ALRM` | data | Dengue com sinais de alarme Data de início dos sintomas. Informar data de início dos sinais de alarme. Considerar a data do primeiro sinal de alarme manifestado | — | 2017 a 2026 |
| `grav_pulso` | `GRAV_PULSO` | texto | Dengue grave (Pulso débil ou indectável). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_conv` | `GRAV_CONV` | texto | Dengue grave (PA convergente). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_ench` | `GRAV_ENCH` | texto | Dengue grave (Tempo de enchimento capilar). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_insuf` | `GRAV_INSUF` | texto | Dengue grave (Acúmulo de líquidos com insuficiência respiratória). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_taqui` | `GRAV_TAQUI` | texto | Dengue grave (Taquicardia). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_extre` | `GRAV_EXTRE` | texto | Dengue grave (Extremidade frias). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_hipot` | `GRAV_HIPOT` | texto | Dengue grave (Hipotensão arterial em fase tardia). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_hemat` | `GRAV_HEMAT` | texto | Dengue grave (Hematêmese). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_melen` | `GRAV_MELEN` | texto | Dengue grave (Melena). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_metro` | `GRAV_METRO` | texto | Dengue grave (Metrorragia volumosa). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_sang` | `GRAV_SANG` | texto | Dengue grave (Sangramento do SNC). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_ast` | `GRAV_AST` | texto | Dengue grave (AST/ALT >1 .000). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_mioc` | `GRAV_MIOC` | texto | Dengue grave (Miocardite). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_consc` | `GRAV_CONSC` | texto | Dengue grave (Alteração da consciência). Informar qual sinal de gravidade foi encontrado | 1 – Sim 2 – Não | 2017 a 2026 |
| `grav_orgao` | `GRAV_ORGAO` | texto | Dengue grave (Outros órgãos). Informar qual sinal de gravidade foi encontrado | — | 2017 a 2026 |
| `dt_grav` | `DT_GRAV` | data | Dengue grave Data de início dos sintomas. Informar data de início dos sinais de alarme. Considerar a data do primeiro sinal de alarme manifestado | — | 2017 a 2026 |
| `mani_hemor` | `MANI_HEMOR` | texto | Manifestação clínica registrada na ficha de Dengue (`MANI_HEMOR`); o dicionário consultado não define o campo isoladamente | — | 2017 a 2026 |
| `laco_n` | `LACO_N` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2017 a 2026 |
| `plasmatico` | `PLASMATICO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2017 a 2026 |
| `evidencia` | `EVIDENCIA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2017 a 2026 |
| `complica` | `COMPLICA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2017 a 2026 |
| `tp_sistema` | `TP_SISTEMA` | texto | Sistema de origem do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2017 a 2026 |
| `nduplic_n` | `NDUPLIC_N` | texto | Não Listar/ Não Contar. 0 ou branco – Não identificado 1 – Não é duplicidade (não listar) 2 – Duplicidade (não contar) | — | 2017 a 2026 |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | 2017 a 2026 |
| `cs_flxret` | `CS_FLXRET` | texto | Fluxo de retorno. Identifica se o registro está habilitado ou foi enviado pelo fluxo de retorno para o município de residência | 0 - Não 1 - habilitado para envio. 2 - enviado | 2017 a 2026 |
| `flxrecebi` | `FLXRECEBI` | texto | Recebida por fluxo de retorno (campo interno). Colocar a estrutura do nº atribuído pelo sistema | — | 2017 a 2026 |
| `migrado_w` | `MIGRADO_W` | texto | Identifica migração (campo interno). Identifica se o registro é oriundo da rotina de migração da base Windows | 1- migrado do Sinan Windows | 2017 a 2026 |

## No lake

- **Dataset no lake:** `datasus/sinan-deng`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 30, inteiro: 2, texto: 165.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`; no dengue, `ANO` vira `ano_dengue_anterior`.
- **Esquema de referência:** `sinan-deng.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- os arquivos do FTP são consolidações nacionais anuais `BR` (`:n_files` pequeno, ~27), a última série de cada ciclo ainda pode estar em `PRELIM` e sujeita a revisão; a ficha unificada Dengue/Chikungunya (desde 2016) exige filtrar por `ID_AGRAVO`/`CLASSI_FIN` para recortar apenas dengue; `CLASSI_FIN` teve categorias históricas distintas (1 - Dengue clássico, 2 - Dengue com complicações, 3 - FHD, 4 - SCD) antes de 2010, o que exige mapeamentos diferentes por período; a idade em `NU_IDADE_N` requer decomposição do primeiro dígito (unidade) antes de comparações; e duplicidades de notificação devem ser verificadas por `NU_NOTIFIC` + município + paciente antes de cálculo de incidência. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 162 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-deng/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-deng
quantilica datasus list sinan-deng

# 2. Baixar microdados de sinan-deng com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-deng -o ./data --start 2010 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-deng -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-deng -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/sinan-deng/2025/sinan-deng_2025-br@20260721.dbc", clean=True)

# Visão geral: casos confirmados de dengue (classificação final tanto em versões antigas quanto novas)
confirmados = qdf.filter(pl.col("classi_fin").is_in([1, 2, 3, 4, 10, 11, 12]))
print(confirmados.group_by("nu_ano").len().sort("nu_ano"))

# Curva epidêmica por semana epidemiológica de início dos sintomas
epi = confirmados.group_by(["sem_pri", "nu_ano"]).len().sort(["nu_ano", "sem_pri"])
print(epi)
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Dengue/Chikungunya (fichas, dicionários e preenchimento)**: https://portalsinan.saude.gov.br/sinan-dengue-chikungunya e https://portalsinan.saude.gov.br/images/documentos/Agravos/Dengue/DIC_DADOS_ONLINE.pdf
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS) e Portaria GM/MS nº 10.175/2026 (atualização da Lista Nacional)
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulos de dengue e de arboviroses
