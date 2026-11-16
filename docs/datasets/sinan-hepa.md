---
dataset:
  id: sinan-hepa
  fonte: datasus
  titulo: Hepatites Virais
  resumo: 'Hepatites Virais do DATASUS: uma ficha de notificação/investigação de hepatites Virais.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: '2023'
  unidade: uma ficha de notificação/investigação de hepatites Virais
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 82
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Hepatites Virais (`sinan-hepa`)

## Resumo

Notificações de hepatites virais (A, B, C, D e E) registradas no SINAN. Cada linha representa uma ficha de investigação de um caso suspeito ou confirmado de hepatite viral.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `HEPA` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `HEPA` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `HEPABR23.dbc`, em que `HEPA` é o prefixo do agravo, `BR` indica a base nacional (o SINAN publica um único arquivo por ano para o Brasil) e `23` é o ano com 2 dígitos (2023).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-hepa/<AAAA>/sinan-hepa_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-hepa/2024/sinan-hepa_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`):
  - `Docs_TAB_SINAN.zip` — pacote de documentação e dicionários para tabulação (~65 MB)
  - `Nota_Tecnica_Toxoplasmose.pdf` — nota técnica sobre toxoplasmose
  - `POP_I_Acesso_a_Microdados_5.pdf` — POP I: acesso a microdados
  - `POP_II_Descompactacao_expansao_conversao_3.pdf` — POP II: descompactação, expansão e conversão (.dbc → .dbf)
  - `POP_III_Instalacao_do_tabulador_TabWin_3.pdf` — POP III: instalação do TabWin
  - `Nota_Tecnica_Intoxicacao_Exogena.pdf` — nota técnica de intoxicação exógena (agravo de outro dataset do mesmo grupo)
  - Tabelas auxiliares (`/SINAN/AUXILIAR`):
  - `TAB_SINANNET.zip` — tabelas de conversão/tabulação (.cnv, .def) do SINAN Net (~44 MB)
  - `TAB_SINANONLINE.zip` — tabelas do SINAN Online (~240 KB)
  - `POPT_Estimativa_TCU_2019_Sinan.zip` — estimativas populacionais TCU 2019 para uso no SINAN
  - O dicionário de dados desta base (`Ficha de Investigação Hepatites Virais`) está contido em `Docs_TAB_SINAN.zip`; os dicionários por agravo não são publicados como arquivos separados.

## Conteúdo

As hepatites virais são de notificação compulsória e fazem parte do DATHI/SVSA do Ministério da Saúde. O SINAN usa uma ficha única para as cinco hepatites, e a etiologia (A, B, C, D ou E) é definida na classificação final com base em marcadores sorológicos e moleculares.

O evento gerador é a suspeita ou o diagnóstico de hepatite viral aguda ou crônica, notificado em ficha de investigação com campos de sintomas, fonte provável de infecção, exposições de risco e resultados laboratoriais (marcadores como HBsAg, anti-HBc IgM, anti-HCV, anti-HAV IgM). A unidade de análise é a notificação do caso.

O FTP traz arquivos nacionais anuais de 2007 a 2023 (cerca de 28 MB). O Boletim Epidemiológico de Hepatites Virais usa séries de detecção por etiologia e distingue casos agudos e crônicos.

Usos: taxa de detecção por etiologia, mortalidade por hepatite viral (com o SIM), fontes de infecção (alimentos, água, transmissão sexual, parenteral e vertical) e monitoramento da meta de eliminação das hepatites virais como problema de saúde pública.

### Cobertura observada

- Índice do FTP (2026-10): 17 arquivos, de 2007 a 2023, 1 UF(s) com arquivos, última atualização em 2025-03-26.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2023), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo real `HEPABR23.dbc` do FTP (campos da ficha do SINAN Net; o leiaute pode variar entre anos). Os microdados públicos não trazem número de notificação nem data de nascimento completa, apenas campos não identificáveis. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (individual ou negativa). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado. |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | Inteiro | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE). |
| `ID_REGIONA` | String | Regional de saúde de notificação. |
| `DT_DIAG` | Data (AAAAMMDD) | Data do diagnóstico. |
| `SEM_DIAG` | String | Semana epidemiológica do diagnóstico (AAAASS). |
| `NU_IDADE_N` | Inteiro codificado | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_GESTANT` | String | Gestante (trimestre de gestação ou não gestante, conforme a ficha). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade (código da ficha do SINAN). |
| `SG_UF` | String | UF de residência. |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `ID_RG_RESI` | String | Regional de saúde de residência. |
| `ID_PAIS` | String | País de residência. |
| `DT_INVEST` | Data (AAAAMMDD) | Data da investigação. |
| `ID_OCUPA_N` | String | Ocupação (CBO, 6 dígitos). |
| `HEPATITE_N` | String | Hepatite suspeita/classificada (indicador por tipo). |
| `HEPATITA` | String | Contato com caso de hepatite A. |
| `HEPATITB` | String | Contato com caso de hepatite B. |
| `SEXUAL` | String | Exposição sexual. |
| `DOMICILI` | String | Contato domiciliar. |
| `OCUPACIO` | String | Exposição ocupacional. |
| `MEDICAMENT` | String | Uso de medicamento injetável. |
| `TATU_PIER` | String | Tatuagem/piercing. |
| `TRANSFUSAO` | String | Transfusão. |
| `AGUA_ALIME` | String | Água/alimento contaminado. |
| `HEMODIALIS` | String | Hemodiálise. |
| `DT_ACIDENT` | Data (AAAAMMDD) | Data do acidente/exposição. |
| `CO_UF_EXP` | String | UF da exposição provável. |
| `CO_MUN_EXP` | String | Município da exposição provável (código IBGE). |
| `RES_HBSAG` | String | Resultado do HBsAg. |
| `RE_ANTIHBC` | String | Resultado do anti-HBc. |
| `RE_ANTIHCV` | String | Resultado do anti-HCV. |
| `DT_COLETA` | Data (AAAAMMDD) | Data da coleta. |
| `ANTIHAVIGM` | String | Resultado do anti-HAV IgM. |
| `ANTIHBCIGM` | String | Resultado do anti-HBc IgM. |
| `FONTE` | String | Fonte provável de infecção. |
| `DT_ENCERRA` | Data (AAAAMMDD) | Data de encerramento da investigação. |
| `CLASSI_FIN` | String | Classificação final do caso. |
| `FORMA` | String | Forma clínica da hepatite. |
| `HAV` | String | Indicador de hepatite A. |
| `HBV` | String | Indicador de hepatite B. |
| `HCV` | String | Indicador de hepatite C. |
| `HDV` | String | Indicador de hepatite D. |
| `HEV` | String | Indicador de hepatite E. |

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
| `dt_diag` | `DT_DIAG` | data | Data dos primeiros sintomas / Diagnóstico. Data dos primeiros sintomas do caso de agravo agudo. Data do diagnóstico do caso de agravo crônico e DRTs Data do acidente nos acidentes da saúde do trabalhador | — | todos |
| `sem_diag` | `SEM_DIAG` | texto | Semana epidemiológica dos primeiros sintomas/ diagnósticos. (campo interno). Semanas do calendário epidemiológico padronizado | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | texto | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil) | — | todos |
| `dt_invest` | `DT_INVEST` | data | Data de investigação. Data em que ocorreu o início da investigação do caso – informar a Data da 1ª visita ao paciente | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado ou aposentado. O ramo de atividade econômica do paciente refere-se as atividades econômicas desenvolvidas nos processos de produção do setor primário (agricultura e extrativismo); secundário (indústria) ou terciário (serviços e comércio) | — | todos |
| `hepatite_n` | `HEPATITE_N` | texto | Suspeita de. Informar de qual tipo de hepatite viral o paciente é suspeito | 1- Hepatite A 2- Hepatite B/C 3- Não especificada | todos |
| `hepatita` | `HEPATITA` | texto | Tomou vacina para Hepatite A. Informar se o paciente tem vacinação contra hepatite A com esquema completo, incompleto ou não vacinado comprovado no cartão de vacinação | 1-Completa 2-Incompleta 3-Não vacinado 9-Ignorado | todos |
| `hepatitb` | `HEPATITB` | texto | Tomou vacina para Hepatite B. Informar se o paciente tem vacinação contra hepatite B com esquema completo, incompleto ou não vacinado comprovado no cartão de vacinação | 1-Completa 2-Incompleta 3-Não vacinado 9-Ignorado | todos |
| `institucio` | `INSTITUCIO` | texto | Institucionalizado em. Informar se paciente é institucionalizado e em que tipo de instituição. Havendo mais de um tipo de instituição considerar o de maior tempo de permanência | 1. Creche 2. Escola 3. Asilo 4. Empresa 5. Penitenciária 6. Hospital/ Clínica 7. Outras 8. Não institucionalizado 9.Ignorado | todos |
| `hiv` | `HIV` | texto | Agravos associados: HIV/AIDS. Informar a presença de outros agravos já diagnosticados no paciente em qualquer momento da vida | 1. Sim 2. Não 9. Ignorado | todos |
| `outra_dst` | `OUTRA_DST` | texto | Agravos associados: Outras DSTs. Informar a presença de outros agravos já diagnosticados no paciente em qualquer momento da vida | 1. Sim 2. Não 9. Ignorado | todos |
| `sexual` | `SEXUAL` | texto | Contato com paciente portador de VHB ou VHC: sexual. Informar se paciente teve contato sexual com paciente com diagnóstico laboratorial específico de portador de VHB ou VHC e há quanto tempo (considerar a data da investigação como parâmetro) | 1. Sim há menos de 6 meses 2. Sim há mais de seis meses 3. Não 9- Ignorado | todos |
| `domicili` | `DOMICILI` | texto | Contato com paciente portador de VHB ou VHC: domiciliar (não sexual). Informar se paciente teve contato domiciliar não sexual com paciente com diagnóstico laboratorial específico de portador de VHB ou VHC e há quanto tempo (considerar a data da investigação como parâmetro) | 1. Sim há menos de 6 meses 2. Sim há mais de seis meses 3. Não 9- Ignorado | todos |
| `ocupacio` | `OCUPACIO` | texto | Contato com paciente portador de VHB ou VHC: ocupacional. Informar se paciente teve exposição ocupacional com paciente com diagnóstico laboratorial específico de portador de VHB ou VHC e há quanto tempo (considerar a data da investigação como parâmetro) | 1. Sim há menos de 6 meses 2. Sim há mais de seis meses 3. Não 9- Ignorado | todos |
| `medicament` | `MEDICAMENT` | texto | O paciente foi submetido ou exposto à: Medicamentos injetáveis. Informar se o paciente submeteu-se a situação de risco e há quanto tempo (considerar a data da investigação como parâmetro). Inclui-se no item Medicamentos Injetáveis quando o paciente usa ou tenha utilizado medicamentos injetáveis receitado por profissional ou não como energéticos (ex. gluconergan), anabolizantes, anfetaminas, etc | 1. Sim há menos de 6 meses 2. Sim há mais de seis meses 3. Não 9. Ignorado | todos |
| `tatu_pier` | `TATU_PIER` | texto | O paciente foi submetido ou exposto à: Tatuagem/ Piercing. Informar se o paciente submeteu-se a situação de risco e há quanto tempo (considerar a data da investigação como parâmetro) | 1. Sim há menos de 6 meses 2. Sim há mais de seis meses 3. Não 9- Ignorado | todos |
| `matbiologi` | `MATBIOLOGI` | texto | O paciente foi submetido ou exposto à: Acidente com Material Biológico. Informar se o paciente submeteu-se a situação de risco e há quanto tempo (considerar a data da investigação como parâmetro) | 1. Sim, há menos de 6 meses 2. Sim, há mais de seis meses 3. Não 9. Ignorado | todos |
| `inal_crack` | `INAL_CRACK` | texto | O paciente foi submetido ou exposto à: Drogas Inaláveis ou Crack.. Informar se o paciente submeteu-se a situação de risco e há quanto tempo (considerar a data da investigação como parâmetro). Inclui-se no ítem Drogas Inaláveis: cocaína inalável | 1. Sim há menos de 6 meses 2. Sim há mais de seis meses 3. Não 9. Ignorado | todos |
| `acupuntura` | `ACUPUNTURA` | texto | O paciente foi submetido ou exposto à: Acupuntura. Informar se o paciente submeteu-se a situação de risco e há quanto tempo (considerar a data da investigação como parâmetro) | 1. Sim, há menos de 6 meses 2. Sim, há mais de seis meses. 3. Não 9- Ignorado | todos |
| `transfusao` | `TRANSFUSAO` | texto | O paciente foi submetido ou exposto à: Transfusão de sangue/derivados. Informar se o paciente submeteu-se a situação de risco e há quanto tempo (considerar a data da investigação como parâmetro) | 1. Sim, há menos de 6 meses 2. Sim, há mais de seis meses 3. Não 9- Ignorado | todos |
| `injetaveis` | `INJETAVEIS` | texto | O paciente foi submetido ou exposto à: drogas injetáveis. Informar se o paciente submeteu-se a situação de risco e há quanto tempo (considerar a data da investigação como parâmetro). Inclui-se no ítem Drogas Injetáveis: silicone industrial, cocaína injetável, etc | 1. Sim, há menos de 6 meses 2- Sim, há mais de seis meses 3- Não 9- Ignorado | todos |
| `cirurgico` | `CIRURGICO` | texto | O paciente foi submetido ou exposto à: Tratamento cirúrgico. Informar se o paciente submeteu-se a situação de risco e há quanto tempo (considerar a data da investigação como parâmetro) | 1-Sim, há menos de 6 meses 2-Sim, há mais de seis meses 3-Não 9-Ignorado | todos |
| `agua_alime` | `AGUA_ALIME` | texto | O paciente foi submetido ou exposto à: Água/ Alimento contaminado. Informar se o paciente submeteu-se a situação de risco e há quanto tempo (considerar a data da investigação como parâmetro) | 1. Sim há menos de 6 meses 2. Sim há mais de seis meses 3. Não 9- Ignorado | todos |
| `dentario` | `DENTARIO` | texto | O paciente foi submetido ou exposto à: Tratamento dentário. Informar se o paciente submeteu-se a situação de risco e há quanto tempo (considerar a data da investigação como parâmetro) | 1. Sim, há menos de 6 meses 2. Sim, há mais de seis meses 3. Não 9- Ignorado | todos |
| `tresmais` | `TRESMAIS` | texto | O paciente foi submetido ou exposto à: Três ou mais parceiros sexuais. Informar se o paciente submeteu-se a situação de risco e há quanto tempo (considerar a data da investigação como parâmetro) | 1. Sim, há menos de 6 meses 2. Sim, há mais de seis meses 3. Não 9- Ignorado | todos |
| `hemodialis` | `HEMODIALIS` | texto | O paciente foi submetido ou exposto à: Hemodiálise. Informar se o paciente submeteu-se a situação de risco e há quanto tempo (considerar a data da investigação como parâmetro) | 1. Sim há menos de 6 meses 2. Sim há mais de seis meses 3. Não 9- Ignorado | todos |
| `transpla` | `TRANSPLA` | texto | O paciente foi submetido ou exposto à: Transplante. Informar se o paciente submeteu-se a situação de risco e há quanto tempo (considerar a data da investigação como parâmetro) | 1. Sim há menos de 6 meses 2. Sim há mais de seis meses 3. Não 9- Ignorado | todos |
| `outras` | `OUTRAS` | texto | O paciente foi submetido ou exposto à: Outras. Informar se o paciente submeteu-se outras situações de risco diferentes das existentes no campo, há quanto tempo. Se sim, especificar a situação. (considerar a data da investigação como parâmetro) | 1. Sim há menos de 6 meses 2. Sim há mais de seis meses 3. Não 9- Ignorado | todos |
| `dt_acident` | `DT_ACIDENT` | data | Data do Acidente ou Transfusão ou Transplante. Informar data do acidente com material biológico ou data da transfusão de sangue/derivados ou data do transplante | — | todos |
| `co_uf_exp` | `CO_UF_EXP` | texto | Local / Município da exposição: UF 1. Informar o Local/ Município de exposição. Atentar para a observação, caso seja suspeita de hepatite A anotar a UF, município, local /nome e telefone da instituição referenciada no campo 35. Caso seja suspeita de hepatite B/C, anotar a UF, município, local /nome e telefone do local onde paciente faz hemodiálise, recebeu transfusão de sangue/hemoderivados ou recebeu transplante | — | todos |
| `co_mun_exp` | `CO_MUN_EXP` | texto | Local / Município da exposição: Município 1. Informar o Local/ Município de exposição. Atentar para a observação, caso seja suspeita de hepatite A anotar a UF, município, local /nome e telefone da instituição referenciada no campo 35. Caso seja suspeita de hepatite B/C, anotar a UF, município, local /nome e telefone do local onde paciente faz hemodiálise, recebeu transfusão de sangue/hemoderivados ou recebeu trans... | — | todos |
| `co_uf_ex2` | `CO_UF_EX2` | texto | Local / Município da exposição: UF 2. Informar o Local/ Município de exposição. Atentar para a observação, caso seja suspeita de hepatite A anotar a UF, município, local /nome e telefone da instituição referenciada no campo 35. Caso seja suspeita de hepatite B/C, anotar a UF, município, local /nome e telefone do local onde paciente faz hemodiálise, recebeu transfusão de sangue/hemoderivados ou recebeu transplante | — | todos |
| `co_mun_ex2` | `CO_MUN_EX2` | texto | Local / Município da exposição: Município 2. Informar o Local/ Município de exposição. Atentar para a observação, caso seja suspeita de hepatite A anotar a UF, município, local /nome e telefone da instituição referenciada no campo 35. Caso seja suspeita de hepatite B/C, anotar a UF, município, local /nome e telefone do local onde paciente faz hemodiálise, recebeu transfusão de sangue/hemoderivados ou recebeu trans... | — | todos |
| `co_uf_ex3` | `CO_UF_EX3` | texto | Local / Município da exposição: UF 3. Informar o Local/ Município de exposição. Atentar para a observação, caso seja suspeita de hepatite A anotar a UF, município, local /nome e telefone da instituição referenciada no campo 35. Caso seja suspeita de hepatite B/C, anotar a UF, município, local /nome e telefone do local onde paciente faz hemodiálise, recebeu transfusão de sangue/hemoderivados ou recebeu transplante | — | todos |
| `co_mun_ex3` | `CO_MUN_EX3` | texto | Local / Município da exposição: Município 3. Informar o Local/ Município de exposição. Atentar para a observação, caso seja suspeita de hepatite A anotar a UF, município, local /nome e telefone da instituição referenciada no campo 35. Caso seja suspeita de hepatite B/C, anotar a UF, município, local /nome e telefone do local onde paciente faz hemodiálise, recebeu transfusão de sangue/hemoderivados ou recebeu trans... | — | todos |
| `bancosangu` | `BANCOSANGU` | texto | Paciente encaminhado de:. Informar se o paciente foi encaminhado à Unidade Notificadora pelo Serviço de Banco de Sangue ou Centro de Testagem e Aconselhamento | 1-Banco de Sangue 2-Centro de Testagem e Aconselhamento (CTA) 3-Não se aplica | todos |
| `res_hbsag` | `RES_HBSAG` | texto | Resultado da Sorologia do Banco de Sangue ou CTA: HBsAg. Informar resultado da sorologia (marcador HBsAg) realizada no Banco de Sangue ou Centro de Testagem e Aconselhamento | 1. Reagente 2. Não reagente 3. Inconclusivo 4. Não realizado 9. Ignorado | todos |
| `re_antihbc` | `RE_ANTIHBC` | texto | Resultado da Sorologia do Banco de Sangue ou CTA:: Anti-HBc total. Informar resultado da sorologia (marcador Anti-HBc total) realizada no Banco de Sangue ou Centro de Testagem e Aconselhamento | 1. Reagente 2. Não reagente 3. Inconclusivo 4. Não realizado 9. Ignorado | todos |
| `re_antihcv` | `RE_ANTIHCV` | texto | Resultado Resultado da Sorologia do Banco de Sangue ou CTA : Anti-HCV. Informar resultado da sorologia (marcador Anti-HCV) realizada no Banco de Sangue ou Centro de Testagem e Aconselhamento | 1. Reagente 2. Não reagente 3. Inconclusivo 4. Não realizado 9. Ignorado | todos |
| `dt_coleta` | `DT_COLETA` | data | Data da coleta da amostra realizada em Banco de Sangue ou CTA. Informar a dia, mês e ano da coleta da amostra para sorologia realizada no Banco de Sangue ou Centro de Testagem e Aconselhamento | — | todos |
| `antihavigm` | `ANTIHAVIGM` | texto | Resultados sorológicos/ virológicos: Anti- HAV IgM. Informar resultado da sorologia para marcador Anti -HAV IgM | 1. Reagente/Positivo 2. Não reagente/Negativo 3. Inconclusivo 4. Não realizado | todos |
| `antihbs` | `ANTIHBS` | texto | Resultados sorológicos / Virológicos: Anti- HBs. Informar resultado da sorologia para marcador Anti -HBs | 1. Reagente/Positivo 2. Não reagente/Negativo 3. Inconclusivo 4. Não realizado | todos |
| `antihdvigm` | `ANTIHDVIGM` | texto | Resultados sorológicos / Virológicos: Anti- HDV IgM. Informar resultado da sorologia para marcador Anti -HDV IgM | 1. Reagente 2. Não reagente 3. Inconclusivo 4. Não realizado | todos |
| `aghbs` | `AGHBS` | texto | Resultados sorológicos / Virológicos: HBsAg. Informar resultado da sorologia para marcador HBsAg | 1. Reagente/Positivo 2. Não reagente/Negativo 3. Inconclusivo 4. Não realizado | todos |
| `aghbe` | `AGHBE` | texto | Resultados sorológicos / Virológicos: HBeAg. Informar resultado da sorologia para marcador HBeAg | 1. Reagente/Positivo 2. Não reagente/Negativo 3. Inconclusivo 4. Não realizado | todos |
| `antihevigm` | `ANTIHEVIGM` | texto | Resultados sorológicos / Virológicos: Anti- HEV-IgM. Informar resultado da sorologia para marcador Anti - HEV IgM | 1. Reagente/Positivo 2. Não reagente/Negativo 3. Inconclusivo 4. Não realizado | todos |
| `antihbcigm` | `ANTIHBCIGM` | texto | Resultados sorológicos / Virológicos: Anti-HBc IgM. Informar resultado da sorologia para marcador Anti - HBc IgM | 1. Reagente/Positivo 2. Não reagente/Negativo 3. Inconclusivo 4. Não realizado | todos |
| `antihbe` | `ANTIHBE` | texto | Resultados sorológicos / Virológicos: Anti-HBe. Informar resultado da sorologia para marcador Anti - HBe | 1. Reagente/Positivo 2. Não reagente/Negativo 3. Inconclusivo 4. Não realizado | todos |
| `antihcv` | `ANTIHCV` | texto | Resultados sorológicos / Virológicos: Anti-HCV. Informar resultado da sorologia para marcador Anti - HCV | 1. Reagente/Positivo 2. Não reagente/Negativo 3. Inconclusivo 4. Não realizado | todos |
| `hbc_total` | `HBC_TOTAL` | texto | Resultados sorológicos / Virológicos: Anti-HBc total. Informar resultado da sorologia para marcador Anti - HBc (total) | 1. Reagente/Positivo 2. Não reagente/Negativo 3. Inconclusivo 4. Não realizado | todos |
| `antihdv` | `ANTIHDV` | texto | Resultados sorológicos / Virológicos: Anti- HDV total. Informar resultado da sorologia para marcador Anti r HDV total | 1. Reagente/Positivo 2. Não reagente/Negativo 3. Inconclusivo 4. Não realizado | todos |
| `tp_sorohcv` | `TP_SOROHCV` | texto | Marcadores sorológicos / Virológicos: HCV -RNA. Informar resultado de exame de biologia molecular HCV –RNA | 1- Reagente 2- Não reagente 3- Inconclusivo 4- Não realizado | todos |
| `gen_vhc` | `GEN_VHC` | texto | Genótipo para VHC. Informar o genótipo do VHC | 1. Genótipo 1 2. Genótipo 2 3. Genótipo 3 4. Genótipo 4 5. Genótipo 5 6. Genótipo 6 7. Não se aplica 9. Ignorado | todos |
| `coletamarc` | `COLETAMARC` | data | Data da coleta da sorologia. Informar o dia, mês e ano da coleta da amostra para sorologia realizada na ocasião da investigação | — | todos |
| `fonte` | `FONTE` | texto | Provável Fonte/ Mecanismo de infecção. Informar a provável fonte de infecção ou mecanismo de infecção | 1. Sexual 2. Transfusional 3. Uso de Drogas 4. Vertical 5. Acidente de Trabalho 6. Hemodiálise 7. Domiciliar 8. Tratamento cirúrgico 9. Tratamento dentário 10. Pessoa/pessoa 11. Alimento/água contaminada 12. Outros 99... | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do encerramento. Informar dia, mês e ano da data do encerramento do caso | — | todos |
| `dsfonte` | `DSFONTE` | texto | Provavel Fonte / Mecanismo de Infecção - Outros. Varcahar(30) | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final | — | todos |
| `forma` | `FORMA` | texto | Especificar forma clínica. Informar no quadrado do campo 43 os CÓDIGOS 1 se a classificação da forma anátomo-clínica for intestinal, 2 se a forma hepato intestinal, 3 se hepato esplênica, 4 se foram aguda 3 5 para outra forma | 1. Intestinal 2. Hepato intestinal 3. Hepato esplênica 4. Aguda 5. Outra, | todos |
| `hav` | `HAV` | texto | Resultado do marcador do vírus da hepatite A (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `hbv` | `HBV` | texto | Resultado do marcador do vírus da hepatite B (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `hcv` | `HCV` | texto | Resultado do marcador do vírus da hepatite C (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `hdv` | `HDV` | texto | Resultado do marcador do vírus da hepatite D (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `hev` | `HEV` | texto | Resultado do marcador do vírus da hepatite E (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-hepa`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 7, texto: 75.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-hepa.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- Uma única ficha cobre cinco doenças com histórias naturais diferentes; filtrar sempre por etiologia e por forma clínica (aguda/crônica) antes de calcular indicadores. Casos crônicos de hepatite B e C têm componente de notificação acumulada ao longo dos anos. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (UF de notificação) ou `SG_UF`/`ID_MN_RESI` (residência) conforme a pergunta, pois os dois podem diferir. Arquivos do diretório PRELIM são preliminares e substituídos pelos finais; prefira sempre os arquivos finais quando o mesmo ano existir nas duas fontes, evitando somar PRELIM e FINAIS. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-hepa").glob("**/*.parquet"))
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
datasus-fetcher list sinan-hepa

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-hepa -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-hepa
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Boletim Epidemiológico de Hepatites Virais (SVSA/MS): https://www.gov.br/aids/pt-br/centrais-de-conteudo/boletins-epidemiologicos
- Guia de Vigilância em Saúde (SVSA/MS): https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
