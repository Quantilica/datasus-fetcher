---
dataset:
  id: sih-er
  fonte: datasus
  titulo: ER - AIH Rejeitadas com código de erro
  resumo: 'ER - AIH Rejeitadas com código de erro do DATASUS: um erro de processamento associado a uma AIH rejeitada.'
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2011-01
    fim: em-curso
  unidade: um erro de processamento associado a uma AIH rejeitada
  granularidade:
    espacial: estabelecimento (CNES) e município de residência do paciente; um arquivo por UF
    temporal: dia da internação e da saída; competência de processamento (mês)
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e competência mensal
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 13
  unidades_de_medida:
    sequencia: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# ER - AIH Rejeitadas com código de erro (`sih-er`)

## Resumo

`sih-er` registra os **erros de processamento das AIH rejeitadas**: cada linha associa uma AIH rejeitada (por número, estabelecimento e datas) ao **código do erro** (`CO_ERRO`) que motivou a rejeição. É o complemento diagnóstico do `sih-rj`, indispensável para entender por que uma internação não foi paga.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/SIHSUS/200801_/Doc`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SIHSUS/200801_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIHSUS/200801_/Dados` | `ER` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `ERSP2401.dbc` — `ER` (AIH Rejeitadas com código de erro) + `SP` (UF) + `24` (ano 2024) + `01` (mês de competência).
- **No armazenamento local do `datasus-fetcher`**: `data/sih-er/<AAAAMM>/sih-er_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sih-er/202401/sih-er_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/IT_SIHSUS_1603.pdf` (Informe Técnico do SIHSUS, 57 KB, 2016) é o dicionário oficial de variáveis; `Auxiliar/TAB_SIH.zip` (~6,1 MB, tabelas e conversores `.cnv`/`.def` atuais) e as versões históricas `TAB_SIH_199201-199712.zip`, `TAB_SIH_199801-200307.zip` e `TAB_SIH_200308-200712.zip` trazem as tabelas de procedimentos, CID e códigos usadas em cada fase.

## Conteúdo

O Sistema de Informações Hospitalares do SUS (SIH/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES), com processamento e disseminação a cargo do DATASUS — e tem como finalidade operacionalizar o pagamento das internações realizadas em hospitais públicos e privados conveniados ao SUS. Por ser um sistema de faturamento, cobre apenas a assistência financiada pelo SUS (não inclui saúde suplementar nem internações particulares) e é a principal fonte nacional para estudar morbidade hospitalar, perfil assistencial e gasto hospitalar.

O evento gerador é a **crítica de consistência** do processamento da AIH, que grava, para cada inconsistência encontrada, o código de erro correspondente (tabela de críticas do SIHSUS). A unidade de análise é a **ocorrência de erro por AIH e competência**; uma AIH com múltiplas críticas pode gerar mais de uma linha, e `SEQUENCIA`/`REMESSA` identificam o lote do gestor. Cada hospital preenche a Autorização de Internação Hospitalar (AIH) e a remete mensalmente ao gestor municipal/estadual, que a valida e a envia ao DATASUS para processamento na competência (`ANO_CMPT`/`MES_CMPT`). O processamento classifica cada AIH como aprovada (arquivo RD), rejeitada (RJ/ER) e detalha os atos profissionais (SP).

O inventário do FTP inicia em 2011-01 (embora o RJ comece em 2008-01) e segue até a competência corrente. O arquivo é pequeno (~0,3 GB para 4.958 arquivos) e tem leiaute fixo de 13 campos, bem distinto do RD: traz apenas identificação da AIH, datas, municípios e o erro. A tabela de significado dos códigos `CO_ERRO` encontra-se nas tabelas auxiliares do SIH (`TAB_SIH.zip`) e no Informe Técnico do SIHSUS.

Aplicações: ranking das causas de rejeição por hospital e município; mensuração do impacto financeiro de cada tipo de erro (quando ligado ao `sih-rj`); apoio à qualificação do faturamento e à capacitação de equipes de faturamento hospitalar; auditoria de gestores que enviam remessas com alto índice de erros; e monitoramento da evolução da qualidade da informação hospitalar.

