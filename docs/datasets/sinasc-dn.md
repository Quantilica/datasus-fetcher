# `sinasc-dn` — Declarações de nascidos vivos (SINASC)

Microdados do Sistema de Informações sobre Nascidos Vivos (SINASC/SVSA-MS) de 1994 em diante, agrupados por UF de residência da mãe. Cada linha representa uma Declaração de Nascido Vivo (um nascimento).

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinasc` — SINASC: Sistema de Informação de Nascidos Vivos |
| **Código no `datasus-fetcher`** | `sinasc-dn` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`) |
| **Particionamento** | `uf / year` |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 1994 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 922 arquivos (~7.2 GB); 28 UF(s) na partição; última atualização 2026-09-28 |
| **Arquivos preliminares** | Sim (diretório PRELIM) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINASC/ANT/DOCS`, `/dissemin/publicos/SINASC/NOV/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINASC/1994_1995/Auxiliar`, `/dissemin/publicos/SINASC/1996_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações sobre Nascidos Vivos (SINASC) foi implantado pelo Ministério da Saúde em 1990 e é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), com coleta descentralizada pelas secretarias municipais e estaduais de saúde. Sua finalidade é fornecer dados sobre nascimentos para vigilância e planejamento das ações de saúde da mulher e da criança, em especial indicadores de pré-natal, parto, prematuridade, peso ao nascer e anomalias congênitas, além de ser o denominador oficial de indicadores de mortalidade infantil e materna.

O evento gerador é o nascimento vivo, registrado na Declaração de Nascido Vivo (DN), documento padronizado em todo o território, preenchido no estabelecimento de saúde ou, em partos domiciliares, pelo cartório ou parteira tradicional. A unidade de análise é o nascido vivo; cada registro traz dados da criança, da mãe, da gestação e do parto.

A DN substituiu a coleta heterogênea feita a partir do registro civil, e o SINASC consolidou-se como a principal fonte de dados de natalidade do país, com cobertura estimada acima de 95% em nível nacional (variável entre regiões). A coleta é regulada pela Portaria SVS/MS nº 116/2009; a DN passou por revisões de leiaute, com inclusão de variáveis como o grupo de Robson e a anomalia congênita detalhada em CID-10. O FTP separa dois períodos: 1994–1995 (layout anterior, prefixo `DNR`) e 1996 em diante.

