---
dataset:
  id: sinan-sifg
  fonte: datasus
  titulo: Sífilis em Gestante
  resumo: 'Sífilis em Gestante do DATASUS: uma ficha de notificação/investigação de sífilis em Gestante.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de sífilis em Gestante
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 34
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Sífilis em Gestante (`sinan-sifg`)

## Resumo

Notificações de sífilis em gestantes (incluindo parturientes e puérperas) registradas no SINAN. Cada linha representa uma ficha de notificação de uma gestação com sífilis.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `SIFG` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `SIFG` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `SIFGBR25.dbc`, em que `SIFG` é o prefixo do agravo, `BR` indica a base nacional (o SINAN publica um único arquivo por ano para o Brasil) e `25` é o ano com 2 dígitos (2025).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-sifg/<AAAA>/sinan-sifg_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-sifg/2024/sinan-sifg_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
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
  - O dicionário de dados desta base (`Ficha de Investigação Sífilis em Gestante`) está contido em `Docs_TAB_SINAN.zip`; os dicionários por agravo não são publicados como arquivos separados.

## Conteúdo

A sífilis em gestante é de notificação compulsória desde 2005 (Portaria nº 33/2005), sob coordenação do DATHI/SVSA, como estratégia de eliminação da sífilis congênita. A ficha acompanha o rastreio no pré-natal e o tratamento da gestante e dos parceiros.

O evento gerador é o diagnóstico de sífilis durante a gestação, no parto ou no puerpério, com resultados de teste treponêmico e não treponêmico, classificação clínica e esquema de tratamento. A unidade de análise é a gestação notificada, e uma mesma mulher pode ter várias fichas.

O FTP traz arquivos nacionais anuais de 2007 a 2025 (cerca de 23 MB). A taxa de detecção cresceu de forma acentuada ao longo da década de 2010, em parte pela ampliação do diagnóstico e da notificação.

Usos: taxa de detecção de sífilis em gestantes por mil nascidos vivos, momento do diagnóstico (trimestre), adequação do tratamento, tratamento do parceiro e relação com a sífilis congênita (`sinan-sifc`).

### Cobertura observada

