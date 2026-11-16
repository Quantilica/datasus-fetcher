---
dataset:
  id: sinan-tube
  fonte: datasus
  titulo: Tuberculose
  resumo: 'Tuberculose do DATASUS: uma ficha de notificação/investigação de tuberculose.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2001'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de tuberculose
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 99
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_contato: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_comu_ex: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Tuberculose (`sinan-tube`)

## Resumo

O `sinan-tube` contém os microdados das notificações e investigações epidemiológicas de casos de Tuberculose (CID-10 A15 a A19) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha de notificação/investigação de um caso suspeito ou confirmado de tuberculose, preenchida pelas unidades de saúde de todo o país e digitada nos módulos Sinan Windows, Sinan Net e Sinan Online. É a maior base de morbidade de doença infecciosa crônica do Brasil, com dezenas de campos que cobrem o diagnóstico, a forma clínica, a rede de exames bacteriológicos (baciloscopias, culturas e testes moleculares), o esquema terapêutico e o acompanhamento mensal do paciente até o encerramento do caso.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `TUBE` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `TUBE` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `TUBEBR22.dbc` — `TUBE` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `22` é o ano de notificação (2022). Na prática, as consolidações até 2019 estão em `FINAIS` e os anos de 2020 a 2025 estão apenas em `PRELIM` (ex.: `TUBEBR25.dbc`), ainda sujeitos a revisão.
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-tube/<AAAA>/sinan-tube_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-tube/2024/sinan-tube_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções de acesso e conversão (`POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`); em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

A tuberculose é uma doença de alta relevância para o sistema de vigilância brasileiro, que a monitora por meio da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) e do GT-SINAN. A notificação é compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, e hoje integra a Lista Nacional de Agravos de Notificação Compulsória consolidada na Portaria GM/MS nº 204/2016. O Brasil integra os 30 países prioritários da OMS para tuberculose, e esta base é o instrumento oficial para dimensionar a incidência anual (por 100 mil habitantes, com as estimativas populacionais TCU), a distribuição das formas clínicas, os agravos associados (HIV/AIDS, diabetes, alcoolismo, tabagismo, uso de outras drogas), as populações-chave (privadas de liberdade, população em situação de rua, profissionais de saúde, imigrantes e beneficiários de programas sociais) e os desfechos do tratamento (cura, abandono, óbito, falência e a incorporação da tuberculose drogarresistente).

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Tuberculose** do SINAN (ficha consolidada v5.0, atual para o regime terapêutico introduzido em 2019). Cada notificação nasce quando o profissional de saúde suspeita de tuberculose (sintomático respiratório com tosse há mais de 15 dias ou caso confirmado por baciloscopia, cultura ou teste molecular rápido) e é completada ao longo da investigação com dados clínicos, laboratoriais, terapêuticos e de acompanhamento mensal até o encerramento (cura, abandono, óbito, transferência ou mudança de diagnóstico). A unidade de análise é o caso notificado (paciente), não o óbito nem a internação, que ficam no SIM e no SIH/SIA.

A série histórica registra três fases do sistema de informação: de **2001 a 2006** os dados provêm do Sinan-Windows (com o campo `MIGRADO_W` distinguindo registros migrados para o Sinan Net); de **2007 em diante**, as bases provêm do Sinan Net e, mais recentemente, do **Sinan Online**, com a mesma base disseminada. O instrumento de coleta foi atualizado de forma relevante ao longo do tempo: a ficha atual incorpora dígitos de acompanhamento mensal das baciloscopias ao longo do tratamento (`BACILOSC_1` a `BACILOSC_6`), controle da situação de encerramento (`SITUA_9_M`, `SITUA_12_M`, `SITUA_ENCE`), registro do teste molecular rápido e de sensibilidade (`TEST_MOLEC`, `TEST_SENSI`), da terapia antirretroviral (`ANT_RETRO`) e das cinco populações-chave (`POP_LIBER`, `POP_RUA`, `POP_SAUDE`, `POP_IMIG`, `BENEF_GOV`).

