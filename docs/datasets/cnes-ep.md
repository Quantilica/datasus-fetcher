# `cnes-ep` — Equipes

O `cnes-ep` contém os microdados do arquivo de **Equipes** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra as equipes de atenção básica e outras equipes vinculadas aos estabelecimentos. Cada registro (linha) representa uma **equipe** (`ID_EQUIPE`) de um estabelecimento, em uma competência mensal, com o tipo de equipe, área de atuação, segmento populacional atendido e datas de ativação/desativação. É a base oficial para monitorar a Estratégia Saúde da Família (ESF) e a cobertura da atenção primária.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cnes` — CNES: Cadastro Nacional de Estabelecimentos de Saúde |
| **Código no `datasus-fetcher`** | `cnes-ep` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`) |
| **Periodicidade** | Mensal (extração por competência) |
| **Cobertura temporal no FTP** | 2007-04 a 2026-09 (conforme `index.json`) |
| **Volume aproximado no FTP** | 6318 arquivos (~583 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`) |

## 1. Contexto Institucional e Epidemiológico

O arquivo `EP` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS e alimentado pelos gestores municipais/estaduais no SCNES. As equipes cadastradas (Equipe de Saúde da Família, Equipe de Atenção Primária, equipes de saúde bucal, NASF/eMulti, equipes ribeirinhas, fluviais, entre outras) são o elemento operacional da Política Nacional de Atenção Básica (PNAB), e seu cadastro no CNES é condição para o repasse de recursos federais de custeio da atenção primária.

O **evento gerador** é a declaração das equipes na FCES/SCNES a cada competência. A **unidade de análise é a equipe de um estabelecimento na competência** (`CNES` + `ID_EQUIPE` + `COMPETEN`), identificada por município + código de área + sequencial. O campo `TIPO_EQP` classifica o tipo de equipe, `AREA_EQP`/`NOMEAREA` identificam a área de atuação, `TIPOSEGM` distingue segmento urbano/rural e as flags `QUILOMBO`, `ASSENTAD`, `POPGERAL`, `ESCOLA`, `INDIGENA` e `PRONASCI` indicam as populações assistidas. `DT_ATIVA` e `DT_DESAT` registram a ativação e a desativação da equipe, e `MOTDESAT`/`TP_DESAT` o motivo e o tipo de desativação.

A série histórica no FTP começa em abril de 2007, período de consolidação do cadastro de equipes após a implantação do CNES. Não há diretório preliminar.

Aplicações analíticas típicas: cobertura populacional estimada da atenção básica, número de equipes de saúde da família e de saúde bucal por município, evolução das equipes ativas ao longo do tempo, identificação de equipes desativadas e motivos, distribuição de equipes por segmento (urbano/rural, quilombola, indígena) e apoio ao cálculo de indicadores de financiamento da atenção primária.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/EP` | `EP` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `EPSP2401.dbc` — `EP` (Equipes), `SP` (UF), `24` (ano), `01` (mês). Há também `EPBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-ep/2024-01/cnes-ep_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Equipes — EP*.dbf") e `TAB_CNES.zip` (domínios de tipo de equipe, área, motivo de desativação).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (7) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `ID_EQUIPE` | String (18) | Código do município + código da área + sequencial da equipe |
| `TIPO_EQP` | String (2) | Tipo de equipe |
| `NOME_EQP` | String (60) | Nome da equipe |
| `AREA_EQP` | String (10) | Código da área da equipe |
| `NOMEAREA` | String (60) | Nome da área |
| `TIPOSEGM` | String (1) | Tipo do segmento: 1 - Urbano, 2 - Rural |
| `DT_ATIVA` / `DT_DESAT` | String (`AAAAMM`) | Competência de ativação / desativação da equipe |
| `QUILOMBO` / `ASSENTAD` | String (1) | Atende população quilombola / assentada: 1 - Sim, 0 - Não |
| `POPGERAL` / `ESCOLA` / `INDIGENA` / `PRONASCI` | String (1) | Populações assistidas: geral / escolares / indígena / PRONASCI |
| `MOTDESAT` | String (2) | Código do motivo de desativação da equipe |
| `TP_DESAT` | String (1) | Tipo de desativação: 1 - Temporário, 2 - Definitivo |
| `NAT_JUR` | String (4) | Natureza jurídica |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CNES` (7), `CODUFMUN` (7), `ID_EQUIPE`, `TIPO_EQP`, `AREA_EQP`, `MOTDESAT` e `NAT_JUR` permanecem `String` com zeros à esquerda; `ID_EQUIPE` é um identificador composto que nunca deve virar inteiro.
- **Datas e competências**: `DT_ATIVA` e `DT_DESAT` são competências `AAAAMM` e permanecem textuais.
- **Valores ausentes e sentinelas**: espaços, `""` e códigos ignorados são convertidos para nulo por `SENTINEL_NULLS`; registros `_deleted` são removidos.
- **Particularidades do dataset**: para medir "equipes ativas" em uma competência é preciso filtrar as equipes vigentes (considerando `DT_ATIVA` ≤ competência e `DT_DESAT` vazio/posterior); uma mesma equipe pode mudar de tipo ou área ao longo do tempo; a cobertura da atenção básica exige combinar o `EP` com estimativas populacionais (IBGE/TAB_POP) e com as regras de ponderação da PNAB; e o mesmo estabelecimento pode ter mais de uma equipe, exigindo deduplicação por `ID_EQUIPE`.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-ep
quantilica datasus list cnes-ep

# 2. Baixar microdados de cnes-ep (uf+yearmonth)
quantilica datasus sync cnes-ep -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-ep -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-ep -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-ep/2024-01/cnes-ep_202401-sp@20261015.dbc", clean=True)

# Equipes ativas por tipo
ativas = (
    qdf.filter(pl.col("dt_desat").is_null())
    .group_by("tipo_eqp")
    .agg(pl.col("id_equipe").n_unique().alias("equipes_ativas"))
    .sort("equipes_ativas", descending=True)
)
print(ativas)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EP`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout EP) e `TAB_CNES.zip`
- **Política Nacional de Atenção Básica (PNAB)** e **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
