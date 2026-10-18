# `cnes-dc` — Dados Complementares

O `cnes-dc` contém os microdados do arquivo de **Dados Complementares** do Cadastro Nacional de Estabelecimentos de Saúde (CNES). Cada registro (linha) representa um estabelecimento de saúde em uma competência mensal, com os atributos cadastrais complementares ao arquivo de Estabelecimentos (`ST`) — gestão, natureza jurídica e, sobretudo, a infraestrutura especializada declarada (hemoterapia, diálise, radioterapia, quimioterapia e perfusionistas) e os tipos de atendimento/conveniados prestados (`AP*CV*`). É a tabela que detalha a capacidade de alta complexidade e o perfil de atendimento do estabelecimento.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cnes` — CNES: Cadastro Nacional de Estabelecimentos de Saúde |
| **Código no `datasus-fetcher`** | `cnes-dc` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`) |
| **Periodicidade** | Mensal (extração por competência) |
| **Cobertura temporal no FTP** | 2005-08 a 2026-09 (conforme `index.json`) |
| **Volume aproximado no FTP** | 6858 arquivos (~122 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`) |

## 1. Contexto Institucional e Epidemiológico

O arquivo `DC` é parte do mesmo sistema CNES (ver `cnes-st`), gerido pelo Ministério da Saúde via Secretaria Executiva/DATASUS e mantido pelos gestores estaduais e municipais. O CNES foi criado pela Portaria SAS/MS nº 403/2000, teve a FCES aprovada pela Portaria SAS/MS nº 511/2000 e foi reinstituído pela Portaria GM/MS nº 1.646/2015. Enquanto o `ST` traz a identidade, localização e classificação geral do estabelecimento, o `DC` aprofunda os requisitos de habilitação sanitária para procedimentos de alta complexidade e a caracterização dos atendimentos.

O **evento gerador** é o preenchimento/atualização da FCES no SCNES, na qual o estabelecimento declara se possui os requisitos físicos e de recursos humanos exigidos para determinadas políticas (por exemplo, diálise e hemoterapia, com campos como `DIALISE`, `HEMOTERA`, `QUIMRADI` e as quantidades de salas). A **unidade de análise é o estabelecimento na competência** (`CNES` + `COMPETEN`). Os campos `AP01CV*` a `AP07CV*` indicam, para sete grandes grupos de atendimento (internação, ambulatorial, SADT, urgência, outros, vigilância em saúde e regulação), se o estabelecimento atende aos convênios SUS, particular, plano de saúde público, plano de saúde privado, plano-seguro próprio e plano-seguro de terceiros.

Historicamente o arquivo `DC` acumulou colunas de diferentes ciclos do CNES — do cadastro de salas de hemodiálise, hemoterapia e dos requisitos de oncologia (radioterapia/quimioterapia) — e inclui os CNS dos responsáveis técnicos dessas áreas. Não há diretório preliminar; as bases são publicadas consolidadas por competência.

Aplicações analíticas típicas: identificação de serviços habilitados em alta complexidade (diálise, hemoterapia, oncologia), análise da oferta de atendimento por tipo de convênio (SUS vs. saúde suplementar), cálculo de capacidade de salas de procedimentos e apoio à regulação assistencial e à programação de políticas de alta complexidade.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/DC` | `DC` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `DCSP2401.dbc` — `DC` é o prefixo de Dados Complementares, `SP` a UF, `24` o ano e `01` o mês de competência. Existem também arquivos `DCBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-dc/2024-01/cnes-dc_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Dados Complementares — DC*.dbf") e o pacote de domínios `TAB_CNES.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (7) | Código do município do estabelecimento: UF + MUNIC (sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `PF_PJ` | String (1) | Indicador de pessoa: 1 - Física, 3 - Jurídica |
| `NIV_DEP` | String (1) | Grau de dependência: 1 - Individual, 3 - Mantida |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `NAT_JUR` | String (4) | Natureza jurídica |
| `DIALISE` | String (1) | Indica requisito de diálise para o CNES: 1 - Sim, 0 - Não |
| `HEMOTERA` | String (1) | Indica requisito de hemoterapia: 1 - Sim, 0 - Não |
| `QUIMRADI` | String (1) | Indica requisito de quimio/radioterapia: 1 - Sim, 0 - Não |
| `CNS_NEFR` | String (15) | CNS do médico nefrologista responsável |
| `S_HBSAGP` / `S_DPI` | Inteiro | Quantidade de salas HBsAG+ / de diálise peritoneal (DPI) |
| `AP01CV01` .. `AP07CV04` | String (1) | Tipos de atendimento prestado por grupo e convênio (1 - Sim, 0 - Não) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CNES`, `CODUFMUN`, `CNS_NEFR` e os códigos `TP_UNID`/`NAT_JUR`/`PF_PJ`/`NIV_DEP` permanecem texto com zeros à esquerda; os blocos `AP*CV*` são flags `"0"/"1"` de string.
- **Datas e competências**: `COMPETEN` é `AAAAMM` e permanece textual (não é convertido pela rotina de datas); em muitos arquivos históricos não há coluna de data `AAAAMMDD`.
- **Valores ausentes e sentinelas**: campos de quantidade vazios, `""` e códigos `9/99/999` são convertidos para nulo por `SENTINEL_NULLS`; linhas marcadas como `_deleted` são descartadas.
- **Particularidades do dataset**: o leiaute do `DC` mudou bastante ao longo dos anos (blocos de salas de radioterapia, hemoterapia e diálise foram acrescentados em competências distintas), de modo que nem todas as colunas existem em todas as competências — a leitura deve tolerar schema variável; os muitos campos `AP*CV*` exigem dicionário para decodificar grupo de atendimento + convênio; e o `DC` só cobre estabelecimentos que declaram essas características, devendo ser sempre lido em conjunto com o `ST`.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-dc
quantilica datasus list cnes-dc

# 2. Baixar microdados de cnes-dc (uf+yearmonth)
quantilica datasus sync cnes-dc -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-dc -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-dc -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-dc/2024-01/cnes-dc_202401-sp@20261015.dbc", clean=True)

# Estabelecimentos com requisito de diálise
dialise = qdf.filter(pl.col("dialise") == "1").select(["cnes", "codufmun"])
print(dialise.height)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/DC`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout DC) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
