---
dataset:
  id: sim-doinf-cid10
  fonte: datasus
  titulo: Declarações de Óbito Infantis CID-10
  resumo: 'Declarações de Óbito Infantis CID-10 do DATASUS: um óbito de menor de 1 ano, a partir de 1996 (CID-10).'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), Coordenação-Geral de Informações e Análise Epidemiológicas (CGIAE)
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '1996'
    fim: em-curso
  unidade: um óbito de menor de 1 ano, a partir de 1996 (CID-10)
  granularidade:
    espacial: município de residência e de ocorrência do óbito
    temporal: dia do óbito; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por ano (por UF de residência no dataset `do`; nacional nos recortes)
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 92
  dados_pessoais:
  - coluna: dtnasc
    categoria: data de nascimento
  - coluna: codbaires
    categoria: bairro (código) de residência ou ocorrência
  - coluna: crm
    categoria: número de registro profissional (CRM) do médico que atestou
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Declarações de Óbito Infantis CID-10 (`sim-doinf-cid10`)

## Resumo

Microdados nacionais do SIM/SVSA-MS com as Declarações de Óbito de menores de 1 ano de 1996 a 2025 (CID-10). Cada linha é um óbito infantil.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/SIM/CID9/DOCS`, `/dissemin/publicos/SIM/CID10/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SIM/CID9/TAB`, `/dissemin/publicos/SIM/CID10/TAB`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIM/CID10/DOFET` | `DOINF` | `year2_pattern` — ano com 2 dígitos (arquivo nacional, sem UF) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `DOINF23.dbc` — `DOINF` (óbitos infantis) + `23` (ano com 2 dígitos, 2023); arquivo nacional, sem sufixo de UF.
- **No armazenamento local do `datasus-fetcher`**: `data/sim-doinf-cid10/<AAAA>/sim-doinf-cid10_<AAAA>@<AAAAMMDD>.dbc`, por exemplo `data/sim-doinf-cid10/2024/sim-doinf-cid10_2024@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação (`datasus-metadata/metadata/documentation/sim.json`):
    - `/dissemin/publicos/SIM/CID9/DOCS/Docs-Tabs-CID9.zip` (0.7 MB)
    - `/dissemin/publicos/SIM/CID9/DOCS/INTRO.pdf` (0.0 MB)
    - `/dissemin/publicos/SIM/CID9/DOCS/MORT98.HLP` (0.1 MB)
    - `/dissemin/publicos/SIM/CID9/DOCS/MTAB16M.pdf` (2.3 MB)
    - `/dissemin/publicos/SIM/CID10/DOCS/Docs_Tabs_CID10.zip` (2.3 MB)
    - `/dissemin/publicos/SIM/CID10/DOCS/Estrutura_do_SIM_2025.pdf` (0.6 MB)
    - `/dissemin/publicos/SIM/CID10/DOCS/Estrutura_SIM_Anterior.pdf` (0.1 MB)
    - `/dissemin/publicos/SIM/CID10/DOCS/Estrutura_SIM_para_CD.pdf` (0.4 MB)
    - `/dissemin/publicos/SIM/CID10/DOCS/Legislacao_PDF.pdf` (0.9 MB)
    - `/dissemin/publicos/SIM/CID10/DOCS/Portaria.pdf` (0.0 MB)
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/sim.json`):
    - `/dissemin/publicos/SIM/CID9/TAB/OBITOS_CID9_TAB.zip` (0.4 MB)
    - `/dissemin/publicos/SIM/CID10/TAB/CNVS_CID10_v2019.rar` (1.1 MB)
    - `/dissemin/publicos/SIM/CID10/TAB/OBITOS_CID10_TAB.zip` (10.3 MB)

## Conteúdo

