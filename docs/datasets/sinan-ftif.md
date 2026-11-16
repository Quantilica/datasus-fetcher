---
dataset:
  id: sinan-ftif
  fonte: datasus
  titulo: Febre Tifoide
  resumo: 'Febre Tifoide do DATASUS: uma ficha de notificação/investigação de febre Tifoide.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de febre Tifoide
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 132
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    pa_des1: 'número inteiro: contagem ou código numérico (ver Descrição)'
    pa_des2: 'número inteiro: contagem ou código numérico (ver Descrição)'
    pa_des3: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Febre Tifoide (`sinan-ftif`)

## Resumo

O `sinan-ftif` contém os microdados das notificações e investigações epidemiológicas de casos de Febre Tifoide (CID-10 A01.0) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de febre tifoide, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. Base de incidência moderada e focada na investigação de transmissão fecal-oral (água/alimentos), com o leiaute da ficha v5.0 (131 colunas): quadro clínico (febre, cefaléia, constipação/diarreia, esplenomegalia), complicações graves (perfuração intestinal e toxemia), o extenso bloco de hemoculturas/uroculturas/coproculturas (3 exames por material) e o tratamento antimicrobiano registrado por classe de antibiótico.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `FTIF` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `FTIF` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `FTIFBR25.dbc` — `FTIF` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As consolidações até 2024 estão em `FINAIS` e os anos de 2025 e 2026 estão apenas em `PRELIM` (ex.: `FTIFBR26.dbc`, atualização de 02/06/2026).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-ftif/<AAAA>/sinan-ftif_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-ftif/2024/sinan-ftif_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

A febre tifoide é agravo de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, constando hoje da Lista Nacional de Agravos de Notificação Compulsória (Portaria GM/MS nº 204/2016). A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), com suporte da rede de laboratórios para o diagnóstico de *Salmonella enterica* sorotipo Typhi e o registro de portadores — a transmissão fecal-oral por água e alimentos aproxima o agravo da vigilância de surtos de Doenças Transmitidas por Alimentos (DTA) e da vigilância do saneamento básico. A base alimenta a vigilância de casos isolados e surtos regionais, o monitoramento da resistência antimicrobiana e a identificação de portadores crônicos.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Febre Tifoide** do SINAN. A notificação nasce com a suspeição clínica (febre prolongada, cefaléia, astenia, constipação/diarreia, tosse, esplenomegalia) e é completada ao longo da investigação com sinais de complicações graves (perfuração intestinal, hemorragia digestiva e toxemia), com o resultado de exames microbiológicos (hemocultura, urocultura, coprocultura e culturas de outros materiais, com data e resultado por material e repetição: `HEMO_R1..3`, `URO_R1..3`, `COPRO_R1..3`, `OUTR_R1..3`) e o tratamento por classes de antibióticos (clorafenicol, ampicilina, sulfa/SMT+TMP, quinolonas e outros, com duração em dias). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. Revisões do dicionário datam de julho/2010 e disciplinaram a leitura de "classicalite final" por caso. Em versões posteriores (categoria de casos de resultado `CLASSI_FIN` não pode ser descartada se qualquer resultado laboratório anexado for *S. typhi*) e a leitura do critério por material (`HEMO/URO/COPRO/OUTR`).

