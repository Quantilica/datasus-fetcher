# `sinasc-dnex` — Declarações de nascidos vivos no exterior

Microdados do SINASC/SVSA-MS com Declarações de Nascido Vivo de nascimentos ocorridos no exterior, de 2014 a 2024. Cada linha é uma DN registrada para um nascimento fora do Brasil, em um arquivo nacional por ano.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinasc` — SINASC: Sistema de Informação de Nascidos Vivos |
| **Código no `datasus-fetcher`** | `sinasc-dnex` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`) |
| **Particionamento** | `year` |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2014 a 2024 (conforme `index.json`) |
| **Volume aproximado no FTP** | 11 arquivos (~0,6 MB); 1 UF(s) na partição; última atualização 2025-12-23 |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINASC/ANT/DOCS`, `/dissemin/publicos/SINASC/NOV/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINASC/1994_1995/Auxiliar`, `/dissemin/publicos/SINASC/1996_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O Sistema de Informações sobre Nascidos Vivos (SINASC) foi implantado pelo Ministério da Saúde em 1990 e é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), com coleta descentralizada pelas secretarias municipais e estaduais de saúde. Sua finalidade é fornecer dados sobre nascimentos para vigilância e planejamento das ações de saúde da mulher e da criança, em especial indicadores de pré-natal, parto, prematuridade, peso ao nascer e anomalias congênitas, além de ser o denominador oficial de indicadores de mortalidade infantil e materna.

Esta base é um recorte pequeno e específico: nascimentos ocorridos no exterior que, por não terem município de ocorrência no Brasil, ficam fora das tabulações por UF. Ela é publicada à parte para que o total de nascimentos não deixe de contar esses registros. A unidade de análise continua sendo o nascido vivo, com dados da criança e da mãe, mas o campo de local de ocorrência refere-se a outro país.

A DN substituiu a coleta heterogênea feita a partir do registro civil, e o SINASC consolidou-se como a principal fonte de dados de natalidade do país, com cobertura estimada acima de 95% em nível nacional (variável entre regiões). A coleta é regulada pela Portaria SVS/MS nº 116/2009; a DN passou por revisões de leiaute, com inclusão de variáveis como o grupo de Robson e a anomalia congênita detalhada em CID-10. O FTP separa dois períodos: 1994–1995 (layout anterior, prefixo `DNR`) e 1996 em diante.