O Sistema de Informação sobre Mortalidade (SIM) foi criado pelo Ministério da Saúde em 1975 e hoje é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), por meio da Coordenação-Geral de Informações e Análises Epidemiológicas (CGIAE), com descentralização para as secretarias municipais e estaduais de saúde. Sua finalidade é prover estatísticas vitais de mortalidade para vigilância epidemiológica, planejamento e avaliação de políticas, com cobertura nacional e identificação do local de residência e de ocorrência. O evento gerador é o óbito, registrado na Declaração de Óbito (DO), documento padronizado em todo o país e de preenchimento obrigatório pelo médico (ou, na ausência, por duas testemunhas em cartório). A DO é organizada em nove blocos (identificação, residência, ocorrência, fetal/menor de 1 ano, condições da mãe, causas do óbito, médico, causas externas, cartório e localidade sem médico) e é alimentada nos municípios, com consolidação estadual e federal.

O recorte infantil reúne os óbitos de menores de 1 ano, subdivididos em neonatais precoces (0–6 dias), neonatais tardios (7–27 dias) e pós-neonatais (28–364 dias). A mortalidade infantil é um dos principais indicadores de desenvolvimento e acesso à saúde, e o bloco IV da DO (dados da mãe e da gestação) é essencial para a análise.

A principal ruptura histórica é a mudança de classificação: a CID-9 vigorou até 1995 e a CID-10 passou a ser usada a partir de 1996, o que torna as séries de causa de morte não diretamente comparáveis sem compatibilização (por exemplo, por agrupamentos de causas). O FTP organiza os arquivos em dois blocos (`SIM/CID9` e `SIM/CID10`), cada um com seu layout, sua pasta de documentação (`DOCS`) e seus arquivos de tabulação (`TAB`). Portarias que regulam a vigilância de óbitos específicos (maternos, Portaria GM/MS nº 1.119/2008; infantis e fetais, Portaria GM/MS nº 72/2010) e o fluxo de coleta de dados do SIM e do SINASC (Portaria SVS/MS nº 116/2009) ampliaram a investigação e melhoraram a captação. Os dados dos anos mais recentes são divulgados primeiro como preliminares e depois consolidados.

Cobertura no FTP: 1996 a 2025, em um único arquivo nacional por ano. Indicadores: taxa de mortalidade infantil (por mil nascidos vivos, com denominador do SINASC), componentes neonatal e pós-neonatal, causas evitáveis, mortalidade por peso ao nascer e por idade materna.

### Cobertura observada