Aplicações analíticas típicas: incidência anual de casos confirmados por faixa etária e sexo; distribuição das formas pulmonares versus extrapulmonares (`FORMA`, `EXTRAPU1_N`, `EXTRAPU2_N`) e o percentual de casos pulmonares com baciloscopia positiva (`BACILOSC_E`); percentual de casos com HIV testado e positivo (`HIV`); monitoramento do esquema terapêutico (drogas prescritas e regime, com data de início em `DT_INIC_TR`); detecção de tuberculose drogarresistente; e indicadores de acompanhamento como o total de contatos examinados (`NU_COMU_EX`), o percentual de tratamento supervisionado (`TRATSUP_AT`) e e a situação de encerramento (`SITUA_ENCE`), que mede cura, abandono e óbito do programa.

### Cobertura observada

- Índice do FTP (2026-10): 25 arquivos, de 2001 a 2025, 1 UF(s) com arquivos, última atualização em 2026-05-07.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2001 a 2025), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `TUBEBR22.dbc` (95 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual, 3 - Surto e outros) |
| `ID_AGRAVO` | String | Código do agravo conforme CID-10 (A15 a A19) |
| `DT_NOTIFIC` | Data (`AAAAMMDD`) | Data de preenchimento da ficha de notificação |
| `NU_ANO` | Inteiro | Ano da notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_MN_RESI` | String (6/7) | Código IBGE do município de residência do caso |
| `DT_DIAG` | Data (`AAAAMMDD`) | Data do diagnóstico do caso |
| `NU_IDADE_N` | Inteiro composto | Idade (o primeiro dígito indica a unidade: dia/mês/ano) |
| `CS_SEXO` | String (1) | Sexo do paciente (M/F/I - Ignorado) |
| `TRATAMENTO` | Inteiro | Tipo de entrada: 1 - Novo, 2 - Recidiva, 3 - Reingresso após abandono, 4 - Não sabe, 5 - Transferência, 6 - Pós-óbito |
| `INSTITUCIO` | Inteiro | Instituição que realizou o diagnóstico/notificação |
| `RAIOX_TORA` | Inteiro | Resultado da radiografia de tórax (positivo/negativo/não realizado) |
| `TESTE_TUBE` | Inteiro | Resultado do teste tuberculínico (PPD) |
| `FORMA` | Inteiro | Forma clínica: 1 - Pulmonar, 2 - Extrapulmonar, 3 - Pulmonar e extrapulmonar |
| `EXTRAPU1_N` / `EXTRAPU2_N` | Inteiro | Localização extrapulmonar primária e secundária (pleural, ganglionar, óssea, neurológica/genitourinária e outras) |
| `BACILOSC_E` / `BACILOS_E2` | Inteiro | Baciloscopias de escarro no diagnóstico: 1 - Positiva, 2 - Negativa, 3 - Não realizada, 4 - Não se aplica |
| `CULTURA_ES` / `CULTURA_OU` | Inteiro | Cultura de escarro e de outro material (positiva/negativa, sensibilidade à ação de antibacilares) |
| `HIV` | Inteiro | Situação de HIV (1 - Positivo, 2 - Negativo, 3 - Em andamento, 4 - Não realizado) |
| `AGRAV*` | Inteiro | Agravos comórbidos e fatores de risco: `AGRAVDIABE` (diabetes), `AGRAVALCOO` (alcoolismo), `AGRAVDROGA` (outras drogas), `AGRAVTABAC` (tabagismo), `AGRAVAIDS` (AIDS), `AGRAVDOENC` (outras doenças), `AGRAVOUTRA` (outros) |
| `DT_INIC_TR` | Data (`AAAAMMDD`) | Data de início do esquema terapêutico |
| `RIFAMPICIN`/`ISONIAZIDA`/`ETAMBUTOL`/`ESTREPTOMI`/`PIRAZINAMI`/`ETIONAMIDA` | Inteiro | Drogas preconizadas no esquema terapêutico (1 - Usou, 2 - Não usou) |
| `TEST_MOLEC` | Inteiro | Teste Molecular Rápido TB (TMR-TB): 1 - Detectável sensível à rifampicina, 2 - Detectável resistente à rifampicina, 3 - Não detectável, 4 - Inconclusivo, 5 - Não realizado |
| `TEST_SENSI` | Inteiro | Teste de sensibilidade (resistente a antibacilares, como isoniazida ou rifampicina) |
| `POP_LIBER`/`POP_RUA`/`POP_SAUDE`/`POP_IMIG`/`BENEF_GOV` | Inteiro | Populações-chave: 1 - Sim, 2 - Não, 3 - Ignorado (privada de liberdade, em situação de rua, profissional de saúde, imigrante, beneficiária de programa social) |
| `BACILOSC_1` a `BACILOSC_6` | Inteiro | Baciloscopias de escarro de acompanhamento (meses 1 a 6): positividade/negatividade parcial na série |
| `SITUA_9_M` / `SITUA_12_M` / `SITUA_ENCE` | Inteiro | Situação de encerramento no 9º mês, no 12º mês e ao fim do esquema: 1 - Cura, 2 - Abandono, 3 - Óbito por TB, 4 - Óbito por outras causas, 5 - Transferência, 6 - Mudança de diagnóstico, 7 - TB-DR, 8 - Mudança de Esquema, 9 - Falência, 10 - Abandono Primário |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `NU_COMU_EX` | Inteiro | Total de contatos examinados na investigação e acompanhamento |
| `TRANSF`/`UF_TRANSF`/`MUN_TRANSF` | Inteiro / String | Registro de transferência de caso entre municípios (1 - Sim) e destino (UF, município) |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_diag` | `DT_DIAG` | data | Data dos primeiros sintomas / Diagnóstico. Data dos primeiros sintomas do caso de agravo agudo. Data do diagnóstico do caso de agravo crônico e DRTs Data do acidente nos acidentes da saúde do trabalhador | — | todos |
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
| `in_vincula` | `IN_VINCULA` | texto | Vinculação. 0 ou branco – Não Vinculado 1 – Vinculado | — | todos |
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
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Ocupação do indivíduo que sofreu o agravo | — | todos |
| `tratamento` | `TRATAMENTO` | texto | Tipo de Entrada. Preencher com o código correspondente ao tipo de entrada do paciente na unidade de saúde. O “caso novo” é todo paciente que nunca se submeteu ao tratamento de | 1. Caso Novo 2. Recidiva 3. Reingresso após Abandono 4. Não Sabe 5. Transferência 6. Pós-óbito | todos |
| `institucio` | `INSTITUCIO` | texto | Institucionalizado em. Informar se paciente é institucionalizado e em que tipo de instituição. Havendo mais de um tipo de instituição considerar o de maior tempo de permanência | 1. Creche 2. Escola 3. Asilo 4. Empresa 5. Penitenciária 6. Hospital/ Clínica 7. Outras 8. Não institucionalizado 9.Ignorado | todos |
| `raiox_tora` | `RAIOX_TORA` | texto | Radiografia do tórax. Resultado da radiografia do tórax por ocasião da notificação (a opção 3 diz respeito a outras alterações não compatíveis com a tuberculose) | 1. Suspeito 2. Normal 3. Outra patologia 4. Não realizado | todos |
| `teste_tube` | `TESTE_TUBE` | texto | Dado de exame laboratorial registrado na ficha de Tuberculose (`TESTE_TUBE`); o dicionário consultado não define o campo isoladamente | — | todos |
| `forma` | `FORMA` | texto | Forma. Forma clínica da tuberculose, por ocasião da notificação, segundo a sua localização | 1. Pulmonar 2. Extrapulmonar 3. Pulmonar + Extrapulmonar | todos |
| `extrapu1_n` | `EXTRAPU1_N` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `extrapu2_n` | `EXTRAPU2_N` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `extrapul_o` | `EXTRAPUL_O` | texto | Se extrapulmonar Outras especificar. Se extrapulmonar outro tipo que não os listados especificar | — | 2001 a 2018 |
| `agravaids` | `AGRAVAIDS` | texto | Doenças e. Informar se existem | 1. Sim | todos |
| `agravalcoo` | `AGRAVALCOO` | texto | Doenças e agravos associados Alcoolismo. Informar se existem agravos associados à tuberculose por ocasião da notificação | 1. Sim 2. Não 9. Ignorado | todos |
| `agravdiabe` | `AGRAVDIABE` | texto | Doenças e agravos associados Diabetes. Informar se existem agravos associados à tuberculose por ocasião da notificação | 1. Sim 2. Não 9. Ignorado | todos |
| `agravdoenc` | `AGRAVDOENC` | texto | Doenças e agravos associados Doença Mental. Informar se existem agravos associados à tuberculose por ocasião da notificação | 1. Sim 2. Não 9. Ignorado | todos |
| `agravoutra` | `AGRAVOUTRA` | texto | Doenças e agravos associados Outras. Informar se existem agravos associados à tuberculose por ocasião da notificação | 1. Sim 2. Não 9. Ignorado | todos |
| `agravoutde` | `AGRAVOUTDE` | texto | Doenças e agravos associados. Especificar qual outros agravos associados | — | 2001 a 2018 |
| `bacilosc_e` | `BACILOSC_E` | texto | Baciloscopia de escarro (diagnóstico). Resultado da baciloscopia de escarro para BAAR (Bacilo álcool ácido resistente) realizada em 1ª e 2ª amostras para diagnóstico O resultado positivo em qualquer das baciloscopia de diagnóstico deve ser informado. Usa-se o a opção 4=Não se aplica para os casos cujo campo 35 (Forma) = 2 (Extrapulmonar) | 1. Positiva 2. Negativa 3. Não realizada 4. Não se aplica | todos |
| `bacilos_e2` | `BACILOS_E2` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `bacilosc_o` | `BACILOSC_O` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `cultura_es` | `CULTURA_ES` | texto | Cultura. Resultado da cultura | 1. Positiva | todos |
| `cultura_ou` | `CULTURA_OU` | texto | Dado de exame laboratorial registrado na ficha de Tuberculose (`CULTURA_OU`); o dicionário consultado não define o campo isoladamente | — | todos |
| `hiv` | `HIV` | texto | HIV. Resultado da sorologia para o vírus da imunodeficiência adquirida, realizado anterior ou posteriormente a | 1. Positivo 2. Negativo 3. Em andamento 4. Não realizado | todos |
| `histopatol` | `HISTOPATOL` | texto | Histopatologia. Resultado do exame histopatólogico para diagnóstico de TB | 1. Baar Positivo 2. Sugestivo de TB 3. Não sugestivo de TB 4. Em andamento 5. Não realizado | todos |
| `dt_inic_tr` | `DT_INIC_TR` | data | Data de início do tratamento atual. Data em que o paciente iniciou o tratamento atual. Em situações de transferência essa data deverá ser igual a data de início do tratamento onde o paciente diagnosticou e iniciou o tratamento | — | todos |
| `rifampicin` | `RIFAMPICIN` | texto | Medicamento do esquema: rifampicina (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `isoniazida` | `ISONIAZIDA` | texto | Medicamento do esquema: isoniazida (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `etambutol` | `ETAMBUTOL` | texto | Medicamento do esquema: etambutol (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `estreptomi` | `ESTREPTOMI` | texto | Medicamento do esquema: estreptomicina (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `pirazinami` | `PIRAZINAMI` | texto | Medicamento do esquema: pirazinamida (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `etionamida` | `ETIONAMIDA` | texto | Medicamento do esquema: etionamida (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `outras` | `OUTRAS` | texto | O paciente foi submetido ou exposto à: Outras. Informar se o paciente submeteu-se outras situações de risco diferentes das existentes no campo, há quanto tempo. Se sim, especificar a situação. (considerar a data da investigação como parâmetro) | 1. Sim há menos de 6 meses 2. Sim há mais de seis meses 3. Não 9- Ignorado | todos |
| `outras_des` | `OUTRAS_DES` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2001 a 2018 |
| `trat_super` | `TRAT_SUPER` | texto | Tratamento diretamente observado (supervisionado) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_contato` | `NU_CONTATO` | inteiro | Número de contatos registrados (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `sg_uf_at` | `SG_UF_AT` | texto | UF do atendimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `id_munic_a` | `ID_MUNIC_A` | texto | Município de notificação atual. Código e nome dos municípios do cadastro do IBGE | — | todos |
| `dt_noti_at` | `DT_NOTI_AT` | data | Data de notificação atual. Data da Notificação Atual | — | todos |
| `sg_uf_2` | `SG_UF_2` | texto | UF de residência atual. Sigla da UF de residência atual | — | todos |
| `id_munic_2` | `ID_MUNIC_2` | texto | Município de residência atual. Identificação do município de residência atual | — | todos |
| `bacilosc_1` | `BACILOSC_1` | texto | Baciloscopia no 1º mês. Resultado da baciloscopia de escarro para BAAR (Bacilo Alcóol- Resistentes) realizada em amostra colhida ao final do 1º mês de tratamento | 1- Positiva 2- Negativa 3- Não realizada 4- Não se aplica | todos |
| `bacilosc_2` | `BACILOSC_2` | texto | Baciloscopia no 2º mês. Resultado da baciloscopia de escarro para BAAR (Bacilo Alcóol- Resistentes) realizada em amostra colhida ao final do 2º mês de tratamento | 1- Positiva 2- Negativa 3- Não realizada 4- Não se aplica | todos |
| `bacilosc_3` | `BACILOSC_3` | texto | Baciloscopia no 3º mês. Resultado da baciloscopia de escarro para BAAR (Bacilo Alcóol- Resistentes) realizada em amostra colhida ao | 1- Positiva 2- Negativa 3- Não realizada 4- Não se aplica | todos |
| `bacilosc_4` | `BACILOSC_4` | texto | Baciloscopia no 4º mês. Resultado da baciloscopia de escarro para BAAR (Bacilo Alcóol- Resistentes) realizada em amostra colhida ao final do 4º mês de tratamento | 1- Positiva 2- Negativa 3- Não realizada 4- Não se aplica | todos |
| `bacilosc_5` | `BACILOSC_5` | texto | Baciloscopia no 5º mês. Resultado da baciloscopia de escarro para BAAR (Bacilo Alcóol- Resistentes) realizada em amostra colhida ao final do 5º mês de tratamento | 1- Positiva 2- Negativa 3- Não realizada 4- Não se aplica | todos |
| `bacilosc_6` | `BACILOSC_6` | texto | Baciloscopia no 6º mês. Resultado das baciloscopias de escarro para BAAR (Bacilo Alcóol- Resistentes) realizadas em amostras colhidas no 6º mês de tratamento | 1- Positiva 2- Negativa 3- Não realizada 4- Não se aplica | todos |
| `tratsup_at` | `TRATSUP_AT` | texto | Tratamento Diretamente Observado (TDO) realizado | 1- Sim 2- Não 9- Ignorado | todos |
| `dt_mudanca` | `DT_MUDANCA` | data | Data registrada na ficha de Tuberculose (`DT_MUDANCA`); o dicionário consultado não define o campo isoladamente | — | todos |
| `nu_comu_ex` | `NU_COMU_EX` | inteiro | Número de comunicantes examinados (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `situa_9_m` | `SITUA_9_M` | texto | Situação de encerramento aos 9 meses de tratamento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `situa_12_m` | `SITUA_12_M` | texto | Situação de encerramento aos 12 meses de tratamento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `situa_ence` | `SITUA_ENCE` | texto | Situação de encerramento. Situação de encerramento do caso notificado | 1. Cura 2. Abandono 3. Óbito por TB 4. Óbito por outras causas 5. Transferência 6. Mudança de Diagnóstico 7. TB-DR 8. Mudança de Esquema 9. Falência 10. Abandono Primário | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data de encerramento. Date | — | todos |
| `tpuninot` | `TPUNINOT` | texto | Tipo da unidade notificadora (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `pop_liber` | `POP_LIBER` | texto | Populações Especiais População privada de liberdade. Informar situação do paciente quanto à condição de vulnerabilidade. Sendo considerada População Privada de Liberdade a população prisional segundo a | 1. Sim 2. Não 9. Ignorado | todos |
| `pop_rua` | `POP_RUA` | texto | Populações Especiais População em situação de rua. Informar situação do paciente quanto à condição de vulnerabilidade | 1. Sim 2. Não 9. Ignorado | todos |
| `pop_saude` | `POP_SAUDE` | texto | Populações Especiais Profissional de saúde. tp_pop_saúde | 1. Sim 2. Não 9. Ignorado | todos |
| `pop_imig` | `POP_IMIG` | texto | Populações Especiais Imigrante. Informar situação do paciente quanto à condição de vulnerabilidade. Sendo considerado Imigrante, o estrangeiro residente no Brasil por menos de 2 anos | 1. Sim 2. Não 9. Ignorado | todos |
| `benef_gov` | `BENEF_GOV` | texto | Beneficiário de programa de transferência de renda do governo. tp-benef_gov | 1- Sim 2- Não 9- Ignorado | todos |
| `agravdroga` | `AGRAVDROGA` | texto | Doenças e agravos associados Uso de drogas ilícitas. Informar se existem agravos associados à tuberculose por ocasião da notificação | 1. Sim 2. Não 9. Ignorado | todos |
| `agravtabac` | `AGRAVTABAC` | texto | Doenças e agravos associados Tabagismo. Informar se existem agravos associados à tuberculose por ocasião da notificação | 1. Sim 2. Não 9. Ignorado | todos |
| `test_molec` | `TEST_MOLEC` | texto | Dado de exame laboratorial registrado na ficha de Tuberculose (`TEST_MOLEC`); o dicionário consultado não define o campo isoladamente | — | todos |
| `test_sensi` | `TEST_SENSI` | texto | Teste de Sensibilidade. Resultado do teste de sensibilidade do paciente para conhecimento oportuno do padrão de resistência às drogas do esquema básico | 1. Resistente somente à Isoniazida 2. Resistente somente à Rifampicina 3. Resistente à Isoniazida e Rifampicina 4. Resistente a | todos |
| `ant_retro` | `ANT_RETRO` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Tuberculose (`ANT_RETRO`); o dicionário consultado não define o campo isoladamente | — | todos |
| `bac_apos_6` | `BAC_APOS_6` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `transf` | `TRANSF` | texto | Se transferência. Preencher com o código correspondente se a situação de encerramento for por “transferência” | 1. Mesmo município 2. Município diferente (mesma UF) 3. UF diferente 4. País diferente 9. Ignorado | todos |
| `uf_transf` | `UF_TRANSF` | texto | UF de transferência (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `mun_transf` | `MUN_TRANSF` | texto | Município de Transferência (destino do paciente). Município para onde o paciente foi transferido (TABELA DO SISTEMA) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-tube`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 13, inteiro: 3, texto: 83.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-tube.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- as bases até 2019 estão em `FINAIS` e os anos 2020 a 2025 apenas em `PRELIM` (sujeitos a revisão); o leiaute da ficha foi atualizado ao longo do tempo (inclusão de `POP_*`, `TEST_MOLEC`, `TEST_SENSI`, `ANT_RETRO`), o que exige tratamento granular por ano e, em alguns registros, valores nulos em campos novos; `NU_IDADE_N` requer decomposição do primeiro dígito (unidade: dia/mês/ano) antes de comparações; os campos de identificação de transferência (`TRANSF`, `UF_TRANSF`, `MUN_TRANSF`, `MIGRADO_W`) indicam movimentação de casos entre unidades/territórios e persistem no DBF para acesso a detalhes de investigação. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 3 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-tube").glob("**/*.parquet"))
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
datasus-fetcher list sinan-tube

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-tube -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-tube
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Tuberculose (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br (documentos em `images/documentos/Agravos/Tuberculose`)
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de tuberculose e Manual de Recomendações para o Controle da Tuberculose no Brasil