### Cobertura observada

- Índice do FTP (2026-10): 4984 arquivos, de 2011-01 a 2026-09, 27 UF(s) com arquivos, última atualização em 2026-11-10.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2011-06 a 2026-05), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

13 colunas no arquivo de 2024-01 (`ERAC2401.dbc`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `SEQUENCIA` | Inteiro | Número sequencial do registro dentro da remessa. |
| `REMESSA` | String | Nome da remessa enviada pelo gestor (padrão `HE<código do gestor>…<AAAAMM>.DTS`). |
| `CNES` | String (7) | Estabelecimento que apresentou a AIH. |
| `AIH` | String (13) | Número da AIH rejeitada (equivale a `N_AIH` do RD/RJ). |
| `ANO / MES` | Inteiro | Ano e mês da competência do processamento. |
| `DT_INTER / DT_SAIDA` | String AAAAMMDD → `pl.Date` | Datas de internação e saída informadas. |
| `MUN_MOV` | String (6) | Município do estabelecimento (movimento). |
| `UF_ZI` | String (6) | Código do gestor/UF de gestão. |
| `MUN_RES` | String (6) | Município de residência do paciente. |
| `UF_RES` | String (2) | UF de residência do paciente (código IBGE de 2 dígitos). |
| `CO_ERRO` | String (6) | Código do erro/crítica que causou a rejeição (p.ex. `020081`); consultar tabela de erros do SIH. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `sequencia` | `SEQUENCIA` | inteiro | Sequencial da AIH na remessa. | — | todos |
| `remessa` | `REMESSA` | texto | Número da remessa. | — | todos |
| `cnes` | `CNES` | texto | Código CNES do hospital. | — | todos |
| `aih` | `AIH` | texto | Número da AIH rejeitada | — | todos |
| `dt_inter` | `DT_INTER` | data | Data de internação (AAAAMMDD, convertida para data); o informe técnico a grafa `DI_INTER` | — | todos |
| `dt_saida` | `DT_SAIDA` | data | Data de saída, no formato aaaammdd. | — | todos |
| `mun_mov` | `MUN_MOV` | texto | Município de movimento (do estabelecimento), código IBGE de 6 dígitos | — | todos |
| `uf_zi` | `UF_ZI` | texto | Município Gestor. | — | todos |
| `mun_res` | `MUN_RES` | texto | Município de residência do paciente, código IBGE de 6 dígitos | — | todos |
| `uf_res` | `UF_RES` | texto | UF de residência do paciente | — | todos |
| `co_erro` | `CO_ERRO` | texto | Código do erro de processamento que motivou a rejeição da AIH | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sih-er`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 2, inteiro: 1, texto: 10.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sih-er.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) o par (`AIH`, `CNES`, competência) liga o ER ao `sih-rj`; (ii) pode haver várias linhas por AIH — conte AIH distintas com `n_unique` ao calcular taxas; (iii) o ER só existe a partir de 2011-01, então rejeições anteriores não têm código de erro neste dataset; (iv) o significado de `CO_ERRO` muda com o tempo, use a tabela auxiliar da data correspondente. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sih-er").glob("**/*.parquet"))
dados = pl.concat(  # períodos diferentes têm colunas e tipos diferentes
    [pl.scan_parquet(a, hive_partitioning=True) for a in arquivos],
    how="diagonal_relaxed",
)

(
    dados.group_by("ano", "mes", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "mes", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Pela linha de comando (`datasus-fetcher`)

```bash
# o que o FTP publica para o dataset (arquivos e tamanho)
datasus-fetcher list sih-er

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sih-er -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sih-er
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIHSUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/IT_SIHSUS_1603.pdf`
- **Manual Técnico Operacional do SIH/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **PCDaS/Fiocruz** (SIH/SUS para pesquisa): https://pcdas.icict.fiocruz.br/
