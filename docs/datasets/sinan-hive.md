---
dataset:
  id: sinan-hive
  fonte: datasus
  titulo: HIV em crianças expostas
  resumo: 'HIV em crianças expostas do DATASUS: uma ficha de notificação/investigação de hIV em crianças expostas.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2015'
    fim: '2024'
  unidade: uma ficha de notificação/investigação de hIV em crianças expostas
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 29
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# HIV em crianças expostas (`sinan-hive`)

## Resumo

Notificações de crianças expostas ao HIV (filhas de mães vivendo com HIV), registradas no SINAN. Cada linha representa uma ficha de acompanhamento de uma criança exposta, do nascimento até a definição do diagnóstico (infectada ou não infectada).

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `HIVE` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `HIVE` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `HIVEBR24.dbc`, em que `HIVE` é o prefixo do agravo, `BR` indica a base nacional (o SINAN publica um único arquivo por ano para o Brasil) e `24` é o ano com 2 dígitos (2024).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-hive/<AAAA>/sinan-hive_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-hive/2024/sinan-hive_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
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
  - O dicionário de dados desta base (`Ficha de Investigação Criança Exposta ao HIV`) está contido em `Docs_TAB_SINAN.zip`; os dicionários por agravo não são publicados como arquivos separados.

## Conteúdo

A notificação de criança exposta ao HIV foi instituída para acompanhar a transmissão vertical, dentro do conjunto de agravos de HIV/aids sob coordenação do DATHI/SVSA. A ficha é distinta das fichas de HIV em crianças infectadas (`sinan-hivc`) e de gestante (`sinan-hivg`).

O evento gerador é o nascimento (ou parto) de criança de mulher vivendo com HIV, notificado na maternidade ou no serviço que acompanha a criança. A unidade de análise é a criança exposta. Os campos registram dados da mãe e do pré-natal, uso de antirretrovirais na gestação, no parto e pela criança, tipo de parto, aleitamento, exames de seguimento e a classificação final (infectada, não infectada ou indeterminada).

No FTP, a série começa em 2015 (10 arquivos nacionais até 2024), refletindo a implantação da ficha em 2014-2015. É a base de referência para o cálculo da taxa de transmissão vertical do HIV.

Usos: proporção de crianças expostas com diagnóstico definido, taxa de transmissão vertical, cobertura de profilaxia na gestação, parto e neonatal, e avaliação das ações do Plano de Eliminação da Transmissão Vertical.

### Cobertura observada

- Índice do FTP (2026-10): 10 arquivos, de 2015 a 2024, 1 UF(s) com arquivos, última atualização em 2025-02-25.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2015 a 2024), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo real `HIVEBR24.dbc` do FTP (campos da ficha do SINAN Net; o leiaute pode variar entre anos). Os microdados públicos não trazem número de notificação nem data de nascimento completa, apenas campos não identificáveis. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

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
| `CLASSI_FIN` | String | Classificação final do caso. |
| `CRITERIO` | String | Critério de confirmação/definição do caso. |
| `DOENCA_TRA` | String | Indica se a doença é relacionada ao trabalho. |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito. |
| `DT_ENCERRA` | Data (AAAAMMDD) | Data de encerramento da investigação. |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças – CID 10) e nomes dos agravos classificados como notificação compulsória (nacional, estadual ou municipal) e as síndromes (febre hemorragia aguda; respiratória aguda; diarréia aguda; sanguinolenta; neurológica aguda; insuficiência renal aguda; outras síndromes | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológica da notificação (campo interno). Semanas do calendário epidemiológico padronizado | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação. Código do município onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. O nome está associado ao código na tabela de municípios | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_diag` | `DT_DIAG` | data | Data dos primeiros sintomas / Diagnóstico. Data dos primeiros sintomas do caso de agravo agudo. Data do diagnóstico do caso de agravo crônico e DRTs Data do acidente nos acidentes da saúde do trabalhador | — | todos |
| `sem_diag` | `SEM_DIAG` | texto | Semana epidemiológica dos primeiros sintomas/ diagnósticos. (campo interno). Semanas do calendário epidemiológico padronizado | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece ao seguinte critério: 1o dígito: 1 – Hora 2 – Dia 3 – Mês 4 – Ano Ex: 3009 – nove meses, 4018 – dezoito anos | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M – Masculino F – Feminino I – Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1 – 1º Trimestre 2 – 2º Trimestre 3 – 3º Trimestre | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1 – Branca 2 – Preta 3 – Amarela (pessoa que se declarou de raça amarela) 4 – Parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5 – Indígena (pessoa que se declarou indígena ou índia) | 1 – Branca 2 – Preta 3 – Amarela 4 – Parda 5 – Indígena 9 – Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. Série e grau que a pessoa está frequentando ou frequentou considerando a última série concluída com aprovação ou grau de instrução do paciente por ocasião da notificação | 0 – Analfabeto 1 – 1ª a 4ª série incompleta do EF 2 – 4ª série completa do EF (antigo 1° grau) 3 – 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4 – Ensino fundamental completo (antigo ginásio ou 1° grau)... | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência. Código do município de residência do caso notificado. O nome está associado ao código na tabela de municípios | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil). País onde residia o paciente por ocasião da notificação | — | todos |
| `dt_invest` | `DT_INVEST` | data | Data da investigação. Data de início da investigação do caso | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo de atividade econômica do paciente refere-se as atividades econômicas desenvolvidas nos processos de produção do setor primário (agricultura e extrativismo); secundário (indústria) ou terciário (serviços e comércio) | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final. Anexo I | — | todos |
| `criterio` | `CRITERIO` | texto | Critério confirmação. Anexo I | — | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho. Indica se a doença está ou não relacionada ao trabalho | 1 - Sim 2 - Não 9 - Ignorado | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. Anexo I | — | todos |
| `dt_obito` | `DT_OBITO` | data | Data de óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data de encerramento. Data do encerramento | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-hive`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 5, inteiro: 1, nulo (vazio nas amostras): 1, texto: 23.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-hive.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- Cada criança deve ser seguida até o encerramento; fichas abertas (`DT_ENCERRA` nula) têm classificação final pendente. Dados mais recentes são preliminares. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (UF de notificação) ou `SG_UF`/`ID_MN_RESI` (residência) conforme a pergunta, pois os dois podem diferir. Arquivos do diretório PRELIM são preliminares e substituídos pelos finais; prefira sempre os arquivos finais quando o mesmo ano existir nas duas fontes, evitando somar PRELIM e FINAIS. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-hive").glob("**/*.parquet"))
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
datasus-fetcher list sinan-hive

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-hive -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-hive
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS): https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Protocolo Clínico e Diretrizes Terapêuticas para Prevenção da Transmissão Vertical de HIV, Sífilis e Hepatites Virais (MS)