- Índice do FTP (2026-10): 19 arquivos, de 2007 a 2025, 1 UF(s) com arquivos, última atualização em 2026-06-30.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2025), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo real `SIFGBR25.dbc` do FTP (campos da ficha do SINAN Net; o leiaute pode variar entre anos). Os microdados públicos não trazem número de notificação nem data de nascimento completa, apenas campos não identificáveis. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (individual ou negativa). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado. |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
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
| `ID_OCUPA_N` | String | Ocupação (CBO, 6 dígitos). |
| `PRE_UFREL` | String | UF de realização do pré-natal. |
| `PRE_MUNIRE` | String | Município de realização do pré-natal (código IBGE). |
| `TPEVIDENCI` | String | Tipo de evidência clínica. |
| `TPTESTE1` | String | Tipo do 1º teste de sífilis. |
| `DSTITULO1` | String | Titulação do 1º teste (texto). |
| `DTTESTE1` | Data (AAAAMMDD) | Data do 1º teste. |
| `TPCONFIRMA` | String | Tipo de confirmação (texto de até 10 caracteres). |
| `TPESQUEMA` | String | Esquema de tratamento da gestante. |
| `DSMOTIVO` | String | Motivo do não tratamento ou tratamento parcial (texto). |
| `TPMOTPARC` | String | Tipo do motivo do tratamento parcial. |
| `TPESQPAR` | String | Esquema de tratamento do parceiro. |
| `TRATPARC` | String | Parceiro tratado. |
| `CLASSI_FIN` | String | Classificação final do caso. |

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
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Variável Essencial Tabela de ocupação padronizada do Sinan | — | todos |
| `pre_ufrel` | `PRE_UFREL` | texto | UF. Sigla da Unidade federada do local da realização do pré -natal | — | todos |
| `pre_munire` | `PRE_MUNIRE` | texto | Município de realização do pré-natal. l | — | todos |
| `tpevidenci` | `TPEVIDENCI` | texto | Classificação Clinica. Classificação clínica da sífilis na gestação 1 - sífilis primária - cancro duro; 2 - sífilis secundária – lesões cutâneo-mucosas (roséolas, sifílides papulosas, condiloma plano, alopécia); 3 - sífilis terciária – lesões cutâneo- mucosas (tubérculos ou gomas); alterações neurológicas (tabes dorsalis, demência); alterações cardiovasculares (aortite sifilítica, aneurisma aórtico); alterações ar... | 1 - Primária 2 - Secundária 3 - Terciária 4 - Latente 9 - Ignorado | todos |
| `tpteste1` | `TPTESTE1` | texto | treponêmico no pré-natal. do teste não treponêmico preconizado para a primeira consulta de pré- natal. Entende-se como teste não treponêmicos o VDRL e o RPR; | 2 - Não reagente 3 - Não realizado 9 - Ignorado | todos |
| `dstitulo1` | `DSTITULO1` | texto | Título. Resultado da titulação do VDRL/RPR | — | todos |
| `dtteste1` | `DTTESTE1` | data | Data. Data da realização do teste não treponêmico no pré-natal | — | todos |
| `tpconfirma` | `TPCONFIRMA` | texto | Teste treponêmico no pré-natal | 1 - Reagente 2 - Não reagente 3 - Não realizado 9 - Ignorado | todos |
| `tpesquema` | `TPESQUEMA` | texto | Esquema de tratamento. Esquema de tratamento preconizado pelo Ministério da Saúde e disponível no Manual de Diretrizes para o Controle da Sífilis Congênita | 1 - Penicilina G benzatina 2.400.000UI 2 - Penicilina G benzatina 4.800.000UI 3 - Penicilina G benzatina 7.200..000UI 4 - Outro esquema 5 - Não realizado 9 - Ignorado | todos |
| `dsmotivo` | `DSMOTIVO` | texto | Outro motivo. Descreve o outro motivo pelo qual o parceiro não foi tratado | — | todos |
| `tpmotparc` | `TPMOTPARC` | texto | Motivo para o não tratamento. Relata o motivo pelo qual o parceiro não foi tratado | 1 - parceiro não teve mais contato com a | todos |
| `tpesqpar` | `TPESQPAR` | texto | Esquema de tratamento prescrito ao parceiro. o | 1 - penicilina g benzatina 2.400.000ui 2 - penicilina g benzatina 4.800.000ui 3 - penicilina g benzatina 7.200..000ui 4 - outro esquema 5 - não realizado 9 - ignorado | todos |
| `tratparc` | `TRATPARC` | texto | Parceiro tratado concomitantem ente à gestante. Verifica se o parceiro foi tratado concomitantemente à gestante | 1 - sim 2 - não 9 - ignorado | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-sifg`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 3, texto: 31.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-sifg.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- A idade é da gestante. Reingresso de notificações da mesma mulher em gestações distintas é esperado; não há identificador único de pessoa nos microdados públicos. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (UF de notificação) ou `SG_UF`/`ID_MN_RESI` (residência) conforme a pergunta, pois os dois podem diferir. Arquivos do diretório PRELIM são preliminares e substituídos pelos finais; prefira sempre os arquivos finais quando o mesmo ano existir nas duas fontes, evitando somar PRELIM e FINAIS. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-sifg").glob("**/*.parquet"))
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
datasus-fetcher list sinan-sifg

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-sifg -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-sifg
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Boletim Epidemiológico de Sífilis (SVSA/MS): https://www.gov.br/aids/pt-br/centrais-de-conteudo/boletins-epidemiologicos
- Guia de Vigilância em Saúde (SVSA/MS): https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
