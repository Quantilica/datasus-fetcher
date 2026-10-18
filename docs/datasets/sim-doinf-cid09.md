# `sim-doinf-cid09` — Declarações de Óbito Infantis CID-9

Microdados nacionais do SIM/SVSA-MS com as Declarações de Óbito de menores de 1 ano de 1979 a 1995, codificadas pela CID-9. Cada linha é um óbito infantil.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sim` — SIM: Sistema de Informação de Mortalidade |
| **Código no `datasus-fetcher`** | `sim-doinf-cid09` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`) |
| **Particionamento** | `year` |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 1979 a 1995 (conforme `index.json`) |
| **Volume aproximado no FTP** | 17 arquivos (~60,8 MB); 1 UF(s) na partição; última atualização 2020-01-31 |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIM/CID9/DOCS`, `/dissemin/publicos/SIM/CID10/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIM/CID9/TAB`, `/dissemin/publicos/SIM/CID10/TAB` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informação sobre Mortalidade (SIM) foi criado pelo Ministério da Saúde em 1975 e hoje é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), por meio da Coordenação-Geral de Informações e Análises Epidemiológicas (CGIAE), com descentralização para as secretarias municipais e estaduais de saúde. Sua finalidade é prover estatísticas vitais de mortalidade para vigilância epidemiológica, planejamento e avaliação de políticas, com cobertura nacional e identificação do local de residência e de ocorrência. O evento gerador é o óbito, registrado na Declaração de Óbito (DO), documento padronizado em todo o país e de preenchimento obrigatório pelo médico (ou, na ausência, por duas testemunhas em cartório). A DO é organizada em nove blocos (identificação, residência, ocorrência, fetal/menor de 1 ano, condições da mãe, causas do óbito, médico, causas externas, cartório e localidade sem médico) e é alimentada nos municípios, com consolidação estadual e federal.

Série histórica pré-1996 de óbitos de menores de 1 ano, na CID-9. Permite reconstruir a queda da mortalidade infantil brasileira nas décadas de 1980 e 1990, ressalvada a elevada subnotificação de óbitos e nascimentos nas regiões Norte e Nordeste.

A principal ruptura histórica é a mudança de classificação: a CID-9 vigorou até 1995 e a CID-10 passou a ser usada a partir de 1996, o que torna as séries de causa de morte não diretamente comparáveis sem compatibilização (por exemplo, por agrupamentos de causas). O FTP organiza os arquivos em dois blocos (`SIM/CID9` e `SIM/CID10`), cada um com seu layout, sua pasta de documentação (`DOCS`) e seus arquivos de tabulação (`TAB`). Portarias que regulam a vigilância de óbitos específicos (maternos, Portaria GM/MS nº 1.119/2008; infantis e fetais, Portaria GM/MS nº 72/2010) e o fluxo de coleta de dados do SIM e do SINASC (Portaria SVS/MS nº 116/2009) ampliaram a investigação e melhoraram a captação. Os dados dos anos mais recentes são divulgados primeiro como preliminares e depois consolidados.

Cobertura no FTP: 1979 a 1995, em um único arquivo nacional por ano. Uso: séries históricas de mortalidade infantil, combinadas com nascidos vivos do SINASC (a partir de 1994 no FTP) ou estimativas demográficas indiretas para o período anterior.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIM/CID9/DOFET` | `DOINF` | `year2_pattern` — ano com 2 dígitos (arquivo nacional, sem UF) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `DOINF95.dbc` — `DOINF` (óbitos infantis, CID-9) + `95` (ano com 2 dígitos, 1995); arquivo nacional, sem sufixo de UF.
- **No armazenamento local do `datasus-fetcher`**: `data/sim-doinf-cid09/<AAAA>/sim-doinf-cid09_<AAAA>@<AAAAMMDD>.dbc` (ex.: `data/sim-doinf-cid09/1995/sim-doinf-cid09_1995@20260828.dbc`); como não há UF na partição, o nome contém apenas o ano.
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

