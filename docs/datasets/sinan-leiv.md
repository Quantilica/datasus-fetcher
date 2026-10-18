# `sinan-leiv` — Leishmaniose Visceral

O `sinan-leiv` contém os microdados das notificações e investigações de casos de Leishmaniose Visceral (LV, ou calazar; CID-10 B55.0) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de leishmaniose visceral humana, digitada no SINAN Net/Sinan Online. A LV é de notificação compulsória em todo o território nacional e a base é o insumo central da vigilância da leishmaniose visceral humana no país.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-leiv` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 2000 a 2025 (conforme `index.json`) |
| **Volume aproximado no FTP** | 26 arquivos (~13,4 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A leishmaniose visceral é uma zoonose parasitária grave (letalidade elevada quando não tratada) causada no Brasil pela *Leishmania infantum* (sin. *L. chagasi*), transmitida por flebotomíneos — sobretudo *Lutzomyia longipalpis* — com o cão doméstico como principal reservatório urbano. A vigilância é gerida pela SVSA/MS por meio do Programa de Vigilância e Controle da Leishmaniose Visceral (que inclui o componente canino com recolhimento de animais sororreativos). A notificação dos casos humanos é compulsória (Portaria SVS/MS nº 104/2011; hoje na Portaria GM/MS nº 204/2016 e atualizações).

O evento gerador é a **Ficha de Investigação da Leishmaniose Visceral** do SINAN (revisada em 2006/2007 como ficha LV_v5), preenchida diante do caso suspeito — febre longa acompanhada de hepatoesplenomegalia, palidez, anemia, emaciação e/ou emagrecimento — e completada ao longo da investigação com parasitológico de medula óssea ou sorologia (ELISA, IFI), classificação de evolução clínica e desfecho. A unidade de análise é o caso individual notificado, em residentes de áreas com ou sem transmissão documentada.

Marcos normativos e de leiaute: a ficha foi revisada a partir de 2006 e a notificação passou a fluir pelo SINAN Net (2007+) e pelo Sinan Online (2014+). A LV transicionou de perfil rural para periurbano/urbano ao longo de 2000-2010 (grandes surtos metropolitanos em Teresina, Belo Horizonte, São Luís e Fortaleza), com confirmação de casos em áreas demonstrativamente de transmissão intensa.

Aplicações analíticas: coeficiente de detecção anual (casos/100 mil), letalidade específica (alta em pediatria), distribuição por faixa etária, sexo, raça/cor e escolaridade, oportuna vigilância de internações e desfecho (cura, óbito, abandono), e mapeamento de municípios prioritários para controle vetorial e vigilância canina.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `LEIV` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `LEIV` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `LEIVBR00.dbc` — prefixo `LEIV`, `BR` (consolidação nacional) e `00` (ano 2000, início da série disponível); a série vai até `LEIVBR25.dbc` (2025). Conforme o inventário atual do FTP não há arquivo em `PRELIM` para este agravo no momento.
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-leiv/<ano>/sinan-leiv_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-leiv/2025/sinan-leiv_2025-br@20260903.dbc`; arquivos preliminares (quando publicados) recebem o sufixo `-preliminar`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/descompactação/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Leishmaniose Visceral — CID-10 B55.0) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_RACA` | Inteiro | Raça/cor (1-Branca ... 5-Indígena, 9-Ignorado) |
| `ID_MN_RESI` | String (6/7) | Município de residência do caso (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `CLASSI_FIN` | Inteiro | Classificação final do caso (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Abandono, 3 - Óbito por LV, 4 - Óbito por outras causas, 5 - Transferência, 6 - Mudança de diagnóstico) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP`, `ID_MN_RESI` (IBGE 6/7 dígitos), `ID_UNIDADE` (CNES) e CBO como `String` com `zfill`; apenas após normalização de rótulos converter `CLASSI_FIN`/`CRITERIO`/`EVOLUCAO`.
- **Datas e competências**: `DT_NOTIF`, `DT_SIN_PRI`, `DT_INVEST`, `DT_OBITO` e `DT_ENCERRA` em `AAAAMMDD` → `pl.Date`; semanas epidemiológicas permanecem inteiras.
- **Valores ausentes e sentinelas**: células em branco, datas `00000000`, códigos `999999`/`99999999` e `9` (ignorado) normalizados para nulo por `SENTINEL_NULLS`; registros com marcador dBASE de exclusão (`_deleted`) removidos.
- **Particularidades do dataset**: casos de LV podem ter demora de encerramento de vários anos (tratamento prolongado e revisão), de modo que consolidações antigas podem ser corrigidas em republicações; por fim, o agravo não tem arquivo anual em `PRELIM` no inventário atual — recomenda-se sempre verificar com `quantilica datasus list sinan-leiv`; códigos de evolução de LV incluem abandono e mudança de diagnóstico, invisíveis nos agravos agudos.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-leiv
quantilica datasus list sinan-leiv

# 2. Baixar microdados de sinan-leiv com recorte adequado à partição do dataset
quantilica datasus sync sinan-leiv -o ./data --start 2000 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-leiv -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-leiv -o ./data/raw --parquet-dir ./data/parquet --start 2000
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de leishmaniose visceral já tratado
qdf = read_dbc("data/sinan-leiv/2025/sinan-leiv_2025-br@20260903.dbc", clean=True)

# Casos confirmados por ano e letalidade específica
confirmados = qdf.filter(pl.col("classi_fin") == 1)
resumo = confirmados.group_by("nu_ano").agg(
    casos=pl.len(),
    obitos_lv=(pl.col("evolucao") == 3).sum(),
)
print(resumo.sort("nu_ano").with_columns(
    (pl.col("obitos_lv") / pl.col("casos")).alias("letalidade")
))

# Distribuição por faixa etária (anos)
faixas = confirmados.select(
    (pl.col("nu_idade_n") // 1000).alias("idade_anos")
).group_by(
    pl.when(pl.col("idade_anos").cut([1, 4, 9, 19, 39, 59])).alias("faixa")
).len()
print(faixas)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Leishmaniose Visceral (ficha/dicionário unidades de saúde)**: https://portalsinan.saude.gov.br/leishmaniose-visceral
- **Nota técnica e Manual de Vigilância e Controle da Leishmaniose Visceral (SVSA/MS)**
- **Portaria GM/MS nº 204/2016** (notificação compulsória)
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
