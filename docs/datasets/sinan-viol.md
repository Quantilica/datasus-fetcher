---
dataset:
  id: sinan-viol
  fonte: datasus
  titulo: Violência doméstica, sexual e/ou outras violências
  resumo: 'Violência doméstica, sexual e/ou outras violências do DATASUS: uma ficha de notificação/investigação de violência doméstica, sexual e/ou outras violências.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2009'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de violência doméstica, sexual e/ou outras violências
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 161
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Violência doméstica, sexual e/ou outras violências (`sinan-viol`)

## Resumo

Notificações de violência interpessoal e autoprovocada (incluindo tentativas de suicídio), de notificação compulsória no SINAN. Cada linha representa uma ficha de notificação/investigação de um caso de violência doméstica, sexual, física, psicológica ou outras formas, atendido em serviços de saúde.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM, 2025; Finais até 2024)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `VIOL` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `VIOL` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `VIOLBR24.dbc`, em que `VIOL` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024). O arquivo preliminar mais recente é `VIOLBR25.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-viol/<AAAA>/sinan-viol_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-viol/2024/sinan-viol_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`Violência Interpessoal/Autoprovocada`) é distribuído no Portal SINAN e no VIVA; não há PDF por agravo no FTP.

## Conteúdo

A notificação de violências é compulsória e imediata em todo o território nacional, conforme a Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023). A vigilância é coordenada pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), em articulação com a área de Vigilância de Violências e Acidentes (VIVA). A notificação de violência contra crianças, adolescentes, mulheres e pessoas idosas decorre de marcos legais como o ECA (Lei nº 8.069/1990), a Lei Maria da Penha (Lei nº 11.340/2006) e o Estatuto da Pessoa Idosa (Lei nº 10.741/2003).

O evento gerador é qualquer caso suspeito ou confirmado de violência interpessoal (doméstica/intrafamiliar, comunitária) ou autoprovocada, incluindo a violência física, psicológica/moral, sexual, tortura, tráfico de seres humanos, violência financeira/econômica, trabalho infantil, intervenção legal e negligência/abandono. O CID-10 utilizado abrange o Capítulo XX (V01–Y98), com destaque para agressões (X85–Y09) e lesões autoprovocadas (X60–X84). A unidade de análise é o caso notificado (um registro por ficha).

O instrumento é a *Ficha de Notificação/Investigação Individual — Violência Interpessoal/Autoprovocada*, que registra dados da pessoa atendida, local de ocorrência, lesões e partes do corpo atingidas, meios de agressão, formas de violência, dados do autor provável da agressão e grau de parentesco. A série no FTP inicia em 2009 (implantação do Sinan Net para violência) e o ano de 2025 está em PRELIM, sujeito a revisão.

Principais usos: dimensionamento e caracterização da violência no país, monitoramento de casos por faixa etária e sexo, vigilância de violência sexual e de violência contra grupos vulneráveis, apoio à rede de proteção e à formulação de políticas públicas de prevenção.

### Cobertura observada

- Índice do FTP (2026-10): 17 arquivos, de 2009 a 2025, 1 UF(s) com arquivos, última atualização em 2026-10-19.
- Conversão local de amostras (4 arquivo(s) Parquet, de 2009 a 2025), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo `VIOLBR09.dbc` (leiaute do SINAN Net; fichas e leiautes podem variar entre anos, por isso a lista reflete esse arquivo). Os arquivos públicos não trazem identificadores individuais como número da notificação (`NU_NOTIFIC`) nem data de nascimento completa. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (registro da ficha de notificação individual). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado. |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | String | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE). |
| `DT_OCOR` | Data (AAAAMMDD) | Data da ocorrência da violência. |
| `SEM_PRI` | String | Semana epidemiológica da ocorrência (AAAASS). |
| `ANO_NASC` | String | Ano de nascimento (o arquivo público não traz a data de nascimento completa). |
| `NU_IDADE_N` | Inteiro | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade. |
| `SG_UF` | String | UF de residência (código IBGE de 2 dígitos). |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `NDUPLIC` | String | Indicador de duplicidade da ficha. |
| `DT_INVEST` | Data (AAAAMMDD) | Data da investigação. |
| `ID_OCUPA_N` | String | Ocupação do trabalhador (CBO 2002, 6 dígitos). |
| `SIT_CONJUG` | String | Situação conjugal. |
| `DEF_TRANS` | String | Pessoa com deficiência/transtorno (geral). |
| `DEF_FISICA` | String | Deficiência física. |
| `DEF_MENTAL` | String | Deficiência mental. |
| `DEF_VISUAL` | String | Deficiência visual. |
| `DEF_AUDITI` | String | Deficiência auditiva. |
| `TRAN_MENT` | String | Transtorno mental. |
| `TRAN_COMP` | String | Transtorno de comportamento. |
| `SG_UF_OCOR` | String | UF de ocorrência da violência. |
| `ID_MN_OCOR` | String | Município de ocorrência da violência (código IBGE). |
| `HORA_OCOR` | String | Hora da ocorrência. |
| `LOCAL_OCOR` | String | Local de ocorrência (descrição de outros em `LOCAL_ESPE`). |
| `OUT_VEZES` | String | A violência ocorreu outras vezes. |
| `LES_AUTOP` | String | Lesão autoprovocada (distingue violência autoprovocada). |
| `VIOL_FISIC` | String | Violência física. |
| `VIOL_PSICO` | String | Violência psicológica/moral. |
| `VIOL_TORT` | String | Tortura. |
| `VIOL_SEXU` | String | Violência sexual. |
| `VIOL_TRAF` | String | Tráfico de seres humanos. |
| `VIOL_FINAN` | String | Violência financeira/econômica. |
| `VIOL_NEGLI` | String | Negligência/abandono. |
| `VIOL_INFAN` | String | Trabalho infantil. |
| `VIOL_LEGAL` | String | Intervenção legal. |
| `VIOL_OUTR` | String | Outra violência (descrição em `VIOL_ESPEC`). |
| `AG_FORCA` | String | Meio de agressão: força corporal/espancamento. |
| `AG_ENFOR` | String | Meio de agressão: enforcamento. |
| `AG_OBJETO` | String | Meio de agressão: objeto contundente. |
| `AG_CORTE` | String | Meio de agressão: objeto perfurocortante. |
| `AG_QUENTE` | String | Meio de agressão: substância/objeto quente. |
| `AG_ENVEN` | String | Meio de agressão: envenenamento. |
| `AG_FOGO` | String | Meio de agressão: arma de fogo. |
| `AG_AMEACA` | String | Meio de agressão: ameaça. |
| `AG_OUTROS` | String | Outro meio de agressão (descrição em `AG_ESPEC`). |
| `SEX_ASSEDI` | String | Violência sexual: assédio sexual. |
| `SEX_ESTUPR` | String | Violência sexual: estupro. |
| `SEX_PUDOR` | String | Violência sexual: atentado violento ao pudor. |
| `SEX_PORNO` | String | Violência sexual: pornografia infantil. |
| `SEX_EXPLO` | String | Violência sexual: exploração sexual. |
| `SEX_OUTRO` | String | Violência sexual: outra (descrição em `SEX_ESPEC`). |
| `LESAO_NAT` | String | Natureza da lesão. |
| `LESAO_CORP` | String | Parte do corpo atingida. |
| `NUM_ENVOLV` | String | Número de envolvidos. |
| `REL_PAI` | String | Autor: pai. |
| `REL_MAE` | String | Autor: mãe. |
| `REL_PAD` | String | Autor: padrasto. |
| `REL_CONJ` | String | Autor: cônjuge. |
| `REL_EXCON` | String | Autor: ex-cônjuge. |
| `REL_NAMO` | String | Autor: namorado(a). |
| `REL_EXNAM` | String | Autor: ex-namorado(a). |
| `REL_FILHO` | String | Autor: filho(a). |
| `REL_DESCO` | String | Autor: desconhecido. |
| `REL_IRMAO` | String | Autor: irmão(ã). |
| `REL_CONHEC` | String | Autor: amigo/conhecido. |
| `REL_CUIDA` | String | Autor: cuidador(a). |
| `REL_PATRAO` | String | Autor: patrão/chefe. |
| `REL_INST` | String | Autor: pessoa com relação institucional. |
| `REL_POL` | String | Autor: policial/agente da lei. |
| `REL_PROPRI` | String | Autor: próprio. |
| `REL_OUTROS` | String | Autor: outro vínculo (descrição em `REL_ESPEC`). |
| `AUTOR_SEXO` | String | Sexo do provável autor. |
| `AUTOR_ALCO` | String | Suspeita de uso de álcool pelo provável autor. |
| `ENC_SAUDE` | String | Encaminhamento: rede de saúde. |
| `ENC_TUTELA` | String | Encaminhamento: conselho tutelar. |
| `ENC_DEAM` | String | Encaminhamento: delegacia da mulher (DEAM). |
| `ENC_DELEG` | String | Encaminhamento: delegacia. |
| `ENC_MPU` | String | Encaminhamento: Ministério Público. |
| `ENC_CREAS` | String | Encaminhamento: CREAS. |
| `ENC_IML` | String | Encaminhamento: IML. |
| `ENC_OUTR` | String | Encaminhamento: outros (descrição em `ENC_ESPEC`). |
| `REL_TRAB` | String | Violência relacionada ao trabalho. |
| `CIRC_LESAO` | String | Circunstância da lesão (CID-10, causa externa). |
| `CLASSI_FIN` | String | Classificação final do caso. |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito, quando aplicável. |
| `REL_MAD` | String | Autor: madrasta. |
| `TPUNINOT` | String | Tipo de unidade notificadora. |
| `ORIENT_SEX` | String | Orientação sexual. |
| `IDENT_GEN` | String | Identidade de gênero. |
| `VIOL_MOTIV` | String | Motivação da violência. |
| `CICL_VID` | String | Ciclo de vida. |
| `DT_ENCERRA` | Data (AAAAMMDD) | Data de encerramento da investigação. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; neurológica aguda; insuficiência renal aguda; outras síndromes | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológica da notificação (campo interno) | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação | — | todos |
| `dt_ocor` | `DT_OCOR` | data | Data da ocorrência da violência | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológica dos primeiros sintomas/ diagnósticos. (campo interno) | — | todos |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o dígito: 1. Hora 2. Dia 3. Mês 4. Ano Ex: 3009 – nove meses, 4018 – dezoito anos | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil). a | — | todos |
| `nduplic` | `NDUPLIC` | texto | Indicador de duplicidade do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_invest` | `DT_INVEST` | data | Data da investigação. data de início da investigação do caso | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Categorias da tabela (Indicar aqui qual a tabela que é utilizado no Sinan NET) | — | todos |
| `sit_conjug` | `SIT_CONJUG` | texto | Situação conjugal | 1. Solteiro 2. Casado/ União consensual 3. Viúvo 4. Separado 8. Não se aplica | todos |
| `def_trans` | `DEF_TRANS` | texto | Possui algum tipo de deficiência/ transtorno | 1. Sim 2. Não 9. Ignorado | todos |
| `def_fisica` | `DEF_FISICA` | texto | Deficiência física | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `def_mental` | `DEF_MENTAL` | texto | Deficiência intelectual | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `def_visual` | `DEF_VISUAL` | texto | Deficiência visual | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `def_auditi` | `DEF_AUDITI` | texto | Deficiência auditiva | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `tran_ment` | `TRAN_MENT` | texto | Transtorno mental | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `tran_comp` | `TRAN_COMP` | texto | Transtorno de. Se o paciente possui algum tipo | 1. Sim | todos |
| `def_out` | `DEF_OUT` | texto | Outras deficiências/ síndromes | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `def_espec` | `DEF_ESPEC` | texto | Outras deficiências/ síndromes (especificar). Especificar qual o tipo de outras deficiências/síndromes | — | todos |
| `sg_uf_ocor` | `SG_UF_OCOR` | texto | UF de ocorrência. Sigla da Unidade Federada de ocorrência do evento por ocasião da notificação | — | todos |
| `id_mn_ocor` | `ID_MN_OCOR` | texto | Município de ocorrência. idência | — | todos |
| `hora_ocor` | `HORA_OCOR` | texto | Hora de ocorrência. hora (hh:mm) | — | todos |
| `local_ocor` | `LOCAL_OCOR` | texto | Local de ocorrência | 01. Residência 02. Habitação coletiva 03. Escola 04. Local de prática esportiva 05. Bar ou similar 06. Via publica 07. Comércio/Serviços 08. Industrias/ construção 09. Outro 99. Ignorado | todos |
| `local_espe` | `LOCAL_ESPE` | texto | Local de ocorrência - Outro (especificar). Ds_outro_tp_loca l_ocorrencia | — | todos |
| `out_vezes` | `OUT_VEZES` | texto | Ocorreu outras vezes? | 1. Sim 2. Não 9. Ignorado | todos |
| `les_autop` | `LES_AUTOP` | texto | A lesão foi autoprovocada? | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `viol_fisic` | `VIOL_FISIC` | texto | Tipo de Violência - Física. a | 1. Sim 2. Não 9. Ignorado | todos |
| `viol_psico` | `VIOL_PSICO` | texto | Tipo de Violência - psicológica/ moral. o_moral | 1. Sim 2. Não 9. Ignorado | todos |
| `viol_tort` | `VIOL_TORT` | texto | Tipo de Violência - Tortura. Informar se ocorreu tortura | 1. Sim 2. Não 9. Ignorado | todos |
| `viol_sexu` | `VIOL_SEXU` | texto | Tipo de Violência - Sexual | 1. Sim 2. Não 9. Ignorado | todos |
| `viol_traf` | `VIOL_TRAF` | texto | Tipo de Violência - Tráfico de seres humanos | 1. Sim 2. Não 9. Ignorado | todos |
| `viol_finan` | `VIOL_FINAN` | texto | Tipo de Violência -. Informar se ocorreu violência | 1. Sim | todos |
| `viol_negli` | `VIOL_NEGLI` | texto | Tipo de Violência - Negligencia/ abandono | 1. Sim 2. Não 9. Ignorado | todos |
| `viol_infan` | `VIOL_INFAN` | texto | Tipo de Violência - Trabalho infantil | 1. Sim 2. Não 9. Ignorado | todos |
| `viol_legal` | `VIOL_LEGAL` | texto | Tipo de Violência - Intervenção legal | 1. Sim 2. Não 9. Ignorado | todos |
| `viol_outr` | `VIOL_OUTR` | texto | Tipo de Violência - Outros | 1. Sim 2. Não 9. Ignorado | todos |
| `viol_espec` | `VIOL_ESPEC` | texto | Outros tipos de violência (especificar) | — | todos |
| `ag_forca` | `AG_FORCA` | texto | Meio de Agressão Força corporal/ espancamento. _espancamento | 1. Sim 2. Não 9. Ignorado | todos |
| `ag_enfor` | `AG_ENFOR` | texto | Meio de Agressão Enforcamento. Informar se o meio de agressão foi através de enforcamento | 1. Sim 2. Não 9. Ignorado | todos |
| `ag_objeto` | `AG_OBJETO` | texto | Meio de Agressão Objeto contundente | 1. Sim 2. Não 9. Ignorado | todos |
| `ag_corte` | `AG_CORTE` | texto | Meio de Agressão Objeto perfuro-cortante. _cortante | 1. Sim 2. Não 9. Ignorado | todos |
| `ag_quente` | `AG_QUENTE` | texto | Meio de Agressão Substancia/objeto | 1. Sim 2. Não | todos |
| `ag_enven` | `AG_ENVEN` | texto | Meio de Agressão Envenenamento, Intoxicação. o | 1. Sim 2. Não 9. Ignorado | todos |
| `ag_fogo` | `AG_FOGO` | texto | Meio de Agressão Arma de fogo. Informar se o meio de agressão foi através de arma de fogo | 1. Sim 2. Não 9. Ignorado | todos |
| `ag_ameaca` | `AG_AMEACA` | texto | Meio de Agressão Ameaça. Informar se o meio de agressão foi através de ameaça | 1. Sim 2. Não 9. Ignorado | todos |
| `ag_outros` | `AG_OUTROS` | texto | Meio de Agressão Outro | 1. Sim 2. Não 9. Ignorado | todos |
| `ag_espec` | `AG_ESPEC` | texto | Meio de Agressão Outro meio de agressão (especificar) | — | todos |
| `sex_assedi` | `SEX_ASSEDI` | texto | Se ocorreu violência sexual, qual tipo? - Assedio sexual. cia_assedio | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `sex_estupr` | `SEX_ESTUPR` | texto | Se ocorreu violência sexual, qual tipo? - Estupro. cia_estupro | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `sex_pudor` | `SEX_PUDOR` | texto | Característica da violência sexual ou da lesão (`SEX_PUDOR`) | — | todos |
| `sex_porno` | `SEX_PORNO` | texto | Se ocorreu violência sexual, qual tipo? - Pornografia infantil. cia_porno_inf | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `sex_explo` | `SEX_EXPLO` | texto | Se ocorreu violência sexual, qual tipo? - Exploração sexual. c_exp_sexual | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `sex_outro` | `SEX_OUTRO` | texto | Se ocorreu violência sexual, qual tipo? - Outro. _sexual_outro | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `sex_espec` | `SEX_ESPEC` | texto | Se ocorreu violência sexual, qual tipo? - Outro tipo de violência sexual (especificar). n_sexual_outro | — | todos |
| `pen_oral` | `PEN_ORAL` | texto | Característica da violência sexual ou da lesão (`PEN_ORAL`) | — | todos |
| `pen_anal` | `PEN_ANAL` | texto | Característica da violência sexual ou da lesão (`PEN_ANAL`) | — | todos |
| `pen_vagina` | `PEN_VAGINA` | texto | Característica da violência sexual ou da lesão (`PEN_VAGINA`) | — | todos |
| `proc_dst` | `PROC_DST` | texto | Procedimento realizado – Profilaxia DST. _dst | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `proc_hiv` | `PROC_HIV` | texto | Procedimento realizado – Profilaxia HIV. _hiv | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `proc_hepb` | `PROC_HEPB` | texto | Procedimento realizado – Profilaxia Hepatite B. _hepatite_b | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `proc_sang` | `PROC_SANG` | texto | Procedimento realizado – Coleta de sangue | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `proc_semen` | `PROC_SEMEN` | texto | Procedimento realizado – Coleta de sêmen | 1. Sim 2. Não 8. Não se aplica | todos |
| `proc_vagin` | `PROC_VAGIN` | texto | Característica da violência sexual ou da lesão (`PROC_VAGIN`) | — | todos |
| `proc_contr` | `PROC_CONTR` | texto | Procedimento realizado – Contracepção de emergência. cao_emergenc | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `proc_abort` | `PROC_ABORT` | texto | Procedimento realizado - Aborto previsto em lei. evisto_lei | 1. Sim 2. Não 8. Não se aplica 9. Ignorado | todos |
| `cons_abort` | `CONS_ABORT` | texto | Consequência identificada da violência (`CONS_ABORT`) | — | todos |
| `cons_grav` | `CONS_GRAV` | texto | Consequência identificada da violência (`CONS_GRAV`) | — | todos |
| `cons_dst` | `CONS_DST` | texto | Consequência identificada da violência (`CONS_DST`) | — | todos |
| `cons_suic` | `CONS_SUIC` | texto | Consequência identificada da violência (`CONS_SUIC`) | — | todos |
| `cons_ment` | `CONS_MENT` | texto | Consequência identificada da violência (`CONS_MENT`) | — | todos |
| `cons_comp` | `CONS_COMP` | texto | Consequência identificada da violência (`CONS_COMP`) | — | todos |
| `cons_estre` | `CONS_ESTRE` | texto | Consequência identificada da violência (`CONS_ESTRE`) | — | todos |
| `cons_outr` | `CONS_OUTR` | texto | Consequência identificada da violência (`CONS_OUTR`) | — | todos |
| `cons_espec` | `CONS_ESPEC` | texto | Consequência identificada da violência (`CONS_ESPEC`) | — | todos |
| `lesao_nat` | `LESAO_NAT` | texto | Característica da violência sexual ou da lesão (`LESAO_NAT`) | — | todos |
| `lesao_espe` | `LESAO_ESPE` | texto | Característica da violência sexual ou da lesão (`LESAO_ESPE`) | — | todos |
| `lesao_corp` | `LESAO_CORP` | texto | Característica da violência sexual ou da lesão (`LESAO_CORP`) | — | todos |
| `num_envolv` | `NUM_ENVOLV` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `rel_sexual` | `REL_SEXUAL` | texto | Relação da vítima com o provável autor da violência (`REL_SEXUAL`) | — | todos |
| `rel_pai` | `REL_PAI` | texto | Relação com a pessoa atendida – Pai. _pai | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_mae` | `REL_MAE` | texto | Relação com a pessoa atendida – Mãe. _mae | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_pad` | `REL_PAD` | texto | Relação com a pessoa atendida – Padrasto. _padrasto | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_conj` | `REL_CONJ` | texto | Relação com a pessoa atendida – Cônjuge. _conjuge | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_excon` | `REL_EXCON` | texto | Relação com a pessoa atendida – Ex- cônjuge. _ex_conjuge | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_namo` | `REL_NAMO` | texto | Relação com a pessoa atendida – Namorado(a). _namorado | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_exnam` | `REL_EXNAM` | texto | Relação com a pessoa atendida – Ex- namorado(a). _ex_namorado | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_filho` | `REL_FILHO` | texto | Relação com a pessoa atendida – Filho (a). _filho | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_desco` | `REL_DESCO` | texto | Relação com a pessoa atendida – Desconhecido. _desconhecido | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_irmao` | `REL_IRMAO` | texto | Relação da vítima com o provável autor da violência (`REL_IRMAO`) | — | todos |
| `rel_conhec` | `REL_CONHEC` | texto | Relação com a pessoa atendida – Amigos/conhecidos. _amigo_conhecid o | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_cuida` | `REL_CUIDA` | texto | Relação com a pessoa atendida – cuidador. _cuidador | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_patrao` | `REL_PATRAO` | texto | Relação com a pessoa atendida – patrão/chefe. _patrao_chefe | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_inst` | `REL_INST` | texto | Relação com a pessoa atendida – pessoa com relação institucional. _institucional | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_pol` | `REL_POL` | texto | Relação com a pessoa atendida – policial/agente da lei. _agente | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_propri` | `REL_PROPRI` | texto | Relação com a pessoa atendida – Própria pessoa | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_outros` | `REL_OUTROS` | texto | Relação com a pessoa atendida – Outros. _outro | 1. Sim 2. Não 9. Ignorado | todos |
| `rel_espec` | `REL_ESPEC` | texto | Relação com a pessoa atendida – Outros (especificar). r_outro | — | todos |
| `autor_sexo` | `AUTOR_SEXO` | texto | Sexo do provável autor da violência. _autor | 1. Masculino 2. Feminino 3. Ambos os sexos 9 .Ignorado | todos |
| `autor_alco` | `AUTOR_ALCO` | texto | Suspeita de uso de álcool | 1. Sim 2. Não 9. Ignorado | todos |
| `enc_saude` | `ENC_SAUDE` | texto | Encaminhamento - Rede da Saúde. Informar se houve encaminhamento no setor da rede da saúdel | 1-Sim 2-Não 9-Ignorado | todos |
| `enc_tutela` | `ENC_TUTELA` | texto | Encaminhamento realizado no atendimento da vítima (`ENC_TUTELA`) | — | todos |
| `enc_vara` | `ENC_VARA` | texto | Encaminhamento realizado no atendimento da vítima (`ENC_VARA`) | — | todos |
| `enc_abrigo` | `ENC_ABRIGO` | texto | Encaminhamento realizado no atendimento da vítima (`ENC_ABRIGO`) | — | todos |
| `enc_sentin` | `ENC_SENTIN` | texto | Encaminhamento realizado no atendimento da vítima (`ENC_SENTIN`) | — | todos |
| `enc_deam` | `ENC_DEAM` | texto | Encaminhamento realizado no atendimento da vítima (`ENC_DEAM`) | — | todos |
| `enc_dpca` | `ENC_DPCA` | texto | Encaminhamento realizado no atendimento da vítima (`ENC_DPCA`) | — | todos |
| `enc_deleg` | `ENC_DELEG` | texto | Encaminhamento realizado no atendimento da vítima (`ENC_DELEG`) | — | todos |
| `enc_mpu` | `ENC_MPU` | texto | Encaminhamento realizado no atendimento da vítima (`ENC_MPU`) | — | todos |
| `enc_mulher` | `ENC_MULHER` | texto | Encaminhamento realizado no atendimento da vítima (`ENC_MULHER`) | — | todos |
| `enc_creas` | `ENC_CREAS` | texto | Encaminhamento realizado no atendimento da vítima (`ENC_CREAS`) | — | todos |
| `enc_iml` | `ENC_IML` | texto | Encaminhamento realizado no atendimento da vítima (`ENC_IML`) | — | todos |
| `enc_outr` | `ENC_OUTR` | texto | Encaminhamento realizado no atendimento da vítima (`ENC_OUTR`) | — | todos |
| `enc_espec` | `ENC_ESPEC` | texto | Encaminhamento realizado no atendimento da vítima (`ENC_ESPEC`) | — | todos |
| `rel_trab` | `REL_TRAB` | texto | Violência relacionada ao trabalho | 1-Sim 2-Não 9-Ignorado | todos |
| `rel_cat` | `REL_CAT` | texto | Se sim, foi emitida a comunicação de acidente de trabalho (CAT). Informar se foi emitida a CAT, caso a violência seja relacionada ao trabalho | 1-Sim 2-Não 8-Não se aplica 9-Ignorado | todos |
| `circ_lesao` | `CIRC_LESAO` | texto | Circunstância da lesão. Tabela de agravos do sistema com códigos (classificação internacional de doenças - CID 10) e nomes dos agravos | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final | — | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. o | — | todos |
| `dt_obito` | `DT_OBITO` | data | Data de óbito | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `rel_mad` | `REL_MAD` | texto | Relação com a pessoa atendida – Madrasta. _madastra | 1. Sim 2. Não 9. Ignorado | todos |
| `tpuninot` | `TPUNINOT` | texto | Tipo da unidade notificadora (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `orient_sex` | `ORIENT_SEX` | texto | Orientação sexual. tp_orientaçao_sex ual | 1. Heterossexual 2. Homossexual (gay/lésbica) 3. Bissexual 8. Não se aplica 9. Ignorado | todos |
| `ident_gen` | `IDENT_GEN` | texto | Identidade de Gênero. Identidade de gênero do paciente | 1. Travesti 2. Transexual Mulher 3. Transexual Homem 8. Não se aplica 9. Ignorado | todos |
| `viol_motiv` | `VIOL_MOTIV` | texto | Violência motivada por: | 01. Sexismo 02. Homofobia/Lesbofobia Bifobia/Transfobia 03. Racismo 04. Intolerância religiosa 05. Xenofobia 06. Conflito geracional 07. Situação de rua 08. Deficiência 09. Outros 88. Não se aplica 99. Ignorado | todos |
| `cicl_vid` | `CICL_VID` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `rede_sau` | `REDE_SAU` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `assist_soc` | `ASSIST_SOC` | texto | Encaminhamento - Rede da Assistencia Social | 1-Sim 2-Não 9-Ignorado | todos |
| `rede_educa` | `REDE_EDUCA` | texto | Encaminhamento - Rede de Educação. ção | 1-Sim 2-Não 9-Ignorado | todos |
| `atend_mulh` | `ATEND_MULH` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `cons_tutel` | `CONS_TUTEL` | texto | Encaminhamento - Conselho Tutelar | 1-Sim 2-Não 9-Ignorado | todos |
| `cons_ido` | `CONS_IDO` | texto | Encaminhamento - Conselho do Idoso. Informar se houve encaminhamento para o Conselho do Idoso | 1-Sim 2-Não 9-Ignorado | todos |
| `deleg_idos` | `DELEG_IDOS` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `dir_human` | `DIR_HUMAN` | texto | Encaminhamento - Centro de Referência dos Direitos Humanos. St_centro_ref_dir eitos_humanos | 1-Sim 2-Não 9-Ignorado | todos |
| `mpu` | `MPU` | texto | Encaminhamento -. Informar se houve | 1-Sim | todos |
| `deleg_cria` | `DELEG_CRIA` | texto | Encaminhamento - Delegacia Especializada de Proteção à Criança e Adolescente. st_del_proteção_c riança_adolescent e | 1-Sim 2-Não 9-Ignorado | todos |
| `deleg_mulh` | `DELEG_MULH` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `deleg` | `DELEG` | texto | Encaminhamento - Outras delegacias. st_ _outra_delegacia | 1-Sim 2-Não 9-Ignorado | todos |
| `infan_juv` | `INFAN_JUV` | texto | Encaminhamento - Justiça da infância e da Juventude. st_justiça_infanci a_juventude | 1-Sim 2-Não 9-Ignorado | todos |
| `defen_publ` | `DEFEN_PUBL` | texto | Encaminhamento - Defensoria pública | 1-Sim 2-Não 9-Ignorado | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data de encerramento. data de encerramento do caso | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-viol`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 12, inteiro: 1, texto: 148.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-viol.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- os campos de forma de violência são múltiplos (uma ficha pode ter mais de uma marcada) e devem ser tratados como flags independentes; a presença de `LES_AUTOP` distingue violência autoprovocada de interpessoal. A notificação depende de atendimento em serviço de saúde, o que implica subnotificação importante, especialmente em violência psicológica e em áreas sem rede de proteção estruturada. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. O arquivo de 2025 é preliminar; como `NU_NOTIFIC` não consta dos arquivos públicos, deduplique por combinação de campos (ex.: `ID_UNIDADE`, `DT_NOTIFIC`, `ID_MN_RESI`, `ANO_NASC`, `CS_SEXO`) ao combinar as fontes. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-viol").glob("**/*.parquet"))
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
datasus-fetcher list sinan-viol

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-viol -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-viol
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (Violência Interpessoal/Autoprovocada): https://portalsinan.saude.gov.br/
- VIVA — Vigilância de Violências e Acidentes (SVSA/MS): https://www.gov.br/saude/pt-br/composicao/svsa/vigilancia-de-violencias-e-acidentes-viva
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Violências: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