Layout CID-9: **confirme por ano** a presença de cada coluna em `Docs-Tabs-CID9.zip`.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DTOBITO` | String `DDMMAAAA` | Data do óbito. |
| `DTNASC` | String `DDMMAAAA` | Data de nascimento da criança. |
| `IDADE` | Inteiro (código composto) | Idade ao morrer: valores `0xx`/`1xx` (minutos/horas), `2xx` (dias), `3xx` (meses); sempre menor que 1 ano. |
| `SEXO` | Inteiro | Sexo: `1`, `2`, `0`/`9` ignorado. |
| `RACACOR` | String | Raça/cor da criança. |
| `PESO` | String / Inteiro (g) | Peso ao nascer em gramas. |
| `GESTACAO / SEMAGESTAC` | Inteiro | Duração da gestação (faixa e semanas). |
| `GRAVIDEZ / PARTO` | Inteiro | Tipo de gravidez e de parto. |
| `IDADEMAE` | String / Inteiro | Idade da mãe em anos. |
| `ESCMAE` | String | Escolaridade da mãe. |
| `QTDFILVIVO / QTDFILMORT` | Inteiro | Filhos nascidos vivos e perdas fetais anteriores. |
| `CODMUNRES` | String (IBGE, 6) | Município de residência da mãe/criança. |
| `CODMUNOCOR` | String (IBGE, 6) | Município de ocorrência. |
| `LOCOCOR` | String | Local de ocorrência do óbito. |
| `CAUSABAS` | String (CID) | Causa básica do óbito (CID-10 ou CID-9 conforme o dataset). |
| `ASSISTMED / NECROPSIA` | String | Assistência médica e necropsia. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CODMUNRES`, `CODMUNOCOR` e `CODMUNNASC` devem ser tratados como `String`; a base usa o código IBGE de 6 dígitos (sem dígito verificador) — mantenha o texto original e use `zfill(6)` apenas se algum arquivo trouxer o código truncado. `CAUSABAS`, `LINHAA`–`LINHAD` e `LINHAII` (CID-10 ou CID-9 conforme o período) e `OCUP`/`CODOCUPMAE` (CBO) são códigos e nunca devem ser convertidos para número. No `wrangle_datasus`, `CODMUNRES` não consta em `CODE_COLUMNS`, mas permanece `String` porque campos caractere do DBF são lidos como texto; `CAUSABAS` e `CAUSABAS_O` constam em `CODE_COLUMNS` e são preservados como `String` limpa.
- **Datas e competências**: nos DBF do SIM e do SINASC as datas (`DTOBITO`, `DTNASC`, `DTCADASTRO`, `DTRECEBIM`, `DTINVESTIG`) vêm como texto `DDMMAAAA`, e `HORAOBITO`/`HORANASC` como `HHMM`. Os nomes sem sublinhado **não** estão em `DATE_COLUMNS` (que cobre `DT_OBITO`, `DT_NASC` etc.), portanto permanecem `String`; converta explicitamente com `pl.col("dtobito").str.to_date("%d%m%Y", strict=False)`.
- **Valores ausentes e sentinelas**: o `wrangle_datasus` faz `strip` das strings e converte em nulo os sentinelas `""`, `" "`, `"999999"`, `"99999999"` e `"00000000"` (data zerada). Códigos categóricos de "ignorado" (`9`, `99`, `999`) **não** viram nulo automaticamente e precisam ser tratados conforme o dicionário de cada variável. Colunas listadas em `INTEGER_COLUMNS` (`IDADE`, `SEXO`, `ESTCIV`, `GRAVIDEZ`, `GESTACAO`, `PARTO`, `CONSULTAS`, `QTDFILVIVO`, `QTDFILMORT`, `ANO`, `MES`) são convertidas para `Int64` com `strict=False`: valores não numéricos (como `M`/`F`/`I` em layouts antigos) viram nulo. Registros com marcador de exclusão dBASE (`_deleted`) são removidos e a coluna é descartada.
Arquivo nacional por ano (sem UF): para análises por estado use `CODMUNRES`/`CODMUNOCOR` (os dois primeiros dígitos do código IBGE identificam a UF). No layout CID-9 muitas colunas da tabela acima podem não existir; liste `frame.columns`. Nascidos vivos antes de 1994 não estão disponíveis no FTP (SINASC), então o cálculo de taxas exige estimativas externas, por exemplo do IBGE.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sim-doinf-cid09
quantilica datasus list sim-doinf-cid09

# 2. Baixar microdados de sim-doinf-cid09 com recorte adequado à partição (year)
quantilica datasus sync sim-doinf-cid09 -o ./data --start 2015 --end 2023

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sim-doinf-cid09 -o ./data --start 2015 --end 2023 --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sim-doinf-cid09 -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2023
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

frame = df.read_dbc("data/sim-doinf-cid09/1995/sim-doinf-cid09_1995@20200131.dbc", dataset="sim-doinf-cid09")
print(frame.shape)

frame = frame.with_columns(
    pl.col("dtobito").str.to_date("%d%m%Y", strict=False).alias("data_obito"),
)
print(frame.columns)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID9/DOFET`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde / SVSA — Sistema de Informação sobre Mortalidade (SIM)**: https://www.gov.br/saude/pt-br/composicao/svsa/sistemas-de-informacao/sim
- **Documentação no FTP (`DOCS`)**: `Estrutura_do_SIM_2025.pdf`, `Estrutura_SIM_para_CD.pdf`, `Docs_Tabs_CID10.zip` (CID-10) e `Docs-Tabs-CID9.zip` (CID-9).
- **Manual de Instruções para o Preenchimento da Declaração de Óbito** (Ministério da Saúde/SVS) e legislação em `Legislacao_PDF.pdf` e `Portaria.pdf` (FTP).
- **PCDaS / Fiocruz** — plataforma de dados com séries do SIM: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde / Wiki SIM** (documentação comunitária do SIM e do DATASUS): https://wiki.saude.gov.br/
