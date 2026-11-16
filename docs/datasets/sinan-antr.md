---
dataset:
  id: sinan-antr
  fonte: datasus
  titulo: Atendimento Antirrábico
  resumo: 'Atendimento Antirrábico do DATASUS: uma ficha de notificação/investigação de atendimento Antirrábico.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2006'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de atendimento Antirrábico
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 90
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  - coluna: id_cns_sus
    categoria: Cartão Nacional de Saúde (CNS)
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Atendimento Antirrábico (`sinan-antr`)

## Resumo

O `sinan-antr` contém os microdados dos atendimentos antirrábicos humanos registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação de um atendimento antirrábico humano (CID-10 W64 — "exposição a vírus da raiva"), a ficha de "acidente por animal potencialmente transmissor de raiva" ou de atendimento profilático, digitado no SINAN Net/Sinan Online pelas unidades de saúde que prestam o atendimento. O agravo é de notificação compulsória: todo acidente por animal potencialmente transmissor da raiva deve ser notificado, independentemente da indicação de vacina ou soro.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ANTR` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ANTR` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `ANTRBR06.dbc` — prefixo `ANTR`, `BR` (consolidação nacional) e `06` (ano 2006, início da série disponível), até `ANTRBR24.dbc` (2024); os anos recentes ficam em `PRELIM` (ex.: `ANTRBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-antr/<AAAA>/sinan-antr_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-antr/2024/sinan-antr_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## Conteúdo

O atendimento antirrábico é a ponta do programa de profilaxia da raiva humana, gerido pela SVSA/MS: todo acidente com animal potencialmente transmissor da raiva (mordedura, arranhadura, lambedura) tem notificação compulsória (Portaria SVS/MS nº 104/2011; Portaria de Consolidação GM/MS nº 204/2016), inclusive acidentes em que o animal é cão ou gato em observação. A sistemática substituiu o antigo SISANTO (sistema dedicado de atendimento antirrábico) e atualmente é alimentada pela **Ficha de Investigação Atendimento Antirrábico Humano** do SINAN (ficha `anti_rabico_v5`, com dicionário `DIC_DADOS_anti_rabico_v5.1`). O volume é alto em todas as UFs — dezenas de milhares de atendimentos anuais — porque envolve profilaxia pré-exposição (vacinadores de produtos animais) e pós-exposição de todo o território.

O evento gerador é a ficha de atendimento antirrábico humano, composta pelo bloco de notificação individual (dados gerais padrão do SINAN) e por dados complementares: tipo de exposição (mordedura, arranhadura, lambedura, contato indireto), localização do ferimento, animal agressor (espécie, passível de observação, situação final do animal após o período observado), tratamento indicado (1 - Pré-exposição, 2 - Dispensa de tratamento, 3 - Observação do animal, 4/5/6 - Soro, vacina, soro + vacina, 7 - Reexposição), doses aplicadas, laboratório produtor da vacina/soro e evento adverso. A unidade de análise é o atendimento/notificação individual — não o caso de raiva humana (que deve estudado no dataset `sinan-raiv`).

A implantação no SINAN data das décadas (dados liberalizados de 2006 em diante no FTP com a base nacional `BR`); a migração do SISANTO para o SINAN consolidou o registro único entre atendimento profilático pós-exposição e pré-exposição, com acompanhamento do esquema profilático por ficha ou transferência vertical entre atendimentos do mesmo paciente.

Aplicações analíticas: volume e distribuição de atendimentos antirrábicos por UF/município, perfil de exposição (tipo de exposição, espécie de animal agressor, condição do animal), razões de esquema aplicado vs. indicado, doses aplicadas e eventos adversos, monitoramento da vigilância passiva (animais observados), e análise de integração com epizootias e casos humanos de raiva (`sinan-raiv`).

### Cobertura observada

- Índice do FTP (2026-10): 21 arquivos, de 2006 a 2026, 1 UF(s) com arquivos, última atualização em 2026-10-13.
- Conversão local de amostras (2 arquivo(s) Parquet, de 2006 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Atendimento Antirrábico Humano — CID-10 W64) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora/unidade de atendimento |
| `DT_ATEND` | Data (`AAAAMMDD`) | Data do atendimento (primeiro atendimento antirrábico) |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `ID_OCUPA_C` | String (6) | Ocupação do paciente, em código CBO (atividades de risco, ex.: profissionais de zoonoses e veterinária) |
| `ID_MN_RESI` | String (6/7) | Município de residência do paciente (IBGE) |
| `SG_UF_ATEND` | String (2) | UF da unidade de atendimento antirrábico |
| `CLASSI_FIN` | Inteiro | Classificação final/condição (conforme dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação/despistos quando aplicável |
| `EVOLUCAO` | Inteiro | Evolução/desfecho do atendimento (conforme dicionário do agravo) |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento |
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
| `id_cns_sus` | `ID_CNS_SUS` | texto | Nº. Cartão SUS. Número do cartão do Sistema Único de Saúde (SUS) do paciente | — | só em 2006 |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil) | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/ Ramo de atividade. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo de atividade | — | todos |
| `ant_contat` | `ANT_CONTAT` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_CONTAT`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_arranh` | `ANT_ARRANH` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_ARRANH`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_lambed` | `ANT_LAMBED` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_LAMBED`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_morded` | `ANT_MORDED` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_MORDED`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_outro_` | `ANT_OUTRO_` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_OUTRO_`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_mucosa` | `ANT_MUCOSA` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_MUCOSA`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_cabeca` | `ANT_CABECA` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_CABECA`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_maos` | `ANT_MAOS` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_MAOS`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_tronco` | `ANT_TRONCO` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_TRONCO`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_membro` | `ANT_MEMBRO` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_MEMBRO`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_memb_1` | `ANT_MEMB_1` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_MEMB_1`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ferimento` | `FERIMENTO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `ant_profun` | `ANT_PROFUN` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_PROFUN`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_superf` | `ANT_SUPERF` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_SUPERF`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_dilace` | `ANT_DILACE` | texto | Antecedente epidemiológico ou exposição registrado na ficha de Atendimento Antirrábico (`ANT_DILACE`); o dicionário consultado não define o campo isoladamente | — | todos |
| `ant_dt_exp` | `ANT_DT_EXP` | data | Data da exposição | — | todos |
| `pre_expos` | `PRE_EXPOS` | texto | Profilaxia antirrábica pré-exposição (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `pos_expos` | `POS_EXPOS` | texto | Profilaxia antirrábica pós-exposição (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tra_antigo` | `TRA_ANTIGO` | texto | Dado do inquérito/tratamento de tracoma (`TRA_ANTIGO`) | — | todos |
| `doses` | `DOSES` | texto | Registro de vacinação (`DOSES`) | — | todos |
| `animal` | `ANIMAL` | texto | Animal envolvido (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `herbiv_des` | `HERBIV_DES` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `outro_des` | `OUTRO_DES` | texto | Principais sinais/ sintomas Se Outro (s) especificar. Informa se apresentou outros sinais e sintomas | — | todos |
| `condic_ani` | `CONDIC_ANI` | texto | Condição do animal agressor (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `observacao` | `OBSERVACAO` | texto | Observações da ficha (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `trat_atual` | `TRAT_ATUAL` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `lab_vacina` | `LAB_VACINA` | texto | Dado de exame laboratorial registrado na ficha de Atendimento Antirrábico (`LAB_VACINA`); o dicionário consultado não define o campo isoladamente | — | todos |
| `lab_vac_de` | `LAB_VAC_DE` | texto | Dado de exame laboratorial registrado na ficha de Atendimento Antirrábico (`LAB_VAC_DE`); o dicionário consultado não define o campo isoladamente | — | todos |
| `lote_vac` | `LOTE_VAC` | texto | Lote da vacina (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_vencim` | `DT_VENCIM` | data | Data de vencimento (do lote da vacina ou do soro) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_dose_1` | `DT_DOSE_1` | texto | Registro de vacinação (`DT_DOSE_1`) | — | todos |
| `dt_dose_2` | `DT_DOSE_2` | texto | Registro de vacinação (`DT_DOSE_2`) | — | todos |
| `dt_dose_3` | `DT_DOSE_3` | texto | Registro de vacinação (`DT_DOSE_3`) | — | todos |
| `dt_dose_4` | `DT_DOSE_4` | texto | Registro de vacinação (`DT_DOSE_4`) | — | todos |
| `dt_dose_5` | `DT_DOSE_5` | texto | Registro de vacinação (`DT_DOSE_5`) | — | todos |
| `dt_vac_1` | `DT_VAC_1` | data | Registro de vacinação (`DT_VAC_1`) | — | todos |
| `dt_vac_2` | `DT_VAC_2` | data | Registro de vacinação (`DT_VAC_2`) | — | todos |
| `dt_vac_3` | `DT_VAC_3` | data | Registro de vacinação (`DT_VAC_3`) | — | todos |
| `dt_vac_4` | `DT_VAC_4` | data | Registro de vacinação (`DT_VAC_4`) | — | todos |
| `dt_vac_5` | `DT_VAC_5` | data | Registro de vacinação (`DT_VAC_5`) | — | todos |
| `fim_animal` | `FIM_ANIMAL` | texto | Situação do animal ao fim da observação (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tra_interr` | `TRA_INTERR` | texto | Dado do inquérito/tratamento de tracoma (`TRA_INTERR`) | — | todos |
| `tra_motivo` | `TRA_MOTIVO` | texto | Dado do inquérito/tratamento de tracoma (`TRA_MOTIVO`) | — | todos |
| `busca_ativ` | `BUSCA_ATIV` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `reacao_vac` | `REACAO_VAC` | texto | Dado de exame laboratorial registrado na ficha de Atendimento Antirrábico (`REACAO_VAC`); o dicionário consultado não define o campo isoladamente | — | todos |
| `tra_indi_n` | `TRA_INDI_N` | texto | Dado do inquérito/tratamento de tracoma (`TRA_INDI_N`) | — | todos |
| `tra_peso` | `TRA_PESO` | texto | Peso. Informar o peso do paciente em Kg | — | todos |
| `tra_qtd_so` | `TRA_QTD_SO` | texto | Dado do inquérito/tratamento de tracoma (`TRA_QTD_SO`) | — | todos |
| `tip_soro` | `TIP_SORO` | texto | Tipo de soro antirrábico (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tra_infilt` | `TRA_INFILT` | texto | Dado do inquérito/tratamento de tracoma (`TRA_INFILT`) | — | todos |
| `tra_infi_1` | `TRA_INFI_1` | texto | Dado do inquérito/tratamento de tracoma (`TRA_INFI_1`) | — | todos |
| `lab_soro` | `LAB_SORO` | texto | Dado de exame laboratorial registrado na ficha de Atendimento Antirrábico (`LAB_SORO`); o dicionário consultado não define o campo isoladamente | — | todos |
| `lab_sor_de` | `LAB_SOR_DE` | texto | Dado de exame laboratorial registrado na ficha de Atendimento Antirrábico (`LAB_SOR_DE`); o dicionário consultado não define o campo isoladamente | — | todos |
| `tra_num_pa` | `TRA_NUM_PA` | texto | Dado do inquérito/tratamento de tracoma (`TRA_NUM_PA`) | — | todos |
| `reacao_sor` | `REACAO_SOR` | texto | Dado de exame laboratorial registrado na ficha de Atendimento Antirrábico (`REACAO_SOR`); o dicionário consultado não define o campo isoladamente | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Data do encerramento da investigação | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | só em 2006 |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | só em 2006 |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | só em 2006 |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | só em 2006 |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | só em 2006 |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | só em 2006 |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | só em 2006 |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | só em 2006 |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-antr`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 17, inteiro: 1, texto: 72.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-antr.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- volume muito alto (21 consolidações anuais, ~513 MB) — atenção ao registro múltiplo de fichas do mesmo paciente ao longo do esquema profilático (a mesma pessoa pode ter vários atendimentos; use `NU_NOTIFIC`, a transferência vertical de lote e `DT_NOTIF` para ordenação); o esquema pode ser interrompido/encerrado antes do fim (ex.: animal observado sadio após 90 dias); cães e gatos em observação geram atendimentos de observação/dispensa sem aplicação de vacina; partes consideráveis dos registros misturam profilaxia pré-exposição (ocupacional) com pós-exposição, que exigem tratamento distinto nas análises. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 9 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-antr").glob("**/*.parquet"))
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
datasus-fetcher list sinan-antr

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-antr -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-antr
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Atendimento Antirrábico (ficha, instrucional, dicionário)**: https://portalsinan.saude.gov.br/atendimento-antirrabico
- **Ficha de Investigação Atendimento Antirrábico Humano (anti_rabico_v5)**: http://portalsinan.saude.gov.br/images/documentos/Agravos/Atendimento%20Anti-rabico/anti_rabico_v5.pdf
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo raiva / profilaxia antirrábica
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
