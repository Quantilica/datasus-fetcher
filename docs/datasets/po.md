---
dataset:
  id: po
  fonte: datasus
  titulo: Painel de Oncologia
  resumo: 'Painel de Oncologia do DATASUS: um caso com procedimento diagnóstico ou terapêutico de câncer registrado.'
  orgao: Ministério da Saúde — DATASUS e Instituto Nacional de Câncer (INCA) (Painel de Oncologia)
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/PAINEL_ONCOLOGIA/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2013'
    fim: em-curso
  unidade: um caso com procedimento diagnóstico ou terapêutico de câncer registrado
  granularidade:
    espacial: município de residência e do estabelecimento de tratamento; arquivo nacional
    temporal: ano e mês do diagnóstico e do primeiro tratamento; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional por ano
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 25
  dados_pessoais:
  - coluna: cns_pac
    categoria: Cartão Nacional de Saúde (CNS)
  - coluna: dt_nasc
    categoria: data de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Painel de Oncologia (`po`)

## Resumo

O `po` contém os registros do **Painel de Oncologia**, que reúne informações sobre **diagnóstico e tratamento de câncer** no Brasil a partir de dados do SIA/SUS, SIH/SUS e do Sistema de Informação do Câncer (SISCAN). Cada registro (linha) representa um **caso** em que houve realização de **procedimento diagnóstico e/ou terapêutico oncológico**, com dados de residência e de atendimento, datas de diagnóstico e de tratamento, sexo, idade ao diagnóstico e estadiamento. É a principal base de acesso público para análise da atenção oncológica no SUS.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/PAINEL_ONCOLOGIA/DOC` (`Dicionario_Painel_Oncologia.txt`)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/PAINEL_ONCOLOGIA/AUXILIAR` (`PAINEL_ONCOLOGIA.zip`, `tab_*.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/PAINEL_ONCOLOGIA/DADOS` | `PO` | UF + AAAA (ex.: `BR2013`, `BR2026`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `POBR2013.dbc` — `PO` é o prefixo, `BR` a cobertura nacional e `2013` o ano de quatro dígitos. Existem arquivos de 2013 a 2026, sempre nacionais (não há arquivos por UF).
- **No armazenamento local do `datasus-fetcher`**: `data/po/<AAAA>/po_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/po/2024/po_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `PAINEL_ONCOLOGIA/DOC` está `Dicionario_Painel_Oncologia.txt` (dicionário de variáveis); em `PAINEL_ONCOLOGIA/AUXILIAR` estão `PAINEL_ONCOLOGIA.zip` e `tab_*.zip`, com definições e conversões (CID, procedimento, município, UF) para tabulação no TabWin.

## Conteúdo

O Painel de Oncologia é mantido pelo **Ministério da Saúde/DATASUS** em parceria com o **Instituto Nacional de Câncer (INCA)** e integra as informações de diagnóstico e tratamento oncológicos do SUS. Sua criação responde à necessidade de monitorar a linha do cuidado do câncer — do diagnóstico ao tratamento — usando os registros administrativos de procedimentos (SIA/SUS, SIH/SUS) e os dados do SISCAN.

O **evento gerador** é a **realização de procedimento oncológico** — exame diagnóstico (APAC de diagnóstico), tratamento (quimioterapia, radioterapia, cirurgia oncológica) ou confirmação anatomopatológica. A **unidade de análise é o caso/procedimento oncológico**, identificado pelos campos `ano_diagn`, `anomes_dia` (competência do diagnóstico), `ano_tratam`, `anomes_tra` (competência do tratamento), `uf_resid`/`mun_resid` (residência), `uf_tratam`/`mun_tratam` (estabelecimento de tratamento), `uf_diagn`/`mun_diag` (estabelecimento de diagnóstico), `tratamento`, `diagnostic`, `idade`, `sexo`, `estadiam` (estadiamento), `cnes_diag`/`cnes_trat` (estabelecimentos), `tempo_trat` (tempo até o tratamento), `cns_pac`, `diag_deth`, `dt_diag`, `dt_trat` e `dt_nasc`.

Os arquivos são anuais e **nacionais** (prefixo `POBR` + ano de 4 dígitos, ex.: `POBR2013.dbc` … `POBR2026.dbc`), com cerca de 194 MB no total e 14 arquivos. Não há quebra por UF no FTP — o particionamento é apenas por ano, com um único "uf" (`BR`). Não há diretório preliminar.

Aplicações analíticas típicas: avaliação do acesso e do tempo entre diagnóstico e tratamento, análise de estadiamento ao diagnóstico, distribuição de casos por sexo, idade e localização, comparação entre local de residência e local de tratamento (fluxos/deslocamento), planejamento de redes de atenção oncológica e monitoramento de políticas de controle do câncer.

### Cobertura observada

- Índice do FTP (2026-10): 14 arquivos, de 2013 a 2026, 1 UF(s) com arquivos, última atualização em 2026-10-17.
- Conversão local de amostras (4 arquivo(s) Parquet, de 2013 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `ano_diagn` / `anomes_dia` | Inteiro | Ano e competência (AAAAMM) do diagnóstico |
| `ano_tratam` / `anomes_tra` | Inteiro | Ano e competência (AAAAMM) do tratamento |
| `uf_resid` / `mun_resid` | String | UF e município de residência do paciente |
| `uf_diagn` / `mun_diag` | String | UF e município do estabelecimento de diagnóstico |
| `uf_tratam` / `mun_tratam` | String | UF e município do estabelecimento de tratamento |
| `tratamento` | String | Código do procedimento de tratamento oncológico |
| `diagnostic` | String | Código do procedimento diagnóstico |
| `idade` | Inteiro | Idade (ao diagnóstico) |
| `sexo` | String | Sexo do paciente |
| `estadiam` | String | Estadiamento (extensão da doença ao diagnóstico) |
| `cnes_diag` / `cnes_trat` | String | CNES dos estabelecimentos de diagnóstico/tratamento |
| `tempo_trat` | Inteiro | Tempo decorrido entre diagnóstico e tratamento |
| `cns_pac` | String | Cartão Nacional de Saúde do paciente |
| `diag_deth` | String | Diagnóstico de óbito (quando aplicável) |
| `dt_diag` / `dt_trat` / `dt_nasc` | Data | Datas de diagnóstico, tratamento e nascimento |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `ano_diagn` | `ANO_DIAGN` | texto | Ano de diagnóstico no formato AAAA | — | todos |
| `anomes_dia` | `ANOMES_DIA` | texto | Ano e mês do diagnóstico no formato AAAAMM | — | todos |
| `ano_tratam` | `ANO_TRATAM` | texto | Ano do primeiro tratamento registrado no formato AAAA | — | todos |
| `anomes_tra` | `ANOMES_TRA` | texto | Ano e mês do primeiro tratamento registrado no formato AAAAMM | — | todos |
| `uf_resid` | `UF_RESID` | texto | Cód. da Unidade de Federação de residência, conforme código IBGE | — | todos |
| `mun_resid` | `MUN_RESID` | texto | Cód. da Unidade de Federação de residência + Cód. do Município de residência, conforme código IBGE | — | todos |
| `uf_tratam` | `UF_TRATAM` | texto | Cód. da Unidade de Federação do estabelecimento onde foi registrado o primeiro tratamento, conforme código IBGE | — | todos |
| `mun_tratam` | `MUN_TRATAM` | texto | Cód. da Unidade de Federação de residência + Cód. do Município de residência do estabelecimento onde foi registrado o primeiro tratamento, conforme código IBGE | — | todos |
| `uf_diagn` | `UF_DIAGN` | texto | Cód. da Unidade de Federação do estabelecimento onde foi registrado o diagnóstico, conforme código IBGE | — | todos |
| `mun_diag` | `MUN_DIAG` | texto | Cód. da Unidade de Federação de residência + Cód. do Município de residência do estabelecimento onde foi registrado o diagnóstico, conforme código IBGE | — | todos |
| `tratamento` | `TRATAMENTO` | texto | Primeiro tratamento registrado: 1 - Cirurgia 2 - Quimioterapia 3 - Radioterapia 4 - Quimioterapia + Radioterapia 5 - Sem informação de tratamento | — | todos |
| `diagnostic` | `DIAGNOSTIC` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `idade` | `IDADE` | texto | Idade do(a) paciente no momento do diagnóstico, de 000 a 999, sendo 999 = idade ignorada | — | todos |
| `sexo` | `SEXO` | texto | Sexo do paciente F - Feminino M - Masculino | — | todos |
| `estadiam` | `ESTADIAM` | texto | Estadiamento registrado da doença* 0 - 0 1 - I 2 - II 3 - III 4 - IV 5 - Não se aplica 9 - Ignorado | — | todos |
| `cnes_diag` | `CNES_DIAG` | texto | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde) onde foi registrado o diagnóstico | — | todos |
| `cnes_trat` | `CNES_TRAT` | texto | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde) onde foi registrado o primeiro tratamento | — | todos |
| `tempo_trat` | `TEMPO_TRAT` | texto | Intervalo de tempo entre o diagnóstico e o primeiro tratamento registrados. 99999 – Sem informação de tratamento Para os casos com informação de tratamento, o campo é composto de dois subcampos. O primeiro, de 1 dígito indica se o tratamento ocorreu antes ou depois do laudo de diagnóstico: ( + ) - tratamento com data registrada posterior ao laudo diagnóstico ( - ) – tratamento com data registrada anterior ao laudo... | — | todos |
| `cns_pac` | `CNS_PAC` | texto | Cartão Nacional de Saúde | — | todos |
| `diag_deth` | `DIAG_DETH` | texto | Diagnóstico detalhado registrado Lista de CID - 10ª Revisão C00 ao C97 D00 ao D09 D37 ao D48 | — | todos |
| `dt_diag` | `DT_DIAG` | texto | Data detalhada do diagnóstico registrado no formato DD/MM/AAAA | — | todos |
| `dt_trat` | `DT_TRAT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `dt_nasc` | `DT_NASC` | data | Data de nascimento do paciente no formato DD/MM/AAAA | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/po`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 1, texto: 24.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `po.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- é uma base de **casos agregados por procedimento**, não um registro clínico completo; um mesmo paciente pode aparecer em múltiplos registros (diagnóstico e tratamento); a identificação usa `cns_pac` (atenção à privacidade e ao pareamento); `tempo_trat` pode ser negativo/inconsistente quando o tratamento precede o registro de diagnóstico; a base é nacional e grande (requer processamento por ano); e há quebras de cobertura/atualização entre anos, recomendando verificar o `index.json` antes de séries longas. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/po").glob("**/*.parquet"))
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
datasus-fetcher list po

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync po -o ./data --start 2020 --end 2024 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset po
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/PAINEL_ONCOLOGIA/DADOS`
- **Painel de Oncologia (DATASUS)**: https://datasus.saude.gov.br/painel-oncologia/
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **INCA — Instituto Nacional de Câncer**: https://www.gov.br/inca/pt-br
- **Dicionário `Dicionario_Painel_Oncologia.txt`** e pacote `PAINEL_ONCOLOGIA.zip` no FTP DATASUS
- **SISCAN — Sistema de Informação do Câncer**: https://www.gov.br/inca/pt-br
