# `sim-dofet-cid10` — Declarações de Óbito Fetais CID-10 (SIM)

Microdados nacionais do SIM/SVSA-MS com as Declarações de Óbito fetais de 1996 a 2025 (CID-10). Cada linha é um óbito fetal registrado, com dados do feto, da mãe e da gestação.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sim` — SIM: Sistema de Informação de Mortalidade |
| **Código no `datasus-fetcher`** | `sim-dofet-cid10` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`) |
| **Particionamento** | `year` |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 1996 a 2025 (conforme `index.json`) |
| **Volume aproximado no FTP** | 30 arquivos (~68.7 MB); 1 UF(s) na partição; última atualização 2026-08-28 |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIM/CID9/DOCS`, `/dissemin/publicos/SIM/CID10/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIM/CID9/TAB`, `/dissemin/publicos/SIM/CID10/TAB` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informação sobre Mortalidade (SIM) foi criado pelo Ministério da Saúde em 1975 e hoje é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), por meio da Coordenação-Geral de Informações e Análises Epidemiológicas (CGIAE), com descentralização para as secretarias municipais e estaduais de saúde. Sua finalidade é prover estatísticas vitais de mortalidade para vigilância epidemiológica, planejamento e avaliação de políticas, com cobertura nacional e identificação do local de residência e de ocorrência. O evento gerador é o óbito, registrado na Declaração de Óbito (DO), documento padronizado em todo o país e de preenchimento obrigatório pelo médico (ou, na ausência, por duas testemunhas em cartório). A DO é organizada em nove blocos (identificação, residência, ocorrência, fetal/menor de 1 ano, condições da mãe, causas do óbito, médico, causas externas, cartório e localidade sem médico) e é alimentada nos municípios, com consolidação estadual e federal.

O recorte fetal reúne as Declarações de Óbito com `TIPOBITO = 1`, isto é, mortes ocorridas antes da expulsão ou extração completa do produto da concepção, independentemente da duração da gestação, com 22 semanas ou mais de gestação ou peso a partir de 500 g conforme as definições adotadas pela vigilância. O bloco IV da DO (óbito fetal ou menor de 1 ano) e as informações sobre a mãe (idade, escolaridade, filhos anteriores) e a gestação (semanas, tipo de gravidez e de parto) são o foco desta base.

A principal ruptura histórica é a mudança de classificação: a CID-9 vigorou até 1995 e a CID-10 passou a ser usada a partir de 1996, o que torna as séries de causa de morte não diretamente comparáveis sem compatibilização (por exemplo, por agrupamentos de causas). O FTP organiza os arquivos em dois blocos (`SIM/CID9` e `SIM/CID10`), cada um com seu layout, sua pasta de documentação (`DOCS`) e seus arquivos de tabulação (`TAB`). Portarias que regulam a vigilância de óbitos específicos (maternos, Portaria GM/MS nº 1.119/2008; infantis e fetais, Portaria GM/MS nº 72/2010) e o fluxo de coleta de dados do SIM e do SINASC (Portaria SVS/MS nº 116/2009) ampliaram a investigação e melhoraram a captação. Os dados dos anos mais recentes são divulgados primeiro como preliminares e depois consolidados.

Cobertura no FTP: 1996 a 2025, em um único arquivo nacional por ano. Indicadores: taxa de mortalidade fetal, mortalidade perinatal (em conjunto com óbitos neonatais precoces do SIM e nascidos vivos do SINASC), óbito fetal por peso e por idade gestacional, e análise de evitabilidade.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIM/CID10/DOFET` | `DOFET` | `year2_pattern` — ano com 2 dígitos (arquivo nacional, sem UF) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `DOFET23.dbc` — `DOFET` (óbitos fetais) + `23` (ano com 2 dígitos, 2023); arquivo nacional, sem sufixo de UF.
- **No armazenamento local do `datasus-fetcher`**: `data/sim-dofet-cid10/<AAAA>/sim-dofet-cid10_<AAAA>@<AAAAMMDD>.dbc` (ex.: `data/sim-dofet-cid10/2023/sim-dofet-cid10_2023@20260828.dbc`); como não há UF na partição, o nome contém apenas o ano.
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

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Layout CID-10 nacional publicado em `SIM/CID10/DOFET`; os nomes abaixo seguem o layout da DO. Confirme a presença de cada coluna por ano em `Estrutura_do_SIM_2025.pdf` (colunas novas, como `SEMAGESTAC`, existem só em anos recentes).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TIPOBITO` | String | Tipo de óbito (`1` = fetal). |
| `DTOBITO` | String `DDMMAAAA` | Data do óbito fetal. |
| `SEXO` | Inteiro | Sexo do feto: `1`, `2`, `0`/`9` ignorado. |
| `RACACOR` | String | Raça/cor do feto. |
| `PESO` | String / Inteiro (g) | Peso ao nascer em gramas. |
| `SEMAGESTAC` | String / Inteiro | Semanas de gestação. |
| `GESTACAO` | Inteiro | Faixa de duração da gestação (`1` <22 semanas … `6` 42 ou mais). |
| `GRAVIDEZ` | Inteiro | Tipo de gravidez: única, dupla, tripla ou mais. |
| `PARTO` | Inteiro | Tipo de parto: vaginal ou cesáreo. |
| `OBITOPARTO` | String | Momento do óbito em relação ao parto: antes, durante ou depois. |
| `IDADEMAE` | String / Inteiro | Idade da mãe em anos. |
| `ESCMAE` | String | Escolaridade da mãe. |
| `QTDFILVIVO / QTDFILMORT` | Inteiro | Número de filhos tidos nascidos vivos e perdas fetais anteriores. |
| `CODMUNRES` | String (IBGE, 6) | Município de residência da mãe. |
| `CODMUNOCOR` | String (IBGE, 6) | Município de ocorrência. |
| `CAUSABAS` | String (CID-10) | Causa básica do óbito fetal (CID-10, em geral capítulo XVI). |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CODMUNRES`, `CODMUNOCOR` e `CODMUNNASC` devem ser tratados como `String`; a base usa o código IBGE de 6 dígitos (sem dígito verificador) — mantenha o texto original e use `zfill(6)` apenas se algum arquivo trouxer o código truncado. `CAUSABAS`, `LINHAA`–`LINHAD` e `LINHAII` (CID-10 ou CID-9 conforme o período) e `OCUP`/`CODOCUPMAE` (CBO) são códigos e nunca devem ser convertidos para número. No `wrangle_datasus`, `CODMUNRES` não consta em `CODE_COLUMNS`, mas permanece `String` porque campos caractere do DBF são lidos como texto; `CAUSABAS` e `CAUSABAS_O` constam em `CODE_COLUMNS` e são preservados como `String` limpa.
- **Datas e competências**: nos DBF do SIM e do SINASC as datas (`DTOBITO`, `DTNASC`, `DTCADASTRO`, `DTRECEBIM`, `DTINVESTIG`) vêm como texto `DDMMAAAA`, e `HORAOBITO`/`HORANASC` como `HHMM`. Os nomes sem sublinhado **não** estão em `DATE_COLUMNS` (que cobre `DT_OBITO`, `DT_NASC` etc.), portanto permanecem `String`; converta explicitamente com `pl.col("dtobito").str.to_date("%d%m%Y", strict=False)`.
- **Valores ausentes e sentinelas**: o `wrangle_datasus` faz `strip` das strings e converte em nulo os sentinelas `""`, `" "`, `"999999"`, `"99999999"` e `"00000000"` (data zerada). Códigos categóricos de "ignorado" (`9`, `99`, `999`) **não** viram nulo automaticamente e precisam ser tratados conforme o dicionário de cada variável. Colunas listadas em `INTEGER_COLUMNS` (`IDADE`, `SEXO`, `ESTCIV`, `GRAVIDEZ`, `GESTACAO`, `PARTO`, `CONSULTAS`, `QTDFILVIVO`, `QTDFILMORT`, `ANO`, `MES`) são convertidas para `Int64` com `strict=False`: valores não numéricos (como `M`/`F`/`I` em layouts antigos) viram nulo. Registros com marcador de exclusão dBASE (`_deleted`) são removidos e a coluna é descartada.
Arquivo nacional por ano (sem UF): para análises por estado use `CODMUNRES`/`CODMUNOCOR` (os dois primeiros dígitos do código IBGE identificam a UF). O limite mínimo de gestação (22 semanas/500 g) afeta a comparabilidade com outras fontes e entre períodos. A causa básica de óbitos fetais é muitas vezes uma afecção originada no período perinatal (capítulo XVI da CID-10). Para taxas é necessário somar aos nascidos vivos (`sinasc-dn`) do mesmo ano.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sim-dofet-cid10
quantilica datasus list sim-dofet-cid10

