---
dataset:
  id: sinan-raiv
  fonte: datasus
  titulo: Raiva
  resumo: 'Raiva do DATASUS: uma ficha de notificação/investigação de raiva.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de raiva
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 96
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
    num_doses: 'número inteiro: contagem ou código numérico (ver Descrição)'
    doses_a: 'número inteiro: contagem ou código numérico (ver Descrição)'
    quantid: quantidade
    varia_vir: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Raiva (`sinan-raiv`)

## Resumo

O `sinan-raiv` contém os microdados das notificações e investigações de casos de Raiva Humana (CID-10 A82) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de raiva humana, digitado no SINAN Net/Sinan Online. A raiva humana é de notificação compulsória imediata (em até 24 horas) e a base é o insumo oficial para acompanhar o último elo do ciclo de vigilância da raiva, cuja meta é a eliminação mediada pelo atendimento antirrábico (dataset `sinan-antr`).

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `RAIV` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `RAIV` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `RAIVBR07.dbc` — prefixo `RAIV`, `BR` (consolidação nacional) e `07` (ano 2007), até `RAIVBR24.dbc` (2024); os anos recentes ficam em `PRELIM` (ex.: `RAIVBR26.dbc`). O volume é minúsculo (~163 kB em 20 arquivos), pois os casos humanos de raiva são eventos raríssimos e esporádicos.
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-raiv/<AAAA>/sinan-raiv_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-raiv/2024/sinan-raiv_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## Conteúdo

A raiva humana é uma encefalite viral de quase 100% de letalidade, uma vez iniciados os sintomas, com notificação compulsória imediata (Portaria SVS/MS nº 104/2011; consolidada na Portaria GM/MS nº 204/2016). A vigilância é da SVSA/MS, por meio do Programa de Vigilância da Raiva, que integra o registro de casos humanos (deste dataset), a vigilância de epizootias em animais (canina, felina, silvestre — morcegos hematófagos e não hematófagos) e o registro de atendimentos antirrábicos (`sinan-antr`). O Brasil reduziu drasticamente o número de casos humanos: a grande maioria na atualidade envolve morcegos silvestres e populações rurais indígenas.

O evento gerador é a **Ficha de Investigação de Raiva Humana** do SINAN (ficha `Raiva_v5`, de 2006, com instrucional e dicionário próprios), preenchida diante do caso suspeito — pessoa com encefalite aguda progressiva (excitação, paralisia, sialorreia, hidrofobia) ou morte súbita por encefalite sem causa, com história de exposição (mordedura, arranhadura, lambedura em mucosa, contato indireto) e/ou epizootia precedente — e completada com exames (imunofluorescência direta e RT-PCR em material clínico) e o desfecho fatal, pois praticamente todos os casos confirmados terminam em óbito. A unidade de análise é o caso suspeito/confirmado individual.

Marcos de leiaute: a ficha `Raiva_v5` (2006) padronizada no SINAN Net traz campos de exposição ao vírus (tipo de exposição, localização), espécie do animal agressor (canina, felina, quiróptera/morcego, primata, raposa), tratamento em curso e datas de aplicação de doses de vacina e soro. Com a expansão da cobertura da vacinação canina, a cadeia dominante de casos humanos atuais envolve morcegos (hematófagos e não hematófagos).

