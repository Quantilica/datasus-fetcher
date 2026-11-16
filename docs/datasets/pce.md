---
dataset:
  id: pce
  fonte: datasus
  titulo: Programa de Controle da Esquistossomose
  resumo: 'Programa de Controle da Esquistossomose do DATASUS: a produção de uma localidade em uma competência (contagens de exames e atividades do programa).'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), Programa de Controle da Esquistossomose
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/PCE/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '1995'
    fim: em-curso
  unidade: a produção de uma localidade em uma competência (contagens de exames e atividades do programa)
  granularidade:
    espacial: localidade e município; um arquivo por UF
    temporal: competência (mês) da atividade; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e ano
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 41
  unidades_de_medida:
    qt_pop: quantidade
    qt_pred: quantidade
    qt_exam: quantidade
    qt_nrecol: quantidade
    qt_1a4: quantidade
    qt_5a16: quantidade
    qt_17: quantidade
    qt_pos: quantidade
    qt_atrat: quantidade
    qt_trat: quantidade
    qt_ci: quantidade
    qt_rec: quantidade
    qt_aus: quantidade
    qt_asc: quantidade
    qt_anc: quantidade
    qt_tae: quantidade
    qt_tt: quantidade
    qt_ev: quantidade
    qt_se: quantidade
    qt_hn: quantidade
    qt_out: quantidade
    qt_cap: quantidade
    qt_pesq: quantidade
    qt_bgla: quantidade
    qt_bstr: quantidade
    qt_bten: quantidade
    qt_out1: quantidade
    qt_posbgla: quantidade
    qt_posbten: quantidade
    qt_posbstr: quantidade
    qt_posout: quantidade
    nu_fase: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Programa de Controle da Esquistossomose (`pce`)

## Resumo