Aplicações: taxa bruta de natalidade e fecundidade, proporção de nascimentos prematuros e de baixo peso, proporção de cesáreas e grupos de Robson, adequação do pré-natal (7 ou mais consultas), gravidez na adolescência, nascidos com anomalias congênitas, perfil por raça/cor e escolaridade da mãe, e denominador para mortalidade infantil (`sim-doinf-*`) e materna (`sim-domat-cid10`).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINASC/1994_1995/Dados/DNRES` | `DNR` | `uf_year_pattern` — UF (2 letras) + ano com 4 dígitos | `dbc` | Não |
| `/dissemin/publicos/SINASC/1996_/Dados/DNRES` | `DN` | `uf_year_pattern` — UF (2 letras) + ano com 4 dígitos | `dbc` | Não |
| `/dissemin/publicos/SINASC/PRELIM/DNRES` | `DN` | `uf_year_pattern` — UF (2 letras) + ano com 4 dígitos (dados preliminares) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `DNSP2023.dbc` — `DN` (declaração de nascido vivo) + `SP` (UF de residência da mãe) + `2023` (ano do nascimento). Para 1994–1995 o prefixo é `DNR` (ex.: `DNRSP1994.dbc`). Preliminares ficam em `SINASC/PRELIM/DNRES`.
- **No armazenamento local do `datasus-fetcher`**: `data/sinasc-dn/<AAAA>/sinasc-dn_<AAAA>-<uf>@<AAAAMMDD>.dbc`; os preliminares recebem o sufixo `-preliminar` no nome do dataset (`sinasc-dn-preliminar_<AAAA>-<uf>@<AAAAMMDD>.dbc`).
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação (`datasus-metadata/metadata/documentation/sinasc.json`):
    - `/dissemin/publicos/SINASC/ANT/DOCS/NASC98.HLP` (0.1 MB)
    - `/dissemin/publicos/SINASC/NOV/DOCS/Estrutura_SINASC_para_CD.pdf` (0.0 MB)
    - `/dissemin/publicos/SINASC/NOV/DOCS/Legislacao_PDF.pdf` (0.9 MB)
    - `/dissemin/publicos/SINASC/NOV/DOCS/Portaria.pdf` (0.0 MB)
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/sinasc.json`):
    - `/dissemin/publicos/SINASC/1994_1995/Auxiliar/Arq_Para_Tabulacao_Ate_1995.zip` (0.4 MB)
    - `/dissemin/publicos/SINASC/1996_/Auxiliar/Arq_Para_Tabulacao_A_Partir_1996.zip` (3.2 MB)

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Colunas do layout 1996 em diante; os anos recentes têm colunas adicionais. Confirme em `Estrutura_SINASC_para_CD.pdf` e use `frame.columns` por ano.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DTNASC` | String `DDMMAAAA` | Data de nascimento. |
| `HORANASC` | String `HHMM` | Hora do nascimento. |
| `SEXO` | Inteiro | Sexo do recém-nascido: `1` masculino, `2` feminino, `0`/`9` ignorado. Em arquivos antigos pode vir como `M`/`F`/`I`. |
| `PESO` | String / Inteiro (g) | Peso ao nascer em gramas. |
| `APGAR1 / APGAR5` | String / Inteiro (0–10) | Índice de Apgar no 1º e no 5º minuto. |
| `RACACOR` | String | Raça/cor do recém-nascido. |
| `CODMUNNASC` | String (IBGE, 6) | Município de ocorrência do nascimento. |
| `CODMUNRES` | String (IBGE, 6) | Município de residência da mãe. |
| `LOCNASC` | String | Local de nascimento: hospital, outro estabelecimento, domicílio, outros. |
| `CODESTAB` | String (CNES, 7) | Estabelecimento de saúde onde ocorreu o nascimento. |
| `IDADEMAE` | Inteiro | Idade da mãe em anos. |
| `ESCMAE` | String | Escolaridade da mãe (anos de estudo, em faixas). |
| `ESTCIVMAE` | String | Estado civil da mãe. |
| `QTDFILVIVO / QTDFILMORT` | Inteiro | Filhos nascidos vivos e perdas fetais/abortos anteriores. |
| `GESTACAO / SEMAGESTAC` | Inteiro | Faixa e número de semanas de gestação. |
| `GRAVIDEZ / PARTO` | Inteiro | Tipo de gravidez (única, dupla…) e de parto (vaginal, cesáreo). |
| `CONSULTAS / CONSPRENAT` | Inteiro | Faixa de consultas de pré-natal (`CONSULTAS`) e número informado (`CONSPRENAT`, layouts recentes). |
| `IDANOMAL / CODANOMAL` | String | Presença de anomalia congênita e sua descrição em CID-10 (capítulo XVII). |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CODMUNRES`, `CODMUNOCOR` e `CODMUNNASC` devem ser tratados como `String`; a base usa o código IBGE de 6 dígitos (sem dígito verificador) — mantenha o texto original e use `zfill(6)` apenas se algum arquivo trouxer o código truncado. `CAUSABAS`, `LINHAA`–`LINHAD` e `LINHAII` (CID-10 ou CID-9 conforme o período) e `OCUP`/`CODOCUPMAE` (CBO) são códigos e nunca devem ser convertidos para número. No `wrangle_datasus`, `CODMUNRES` não consta em `CODE_COLUMNS`, mas permanece `String` porque campos caractere do DBF são lidos como texto; `CAUSABAS` e `CAUSABAS_O` constam em `CODE_COLUMNS` e são preservados como `String` limpa.
- **Datas e competências**: nos DBF do SIM e do SINASC as datas (`DTOBITO`, `DTNASC`, `DTCADASTRO`, `DTRECEBIM`, `DTINVESTIG`) vêm como texto `DDMMAAAA`, e `HORAOBITO`/`HORANASC` como `HHMM`. Os nomes sem sublinhado **não** estão em `DATE_COLUMNS` (que cobre `DT_OBITO`, `DT_NASC` etc.), portanto permanecem `String`; converta explicitamente com `pl.col("dtobito").str.to_date("%d%m%Y", strict=False)`.
- **Valores ausentes e sentinelas**: o `wrangle_datasus` faz `strip` das strings e converte em nulo os sentinelas `""`, `" "`, `"999999"`, `"99999999"` e `"00000000"` (data zerada). Códigos categóricos de "ignorado" (`9`, `99`, `999`) **não** viram nulo automaticamente e precisam ser tratados conforme o dicionário de cada variável. Colunas listadas em `INTEGER_COLUMNS` (`IDADE`, `SEXO`, `ESTCIV`, `GRAVIDEZ`, `GESTACAO`, `PARTO`, `CONSULTAS`, `QTDFILVIVO`, `QTDFILMORT`, `ANO`, `MES`) são convertidas para `Int64` com `strict=False`: valores não numéricos (como `M`/`F`/`I` em layouts antigos) viram nulo. Registros com marcador de exclusão dBASE (`_deleted`) são removidos e a coluna é descartada.
Os arquivos agrupam por UF de **residência da mãe** (`CODMUNRES`); use `CODMUNNASC` para análise por local de ocorrência. Os layouts de 1994–1995 (prefixo `DNR`) e de 1996 em diante diferem, e variáveis recentes (`CONSPRENAT`, `MESPRENAT`, `TPROBSON`, `STCESPARTO`, `TPAPRESENT`) não existem nos anos antigos: harmonize colunas antes de empilhar anos. `SEXO` pode vir como `M`/`F`/`I` em anos antigos e vira nulo na conversão `Int64`. Os dados preliminares são sujeitos a revisão; ao consolidar, prefira a versão final do mesmo ano/UF. Códigos "ignorado" (`9`, `99`, `999`) continuam presentes e devem ser tratados na análise (por exemplo, `CONSULTAS = 9`, `PESO = 9999`).

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinasc-dn
quantilica datasus list sinasc-dn

