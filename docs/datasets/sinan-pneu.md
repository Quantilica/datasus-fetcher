---
dataset:
  id: sinan-pneu
  fonte: datasus
  titulo: Pneumoconioses relacionadas ao trabalho
  resumo: Notificações de pneumoconioses — doenças respiratórias causadas pela inalação de poeiras minerais ou orgânicas no ambiente de trabalho — registradas no SINAN.
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2006'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de pneumoconioses relacionadas ao trabalho
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 83
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Pneumoconioses relacionadas ao trabalho (`sinan-pneu`)

## Resumo

Notificações de pneumoconioses — doenças respiratórias causadas pela inalação de poeiras minerais ou orgânicas no ambiente de trabalho — registradas no SINAN. Cada linha representa uma ficha de investigação de um caso de pneumoconiose ocupacional.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (dBASE comprimido)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2006 a 2026 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 21 arquivos (~377 KB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim (diretório PRELIM, 2023–2026; Finais até 2022)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `PNEU` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `PNEU` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `PNEUBR24.dbc`, em que `PNEU` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024, preliminar).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-pneu/<partição>/sinan-pneu_br_2006_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`DRT Pneumoconioses Relacionadas ao Trabalho`) é distribuído no Portal SINAN; não há PDF por agravo no FTP.

## Conteúdo

As pneumoconioses integram a lista de Doenças e Agravos Relacionados ao Trabalho (DART) de notificação compulsória no SUS, sob a coordenação da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) e operacionalização da RENAST/CEREST. A notificação compulsória decorre da Portaria MS nº 777/2004 e da Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V; Portaria GM/MS nº 217/2023).

O evento gerador é todo quadro de fibrose pulmonar ou doença respiratória causada pela inalação de poeiras minerais ou orgânicas, com destaque para asbestose (Amianto), silicose, pneumoconiose do trabalhador do carvão e pneumoconioses por poeiras mistas (CID-10 J60–J65). A exposição ocorre em mineração, construção civil, metalurgia, siderurgia, cerâmica, cimento e agricultura. A unidade de análise é o caso notificado (um registro por ficha), com ocupação (CBO), situação no mercado de trabalho e dados da empresa contratante (CNAE, CNPJ/CPF).

O instrumento é a *Ficha de Investigação — Pneumoconioses Relacionadas ao Trabalho*, que registra o tipo de pneumoconiose, o agente de exposição, o tempo de exposição, os exames (radiografia de tórax segundo a classificação OIT/BI-RADS de pneumoconiose, espirometria) e a conduta. A série no FTP inicia em 2006; os dados de 2023 em diante estão em PRELIM e sujeitos a revisão.

Principais usos: vigilância de pneumoconioses por ramo (CNAE) e ocupação (CBO), monitoramento de programas de proteção respiratória, apoio à caracterização de nexo para fins previdenciários e embasamento de ações de VISAT e de restrição/interdição de exposições.

### Cobertura observada