O `pce` contém os registros de **atividades de controle da esquistossomose** realizadas pelo Programa de Controle da Esquistossomose (PCE) do Ministério da Saúde. Cada registro (linha) representa a produção de uma **localidade** (distrito, localidade ou área de atuação) em uma **competência** (mês/ano), agregando contagens de exames realizados, positivos, tratamentos, internações, formas clínicas e ações de controle (moluscocidas, atividades educativas etc.). É a base histórica do PCE, que evoluiu posteriormente para o sistema SISPCE.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/PCE/DOCS` (`DIC_DADOS_SISPCE_PCE-DG.txt`)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/PCE/AUXILIAR` (`tab_pce.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/PCE/DADOS` | `PCE` | UF + AA (ex.: `PESP00`, `PCEAL15`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `PESP00.dbc` — `PCE` é o prefixo, `SP` a UF e `00` o ano (2000). Há variações de dois dígitos (`PCEP00`, `PCESP15`). O `.dbc` é a versão compactada do DBF (`DBC`/DATASUS).
- **No armazenamento local do `datasus-fetcher`**: `data/pce/<AAAA>/pce_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/pce/2024/pce_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `PCE/DOCS` está `DIC_DADOS_SISPCE_PCE-DG.txt` (dicionário de dados, com a lista completa de `QT_*` e suas descrições); em `PCE/AUXILIAR` está `tab_pce.zip`, com o arquivo `pce.def` (definições) e tabelas de conversão `.cnv` (UF, município, localidade, região), usados pelo TabWin.

## Conteúdo

A esquistossomose mansônica é uma doença parasitária de veiculação hídrica, endêmica em diversas regiões do Brasil, historicamente nas áreas litorâneas do Nordeste e em partes do Sudeste. O **Programa de Controle da Esquistossomose (PCE)** foi implantado pelo Ministério da Saúde para reduzir a morbidade por meio de busca ativa de casos (exames coproscópicos), tratamento dos positivos, controle do molusco vetor (*Biomphalaria*) e ações de saneamento e educação em saúde.

O **evento gerador** é a **atividade de controle realizada na localidade** — um exame, um tratamento, uma aplicação de moluscocida — que é agregada por localidade e competência no registro do PCE. A **unidade de análise é o registro de produção por distrito/localidade e competência**, com os campos `ID_UF`, `SG_UF`, `ID_DISTR`, `ID_LOC`, `DT_COMP` e uma grande família de contadores `QT_*`: população trabalhada (`QT_POP`), exames realizados (`QT_EXAM`), positivos (`QT_POS`), quantidade por faixa de idade (`QT_1A4`, `QT_5A16`, `QT_17`), tratamentos (`QT_ATRAT`, `QT_TRAT`), formas clínicas (aguda/crônica/compensada/descompensada), internações, recusas, ausências, controle de caracóis (`QT_CI`, `QT_REC`) etc.

O sistema foi, ao longo do tempo, substituído/modernizado pelo **SISPCE**. Os dados no FTP cobrem de 1995 a 2026, com um arquivo `.dbc` por UF e ano (prefixo `PCE` + UF + dois dígitos do ano). Apenas 20 UFs possuem dados, refletindo a distribuição histórica da endemia. Não há diretório preliminar.

Aplicações analíticas típicas: séries históricas de positividade e exames por localidade, avaliação da cobertura do programa, distribuição espacial da esquistossomose, monitoramento de formas clínicas graves e internações, e avaliação de impacto de intervenções de controle.

### Cobertura observada

- Índice do FTP (2026-10): 460 arquivos, de 1995 a 2026, 20 UF(s) com arquivos, última atualização em 2026-07-06.
- Conversão local de amostras (5 arquivo(s) Parquet, de 1995 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `ID_UF` | String (2) | Código da unidade da federação |
| `SG_UF` | String (2) | Sigla da UF |
| `ID_DISTR` | String | Código do distrito sanitário/localidade |
| `ID_LOC` | String | Código da localidade de atuação |
| `DT_COMP` | String (`AAAAMM`) | Competência (mês/ano) da produção |
| `QT_POP` | Inteiro | População trabalhada na localidade |
| `QT_EXAM` | Inteiro | Exames coproscópicos realizados |
| `QT_POS` | Inteiro | Exames positivos |
| `QT_1A4` / `QT_5A16` / `QT_17` | Inteiro | Exames por faixa de idade (1-4, 5-16, 17+) |
| `QT_ATRAT` / `QT_TRAT` | Inteiro | Tratamentos iniciados/concluídos |
| `QT_NRECOL` | Inteiro | Amostras não recolhidas |
| `QT_CI` / `QT_REC` | Inteiro | Controle de caracóis / recusas |
| `QT_AUS` / `QT_ASC` / `QT_ANC` | Inteiro | Ausências e classificações clínicas |
| `QT_TT` / `QT_EV` / `QT_SE` / `QT_HN` / `QT_OUT` / `QT_CAP` / `QT_PESQ` | Inteiro | Outros contadores de atividades/desfechos |

> A lista completa de colunas `QT_*` e suas descrições está no dicionário `DIC_DADOS_SISPCE_PCE-DG.txt` (documentação oficial no FTP).

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `id_uf` | `ID_UF` | texto | Unidade da Federação (UF) onde foi executada a atividade do programa. | Códigos e siglas padronizados pelo IBGE | todos |
| `sg_uf` | `SG_UF` | texto | Unidade da Federação (UF) onde foi executada a atividade do programa. | Códigos e siglas padronizados pelo IBGE | 1995 a 2017 |
| `id_distr` | `ID_DISTR` | texto | Código do Distrito e Regional de Saúde onde foi executada a atividade do programa. | Códigos cadastrados no Sistema de Localização Geográfica (SISLOC). | todos |
| `id_loc` | `ID_LOC` | texto | Localidade (bairro, vila, povoado, fazenda, sítio etc) onde foi executada a atividade do programa. | Códigos cadastrados no Sistema de Localização Geográfica (SISLOC). | todos |
| `dt_comp` | `DT_COMP` | texto | Mês e o ano em que a atividade do programa foi executada. | — | todos |
| `qt_pop` | `QT_POP` | inteiro ou texto | População trabalhada: número de pessoas que receberam o recipiente para coleta do material para exame. | — | todos |
| `qt_pred` | `QT_PRED` | inteiro ou texto | Número de domicílios/prédios visitados | — | todos |
| `qt_exam` | `QT_EXAM` | inteiro ou texto | Número de pessoas examinadas (coproscopia). | — | todos |
| `qt_nrecol` | `QT_NRECOL` | inteiro ou texto | Número de recipientes não recolhidos. | — | todos |
| `qt_1a4` | `QT_1A4` | inteiro ou texto | Número de pessoas cujo exame da lâmina identificou entre 1 a 4 ovos. | — | todos |
| `qt_5a16` | `QT_5A16` | inteiro ou texto | Número de pessoas cujo exame da lâmina identificou entre 5 a 16 ovos. | — | todos |
| `qt_17` | `QT_17` | inteiro ou texto | Número de pessoas cujo exame da lâmina identificou 17 ovos ou mais. | — | todos |
| `qt_pos` | `QT_POS` | inteiro ou texto | Número de pessoas cujos exames foram identificados com ovos de Schistosoma mansoni. | — | todos |
| `qt_atrat` | `QT_ATRAT` | inteiro ou texto | Número de pessoas previstas para serem medicadas contra a esquistossomose. Não significa que todos são positivos. | — | todos |
| `qt_trat` | `QT_TRAT` | inteiro ou texto | Número de pessoas tratadas contra a esquistossomose. | — | todos |
| `qt_ci` | `QT_CI` | inteiro ou texto | Número de pessoas não tratadas por contraindicação:  Doenças cardíacas;  Estado febril;  Epilepsia ou outras doenças neurológicas;  Gravidez;  Amamentação;  Outros motivos. | — | todos |
| `qt_rec` | `QT_REC` | inteiro ou texto | Número de pessoas não tratadas por recusa. | — | todos |
| `qt_aus` | `QT_AUS` | inteiro ou texto | Número de pessoas não tratadas por ausência. | — | todos |
| `qt_asc` | `QT_ASC` | inteiro ou texto | Número de pessoas cujo exame da lâmina identificou ovos de Ascaris lumbricoides. | — | todos |
| `qt_anc` | `QT_ANC` | inteiro ou texto | Número de pessoas cujo exame da lâmina identificou ovos de Ancilostomo duodenale. | — | todos |
| `qt_tae` | `QT_TAE` | inteiro ou texto | Número de pessoas cujo exame da lâmina identificou ovos de Taenia. | — | todos |
| `qt_tt` | `QT_TT` | inteiro ou texto | Número de pessoas cujo exame da lâmina identificou ovos de Trichocephalus trichiura. | — | todos |
| `qt_ev` | `QT_EV` | inteiro ou texto | Número de pessoas cujo exame da lâmina identificou ovos de Enterobius vermicularis. | — | todos |
| `qt_se` | `QT_SE` | inteiro ou texto | Número de pessoas cujo exame da lâmina identificou ovos de Strongyloides stercoralis. | — | todos |
| `qt_hn` | `QT_HN` | inteiro ou texto | Número de pessoas cujo exame da lâmina identificou ovos de Hymenolepis nana. | — | todos |
| `qt_out` | `QT_OUT` | inteiro ou texto | Número de pessoas cujo exame da lâmina identificou ovos de outras verminoses. | — | todos |
| `qt_cap` | `QT_CAP` | inteiro ou texto | Número de caramujos capturados na atividade de malacologia. | — | todos |
| `qt_pesq` | `QT_PESQ` | inteiro ou texto | Número de estações pesquisadas. | — | todos |
| `qt_bgla` | `QT_BGLA` | inteiro ou texto | Quantidade de caramujos capturados da espécie Biomphalaria glabrata. | — | todos |
| `qt_bstr` | `QT_BSTR` | inteiro ou texto | Quantidade de caramujos capturados da espécie Biomphalaria straminea. | — | todos |
| `qt_bten` | `QT_BTEN` | inteiro ou texto | Quantidade de caramujos capturados da espécie Biomphalaria tenagophila. | — | todos |
| `qt_out1` | `QT_OUT1` | inteiro ou texto | Quantidade de caramujos capturados de outras espécies | — | todos |
| `qt_posbgla` | `QT_POSBGLA` | inteiro ou texto | Quantidade de caramujos positivos da espécie Biomphalaria glabrata. | — | todos |
| `qt_posbten` | `QT_POSBTEN` | inteiro ou texto | Quantidade de caramujos positivos da espécie Biomphalaria tenagophila. | — | todos |
| `qt_posbstr` | `QT_POSBSTR` | inteiro ou texto | Quantidade de caramujos positivos da espécie Biomphalaria straminea. | — | todos |
| `qt_posout` | `QT_POSOUT` | inteiro ou texto | Quantidade de caramujos positivos de outras espécies. | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `cs_fase` | `CS_FASE` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026 |
| `nu_fase` | `NU_FASE` | inteiro | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026 |
| `id_drs` | `ID_DRS` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | só em 2026 |

## No lake

- **Dataset no lake:** `datasus/pce`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): inteiro: 32, texto: 40.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `pce.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- os dados são **agregados** (não é base de pacientes individuais); a cobertura é restrita a 20 UFs (áreas endêmicas); há apenas `DOCS`/`AUXILIAR` em maiúsculas; o `.dbc` precisa ser descompactado (DBF) antes da leitura; a nomenclatura de anos usa 2 dígitos, exigindo o mapa de ano correto; e há sobreposição histórica com o SISPCE, recomendando atenção a mudanças de sistema no período. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Tipo que varia entre períodos:** `qt_pop`, `qt_pred`, `qt_exam`, `qt_nrecol`, `qt_1a4`, `qt_5a16`, `qt_17`, `qt_pos`, `qt_atrat`, `qt_trat`, `qt_ci`, `qt_rec`, `qt_aus`, `qt_asc`, `qt_anc`, `qt_tae`, `qt_tt`, `qt_ev`, `qt_se`, `qt_hn`, `qt_out`, `qt_cap`, `qt_pesq`, `qt_bgla`, `qt_bstr` e outras aparecem com mais de um tipo nas amostras (por exemplo, inteiro em alguns períodos e texto em outros); leia a coluna `Tipo` do dicionário e converta explicitamente antes de empilhar períodos. Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Colunas que não existem em todo o período:** 4 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/pce").glob("**/*.parquet"))
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
datasus-fetcher list pce

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync pce -o ./data --start 2020 --end 2024 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset pce
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/PCE/DADOS`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde — Vigilância da Esquistossomose e PCE/SISPCE**: https://www.gov.br/saude/pt-br
- **Dicionário de dados `DIC_DADOS_SISPCE_PCE-DG.txt`** e pacote `tab_pce.zip` no FTP DATASUS
- **Guia de Vigilância em Saúde (MS)** — capítulo de esquistossomose mansoni
