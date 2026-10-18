# `cnes-pf` — Profissional

O `cnes-pf` contém os microdados do arquivo de **Profissionais** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra os vínculos dos profissionais de saúde com os estabelecimentos cadastrados. Cada registro (linha) representa um **vínculo profissional–estabelecimento–ocupação (CBO)** em uma competência mensal, descrevendo a ocupação exercida, o vínculo empregatício com o SUS, a carga horária e o conselho de classe. É a maior base do CNES em volume e a principal fonte para dimensionar a força de trabalho em saúde no Brasil.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cnes` — CNES: Cadastro Nacional de Estabelecimentos de Saúde |
| **Código no `datasus-fetcher`** | `cnes-pf` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`) |
| **Periodicidade** | Mensal (extração por competência) |
| **Cobertura temporal no FTP** | 2005-08 a 2026-09 (conforme `index.json`) |
| **Volume aproximado no FTP** | 6858 arquivos (~46,7 GB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`) |

## 1. Contexto Institucional e Epidemiológico

O arquivo `PF` integra o CNES, sistema oficial mantido pelo Ministério da Saúde (Secretaria Executiva/DATASUS) e alimentado continuamente pelos estabelecimentos de saúde por meio do SCNES, sob responsabilidade dos gestores estaduais e municipais (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015). Ele materializa a dimensão "trabalhadores" do cadastro e é a base para políticas de gestão do trabalho e da educação na saúde, para a vinculação de produção assistencial (SIH/SIA) e para a identificação de profissionais habilitados.

O **evento gerador** é a declaração mensal dos profissionais vinculados ao estabelecimento na FCES/SCNES. A **unidade de análise é o vínculo** identificado pela terna `CNES` + `CPF_PROF` (ou `CNS_PROF`) + `CBO` + `VINCULAC`, em cada competência. Um mesmo profissional pode ter vários vínculos (em um ou vários estabelecimentos), com diferentes ocupações (CBO) e cargas horárias. O arquivo traz o nome (`NOMEPROF`), o CBO, o CNS, o conselho de classe (`CONSELHO`/`REGISTRO`), os indicadores de vínculo com o SUS (`VINCUL_C`, `VINCUL_A`, `VINCUL_N`) e a carga horária decomposta (hospitalar, ambulatorial e outras).

A nomenclatura histórica reflete sucessivas ampliações: a padronização de CNS e CPF, a introdução de `CPF_UNICO`/`CBO_UNICO` (contadores de unicidade) e o campo `UFMUNRES` (município de residência do profissional). Não há diretório preliminar. O volume é muito alto porque inclui todas as ocupações de nível superior, técnico e médio vinculadas a cada estabelecimento, mês a mês.

Aplicações analíticas típicas: número de médicos, enfermeiros, técnicos e demais profissionais por município/UF, razão profissional por habitante, carga horária média, identificação de profissionais SUS vs. não SUS, planejamento de recursos humanos, estudos de fixação/rotatividade e vinculação de registros de produção (por exemplo, CBO do executante em SIA/SIH).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/PF` | `PF` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `PFSP2401.dbc` — `PF` (Profissionais), `SP` (UF), `24` (ano), `01` (mês). Há também `PFBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-pf/2024-01/cnes-pf_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Profissionais — PF*.dbf") e o pacote de domínios `TAB_CNES.zip` (que inclui a tabela de CBO e de conselhos).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `CPF_PROF` | String (11) | CPF do profissional (ou `99999999999` se não informado) |
| `CNS_PROF` | String (15) | Cartão Nacional de Saúde do profissional |
| `NOMEPROF` | String (60) | Nome do profissional |
| `CBO` | String (6) | Código da ocupação/especialidade (CBO) |
| `CONSELHO` | String (2) | Código do conselho de classe |
| `REGISTRO` | String (13) | Número do registro no conselho de classe |
| `VINCULAC` | String (6) | Vínculo empregatício (código composto) |
| `VINCUL_C` / `VINCUL_A` / `VINCUL_N` | String (1) | Vínculo: contratado SUS / autônomo SUS / não identificado |
| `PROF_SUS` / `PROFNSUS` | String (1) | Caracterização do profissional que realiza atendimento SUS / não SUS |
| `HORA_AMB` / `HORAHOSP` / `HORAOUTR` | String (3) | Carga horária ambulatorial / hospitalar / outras |
| `UFMUNRES` | String (8) | UF + município de residência do profissional |
| `NAT_JUR` | String (4) | Natureza jurídica do estabelecimento |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CNES` (7), `CODUFMUN`/`UFMUNRES` (UF+6), `CBO` (6), `CONSELHO`, `REGISTRO`, `CPF_PROF`, `CNS_PROF` e `NAT_JUR` devem permanecer `String` com zeros à esquerda — em especial `CBO` e o município nunca podem virar inteiro.
- **Datas e competências**: `COMPETEN` é `AAAAMM` e permanece textual; o arquivo não possui colunas de data `AAAAMMDD` típicas.
- **Valores ausentes e sentinelas**: `CPF_PROF = 99999999999` e `CNS_PROF = 999999999999999` são marcadores de ausência previstos pelo dicionário e devem ser tratados como nulo; espaços em branco e `9/99/999` também são convertidos por `SENTINEL_NULLS`; registros `_deleted` são removidos.
- **Particularidades do dataset**: como um profissional pode ter múltiplos vínculos e CBOs, contagens de "profissionais" exigem deduplicação por `CPF_PROF`/`CNS_PROF`; cargas horárias são texto e podem ultrapassar limites plausíveis (validação recomendada); os campos `CPF_UNICO`/`CBO_UNICO` ajudam a detectar duplicidades; e por ser a maior tabela do CNES (~43,5 GB), o processamento deve ser particionado por UF/competência e convertido a Parquet para análises.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-pf
quantilica datasus list cnes-pf

# 2. Baixar microdados de cnes-pf (uf+yearmonth); restrinja UF e período pelo volume
quantilica datasus sync cnes-pf -o ./data --start 2024-01 --end 2024-03 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-pf -o ./data --docs --aux --start 2024-01 --end 2024-03

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-pf -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-03
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-pf/2024-01/cnes-pf_202401-sp@20261015.dbc", clean=True)

# Médicos distintos (CBO inicia com 225) vinculados ao SUS
medicos = (
    qdf.filter(pl.col("cbo").str.starts_with("2254") & (pl.col("prof_sus") == "1"))
    .select(pl.col("cpf_prof").n_unique().alias("medicos_sus"))
)
print(medicos)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/PF`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout PF) e `TAB_CNES.zip` (tabela CBO e conselhos)
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