Aplicações analíticas: monitor da eliminação da raiva, espécie do animal agressor e localização provável de infecção, letalidade (aprox. 100% nos casos confirmados), casos em população indígena e rural, e integração com epizootias e atendimentos antirrábicos (dataset `sinan-antr`).

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-06-02.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Raiva Humana — CID-10 A82.9 e demais A82.x) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave; compulsória imediata) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (encefalite progressiva) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `ESP_ANIMAL` | String | Espécie do animal agressor (1 - Canina, 2 - Felina, 3 - Quiróptera/Morcego, 4 - Primata, 5 - Raposa, 7 - Outra, 9 - Ignorado) |
| `CLASSI_FIN` | Inteiro | Classificação final (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

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
| `nduplic_n` | `NDUPLIC_N` | texto | Não Listar/ Não Contar. 0 ou branco – Não identificado 1 – Não é duplicidade (não listar) 2 – Duplicidade (não contar) | — | todos |
| `cs_flxret` | `CS_FLXRET` | texto | Fluxo de retorno. Identifica se o registro está habilitado ou foi enviado pelo fluxo de retorno para o município de residência | 0 - Não 1 - habilitado para envio. 2 - enviado | todos |
| `flxrecebi` | `FLXRECEBI` | texto | Recebida por fluxo de retorno (campo interno). Colocar a estrutura do nº atribuído pelo sistema | — | todos |
| `migrado_w` | `MIGRADO_W` | texto | Identifica migração (campo interno). Identifica se o registro é oriundo da rotina de migração da base Windows | 1- migrado do Sinan Windows | todos |
| `dt_invest` | `DT_INVEST` | data | Data da Investigação. Data em que iniciou a investigação – informar a Data da 1ª visita | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/ Ramo de atividade. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo de atividade | — | todos |
| `arranhao` | `ARRANHAO` | texto | Tipo de exposição ao vírus rábico Arranhão. Forma de exposição ao vírus da raiva | 1. Sim 2. Não 9. Ignorado | todos |
| `lambedura` | `LAMBEDURA` | texto | Tipo de exposição ao vírus rábico Lambedura. Forma de exposição ao vírus da raiva | 1. Sim 2. Não 9. Ignorado | todos |
| `mordedura` | `MORDEDURA` | texto | Tipo de exposição ao vírus rábico Mordedura. Forma de exposição ao vírus da raiva | 1. Sim 2. Não 9. Ignorado | todos |
| `contato` | `CONTATO` | texto | Tipo de exposição ao vírus rábico Contato Indireto | 1. Sim 2. Não 9. Ignorado | todos |
| `mucosa` | `MUCOSA` | texto | Localização Mucosa. Localização do ferimento | 1. Sim 2. Não | todos |
| `cabeca` | `CABECA` | texto | Localização Cabeça/Pescoço | 1. Sim 2. Não 9. Ignorado | todos |
| `maos_n` | `MAOS_N` | texto | Localização Mãos. Localização do ferimento | 1. Sim 2. Não 9. Ignorado | todos |
| `pes` | `PES` | texto | Localização Pés. Localização do ferimento | 1. Sim 2. Não 9. Ignorado | todos |
| `tronco` | `TRONCO` | texto | Localização Tronco. Localização do ferimento | 1. Sim 2. Não 9. Ignorado | todos |
| `superiores` | `SUPERIORES` | texto | Localização Membros Superiores | 1. Sim 2. Não 9. Ignorado | todos |
| `inferiores` | `INFERIORES` | texto | Localização Membros Inferiores | 1. Sim 2. Não 9. Ignorado | todos |
| `feriment_n` | `FERIMENT_N` | texto | Ferimento. Quantidade de ferimentos no paciente | 1. único 2. múltiplo 3. sem ferimento 9. ignorado | todos |
| `profundo` | `PROFUNDO` | texto | Tipo de ferimento – Profundo. Informa se tipo de ferimento Profundo | 1. Sim 2. Não 9. Ignorado | todos |
| `superficia` | `SUPERFICIA` | texto | Tipo de ferimento – Superficial. Informa se tipo de ferimento Superficial | 1. Sim 2. Não 9. Ignorado | todos |
| `dilacerant` | `DILACERANT` | texto | Tipo de ferimento – Dilacerante. o | 1. Sim 2. Não 9. Ignorado | todos |
| `dt_expo` | `DT_EXPO` | data | Data da exposição. Data em que | — | todos |
| `antec_pre` | `ANTEC_PRE` | texto | Tem antecedentes de tratamento anti- rábico ? Pré-exposição | 1-Sim 2-Não 9-Ignorado | todos |
| `antec_pos` | `ANTEC_POS` | texto | Tem antecedentes de tratamento anti- rábico ? Pós-exposição | 1-Sim 2-Não 9-Ignorado | todos |
| `num_doses` | `NUM_DOSES` | inteiro | Número de doses aplicadas. Informa nºde doses aplicadas | — | todos |
| `dt_tr_rab` | `DT_TR_RAB` | data | Data da última dose | — | todos |
| `especie_n` | `ESPECIE_N` | texto | Espécie do animal agressor | 1. canina 2. felina 3. quiróptera(m orcego) 4. primata (macaco) 5. raposa 6. herbívora 7. outra 9. ignorada | todos |
| `esp_out` | `ESP_OUT` | texto | Espécie do animal agressor Outra, especificar. o | — | todos |
| `vacinad` | `VACINAD` | texto | Animal vacinado. Se o animal foi | 1. Sim | todos |
| `hospitaliz` | `HOSPITALIZ` | texto | Ocorreu hospitalização. Se ocorreu hospitalização do paciente | 1. Sim 2. Não 9. Ignorado | todos |
| `dt_interna` | `DT_INTERNA` | data | Data da internação. Data de internação, caso tenha ocorrido | — | todos |
| `uf_hospital` | `UF` | texto | UF do hospital de internação (coluna `UF` da fonte, renomeada pelo conversor porque `uf` é coluna do lake) | — | todos |
| `municipio` | `MUNICIPIO` | texto | Município do hospital. Nome completo do município onde o paciente foi internado | — | todos |
| `aerofobia` | `AEROFOBIA` | texto | Principais sinais/ sintomas Aerofobia. Se apresentou aerofobia | 1. Sim 2. Não 9. Ignorado | todos |
| `hidrofobi` | `HIDROFOBI` | texto | Principais sinais/ sintomas Hidrofobia. Se apresentou hidrofobia | 1. Sim 2. Não 9. Ignorado | todos |
| `disfagia` | `DISFAGIA` | texto | Principais sinais/ sintomas Disfagia. Se apresentou disfagia | 1. Sim 2. Não 9. Ignorado | todos |
| `parestesi` | `PARESTESI` | texto | Principais sinais/ sintomas Parestesia. Se apresentou parestesia | 1. Sim 2. Não 9. Ignorado | todos |
| `agressivi` | `AGRESSIVI` | texto | Principais sinais/ sintomas Agressividade. Se apresentou agressividade | 1. Sim 2. Não 9. Ignorado | todos |
| `paralisia` | `PARALISIA` | texto | Principais sinais/ sintomas Paralisia. Se apresentou paralisia | 1. Sim 2. Não 9. Ignorado | todos |
| `agitacao` | `AGITACAO` | texto | Principais sinais/ sintomas Agitação Psicomotora. Se apresentou agitação psicomotora | 1. Sim 2. Não 9. Ignorado | todos |
| `febre` | `FEBRE` | texto | Principais sinais/ sintomas Febre. Se apresentou febre | 1. Sim 2. Não 9. Ignorado | todos |
| `outro` | `OUTRO` | texto | Principais sinais/ sintomas Outro (s). Se apresentou outros sinais/ sintomas | 1. Sim 2. Não 9. Ignorado | todos |
| `outro_des` | `OUTRO_DES` | texto | Principais sinais/ sintomas Se Outro (s) especificar. Informa se apresentou outros sinais e sintomas | — | todos |
| `anti_rab` | `ANTI_RAB` | texto | Aplicação de vacina anti-rábica atualmente. Se o paciente foi submetido a tratamento anti- | 1. Sim 2. Não 9. Ignorado | todos |
| `dt_r_tra` | `DT_R_TRA` | data | Data do início do tratamento | — | todos |
| `doses_a` | `DOSES_A` | inteiro | Número de doses aplicadas. Número de doses aplicadas no tratamento | — | todos |
| `dt_vac1` | `DT_VAC1` | data | Data da 1ª dose da vacina. Data da primeira dose aplicada no tratamento | — | todos |
| `dt_vac_ult` | `DT_VAC_ULT` | data | Data da última dose da vacina. Data da última dose aplicada no tratamento | — | todos |
| `tra_soro` | `TRA_SORO` | texto | Foi aplicado soro?. Se foi aplicado o soro no tratamento | 1. Sim 2. Não 9. Ignorado | todos |
| `dt_apli_so` | `DT_APLI_SO` | data | Se sim, data da aplicação. Data da aplicação do soro | — | todos |
| `quantid` | `QUANTID` | inteiro | Quantidade de soro aplicada. Quantidade do soro aplicado em ml | — | todos |
| `infiltra` | `INFILTRA` | texto | Infiltração de soro no (s) local (ais) do (s) ferimento (s). Informa se houve infiltração no local do ferimento | 1. Sim total 2- Sim parcial 3. Não 9. Ignorado | todos |
| `imuno_dire` | `IMUNO_DIRE` | texto | Diagnóstico laboratorial – Imunofluorescência direta | 1. Positivo 2. Negativo 3.Inconclusivo 4. Não realizado | todos |
| `imuno_indi` | `IMUNO_INDI` | texto | Diagnóstico laboratorial – Imunofluorescência indireta. Se foi realizado exame de imunofluorescência indireta | 1. Positivo 2. Negativo 3.Inconclusivo 4. Não realizado | todos |
| `histolog_n` | `HISTOLOG_N` | texto | Diagnóstico laboratorial – Histológico. Se foi realizado exame histológico | 1. Positivo 2. Negativo 3.Inconclusivo 4. Não realizado | todos |
| `prova_biol` | `PROVA_BIOL` | texto | Diagnóstico laboratorial – Prova. Informa se foi realizada Prova | 1. Positivo 2. Negativo | todos |
| `varia_vir` | `VARIA_VIR` | inteiro | Variante. Informa qual variante foi identificada | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final | 1. Confirmado 2. Descartado | todos |
| `criterio` | `CRITERIO` | texto | Critério de confirmação/ descarte. Especifica o tipo de diagnóstico utilizado | 1. Laboratório 2. Óbito com clínica compatível + vínculo epidemiológico 3. Evolução clínica | todos |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência?. Indica se o caso é autóctone do município de residência | 1 – Sim 2 – Não 3 – Indeterminado | todos |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o paciente foi provavelmente infectado | — | todos |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente | — | todos |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). Código do município onde o paciente foi provavelmente infectado. O nome está associado ao código na tabela de municípios | — | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho. Informa se o paciente adquiriu a doença em decorrência das condições/ situação do trabalho | 1. Sim 2. Não 9. Ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Data do encerramento da investigação | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-raiv`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 19, inteiro: 5, texto: 72.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-raiv.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- volume mínimo (20 consolidações `BR` anuais, ~163 kB) — cada caso humano é um evento raro e muito investigado; cada leitura anual recupera casos confirmados dispersos em poucas UFs; casos registrados em município de internação podem divergir do município de residência (exposição rural), e o arquivo do ano corrente em `PRELIM` é sujeito a revisão. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-raiv").glob("**/*.parquet"))
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
datasus-fetcher list sinan-raiv

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-raiv -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-raiv
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Raiva Humana**: https://portalsinan.saude.gov.br/raiva-humana
- **Ficha de Investigação Raiva Humana (Raiva_v5)**: http://portalsinan.saude.gov.br/images/documentos/Agravos/Raiva%20Humana/Raiva_v5.pdf
- **Portaria GM/MS nº 204/2016**, **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo raiva; Programa Nacional de Profilaxia da Raiva
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
