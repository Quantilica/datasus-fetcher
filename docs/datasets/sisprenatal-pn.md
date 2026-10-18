# `sisprenatal-pn` — Pré-Natal

Microdados do SISPRENATAL (Sistema de Monitoramento e Avaliação do Pré-Natal, Parto, Puerpério e Criança) do Ministério da Saúde, com registros de acompanhamento de gestantes no SUS entre 2012 e 2014. A unidade de registro é o acompanhamento da gestante, por UF e mês.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sisprenatal` — SISPRENATAL: Sistema de Monitoramento e Avaliação do Pré-Natal, Parto, Puepério e Criança |
| **Código no `datasus-fetcher`** | `sisprenatal-pn` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal |
| **Cobertura temporal no FTP** | 2012-01 a 2014-12 (conforme `index.json`) |
| **Volume aproximado no FTP** | 944 arquivos (~232,4 MB); 27 UF(s) na partição; última atualização 2015-01-06 |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | Não aplicável (o catálogo `meta.docs` não define diretório de documentação para este sistema) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SISPRENATAL/201201_/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O SISPRENATAL foi criado pelo Ministério da Saúde para acompanhar a implementação do Programa de Humanização no Pré-Natal e Nascimento (PHPN, Portaria GM/MS nº 569/2000) e, depois, da Rede Cegonha (2011), registrando o cadastro da gestante, as consultas, os exames e a imunização do pré-natal, além de dados do parto e do puerpério. Sua gestão cabe à área técnica de saúde da mulher (SAPS/MS), com o DATASUS como desenvolvedor.

O instrumento de coleta é a ficha de cadastramento da gestante e as fichas de acompanhamento do pré-natal, digitadas pelas unidades de saúde no sistema. A unidade de análise é a gestante acompanhada (ou o evento de acompanhamento, conforme o arquivo mensal), o que implica atenção a duplicidades entre meses.

A versão disponibilizada no FTP cobre janeiro/2012 a dezembro/2014 (36 competências, 27 UF, ~232 MB), a fase final do sistema legado antes da migração para os sistemas de informação da atenção básica (e-SUS AB/SISAB) e para a estratégia de pré-natal via cadastros ambulatoriais. A cobertura é parcial: municípios que não digitavam no SISPRENATAL ficam fora ou subrepresentados.

Aplicações: proporção de gestantes com 6 ou mais consultas (adequação do pré-natal), início precoce do pré-natal (1º trimestre), realização de exames de rotina (sífilis, HIV), imunização antitetânica e realização de consulta puerperal; análises de qualidade do pré-natal comparadas aos dados do SINASC (`sinasc-dn`).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SISPRENATAL/201201_/Dados` | `PN` | `uf_year2_month_pattern` — UF (2 letras) + ano (2 dígitos) + mês (2 dígitos) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `PNSP1201.dbc` — `PN` (pré-natal) + `SP` (UF) + `12` (ano 2012) + `01` (mês).
- **No armazenamento local do `datasus-fetcher`**: `data/sisprenatal-pn/<AAAAMM>/sisprenatal-pn_<AAAAMM>-<uf>@<AAAAMMDD>.dbc` (ex.: `data/sisprenatal-pn/201201/sisprenatal-pn_201201-sp@20150106.dbc`).
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação: nenhum arquivo catalogado em `documentation/sisprenatal.json` (não há `meta.docs` para `sisprenatal`); o dicionário de variáveis está dentro do pacote de tabulação listado abaixo.
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/sisprenatal.json`):
    - `/dissemin/publicos/SISPRENATAL/201201_/Auxiliar/TAB_SISPRENATAL.zip` (3.8 MB)

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Nomes verificados contra o arquivo real `PNSP1408.dbc` (36 colunas). Não há municípios de residência da gestante, apenas o da UBS.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `NU_ANO_GES` | String (4) | Ano da gestação. |
| `DT_ATEND` | String `AAAAMM` | Competência do atendimento. |
| `CO_UF_IBGE` | String (2) | UF (código IBGE). |
| `CO_MUN_UBS` | String (IBGE, 6) | Município da unidade básica de saúde. |
| `CO_PAIS` | String (3) | País da gestante. |
| `NU_GESTA` / `CO_GESTANT` | String | Número da gestação e identificador da gestante no sistema. |
| `NU_CNS` / `NU_NIS` / `NU_NIS_REP` | String (15) | Cartão Nacional de Saúde e NIS da gestante e do responsável (dados pessoais: tratar conforme a LGPD). |
| `NU_IDADE` | String (15) | Idade da gestante. |
| `DS_ZONA` | String (50) | Zona de residência (descrição). |
| `CO_ESC_GP` / `CO_RAC_GP` / `CO_ETN_GP` / `CO_STF_GP` | String | Escolaridade, raça, etnia e situação familiar da gestante. |
| `DT_DUM` / `DT_DPP` | String `AAAAMMDD` | Data da última menstruação e data provável do parto. |
| `DT_INC` | String `AAAAMMDD` | Data de inclusão do registro. |
| `CO_TPO_GRA` | String (10) | Tipo de gravidez. |
| `ST_GRA_ANT` / `ST_GRA_PLA` / `ST_AUX_DSL` / `ST_GESTAC` | String (1) | Indicadores: gravidez anterior, planejada, auxílio e situação da gestação. |
| `QT_AB_ECT` / `QT_AB_GER` / `QT_AB_MOL` | String (3) | Histórico de abortamentos: ectópicos, gerais e molares. |
| `QT_MOR_APS` / `QT_MOR_PS` / `QT_NSC_MOR` / `QT_NSC_VIV` | String (3) | Mortes (antes e após o primeiro semestre de vida), nascidos mortos e nascidos vivos anteriores. |
| `QT_PRT_CIR` / `QT_PRT_FOR` / `QT_PRT_VAG` | String (3) | Partos anteriores: cesáreos, fórceps e vaginais. |
| `QT_CONS` / `QT_CONSULT` | Inteiro / String (3) | Número de consultas de pré-natal (mesma informação em duas colunas). |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CO_MUN_UBS`, `CO_UF_IBGE`, `NU_CNS`, `NU_NIS` e `CO_GESTANT` devem permanecer `String` (os campos caractere do DBF são lidos como texto), preservando zeros à esquerda; os códigos de município têm 7 caracteres (IBGE com dígito verificador).
- **Datas e competências**: `DT_ATEND` é a competência (`AAAAMM`) e `NU_ANO_GES` o ano; `DT_DUM`, `DT_DPP` e `DT_INC` vêm como texto `AAAAMMDD` e devem ser convertidas explicitamente (`str.to_date("%Y%m%d", strict=False)`).
- **Valores ausentes e sentinelas**: o `wrangle_datasus` faz `strip` das strings e converte `""` e sentinelas em nulo. Códigos categóricos de "ignorado" (por exemplo `9`) **não** viram nulo automaticamente. Registros marcados como excluídos no dBASE (`_deleted`) são removidos.