- Índice do FTP (2026-10): 21 arquivos, de 2006 a 2026, 1 UF(s) com arquivos, última atualização em 2026-09-02.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2006 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo `PNEUBR26.dbc` (leiaute do SINAN Net; fichas e leiautes podem variar entre anos, por isso a lista reflete esse arquivo). Os arquivos públicos não trazem identificadores individuais como número da notificação (`NU_NOTIFIC`) nem data de nascimento completa. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (registro da ficha de notificação individual). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado. |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | String | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE). |
| `ID_UNIDADE` | String | Código CNES da unidade de saúde notificadora (7 dígitos). |
| `DT_DIAG` | Data (AAAAMMDD) | Data do diagnóstico. |
| `SEM_DIAG` | String | Semana epidemiológica do diagnóstico (AAAASS). |
| `ANO_NASC` | String | Ano de nascimento (o arquivo público não traz a data de nascimento completa). |
| `NU_IDADE_N` | Inteiro | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade. |
| `SG_UF` | String | UF de residência (código IBGE de 2 dígitos). |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `ID_OCUPA_N` | String | Ocupação do trabalhador (CBO 2002, 6 dígitos). |
| `SIT_TRAB` | String | Situação no mercado de trabalho. |
| `CNAE` | String | Atividade econômica da empresa contratante (CNAE). |
| `FLUXO_AERE` | String | Doença preexistente: alteração de fluxo aéreo. |
| `TUBE` | String | Doença preexistente: tuberculose. |
| `CANCER` | String | Doença preexistente: câncer. |
| `ARTRITE` | String | Doença preexistente: artrite. |
| `TIREOIDITE` | String | Doença preexistente: tireoidite. |
| `OUTRO_DOE` | String | Outra doença preexistente (descrição em `OUT_DOE_DE`). |
| `POEIRAS` | String | Exposição a poeiras. |
| `SILICA` | String | Exposição a sílica. |
| `ASBESTO` | String | Exposição a asbesto/amianto. |
| `CARVAO` | String | Exposição a carvão. |
| `POE_MISTA` | String | Exposição a poeiras mistas. |
| `METAL` | String | Exposição a metais. |
| `POE_ABRASI` | String | Exposição a poeiras abrasivas. |
| `BERILIO` | String | Exposição a berílio. |
| `POE_ORGANI` | String | Exposição a poeiras orgânicas. |
| `RAIOX` | String | Exame de raio-X de tórax realizado. |
| `BIOPSIA` | String | Biópsia realizada. |
| `TOMOGRAFIA` | String | Tomografia realizada. |
| `OUT_EXAME` | String | Outro exame realizado. |
| `DIAG_ESP` | String | Diagnóstico específico (CID-10). |
| `TRAB_DOE` | String | Outros trabalhadores com a mesma doença no local de trabalho. |
| `STAVALIA` | String | Status da avaliação (STAVALIA). |
| `STRESULTA` | String | Status do resultado (STRESULTA). |
| `AFAST_RISC` | String | Conduta: afastamento do local de risco. |
| `INDIVIDUAL` | String | Conduta: ação individual. |
| `MUDA_TRAB` | String | Conduta: mudança de função/posto de trabalho. |
| `NENHUM` | String | Conduta: nenhuma ação. |
| `COLETIVA` | String | Conduta: ação coletiva. |
| `AFAST_TRAB` | String | Conduta: afastamento do trabalho. |
| `CONDUTA` | String | Conduta adotada (marcação geral da ficha). |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito, quando aplicável. |
| `CAT` | String | Foi emitida a Comunicação de Acidente do Trabalho (CAT)? |
| `VINC_ESP` | String | Descrição textual do vínculo/exposição específica. |

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
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência. co_municipio_res idencia | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil). co_pais_residenc ia | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Ocupação do indivíduo que sofreu o agravo | — | todos |
| `sit_trab` | `SIT_TRAB` | texto | Situação no mercado de trabalho. Situação de trabalho do indivíduo que sofreu o agravo | 01. Empregado registrado com carteira assinada 02. Empregado não registrado 03. Autônomo/conta própria 04. Servidor público estatuário 05. Servidor público celetista 06. Aposentado 07. Desempregado 08. Trabalho tempor... | todos |
| `nutempo` | `NUTEMPO` | texto | Número que compõe o tempo (de exposição ou de ocorrência); a unidade está em `tptempo` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tptempo` | `TPTEMPO` | texto | Unidade do tempo informado em `nutempo` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `cnae` | `CNAE` | texto | Código da atividade Econômica(CNAE). Classificação Nacional da Atividade Econômica do Contratante | — | todos |
| `uf_emp` | `UF_EMP` | texto | UF. Unidade da Federação | — | todos |
| `mun_emp` | `MUN_EMP` | texto | Município. Código (IBGE) | — | todos |
| `terceiriza` | `TERCEIRIZA` | texto | O empregador é empresa Terceirizada | 01- sim 02- não 03- não se aplica 09- ignorado | todos |
| `fluxo_aere` | `FLUXO_AERE` | texto | Agravos associados Limitação crônica ao fluxo aéreo. Condição associada ao agravo – Limitação crônica ao fluxo aéreo | 1- sim 2- não 9- ignorado | todos |
| `tube` | `TUBE` | texto | Agravos associados Tuberculose. Condição associada ao agravo – Tuberculose | 1- sim 2- não 9- ignorado | todos |
| `cancer` | `CANCER` | texto | Agravos associados Câncer. Condição associada ao agravo – Câncer | 1- sim 2- não 9- ignorado | todos |
| `artrite` | `ARTRITE` | texto | Agravos associados Artrite reumatóide. st_doenca_artrite_reumatoid e | 1- sim 2- não 9- ignorado | todos |
| `tireoidite` | `TIREOIDITE` | texto | Agravos associados Tireoidite. Condição associada ao agravo – Tireoidite | 1- sim 2- não 9- ignorado | todos |
| `outro_doe` | `OUTRO_DOE` | texto | Agravos associados Outros | — | todos |
| `nutemporis` | `NUTEMPORIS` | texto | Número que compõe o tempo de exposição ao agente de risco; a unidade está em `tptemporis` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tptemporis` | `TPTEMPORIS` | texto | Unidade do tempo informado em `nutemporis` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `regime` | `REGIME` | texto | Regime de tratamento | 1- hospitalar 2- ambulatorial | todos |
| `poeiras` | `POEIRAS` | texto | A exposição a poeiras e minerais ocorreu em um ou mais vínculos distintos da empresa. Se = 2, 9 ou null, pular para campo 51 (Agentes de Exposição) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `silica` | `SILICA` | texto | Agentes de Exposição Sílica. O paciente esteve exposto à Sílica | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `asbesto` | `ASBESTO` | texto | Agentes de Exposição Asbesto. O paciente esteve exposto ao Asbesto | 1 – Sim 2 – Não | todos |
| `carvao` | `CARVAO` | texto | Agentes de Exposição Poeiras de carvão mineral. O paciente esteve exposto a Poeiras de Carvão Mineral | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `poe_mista` | `POE_MISTA` | texto | Agentes de Exposição Poeira mista (silicato, talco). O paciente esteve exposto a Poeira mista (silicato, talco) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `metal` | `METAL` | texto | Agentes de Exposição metais duros (cobalto,titânio, tungestênio). O paciente esteve exposto a metais duros | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `poe_abrasi` | `POE_ABRASI` | texto | Agentes de Exposição Poeiras de abrasivos. O paciente esteve exposto a Poeiras de abrasivos | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `berilio` | `BERILIO` | texto | Agentes de Exposição berilio. O paciente esteve exposto a berilio | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `poe_organi` | `POE_ORGANI` | texto | Agentes de Exposição Poeiras orgânicas. O paciente esteve exposto a poeira orgânica | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `fuma` | `FUMA` | texto | Hábito de fumar. Hábito do paciente em relação ao fumo | 1 – Sim 2 – Não 3 – Ex-fumante 9 – Ignorado | todos |
| `tempo_fuma` | `TEMPO_FUMA` | texto | Tempo de tabagismo (número); a unidade está em `tp_temp_fu` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tp_temp_fu` | `TP_TEMP_FU` | texto | Unidade do tempo de tabagismo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `raiox` | `RAIOX` | texto | Confirmação Diagnóstica Radiografia de tórax. Confirmação de Diagnóstico através de Radiografia de Tórax | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `biopsia` | `BIOPSIA` | texto | Confirmação Diagnóstica Biópsia pulmonar. Confirmação de Diagnóstico através de Biópsia Pulmonar | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `tomografia` | `TOMOGRAFIA` | texto | Confirmação Diagnóstica Tomografia de tórax de alta resolução. Confirmação de Diagnóstico através de Tomografia de tórax de alta resolução | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `out_exame` | `OUT_EXAME` | texto | Confirmação Diagnóstica Outro. Confirmação de Diagnóstico através de outro exame/outra prova | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `diag_esp` | `DIAG_ESP` | texto | Diagnóstico Específico CID 10. Diagnóstico específico – CID 10 | — | todos |
| `trab_doe` | `TRAB_DOE` | texto | Há ou houve outros trabalhadores com a. st_trabalhador_mesma_doe nca | 1 – Sim 2 – Não | todos |
| `stavalia` | `STAVALIA` | texto | Avaliação funcional (prova de função pulmonar) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stresulta` | `STRESULTA` | texto | Resultado da avaliação funcional. st_resulta_avaliacao_funcion al | 1- Normal 2- Alterada | todos |
| `afast_risc` | `AFAST_RISC` | texto | Conduta geral afastamento do agente do risco com mudança de função e/ ou posto de trabalho. st_conduta_afastamento_ris co | 1- Sim 2- Não | todos |
| `individual` | `INDIVIDUAL` | texto | Conduta geral adoção de proteção individual. st_conduta_protecao_individ ual | 1-Sim 2-Não | todos |
| `muda_trab` | `MUDA_TRAB` | texto | Conduta geral adoção de mudança na organização do trabalho. st_conduta_mudanca_trabal ho | 1-Sim 2- Não | todos |
| `nenhum` | `NENHUM` | texto | Conduta geral nenhum. Atitude tomada em relação ao agravo – nenhuma | 1-Sim 2-Não | todos |
| `coletiva` | `COLETIVA` | texto | Conduta geral adoção de proteção coletiva. st_conduta_protecao_coletiv a | 1-Sim 2-Não | todos |
| `afast_trab` | `AFAST_TRAB` | texto | Conduta geral Afastamento do local de trabalho. Atitude tomada em relação ao agravo – afastamento do local de trabalho | 1-Sim 2-Não | todos |
| `conduta` | `CONDUTA` | texto | Conduta geral outros. Atitude tomada em relação ao agravo – outros | 1-Sim 2-Não | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. Como evoluiu a situação do paciente | 1- Cura 2- Cura não confirmada 3- Incapacidade temporária 4- Incapacidade permanente parcial 5- Incapacidade permanente total 6- Óbito por doença relacionada ao trabalho 7- Óbito por outra causa 8- Outro 9- Ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Se óbito, data. Data do óbito | — | todos |
| `cat` | `CAT` | texto | Foi emitida a comunicação de acidente do trabalho | 1- Sim 2- Não 3- Não se aplica 9- Ignorado | todos |
| `out_doe_de` | `OUT_DOE_DE` | texto | Agravos associados se Outros especificar | — | todos |
| `vinc_esp` | `VINC_ESP` | texto | Especificar. Habilitar se campo 49 (A exposição a poeiras e minerais ocorreu em um ou mais vínculos distintos da empresa) = 1 | — | todos |
| `condut_des` | `CONDUT_DES` | texto | Conduta geral Se outros especificar | — | todos |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal. nu_lote_horizont al | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-pneu`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 10, inteiro: 1, nulo (vazio nas amostras): 4, texto: 72.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-pneu.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- a latência longa e o nexo dependente de leitura radiológica padronizada (OIT) tornam a base pequena e sujeita a subnotificação; o tipo de pneumoconiose pode não ser codificado de forma padronizada entre anos. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. Arquivos do diretório PRELIM (2023+) são preliminares; como `NU_NOTIFIC` não consta dos arquivos públicos, deduplique por combinação de campos (ex.: `ID_UNIDADE`, `DT_NOTIFIC`, `ID_MN_RESI`, `ANO_NASC`, `CS_SEXO`) ao combinar as duas fontes. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-pneu/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-pneu
quantilica datasus list sinan-pneu

# 2. Baixar microdados de sinan-pneu (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-pneu -o ./data --start 2015 --end 2022 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-pneu -o ./data --docs --aux --start 2015 --end 2022 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-pneu -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2022 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/PNEUBR22.dbc", dataset="sinan-pneu")

# Notificações por UF e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Tipos de pneumoconiose e agentes de exposição mais frequentes
print(
    frame.group_by("id_agravo")
    .agg(pl.len().alias("n"))
    .sort("n", descending=True)
    .head()
)
print(
    frame.group_by("id_ocupa_n")
    .agg(pl.len().alias("n"))
    .sort("n", descending=True)
    .head()
)
print(resumo.head())
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (DRT Pneumoconioses Relacionadas ao Trabalho): https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Saúde do Trabalhador: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- RENAST — Rede Nacional de Atenção Integral à Saúde do Trabalhador: https://www.gov.br/saude/pt-br/composicao/svsa/saude-do-trabalhador/renast