Aplicações analíticas típicas: percentual de casos confirmados com culturas positivas por material (hemocultura, urocultura, coprocultura); frequência de complicações graves (`PERFURA`); investigação de contatos (`CONTATO`, `SUGE_VINCU`/`VINC_OUT`) e fontes prováveis de água/alimentos; percentual de casos com uso de cada classe de antibiótico e duração média do tratamento (`DIAS`); letalidade por ano e região.

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-06-02.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `FTIFBR23.dbc` (131 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `CONTATO` | Inteiro | Contato com caso parecido de febre tifoide (1 - Sim, 2 - Não) |
| `CONT_OUT` / `SUGE_VINCU` / `VINC_OUT` | Inteiro/String | Detalhe do contato sugerido como vínculo epidemiológico e descrição |
| `ASSINTOMAT` | Inteiro | Caso assintomático (portador) |
| `FEBRE`/`CEFALEIA`/`DIARREIA`/`CONSTIPA`/`ASTENIA`/`TOSSE`/`ESPLENO`/`TIFICA`/`NAUSEAS`/`VOMITOS`/`DOR` | Inteiro | Sinais e sintomas: febre, cefaléia, diarreia, constipação, astenia, tosse, esplenomegalia, "manchas tíficas" (roséolas), náuseas, vômitos e dor abdominal |
| `ENTERO` | Inteiro | Quadro de toxemia/estado entérico grave |
| `PERFURA` | Inteiro | Perfuração intestinal (complicação grave) |
| `COMP_OUT` / `COMP_OUT_D` | Inteiro/String | Outras complicações e sua descrição |
| `ATENDIMENT` / `DT_ATENDE` / `UF` / `MUNICIPIO` | Inteiro/Data/String | Atendimento, data e local (UF/município) |
| `SANGUE`/`FEZES`/`URINA`/`ANTIBIOTIC` | Inteiro | Materiais coletados para exame (sangue, fezes, urina) e uso prévio de antibiótico (interferência no cultivo) |
| `DT_HEMO1`/`HEMO_R1`/`HEMO_D_1` a `DT_HEMO3`/`HEMO_R3`/`HEMO_D_3` | Data/Inteiro | Hemoculturas (1 a 3): data da coleta, resultado e diagnóstico (positivo para *S. typhi*) |
| `DT_URO`/`URO_R1` a `DT_URO3`/`URO_R3` | Data/Inteiro | Uroculturas: data, resultado e diagnóstico |
| `DT_COPRO1`/`COPRO_R1` a `DT_COPRO3`/`COPRO_R3` | Data/Inteiro | Coproculturas: data, resultado e diagnóstico (investigação de portadores) |
| `DT_OUTR1`/`OUTR_R1` a `DT_OUTR3`/`OUTR_R3` | Data/Inteiro | Outros materiais exames: data, resultado e diagnóstico |
| `CLORAFEN`/`AMPICILINA`/`SULFA`/`QUINOLONA` | Inteiro | Antibióticos utilizados no tratamento (1 - Sim, 2 - Não, 9 - Ignorado) |
| `ANT_OUTR` / `ANT_OUT_D` | Inteiro/String | Outros antibióticos e descrição |
| `DIAS` | Inteiro | Duração do tratamento antimicrobiano (dias) |
| `CLASSI_FIN` | Inteiro | Classificação final do caso: 1 - Confirmado, 2 - Descartado |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte (laboratorial, clínico-epidemiológico) |
| `DOENCA_TRA` | Inteiro | Doença relacionada ao trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito por febre tifoide, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` / `DT_ENCERRA` | Data (`AAAAMMDD`) | Data do óbito e de encerramento do caso |

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
| `dt_invest` | `DT_INVEST` | data | Data da Investigação. dt_investigaçao | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/ Ramo de atividade. o | — | todos |
| `contato` | `CONTATO` | texto | Contato compatível com caso de febre tifóide (até 45 dias antes do início dos sinais e sintomas).. _febre | 1. Domicílio 2. Vizinhança 3. Trabalho 4. Creche/escola 5. Posto de saúde/hospita l 6. Outro Estado/Municí pio 7. Outros 8. Sem história de contato 9. Ignorado | todos |
| `cont_out` | `CONT_OUT` | texto | Contato compatível com caso de febre tifóide (até 45 dias antes do início dos sinais e sintomas). Se Outros especificar. _febre_outro | — | todos |
| `suge_vincu` | `SUGE_VINCU` | texto | Sugestão de vínculo com. Identificar fontes de infecção mais comuns | 1. Consumo de água não tratada 2. Exposição à esgoto 3. Alimento suspeito 4. Deslocamento 5.Outros 9. Ignorado | todos |
| `vinc_out` | `VINC_OUT` | texto | Se outros, especificar | — | todos |
| `assintomat` | `ASSINTOMAT` | texto | Sinais e sintomas Assintomático | 1. Sim 2. Não 9. Ignorado | todos |
| `febre` | `FEBRE` | texto | Sinais e sintomas Febre. O paciente teve febre | 1. Sim 2. Não 9. Ignorado | todos |
| `cefaleia` | `CEFALEIA` | texto | Sinais e sintomas Cefaléia. a | 1. Sim 2. Não 9. Ignorado | todos |
| `diarreia` | `DIARREIA` | texto | Sinais e sintomas Diarréia. a | 1. Sim 2. Não 9. Ignorado | todos |
| `constipa` | `CONSTIPA` | texto | Sinais e sintomas Constipação | 1. Sim 2. Não 9. Ignorado | todos |
| `astenia` | `ASTENIA` | texto | Sinais e sintomas Astenia. O paciente apresentou astenia | 1. Sim 2. Não 9. Ignorado | todos |
| `tosse` | `TOSSE` | texto | Sinais e sintomas Tosse. O paciente teve tosse | 1. Sim 2. Não 9. Ignorado | todos |
| `espleno` | `ESPLENO` | texto | Sinais e sintomas Esplenomegalia | 1. Sim 2. Não 9. Ignorado | todos |
| `tifica` | `TIFICA` | texto | Sinais e sintomas Roséola tífica. a_tifica | 1. Sim 2. Não 9. Ignorado | todos |
| `nauseas` | `NAUSEAS` | texto | Sinais e sintomas Náuseas. a | 1. Sim 2. Não 9. Ignorado | todos |
| `vomitos` | `VOMITOS` | texto | Sinais e sintomas Vômitos. O paciente apresentou vômitos | 1. Sim 2. Não | todos |
| `dor` | `DOR` | texto | Sinais e sintomas Dor abdominal | 1. Sim 2. Não 9. Ignorado | todos |
| `pulso` | `PULSO` | texto | Sinais e sintomas Dissociação pulso/temperatura | 1. Sim 2. Não 9. Ignorado | todos |
| `entero` | `ENTERO` | texto | Complicações Enterorragia | 1. Sim 2. Não 9. Ignorado | todos |
| `perfura` | `PERFURA` | texto | Complicações Perfurações intestinais | 1. Sim 2. Não 9. Ignorado | todos |
| `comp_out` | `COMP_OUT` | texto | Complicações Outras | 1. Sim 2. Não 9. Ignorado | todos |
| `comp_out_d` | `COMP_OUT_D` | texto | Complicações Se Outras, especificar. _outro | — | todos |
| `atendiment` | `ATENDIMENT` | texto | Tipo de atendimento. Tipo de atendimento recebido pelo paciente em decorrência da suspeita de febre tifóide | 1. Hospitalar 2. Ambulatorial 3. Domiciliar 4. Nenhum 9. Ignorado | todos |
| `dt_atende` | `DT_ATENDE` | data | Data do atendimento | — | todos |
| `uf_hospital` | `UF` | texto | UF do hospital de internação (coluna `UF` da fonte, renomeada pelo conversor porque `uf` é coluna do lake) | — | todos |
| `municipio` | `MUNICIPIO` | texto | Município do hospital | — | todos |
| `sangue` | `SANGUE` | texto | Material coletado Sangue. ado_sangue | 1. Sim 2. Não 9. Ignorado | todos |
| `fezes` | `FEZES` | texto | Material coletado Fezes. ado_fezes | 1. Sim 2. Não 9. Ignorado | todos |
| `urina` | `URINA` | texto | Material coletado Urina. ado_medular | 1. Sim 2. Não 9. Ignorado | todos |
| `antibiotic` | `ANTIBIOTIC` | texto | Uso de antibiótico antes da coleta do material. o | 1. Sim 2. Não | todos |
| `dt_hemo1` | `DT_HEMO1` | data | Hemocultura Data da 1ª Coleta. coleta_1 | — | todos |
| `hemo_r1` | `HEMO_R1` | texto | Hemocultura Resultado da 1° coleta. resultado_1 | 1. Salmonella typhi 2. Salmonella SPP 3. Negativo 4. Outro agente | todos |
| `hemo_d_1` | `HEMO_D_1` | texto | Hemocultura Resultado da 1° coleta Especificar. resultado_1 | — | todos |
| `dt_hemo2` | `DT_HEMO2` | data | Hemocultura Data da 2ª Coleta. coleta_2 | — | todos |
| `hemo_r2` | `HEMO_R2` | texto | Hemocultura Resultado da 2° coleta. resultado_2 | 1. Salmonella typhi 2. Salmonella SPP 3. Negativo 4. Outro agente | todos |
| `hemo_d_2` | `HEMO_D_2` | texto | Hemocultura Resultado da 2° coleta Especificar. resultado_2 | — | todos |
| `dt_hemo3` | `DT_HEMO3` | data | Hemocultura Data da 3ª Coleta. coleta_3 | — | todos |
| `hemo_r3` | `HEMO_R3` | texto | Hemocultura Resultado da 3° coleta. resultado_3 | 1. Salmonella typhi 2. Salmonella SPP 3. Negativo 4. Outro agente | todos |
| `hemo_d_3` | `HEMO_D_3` | texto | Hemocultura Resultado da 3° coleta Especificar. resultado_3 | — | todos |
| `dt_uro` | `DT_URO` | data | Urocultura Data da 1ª Coleta. coleta_1 | — | todos |
| `uro_r1` | `URO_R1` | texto | Urocultura Resultado da 1°coleta. esultado_1 | 1. Salmonella typhi 2. Salmonella SPP 3. Negativo 4. Outro agente | todos |
| `uro_d` | `URO_D` | texto | Urocultura Resultado da 1°coleta Especificar. Ds_mielocultura _resultado_1 | — | todos |
| `dt_uro2` | `DT_URO2` | data | Urocultura Data da 2ª Coleta. Dt_mielocultura _coleta_2 | — | todos |
| `uro_r2` | `URO_R2` | texto | Urocultura Resultado da 2° coleta. tp_ mielocultura_res ultado_2 | 1. Salmonella typhi 2. Salmonella SPP 3. Negativo 4. Outro agente | todos |
| `uro_d_2` | `URO_D_2` | texto | Urocultura Resultado da 2° coleta Especificar. ds_ mielocultura_res ultado_2 | — | todos |
| `dt_uro3` | `DT_URO3` | data | Urocultura Data da 3ª Coleta. _coleta_3 | — | todos |
| `uro_r3` | `URO_R3` | texto | Urocultura Resultado da 3° coleta. tp_ mielocultura_res ultado_3 | 1. Salmonella typhi 2. Salmonella SPP 3. Negativo 4. Outro agente | todos |
| `uro_d_3` | `URO_D_3` | texto | Urocultura Resultado da 3° coleta Especificar. resultado_3 | — | todos |
| `dt_copro1` | `DT_COPRO1` | data | Coprocultura data da 1° coleta. coleta_1 | — | todos |
| `copro_r1` | `COPRO_R1` | texto | Coprocultura Resultado da 1° coleta. resultado_1 | 1. Salmonella typhi 2. Salmonella SPP 3. Negativo 4. Outro agente | todos |
| `copro_d_1` | `COPRO_D_1` | texto | Coprocultura Resultado da 1° coleta Especificar. resultado_1 | — | todos |
| `dt_copro2` | `DT_COPRO2` | data | Coprocultura data da 2° coleta. coleta_2 | — | todos |
| `copro_r2` | `COPRO_R2` | texto | Coprocultura Resultado da 2° coleta. resultado_2 | 1. Salmonella typhi 2. Salmonella SPP 3. Negativo 4. Outro agente | todos |
| `copro_d_2` | `COPRO_D_2` | texto | Coprocultura Resultado da 2° coleta Especificar. resultado_2 | — | todos |
| `dt_copro3` | `DT_COPRO3` | data | Coprocultura Data da 3ª Coleta. coleta_3 | — | todos |
| `copro_r3` | `COPRO_R3` | texto | Coprocultura Resultado da 3° coleta. resultado_3 | 1. Salmonella typhi 2. Salmonella SPP 3. Negativo 4. Outro agente | todos |
| `copro_d_3` | `COPRO_D_3` | texto | Coprocultura Resultado da 3° coleta Especificar. resultado_3 | — | todos |
| `dt_outr1` | `DT_OUTR1` | data | Outro exame Data da 1ª Coleta. 1 | — | todos |
| `outr_r1` | `OUTR_R1` | texto | Outro exame Resultado. do_1 | 1. Salmonella typhi 2. Salmonella SPP 3. Negativo 4. Outro agente | todos |
| `outr_d1` | `OUTR_D1` | texto | Outro exame Resultado Especificar. do_1 | — | todos |
| `dt_outr2` | `DT_OUTR2` | data | Outro exame Data da 2ª Coleta. 2 | — | todos |
| `outr_r2` | `OUTR_R2` | texto | Outro exame Resultado. do_2 | 1. Salmonella typhi 2. Salmonella SPP 3. Negativo 4. Outro agente | todos |
| `outr_d2` | `OUTR_D2` | texto | Outro exame Resultado Especificar. do_2 | — | todos |
| `dt_outr3` | `DT_OUTR3` | data | Outro exame Data da 3ª Coleta. 3 | — | todos |
| `outr_r3` | `OUTR_R3` | texto | Outro exame Resultado. do_3 | 1. Salmonella typhi 2. Salmonella SPP 3. Negativo 4. Outro agente | todos |
| `outr_d3` | `OUTR_D3` | texto | Outro exame Resultado Especificar. ds- outro_resultado_ 3 | — | todos |
| `clorafen` | `CLORAFEN` | texto | Antibióticos utilizados no tratamento Cloranfenicol. cloranfenicol | 1. Sim 2. Não 9. Ignorado | todos |
| `ampicilina` | `AMPICILINA` | texto | Antibióticos utilizados no tratamento Ampicilina | 1. Sim 2. Não 9. Ignorado | todos |
| `sulfa` | `SULFA` | texto | Antibióticos utilizados no tratamento Sulfametaxazol+Trimetropina | 1. Sim 2. Não 9. Ignorado | todos |
| `quinolona` | `QUINOLONA` | texto | Antibióticos utilizados no tratamento | 1. Sim 2. Não | todos |
| `ant_outr` | `ANT_OUTR` | texto | Antibióticos utilizados no tratamento Outro | 1. Sim 2. Não 9. Ignorado | todos |
| `ant_out_d` | `ANT_OUT_D` | texto | Se outros, especificar | — | todos |
| `dias` | `DIAS` | texto | Tempo de uso (dias). Tempo de uso do antibiótico (em dias) | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final | 1. Confirmado 2. Descartado | todos |
| `criterio` | `CRITERIO` | texto | Critério de confirmação/Descarte | 1. Laboratorial 2. Clínico epidemiológico | todos |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência? | 1 – Sim 2 – Não 3 – Indeterminado | todos |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o paciente foi provavelmente infectado | — | todos |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). o | — | todos |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). _infeccao | — | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho | 1. Sim 2. Não 9. Ignorado | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. o | 1. Cura 2. Óbito por febre tifóide 3. óbito por outras causas 9. Ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Data do encerramento da investigação | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | todos |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `dt_desc1` | `DT_DESC1` | data | Informações complementares e observações Data de deslocamento 1. informar data de deslocamento 1 | — | todos |
| `dt_desc2` | `DT_DESC2` | data | Informações complementares e observações Data de deslocamento 2. informar data de deslocamento 2 | — | todos |
| `dt_desc3` | `DT_DESC3` | data | Informações complementares e observações Data de deslocamento 3. informar data de deslocamento 3 | — | todos |
| `co_uf_des1` | `CO_UF_DES1` | texto | Informações complementares e observações UF deslocamento 1. 1 | — | todos |
| `co_uf_des2` | `CO_UF_DES2` | texto | Informações complementares e observações UF deslocamento 2. 2 | — | todos |
| `co_uf_des3` | `CO_UF_DES3` | texto | Informações complementares e. 3 | — | todos |
| `mun_des1` | `MUN_DES1` | texto | Informações complementares e observações Município deslocamento 1. mento_1 | — | todos |
| `mun_des2` | `MUN_DES2` | texto | Informações complementares e observações Município deslocamento 2. mento_2 | — | todos |
| `mun_des3` | `MUN_DES3` | texto | Informações complementares e observações Município deslocamento 3. mento_3 | — | todos |
| `pa_des1` | `PA_DES1` | inteiro | Informações complementares e observações País deslocamento 1. o_1 | — | todos |
| `pa_des2` | `PA_DES2` | inteiro | Informações complementares e observações País deslocamento 2. o_2 | — | todos |
| `pa_des3` | `PA_DES3` | inteiro | Informações complementares e observações País deslocamento. o_3 | — | todos |
| `ds_trans1` | `DS_TRANS1` | texto | Informações complementares e observações Meio de transporte 1. informar o meio de transporte de deslocamento 1 | — | todos |
| `ds_trans2` | `DS_TRANS2` | texto | Informações complementares e observações Meio de transporte 2. informar o meio de transporte de deslocamento 2 | — | todos |
| `ds_trans3` | `DS_TRANS3` | texto | Informações complementares e observações Meio de transporte 3. informar o meio de transporte de deslocamento 3 | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-ftif`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 28, inteiro: 4, texto: 100.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-ftif.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- o bloco laboratorial é organizado em 3 exames por material (hemocultura, urocultura, coprocultura e outros), que devem ser processados mediante "explodir" colunas por coluna de resultado; a validação do dicionário impede descartar casos com qualquer resultado *S. typhi* positivo — essa consistência deve ser preservada em pipelines; o histórico de contatos e portadores (`COPRO_R*`) é peça-chave para estudos de portador crônico; e o campo `ASSINTOMAT` marca portadores assintomáticos, que não devem ser contabilizados como casos de doença. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-ftif").glob("**/*.parquet"))
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
datasus-fetcher list sinan-ftif

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-ftif -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-ftif
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Febre Tifoide (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de febre tifoide (doença de transmissão fecal-oral, vigilância de portadores)
