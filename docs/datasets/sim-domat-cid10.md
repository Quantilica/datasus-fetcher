# `sim-domat-cid10` — Declarações de Óbitos Maternos CID-10

Microdados nacionais do SIM/SVSA-MS com os óbitos maternos de 1996 a 2025 (CID-10). Cada linha é um óbito materno.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sim` — SIM: Sistema de Informação de Mortalidade |
| **Código no `datasus-fetcher`** | `sim-domat-cid10` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`) |
| **Particionamento** | `year` |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 1996 a 2025 (conforme `index.json`) |
| **Volume aproximado no FTP** | 30 arquivos (~4,6 MB); 1 UF(s) na partição; última atualização 2026-08-28 |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIM/CID9/DOCS`, `/dissemin/publicos/SIM/CID10/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIM/CID9/TAB`, `/dissemin/publicos/SIM/CID10/TAB` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informação sobre Mortalidade (SIM) foi criado pelo Ministério da Saúde em 1975 e hoje é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), por meio da Coordenação-Geral de Informações e Análises Epidemiológicas (CGIAE), com descentralização para as secretarias municipais e estaduais de saúde. Sua finalidade é prover estatísticas vitais de mortalidade para vigilância epidemiológica, planejamento e avaliação de políticas, com cobertura nacional e identificação do local de residência e de ocorrência. O evento gerador é o óbito, registrado na Declaração de Óbito (DO), documento padronizado em todo o país e de preenchimento obrigatório pelo médico (ou, na ausência, por duas testemunhas em cartório). A DO é organizada em nove blocos (identificação, residência, ocorrência, fetal/menor de 1 ano, condições da mãe, causas do óbito, médico, causas externas, cartório e localidade sem médico) e é alimentada nos municípios, com consolidação estadual e federal.

O recorte materno reúne óbitos de mulheres cujas causas se relacionam à gravidez, parto e puerpério, a partir de 1996. A Razão de Mortalidade Materna (RMM) é indicador-chave do Objetivo de Desenvolvimento Sustentável 3, e sua vigilância é regulada pela Portaria GM/MS nº 1.119/2008, que determina investigação obrigatória dos óbitos de mulheres em idade fértil.

A principal ruptura histórica é a mudança de classificação: a CID-9 vigorou até 1995 e a CID-10 passou a ser usada a partir de 1996, o que torna as séries de causa de morte não diretamente comparáveis sem compatibilização (por exemplo, por agrupamentos de causas). O FTP organiza os arquivos em dois blocos (`SIM/CID9` e `SIM/CID10`), cada um com seu layout, sua pasta de documentação (`DOCS`) e seus arquivos de tabulação (`TAB`). Portarias que regulam a vigilância de óbitos específicos (maternos, Portaria GM/MS nº 1.119/2008; infantis e fetais, Portaria GM/MS nº 72/2010) e o fluxo de coleta de dados do SIM e do SINASC (Portaria SVS/MS nº 116/2009) ampliaram a investigação e melhoraram a captação. Os dados dos anos mais recentes são divulgados primeiro como preliminares e depois consolidados.

Cobertura no FTP: 1996 a 2025, em um único arquivo nacional por ano. Indicadores: razão de mortalidade materna (por 100 mil nascidos vivos, com denominador do SINASC), proporção de óbitos maternos investigados, causas diretas e indiretas, e perfil por raça/cor e idade.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIM/CID10/DOFET` | `DOMAT` | `year2_pattern` — ano com 2 dígitos (arquivo nacional, sem UF) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `DOMAT23.dbc` — `DOMAT` (óbitos maternos) + `23` (ano com 2 dígitos, 2023); arquivo nacional, sem sufixo de UF.
- **No armazenamento local do `datasus-fetcher`**: `data/sim-domat-cid10/<AAAA>/sim-domat-cid10_<AAAA>@<AAAAMMDD>.dbc` (ex.: `data/sim-domat-cid10/2023/sim-domat-cid10_2023@20260828.dbc`); como não há UF na partição, o nome contém apenas o ano.
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

