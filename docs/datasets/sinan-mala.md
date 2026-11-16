---
dataset:
  id: sinan-mala
  fonte: datasus
  titulo: Malária
  resumo: O sinan-mala contém os microdados das notificações e investigações de casos de Malária (CID-10 B50-B54) registrados no Sistema de Informação de Agravos de Notificação (SINAN).
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2004'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de malária
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 104
  unidades_de_medida:
    pmm: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Malária (`sinan-mala`)

## Resumo

O `sinan-mala` contém os microdados das notificações e investigações de casos de Malária (CID-10 B50-B54) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de malária digitado no SINAN Net/Sinan Online. Importante: a base SINAN cobre primordialmente a malária extra-amazônica, pois os casos das unidades federadas da Amazônia Legal são registrados no SIVEP-Malária — o SINAN observa o padrão de vigilância fora dessa região.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2004 a 2026 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 23 arquivos (~2,9 MB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim (diretório `PRELIM`)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `MALA` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `MALA` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `MALABR04.dbc` — prefixo `MALA`, `BR` (consolidação nacional) e `04` (ano 2004, primeiro ano da série do SINAN no FTP); a série de arquivos finais vai até `MALABR23.dbc` (2023), com os anos recentes em `PRELIM` (ex.: `MALABR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-mala/<ano>/sinan-mala_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-mala/2023/sinan-mala_2023-br@20260831.dbc`; o dataset também mantém a variante `-preliminar` para os arquivos do `PRELIM`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/descompactação/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## Conteúdo

A malária é uma doença parasitária causada por plasmódios (*Plasmodium falciparum*, *P. vivax*, *P. malariae* e, mais recentemente, *P. knowlesi*), transmitida pela picada do mosquito *Anopheles* e considerada doença prioritária do cenário de eliminação nacional. A vigilância é híbrida: a Portaria SVS/MS nº 104/2011 (hoje consubstanciada na Portaria de Consolidação GM/MS nº 204/2016) determinou que os casos de malária na Região da Amazônia Legal (Acre, Amapá, Amazonas, Maranhão, Mato Grosso, Pará, Rondônia, Roraima e Tocantins) sejam registrados no **SIVEP-Malária**, enquanto a malária **extra-amazônica** deve ser notificada no **SINAN**. O FTP do DATASUS, no entanto, divulga a consolidação nacional `BR` da base SINAN, que concentra sobretudo a malária registrada fora da Amazônia Legal, além de remanescentes de notificação polinomiais da série histórica.

O evento gerador neste dataset é a **Ficha de Notificação/Investigação de Malária do SINAN** (ficha `Malaria_v5`). A unidade de análise é o caso suspeito/confirmado notificado individualmente, com confirmação por exame do tipo de plasmódio (gota espessa/lâmina delgada ou teste rápido TDR) registrada na investigação. A notificação é compulsória em todo o território nacional mediante confirmação, com o caso classificado por espécie infectante.

Aplicações analíticas: coeficiente parasitário anual (casos confirmados por 10 mil habitantes) especialmente em territórios extra-amazônicos, distribuição por espécie infectante, vigilância de casos importados/viajantes e de reintroduções em áreas de fronteira, letalidade da *P. falciparum*, e análises de integração com a base do SIVEP-Malária.

### Cobertura observada

- Índice do FTP (2026-10): 23 arquivos, de 2004 a 2026, 1 UF(s) com arquivos, última atualização em 2026-08-31.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2004 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Malária — CID-10 B50-B54) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (8-30 dias antes do exame) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_RACA` | Inteiro | Raça/cor (1-Branca, 2-Preta, 3-Amarela, 4-Parda, 5-Indígena, 9-Ignorado) |
| `ID_OCUPA_C` | String (6) | Ocupação do paciente, código CBO (relevante para exposição ocupacional em áreas florestais e rurais) |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `CLASSI_FIN` | Inteiro | Classificação final: 1 - Confirmado (quando o resultado do exame ≠ negativo), 2 - Descartado (exame negativo), 8 - Inconclusivo |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Abandono, 3 - Óbito pelo agravo, 4 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação. co_municipio_not ificacao | — | todos |
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora. co_unidade_notifi cacao | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escolar` | `CS_ESCOLAR` | texto | Escolaridade do paciente (formato do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2004 a 2004 |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno). ds_semana_notifi cacao | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico. dt_diagnostico_si ntoma | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno). ds_semana_sinto ma | — | todos |
| `nu_idade` | `NU_IDADE` | texto | Idade do paciente (formato do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2004 a 2004 |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência. co_municipio_res idencia | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil). co_pais_residenc ia | — | todos |
| `id_dg_not` | `ID_DG_NOT` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Malária (`ID_DG_NOT`); o dicionário consultado não define o campo isoladamente | — | 2004 a 2004 |
| `id_ev_not` | `ID_EV_NOT` | texto | Código (tipo, identificação ou classificação) registrado na ficha de Malária (`ID_EV_NOT`); o dicionário consultado não define o campo isoladamente | — | 2004 a 2004 |
| `ant_dt_inv` | `ANT_DT_INV` | data | Data da investigação | — | 2004 a 2004 |
| `ocupacao` | `OCUPACAO` | texto | Ocupação do paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2004 a 2004 |
| `transfu` | `TRANSFU` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `dttransfu` | `DTTRANSFU` | data | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `utransfu` | `UTRANSFU` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `uftransfu` | `UFTRANSFU` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `ptransfu` | `PTRANSFU` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `mtransfu` | `MTRANSFU` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `pusuario` | `PUSUARIO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `pmalaria` | `PMALARIA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `amalaria` | `AMALARIA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `assintom` | `ASSINTOM` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `febre` | `FEBRE` | texto | Sinais e sintomas FEBRE PERSISTENTE. st_sinais_febre_persist ente | 1-sim; 2-não; 9-ignorado | 2004 a 2004 |
| `calafrio` | `CALAFRIO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `sudorese` | `SUDORESE` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `cli_outro` | `CLI_OUTRO` | texto | Manifestação clínica registrada na ficha de Malária (`CLI_OUTRO`); o dicionário consultado não define o campo isoladamente | — | 2004 a 2004 |
| `cd_outro` | `CD_OUTRO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `gestante` | `GESTANTE` | texto | Indica se a paciente está gestante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2004 a 2004 |
| `hospital` | `HOSPITAL` | texto | Nome Do Hospital. VARCHAR (8) | — | 2004 a 2004 |
| `dinterna` | `DINTERNA` | data | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `ufinterna` | `UFINTERNA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `minterna` | `MINTERNA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `dexame` | `DEXAME` | data | Data do exame. Data em que foi realizado o exame. Permite avaliar se o exame está sendo realizado no prazo previsto | — | todos |
| `pmm` | `PMM` | inteiro ou texto | Parasitos por mm³. Densidade parasitária por plasmódio em mm3. Permite avaliar o nível de gravidade da doença e atraso no tratamento | — | todos |
| `pcruz` | `PCRUZ` | texto | Parasitemia em cruzes. Densidade parasitária por plasmódio em cruzes. Permite avaliar o nível de gravidade da doença e atraso no tratamento | 1. menor ½ + (Menor que meia cruz) 2. 1/2 + (Meia cruz) 3. + (Uma cruz) 4. ++ (Duas cruzes) 5. +++ (Três cruzes) 6. ++++ (Quatro cruzes) | todos |
| `result` | `RESULT` | texto | Resultado do exame. Resultado do exame identificando as espécies e formas parasitárias. Orienta o tratamento e permite a avaliação das espécies parasitárias existentes | 1 – negativo 2 – F 3 – F + FG 4 – V 5 – F+ V 6 – V + FG 7 – FG | todos |
| `cloroq` | `CLOROQ` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `primaq` | `PRIMAQ` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `tetrac` | `TETRAC` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `mefloq` | `MEFLOQ` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `artesu` | `ARTESU` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `quinino` | `QUININO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `artem` | `ARTEM` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `clind` | `CLIND` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `cloroqi` | `CLOROQI` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `quininoi` | `QUININOI` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `artei` | `ARTEI` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `artemi` | `ARTEMI` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `clindi` | `CLINDI` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `doxoci` | `DOXOCI` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `soutros` | `SOUTROS` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 2004 a 2004 |
| `dtrata` | `DTRATA` | data | Data do inicio do tratamento. Data em que iniciou o tratamento. Permite avaliar se o tratamento está sendo realizado imediatamente após o diagnóstico | — | todos |
| `con_classi` | `CON_CLASSI` | texto | Classificação da forma clínica | 1. Forma bubônica 2. Forma pneumônica 3. Forma septicêmica 4 outra | 2004 a 2004 |
| `con_confir` | `CON_CONFIR` | texto | Dado de conclusão do caso na ficha de Malária (`CON_CONFIR`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2004 a 2004 |
| `con_inf_mu` | `CON_INF_MU` | texto | Dado de conclusão do caso na ficha de Malária (`CON_INF_MU`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2004 a 2004 |
| `con_inf_uf` | `CON_INF_UF` | texto | Dado de conclusão do caso na ficha de Malária (`CON_INF_UF`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2004 a 2004 |
| `con_inf_pa` | `CON_INF_PA` | texto | Dado de conclusão do caso na ficha de Malária (`CON_INF_PA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2004 a 2004 |
| `con_doenca` | `CON_DOENCA` | texto | Dado de conclusão do caso na ficha de Malária (`CON_DOENCA`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2004 a 2004 |
| `con_evoluc` | `CON_EVOLUC` | texto | Dado de conclusão do caso na ficha de Malária (`CON_EVOLUC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2004 a 2004 |
| `con_dt_obi` | `CON_DT_OBI` | data | Dado de conclusão do caso na ficha de Malária (`CON_DT_OBI`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2004 a 2004 |
| `con_dt_enc` | `CON_DT_ENC` | data | Dado de conclusão do caso na ficha de Malária (`CON_DT_ENC`): classificação, critério de confirmação, local provável de infecção ou evolução | — | 2004 a 2004 |
| `in_vincula` | `IN_VINCULA` | texto | Vinculação. 0 ou branco – Não Vinculado 1 – Vinculado | — | 2004 a 2004 |
| `nduplic` | `NDUPLIC` | texto | Indicador de duplicidade do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2004 a 2004 |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | 2011 a 2026 |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | 2011 a 2026 |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2011 a 2026 |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | 2011 a 2026 |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | 2011 a 2026 |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | 2011 a 2026 |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | 2011 a 2026 |
| `dt_invest` | `DT_INVEST` | data | Data da investigação. Informe a data do início da investigação | — | 2011 a 2026 |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/ Ramo de Atividade Econômica. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo de atividade econômica do paciente refere-se as atividades econômicas | — | 2011 a 2026 |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final. tp_classificacao_fi nal | 1. Confirmado 2. Descartado | 2011 a 2026 |
| `at_ativida` | `AT_ATIVIDA` | texto | Principal atividade nos últimos 15 dias. tp_principal_atividad e | 1 – agricultura 2 – Pecuária 3 – Doméstica 4- Turismo 5 – Garimpagem 6 – Exploração vegetal 7- caça/pesca 8 – construtor de estradas / barragens 9 – Mineração 10 – Viajante 11 – Outros 99 - ignorado | 2011 a 2026 |
| `at_lamina` | `AT_LAMINA` | texto | Tipo de lâmina. Identificar se é um caso novo (BA/BP) ou uma recaída/recrudescência (LVC) | 1 – BP 2 – BA 3 - LVC | 2011 a 2026 |
| `at_sintoma` | `AT_SINTOMA` | texto | Sintomas. Identificar se o paciente está com ou sem sintomas característicos da malária. Permite avaliar a existência de assintomáticos interferindo na transmissão da doença | 1. Com sintomas 2. Sem sintomas | 2011 a 2026 |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência?. tp_autoctone_reside ncia | 1 – Sim 2 – Não 3 – Indeterminado | 2011 a 2026 |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção) | — | 2011 a 2026 |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente infectado | — | 2011 a 2026 |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). co_municipio_infecc ao | — | 2011 a 2026 |
| `loc_inf` | `LOC_INF` | texto | Localidade provável de infecção. no_localidade_infec cao | — | 2011 a 2026 |
| `tra_esquem` | `TRA_ESQUEM` | texto | Esquema de tratamento utilizado. tp_esquema_tratam ento | 1- Infecções por Pv com Cloroquina em 3 dias e Primaquina em 7 dias; 2- Infecções por Pf com Quinina em 3 dias + Doxiciclina em 5 dias + primaquina no 6º dia; 3- Infecções mistas por Pv + Pf com Mefloquina em dose úni... | 2011 a 2026 |
| `dstraesque` | `DSTRAESQUE` | texto | Esquema de tratamento utilizado - Outro. ds_esquema_tratam ento_outro | — | 2011 a 2026 |
| `nu_lote_i` | `NU_LOTE_I` | texto | Transferência vertical da investigação. Descrever aqui a estrutura da composição do número do lote | — | 2011 a 2026 |
| `dt_encerra` | `DT_ENCERRA` | data | Data de Encerramento. Data do encerramento da investigação | — | 2011 a 2026 |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | 2011 a 2026 |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | 2011 a 2026 |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | 2011 a 2026 |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | 2011 a 2026 |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | 2011 a 2026 |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | 2011 a 2026 |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | 2011 a 2026 |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | 2011 a 2026 |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal. nu_lote_horizont al | — | 2011 a 2026 |

## No lake

- **Dataset no lake:** `datasus/sinan-mala`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 18, inteiro: 2, texto: 85.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-mala.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- como os registros estão em arquivos consolidados `BR` anuais, o volume é pequeno (23 arquivos, ~2,9 MB), pois a malária da Amazônia Legal está majoritariamente registrada no SIVEP-Malária em vez do SINAN — a base SINAN subestima a carga total nacional de malária, devendo ser combinada com o SIVEP para séries completas; os arquivos dos anos recentes em `PRELIM` ainda são sujeitos a revisão. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Tipo que varia entre períodos:** `pmm` aparecem com mais de um tipo nas amostras (por exemplo, inteiro em alguns períodos e texto em outros); leia a coluna `Tipo` do dicionário e converta explicitamente antes de empilhar períodos. Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Colunas que não existem em todo o período:** 83 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-mala/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-mala
quantilica datasus list sinan-mala

# 2. Baixar microdados de sinan-mala com recorte adequado à partição do dataset
quantilica datasus sync sinan-mala -o ./data --start 2004 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-mala -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-mala -o ./data/raw --parquet-dir ./data/parquet --start 2004
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de malária (casos SINAN, visão extra-amazônica)
qdf = read_dbc("data/sinan-mala/2023/sinan-mala_2023-br@20260831.dbc", clean=True)

# Casos confirmados por ano e UF
print(
    qdf.filter(pl.col("classi_fin") == 1)
    .group_by("nu_ano", "sg_uf_not")
    .len()
    .sort(["nu_ano", "sg_uf_not"])
)

# Casos confirmados por município de residência, para vigilância extra-amazônica
print(
    qdf.filter(pl.col("classi_fin") == 1)
    .group_by("id_mn_resi")
    .len()
    .sort("len", descending=True)
)
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Malária (ficha/procedimentos)**: https://portalsinan.saude.gov.br/malaria
- **Ficha de Investigação Malária SINAN NET**: http://portalsinan.saude.gov.br/images/documentos/Agravos/Malaria/Malaria_v5.pdf
- **SIVEP-Malária (Amazônia Legal)**: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/m/sivep-malaria
- **Portaria SVS/MS nº 104/2011** e **Portaria GM/MS nº 204/2016** (notificação compulsória)
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
