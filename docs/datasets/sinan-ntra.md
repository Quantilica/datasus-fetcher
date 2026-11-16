---
dataset:
  id: sinan-ntra
  fonte: datasus
  titulo: Notificação de Tracoma
  resumo: 'Notificação de Tracoma do DATASUS: uma ficha de notificação/investigação de notificação de Tracoma.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2010'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de notificação de Tracoma
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 27
  unidades_de_medida:
    nu_casoexa: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_casopos: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Notificação de Tracoma (`sinan-ntra`)

## Resumo

Notificações individuais de casos de tracoma, de notificação compulsória no SINAN. Cada linha representa uma ficha de notificação/investigação de um caso de tracoma (conjuntivite e ceratoconjuntivite por *Chlamydia trachomatis*), atendido em serviços de saúde.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório PRELIM, 2025–2026; Finais até 2024)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `NTRA` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `NTRA` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `NTRABR24.dbc`, em que `NTRA` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-ntra/<AAAA>/sinan-ntra_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-ntra/2024/sinan-ntra_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`Notificação Individual de Tracoma`) é distribuído no Portal SINAN; não há PDF por agravo no FTP.

## Conteúdo

O tracoma é uma doença ocular inflamatória crônica causada pela bactéria *Chlamydia trachomatis*, classificada pela OMS como doença tropical negligenciada (DTN) e incluída entre as metas de eliminação como problema de saúde pública até 2030. No Brasil, é agravo de notificação compulsória conforme a Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023) e integra o Programa de Vigilância e Controle do Tracoma da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS).

O evento gerador é todo caso suspeito ou confirmado de tracoma, tipicamente em populações de baixa renda, áreas rurais, periferias urbanas e comunidades ribeirinhas, associado a condições precárias de saneamento, aglomeração e higiene. O diagnóstico é clínico-oftalmológico (classificação OMS: TF, TI, TS, TT, CO) e pode ser confirmado por exame laboratorial. A unidade de análise é o caso notificado (um registro por ficha).

O instrumento é a *Ficha de Notificação/Investigação Individual — Tracoma*, que registra a forma clínica (tracoma folicular TF, inflamatório intenso TI, cicatricial TS, trichiasis tracomatoso TT, opacificação da córnea CO), dados de exames, tratamento realizado e encaminhamento para cirurgia (quando indicado) e investigação de comunicantes. A série no FTP inicia em 2010; os dados de 2025 e 2026 estão em PRELIM e sujeitos a revisão.

Principais usos: vigilância da forma e distribuição do tracoma, monitoramento de indicadores de eliminação (prevalência de TF em crianças de 1 a 9 anos), avaliação de campanhas de tratamento em massa com azitromicina e embasamento de ações de saneamento e educação em saúde.

### Cobertura observada

- Índice do FTP (2026-10): 17 arquivos, de 2010 a 2026, 1 UF(s) com arquivos, última atualização em 2026-05-29.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2010 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

As colunas abaixo foram extraídas do cabeçalho do arquivo mais recente (`NTRABR26.dbc`). Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação do inquérito. |
| `NU_ANO` | String | Ano da notificação. |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado (A71). |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE, 7 dígitos). |
| `ID_UNIDADE` | String | Código CNES da unidade notificadora (7 dígitos). |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `ID_REGIONA` | String | Código da regional de saúde. |
| `CS_INQUERI` | String | Tipo de inquérito realizado. |
| `NU_CASOEXA` | Inteiro | Número de casos examinados. |
| `NU_CASOPOS` | Inteiro | Número de casos positivos. |
| `DT_DIGITA` | Data (AAAAMMDD) | Data de digitação do registro. |
| `DT_TRANSUS` / `DT_TRANSDM` / `DT_TRANSSM` / `DT_TRANSRM` / `DT_TRANSRS` / `DT_TRANSSE` | Data (AAAAMMDD) | Datas de transferência do registro entre as esferas do SINAN (US, distrital/municipal, estadual/regional, federal). |
| `NU_LOTE_V` / `NU_LOTE_H` | String | Números dos lotes de transferência vertical e horizontal. |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação | — | todos |
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno) | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `cs_inqueri` | `CS_INQUERI` | texto | Indica caso identificado em inquérito (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_casoexa` | `NU_CASOEXA` | inteiro | Número de casos examinados (inquérito) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_casopos` | `NU_CASOPOS` | inteiro | Número de casos positivos (inquérito) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_transus` | `DT_TRANSUS` | data | Data de transferência da unidade de saúde. Data de Transferência do registro da Unidade de Saúde para do nível superior do sistema | — | todos |
| `dt_transdm` | `DT_TRANSDM` | data | Data de transferência do distrito municipal. Data de Transferência do registro do Distrito Municipal para do nível superior do sistema | — | todos |
| `dt_transsm` | `DT_TRANSSM` | data | Data de transferência da secretaria municipal de saúde. Data de Transferência do registro da secretaria municipal para do nível superior do sistema | — | todos |
| `dt_transrm` | `DT_TRANSRM` | data | Data de transferência da regional municipal. Data de Transferência do registro da Regional Municipal para do nível superior do sistema | — | todos |
| `dt_transrs` | `DT_TRANSRS` | data | Data de transferência da regional de saúde. Data de Transferência do registro da Regional de Saúde para do nível superior do sistema | — | todos |
| `dt_transse` | `DT_TRANSSE` | data | Data de transferência da secretaria estadual de saúde. Data de Transferência do registro da Secretaria Estadual para do nível superior do sistema | — | todos |
| `nu_lote` | `NU_LOTE` | texto | Número do lote (campo de controle da transmissão) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_lote_v` | `NU_LOTE_V` | texto | Número do lote vertical. Descrever aqui a estrutura da composição do número do lote | — | todos |
| `nu_lote_h` | `NU_LOTE_H` | texto | Número do lote horizontal | — | todos |
| `nu_sema_ep` | `NU_SEMA_EP` | texto | Semana epidemiológica (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tpuninot` | `TPUNINOT` | texto | Tipo da unidade notificadora (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2010 |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `nu_notific` | `NU_NOTIFIC` | texto | Nº da Notificação. Número da Notificação | — | só em 2015 |
| `ident_micr` | `IDENT_MICR` | texto | Identificação do micro (campo interno) | — | só em 2015 |

## No lake

- **Dataset no lake:** `datasus/sinan-ntra`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 8, inteiro: 2, texto: 17.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-ntra.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- o layout é compacto e traz contagens por notificação de inquérito (`NU_CASOEXA` examinados, `NU_CASOPOS` positivos), sem dados individuais de pacientes; o detalhamento por forma clínica está no dataset `sinan-trac`. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT`. Arquivos do diretório PRELIM são preliminares; deduplique ao combinar as fontes. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 3 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-ntra").glob("**/*.parquet"))
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
datasus-fetcher list sinan-ntra

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-ntra -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-ntra
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (Notificação Individual de Tracoma): https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Tracoma: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- OMS — Eliminação do tracoma como problema de saúde pública (metas 2030): https://www.who.int/health-topics/trachoma