Uso: reconciliação de totais de nascimentos por ocorrência, estudos de migração e de registros de brasileiros nascidos no exterior. Por ter apenas 11 arquivos (~0,6 MB), é adequado para carga completa e inspeção manual.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINASC/1996_/Dados/DNRES` | `DNEX` | `year_pattern` — ano com 4 dígitos (arquivo nacional, sem UF) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `DNEX2023.dbc` — `DNEX` (declaração de nascido vivo no exterior) + `2023` (ano com 4 dígitos); arquivo nacional, sem UF.
- **No armazenamento local do `datasus-fetcher`**: `data/sinasc-dnex/<AAAA>/sinasc-dnex_<AAAA>@<AAAAMMDD>.dbc` (ex.: `data/sinasc-dnex/2023/sinasc-dnex_2023@20251223.dbc`).
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

Nomes verificados contra o arquivo real `DNEX2024.dbc` (61 colunas, layout próprio do `DNEX`, distinto do `DN`). O país de residência da mãe é `CODPAISRES`; não há coluna de país de ocorrência.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DTNASC` | String `DDMMAAAA` | Data de nascimento. |
| `HORANASC` | String `HHMM` | Hora do nascimento. |
| `SEXO` | String | Sexo do recém-nascido. |
| `PESO` | String (g) | Peso ao nascer em gramas. |
| `APGAR1` / `APGAR5` | String | Apgar no 1º e 5º minuto. |
| `RACACOR` | String | Raça/cor do recém-nascido. |
| `CODMUNNASC` | String (IBGE, 7) | Município de ocorrência do nascimento. |
| `CODESTAB` | String (7) | Estabelecimento de ocorrência. |
| `LOCNASC` | String | Local de ocorrência do nascimento. |
| `CODMUNRES` | String (IBGE, 7) | Município de residência da mãe no Brasil, quando informado. |
| `CODPAISRES` | String (3) | País de residência da mãe. |
| `IDADEMAE` / `DTNASCMAE` | String | Idade e data de nascimento da mãe. |
| `ESCMAE` / `ESCMAE2010` / `SERIESCMAE` | String | Escolaridade da mãe (layouts de escolaridade anterior e de 2010, e série). |
| `ESTCIVMAE` / `RACACORMAE` / `CODOCUPMAE` | String | Estado civil, raça/cor e ocupação (CBO) da mãe. |
| `NATURALMAE` / `CODMUNNATU` / `CODUFNATU` | String | Naturalidade da mãe (país, município e UF). |
| `QTDFILVIVO` / `QTDFILMORT` / `QTDGESTANT` / `QTDPARTNOR` / `QTDPARTCES` | String | Histórico obstétrico: filhos vivos e mortos, gestações e partos normais e cesáreos anteriores. |
| `GESTACAO` / `SEMAGESTAC` / `TPMETESTIM` / `DTULTMENST` | String | Duração da gestação, semanas de gestação, método de estimativa e data da última menstruação. |
| `GRAVIDEZ` / `PARTO` / `TPAPRESENT` / `STTRABPART` / `STCESPARTO` | String | Tipo de gravidez, tipo de parto, apresentação fetal, trabalho de parto induzido e cesárea antes do trabalho de parto. |
| `CONSULTAS` / `CONSPRENAT` / `MESPRENAT` | String | Consultas de pré-natal (faixa e número) e mês de início do pré-natal. |
| `TPROBSON` / `PARIDADE` / `KOTELCHUCK` | String | Classificação de Robson, paridade e índice de Kotelchuck. |
| `IDANOMAL` / `CODANOMAL` | String | Indicador de anomalia congênita e anomalia em CID-10 (capítulo XVII). |
| `IDADEPAI` | String | Idade do pai. |
| `DTCADASTRO` / `DTRECEBIM` / `DTRECORIGA` / `DTDECLARAC` | String `DDMMAAAA` | Datas de cadastro, recebimento, recebimento original e declaração. |
| `NUMEROLOTE` / `VERSAOSIST` / `CONTADOR` / `DIFDATA` | String | Controle do sistema: lote, versão, contador e diferença de datas. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CODMUNRES`, `CODMUNNATU` e `CODMUNNASC` devem ser tratados como `String`; as colunas têm 7 caracteres (IBGE com dígito verificador) — mantenha o texto original e use `zfill(6)` apenas se algum arquivo trouxer o código truncado. `CODANOMAL` (CID-10) e `CODOCUPMAE` (CBO) são códigos e nunca devem ser convertidos para número. No `wrangle_datasus`, `CODMUNRES` não consta em `CODE_COLUMNS`, mas permanece `String` porque campos caractere do DBF são lidos como texto;
- **Datas e competências**: nos DBF do SIM e do SINASC as datas (`DTNASC`, `DTNASCMAE`, `DTCADASTRO`, `DTRECEBIM`, `DTULTMENST`) vêm como texto `DDMMAAAA`, e `HORANASC` como `HHMM`. Os nomes sem sublinhado **não** estão em `DATE_COLUMNS` (que cobre `DT_OBITO`, `DT_NASC` etc.), portanto permanecem `String`; converta explicitamente com `pl.col("dtnasc").str.to_date("%d%m%Y", strict=False)`.
- **Valores ausentes e sentinelas**: o `wrangle_datasus` faz `strip` das strings e converte em nulo os sentinelas `""`, `" "`, `"999999"`, `"99999999"` e `"00000000"` (data zerada). Códigos categóricos de "ignorado" (`9`, `99`, `999`) **não** viram nulo automaticamente e precisam ser tratados conforme o dicionário de cada variável. Colunas listadas em `INTEGER_COLUMNS` (entre as presentes neste arquivo: `GRAVIDEZ`, `GESTACAO`, `PARTO`, `CONSULTAS`, `QTDFILVIVO`, `QTDFILMORT`, `SEXO`) são convertidas para `Int64` com `strict=False`: valores não numéricos (como `M`/`F`/`I` em layouts antigos) viram nulo. Registros com marcador de exclusão dBASE (`_deleted`) são removidos e a coluna é descartada.
Base de baixo volume e cobertura 2014–2024; layout verificado em `DNEX2024.dbc`, que difere do `DN` (por exemplo, não há `ANO`/`MES` nem `OCUP`). Não há UF na partição; a UF pode ser derivada dos dois primeiros dígitos de `CODMUNRES`. Os códigos de município de residência, quando existem, seguem 6 dígitos IBGE. Como os registros são poucos por ano, evite agregações por município.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinasc-dnex
quantilica datasus list sinasc-dnex

# 2. Baixar microdados de sinasc-dnex com recorte adequado à partição (year)
quantilica datasus sync sinasc-dnex -o ./data --start 2015 --end 2023

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinasc-dnex -o ./data --start 2015 --end 2023 --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinasc-dnex -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2023
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

frame = df.read_dbc("data/sinasc-dnex/2023/sinasc-dnex_2023@20251223.dbc", dataset="sinasc-dnex")
print(frame.shape)

frame = frame.with_columns(pl.col("dtnasc").str.to_date("%d%m%Y", strict=False))
print(frame.group_by(pl.col("dtnasc").dt.year()).len().sort("dtnasc"))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINASC/1996_/Dados/DNRES`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde / SVSA — Sistema de Informações sobre Nascidos Vivos (SINASC)**: https://www.gov.br/saude/pt-br/composicao/svsa/sistemas-de-informacao/sinasc
- **Documentação no FTP (`DOCS`)**: `Estrutura_SINASC_para_CD.pdf`, `NASC98.HLP` (layout até 1995), `Legislacao_PDF.pdf` e `Portaria.pdf`.
- **Manual de Instruções para o Preenchimento da Declaração de Nascido Vivo** (Ministério da Saúde/SVS).
- **PCDaS / Fiocruz** — plataforma de dados com séries do SINASC: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde** (DATASUS): https://wiki.saude.gov.br/
