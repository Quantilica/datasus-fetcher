# `cnes-eq` — Equipamentos

O `cnes-eq` contém os microdados do arquivo de **Equipamentos** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra os equipamentos médico-hospitalares e odontológicos existentes nos estabelecimentos. Cada registro (linha) representa um **tipo de equipamento** (`TIPEQUIP` + `CODEQUIP`) de um estabelecimento, em uma competência mensal, com as quantidades existente e em uso e os indicadores de disponibilidade para o SUS. É a principal fonte oficial sobre a capacidade tecnológica instalada da rede de saúde.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cnes` — CNES: Cadastro Nacional de Estabelecimentos de Saúde |
| **Código no `datasus-fetcher`** | `cnes-eq` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`) |
| **Periodicidade** | Mensal (extração por competência) |
| **Cobertura temporal no FTP** | 2005-08 a 2026-09 (conforme `index.json`) |
| **Volume aproximado no FTP** | 6857 arquivos (~1,6 GB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`) |

## 1. Contexto Institucional e Epidemiológico

O arquivo `EQ` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS e alimentado pelos estabelecimentos no SCNES. Os equipamentos cadastrados são pré-requisito para habilitação de serviços e para o faturamento de diversos procedimentos (por exemplo, imagem, diálise, radioterapia e exames laboratoriais) e são usados na regulação e no planejamento da oferta de tecnologia em saúde.

O **evento gerador** é a declaração dos equipamentos na FCES/SCNES a cada competência. A **unidade de análise é o tipo de equipamento de um estabelecimento na competência** (`CNES` + `TIPEQUIP` + `CODEQUIP` + `COMPETEN`). `QT_EXIST` é a quantidade existente, `QT_USO` a efetivamente em uso, e `IND_SUS`/`IND_NSUS` indicam se o equipamento está ou não disponível para o SUS. O tipo (`TIPEQUIP`) agrupa grandes categorias (diagnóstico por imagem, métodos gráficos, infraestrutura, equipamentos para manutenção da vida, etc.) e `CODEQUIP` detalha o item.

A série histórica começa em agosto de 2005 e as categorias de equipamentos evoluíram com a incorporação tecnológica e com revisões das tabelas de domínio. Não há diretório preliminar.

Aplicações analíticas típicas: disponibilidade de tomógrafos, ressonâncias, mamógrafos e outros equipamentos de imagem por região, equipamentos para atenção oncológica e nefrológica, identificação de equipamentos ociosos (`QT_EXIST - QT_USO`), apoio à política de incorporação tecnológica e à regulação de acesso a exames de alta complexidade.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/EQ` | `EQ` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `EQSP2401.dbc` — `EQ` (Equipamentos), `SP` (UF), `24` (ano), `01` (mês). Há também `EQBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-eq/2024-01/cnes-eq_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Equipamentos — EQ*.dbf") e `TAB_CNES.zip` (domínios de tipo/código de equipamento).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `TIPEQUIP` | String (1) | Código do tipo/grupo do equipamento |
| `CODEQUIP` | String (2) | Código do equipamento dentro do tipo |
| `QT_EXIST` | Inteiro | Quantidade existente do equipamento |
| `QT_USO` | Inteiro | Quantidade em uso do equipamento |
| `IND_SUS` | String (1) | Indicador de disponibilidade para o SUS: 1 - Sim, 0 - Não |
| `IND_NSUS` | String (1) | Indicador de equipamento não disponível para o SUS: 1 - Sim, 0 - Não |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `NATUREZA` | String (2) | Código da natureza da organização |
| `TPGESTAO` | String (1) | Tipo de gestão de saúde |
| `PF_PJ` | String (1) | Indicador de pessoa: 1 - Física, 3 - Jurídica |
| `NAT_JUR` | String (4) | Natureza jurídica |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CNES` (7), `CODUFMUN` (6), `TIPEQUIP`, `CODEQUIP`, `TP_UNID` e `NAT_JUR` permanecem `String` com zeros à esquerda; os campos `IND_*` são flags `"0"/"1"`.
- **Datas e competências**: `COMPETEN` é `AAAAMM` e permanece textual.
- **Valores ausentes e sentinelas**: quantidades vazias, `""` e códigos ignorados são convertidos para nulo por `SENTINEL_NULLS`; registros `_deleted` são removidos.
- **Particularidades do dataset**: no leiaute `EQ` as quantidades `QT_EXIST`/`QT_USO` aparecem como texto (`CHAR(3)`), exigindo conversão cuidadosa para inteiro; como no `LT`, a granularidade é tipo–item, exigindo agregação por estabelecimento; `IND_SUS` e `IND_NSUS` podem ser inconsistentes e requerem validação; e as tabelas de domínio de equipamentos são atualizadas periodicamente, de modo que análises históricas longas precisam mapear códigos ao longo do tempo.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-eq
quantilica datasus list cnes-eq

# 2. Baixar microdados de cnes-eq (uf+yearmonth)
quantilica datasus sync cnes-eq -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-eq -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-eq -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-eq/2024-01/cnes-eq_202401-sp@20261015.dbc", clean=True)

# Equipamentos em uso disponíveis para o SUS por grupo
eq = (
    qdf.filter(pl.col("ind_sus") == "1")
    .group_by("tipequip")
    .agg(pl.col("qt_uso").sum().alias("em_uso_sus"))
    .sort("em_uso_sus", descending=True)
)
print(eq)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EQ`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout EQ) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