- Índice do FTP (2026-10): 30 arquivos, de 1996 a 2025, 1 UF(s) com arquivos, última atualização em 2026-08-28.
- Conversão local de amostras (5 arquivo(s) Parquet, de 1996 a 2025), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Layout CID-10 do recorte infantil; confirme por ano a presença de cada coluna em `Estrutura_do_SIM_2025.pdf` e em `Docs_Tabs_CID10.zip`.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DTOBITO` | String `DDMMAAAA` | Data do óbito. |
| `DTNASC` | String `DDMMAAAA` | Data de nascimento da criança. |
| `IDADE` | Inteiro (código composto) | Idade ao morrer: valores `0xx`/`1xx` (minutos/horas), `2xx` (dias), `3xx` (meses); sempre menor que 1 ano. |
| `SEXO` | Inteiro | Sexo: `1`, `2`, `0`/`9` ignorado. |
| `RACACOR` | String | Raça/cor da criança. |
| `PESO` | String / Inteiro (g) | Peso ao nascer em gramas. |
| `GESTACAO / SEMAGESTAC` | Inteiro | Duração da gestação (faixa e semanas). |
| `GRAVIDEZ / PARTO` | Inteiro | Tipo de gravidez e de parto. |
| `IDADEMAE` | String / Inteiro | Idade da mãe em anos. |
| `ESCMAE` | String | Escolaridade da mãe. |
| `QTDFILVIVO / QTDFILMORT` | Inteiro | Filhos nascidos vivos e perdas fetais anteriores. |
| `CODMUNRES` | String (IBGE, 6) | Município de residência da mãe/criança. |
| `CODMUNOCOR` | String (IBGE, 6) | Município de ocorrência. |
| `LOCOCOR` | String | Local de ocorrência do óbito. |
| `CAUSABAS` | String (CID) | Causa básica do óbito (CID-10 ou CID-9 conforme o dataset). |
| `ASSISTMED / NECROPSIA` | String | Assistência médica e necropsia. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `contador` | `CONTADOR` | texto | Contador: número sequencial do registro no arquivo (campo interno) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tipobito` | `TIPOBITO` | texto | Tipo do óbito Óbito fetal: morte antes da expulsão ou da extração completa do corpo da Mãe, independentemente da duração da gravidez. Indica o óbito o fato de o feto, depois da expulsão do corpo materno, não respirar nem apresentar nenhum outro sinal de vida, como batimentos do coração, pulsações do cordão umbilical ou movimentos efetivos dos músculos de contração voluntária | 1-Fetal; 2-Não Fetal | todos |
| `dtobito` | `DTOBITO` | texto | Data em que occoreu o óbito. | Data no padrão ddmmaaaa | todos |
| `natural` | `NATURAL` | texto | Município e Unidade da Federação onde o falecido nasceu. Se estrangeiro informar País | Números | todos |
| `dtnasc` | `DTNASC` | texto | Data do nascimento do falecido. Em caso de óbito fetal as datas de óbito e nascimento deverão ser iguais. | Data no padrão ddmmaaaa | todos |
| `idade` | `IDADE` | texto | Idade do falecido em minutos, horas, dias, meses ou anos | Idade: composto de dois subcampos. - O primeiro, de 1 dígito, indica a unidade da idade (se 1 = minuto, se 2 = hora, se 3 = mês, se 4 = ano, se = 5 idade maior que 100 anos). - O segundo, de dois dígitos, indica a qua... | todos |
| `sexo` | `SEXO` | texto | Sexo do falecido. “Ignorado” selecionada em casos especiais como cadáveres mutilados, em estado avançado de decomposição, genitália indefinida ou hermafroditismo | M,1 – masculino; F,2 – feminino; I,0,9 - ignorado | todos |
| `racacor` | `RACACOR` | texto | Cor informada pelo responsável pelas informações do falecido | 1 – Branca; 2 – Preta; 3 – Amarela; 4 – Parda; 5 – Indígena | todos |
| `estciv` | `ESTCIV` | texto | Situação conjugal do falecido informada pelos familiares | 1 – Solteiro; 2 – Casado; 3 – Viúvo; 4 – Separado judicialmente/divorciado; 5 – União estável; 9 – Ignorado | todos |
| `esc` | `ESC` | texto | Escolaridade em anos | 1 – Nenhuma; 2 – de 1 a 3 anos; 3 – de 4 a 7 anos; 4 – de 8 a 11 anos; 5 – 12 anos e mais; 9 – Ignorado. | todos |
| `ocup` | `OCUP` | texto | Tipo de trabalho que o falecido desenvolveu na maior parte de sua vida produtiva. Preenchimento de acordo com Classificação Brasileira de Ocupações – CBO 2002 | Números | todos |
| `codbaires` | `CODBAIRES` | texto | Código do bairro de residência do falecido (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 1996 a 2005 |
| `codmunres` | `CODMUNRES` | texto | Código do município de residência. Em caso de óbito fetal, considerar o município de residência da mãe | Números | todos |
| `lococor` | `LOCOCOR` | texto | Local de ocorrência do óbito | 1 – hospital; 2 – outros estabelecimentos de saúde; 3 – domicílio; 4 – via pública; 5 – outros; 6 - aldeia indígena; 9 – ignorado. | todos |
| `codmunocor` | `CODMUNOCOR` | texto | Código relativo ao município onde ocorreu o óbito | Números | todos |
| `idademae` | `IDADEMAE` | texto | Idade da mãe | Números | todos |
| `escmae` | `ESCMAE` | texto | Escolaridade da mãe em anos | 1 – Nenhuma; 2 – de 1 a 3 anos; 3 – de 4 a 7 anos; 4 – de 8 a 11 anos; 5 – 12 anos e mais; 9 – Ignorado | todos |
| `ocupmae` | `OCUPMAE` | texto | Tipo de trabalho exercido habitualmente pela Mãe, de acordo com Classificação Brasileira de Ocupações – CBO 2002. No caso da mãe do falecido(a) ser “aposentada”, preencher com a ocupação habitual anterior. | — | todos |
| `qtdfilvivo` | `QTDFILVIVO` | texto | Número de filhos vivos | Número; 9 - igonorado | todos |
| `qtdfilmort` | `QTDFILMORT` | texto | Número de filhos mortos. Não incluir a criança cujo óbito se notifica na respectiva DO | Número; 9 - igonorado | todos |
| `gravidez` | `GRAVIDEZ` | texto | Tipo de gravidez | 1 – única; 2 – dupla; 3 – tripla e mais; 9 – ignorada | todos |
| `gestacao` | `GESTACAO` | texto | Faixas de semanas de gestação | 1 - Menos de 22 semanas; 2 - 22 a 27 semanas; 3 - 28 a 31 semanas; 4 - 32 a 36 semanas; 5 - 37 a 41 semanas; 6 - 42 e + semanas | todos |
| `parto` | `PARTO` | texto | Tipo de parto | 1 – vaginal; 2 – cesáreo; 9 – ignorado | todos |
| `obitoparto` | `OBITOPARTO` | texto | Momento do óbito em relação ao parto | 1 - antes; 2– durante; 3–depois; 9– Ignorado | todos |
| `peso` | `PESO` | texto | Peso ao nascer em gramas | Número (quatro algarismos) | todos |
| `obitograv` | `OBITOGRAV` | texto | Óbito na gravidez | 1 – sim; 2 – não; 9 – ignorado | todos |
| `obitopuerp` | `OBITOPUERP` | texto | Óbito no puerpério | 1 – Sim, até 42 dias após o parto; 2 – Sim, de 43 dias a 1 ano; 3 – Não; 9 – Ignorado. | todos |
| `assistmed` | `ASSISTMED` | texto | Se refere ao atendimento médico continuado que o paciente recebeu, ou não, durante a enfermidade que ocasionou o óbito | 1 – sim; 2 – não; 9 – ignorado | todos |
| `exame` | `EXAME` | texto | Realização de exame | 1 – sim; 2 – não; 9 – ignorado | todos |
| `cirurgia` | `CIRURGIA` | texto | Realização de cirurgia | 1 – sim; 2 – não; 9 – ignorado | todos |
| `necropsia` | `NECROPSIA` | texto | Refere-se a execução ou não de necropsia para confirmação do diagnóstico | 1 – sim; 2 – não; 9 – ignorado | todos |
| `causabas` | `CAUSABAS` | texto | Causa básica da DO | *;letras; números; | todos |
| `linhaa` | `LINHAA` | texto | CIDs informados na Linha A da DO referente ao diagnóstico na Linha A da DO (causa terminal - doença ou estado mórbido que causou diretamente a morte) | *;letras; números; | todos |
| `linhab` | `LINHAB` | texto | CIDs informados na Linha B da DO referente ao diagnóstico na Linha B da DO (causa antecedente ou conseqüencial - estado mórbido, se existir, que produziu a causa direta da morte registrada na linha A) | *;letras; números; | todos |
| `linhac` | `LINHAC` | texto | CIDs informados na Linha C da DO referente ao diagnóstico na Linha C da DO (causa antecedente ou conseqüencial - estado mórbido, se existir, que produziu a causa | *;letras; números; | todos |
| `linhad` | `LINHAD` | texto | CIDs informados na Linha D da DO referente ao diagnóstico na Linha D da DO (causa básica – estado mórbido, se existir, que produziu a causa direta da morte registrada na linha A) | letras; números; * | todos |
| `linhaii` | `LINHAII` | texto | CIDs informados na Parte II da DO | — | todos |
| `circobito` | `CIRCOBITO` | texto | Tipo de morte violenta ou circunstâncias em que se deu a morte não natural | 1 – acidente; 2 – suicídio; 3 – homicídio; 4 – outros; 9 – ignorado | todos |
| `acidtrab` | `ACIDTRAB` | texto | Indica se o evento que desencadeou o óbito está relacionado ao processo de trabalho | 1 – sim; 2 – não; 9 – ignorado | todos |
| `fonte` | `FONTE` | texto | fonte de informação utilizada para o preenchimento dos campos 48 e 49 | 1 – ocorrência policial; 2 – hospital; 3 – família; 4 – outra; 9 – ignorado | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `codestab` | `CODESTAB` | texto | Código do estabelecimento de saúde constante do Cadastro Nacional de Estabelecimento de Saúde | Números | 2005 a 2025 |
| `atestante` | `ATESTANTE` | texto | Condição do médico atestante | 1 - Assistente; 2 – Substituto; 3 – IML; 4 – SVO; 5 – Outro | 2005 a 2025 |
| `ufinform` | `UFINFORM` | texto | UF que informou o registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2005 |
| `origem` | `ORIGEM` | texto | Origem do registro: 01 Oracle; 02 banco estadual disponibilizado via FTP; 03 banco SEADE; 9 ignorado | — | 2011 a 2025 |
| `horaobito` | `HORAOBITO` | texto | Horário do óbito | Números (padrão 24 horas 00:00) | 2011 a 2025 |
| `comunsvoim` | `COMUNSVOIM` | texto | Código do município do SVO ou do IML | Números | 2011 a 2025 |
| `dtatestado` | `DTATESTADO` | texto | Data em que o atestado foi assinado | Data no padrão ddmmaaaa | 2011 a 2025 |
| `tppos` | `TPPOS` | texto | Óbito investigado | 1 – sim; 2 – não | 2011 a 2025 |
| `dtinvestig` | `DTINVESTIG` | texto | Data da investigação do óbito | Data no padrão ddmmaaaa | 2011 a 2025 |
| `causabas_o` | `CAUSABAS_O` | texto | Causa básica informada antes da resseleção | *; letras;números | 2011 a 2025 |
| `dtcadastro` | `DTCADASTRO` | texto | Data do cadastro do óbito | Data no padrão ddmmaaaa | 2011 a 2025 |
| `fonteinv` | `FONTEINV` | texto | Fonte de investigação | 1 – Comitê de Morte Materna e/ou Infantil; 2 – Visita domiciliar / Entrevista família; 3 – Estabelecimento de Saúde / Prontuário; 4 – Relacionado com outros bancos de dados; 5 – S V O; 6 – I M L; 7 – Outra fonte; 8 – ... | 2011 a 2025 |
| `dtrecebim` | `DTRECEBIM` | texto | Data do recebimento | Data no padrão ddmmaaaa | 2011 a 2025 |
| `dtrecorig` | `DTRECORIG` | texto | Data de recebimento original do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2011 |
| `dtrecoriga` | `DTRECORIGA` | texto | Campo Criado no Tratamento para Data do recebimento original | Data no padrão ddmmaaaa | 2011 a 2025 |
| `causamat` | `CAUSAMAT` | texto | CID da causa externa associada a uma causa materna | Letras; números; * ; / | 2011 a 2025 |
| `esc2010` | `ESC2010` | texto | Escolaridade 2010. Nível da última série concluída pelo falecido | 0 – Sem escolaridade; 1 – Fundamental I (1ª a 4ª série); 2 – Fundamental II (5ª a 8ª série); 3 – Médio (antigo 2º Grau); 4 – Superior incompleto; 5 – Superior completo; 9 – Ignorado | 2011 a 2025 |
| `escmae2010` | `ESCMAE2010` | texto | Escolaridade 2010. Nível da última série concluída pela mãe | 0 – Sem escolaridade; 1 – Fundamental I (1ª a 4ª série); 2 – Fundamental II (5ª a 8ª série); 3 – Médio (antigo 2º Grau); 4 – Superior incompleto; 5 – Superior completo; 9 – Ignorado | 2011 a 2025 |
| `stdoepidem` | `STDOEPIDEM` | texto | Status de DO Epidemiológica | 1 - Sim; 0 - Não | 2011 a 2025 |
| `stdonova` | `STDONOVA` | texto | Status de DO Nova | 1 - Sim; 0 - Não | 2011 a 2025 |
| `dtcadinv` | `DTCADINV` | texto | Data do cadastro de investigação | Data no padrão ddmmaaaa | 2011 a 2025 |
| `tpobitocor` | `TPOBITOCOR` | texto | Momento do óbito em relação à gestação, parto ou puerpério (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2011 a 2025 |
| `dtcadinf` | `DTCADINF` | texto | Quando preenchido indica se a investigação foi realizada | Data no padrão ddmmaaaa | 2011 a 2025 |
| `morteparto` | `MORTEPARTO` | texto | Momento do óbito em relação ao parto após investigação | 1 - antes; 2– durante; 3–após; 9– Ignorado | 2011 a 2025 |
| `codmunnatu` | `CODMUNNATU` | texto | Código do município de naturalidade do falecido. | Números | 2017 a 2025 |
| `seriescfal` | `SERIESCFAL` | texto | Última série escolar concluída pelo falecido | Números de 1 a 8 | 2017 a 2025 |
| `estabdescr` | `ESTABDESCR` | texto | Descrição do estabelecimento de ocorrência do óbito (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2017 a 2025 |
| `seriescmae` | `SERIESCMAE` | texto | Última série escolar concluída pela mãe | Números de 1 a 8 | 2017 a 2025 |
| `semagestac` | `SEMAGESTAC` | texto | Semanas de gestação com dois algarismos | Números com dois algarismos; 9 - igonorado | 2017 a 2025 |
| `tpmorteoco` | `TPMORTEOCO` | texto | Situação gestacional ou pósgestacional em que ocorreu o óbito | 1 – na gravidez; 2 – no parto; 3 – no abortamento; 4 – até 42 dias após o término do parto; 5 – de 43 dias a 1 ano após o término da gestação ; 8 – não ocorreu nestes períodos; 9 – ignorado. | 2017 a 2025 |
| `cb_pre` | `CB_PRE` | texto | Causa básica (CID-10) antes da investigação do óbito (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2017 a 2025 |
| `crm` | `CRM` | texto | Número do CRM do médico que assinou a declaração de óbito | — | só em 2017 |
| `numerolote` | `NUMEROLOTE` | texto | Número do lote | Números | 2017 a 2025 |
| `stcodifica` | `STCODIFICA` | texto | Status de instalação | Se codificadora (valor: S) ou não (valor: N) | 2017 a 2025 |
| `codificado` | `CODIFICADO` | texto | Informa se formulario foi codificado | Se estiver codificado (valor: S) ou não (valor: N) | 2017 a 2025 |
| `versaosist` | `VERSAOSIST` | texto | Versão do sistema | Números; . | 2017 a 2025 |
| `versaoscb` | `VERSAOSCB` | texto | Versão do seletor de causa básica | Números; . | 2017 a 2025 |
| `atestado` | `ATESTADO` | texto | CIDs informados no atestado | Letras; números; * ; / | 2017 a 2025 |
| `escmaeagr1` | `ESCMAEAGR1` | texto | Escolaridade da mãe agregada (ormulário a partir de 2010) | 00 – Sem Escolaridade; 01 – Fundamental I Incompleto; 02 – Fundamental I Completo; 03 – Fundamental II Incompleto; 04 – Fundamental II Completo; 05 – Ensino Médio Incompleto; 06 – Ensino Médio Completo; 07 – Superior ... | 2017 a 2025 |
| `escfalagr1` | `ESCFALAGR1` | texto | Escolaridade do falecido agregada (formulário a partir de 2010) | 00 – Sem Escolaridade; 01 – Fundamental I Incompleto; 02 – Fundamental I Completo; 03 – Fundamental II Incompleto; 04 – Fundamental II Completo; 05 – Ensino Médio Incompleto; 06 – Ensino Médio Completo; 07 – Superior ... | 2017 a 2025 |
| `difdata` | `DIFDATA` | texto | Diferença entre a data de óbito e data do recebimento original da DO ([DTOBITO] – [DTRECORIG]) | Números | 2017 a 2025 |
| `nudiasobco` | `NUDIASOBCO` | texto | Diferença entre a data óbito e a data conclusão da investigação, em dias. | Números | 2017 a 2025 |
| `nudiasobin` | `NUDIASOBIN` | texto | Número de dias entre o óbito e o início da investigação | — | 2017 a 2025 |
| `dtconinv` | `DTCONINV` | texto | Data da conclusão da investigação | Data no padrão ddmmaaaa | 2017 a 2025 |
| `fontes` | `FONTES` | texto | Combinado de caracteres conforme o preenchimento dos campos de fontes (FONTENTREV, FONTEAMBUL, FONTEPRONT, FONTESVO, FONTEIML, FONTEPROF): se preenchido caractere “S”, se o campo estiver vazio caractere “X” | Letras | 2017 a 2025 |
| `tpresginfo` | `TPRESGINFO` | texto | Informa se a investigação permitiu o resgate de alguma causa de óbito não informado, ou a correção de alguma antes informada | 01 - Não acrescentou nem corrigiu informação; 02 - Sim, permitiu o resgate de novas informações; 03 - Sim, permitiu a correção de alguma das causas informadas originalmente. | 2017 a 2025 |
| `tpnivelinv` | `TPNIVELINV` | texto | Tipo de nível investigador | E – estadual; R- regional; M- Municipal | 2017 a 2025 |
| `nudiasinf` | `NUDIASINF` | texto | Número de dias entre datas do processo de investigação do óbito (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2017 a 2025 |
| `dtconcaso` | `DTCONCASO` | texto | Data de conclusão do caso | Data no padrão ddmmaaaa | 2017 a 2025 |
| `fontesinf` | `FONTESINF` | texto | Fontes de informação usadas na investigação do óbito (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2017 a 2025 |
| `altcausa` | `ALTCAUSA` | texto | Indica se houve correção ou alteração da causa do óbito após investigação | 1- Sim; 2 – Não | 2017 a 2025 |

## No lake

- **Dataset no lake:** `datasus/sim-doinf-cid10`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): texto: 92.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sim-doinf-cid10.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- **Colunas que não existem em todo o período:** 52 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sim-doinf-cid10").glob("**/*.parquet"))
dados = pl.concat(  # períodos diferentes têm colunas e tipos diferentes
    [pl.scan_parquet(a, hive_partitioning=True) for a in arquivos],
    how="diagonal_relaxed",
)

(dados.group_by("ano").agg(pl.len().alias("linhas")).sort("ano").collect())
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Pela linha de comando (`datasus-fetcher`)

```bash
# o que o FTP publica para o dataset (arquivos e tamanho)
datasus-fetcher list sim-doinf-cid10

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sim-doinf-cid10 -o ./data --start 2020 --end 2024 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sim-doinf-cid10
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DOFET`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde / SVSA — Sistema de Informação sobre Mortalidade (SIM)**: https://www.gov.br/saude/pt-br/composicao/svsa/sistemas-de-informacao/sim
- **Documentação no FTP (`DOCS`)**: `Estrutura_do_SIM_2025.pdf`, `Estrutura_SIM_para_CD.pdf`, `Docs_Tabs_CID10.zip` (CID-10) e `Docs-Tabs-CID9.zip` (CID-9).
- **Manual de Instruções para o Preenchimento da Declaração de Óbito** (Ministério da Saúde/SVS) e legislação em `Legislacao_PDF.pdf` e `Portaria.pdf` (FTP).
- **PCDaS / Fiocruz** — plataforma de dados com séries do SIM: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde / Wiki SIM** (documentação comunitária do SIM e do DATASUS): https://wiki.saude.gov.br/