# 2. Baixar microdados de sim-dofet-cid10 com recorte adequado à partição (year)
quantilica datasus sync sim-dofet-cid10 -o ./data --start 2015 --end 2023

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sim-dofet-cid10 -o ./data --start 2015 --end 2023 --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sim-dofet-cid10 -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2023
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

frame = df.read_dbc("data/sim-dofet-cid10/2023/sim-dofet-cid10_2023@20260828.dbc", dataset="sim-dofet-cid10")
print(frame.shape)

frame = frame.with_columns(
    pl.col("dtobito").str.to_date("%d%m%Y", strict=False).alias("data_obito"),
)
# Óbitos fetais por faixa de peso e tipo de parto
print(frame.group_by(["gestacao", "parto"]).len().sort("len", descending=True).head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DOFET`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde / SVSA — Sistema de Informação sobre Mortalidade (SIM)**: https://www.gov.br/saude/pt-br/composicao/svsa/sistemas-de-informacao/sim
- **Documentação no FTP (`DOCS`)**: `Estrutura_do_SIM_2025.pdf`, `Estrutura_SIM_para_CD.pdf`, `Docs_Tabs_CID10.zip` (CID-10) e `Docs-Tabs-CID9.zip` (CID-9).
- **Manual de Instruções para o Preenchimento da Declaração de Óbito** (Ministério da Saúde/SVS) e legislação em `Legislacao_PDF.pdf` e `Portaria.pdf` (FTP).
- **PCDaS / Fiocruz** — plataforma de dados com séries do SIM: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde / Wiki SIM** (documentação comunitária do SIM e do DATASUS): https://wiki.saude.gov.br/
