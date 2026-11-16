---
dataset:
  id: resp
  fonte: datasus
  titulo: Notificações de casos suspeitos de SCZ
  resumo: 'Notificações de casos suspeitos de SCZ do DATASUS: uma notificação individual de caso suspeito de Síndrome Congênita associada ao vírus Zika.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA)
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/RESP/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2015'
    fim: '2024'
  unidade: uma notificação individual de caso suspeito de Síndrome Congênita associada ao vírus Zika
  granularidade:
    espacial: município de residência da mãe e de notificação; um arquivo por UF
    temporal: data da notificação; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e ano
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 80
  dados_pessoais:
  - coluna: dt_nasc
    categoria: data de nascimento
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Notificações de casos suspeitos de SCZ (`resp`)

## Resumo

O `resp` contém as **notificações de casos suspeitos de Síndrome Congênita associada à infecção pelo vírus Zika (SCZ)**, incluindo microcefalia e outras alterações do sistema nervoso central, registradas no sistema **RESP (Registro de Eventos em Saúde Pública)**. Cada registro (linha) é uma **notificação individual** de um caso suspeito, com dados de notificação, residência, dados clínicos e de investigação laboratorial. É a base usada pelo Ministério da Saúde no monitoramento da emergência de saúde pública de 2015-2016 e nas análises de desfechos congênitos associados ao Zika.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/RESP/DOCS` (`DIC_DADOS_RESP.txt`)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/RESP/AUXILIAR` (`tabresp.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/RESP/DADOS` | `RESP` | UF + AA (ex.: `AC15`, `SP16`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `RESPAC15.dbc` — `RESP` é o prefixo, `AC` a UF e `15` o ano (2015). Há um `.dbc` por UF e ano, de 2015 a 2024.
- **No armazenamento local do `datasus-fetcher`**: `data/resp/<AAAA>/resp_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/resp/2024/resp_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `RESP/DOCS` está `DIC_DADOS_RESP.txt` (dicionário de dados, com as variáveis e seus domínios); em `RESP/AUXILIAR` está `tabresp.zip`, com o arquivo `RESP.def` (definições) e tabelas de conversão `.cnv` usadas pelo TabWin.

## Conteúdo

Em resposta à **emergência de saúde pública** deflagrada a partir de 2015, quando se observou o aumento de casos de microcefalia e alterações do sistema nervoso central possivelmente associados à infecção pelo vírus Zika durante a gestação, o Ministério da Saúde implantou um **registro específico de notificação** — o sistema **RESP** — para captar os casos suspeitos de **Síndrome Congênita associada ao Zika (SCZ)**. O sistema complementa os instrumentos do SINAN para essa condição.

O **evento gerador** é a **notificação de um caso suspeito de SCZ/microcefalia** por uma unidade de saúde. A **unidade de análise é a notificação individual**, com os campos típicos de notificação (`TP_NOT`, `ID_AGRAVO`, `DT_NOTIFIC`, `SEM_NOT`, `NU_ANO`, `SG_UF_NOT`, `ID_MUNICIP`, `ID_REGIONA`, `ID_UNIDADE`), dados da mãe e da gestação (`CS_GESTANT`, `NU_IDADE_N`, `CS_SEXO`, `CS_RACA`, `CS_ESCOL_N`), residência (`SG_UF`, `ID_MN_RESI`, `ID_RG_RESI`), dados clínicos e de investigação (classificação final, critério de confirmação/descarte, resultados de exames e evolução), além de datas como `DT_SIN_PRI` (primeiros sintomas) e `DT_INVEST` (investigação).

Os dados são organizados por UF e ano (prefixo `RESP` + UF + dois dígitos do ano, ex.: `RESPAC15.dbc`) e cobrem 2015 a 2024. Apenas UFs com notificações aparecem (28 UFs). Não há diretório preliminar.

Aplicações analíticas típicas: monitoramento temporal e espacial da SCZ, cálculo de prevalência/incidência de microcefalia, análise de desfechos gestacionais, avaliação da completude e da qualidade da notificação, investigação de associação com arboviroses e avaliação da resposta à emergência.

### Cobertura observada

- Índice do FTP (2026-10): 280 arquivos, de 2015 a 2024, 28 UF(s) com arquivos, última atualização em 2024-07-01.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2015 a 2024), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (individual/negativa etc.) |
| `ID_AGRAVO` | String | Código do agravo (SCZ/Zika) |
| `DT_NOTIFIC` | Data (`AAAAMMDD`) | Data da notificação |
| `SEM_NOT` | String (`AAAAWW`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município notificante |
| `ID_MUNICIP` | String | Código do município notificante |
| `ID_UNIDADE` | String | Código da unidade notificante (CNES) |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data dos primeiros sintomas |
| `NU_IDADE_N` | String | Código de idade (unidade + valor) |
| `CS_SEXO` | String | Sexo do paciente |
| `CS_GESTANT` | String | Situação/idade gestacional |
| `CS_RACA` / `CS_ESCOL_N` | String | Raça/cor e escolaridade |
| `SG_UF` / `ID_MN_RESI` / `ID_RG_RESI` | String | UF, município e região de residência |
| `CLASSI_FIN` / `CRITERIO` | String | Classificação final e critério de confirmação/descarte |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |

> A lista completa de variáveis (inclusive as laboratoriais e de desfecho) está no dicionário `DIC_DADOS_RESP.txt` (documentação oficial no FTP).

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_seq` | `CO_SEQ` | texto | Código sequencial de identificação do registro na base de dados de disseminação. | — | todos |
| `dt_notific` | `DT_NOTIFIC` | texto | Data de preenchimento do formulário. | DDMMAAAA | todos |
| `ano_not` | `ANO_NOT` | texto | Ano da notificação | AAAA | todos |
| `tp_notific` | `TP_NOTIFIC` | texto | Tipo da notificação | 1- Recém-nascido com microcefalia (≤ 28 dias); 2- Criança com microcefalia e/ou alterações do SNC (> 28 dias); 3- Feto com alterações do SNC; 4- Feto em risco; 5- Natimorto com microcefalia e/ou alterações do SNC; 6- ... | todos |
| `dt_nascmae` | `DT_NASCMAE` | texto | Data de nascimento da gestante/mãe | DDMMAAAA | todos |
| `idadeges` | `IDADEGES` | texto | Idade da gestante/mãe | — | todos |
| `racacor` | `RACACOR` | texto | Cor ou raça declarada | 1-Branca 2-Negra 3-Amarela 4-Parda 5-Indígena 9-Ignorado | todos |
| `regiaores` | `REGIAORES` | texto | Macrorregião de residência da gestante/mãe | Códigos de 1 a 5 padronizados pelo IBGE: 1- Norte; 2- Nordeste; 3- Sudeste; 4- Sul; 5- Centro oeste. | todos |
| `ufres` | `UFRES` | texto | Unidade da federação de residência da gestante/mãe | Códigos padronizados pelo IBGE | todos |
| `codmunres` | `CODMUNRES` | texto | Município de residência da gestante/mãe | Códigos padronizados pelo IBGE | todos |
| `sexo` | `SEXO` | texto | Sexo da criança, recém-nascido, feto ou natimorto. | 1-Masculino 2-Feminino 9-Ignorado | todos |
| `dt_nasc` | `DT_NASC` | data | Data de nascimento da criança, recém- nascido ou do feto. | DDMMAAAA | todos |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento da criança, recém- nascido ou do feto. | AAAA | todos |
| `peso` | `PESO` | texto | Peso ao nascer (ou do natimorto) em gramas | — | todos |
| `compriment` | `COMPRIMENT` | texto | Comprimento ao nascer (ou do natimorto) em centímetros | — | todos |
| `perimcefal` | `PERIMCEFAL` | texto | Perímetro cefálico ao nascer (ou do natimorto) em centímetros com uma casa decimal – Exemplo: 31.5 | — | todos |
| `diamcefal` | `DIAMCEFAL` | texto | Medida da Circunferência Craniana, em centímetros incluindo a decimal (exemplo: 28.5), para detecção intrauterina da alteração congênita. | — | todos |
| `microcefal` | `MICROCEFAL` | texto | Tipos de alterações congênitas detectadas | 1- Microcefalia apenas; 2- Microcefalia com alteração do SNC; 3- Microcefalia com outras alterações congênitas; 4- Alterações congênitas sem microcefalia. | todos |
| `def_neuro` | `DEF_NEURO` | texto | Foi informada deficiência neurológica entre as alterações congênitas detectadas? | 1- Sim; 2- Não. | todos |
| `def_audit` | `DEF_AUDIT` | texto | Foi informada deficiência auditiva entre as alterações congênitas detectadas? | 1- Sim; 2- Não. | todos |
| `def_visual` | `DEF_VISUAL` | texto | Foi informada deficiência visual entre as alterações congênitas detectadas? | 1- Sim; 2- Não. | todos |
| `tpdeteccao` | `TPDETECCAO` | texto | Momento em que foi identificada a alteração congênita | 1- Intrauterino (na gestação); 2- Pós-Parto; 3- Não detectada; 9- Ignorado. | todos |
| `gest_diag` | `GEST_DIAG` | texto | Idade gestacional, em semanas, em que foi detectada a alteração congênita (pode ser ainda na gestação ou momento do parto) | — | todos |
| `gravidez` | `GRAVIDEZ` | texto | Tipo de Gravidez | 1- Única; 2- Dupla; 3- Tripla ou mais; 9- Ignorado. | todos |
| `class_feto` | `CLASS_FETO` | texto | Classificação do nascido vivo ou natimorto quanto ao período gestacional no momento do parto. | 1- Pré-Termo (menor que 37 semanas de gestação); 2- A Termo (idade gestacional entre 37 e 41 semanas e 6 dias); 3- Pós-Termo (idade gestacional igual ou maior que 42 semanas). | todos |
| `dt_sintoma` | `DT_SINTOMA` | texto | Data provável de início de qualquer sintoma da gestante/mãe | DDMMAAAA | todos |
| `febre_ges` | `FEBRE_GES` | texto | Febre na gestação | 1- Sim; 2- Não; 9- Ignorado. | todos |
| `exant_ges` | `EXANT_GES` | texto | Exantema na gestação | 1- Sim, no 1º trimestre; 2- Sim, no 2º trimestre; 3- Sim, no 3º trimestre; 4- Sim, mas não lembra a data ou período gestacional; 5- Não apresentou exantema; 9- Não sabe. | todos |
| `prurido` | `PRURIDO` | texto | Foi informado prurido entre outros sinais e sintomas durante a gestação? | 1- Sim; 2- Não. | todos |
| `conjuntiv` | `CONJUNTIV` | texto | Foi informada hiperemia conjuntival (Conjuntivite não purulenta) entre outros sinais e sintomas durante a gestação? | 1- Sim; 2- Não. | todos |
| `dor_artic` | `DOR_ARTIC` | texto | Foi informada dor em articulação entre outros sinais e sintomas durante a gestação? | 1- Sim; 2- Não. | todos |
| `dor_musc` | `DOR_MUSC` | texto | Foi informada dor muscular entre outros sinais e sintomas durante a gestação? | 1- Sim; 2- Não. | todos |
| `edema` | `EDEMA` | texto | Foi informado edema em articulações entre outros sinais e sintomas durante a gestação? | 1- Sim; 2- Não. | todos |
| `cefaleia` | `CEFALEIA` | texto | Foi informada cefaleia entre outros sinais e sintomas durante a gestação? | 1- Sim; 2- Não. | todos |
| `hipert_gan` | `HIPERT_GAN` | texto | Foi informada hipertrofia ganglionar entre outros sinais e sintomas durante a gestação? | 1- Sim; 2- Não. | todos |
| `neurolog` | `NEUROLOG` | texto | Foi informado acometimento neurológico entre outros sinais e sintomas durante a gestação? | 1- Sim; 2- Não. | todos |
| `exa_torsch` | `EXA_TORSCH` | texto | Diagnóstico laboratorial para, pelo menos, um dos STORCH (Sífilis, Toxoplasmose, Rubéola, Citomegalovírus, Herpes vírus) na gestação ou pós-parto imediato. | 1- Sim; 2- Não; 9- Ignorado. | todos |
| `resul_s` | `RESUL_S` | texto | Diagnóstico laboratorial para Sífilis durante a gestação ou no pós- parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `resul_to` | `RESUL_TO` | texto | Diagnóstico laboratorial para Toxoplasmose durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `resul_c` | `RESUL_C` | texto | Diagnóstico laboratorial para Citomegalovírus durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `resul_h` | `RESUL_H` | texto | Diagnóstico laboratorial para Herpes vírus durante a gestação ou no pós- parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `resul_z` | `RESUL_Z` | texto | Diagnóstico laboratorial para Vírus Zika durante a gestação ou no pós-parto imediato. | 1- Sim; 0- Não. . | todos |
| `so_igg_z` | `SO_IGG_Z` | texto | Resultado para Sorologia IgG para Zika Vírus durante a gestação ou no pós- parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `so_igm_z` | `SO_IGM_Z` | texto | Resultado para Sorologia IgM para Zika Vírus durante a gestação ou no pós- parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `tr_igg_z` | `TR_IGG_Z` | texto | Resultado do teste rápido Sorologia IgG para Zika vírus durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `tr_igm_z` | `TR_IGM_Z` | texto | Resultado do teste rápido Sorologia IgM para Zika vírus durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `pcr_z` | `PCR_Z` | texto | Resultado de PCR para Zika vírus durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `hist_arbov` | `HIST_ARBOV` | texto | Histórico de infecção recente por outros arbovírus | 1- Dengue; 2- Chikungunya; 3- Dengue e Chikungunya; 4- Sem histórico de doença; 9- Ignorado | todos |
| `hist_malfo` | `HIST_MALFO` | texto | Histórico de malformação congênita em familiares/parentes | 1- Sim; 2- Não; 9- Ignorado. | todos |
| `rnexa_tors` | `RNEXA_TORS` | texto | Diagnóstico laboratorial do recém- nascido para, pelo menos, um dos STORCH (Sífilis, Toxoplasmose, Rubéola, Citomegalovírus, Herpes vírus) na gestação ou pós-parto imediato. | 1- Sim; 2- Não; 9- Ignorado. | todos |
| `rnresul_s` | `RNRESUL_S` | texto | Diagnóstico laboratorial do recém- nascido para Sífilis durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `rnresul_to` | `RNRESUL_TO` | texto | Diagnóstico laboratorial do recém- nascido para Toxoplasmose durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `rnresul_c` | `RNRESUL_C` | texto | Diagnóstico laboratorial do recém- nascido para Citomegalovírus durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `rnresul_h` | `RNRESUL_H` | texto | Diagnóstico laboratorial do recém- nascido para Herpes vírus durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `rnresul_z` | `RNRESUL_Z` | texto | Diagnóstico laboratorial do recém- nascido para Vírus Zika durante a gestação ou no pós-parto imediato. | 1- Sim; 0- Não. . | todos |
| `rnso_igg_z` | `RNSO_IGG_Z` | texto | Resultado do recém-nascido para Sorologia IgG para Zika Vírus durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `rnso_igm_z` | `RNSO_IGM_Z` | texto | Resultado do recém-nascido para Sorologia IgM para Zika Vírus durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `rntr_igg_z` | `RNTR_IGG_Z` | texto | Resultado do teste rápido Sorologia IgG do recém-nascido para Zika vírus durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `rntr_igm_z` | `RNTR_IGM_Z` | texto | Resultado do teste rápido Sorologia IgM do recém-nascido para Zika vírus durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `rnpcr_z` | `RNPCR_Z` | texto | Resultado de PCR do recém-nascido para Zika vírus durante a gestação ou no pós-parto imediato. | 1- Reagente/Positivo; 2- Não reagente/Negativo; 3- Indetectável/ Indeterminado; 4- Não realizado; 9- Ignorado. | todos |
| `exame_uss` | `EXAME_USS` | texto | Resultado da ultrassonografia realizada durante a gestação. | 1- Resultado Normal; 2- Resultado alterado, sugestivo de infecção congênita; 3- Resultado alterado, com outras alterações; 4- Resultado indeterminado; 5- Não realizado; 9- Ignorado. | todos |
| `dt_uss` | `DT_USS` | texto | Data da ultrassonografia realizada durante a gestação. | DDMMAAAA | todos |
| `exa_transf` | `EXA_TRANSF` | texto | Resultado de ultrassonografia transfontanela realizada durante a gestação. | 1- Resultado Normal; 2- Resultado alterado, sugestivo de infecção congênita; 3- Resultado alterado, com outras alterações; 4- Resultado indeterminado; 5- Não realizado; 9- Ignorado. | todos |
| `dt_transf` | `DT_TRANSF` | texto | Data da ultrassonografia transfontanela realizada durante a gestação. | DDMMAAAA | todos |
| `exame_tc` | `EXAME_TC` | texto | Resultado de tomografia computadorizada realizada durante a gestação. | 1- Resultado Normal; 2- Resultado alterado, sugestivo de infecção congênita; 3- Resultado alterado, com outras alterações; 4- Resultado indeterminado; 5- Não realizado; 9- Ignorado. | todos |
| `dt_tc` | `DT_TC` | texto | Data da tomografia computadorizada realizada durante a gestação. | DDMMAAAA | todos |
| `exame_rs` | `EXAME_RS` | texto | Resultado de ressonância magnética realizada durante a gestação. | 1- Resultado Normal; 2- Resultado alterado, sugestivo de infecção congênita; 3- Resultado alterado, com outras alterações; 4- Resultado indeterminado; 5- Não realizado; 9- Ignorado. | todos |
| `dt_rs` | `DT_RS` | texto | Data da ressonância magnética realizada durante a gestação. | DDMMAAAA | todos |
| `regiaonot` | `REGIAONOT` | texto | Macrorregião do local de notificação | Códigos de 1 a 5 padronizados pelo IBGE: 1- Norte; 2- Nordeste; 3- Sudeste; 4- Sul; 5- Centro oeste. | todos |
| `ufnot` | `UFNOT` | texto | Unidade da Federação do local de notificação | Códigos padronizados pelo IBGE | todos |
| `codmunnot` | `CODMUNNOT` | texto | Município do local de notificação | Códigos padronizados pelo IBGE | todos |
| `st_obito` | `ST_OBITO` | texto | Evolução para óbito? | 1- Sim; 2- Não; 9- Ignorado. | todos |
| `dt_obito` | `DT_OBITO` | data | Data do óbito | DDMMAAAA | todos |
| `classifin` | `CLASSIFIN` | texto | Classificação final do caso. | 1- Confirmado; 2- Provável; 3- Em investigação; 4- Inconclusivo; 5- Descartado; 6- Excluído. | todos |
| `etiologia` | `ETIOLOGIA` | texto | Etiologia | 1- Vírus Zika; 2- STORCH; 3- Coinfecção (STORCH + Zika); 4- Etiologia desconhecida; 9- Ignorado. | todos |
| `criterio` | `CRITERIO` | texto | Critérios para classificação final do caso | — | todos |
| `status_not` | `STATUS_NOT` | texto | Situação do registro | 1- Ativo; 2- Reativado; 3- Inativo. | todos |
| `dt_ult_alt` | `DT_ULT_ALT` | texto | Data da última atualização do registro. | DDMMAAAA | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/resp`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 2, texto: 78.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `resp.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- a notificação é **individual**, mas sujeita a subnotificação e a alterações retroativas; o sistema surgiu em 2015 para a emergência do Zika, portanto a série começa abruptamente; `NU_IDADE_N` codifica unidade (hora/dia/mês/ano) e valor; a cobertura varia por UF; e a base é pequena em volume mas deve ser analisada com atenção às definições de caso vigentes em cada período. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/resp").glob("**/*.parquet"))
dados = pl.concat(  # períodos diferentes têm colunas e tipos diferentes
    [pl.scan_parquet(a, hive_partitioning=True) for a in arquivos],
    how="diagonal_relaxed",
)

(dados.group_by("ano", "uf").agg(pl.len().alias("linhas")).sort("ano", "uf").collect())
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Pela linha de comando (`datasus-fetcher`)

```bash
# o que o FTP publica para o dataset (arquivos e tamanho)
datasus-fetcher list resp

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync resp -o ./data --start 2020 --end 2024 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset resp
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/RESP/DADOS`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde — Síndrome Congênita associada ao Zika e microcefalia**: https://www.gov.br/saude/pt-br
- **Boletins Epidemiológicos do MS (SCZ/Zika)**
- **Dicionário `DIC_DADOS_RESP.txt`** e pacote `tabresp.zip` no FTP DATASUS
