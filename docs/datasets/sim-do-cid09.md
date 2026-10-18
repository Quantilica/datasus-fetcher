# `sim-do-cid09` — Declarações de Óbito CID-9

Microdados do Sistema de Informação sobre Mortalidade (SIM/SVSA-MS) com os óbitos ocorridos de 1979 a 1995, codificados pela CID-9, organizados por UF de residência. Cada linha representa uma Declaração de Óbito (um óbito) com características do falecido, local de residência/ocorrência e causa básica.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sim` — SIM: Sistema de Informação de Mortalidade |
| **Código no `datasus-fetcher`** | `sim-do-cid09` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`) |
| **Particionamento** | `uf / year` |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 1979 a 1995 (conforme `index.json`) |
| **Volume aproximado no FTP** | 466 arquivos (~757,3 MB); 28 UF(s) na partição; última atualização 2025-01-24 |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SIM/CID9/DOCS`, `/dissemin/publicos/SIM/CID10/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SIM/CID9/TAB`, `/dissemin/publicos/SIM/CID10/TAB` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informação sobre Mortalidade (SIM) foi criado pelo Ministério da Saúde em 1975 e hoje é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), por meio da Coordenação-Geral de Informações e Análises Epidemiológicas (CGIAE), com descentralização para as secretarias municipais e estaduais de saúde. Sua finalidade é prover estatísticas vitais de mortalidade para vigilância epidemiológica, planejamento e avaliação de políticas, com cobertura nacional e identificação do local de residência e de ocorrência. O evento gerador é o óbito, registrado na Declaração de Óbito (DO), documento padronizado em todo o país e de preenchimento obrigatório pelo médico (ou, na ausência, por duas testemunhas em cartório). A DO é organizada em nove blocos (identificação, residência, ocorrência, fetal/menor de 1 ano, condições da mãe, causas do óbito, médico, causas externas, cartório e localidade sem médico) e é alimentada nos municípios, com consolidação estadual e federal.

Este dataset reúne a série histórica pré-1996 (arquivos `DORES`, "óbitos por residência") em que a causa é registrada em CID-9. A unidade de análise é o óbito, e a UF do arquivo refere-se à residência do falecido, não à ocorrência; óbitos de residentes no exterior não entram neste recorte. O layout dessa época é mais enxuto que o atual e a codificação de campos como idade e sexo difere do padrão pós-1996.

A principal ruptura histórica é a mudança de classificação: a CID-9 vigorou até 1995 e a CID-10 passou a ser usada a partir de 1996, o que torna as séries de causa de morte não diretamente comparáveis sem compatibilização (por exemplo, por agrupamentos de causas). O FTP organiza os arquivos em dois blocos (`SIM/CID9` e `SIM/CID10`), cada um com seu layout, sua pasta de documentação (`DOCS`) e seus arquivos de tabulação (`TAB`). Portarias que regulam a vigilância de óbitos específicos (maternos, Portaria GM/MS nº 1.119/2008; infantis e fetais, Portaria GM/MS nº 72/2010) e o fluxo de coleta de dados do SIM e do SINASC (Portaria SVS/MS nº 116/2009) ampliaram a investigação e melhoraram a captação. Os dados dos anos mais recentes são divulgados primeiro como preliminares e depois consolidados.

Usos típicos: reconstrução de séries longas de mortalidade geral e por causa (taxas brutas e padronizadas por idade), esperança de vida e mortalidade infantil históricas. Para análises que atravessam 1996 é preciso aplicar tabelas de compatibilização CID-9/CID-10, incluindo as tabelas de `Docs-Tabs-CID9.zip` e o pacote `OBITOS_CID9_TAB.zip`.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIM/CID9/DORES` | `DOR` | `uf_year2_pattern` — UF (2 letras) + ano com 2 dígitos | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `DORSP95.dbc` — `DOR` (prefixo de óbitos por residência CID-9) + `SP` (UF) + `95` (ano com 2 dígitos, 1995).
- **No armazenamento local do `datasus-fetcher`**: `data/sim-do-cid09/<AAAA>/sim-do-cid09_<AAAA>-<uf>@<AAAAMMDD>.dbc` (ex.: `data/sim-do-cid09/1995/sim-do-cid09_1995-sp@20250124.dbc`); a data após `@` é a data de modificação do arquivo no FTP. Um `.manifest.json` acompanha cada arquivo.
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
| `DTOBITO` | String `DDMMAAAA` | Data do óbito. |
| `IDADE` | Inteiro / String (layout antigo) | Idade do falecido; a codificação difere da CID-10 e deve ser conferida em `Estrutura_SIM_Anterior.pdf`/`Docs-Tabs-CID9.zip`. |
| `SEXO` | String / Inteiro | Sexo. Em layouts antigos pode vir como texto (`M`, `F`, `I`), caso em que a conversão para `Int64` produz nulo. |
| `CODMUNRES` | String | Município de residência (código IBGE de 6 dígitos). |
| `CAUSABAS` | String (CID-9) | Causa básica do óbito segundo a CID-9, no estilo numérico de 3–4 dígitos. |
| `CODMUNOCOR` | String | Município de ocorrência. |
| `LOCOCOR` | String | Local de ocorrência do óbito. |
| `ESTCIV / OCUP` | String | Estado civil e ocupação, quando presentes no layout do ano. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CODMUNRES`, `CODMUNOCOR` e `CODMUNNASC` devem ser tratados como `String`; a base usa o código IBGE de 6 dígitos (sem dígito verificador) — mantenha o texto original e use `zfill(6)` apenas se algum arquivo trouxer o código truncado. `CAUSABAS`, `LINHAA`–`LINHAD` e `LINHAII` (CID-10 ou CID-9 conforme o período) e `OCUP`/`CODOCUPMAE` (CBO) são códigos e nunca devem ser convertidos para número. No `wrangle_datasus`, `CODMUNRES` não consta em `CODE_COLUMNS`, mas permanece `String` porque campos caractere do DBF são lidos como texto; `CAUSABAS` e `CAUSABAS_O` constam em `CODE_COLUMNS` e são preservados como `String` limpa.
- **Datas e competências**: nos DBF do SIM e do SINASC as datas (`DTOBITO`, `DTNASC`, `DTCADASTRO`, `DTRECEBIM`, `DTINVESTIG`) vêm como texto `DDMMAAAA`, e `HORAOBITO`/`HORANASC` como `HHMM`. Os nomes sem sublinhado **não** estão em `DATE_COLUMNS` (que cobre `DT_OBITO`, `DT_NASC` etc.), portanto permanecem `String`; converta explicitamente com `pl.col("dtobito").str.to_date("%d%m%Y", strict=False)`.
- **Valores ausentes e sentinelas**: o `wrangle_datasus` faz `strip` das strings e converte em nulo os sentinelas `""`, `" "`, `"999999"`, `"99999999"` e `"00000000"` (data zerada). Códigos categóricos de "ignorado" (`9`, `99`, `999`) **não** viram nulo automaticamente e precisam ser tratados conforme o dicionário de cada variável. Colunas listadas em `INTEGER_COLUMNS` (`IDADE`, `SEXO`, `ESTCIV`, `GRAVIDEZ`, `GESTACAO`, `PARTO`, `CONSULTAS`, `QTDFILVIVO`, `QTDFILMORT`, `ANO`, `MES`) são convertidas para `Int64` com `strict=False`: valores não numéricos (como `M`/`F`/`I` em layouts antigos) viram nulo. Registros com marcador de exclusão dBASE (`_deleted`) são removidos e a coluna é descartada.
Layout CID-9: confirme o nome e o domínio de cada coluna em `Docs-Tabs-CID9.zip` antes de analisar, pois `SEXO` e `IDADE` podem usar codificação diferente da CID-10 e a conversão `Int64` do `wrangle_datasus` transformaria valores textuais em nulo. A causa em CID-9 não deve ser misturada com CID-10 na mesma coluna sem rótulo de versão; mantenha o dataset de origem como metadado. O ano de 2 dígitos no nome do arquivo (`95`) é expandido para 1995 pelo fetcher.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sim-do-cid09
quantilica datasus list sim-do-cid09

# 2. Baixar microdados de sim-do-cid09 com recorte adequado à partição (uf / year)
quantilica datasus sync sim-do-cid09 -o ./data --start 2015 --end 2023 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sim-do-cid09 -o ./data --start 2015 --end 2023 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sim-do-cid09 -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2023 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

# Leitura de um arquivo baixado (descompacta o .dbc em Rust e aplica o wrangle_datasus)
frame = df.read_dbc("data/sim-do-cid09/1995/sim-do-cid09_1995-sp@20250124.dbc", dataset="sim-do-cid09")
print(frame.shape, frame.columns[:12])

# Datas do SIM ficam como texto DDMMAAAA: converter explicitamente
frame = frame.with_columns(
    pl.col("dtobito").str.to_date("%d%m%Y", strict=False).alias("data_obito"),
)
print(frame.group_by('causabas').len().sort('len', descending=True).head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIM/CID9/DORES`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde / SVSA — Sistema de Informação sobre Mortalidade (SIM)**: https://www.gov.br/saude/pt-br/composicao/svsa/sistemas-de-informacao/sim
- **Documentação no FTP (`DOCS`)**: `Estrutura_do_SIM_2025.pdf`, `Estrutura_SIM_para_CD.pdf`, `Docs_Tabs_CID10.zip` (CID-10) e `Docs-Tabs-CID9.zip` (CID-9).
- **Manual de Instruções para o Preenchimento da Declaração de Óbito** (Ministério da Saúde/SVS) e legislação em `Legislacao_PDF.pdf` e `Portaria.pdf` (FTP).
- **PCDaS / Fiocruz** — plataforma de dados com séries do SIM: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde / Wiki SIM** (documentação comunitária do SIM e do DATASUS): https://wiki.saude.gov.br/
