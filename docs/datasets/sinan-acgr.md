---
dataset:
  id: sinan-acgr
  fonte: datasus
  titulo: Acidente de trabalho
  resumo: Notificações de acidentes de trabalho graves e fatais — aqueles que resultam em óbito, mutilação, internação ou que ocorrem com menores de 18 anos — registrados no SINAN.
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2006'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de acidente de trabalho
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 56
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Acidente de trabalho (`sinan-acgr`)

## Resumo

Notificações de acidentes de trabalho graves e fatais — aqueles que resultam em óbito, mutilação, internação ou que ocorrem com menores de 18 anos — registrados no SINAN. Cada linha representa uma ficha de investigação de acidente de trabalho, com dados do trabalhador, da empresa contratante e da lesão.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (dBASE comprimido)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2006 a 2026 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 21 arquivos (~176,9 MB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim (diretório PRELIM, 2023–2026; Finais até 2022)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ACGR` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ACGR` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `ACGRBR24.dbc`, em que `ACGR` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024, preliminar).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-acgr/<partição>/sinan-acgr_br_2006_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`, `Nota_Tecnica_Doenca_de_Creutzfeldt-Jakob(DCJ).pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`DRT Acidente Trabalho Grave`) é distribuído no Portal SINAN; não há PDF por agravo no FTP.

## Conteúdo

O agravo integra a vigilância em Saúde do Trabalhador do SUS, sob responsabilidade da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), operacionalizada pela Rede Nacional de Atenção Integral à Saúde do Trabalhador (RENAST) e pelos Centros de Referência em Saúde do Trabalhador (CEREST). A notificação compulsória foi estabelecida pela Portaria MS nº 777/2004 e consolidada na Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V).

O evento gerador é todo acidente de trabalho por causas não naturais (Capítulo XX da CID-10, V01 a Y98), típico ou de trajeto, que provoque lesão corporal ou perturbação funcional com perda/redução da capacidade para o trabalho, hospitalização ou morte. Consideram-se graves os acidentes fatais, com mutilações (poli traumatismos, amputações, esmagamentos, TCE, fratura de coluna, lesão medular, trauma visceral, eletrocussão, asfixia, queimaduras e aborto) e os ocorridos com menores de 18 anos. A unidade de análise é o trabalhador acidentado notificado (um registro por ficha), com o CID-10 da causa (V01–Y98) e o CID-10 da lesão registrados separadamente.

O instrumento é a *Ficha de Investigação — Acidente de Trabalho Grave* (CID-10 Y96), que cobre identificação, residência, antecedentes ocupacionais (CBO, situação no mercado de trabalho, tempo na ocupação), dados da empresa contratante (CNPJ/CPF, CNAE, terceirização), características do acidente (hora, horas após a jornada, local, tipo, veículo, outros trabalhadores atingidos) e conclusão (diagnóstico, regime de tratamento, evolução e CAT). A série no FTP inicia em 2006, no bojo da implantação nacional do SINAN Net; dados de 2023 em diante estão em PRELIM e sujeitos a revisão.

Principais usos: incidência e mortalidade por acidentes de trabalho graves, análise por ramo de atividade econômica (CNAE) e ocupação (CBO), avaliação da emissão de CAT, identificação de setores críticos para intervenção de VISAT (Vigilância em Saúde do Trabalhador) e apoio à rede sentinela.

### Cobertura observada