Layout CID-10 do recorte materno; confirme `OBITOGRAV`, `OBITOPUERP` e `TPMORTEOCO` por ano em `Estrutura_do_SIM_2025.pdf`.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DTOBITO` | String `DDMMAAAA` | Data do óbito. |
| `IDADE` | Inteiro (código composto) | Idade da falecida (unidade + valor). |
| `SEXO` | Inteiro | Sexo (feminino na prática). |
| `RACACOR` | String | Raça/cor. |
| `ESTCIV` | Inteiro | Estado civil. |
| `ESC` | String | Escolaridade. |
| `OCUP` | String (CBO, 6) | Ocupação habitual. |
| `CODMUNRES` | String (IBGE, 6) | Município de residência. |
| `CODMUNOCOR` | String (IBGE, 6) | Município de ocorrência. |
| `LOCOCOR` | String | Local de ocorrência. |
| `CAUSABAS` | String (CID-10) | Causa básica (capítulo XV, O00–O99, e demais causas maternas/ tardias conforme definição). |
| `OBITOGRAV` | String | Óbito durante a gravidez (`1` sim, `2` não, `9` ignorado). |
| `OBITOPUERP` | String | Óbito no puerpério: até 42 dias, de 43 dias a 1 ano, ou não. |
| `TPMORTEOCO` | String | Momento do óbito em relação ao ciclo gravídico-puerperal. |
| `ASSISTMED / NECROPSIA` | String | Assistência médica e necropsia. |
| `TPPOS / DTINVESTIG` | String | Óbito investigado e data da investigação. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CODMUNRES`, `CODMUNOCOR` e `CODMUNNASC` devem ser tratados como `String`; a base usa o código IBGE de 6 dígitos (sem dígito verificador) — mantenha o texto original e use `zfill(6)` apenas se algum arquivo trouxer o código truncado. `CAUSABAS`, `LINHAA`–`LINHAD` e `LINHAII` (CID-10 ou CID-9 conforme o período) e `OCUP`/`CODOCUPMAE` (CBO) são códigos e nunca devem ser convertidos para número. No `wrangle_datasus`, `CODMUNRES` não consta em `CODE_COLUMNS`, mas permanece `String` porque campos caractere do DBF são lidos como texto; `CAUSABAS` e `CAUSABAS_O` constam em `CODE_COLUMNS` e são preservados como `String` limpa.
- **Datas e competências**: nos DBF do SIM e do SINASC as datas (`DTOBITO`, `DTNASC`, `DTCADASTRO`, `DTRECEBIM`, `DTINVESTIG`) vêm como texto `DDMMAAAA`, e `HORAOBITO`/`HORANASC` como `HHMM`. Os nomes sem sublinhado **não** estão em `DATE_COLUMNS` (que cobre `DT_OBITO`, `DT_NASC` etc.), portanto permanecem `String`; converta explicitamente com `pl.col("dtobito").str.to_date("%d%m%Y", strict=False)`.
- **Valores ausentes e sentinelas**: o `wrangle_datasus` faz `strip` das strings e converte em nulo os sentinelas `""`, `" "`, `"999999"`, `"99999999"` e `"00000000"` (data zerada). Códigos categóricos de "ignorado" (`9`, `99`, `999`) **não** viram nulo automaticamente e precisam ser tratados conforme o dicionário de cada variável. Colunas listadas em `INTEGER_COLUMNS` (`IDADE`, `SEXO`, `ESTCIV`, `GRAVIDEZ`, `GESTACAO`, `PARTO`, `CONSULTAS`, `QTDFILVIVO`, `QTDFILMORT`, `ANO`, `MES`) são convertidas para `Int64` com `strict=False`: valores não numéricos (como `M`/`F`/`I` em layouts antigos) viram nulo. Registros com marcador de exclusão dBASE (`_deleted`) são removidos e a coluna é descartada.
Arquivo nacional por ano (sem UF): para análises por estado use `CODMUNRES`/`CODMUNOCOR` (os dois primeiros dígitos do código IBGE identificam a UF). Volume muito pequeno (~4,6 MB para 30 anos): ideal para carga completa. A RMM exige o denominador de nascidos vivos por residência (`sinasc-dn`), e a definição de óbito materno (diretas, indiretas, tardias) deve ser aplicada explicitamente sobre `CAUSABAS`, `OBITOGRAV` e `OBITOPUERP`. Há subinformação de óbitos maternos, parcialmente corrigida por investigação de óbitos de mulheres em idade fértil.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sim-domat-cid10
quantilica datasus list sim-domat-cid10

# 2. Baixar microdados de sim-domat-cid10 com recorte adequado à partição (year)
quantilica datasus sync sim-domat-cid10 -o ./data --start 2015 --end 2023

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sim-domat-cid10 -o ./data --start 2015 --end 2023 --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sim-domat-cid10 -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2023
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

frame = df.read_dbc("data/sim-domat-cid10/2023/sim-domat-cid10_2023@20260828.dbc", dataset="sim-domat-cid10")
print(frame.shape)

frame = frame.with_columns(
    pl.col("dtobito").str.to_date("%d%m%Y", strict=False).alias("data_obito"),
)
print(frame.group_by("causabas").len().sort("len", descending=True).head(10))
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
