# `pce` — Programa de Controle da Esquistossomose

O `pce` contém os registros de **atividades de controle da esquistossomose** realizadas pelo Programa de Controle da Esquistossomose (PCE) do Ministério da Saúde. Cada registro (linha) representa a produção de uma **localidade** (distrito, localidade ou área de atuação) em uma **competência** (mês/ano), agregando contagens de exames realizados, positivos, tratamentos, internações, formas clínicas e ações de controle (moluscocidas, atividades educativas etc.). É a base histórica do PCE, que evoluiu posteriormente para o sistema SISPCE.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `pce` — PCE: Programa de Controle da Esquistossomose |
| **Código no `datasus-fetcher`** | `pce` |
| **Formato dos arquivos** | `.dbc` (compactado do DBF) |
| **Particionamento** | `uf`, `year` (um arquivo por UF e ano) |
| **Periodicidade** | Mensal (competências consolidadas por ano) |
| **Cobertura temporal no FTP** | 1995 a 2026 (conforme `index.json`; 20 UFs com dados) |
| **Volume aproximado no FTP** | 460 arquivos (~15,5 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/PCE/DOCS` (`DIC_DADOS_SISPCE_PCE-DG.txt`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/PCE/AUXILIAR` (`tab_pce.zip`) |

## 1. Contexto Institucional e Epidemiológico

A esquistossomose mansônica é uma doença parasitária de veiculação hídrica, endêmica em diversas regiões do Brasil, historicamente nas áreas litorâneas do Nordeste e em partes do Sudeste. O **Programa de Controle da Esquistossomose (PCE)** foi implantado pelo Ministério da Saúde para reduzir a morbidade por meio de busca ativa de casos (exames coproscópicos), tratamento dos positivos, controle do molusco vetor (*Biomphalaria*) e ações de saneamento e educação em saúde.

O **evento gerador** é a **atividade de controle realizada na localidade** — um exame, um tratamento, uma aplicação de moluscocida — que é agregada por localidade e competência no registro do PCE. A **unidade de análise é o registro de produção por distrito/localidade e competência**, com os campos `ID_UF`, `SG_UF`, `ID_DISTR`, `ID_LOC`, `DT_COMP` e uma grande família de contadores `QT_*`: população trabalhada (`QT_POP`), exames realizados (`QT_EXAM`), positivos (`QT_POS`), quantidade por faixa de idade (`QT_1A4`, `QT_5A16`, `QT_17`), tratamentos (`QT_ATRAT`, `QT_TRAT`), formas clínicas (aguda/crônica/compensada/descompensada), internações, recusas, ausências, controle de caracóis (`QT_CI`, `QT_REC`) etc.

O sistema foi, ao longo do tempo, substituído/modernizado pelo **SISPCE**. Os dados no FTP cobrem de 1995 a 2026, com um arquivo `.dbc` por UF e ano (prefixo `PCE` + UF + dois dígitos do ano). Apenas 20 UFs possuem dados, refletindo a distribuição histórica da endemia. Não há diretório preliminar.

Aplicações analíticas típicas: séries históricas de positividade e exames por localidade, avaliação da cobertura do programa, distribuição espacial da esquistossomose, monitoramento de formas clínicas graves e internações, e avaliação de impacto de intervenções de controle.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/PCE/DADOS` | `PCE` | UF + AA (ex.: `PESP00`, `PCEAL15`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `PESP00.dbc` — `PCE` é o prefixo, `SP` a UF e `00` o ano (2000). Há variações de dois dígitos (`PCEP00`, `PCESP15`). O `.dbc` é a versão compactada do DBF (`DBC`/DATASUS).
- **No armazenamento local do `datasus-fetcher`**: `data/pce/2024/pce_2024-sp@20251029.dbc` (partição por UF e ano).
- **Documentação e Tabelas Auxiliares associadas**: em `PCE/DOCS` está `DIC_DADOS_SISPCE_PCE-DG.txt` (dicionário de dados, com a lista completa de `QT_*` e suas descrições); em `PCE/AUXILIAR` está `tab_pce.zip`, com o arquivo `pce.def` (definições) e tabelas de conversão `.cnv` (UF, município, localidade, região), usados pelo TabWin.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

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

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_UF`, `SG_UF`, `ID_DISTR` e `ID_LOC` são códigos/texto e devem permanecer `String`; `DT_COMP` é `AAAAMM`.
- **Datas e competências**: `DT_COMP` (`AAAAMM`) é a competência de produção; a rotina de datas não deve forçá-la a `AAAAMMDD`.
- **Valores ausentes e sentinelas**: contadores vazios representam zero atividade; alguns campos de código podem usar sentinelas/`ignorado`.
- **Particularidades do dataset**: os dados são **agregados** (não é base de pacientes individuais); a cobertura é restrita a 20 UFs (áreas endêmicas); há apenas `DOCS`/`AUXILIAR` em maiúsculas; o `.dbc` precisa ser descompactado (DBF) antes da leitura; a nomenclatura de anos usa 2 dígitos, exigindo o mapa de ano correto; e há sobreposição histórica com o SISPCE, recomendando atenção a mudanças de sistema no período.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para pce
quantilica datasus list pce

# 2. Baixar microdados com recorte de anos e UFs (partition uf+year)
quantilica datasus sync pce -o ./data --start 2000 --end 2024 --regions pe al ba

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync pce -o ./data --docs --aux --start 2000 --end 2024 --regions pe

# 4. Pipeline completo: download, descompactação do .dbc e conversão para Parquet
quantilica datasus pipeline pce -o ./data/raw --parquet-dir ./data/parquet --start 2000 --end 2024 --regions pe
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

pce = read_dbc("data/raw/pce/2024/pce_2024-pe.dbc", clean=True)

# Positividade por competência
resumo = (
    pce.group_by("dt_comp")
    .agg([
        pl.col("qt_exam").sum().alias("exames"),
        pl.col("qt_pos").sum().alias("positivos"),
    ])
    .with_columns((pl.col("positivos") / pl.col("exames")).alias("positividade"))
    .sort("dt_comp")
)
print(resumo)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/PCE/DADOS`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde — Vigilância da Esquistossomose e PCE/SISPCE**: https://www.gov.br/saude/pt-br
- **Dicionário de dados `DIC_DADOS_SISPCE_PCE-DG.txt`** e pacote `tab_pce.zip` no FTP DATASUS
- **Guia de Vigilância em Saúde (MS)** — capítulo de esquistossomose mansoni