Os registros são mensais e uma mesma gestante pode aparecer em vários meses: deduplique antes de calcular indicadores por gestante. Municípios que não digitaram no sistema aparecem como lacuna, e não como zero.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sisprenatal-pn
quantilica datasus list sisprenatal-pn

# 2. Baixar microdados de sisprenatal-pn com recorte adequado à partição (uf / yearmonth)
quantilica datasus sync sisprenatal-pn -o ./data --start 2010-01 --end 2012-12 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sisprenatal-pn -o ./data --start 2010-01 --end 2012-12 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sisprenatal-pn -o ./data/raw --parquet-dir ./data/parquet --start 2010-01 --end 2012-12 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

frame = df.read_dbc("data/sisprenatal-pn/201201/sisprenatal-pn_201201-sp@20150106.dbc", dataset="sisprenatal-pn")
print(frame.shape)
print(frame.columns)

print(frame.group_by("qt_cons").len().sort("qt_cons"))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SISPRENATAL/201201_/Dados`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde — Programa de Humanização no Pré-Natal e Nascimento (PHPN)**, Portaria GM/MS nº 569/2000, e Rede Cegonha (Portaria GM/MS nº 1.459/2011).
- **Pacote de tabulação no FTP**: `TAB_SISPRENATAL.zip` (inclui o dicionário de variáveis e arquivos de conversão).
- **PCDaS / Fiocruz**: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde** (DATASUS): https://wiki.saude.gov.br/
