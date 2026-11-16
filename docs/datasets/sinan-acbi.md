---
dataset:
  id: sinan-acbi
  fonte: datasus
  titulo: Acidente de trabalho com material biológico
  resumo: 'Acidente de trabalho com material biológico do DATASUS: uma ficha de notificação/investigação de acidente de trabalho com material biológico.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2006'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de acidente de trabalho com material biológico
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 70
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Acidente de trabalho com material biológico (`sinan-acbi`)

## Resumo

Notificações de acidentes de trabalho em que o trabalhador foi exposto, de forma direta ou indireta, a material biológico (orgânico) potencialmente contaminado por patógenos, registradas no SINAN. Cada linha representa uma ficha de investigação de acidente com material biológico, alimentada por serviços de saúde públicos e privados de todos os portes.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM, 2023–2026; Finais até 2022)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ACBI` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ACBI` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `ACBIBR24.dbc`, em que `ACBI` é o prefixo do agravo, `BR` indica a base nacional (o SINAN publica um único arquivo por ano para o Brasil) e `24` é o ano com 2 dígitos (2024, preliminar).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-acbi/<AAAA>/sinan-acbi_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-acbi/2024/sinan-acbi_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`):
    - `Docs_TAB_SINAN.zip` — pacote de documentação e dicionários para tabulação (~65 MB)
    - `POP_I_Acesso_a_Microdados_5.pdf` — POP I: acesso a microdados
    - `POP_II_Descompactacao_expansao_conversao_3.pdf` — POP II: descompactação, expansão e conversão (.dbc → .dbf)
    - `POP_III_Instalacao_do_tabulador_TabWin_3.pdf` — POP III: instalação do TabWin
    - `Nota_Tecnica_Doenca_de_Creutzfeldt-Jakob(DCJ).pdf` — nota técnica sobre DCJ
  - Tabelas auxiliares (`/SINAN/AUXILIAR`):
    - `TAB_SINANNET.zip` — tabelas de conversão/tabulação (.cnv, .def) do SINAN Net (~44 MB)
    - `TAB_SINANONLINE.zip` — tabelas do SINAN Online (~240 KB)
    - `POPT_Estimativa_TCU_2019_Sinan.zip` — estimativas populacionais TCU 2019 para uso no SINAN
  - O dicionário desta base (`DRT Acidente Trabalho Biológico`) é distribuído no Portal SINAN e referenciado em `Docs_TAB_SINAN.zip`; não há PDF por agravo no FTP.

## Conteúdo

O agravo integra a vigilância em Saúde do Trabalhador do Sistema Único de Saúde, coordenada pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) por meio da Coordenação-Geral de Vigilância em Saúde do Trabalhador e da Trabalhadora. A notificação compulsória dos acidentes com exposição a material biológico foi estabelecida pela Portaria MS nº 777/2004 e consolidada pela Portaria de Consolidação nº 4/2017 (Anexo V), operacionalizada na Rede Nacional de Atenção Integral à Saúde do Trabalhador (RENAST) e nos Centros de Referência em Saúde do Trabalhador (CEREST).

O evento gerador é o acidente de trabalho com exposição percutânea, mucosa, pele íntegra ou não íntegra a sangue e outros fluidos orgânicos, por material perfurocortante ou não; a unidade de análise é o trabalhador acidentado notificado (um registro por ficha), independentemente do vínculo empregatício. O instrumento é a *Ficha de Investigação — Acidente de Trabalho com Exposição à Material Biológico* (CID-10 Z20.9), que cobre dados gerais, notificação individual, residência, antecedentes epidemiológicos (ocupação, situação no mercado de trabalho, tempo na ocupação), dados da empresa contratante (CNAE, CNPJ/CPF) e dados específicos do acidente e do paciente-fonte.

A série publicada no FTP inicia em 2006, com implantação nacional do Sinan Net. Os arquivos de 2023 a 2026 estão no diretório PRELIM (dados preliminares, sujeitos a revisão até o fechamento), enquanto as competências até 2022 estão em FINAIS. Por ser uma base sentinela da RENAST, a cobertura depende da capilaridade dos serviços notificadores, com subnotificação conhecida em estados menos estruturados.

Principais usos: perfil de exposição ocupacional por categoria profissional e CBO, avaliação de adesão a protocolos de profilaxia pós-exposição (HIV, hepatites B e C), monitoramento de uso de EPI, acompanhamento sorológico e cálculo de taxas de incidência de acidentes biológicos em profissionais de saúde.

### Cobertura observada

- Índice do FTP (2026-10): 21 arquivos, de 2006 a 2026, 1 UF(s) com arquivos, última atualização em 2026-10-23.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2006 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo `ACBIBR10.dbc` (leiaute do SINAN Net; fichas e leiautes podem variar entre anos, por isso a lista reflete esse arquivo). Os arquivos públicos não trazem identificadores individuais como número da notificação (`NU_NOTIFIC`) nem data de nascimento completa. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

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
| `CNAE` | String | Atividade econômica da empresa contratante (CNAE). |
| `PERCUTANEA` | String | Exposição percutânea (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `PELE_INTEG` | String | Exposição em pele íntegra (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `PELE_NAO_I` | String | Exposição em pele não íntegra (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `OUTRO_EXP` | String | Outro tipo de exposição (descrição em `OUT_EXP_DE`). |
| `MAT_ORG` | String | Material orgânico envolvido (descrição de outros em `MAT_ORG_DE`). |
| `TIPO_ACID` | String | Circunstância do acidente. |
| `AGENTE` | String | Agente (objeto) causador do acidente. |
| `LUVA` | String | Uso de luvas (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `AVENTAL` | String | Uso de avental (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `OCULOS` | String | Uso de óculos (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `MASCARA` | String | Uso de máscara (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `FACIAL` | String | Uso de protetor facial (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `BOTA` | String | Uso de botas (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `VACINA` | String | Trabalhador vacinado contra hepatite B. |
| `ANTI_HIV` | String | Resultado do anti-HIV do trabalhador no momento do acidente. |
| `HBSAG` | String | Resultado do HBsAg do trabalhador. |
| `ANTI_HBS` | String | Resultado do anti-HBs do trabalhador. |
| `ANTI_HCV` | String | Resultado do anti-HCV do trabalhador. |
| `FONTE` | String | Paciente-fonte conhecido. |
| `FO_HBSAG` | String | HBsAg do paciente-fonte. |
| `FO_ANT_HIV` | String | Anti-HIV do paciente-fonte. |
| `FO_ANT_HBC` | String | Anti-HBc do paciente-fonte. |
| `FO_ANT_HCV` | String | Anti-HCV do paciente-fonte. |
| `SEM_QUIMIO` | String | Sem quimioprofilaxia (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `RECUSA_QUI` | String | Recusa da quimioprofilaxia (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `AZT3TC` | String | Esquema de quimioprofilaxia AZT+3TC. |
| `AZT3TC_IND` | String | Esquema AZT+3TC+indinavir. |
| `AZT3TC_NFV` | String | Esquema AZT+3TC+nelfinavir. |
| `IMU_HEP_B` | String | Imunoglobulina humana anti-hepatite B. |
| `VAC_HEP_B` | String | Vacinação contra hepatite B após o acidente. |
| `OUTRO_ARV` | String | Outro esquema antirretroviral (descrição em `OUT_ARV_ES`). |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito, quando aplicável. |
| `CAT` | String | Foi emitida a Comunicação de Acidente do Trabalho (CAT)? |
| `MUCOSA` | String | Exposição em mucosa (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |

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
| `dt_acid` | `DT_ACID` | data | Data do acidente | — | todos |
| `sem_acid` | `SEM_ACID` | texto | Semana epidemiológica do acidente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
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
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Ocupação do indivíduo que sofreu o agravo | — | todos |
| `sit_trab` | `SIT_TRAB` | texto | Situação no mercado de trabalho. Situação de trabalho do indivíduo que sofreu o agravo | 1. Empregado registrado com carteira assinada 2. Empregado não registrado 3. Autônomo/cont a própria 4. Servidor público estatuário | todos |
| `nutempo` | `NUTEMPO` | texto | Número que compõe o tempo (de exposição ou de ocorrência); a unidade está em `tptempo` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tptempo` | `TPTEMPO` | texto | Unidade do tempo informado em `nutempo` (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `cnae` | `CNAE` | texto | Código da atividade Econômica(CNAE). Classificação Nacional da Atividade Econômica do Contratante | — | todos |
| `uf_emp` | `UF_EMP` | texto | UF. Unidade da Federação da empresa contratante | — | todos |
| `mun_emp` | `MUN_EMP` | texto | Município. Código (IBGE) | — | todos |
| `terceiriza` | `TERCEIRIZA` | texto | O empregador é empresa Terceirizada. O empregador é de alguma empresa terceirizada | 01- Sim 02- Não 03- Não se aplica 09- Ignorado | todos |
| `percutanea` | `PERCUTANEA` | texto | Tipo de exposição Percutânea. – | 1. Sim 2. Não 9. Ignorado | todos |
| `pele_integ` | `PELE_INTEG` | texto | Tipo de exposição Pele (integra). – | 1. Sim 2. Não 9. Ignorado | todos |
| `pele_nao_i` | `PELE_NAO_I` | texto | Tipo de exposição Pele (Não íntegra). – | 1. Sim 2. Não 9. Ignorado | todos |
| `outro_exp` | `OUTRO_EXP` | texto | Tipo de exposição Outro. – | 1. Sim 2. Não 9. Ignorado | todos |
| `out_exp_de` | `OUT_EXP_DE` | texto | Tipo de exposição Outro (especificar). Se outro tipo de exposição (Especificar) | — | todos |
| `mat_org` | `MAT_ORG` | texto | Material orgânico | 1-Sangue 2-Líquor 3-Líquido pleural 4-Líquido ascítico 5-Líquido amniótico 6-Fluído com sangue 7-Soro/plasma 8-Outros 9-Ignorado | todos |
| `mat_org_de` | `MAT_ORG_DE` | texto | Outro material orgânico especificar. Se outro tipo de material orgânico (Especificar) | — | todos |
| `tipo_acid` | `TIPO_ACID` | texto | Circunstância do Acidentado. – | 01 - Administ. de medicação endovenosa 02 - Administ. de medicação intramuscular 03 - Administ. de medicação subcutânea 04 - Administ. de | todos |
| `agente` | `AGENTE` | texto | Agente. – | 1-Agulha com lúmen (luz) | todos |
| `luva` | `LUVA` | texto | Uso de EPI (aceita mais de uma opção) LUVA. – | 1- Sim 2 - Não 9 - Ignorado | todos |
| `avental` | `AVENTAL` | texto | Uso de EPI (aceita mais de uma opção) Avental. – | 1- Sim 2 - Não 9 - Ignorado | todos |
| `oculos` | `OCULOS` | texto | Uso de EPI (aceita mais de uma opção) Óculos. – | 1- Sim 2 - Não 9 - Ignorado | todos |
| `mascara` | `MASCARA` | texto | Uso de EPI (aceita mais de uma opção) Máscara. – | 1- Sim 2 - Não 9 - Ignorado | todos |
| `facial` | `FACIAL` | texto | Uso de EPI (aceita mais de uma opção) Proteção Facial. – | 1- Sim 2 - Não 9 - Ignorado | todos |
| `bota` | `BOTA` | texto | Uso de EPI (aceita mais de uma opção) Bota. – | 1- Sim 2 - Não 9 - Ignorado | todos |
| `vacina` | `VACINA` | texto | Situação vacinal do acidentado em relação a hepatite B (3 Doses) | 1- Vacinado 2- Não vacinado 9 - Ignorado | todos |
| `anti_hiv` | `ANTI_HIV` | texto | Resultados de exame do acidentado (no momento do acidente – Data Zero) Anti - HIV | 1- Positivo 2- Negativo 3- Inconclusiv o 4- Não realizado 9- Ignorado | todos |
| `hbsag` | `HBSAG` | texto | Resultados de | 1-Positivo | todos |
| `anti_hbs` | `ANTI_HBS` | texto | Resultados de exame do acidentado (no momento do acidente – Data Zero) Anti - Hbs | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado 9- Ignorado | todos |
| `anti_hcv` | `ANTI_HCV` | texto | Resultados de exame do acidentado (no momento do acidente – Data Zero) Anti - HCV | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado 9- Ignorado | todos |
| `fonte` | `FONTE` | texto | Paciente fonte conhecida | 1- Sim 2- Não 9- Ignorado | todos |
| `fo_hbsag` | `FO_HBSAG` | texto | Se sim, qual o resultado dos testes sorológicos HbsAg | 1-Positivo 2-Negativo 3-Inconclusivo 4-Em andamento 5-Não realizado 9-Ignorado | todos |
| `fo_ant_hiv` | `FO_ANT_HIV` | texto | Se sim, qual o resultado dos testes sorológicos Anti - Hiv | 1-Positivo 2-Negativo 3-Inconclusivo 4-Em andamento 5-Não realizado 9-Ignorado | todos |
| `fo_ant_hbc` | `FO_ANT_HBC` | texto | Se sim, qual o resultado dos testes sorológicos Anti - HBc | 1-Positivo 2-Negativo 3-Inconclusivo 4-Em andamento 5-Não realizado 9-Ignorado | todos |
| `fo_ant_hcv` | `FO_ANT_HCV` | texto | Se sim, qual o resultado dos testes sorológicos Anti - HCV | 1-Positivo 2-Negativo 3-Inconclusivo 4-Em andamento 5-Não realizado 9-Ignorado | todos |
| `sem_quimio` | `SEM_QUIMIO` | texto | Conduta no momento do acidente Sem indicação de quimioprofilaxia | 1- Sim 2- Não 9-Ignorado | todos |
| `recusa_qui` | `RECUSA_QUI` | texto | Conduta no momento do acidente Recusou quimioprofilaxia indicada | 1-Sim 2-Não 9-Ignorado | todos |
| `azt3tc` | `AZT3TC` | texto | Conduta no momento do acidente AZT+3TC | 1-Sim 2-Não 9-Ignorado | todos |
| `azt3tc_ind` | `AZT3TC_IND` | texto | Conduta no momento do acidente AZT+3TC+Indinavir. r | 1-Sim 2-Não 9-Ignorado | todos |
| `azt3tc_nfv` | `AZT3TC_NFV` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `imu_hep_b` | `IMU_HEP_B` | texto | Conduta no momento do acidente Imunoglobulina humana contra hepatite B (HBIG) | 1-Sim 2-Não 9-Ignorado | todos |
| `vac_hep_b` | `VAC_HEP_B` | texto | Conduta no momento do acidente Vacina contra hepatite B. b | 1-Sim 2-Não 9-Ignorado | todos |
| `outro_arv` | `OUTRO_ARV` | texto | Conduta no momento do acidente Outro esquema de ARV | 1-Sim 2-Não 9-Ignorado | todos |
| `out_arv_es` | `OUT_ARV_ES` | texto | Conduta no momento do acidente Especifique | — | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso | 1-Alta com conversão sorológica Especificar vírus 2-Alta sem conversão sorológica 3-Alta paciente fonte negativo 4-Abandono 5-Óbito por acidente com exposição a material biológico 6-Óbito por outra causa 9-Ignorado | todos |
| `evo_outr` | `EVO_OUTR` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `dt_obito` | `DT_OBITO` | data | Se Óbito, Data do Óbito | — | todos |
| `cat` | `CAT` | texto | Foi emitida a Comunicação de Acidente no Trabalho - CAT | 1 – Sim 2 – Não 3 – Não se aplica 9 – Ignorado | todos |
| `mucosa` | `MUCOSA` | texto | Tipo de exposição Mucosa (oral / ocular). – | 1. Sim 2. Não 9. Ignorado | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-acbi`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 3, inteiro: 1, texto: 66.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-acbi.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- a tabela `1` do SINAN tem apenas o agravo específico, mas os campos de ocupação e CNAE podem vir incompletos em notificações de baixa qualidade; o profissional de saúde é a categoria predominante, e o `ID_OCUPA_N` deve ser agregado por grandes grupos. `ID_AGRAVO` é sempre `Z20.9`. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. Arquivos do diretório PRELIM (2023+) são preliminares e substituídos pelos finais; como `NU_NOTIFIC` não consta dos arquivos públicos, deduplique por combinação de campos (ex.: `ID_UNIDADE`, `DT_NOTIFIC`, `ID_MN_RESI`, `ANO_NASC`, `CS_SEXO`) ao combinar as duas fontes. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-acbi").glob("**/*.parquet"))
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
datasus-fetcher list sinan-acbi

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-acbi -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-acbi
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (DRT Acidente de Trabalho Biológico): https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Saúde do Trabalhador: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- RENAST — Rede Nacional de Atenção Integral à Saúde do Trabalhador: https://www.gov.br/saude/pt-br/composicao/svsa/saude-do-trabalhador/renast
