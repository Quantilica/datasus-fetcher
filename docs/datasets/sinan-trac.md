---
dataset:
  id: sinan-trac
  fonte: datasus
  titulo: Inquérito de Tracoma
  resumo: 'Inquérito de Tracoma do DATASUS: uma ficha de notificação/investigação de inquérito de Tracoma.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2009'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de inquérito de Tracoma
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 31
  unidades_de_medida:
    nu_caso: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Inquérito de Tracoma (`sinan-trac`)

## Resumo

Registros de inquéritos populacionais de tracoma (busca ativa de casos) conduzidos no âmbito da vigilância epidemiológica e registrados no SINAN. Cada linha representa o resultado do exame oftalmológico de um indivíduo examinado durante um inquérito domiciliar, escolar ou comunitário.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM, 2025–2026; Finais até 2024)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `TRAC` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `TRAC` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `TRACBR24.dbc`, em que `TRAC` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-trac/<AAAA>/sinan-trac_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-trac/2024/sinan-trac_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`Inquérito de Tracoma`) é distribuído no Portal SINAN; não há PDF por agravo no FTP.

## Conteúdo

O inquérito de tracoma integra o Programa de Vigilância e Controle do Tracoma da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), alinhado à meta da OMS de eliminação do tracoma como problema de saúde pública até 2030. O tracoma é uma ceratoconjuntivite crônica causada por *Chlamydia trachomatis*, doença tropical negligenciada associada a condições precárias de saneamento, aglomeração e higiene, com maior prevalência em áreas rurais, ribeirinhas e periferias urbanas.

O evento gerador é o exame oftalmológico realizado em massa durante inquéritos de busca ativa, com o objetivo de estimar a prevalência de tracoma, especialmente a forma folicular (TF) em crianças de 1 a 9 anos — indicador-chave de eliminação. A unidade de análise é o **indivíduo examinado** (um registro por pessoa), e não apenas os casos confirmados; por isso a base é mais ampla que a notificação individual. O diagnóstico segue a classificação OMS (TF, TI, TS, TT, CO).

O instrumento é a *Ficha de Inquérito de Tracoma*, que registra dados do município e localidade investigada, características do indivíduo examinado (idade, sexo, escola), data do exame, resultado por olho (direito/esquerdo), forma clínica e tratamento. A série no FTP inicia em 2009; os dados de 2025 e 2026 estão em PRELIM e sujeitos a revisão.

Principais usos: cálculo de prevalência de tracoma e de TF em crianças, monitoramento de indicadores de eliminação, avaliação de campanhas de tratamento em massa com azitromicina e priorização de municípios e localidades para intervenção (saneamento, educação em saúde e busca ativa).

### Cobertura observada

- Índice do FTP (2026-10): 18 arquivos, de 2009 a 2026, 1 UF(s) com arquivos, última atualização em 2026-05-29.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2009 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

As colunas abaixo foram extraídas do cabeçalho do arquivo mais recente (`TRACBR26.dbc`). Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação do registro. |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado (A71). |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | String | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE, 6 dígitos). |
| `ID_REGIONA` | String | Código da regional de saúde. |
| `ID_UNIDADE` | String | Código CNES da unidade responsável (7 dígitos). |
| `CS_INQUERI` | String | Tipo de inquérito realizado. |
| `NU_CASO` | Inteiro | Número de casos registrados. |
| `SG_UF` | String | UF de residência (código IBGE de 2 dígitos). |
| `ID_MUNI_RE` | String | Município de residência (código IBGE, 6 dígitos). |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `NU_IDADE_N` | Inteiro | Idade. |
| `FORMA_TF` / `FORMA_TI` / `FORMA_TS` / `FORMA_TT` / `FORMA_CO` | String | Indicadores das formas clínicas: TF (folicular), TI (inflamatório intenso), TS (cicatricial), TT (triquíase) e CO (opacificação da córnea). |
| `ENCAMINHA` | String | Encaminhamento do examinado. |
| `DT_DIGITA` | Data (AAAAMMDD) | Data de digitação do registro. |
| `DT_TRANSUS` / `DT_TRANSDM` / `DT_TRANSSM` / `DT_TRANSRM` / `DT_TRANSRS` / `DT_TRANSSE` | Data (AAAAMMDD) | Datas de transferência do registro entre as esferas do SINAN (US, distrital/municipal, estadual/regional, federal). |
| `NU_LOTE_V` / `NU_LOTE_H` | String | Números dos lotes de transferência vertical e horizontal. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno) | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora | — | todos |
| `cs_inqueri` | `CS_INQUERI` | texto | Indica caso identificado em inquérito (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_caso` | `NU_CASO` | inteiro | Número de casos (inquérito) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_muni_re` | `ID_MUNI_RE` | texto | Município. Código do | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `forma_tf` | `FORMA_TF` | texto | Dado do inquérito de tracoma (`FORMA_TF`) | — | todos |
| `forma_ti` | `FORMA_TI` | texto | Dado do inquérito de tracoma (`FORMA_TI`) | — | todos |
| `forma_ts` | `FORMA_TS` | texto | Dado do inquérito de tracoma (`FORMA_TS`) | — | todos |
| `forma_tt` | `FORMA_TT` | texto | Dado do inquérito de tracoma (`FORMA_TT`) | — | todos |
| `forma_co` | `FORMA_CO` | texto | Dado do inquérito de tracoma (`FORMA_CO`) | — | todos |
| `encaminha` | `ENCAMINHA` | texto | Dado do inquérito de tracoma (`ENCAMINHA`) | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data ou texto | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data ou texto | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data ou texto | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_transrm` | `DT_TRANSRM` | data ou texto | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data ou texto | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data ou texto | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-trac`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 8, inteiro: 2, texto: 27.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-trac.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- este é o **inquérito** (busca ativa, indivíduos examinados), distinto da **notificação individual** de casos em `sinan-ntra`. O denominador é o número de examinados, e a base não deve ser usada para contagem de casos notificados. Os leiautes variam substancialmente entre campanhas, especialmente nos indicadores de forma clínica (`FORMA_*`). Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` ou `ID_MUNICIP` conforme a pergunta. Arquivos do diretório PRELIM (2025+) são preliminares; deduplique com cautela ao combinar as fontes. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Tipo que varia entre períodos:** `dt_transus`, `dt_transdm`, `dt_transsm`, `dt_transrm`, `dt_transrs`, `dt_transse` aparecem com mais de um tipo nas amostras (por exemplo, inteiro em alguns períodos e texto em outros); leia a coluna `Tipo` do dicionário e converta explicitamente antes de empilhar períodos. Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-trac").glob("**/*.parquet"))
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
datasus-fetcher list sinan-trac

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-trac -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-trac
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do inquérito (Inquérito de Tracoma): https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Tracoma: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- OMS — Eliminação do tracoma como problema de saúde pública (metas 2030): https://www.who.int/health-topics/trachoma
