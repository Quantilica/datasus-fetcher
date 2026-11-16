---
dataset:
  id: sinan-botu
  fonte: datasus
  titulo: Botulismo
  resumo: 'Botulismo do DATASUS: uma ficha de notificação/investigação de botulismo.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de botulismo
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 152
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nuatend: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nuconsome: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: dt_nasc
    categoria: data de nascimento
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Botulismo (`sinan-botu`)

## Resumo

O `sinan-botu` contém os microdados das notificações e investigações epidemiológicas de casos de Botulismo (CID-10 A05.1) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de botulismo, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. É uma base de baixa incidência e alta gravidade (doença paralítica aguda, com uso frequente de ventilação mecânica), com 149 colunas: quadro neurológico detalhado (sintomas cranio-neuro-oftalmológicos de bulbar a respiratório), a forma de botulismo, o extenso bloco de investigação do alimento incriminado e materiais (soro, fezes e alimentos coletados com resultado e tipo de toxina), o tratamento com soro antibotulínico e a evolução do caso.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `BOTU` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `BOTU` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `BOTUBR25.dbc` — `BOTU` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As bases de 2007 a 2024 estão em `FINAIS` e os anos de 2025 e 2026 apenas em `PRELIM` (atualização de 25/05/2026).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-botu/<AAAA>/sinan-botu_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-botu/2024/sinan-botu_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip`, as instruções POP_I/II/III de acesso, descompactação e tabulação e a ficha/instruções de botulismo; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

O botulismo é agravo de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, constando hoje da Lista Nacional de Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), com apoio dos laboratórios de referência (LACEN e institutos como Adolfo Lutz) para confirmação pela detecção da toxina botulínica. É um dos agravos com resposta CIEVS mais ágil: notificação imediata por telefone/fax pelo profissional de saúde, pela baixa incidência, alta letalidade e dependência do tratamento precoce com soro antibotulínico — a detecção rápida de casos permite o bloqueio de transmispor via alimentos e permite o envio assistido de soro para os serviços de assistência.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Botulismo** do SINAN (dicionário de dados v5.0, revisado em julho/2010). A notificação nasce com a suspeição clínica de doença paralítica aguda (sintomas: diplopia/visão dupla, ptose palpebral, disfagia, disartria, disfonia, boca seca, fraqueza muscular flácida/simétrica descendente, dispneia/insuficiência respiratória: campos `ST*`) nas suas três formas — alimentar (`STALIMENTO`: suspeita de transmissão alimentar), intestinal (lactente) e por ferimento (`TPBOTULISM`: 1 - Alimentar, 2 - Intestinal, 3 - Por ferimento, 4 - Outra) — e é completada ao longo da investigação com o bloco neurológico de exames e sinais (reflexos `TPNEURO`, sinais cranio-neuro-oftalmológicos/bulbares e de membros e sensibilidade `STPTOSE`/`STOFTALMO`/`STMIDRIASE`/`STFACIAL`/`STBULBAR`/`STMEMSUP`, `STMEMINF`, `STSENSIVEL`, `TP_MOTORA`/`TP_REPETE`, eletromiografia `STELETRO`), o material coletado para pesquisa de toxina (soro, fezes e amostras de alimentos, com resultado e tipo de toxina: `STSOROMAT`/`DTSOROCOL`/`STSORORES`/`TPSOROTOX`, `STFEZESMAT`/`DTFEZESCOL`/`STFEZESRES`/`TPFEZESTOX`, amostras de alimentos/bromatológicas), o alimento incriminado e o local de ingestão/coleta (`STCASEIRA`, `STCOMERCIO`, `STEXPALIM`, `DS_INDUS`, `DS_INGEST`, locais `STDOMICILI`...`STFESTA`), o tratamento (soro antibotulínico `STSORO`, antibiótico e ventilação mecânica `STVENTILA`) e o agente incriminado se descartado (`AGENTE_OUT`). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net); as bases de 2007 a 2024 estão em `FINAIS` e os anos de 2025 e 2026 apenas em `PRELIM` (ex.: `BOTUBR25.dbc`, atualização de 25/05/2026). O dicionário de dados v5.0 (revisado em julho/2010) provê tabela de classificação final em dois grupos (1 - Confirmado; 2 - Descartado, com especificação de outro agente em `AGENTE_OUT`) e o critério de confirmação/descarte (1 - Laboratorial, 2 - Clínico-epidemiológico). O tipo de toxina botulínica é identificado no soro e nas fezes (campos `TPSOROTOX` e `TPFEZESTOX`, tipos A a G, 7 - Outra, 9 - Ignorado).

Aplicações analíticas típicas: número e distribuição de casos confirmados (baixa incidência, com foco em conservas caseiras `STCASEIRA`); formas de botulismo (`TPBOTULISM`); uso de soro antibotulínico e ventilação mecânica em UTI (`STSORO`, `STVENTILA`); letalidade (`EVOLUCAO`); e investigação do alimento incriminado e das toxinas identificadas (`TPSOROTOX`, `TPFEZESTOX`, `TP_ALI1TOX`), fundamental para bloqueios e alertas CIEVS.

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-10-29.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `BOTUBR25.dbc` (149 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `SEM_NOT` / `NU_ANO` | Data (`AAAAMMDD`)/Inteiro | Data, semana epidemiológica e ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `DT_SIN_PRI` / `SEM_PRI` | Data/Inteiro | Data e semana de início dos sintomas |
| `NU_IDADE_N` / `CS_SEXO` | Inteiro/String | Idade decomposta por unidade e sexo |
| `DT_INVEST` / `DTATEND` / `NUATEND` | Data/Inteiro | Data da investigação e dados de atendimento |
| `DTSUSPEIC` | Data (`AAAAMMDD`) | Data suspeição/primeira atuação clínica |
| `STHOSPITAL` / `DTINTERNA` / `DTALTA` | Inteiro/Data | Hospitalização, data de internação e de alta |
| `STFEBRE`/`STNAUSEA`/`STVOMITO`/`STDIARREIA`/`STCONSTIPA`/`STCEFALEIA`/`STTONTURA` | Inteiro | Sintomas prodômicos: febre, náuseas, vômitos, diarreia, constipação, cefaleia, tontura |
| `STVISAO`/`STDIPLOPIA`/`STDISARTRI`/`STDISFONIA`/`STDISFAGIA`/`STBOCA` | Inteiro | Sintomas neurológicos: visão turva/diplopia, disartria, disfonia, disfagia, boca seca |
| `STFERIMENT`/`STFLACIDEZ`/`STDISPNEIA`/`STRESPIRA`/`STCARDIACA`/`STCOMA`/`STPARESTES` | Inteiro | Ferimento, flacidez, dispneia, insuficiência respiratória/cardíaca, coma, parestesias |
| `STPTOSE`/`STOFTALMO`/`STMIDRIASE`/`STFACIAL`/`STBULBAR` | Inteiro | Sinais de envolvimento de nervos cranianos: ptose, oftalmoparesia, midriase, paralisia facial, bulbar |
| `STMEMINF`/`STMEMSUP`/`STDESCENDE`/`STSIMETRIC`/`STSENSIVEL` | Inteiro | Paralisia em membros inferiores/superiores, forma descendente, simetria e sensibilidade |
| `TPNEURO` | Inteiro | Reflexos neurológicos: 1 - Normais, 2 - Aumentados, 3 - Reduzidos/Ausentes, 9 - Ignorado |
| `STALIMENTO` / `DSALIMENTO` | Inteiro/String | Suspeita de transmissão alimentar (1 - Sim) e descrição do alimento |
| `TPBOTULISM` | Inteiro | Forma de botulismo: 1 - Alimentar, 2 - Intestinal, 3 - Por ferimento, 4 - Outra |
| `STCASEIRA` / `STCOMERCIO` / `STEXPALIM` / `DS_INDUS` | Inteiro/String | Natureza do alimento: doméstico caseiro, comercial, exportação e descrição do industrializado |
| `STDOMICILI` / `STESCOLA` / `STTRABALHO` / `STRESTAURA` / `STFESTA` / `STOUTROLOC` | Inteiro | Local de ocorrência da ingestão: domicílio, escola, trabalho, restaurante, festa, outro |
| `NUCONSOME` | Inteiro | Número de pessoas que consumiram o alimento |
| `STSORO` / `STANTIBIO` / `STOUTROTRA` / `STVENTILA` | Inteiro | Tratamento: soro antibotulínico, antibiótico, outro tratamento, ventilação mecânica |
| `DTSORO` / `STANTIBOTU` | Data/Inteiro | Data de aplicação do soro antitoxina e aplicação |
| `STSOROMAT` / `DTSOROCOL` / `STSORORES` / `TPSOROTOX` | Inteiro/Data | Soro coletado: data, resultado da pesquisa de toxina e tipo de toxina (A-G, 7 - Outra, 9 - Ignorado) |
| `STFEZESMAT` / `DTFEZESCOL` / `STFEZESRES` / `TPFEZESTOX` | Inteiro/Data | Fezes coletadas: data, resultado da pesquisa de toxina e tipo de toxina |
| `ST_ALI1COL` / `DS_ALI1OUT` / `DT_ALI1COL` / `RESALIM1` / `TP_ALI1TOX` | Inteiro/Data/String | Alimento 1 coletado: descrição, data, resultado e tipo de toxina identificada |
| `ST_ALI2COL` / `DS_ALI2OUT` / `DT_ALI2COL` / `ST_ALI2RES` / `TP_ALI2TO` | Inteiro/Data/String | Alimento 2 coletado: descrição, data, resultado e tipo de toxina identificada |
| `STELETRO` / `DTELETRO` | Inteiro/Data | Eletromiografia realizada e data |
| `TP_LIQUOR` / `NU_CELULA` / `NU_PROTEI` / `DT_LIQUOR` | Inteiro/Data | Exame de liquor: resultado, células, proteínas e data |
| `CLASSI_FIN` | Inteiro | Classificação final do caso: 1 - Confirmado, 2 - Descartado (especificar outro agente) |
| `AGENTE_OUT` | String | Outro agente identificado quando o caso é descartado |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte: 1 - Laboratorial, 2 - Clínico-epidemiológico |
| `TPCLINICA` / `TPBROMATO` / `DSCAUSALIM` | Inteiro/String | Avaliação clínica e bromatológica e descrição da causa/alimento |
| `TP_MOTORA` / `TP_REPETE` / `TP_SENSITI` | Inteiro | Aspectos clínicos: padrão motor, repetição e sensibilidade |
| `DOENCA_TRA` | Inteiro | Doença relacionada ao trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `EVOLUCAO` | Inteiro | Evolução do caso: 1 - Cura, 2 - Óbito por botulismo, 3 - Óbito por outras causas, 9 - Ignorado |
| `DT_OBITO` / `DT_ENCERRA` / `DT_DIGITA` | Data (`AAAAMMDD`) | Data do óbito, de encerramento e de digitação |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

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
| `dt_nasc` | `DT_NASC` | data | Data de nascimento. Data de nascimento do paciente | — | 2007 a 2013 |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil) | — | todos |
| `dt_invest` | `DT_INVEST` | data | Data da Investigação. Data em que ocorreu a investigação – informar a Data da 1ª visita ao paciente | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo de atividade econômica | — | todos |
| `dtatend` | `DTATEND` | data | Data do 1º atendimento. Data do 1º atendimento médico do paciente em posto de saúde, unidade de saúde ou hospital | — | todos |
| `nuatend` | `NUATEND` | inteiro | Nº total de atendimentos até a suspeição clínica. number(4,0) | — | todos |
| `dtsuspeic` | `DTSUSPEIC` | data | Data da suspeição clínica. Informar a data da suspeita clínica | — | todos |
| `sthospital` | `STHOSPITAL` | texto | Ocorreu Hospitalização. Informar se o paciente foi internado | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `dtinterna` | `DTINTERNA` | data | Data da Internação | — | todos |
| `dtalta` | `DTALTA` | data | Data da alta hospitalar. Data em que o paciente teve alta hospitalar e retornou ao domicílio | — | todos |
| `stfebre` | `STFEBRE` | texto | Sinais e sintomas Febre. Informar se o paciente apresentou Febre | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stnausea` | `STNAUSEA` | texto | Sinais e sintomas Náusea. Informar se o paciente apresentou Náusea | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stvomito` | `STVOMITO` | texto | Sinais e sintomas Vômito. Informar se o paciente apresentou Vômito | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stdiarreia` | `STDIARREIA` | texto | Sinais e sintomas Diarréia. Informar se o paciente apresentou Diarréia | 1 – Sim 2 – Não | todos |
| `stconstipa` | `STCONSTIPA` | texto | Sinais e sintomas Constipação. Informar se o paciente apresentou Constipação | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stcefaleia` | `STCEFALEIA` | texto | Sinais e sintomas Cefaléia. Informar se o paciente apresentou Cefaléia | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `sttontura` | `STTONTURA` | texto | Sinais e sintomas Tontura. Informar se o paciente apresentou Tontura | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stvisao` | `STVISAO` | texto | Sinais e sintomas Visão turva. Informar se o paciente apresentou Visão turva | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stdiplopia` | `STDIPLOPIA` | texto | Sinais e sintomas Diplopia. Informar se o paciente apresentou Diplopia (visão dupla) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stdisartri` | `STDISARTRI` | texto | Sinais e sintomas Disartria. Informar se o paciente apresentou Disartria (dificuldade para falar) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stdisfonia` | `STDISFONIA` | texto | Sinais e sintomas Disfonia. Informar se o paciente apresentou Disfonia (alteração da voz) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stdisfagia` | `STDISFAGIA` | texto | Sinais e sintomas Disfagia. Informar se o paciente apresentou Disfagia (dificuldade para engolir) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stboca` | `STBOCA` | texto | Sinais e sintomas Boca seca. Informar se o paciente apresentou Boca seca | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stferiment` | `STFERIMENT` | texto | Sinais e sintomas Ferimento. Informar se o paciente apresenta algum Ferimento aberto ou em cicatrização | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stflacidez` | `STFLACIDEZ` | texto | Sinais e sintomas Flacidez de pescoço. Informar se o paciente apresentou Flacidez de pescoço | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stdispneia` | `STDISPNEIA` | texto | Sinais e sintomas Dispnéia. Informar se o paciente apresentou Dispnéia | 1 – Sim 2 – Não | todos |
| `strespira` | `STRESPIRA` | texto | Sinais e sintomas Insuficiência respiratória. Informar se o paciente apresentou Insuficiência respiratória | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stcardiaca` | `STCARDIACA` | texto | Sinais e sintomas Insuficiência cardíaca. Informar se o paciente apresentou Insuficiência cardíaca | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stcoma` | `STCOMA` | texto | Sinais e sintomas Coma. Informar se o paciente entrou em Coma | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stparestes` | `STPARESTES` | texto | Sinais e sintomas Parestesia. Informar se o paciente apresentou Parestesia e o local do corpo | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stoutrosin` | `STOUTROSIN` | texto | Sinais e sintomas Outros. Informar se o paciente apresentou outro(s) sinal(is) e sintoma(s) e descrever qual(is) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stptose` | `STPTOSE` | texto | Exame Neurológico Ptose Palpebral. Informar se o exame neurológico apresentou Ptose palpebral | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stoftalmo` | `STOFTALMO` | texto | Exame Neurológico Oftalmoparesia / Oftalmoplegia. Informar se o exame neurológico apresentou Oftalmoparesia / Oftalmoplegia | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stmidriase` | `STMIDRIASE` | texto | Exame Neurológico Midríase. Informar se o exame neurológico apresentou Midríase | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stfacial` | `STFACIAL` | texto | Exame Neurológico. Informar se o exame | 1 – Sim | todos |
| `stbulbar` | `STBULBAR` | texto | Exame Neurológico Comprometimento da Musculatura Bulbar. Informar se o exame neurológico apresentou Comprometimento da Musculatura Bulbar | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stmeminf` | `STMEMINF` | texto | Exame Neurológico Fraqueza em Membros Inferiores. Informar se o exame neurológico apresentou Fraqueza em Membros Inferiores | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stmemsup` | `STMEMSUP` | texto | Exame Neurológico Fraqueza em Membros Superiores. Informar se o exame neurológico apresentou Fraqueza em Membros Superiores | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stdescende` | `STDESCENDE` | texto | Exame Neurológico Fraqueza Descendente. Informar se o exame neurológico apresentou Fraqueza Descendente | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stsimetric` | `STSIMETRIC` | texto | Exame Neurológico Fraqueza Simétrica. Informar se o exame neurológico apresentou Fraqueza Simétrica | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stsensivel` | `STSENSIVEL` | texto | Exame Neurológico Alterações de Sensibilidade. Informar se o exame neurológico apresentou Alterações de Sensibilidade | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `tpneuro` | `TPNEURO` | texto | Reflexos Neurológicos. Informar os reflexos neurológicos do paciente | 1 – Normais 2 – Aumentados 3 – Reduzidos/ Ausentes 9 – Ignorado | todos |
| `stalimento` | `STALIMENTO` | texto | Suspeita de transmissão alimentar?. Informar se o caso de botulismo é de suspeita de origem alimentar | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `dsalimento` | `DSALIMENTO` | texto | Se sim, qual alimento suspeito. Se o caso for de origem alimentar, informar qual foi o alimento suspeito | — | todos |
| `stcaseira` | `STCASEIRA` | texto | Produção do alimento suspeito Caseira. Informar se o alimento é produzido de forma artesanal | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stcomercio` | `STCOMERCIO` | texto | Produção do alimento suspeito Industrial/ Comercial. Informar se o alimento suspeito é comercializado e/ou produzido em indústria alimentícia | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stexpalim` | `STEXPALIM` | texto | Exposição ao alimento. Informar se o paciente ingeriu o alimento suspeito somente uma vez (exposição única) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stdomicili` | `STDOMICILI` | texto | Local da ingestão Domicílio. Informar se o local da ingestão do alimento suspeito foi no domicílio do paciente | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stescola` | `STESCOLA` | texto | Local da ingestão Creche/ escola. Informar se o local da ingestão do alimento suspeito foi em creche ou escola | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `sttrabalho` | `STTRABALHO` | texto | Local da ingestão Trabalho. Informar se o local da ingestão do alimento suspeito foi no trabalho | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `strestaura` | `STRESTAURA` | texto | Local da ingestão Restaurante/ Bar/ Lanchonete. Informar se o local da ingestão do alimento suspeito foi em restaurante, bar e/ou lanchonete | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stfesta` | `STFESTA` | texto | Local da ingestão Festa. Informar se o local da ingestão do alimento suspeito foi em uma festa | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stoutroloc` | `STOUTROLOC` | texto | Local da ingestão Outro. Caso a ingestão do alimento suspeito não se enquadre em nenhuma das alternativas anteriores, marcar “Outro” | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `nuconsome` | `NUCONSOME` | inteiro | Número de pessoas (comensais) que consumiram o alimento suspeito. Informar o número de pessoas que ingeriu o alimento suspeito de ter causado botulismo | — | todos |
| `stsoro` | `STSORO` | texto | Tratamento Soro antibotulínico. Informar se o paciente foi tratado com soro antibotulínico | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stantibio` | `STANTIBIO` | texto | Tratamento Antibioticoterapia. Informar se o paciente foi tratado com antibiótico | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stoutrotra` | `STOUTROTRA` | texto | Tratamento outros. Informar se o paciente necessitou fazer outro tipo de tratamento | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `dtsoro` | `DTSORO` | data | Se recebeu soro antibotulínico, data da administração. Caso o paciente tenha sido tratado com soro antibotulínico, informar a data da administração | — | todos |
| `stantibotu` | `STANTIBOTU` | texto | Se recebeu soro antibotulínico, foi após a coleta do material clínico ?. Caso o paciente tenha sido tratado com soro antibotulínico, informar se a administração do soro foi posterior a coleta de material clínico do paciente | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stsoromat` | `STSOROMAT` | texto | Coletou material ? Material coletado Soro. Informar se foi coletado soro do paciente | 1 – Sim 2 – Não | todos |
| `dtsorocol` | `DTSOROCOL` | data | Data da coleta Soro. Informar a data da coleta do soro do paciente | — | todos |
| `stfezesmat` | `STFEZESMAT` | texto | Coletou Material ? Material coletado Fezes. Informar se foi coletado fezes do paciente | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `dtfezescol` | `DTFEZESCOL` | data | Data da coleta Fezes. Informar a data da coleta das fezes do paciente | — | todos |
| `steletro` | `STELETRO` | texto | Exames complementares Eletroneuromiografia. Informar se houve exame complementar Eletroneuromiografia | 1 – Realizado 2 – Não Realizado | todos |
| `dteletro` | `DTELETRO` | data | Exames complementares Data da realização. Informar a data do exame complementar Eletroneuromiografia | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final. Informar se o caso foi confirmado ou descartado | 1- Confirmado 2- Descartado (especificar outro agente) | todos |
| `agente_out` | `AGENTE_OUT` | texto | Se descartado, (especificar outro agente). Especificar outro agente se descartado | — | todos |
| `criterio` | `CRITERIO` | texto | Critério de confirmação/ descarte. Informar o critério em que o caso foi confirmado ou | 1- Laboratorial 2- Clínico- | todos |
| `tpbotulism` | `TPBOTULISM` | texto | Forma de botulismo. Em confirmação do caso de botulismo, informar a forma de transmissão do Botulismo | 1- Alimentar 2- Intestinal 3- Por ferimento 4- Outra | todos |
| `stclinica` | `STCLINICA` | texto | Presença de toxina botulínica na amostra - Clínica. Informar se houve isolamento de toxina botulínica na amostra clínica | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `stbromato` | `STBROMATO` | texto | Presença de toxina botulínica na amostra Bromatológica. Informar se houve isolamento de toxina botulínica na amostra bromatológica | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `tpclinica` | `TPCLINICA` | texto | Tipo de toxina isolada na amostra Clínica. Se houver presença de toxina, informar o tipo de toxina botulínica na amostra clínica | 1 – A 2 – B 3 – AB 4 – E 5 – F 6 – G 7 – Outra 9 – Ignorado | todos |
| `tpbromato` | `TPBROMATO` | texto | Tipo de toxina isolada na amostra Bromatológica. Se houver presença de toxina, informar o tipo de toxina botulínica na amostra bromatológica | 1 – A 2 – B 3 – AB 4 – E 5 – F 6 – G 7 – Outra 9 – Ignorado | todos |
| `dscausalim` | `DSCAUSALIM` | texto | Qual a causa/ alimento incriminado/ alimento potencialmente suspeito. Informar a causa do botulismo (ex. ferimento) e/ou especificar o alimento incriminado e/ou alimento potencialmente suspeito | — | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho. Se o paciente adquiriu a doença em decorrência das condições/ situação do trabalho | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do Caso. Informar a evolução do caso | 1 – Cura 2 – Óbito por botulismo 3 – Óbito por outras causas 9 – Ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito. Em caso de óbito, informar a data do óbito | — | todos |
| `stventila` | `STVENTILA` | texto | Tratamento Assistência ventilatória. Informar se o paciente necessitou de assistência ventilatória (ventilação mecânica) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `uf_hosp` | `UF_HOSP` | texto | UF de internação. Informe a sigla da UF onde o paciente foi internado | — | todos |
| `mun_hosp` | `MUN_HOSP` | texto | Município do Hospital. Informe Nome do município onde o paciente foi internado | — | todos |
| `ds_pares` | `DS_PARES` | texto | Sinais e sintomas Parestesia (onde). Informar onde o paciente apresentou Parestesia | — | todos |
| `ds_outrosi` | `DS_OUTROSI` | texto | Sinais e sintomas Outros (especificar). Especificar o outro sinal e sintoma do paciente | — | todos |
| `ds_indus` | `DS_INDUS` | texto | Se Industrial/ Comercial, especificar marca, data. Informar o nome comercial, nome da | — | todos |
| `ds_ingest` | `DS_INGEST` | texto | Se única, tempo decorrido entre ingestão e início dos sintomas. Informar o tempo (em horas) decorrido entre ingestão do alimento suspeito e início dos sintomas Ex.: Hora da ingestão – Hora início dos sintomas | — | todos |
| `ds_ini_ges` | `DS_INI_GES` | texto | Se múltipla, tempo decorrido entre a primeira ingestão e início dos sintomas. Informar o tempo decorrido entre a 1ª ingestão do alimento suspeito e início dos sintomas Ex.: Hora da 1ª ingestão – Hora início dos sintomas | — | todos |
| `ds_fim_ges` | `DS_FIM_GES` | texto | Se múltipla, tempo decorrido entre a última ingestão e início dos sintomas. Informar o tempo decorrido entre a última ingestão do alimento suspeito e início dos sintomas Ex.: Hora da última ingestão – Hora início dos sintomas | — | todos |
| `ds_outr_lo` | `DS_OUTR_LO` | texto | Local da ingestão Se outro, especificar. Especificar o local da ingestão do alimento suspeito | — | todos |
| `uf_ing` | `UF_ING` | texto | UF. Unidade Federada da ingestão do alimento suspeito | — | todos |
| `mun_ing` | `MUN_ING` | texto | Município onde ingeriu o alimento suspeito. Município da ingestão do alimento suspeito e código do IBGE | — | todos |
| `ds_trat` | `DS_TRAT` | texto | Tratamento Se outros, especificar. Descrever outro tipo de tratamento feito no paciente (ex. traqueostomia) | — | todos |
| `stsorores` | `STSORORES` | texto | Resultado Soro. Informar o resultado da análise do soro do paciente | 1- Presença de toxina 2- Ausência de toxina 3- Inconclusivo 4- Não realizado | todos |
| `tpsorotox` | `TPSOROTOX` | texto | Tipo de Toxina Soro. Se houver presença de toxina no soro, informar o tipo de toxina botulínica | 1- A 2- B 3- AB 4- E 5- F 6- G 7- Outra 9- Ign | todos |
| `stfezesres` | `STFEZESRES` | texto | Resultado Fezes. Informar o resultado da análise das fezes do paciente | 1- Presença de toxina 2- Ausência de toxina 3- Inconclusivo 4- Não realizado | todos |
| `tpfezestox` | `TPFEZESTOX` | texto | Tipo de Toxina Fezes. Se houver presença de toxina nas fezes, informar o tipo de toxina botulínica | 1- A 2- B 3- AB 4- E 5- F 6- G 7- Outra 9- Ign | todos |
| `st_ali1col` | `ST_ALI1COL` | texto | Coletou Material ? Alimento 1. Informar se foi coletado alimento suspeito 1 para análise | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ds_ali1out` | `DS_ALI1OUT` | texto | Material coletado Especificar Alimento 1. Especificar alimento suspeito 1 encaminhado para análise | — | todos |
| `dt_ali1col` | `DT_ALI1COL` | data | Data da coleta Alimento 1. Informar a data da coleta do alimento 1 | — | todos |
| `resalim1` | `RESALIM1` | texto | Resultado Alimento 1. Informar o resultado da análise do alimento 1 | 1- Presença de toxina 2- Ausência de toxina 3- Inconclusivo 4- Não realizado | todos |
| `tp_ali1tox` | `TP_ALI1TOX` | texto | Tipo de Toxina Alimento 1. Se houver presença de toxina no alimento 1, informar o tipo de toxina botulínica | 1- A 2- B 3- AB 4- E 5- F 6- G 7- Outra 9- Ign | todos |
| `st_ali2col` | `ST_ALI2COL` | texto | Coletou Material? Alimento 2. Informar se foi coletado alimento suspeito 2 para análise | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ds_ali2out` | `DS_ALI2OUT` | texto | Material coletado Especificar Alimento 2. Especificar alimento suspeito 2 encaminhado para análise | — | todos |
| `dt_ali2col` | `DT_ALI2COL` | data | Data da coleta Alimento 2. Informar a data da coleta do alimento 2 | — | todos |
| `st_ali2res` | `ST_ALI2RES` | texto | Situação do alimento (campo do surto de doenças transmitidas por alimentos) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tp_ali2to` | `TP_ALI2TO` | texto | Tipo de Toxina Alimento 2. Se houver presença de toxina no alimento 2, informar o tipo de toxina botulínica | 1- A 2- B 3- AB 4- E 5- F 6- G 7- Outra 9- Ign | todos |
| `tp_colout` | `TP_COLOUT` | texto | Coletou Material ? Outros. Informar e especificar se houve coleta de outro alimento ou material clínico para pesquisa de toxina botulínica ou presença de esporos de Clostridium botulinum (ex. lavado intestinal, lavado gástrico, vísceras, tecido de feridas) | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `ds_outro` | `DS_OUTRO` | texto | Material coletado Outros especificar. Especificar o material coletado | — | todos |
| `dt_colout` | `DT_COLOUT` | data | Data da coleta Outro. Informar a data da coleta deste outro material coletado | — | todos |
| `resalimout` | `RESALIMOUT` | texto | Resultado Outro. Informar o resultado da análise do outro material | 1- Presença de toxina | todos |
| `tp_toxoutr` | `TP_TOXOUTR` | texto | Tipo de Toxina Outro. Se houver presença de toxina, informar o tipo de toxina botulínica | 1- A 2- B 3- AB 4- E 5- F 6- G 7- Outra 9- Ign | todos |
| `tp_liquor` | `TP_LIQUOR` | texto | Exames complementares Líquor. Informar se líquor foi coletado | 1 – Realizado 2 – Não Realizado | todos |
| `nu_celula` | `NU_CELULA` | texto | Exames complementares número de células/mm3. Informar o número de células/ mm3 | — | todos |
| `nu_protei` | `NU_PROTEI` | texto | Exames complementares Proteínas mg%. Informar o número de Proteínas mg% | — | todos |
| `dt_liquor` | `DT_LIQUOR` | data | Exames complementares Data da Coleta. Informar a data da coleta do líquor | — | todos |
| `tp_sensiti` | `TP_SENSITI` | texto | Neurocondução Sensitiva. Informar resultado da Neurocondução Sensitiva | 1 – Normal 2 – Diminuição de amplitude 3 – Lentificações | todos |
| `tp_motora` | `TP_MOTORA` | texto | Neurocondução Motora. Informar resultado da Neurocondução Motora | 1 – Normal 2 – Diminuição de amplitude 3 – Lentificações | todos |
| `tp_repete` | `TP_REPETE` | texto | Estimulação repetitiva. Informar resultado da Estimulação repetitiva | 1 – Normal 2 – Decremento (freq baixa) 3 – Incremento (freq alta) | todos |
| `ds_ali1` | `DS_ALI1` | texto | Informações complementares e observações Tipo de alimento 1. Descrever alimentos potencialmente suspeitos para botulismo, ingeridos nos últimos 10 dias anteriores do início dos sintomas Tipo de alimento 1 | — | todos |
| `ds_ali2` | `DS_ALI2` | texto | Informações Complementares e observações Tipo de alimento 2. Descrever alimentos potencialmente suspeitos para botulismo, ingeridos nos últimos 10 dias | — | todos |
| `ds_local1` | `DS_LOCAL1` | texto | Informações Complementares e observações Local de consumo 1. Descrever alimentos potencialmente suspeitos para botulismo, ingeridos nos últimos 10 dias anteriores do início dos sintomas Local de consumo 1 | — | todos |
| `ds_local2` | `DS_LOCAL2` | texto | Informações Complementares e observações Local de consumo 2. Descrever alimentos potencialmente suspeitos para botulismo, ingeridos nos últimos 10 dias anteriores do início dos sintomas Local de consumo 2 | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Informar a data de encerramento da investigação do caso. Lembrar que é necessário o acompanhamento do paciente até ele receber alta médica | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2017 a 2026 |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | 2017 a 2026 |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | 2017 a 2026 |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | 2017 a 2026 |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | 2017 a 2026 |
| `dt_trnasrm` | `DT_TRNASRM` | data | Data de transmissão do registro (nome gravado com erro de grafia na fonte) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2017 a 2026 |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | 2017 a 2026 |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | 2017 a 2026 |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | 2017 a 2026 |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | 2017 a 2026 |

## No lake

- **Dataset no lake:** `datasus/sinan-botu`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 25, inteiro: 3, nulo (vazio nas amostras): 8, texto: 124.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-botu.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- base de casuística rara (dezenas de casos por ano) — qualquer validação de agregação é sensível a erros: atenção com `CLASSI_FIN` (descartado exige especificar outro agente em `AGENTE_OUT`); a forma alimentar exige o bloco do alimento suspeito (`STALIMENTO`/`DSALIMENTO`, natureza caseira/comercial `STCASEIRA`, local de ingestão `STDOMICILI`) e as amostras bromatológicas (`ST_ALI1COL`...); `TPSOROTOX`/`TPFEZESTOX` devem ser tratados como código do tipo de toxina (A–G/Outra) e não como caso confirmado; e o campo `NU_LOTE_V` (lote do soro antibotulínico do PNI) e a natureza do alimento implicado (caseiro vs comercial `STCASEIRA`/`STCOMERCIO`) são fundamentais para estudos de botulismo alimentar. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 11 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-botu").glob("**/*.parquet"))
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
datasus-fetcher list sinan-botu

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-botu -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-botu
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Botulismo (ficha e dicionário de dados v5.0, rev. julho/2010)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de Botulismo (epidemiologia e vigilância de conservas caseiras)