# 2. Baixar microdados de sinasc-dn com recorte adequado à partição (uf / year)
quantilica datasus sync sinasc-dn -o ./data --start 2015 --end 2023 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinasc-dn -o ./data --start 2015 --end 2023 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinasc-dn -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2023 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

frame = df.read_dbc("data/sinasc-dn/2023/sinasc-dn_2023-sp@20250301.dbc", dataset="sinasc-dn")

# DTNASC e outras datas do SINASC vêm como texto DDMMAAAA
frame = frame.with_columns(
    pl.col("dtnasc").str.to_date("%d%m%Y", strict=False).alias("data_nasc"),
)

# Proporção de cesáreas (PARTO: 1 vaginal, 2 cesáreo) por município de residência
cesareas = (
    frame.filter(pl.col("parto").is_in([1, 2]))
    .group_by("codmunres")
    .agg((pl.col("parto") == 2).mean().alias("prop_cesarea"), pl.len().alias("nascidos"))
    .sort("nascidos", descending=True)
)
print(cesareas.head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1994_1995/Dados/DNRES`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde / SVSA — Sistema de Informações sobre Nascidos Vivos (SINASC)**: https://www.gov.br/saude/pt-br/composicao/svsa/sistemas-de-informacao/sinasc
- **Documentação no FTP (`DOCS`)**: `Estrutura_SINASC_para_CD.pdf`, `NASC98.HLP` (layout até 1995), `Legislacao_PDF.pdf` e `Portaria.pdf`.
- **Manual de Instruções para o Preenchimento da Declaração de Nascido Vivo** (Ministério da Saúde/SVS).
- **PCDaS / Fiocruz** — plataforma de dados com séries do SINASC: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde** (DATASUS): https://wiki.saude.gov.br/