- Índice do FTP (2026-10): 21 arquivos, de 2006 a 2026, 1 UF(s) com arquivos, última atualização em 2026-10-23.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2006 a 2023), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo `ACGRBR09.dbc` (leiaute do SINAN Net; fichas e leiautes podem variar entre anos, por isso a lista reflete esse arquivo). Os arquivos públicos não trazem identificadores individuais como número da notificação (`NU_NOTIFIC`) nem data de nascimento completa. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

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
| `DT_ACID` | Data (AAAAMMDD) | Data do acidente. |
| `SEM_ACID` | String | Semana epidemiológica do acidente (AAAASS). |
| `ANO_NASC` | String | Ano de nascimento (o arquivo público não traz a data de nascimento completa). |
| `NU_IDADE_N` | Inteiro | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade. |
| `SG_UF` | String | UF de residência (código IBGE de 2 dígitos). |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `ID_OCUPA_N` | String | Ocupação do trabalhador (CBO 2002, 6 dígitos). |
| `SIT_TRAB` | String | Situação no mercado de trabalho. |
| `LOCAL_ACID` | String | Local onde ocorreu o acidente. |
| `CNAE` | String | Atividade econômica da empresa contratante (CNAE). |
| `CNAE_PRIN` | String | CNAE da atividade principal da empresa. |
| `HORA_ACID` | String | Hora do acidente. |
| `MIN_ACID` | String | Minuto do acidente. |
| `HORA_JOR` | String | Hora da jornada de trabalho em que ocorreu o acidente. |
| `MIN_JOR` | String | Minuto da jornada de trabalho. |
| `UF_ACID` | String | UF de ocorrência do acidente. |
| `MUN_ACID` | String | Município de ocorrência do acidente. |
| `CID_ACID` | String | Código CID-10 da causa externa do acidente. |
| `TIPO_ACID` | String | Tipo de acidente (típico ou de trajeto). |
| `MAIS_TRAB` | String | Acidente atingiu mais de um trabalhador. |
| `NU_TRAB` | String | Número de trabalhadores atingidos. |
| `ATENDE_MED` | String | Houve atendimento médico. |
| `DT_ATENDE` | Data (AAAAMMDD) | Data do atendimento médico. |
| `UF_ATENDE` | String | UF da unidade de atendimento. |
| `MUN_ATENDE` | String | Município da unidade de atendimento. |
| `UNI_ATENDE` | String | Código CNES da unidade de atendimento. |
| `PART_CORP1` | String | Parte do corpo atingida (1ª). |
| `PART_CORP2` | String | Parte do corpo atingida (2ª). |
| `PART_CORP3` | String | Parte do corpo atingida (3ª). |
| `CID_LESAO` | String | Código CID-10 da lesão (diagnóstico). |
| `REGIME` | String | Regime de tratamento (hospitalar, ambulatorial ou ambos). |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito, quando aplicável. |
| `CAT` | String | Foi emitida a Comunicação de Acidente do Trabalho (CAT)? |

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
| `dt_acid` | `DT_ACID` | data | Data do acidente | — | todos |
| `sem_acid` | `SEM_ACID` | texto | Semana epidemiológica do acidente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
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
| `sit_trab` | `SIT_TRAB` | texto | Situação no mercado de trabalho. Situação de trabalho do indivíduo que sofreu o agravo | 01. Empregado registrado com carteira assinada 02. Empregado não registrado 03. Autônomo/conta própria 04. Servidor público estatuário 05. Servidor público | todos |
| `nutempo` | `NUTEMPO` | texto | Número que compõe o tempo (de exposição ou de ocorrência); a unidade está em `tptempo` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tptempo` | `TPTEMPO` | texto | Unidade do tempo informado em `nutempo` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `local_acid` | `LOCAL_ACID` | texto | Local onde ocorreu o acidente | 1 – Instalações do Contratante 2 – Via Pública 3 – Instalações de terceiros 4 – Domicílio próprio 9 – Ignorado | todos |
| `cnae` | `CNAE` | texto | Código da atividade Econômica(CNAE). Classificação Nacional da Atividade Econômica do Contratante | — | todos |
| `uf_emp` | `UF_EMP` | texto | UF. Unidade da Federação da empresa contratante | — | todos |
| `mun_emp` | `MUN_EMP` | texto | Município. Código (IBGE) | — | todos |
| `terceiriza` | `TERCEIRIZA` | texto | O empregador é empresa Terceirizada. O empregador é de alguma empresa terceirizada | 01- Sim 02- Não 03- Não se aplica 09- Ignorado | todos |
| `cnae_prin` | `CNAE_PRIN` | texto | Se empresa terceirizada, Qual o CNAE da empresa terceirizada. Habilitar se campo 46 - O empregador é empresa terceirizada = 1 | — | todos |
| `hora_acid` | `HORA_ACID` | texto | Hora do Acidente. H (Hora) | — | todos |
| `min_acid` | `MIN_ACID` | texto | Minutos do Acidente. M(Minutos) | — | todos |
| `hora_jor` | `HORA_JOR` | texto | Horas após início da jornada. H (Hora) | — | todos |
| `min_jor` | `MIN_JOR` | texto | Minutos após início da jornada. M (Minutos) | — | todos |
| `uf_acid` | `UF_ACID` | texto | UF. Unidade Federativa do local do acidente | — | todos |
| `mun_acid` | `MUN_ACID` | texto | Município de ocorrência do acidente. Município onde ocorreu o acidente | — | todos |
| `cid_acid` | `CID_ACID` | texto | Código da Causa do Acidente CID 10 (de V01 a Y98) CID 10 | — | todos |
| `tipo_acid` | `TIPO_ACID` | texto | Tipo de Acidente | 1 – Típico 2 – Trajeto 9 – Ignorado | todos |
| `mais_trab` | `MAIS_TRAB` | texto | Houve Outros Trabalhadores Atingidos? | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `nu_trab` | `NU_TRAB` | texto | Se Sim, Quantos | — | todos |
| `atende_med` | `ATENDE_MED` | texto | Ocorreu Atendimento Médico ? | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `dt_atende` | `DT_ATENDE` | data | Data do Atendimento | — | todos |
| `uf_atende` | `UF_ATENDE` | texto | UF. Unidade Federativa do local do atendimento | — | todos |
| `mun_atende` | `MUN_ATENDE` | texto | Município do Atendimento | — | todos |
| `uni_atende` | `UNI_ATENDE` | texto | Nome da Unidade de Saúde de Atendimento | — | todos |
| `part_corp1` | `PART_CORP1` | texto | Partes do corpo atingida 1. Parte do corpo atingida no acidente – 1 | 01- Olho 02- Cabeça 03- Pescoço 04- Tórax 05- Abdome 06- Mão 07- Membro superior 08- Membro inferior 09- Pé 10- Todo o corpo 11- Outro 99- Ignorado | todos |
| `part_corp2` | `PART_CORP2` | texto | Partes do Corpo Atingida 2 | 01-Olho 02-Cabeça 03-Pescoço | todos |
| `part_corp3` | `PART_CORP3` | texto | Partes do Corpo Atingida 3 | 01-Olho 02-Cabeça 03-Pescoço 04-Tórax 05-Abdome 06-Mão 07-Membro superior 08-Membro inferior 09-Pé 10-Todo o corpo 11-Outro 99- Ignorado | todos |
| `cid_lesao` | `CID_LESAO` | texto | Diagnóstico da lesão CID 10 | — | todos |
| `regime` | `REGIME` | texto | Regime de Tratamento | 1 – Hospitalar 2 – Ambulatório 3 – Ambos 9 – Ignorado | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso | 1 – Cura 2 – Incapacidade temporária 3 – Incapacidade parcial permanente 4 – Incapacidade total permanente 5 – Óbito por acidente de trabalho grave 6 – Óbito por outras | todos |
| `dt_obito` | `DT_OBITO` | data | Se Óbito, Data do Óbito | — | todos |
| `cat` | `CAT` | texto | Foi emitida a Comunicação de Acidente no Trabalho - CAT | 1 – Sim 2 – Não 3 – Não se aplica 9 – Ignorado | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-acgr`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 4, inteiro: 1, texto: 51.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-acgr.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- este dataset cobre apenas acidentes graves/fatais; acidentes com material biológico estão em `sinan-acbi` e acidentes leves não são notificados no SINAN. O `CID_ACID` (causa, V01–Y98) não deve ser confundido com o diagnóstico da lesão (campo de diagnóstico, CID-10 de lesão). Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. Arquivos do diretório PRELIM (2023+) são preliminares; como `NU_NOTIFIC` não consta dos arquivos públicos, deduplique por combinação de campos (ex.: `ID_UNIDADE`, `DT_NOTIFIC`, `ID_MN_RESI`, `ANO_NASC`, `CS_SEXO`) ao combinar as duas fontes. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-acgr/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-acgr
quantilica datasus list sinan-acgr

# 2. Baixar microdados de sinan-acgr (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-acgr -o ./data --start 2020 --end 2022 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-acgr -o ./data --docs --aux --start 2020 --end 2022 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-acgr -o ./data/raw --parquet-dir ./data/parquet --start 2020 --end 2022 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/ACGRBR22.dbc", dataset="sinan-acgr")

# Notificações por UF e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Tipos de acidente e evolução
print(frame.group_by("tipo_acid").agg(pl.len().alias("n")).sort("n", descending=True))
print(frame.group_by("evolucao").agg(pl.len().alias("n")).sort("n", descending=True))
print(resumo.head())
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (DRT Acidente de Trabalho Grave): https://portalsinan.saude.gov.br/drt-acidente-de-trabalho-grave
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Saúde do Trabalhador: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- RENAST — Rede Nacional de Atenção Integral à Saúde do Trabalhador: https://www.gov.br/saude/pt-br/composicao/svsa/saude-do-trabalhador/renast
