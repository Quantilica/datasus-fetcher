# `sim-do-cid10` — Declarações de Óbito CID-10

Microdados do Sistema de Informação sobre Mortalidade (SIM/SVSA-MS) com todos os óbitos (fetais e não fetais) ocorridos a partir de 1996, codificados na CID-10 e agrupados por UF de residência. Cada linha representa uma Declaração de Óbito.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sim` — SIM: Sistema de Informação de Mortalidade |
| **Código no `datasus-fetcher`** | `sim-do-cid10` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`) |
| **Particionamento** | `uf / year` |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 1996 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 868 arquivos (~5,2 GB); 28 UF(s) na partição; última atualização 2026-09-28 |
| **Arquivos preliminares** | Sim (diretório PRELIM) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIM/CID9/DOCS`, `/dissemin/publicos/SIM/CID10/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIM/CID9/TAB`, `/dissemin/publicos/SIM/CID10/TAB` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informação sobre Mortalidade (SIM) foi criado pelo Ministério da Saúde em 1975 e hoje é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), por meio da Coordenação-Geral de Informações e Análises Epidemiológicas (CGIAE), com descentralização para as secretarias municipais e estaduais de saúde. Sua finalidade é prover estatísticas vitais de mortalidade para vigilância epidemiológica, planejamento e avaliação de políticas, com cobertura nacional e identificação do local de residência e de ocorrência. O evento gerador é o óbito, registrado na Declaração de Óbito (DO), documento padronizado em todo o país e de preenchimento obrigatório pelo médico (ou, na ausência, por duas testemunhas em cartório). A DO é organizada em nove blocos (identificação, residência, ocorrência, fetal/menor de 1 ano, condições da mãe, causas do óbito, médico, causas externas, cartório e localidade sem médico) e é alimentada nos municípios, com consolidação estadual e federal.

É o dataset principal do SIM: base de referência nacional para mortalidade geral, por causa, idade, sexo, raça/cor, escolaridade e território. A unidade de análise é o óbito; o arquivo `DO<UF><AAAA>` reúne os óbitos de residentes naquela UF. Os arquivos com óbitos fetais (`TIPOBITO = 1`) estão incluídos no mesmo layout, e cortes específicos (fetal, infantil, materno, causas externas) são também publicados em datasets separados `sim-dofet-*`, `sim-doinf-*`, `sim-domat-*` e `sim-doext-*`.

A principal ruptura histórica é a mudança de classificação: a CID-9 vigorou até 1995 e a CID-10 passou a ser usada a partir de 1996, o que torna as séries de causa de morte não diretamente comparáveis sem compatibilização (por exemplo, por agrupamentos de causas). O FTP organiza os arquivos em dois blocos (`SIM/CID9` e `SIM/CID10`), cada um com seu layout, sua pasta de documentação (`DOCS`) e seus arquivos de tabulação (`TAB`). Portarias que regulam a vigilância de óbitos específicos (maternos, Portaria GM/MS nº 1.119/2008; infantis e fetais, Portaria GM/MS nº 72/2010) e o fluxo de coleta de dados do SIM e do SINASC (Portaria SVS/MS nº 116/2009) ampliaram a investigação e melhoraram a captação. Os dados dos anos mais recentes são divulgados primeiro como preliminares e depois consolidados.

Indicadores: taxa de mortalidade geral e específica por causa, proporção de óbitos por causas mal definidas (capítulo XVIII), mortalidade prematura (30–69 anos) por doenças crônicas não transmissíveis, mortalidade por causas externas, razão de mortalidade materna (em conjunto com SINASC), mortalidade infantil, e qualidade da informação (percentual de campos ignorados).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIM/CID10/DORES` | `DO` | `uf_year_pattern` — UF (2 letras) + ano com 4 dígitos | `dbc` | Não |
| `/dissemin/publicos/SIM/PRELIM/DORES` | `DO` | `uf_year_pattern` — UF (2 letras) + ano com 4 dígitos (dados preliminares) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `DOSP2023.dbc` — `DO` (declaração de óbito) + `SP` (UF de residência) + `2023` (ano do óbito). Os preliminares ficam em `SIM/PRELIM/DORES` com o mesmo padrão.
- **No armazenamento local do `datasus-fetcher`**: `data/sim-do-cid10/<AAAA>/sim-do-cid10_<AAAA>-<uf>@<AAAAMMDD>.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset (`sim-do-cid10-preliminar_<AAAA>-<uf>@<AAAAMMDD>.dbc`).
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

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TIPOBITO` | String (1 dígito) | Tipo de óbito: `1` fetal, `2` não fetal. |
| `DTOBITO` | String `DDMMAAAA` | Data do óbito. |
| `HORAOBITO` | String `HHMM` | Hora do óbito. |
| `DTNASC` | String `DDMMAAAA` | Data de nascimento do falecido. |
| `IDADE` | Inteiro (código composto) | Idade codificada em 3 dígitos: 1º dígito é a unidade (`0` minutos, `1` horas, `2` dias, `3` meses, `4` anos, `5` anos acima de 99) e os demais, o valor. Ex.: `4025` = 25 anos. |
| `SEXO` | Inteiro | Sexo: `1` masculino, `2` feminino, `0`/`9` ignorado. |
| `RACACOR` | String | Raça/cor: `1` branca, `2` preta, `3` amarela, `4` parda, `5` indígena. |
| `ESTCIV` | Inteiro | Estado civil (`1` solteiro … `5` união estável, `9` ignorado). |
| `ESC` | String | Escolaridade em anos de estudo (faixas), conforme o dicionário. |
| `OCUP` | String (CBO, 6 dígitos) | Ocupação habitual do falecido (CBO-2002). |
| `CODMUNRES` | String (IBGE, 6 dígitos) | Município de residência do falecido. |
| `LOCOCOR` | String | Local de ocorrência: hospital, outros estabelecimentos de saúde, domicílio, via pública, outros. |
| `CODMUNOCOR` | String (IBGE, 6 dígitos) | Município de ocorrência do óbito. |
| `CAUSABAS` | String (CID-10) | Causa básica do óbito (selecionada/codificada segundo as regras da CID-10). |
| `LINHAA` | String (CID-10) | Causas da Parte I do atestado (linhas A–D: `LINHAA`, `LINHAB`, `LINHAC`, `LINHAD`) e Parte II (`LINHAII`). |
| `CIRCOBITO` | String | Circunstância do óbito externo: acidente, suicídio, homicídio, outros. |
| `ASSISTMED / NECROPSIA` | String | Indicam se houve assistência médica e se foi realizada necropsia. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CODMUNRES`, `CODMUNOCOR` e `CODMUNNASC` devem ser tratados como `String`; a base usa o código IBGE de 6 dígitos (sem dígito verificador) — mantenha o texto original e use `zfill(6)` apenas se algum arquivo trouxer o código truncado. `CAUSABAS`, `LINHAA`–`LINHAD` e `LINHAII` (CID-10 ou CID-9 conforme o período) e `OCUP`/`CODOCUPMAE` (CBO) são códigos e nunca devem ser convertidos para número. No `wrangle_datasus`, `CODMUNRES` não consta em `CODE_COLUMNS`, mas permanece `String` porque campos caractere do DBF são lidos como texto; `CAUSABAS` e `CAUSABAS_O` constam em `CODE_COLUMNS` e são preservados como `String` limpa.
- **Datas e competências**: nos DBF do SIM e do SINASC as datas (`DTOBITO`, `DTNASC`, `DTCADASTRO`, `DTRECEBIM`, `DTINVESTIG`) vêm como texto `DDMMAAAA`, e `HORAOBITO`/`HORANASC` como `HHMM`. Os nomes sem sublinhado **não** estão em `DATE_COLUMNS` (que cobre `DT_OBITO`, `DT_NASC` etc.), portanto permanecem `String`; converta explicitamente com `pl.col("dtobito").str.to_date("%d%m%Y", strict=False)`.
- **Valores ausentes e sentinelas**: o `wrangle_datasus` faz `strip` das strings e converte em nulo os sentinelas `""`, `" "`, `"999999"`, `"99999999"` e `"00000000"` (data zerada). Códigos categóricos de "ignorado" (`9`, `99`, `999`) **não** viram nulo automaticamente e precisam ser tratados conforme o dicionário de cada variável. Colunas listadas em `INTEGER_COLUMNS` (`IDADE`, `SEXO`, `ESTCIV`, `GRAVIDEZ`, `GESTACAO`, `PARTO`, `CONSULTAS`, `QTDFILVIVO`, `QTDFILMORT`, `ANO`, `MES`) são convertidas para `Int64` com `strict=False`: valores não numéricos (como `M`/`F`/`I` em layouts antigos) viram nulo. Registros com marcador de exclusão dBASE (`_deleted`) são removidos e a coluna é descartada.
Arquivos `DO<UF>` agrupam por UF de **residência**; para análise por local de ocorrência use `CODMUNOCOR`. Os arquivos preliminares (diretório `PRELIM`) são sujeitos a revisão e podem ser substituídos pela versão final: ao consolidar, prefira a versão `FINAL` do mesmo ano/UF e mantenha o carimbo de data do arquivo. `IDADE` em `Int64` é um código composto (unidade + valor), não a idade em anos: decodifique antes de agrupar. Óbitos fetais compartilham o arquivo (`TIPOBITO = 1`) e devem ser excluídos de taxas de mortalidade geral.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sim-do-cid10
quantilica datasus list sim-do-cid10

# 2. Baixar microdados de sim-do-cid10 com recorte adequado à partição (uf / year)
quantilica datasus sync sim-do-cid10 -o ./data --start 2015 --end 2023 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sim-do-cid10 -o ./data --start 2015 --end 2023 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sim-do-cid10 -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2023 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

# Leitura de um arquivo baixado (descompacta o .dbc em Rust e aplica o wrangle_datasus)
frame = df.read_dbc("data/sim-do-cid10/2023/sim-do-cid10_2023-sp@20250301.dbc", dataset="sim-do-cid10")
print(frame.shape, frame.columns[:12])

# Datas do SIM ficam como texto DDMMAAAA: converter explicitamente
frame = frame.with_columns(
    pl.col("dtobito").str.to_date("%d%m%Y", strict=False).alias("data_obito"),
)
print(
    frame.filter(pl.col("tipobito") == "2")
    .group_by("causabas")
    .len()
    .sort("len", descending=True)
    .head(10)
)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID10/DORES`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde / SVSA — Sistema de Informação sobre Mortalidade (SIM)**: https://www.gov.br/saude/pt-br/composicao/svsa/sistemas-de-informacao/sim
- **Documentação no FTP (`DOCS`)**: `Estrutura_do_SIM_2025.pdf`, `Estrutura_SIM_para_CD.pdf`, `Docs_Tabs_CID10.zip` (CID-10) e `Docs-Tabs-CID9.zip` (CID-9).
- **Manual de Instruções para o Preenchimento da Declaração de Óbito** (Ministério da Saúde/SVS) e legislação em `Legislacao_PDF.pdf` e `Portaria.pdf` (FTP).
- **PCDaS / Fiocruz** — plataforma de dados com séries do SIM: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde / Wiki SIM** (documentação comunitária do SIM e do DATASUS): https://wiki.saude.gov.br/
