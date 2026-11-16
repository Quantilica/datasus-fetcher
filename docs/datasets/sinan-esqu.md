---
dataset:
  id: sinan-esqu
  fonte: datasus
  titulo: Esquistossomose
  resumo: 'Esquistossomose do DATASUS: uma ficha de notificação/investigação de esquistossomose.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de esquistossomose
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 55
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    an_quant: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Esquistossomose (`sinan-esqu`)

## Resumo

O `sinan-esqu` contém os microdados das notificações e investigações epidemiológicas de casos de Esquistossomose mansoni (CID-10 B65.x) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de esquistossomose, preenchida pelas unidades de saúde de todo o país (com concentração histórica nas áreas endêmicas do Nordeste e Sudeste) e digitada no SINAN Net/Sinan Online. É a única base do SINAN com foco em doença parasitária crônica e laboratório de parasitologia (Kato-Katz), com 53 colunas: exames parasitológicos (Análise Quantitativa — número de ovos no Kato-Katz; Análise Qualitativa — Hoffman; e outros exames), quadro clínico e forma de apresentação (intestinal, hepato-intestinal, hepatoesplênica, aguda), tratamento (praziquantel/oxamniquine, e motivo da não realização), verificação de cura em até 3 amostras e a geolocalização da fonte provável de infecção (com nome de propriedade rural e coleção hídrica).

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ESQU` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ESQU` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `ESQUBR25.dbc` — `ESQU` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). A série em `FINAIS` vai de 2007 a 2022 e os anos de 2023 a 2026 estão apenas em `PRELIM` (ex.: `ESQUBR26.dbc`, atualização de 02/06/2026).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-esqu/<AAAA>/sinan-esqu_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-esqu/2024/sinan-esqu_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip`, as instruções POP_I/II/III de acesso, descompactação e tabulação e a ficha/dicionário de esquistossomose; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

A vigilância é conduzida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) em articulação com as Vigilâncias em Saúde dos estados e municípios das áreas endêmicas — bolsões históricos no Nordeste (Pernambuco, Bahia, Alagoas, Sergipe) e Sudeste (Minas Gerais e Espírito Santo) — e é complementada pelo Programa de Vigilância e Controle da Esquistossomose (PCE). A transmissão se dá por contato com coleções hídricas contaminadas com larvas (cercárias) de *Schistosoma mansoni*, liberadas por caramujos *Biomphalaria* — o que amarra a vigilância epidemiológica a fatores de saneamento, uso de água para trabalho (trabalhadores rurais), lazer e irrigação.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Esquistossomose** do SINAN Net (dicionário de dados v5.0, seções específicas revisadas em março/2012). A notificação nasce com a suspeição clínico-laboratorial e a confirmação se dá por exames parasitológicos de fezes: a **Análise Quantitativa (Kato-Katz)** registra a carga parasitária em ovos (`AN_QUANT`: 0 - 0 ovos; 1 - 1 ou mais ovos) e a **Análise Qualitativa (Hoffman)** o resultado do exame qualitativo (`AN_QUALI`: 1 - Positivo, 2 - Negativo, 3 - Não realizado), com data da coproscopia (`DT_COPRO`) e outros exames (`OUTROS`/`OUTRO_EX`). A investigação é completada com: a forma clínica (`FORMA`: 1 - Intestinal, 2 - Hepato-intestinal, 3 - Hepatoesplênica, 4 - Aguda, 5 - Outra, com descrição em `DS_FORMA`); o tratamento (realizado — praziquantel ou oxamniquine — `TRATAM` e `DTTRAT`, ou o motivo da não realização: contra-indicação, recusa ou ausente em `TRATANAO`); a verificação de cura em até 3 amostras (`STCURA1`, `STCURA2`, `STCURA3`: 0 - zero ovos, 1 - um ou mais ovos, 2 - Não realizado, com datas `DT_RESU3`); e a localização da fonte provável de infecção — UF, país, município, distrito, bairro (`COUFINF`, `COPAISINF`, `COMUNINF`, `CODISINF`, `CO_BAINFC`/`NOBAIINF`), nome da propriedade rural (`NOPROPIN`) e nome da coleção hídrica onde ocorreu a transmissão (`NOCOLINF`), campos essenciais para o mapeamento dos focos. A unidade de análise é o caso notificado.

A série histórica em `FINAIS` inicia em **2007** (implantação nacional do Sinan Net) e vai até **2022**; os anos de 2023 a 2026 estão apenas em `PRELIM` (ex.: `ESQUBR26.dbc`, atualização de 02/06/2026). O agravo autóctone é assinalado em `TPAUTOCTO` (1 - Sim, o sistema preenche automaticamente UF/país/município com os da residência; 2 - Não; 3 - Indeterminado) — mecanismo central para a distinção entre casos de transmissão local e casos em que a infecção ocorreu em outra área (não endêmica no município de residência). A cada caso notificado é possível o acompanhamento longitudinal do tratamento e da cura (até 3 amostras de fezes), o que permite estimar a efetividade do tratamento (cura parasitológica) e a recrudescência de carga parasitária em áreas de reinfecção.

Aplicações analíticas típicas: carga total de ovos por caso (Kato-Katz) e sua evolução por região endêmica; distribuição de formas clínicas (`FORMA`, com destaque para a forma hepatoesplênica/sévera); cobertura e resultado de tratamento (`TRATAM`, `TRATANAO`) e taxa de cura parasitológica (`STCURA1..3` — "0 ovos" na amostra de controle); mapeamento de focos de transmissão pela coleção hídrica e propriedade (`NOCOLINF`, `NOPROPIN`, local `COUFINF`/`COMUNINF`); estudo da autoctonia (`TPAUTOCTO`) e do risco associado ao trabalho (`DOENCA_TRA`); e letalidade (`EVOLUCAO`: 1 - Cura, 2 - Não Cura, 3 - Óbito por esquistossomose, 4 - Óbito por outras causas, 9 - Ignorado).

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-06-02.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `ESQUBR24.dbc` (53 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` / `DT_NOTIFIC` / `SEM_NOT` / `NU_ANO` | Data/Inteiro | Tipo de notificação, data, semana epidemiológica e ano |
| `ID_MUNICIP` / `SG_UF` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município e UF de notificação e residência |
| `ID_UNIDADE` / `ID_REGIONA` | String | Código CNES da unidade notificante e região de saúde |
| `DT_SIN_PRI` / `SEM_PRI` | Data/Inteiro | Data e semana de início dos sintomas |
| `NU_IDADE_N` / `CS_SEXO` / `CS_GESTANT` / `CS_RACA` / `CS_ESCOL_N` | Inteiro/String | Idade decomposta, sexo, gestação, raça/cor e escolaridade |
| `DT_INVEST` / `ID_OCUPA_N` | Data/Inteiro | Data da investigação e ocupação (CBO — relevante no agravo: trabalhadores rurais) |
| `DT_COPRO` | Data (`AAAAMMDD`) | Data da coproscopia |
| `AN_QUANT` | Inteiro | Análise Quantitativa (Kato-Katz): número de ovos — 0 - 0 (zero) ovos, 1 - 1 (um) ou mais ovos |
| `AN_QUALI` | Inteiro | Análise Qualitativa (Hoffman): 1 - Positivo, 2 - Negativo, 3 - Não realizado |
| `OUTROS` / `OUTRO_EX` | Inteiro/String | Resultado de outros exames parasitológicos e sua especificação |
| `TRATAM` | Inteiro | Fez tratamento? (1 - Sim, 3 - Não, 9 - Ignorado) |
| `DTTRAT` | Data (`AAAAMMDD`) | Data do tratamento |
| `TRATANAO` | Inteiro | Motivo do não tratamento: 1 - Contra-indicação, 2 - Recusa, 3 - Ausente, 9 - Ignorado |
| `STCURA1` / `STCURA2` / `STCURA3` | Inteiro | Verificação de cura (1ª, 2ª e 3ª amostra): 0 - 0 (zero) ovos, 1 - 1 (um) ou mais ovos, 2 - Não realizado |
| `DT_RESU3` | Data (`AAAAMMDD`) | Data do resultado da análise de verificação de cura (3ª amostra) |
| `FORMA` | Inteiro | Forma clínica: 1 - Intestinal, 2 - Hepato-intestinal, 3 - Hepatoesplênica, 4 - Aguda, 5 - Outra |
| `DS_FORMA` | String | Descrição da outra forma clínica (quando `FORMA` = 5) |
| `TPAUTOCTO` | Inteiro | O caso é autóctone do município de residência? 1 - Sim (preenche automaticamente UF/país/município da fonte de infecção), 2 - Não, 3 - Indeterminado |
| `COUFINF` / `COPAISINF` / `COMUNINF` / `CODISINF` | String | UF, país, município e distrito prováveis da fonte de infecção |
| `CO_BAINFC` / `NOBAIINF` | String | Bairro provável da fonte de infecção (código ou nome digitado) |
| `NOPROPIN` | String | Nome da propriedade onde ocorreu a transmissão (área rural) |
| `NOCOLINF` | String | Nome da coleção hídrica onde ocorreu a transmissão |
| `DOENCA_TRA` | Inteiro | Doença relacionada ao trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `EVOLUCAO` | Inteiro | Evolução do caso: 1 - Cura, 2 - Não Cura, 3 - Óbito por esquistossomose, 4 - Óbito por outras causas, 9 - Ignorado |
| `DT_OBITO` / `DT_ENCERRA` / `DT_DIGITA` | Data (`AAAAMMDD`) | Data do óbito, de encerramento do caso e de digitação |
| `DT_TRANS*` | Data (`AAAAMMDD`) | Datas de tramitação e trânsito entre níveis do sistema |

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
| `dt_invest` | `DT_INVEST` | data | Data da Investigação. Data em que ocorreu a investigação – informar a Data da 1ª visita feita ao portador de esquistossomose | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Ocupação do indivíduo que sofreu o agravo | — | todos |
| `dt_copro` | `DT_COPRO` | data | Data da Coproscopia. Informar a data de realização da coproscopia | — | todos |
| `an_quant` | `AN_QUANT` | inteiro | Análise Quantitativa. Informar o número de ovos que foi encontrado no exame Kato-Katz | 0 –0(zero) 1- 1 (um) ou mais ovos | todos |
| `outros` | `OUTROS` | texto | Outros. Anotar o CÓDIGO 3 se outro exame não foi realizado e 1 ou 2 , respectivamente, conforme o resultado tenha sido positivo ou | 1. Positivo 2. Negativo 3. Não realizado | todos |
| `tratam` | `TRATAM` | texto | Fez Tratamento? | 1. Sim, Praziquantel 2. Sim, Oxaminiquine 3. Não 9. Ignorado | todos |
| `tratanao` | `TRATANAO` | texto | Caso não tenha feito tratamento, qual o motivo? | 1. Contra- indicação 2. Recusa 3. Ausente 9. Ignorado | todos |
| `stcura1` | `STCURA1` | texto | Resultado da análise de verificação de cura - 1ª amostra. Informar no quadrado correspondente à 1a amostra o CÓDIGO 1 ou 2, conforme o número de ovos detectados no exame tenha sido, respectivamente, 0 ou mais de 1 | 0 – 0 (zero) 1- 1 ou + 2. Não Realizado | todos |
| `stcura2` | `STCURA2` | texto | de verificação de cura - 2ª amostra. respectivo à 2a amostra o CÓDIGO 1 ou 2, conforme o número de ovos detectados no exame tenha sido, respectivamente, 0 ou mais de 1 | 1- 1 ou + 2. Não Realizado | todos |
| `stcura3` | `STCURA3` | texto | Resultado da análise de verificação de cura - 3ª amostra. Informar no quadrado respectivo à 3a amostra o CÓDIGO 1 ou 2, conforme o número de ovos detectados no exame tenha sido, respectivamente, 0 ou mais de 1 | 0 – 0 (zero) 1- 1 ou + 2. Não Realizado | todos |
| `forma` | `FORMA` | texto | Especificar forma clínica. Informar no quadrado do campo 43 os CÓDIGOS 1 se a classificação da forma anátomo-clínica for intestinal, 2 se a forma hepato intestinal, 3 se hepato esplênica, 4 se foram aguda 3 5 para outra forma | 1. Intestinal 2. Hepato intestinal 3. Hepato esplênica 4. Aguda 5. Outra, | todos |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é autóctone do município de residência? | 1-sim 2-não 3- indeterminado | todos |
| `coufinf` | `COUFINF` | texto | UF. Local provável da fonte de infecção UF | — | todos |
| `copaisinf` | `COPAISINF` | texto | País. País provável da fonte de infecção | — | todos |
| `comuninf` | `COMUNINF` | texto | Município. Município provável da fonte de infecção | — | todos |
| `nopropin` | `NOPROPIN` | texto | Nome da propriedade (se área rural). Informar o nome da propriedade onde ocorreu a transmissão, se área rural | — | todos |
| `nocolinf` | `NOCOLINF` | texto | Nome da coleção hídrica (nota 2). Informar o nome da coleção hídrica onde ocorreu a transmissão | — | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho. Informar no quadrado do campo 52 o CÓDIGO 1 se o caso , estiver relacionado ao trabalho, 2 se não relacionado ao trabalho ou 9 se ignorado, | 1. Sim 2. Não 9. Ignorado | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. Informar no quadrado do campo 53 o CÓDIGO 1 for cura, 2 para não cura, 3 para óbito por esquistossomose, 4 para óbito por outras causas ou 9 se ignorado | 1. Cura 2, Não Cura 3. Óbito por esquistossomose 4-Óbito por outras causas 9. Ignorado | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Informar a data do encerramento do caso | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito. Informar a data do óbito | — | todos |
| `ds_forma` | `DS_FORMA` | texto | Especificar forma clínica, se Outro especificar. Habilitar se campo 43 (Especificar forma clinica) = 5 | — | todos |
| `an_quali` | `AN_QUALI` | texto | Análise Qualitativa. Anotar o CÓDIGO 3 se o exame Hoffman não foi realizado e 1 ou 2, respectivamente, conforme o resultado tenha sido positivo ou negativo | 1. Positivo 2. Negativo 3. Não realizado | todos |
| `dttrat` | `DTTRAT` | data | Data do tratamento | — | todos |
| `dt_resu3` | `DT_RESU3` | data | Data do resultado da 3ª amostra | — | todos |
| `outro_ex` | `OUTRO_EX` | texto | Outros exames, especificar. Anotar no campo 37, qual o nome do outro exame realizado | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-esqu`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 14, inteiro: 2, nulo (vazio nas amostras): 2, texto: 39.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-esqu.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- a verificação de cura usa a codificação "0/1" (número de ovos) e não "positivo/negativo" — diferente de `AN_QUALI`/`OUTROS` (1 - Positivo/2 - Negativo/3 - Não realizado), o que exige mapeamentos distintos; `AN_QUANT` = 0 pode significar "negativo" ou resultado de cura, e o campo só distingue presença/ausência de ovos (não a carga exata); os campos de fonte de infecção são preenchidos automaticamente quando `TPAUTOCTO` = 1 (durante análises, filtrar casos autóctones separa transmissão local de importação); `NOPROPIN` e `NOCOLINF` são texto livre (nome de propriedade e coleção hídrica) e exigem normalização para estudos de focos. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-esqu").glob("**/*.parquet"))
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
datasus-fetcher list sinan-esqu

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-esqu -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-esqu
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Esquistossomose (ficha e dicionário de dados v5.0, rev. março/2012)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de Esquistossomose (Programa de Vigilância e Controle da Esquistossomose, PCE)
