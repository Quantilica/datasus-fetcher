# `siscolo-cc` — Citopatológico de Colo de Útero

Microdados do SISCOLO (INCA/DATASUS) com os laudos citopatológicos do colo do útero realizados no SUS entre 2006 e 2015, por UF e mês. Cada linha representa um exame citopatológico.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `siscolo` — SISCOLO: Sistema de Informações de Cânceres de Colo de Útero |
| **Código no `datasus-fetcher`** | `siscolo-cc` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal |
| **Cobertura temporal no FTP** | 2006-01 a 2015-10 (conforme `index.json`) |
| **Volume aproximado no FTP** | 2858 arquivos (~2,5 GB); 27 UF(s) na partição; última atualização 2022-08-17 |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | Não aplicável (o catálogo `meta.docs` não define diretório de documentação para este sistema) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SISCAN/SISCOLO4/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O SISCOLO (Sistema de Informações do Câncer do Colo do Útero) e o SISMAMA (Sistema de Informação do Câncer de Mama) foram criados pelo Instituto Nacional de Câncer (INCA) e pelo DATASUS para apoiar o monitoramento e a gestão dos programas nacionais de controle dos cânceres do colo do útero e de mama, registrando os exames de rastreamento e de confirmação diagnóstica realizados no SUS. A partir de 2013 ambos foram substituídos gradualmente pelo Sistema de Informação do Câncer (SISCAN), implantado pela Portaria GM/MS nº 3.394/2013 em plataforma web; no FTP, os arquivos do SISCOLO e do SISMAMA ficam sob `SISCAN/` e cobrem apenas o período em que os sistemas legados estavam em uso. Cobertura no FTP: janeiro/2006 a outubro/2015, 27 UF, mensal.

Este dataset contém os laudos de exames citopatológicos (Papanicolaou) do colo do útero, usados no rastreamento organizado da população feminina de 25 a 64 anos; a unidade de análise é o exame (um laudo por linha, não uma mulher). O instrumento de coleta é o requisição/laudo do exame citopatológico, digitado pelos laboratórios no SISCOLO.

Indicadores: cobertura do rastreamento, razão de exames citopatológicos em mulheres de 25–64 anos, percentual de amostras insatisfatórias, percentual de exames alterados (ASC-US, LSIL, HSIL…) e positividade. Uma mulher pode aparecer em vários exames; o rastreamento individual exige vinculação por identificador, quando disponível.

Volume expressivo (~2,5 GB, 2.858 arquivos) em razão do número de exames; prefira recortes por UF e período.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SISCAN/SISCOLO4/Dados` | `CC` | `uf_year2_month_pattern` — UF (2 letras) + ano (2 dígitos) + mês (2 dígitos) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `CCSP1001.dbc` — `CC` (citopatológico) + `SP` (UF) + `10` (ano 2010) + `01` (mês).
- **No armazenamento local do `datasus-fetcher`**: `data/siscolo-cc/<AAAAMM>/siscolo-cc_<AAAAMM>-<uf>@<AAAAMMDD>.dbc` (ex.: `data/siscolo-cc/201001/siscolo-cc_201001-sp@20220817.dbc`).
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação: nenhum arquivo catalogado em `documentation/siscolo.json` (não há `meta.docs` para `siscolo`); o dicionário de variáveis está dentro do pacote de tabulação listado abaixo.
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/siscolo.json`):
    - `/dissemin/publicos/SISCAN/SISCOLO4/Auxiliar/TAB_SISCOLO4.zip` (1.7 MB)

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Nomes verificados contra o arquivo real `CCRJ1503.dbc` (102 colunas; resultado do exame citopatológico do colo do útero). Cada linha é um registro agregado de exames da competência, por isso há muitos contadores (`String` de 8 caracteres).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CO_US` / `CO_US_UF` / `CO_US_IBGE` | String | Unidade solicitante: código, UF e município (IBGE, 7). |
| `CO_CNES` | String (CNES, 7) | CNES do estabelecimento. |
| `REGUS` / `REGRESID` / `REGLAB` | String | Indicadores de região da unidade, da residência e do laboratório. |
| `CO_PAC_UF` / `CO_PAC_IBG` | String | UF e município (IBGE, 7) de residência da paciente. |
| `ANO_COMP` / `DT_ID_COMP` | String | Ano e competência (`AAAAMM`) do registro. |
| `CO_FX_ETAR` | String | Faixa etária da paciente. |
| `DINTCOLETA` / `DINTRESULT` / `DINTTEMPEX` | String | Intervalos (categorizados) entre coleta, resultado e tempo de exame. |
| `QTDEXA` | String | Quantidade de exames do registro. |
| `CO_PAC_IDA` | String (3) | Idade da paciente. |
| `CO_PAC_ESC` / `CO_PAC_RAC` | String | Escolaridade e raça/cor da paciente. |
| `CO_RES_NOR` | String | Indicador de residência (campo do layout). |
| `CLABIBGE` / `CLABUF` | String | Município (IBGE, 7) e UF do laboratório. |
| `CO_ATI_ESC` / `CO_ATI_GLA` / `CO_ATI_IND` / `CO_CEL_ESC` / `CO_CEL_GLA` / `CO_NEO_MAL` | String | Indicadores de atipias e neoplasia maligna nas células escamosas e glandulares. |
| `CO_AMOSTRA` / `CO_ADEQ_MA` | String | Indicador de amostra e adequabilidade do material (satisfatória/insatisfatória). |
| `CO_BEN_INF` / `CO_BEN_MET` / `CO_BEN_REP` / `CO_BEN_ATR` / `CO_BEN_RAD` / `CO_BEN_OUT` | String | Alterações benignas: inflamação, metaplasia, reparação, atrofia, radiação e outras. |
| `CO_MIC_LAC` / `CO_MIC_COC` / `CO_MIC_CHL` / `CO_MIC_ACT` / `CO_MIC_BAC` / `CO_MIC_TRI` / `CO_MIC_HER` / `CO_MIC_CAN` / `CO_MIC_GAR` / `CO_MIC_OUT` | String | Microbiologia: Lactobacillus, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, herpes, Candida, Gardnerella e outros. |
| `CO_ANM_PRE` / `DT_ANM_PRE` | String | Exame citopatológico anterior e ano de realização. |
| `ST_MON_EXT` / `TEMPCITANT` | String | Indicadores de monitoramento externo e tempo desde a citologia anterior. |
| `QUANTEXAME` / `REPREZT` / `RESNORM` / `POSNAONEO` / `LESALTGRA` / `PSNAONPLA` / `NLSALTGRA` / `PSNNPLA` / `NALTGRA` / `LBGRAU` / `LAGRAU` / `LAGRAUMI`` | String (8) | Contadores agregados por registro de resultados (representatividade, normal, lesões de baixo e alto grau etc.). |
| `CARCINO` / `C_EPI_ESCA` / `C_EPI_GLAN` / `CO_EPI_MET` / `ADENCARCIN` / `DENCARCINV` / `OUTNEO` / `ALTERADO` / `CVCIONAL` / `MEIOLIQU` | String (8) | Contadores de carcinomas epiteliais, adenocarcinomas, outras neoplasias e demais resultados. |
| `AMOSREJAUS` / `AMOSREJDAN` / `AMOSREJALH` / `AMOSREJOUT` / `REJEITADA` / `SATISFACT` / `INSATSFAC` / `CO_INSA_AC` / `CO_INSA_SA` / `CO_INSA_PI` / `CO_INSA_AR` / `CO_INSA_CO` / `CO_INSA_SU` / `CO_INSA_OU` | String (8) | Contadores de amostras rejeitadas, satisfatórias e insatisfatórias, com motivos. |
| `CBEMINFLA` / `CBEMMETAS` / `CBEMREPAR` / `CBEMATROF` / `CBEMRADI` / `CBEMOUT` / `CMICLACT` / `CMICCOCO` / `CMICCHLA` / `CMICACTI` / `CMICBACI` / `CMICTRICO` / `CMICHERP` / `CMICCAND` / `CMICGARD` / `CMICOUT`` | String (8) | Contadores agregados de alterações benignas e microbiologia. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CO_US_IBGE`, `CO_PAC_IBG`, `CLABIBGE`, `CO_CNES` e `CO_US` devem permanecer `String` (os campos caractere do DBF são lidos como texto), preservando zeros à esquerda; os códigos de município têm 7 caracteres (IBGE com dígito verificador).
- **Datas e competências**: `DT_ID_COMP` é a competência (`AAAAMM`) e `ANO_COMP` o ano; não há colunas de data completa neste arquivo.
- **Valores ausentes e sentinelas**: o `wrangle_datasus` faz `strip` das strings e converte `""` e sentinelas em nulo. Códigos categóricos de "ignorado" (por exemplo `9`) **não** viram nulo automaticamente. Registros marcados como excluídos no dBASE (`_deleted`) são removidos.

Um registro não equivale a uma mulher: para cobertura populacional é necessário deduplicar. Os arquivos usam UF de **residência** (`CO_PAC_UF`) ou da unidade (`CO_US_UF`) conforme o campo; verifique antes de agregar por UF. Como o sistema legado foi substituído pelo SISCAN, os dados cobrem somente 2006–2015.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para siscolo-cc
quantilica datasus list siscolo-cc

# 2. Baixar microdados de siscolo-cc com recorte adequado à partição (uf / yearmonth)
quantilica datasus sync siscolo-cc -o ./data --start 2010-01 --end 2012-12 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync siscolo-cc -o ./data --start 2010-01 --end 2012-12 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline siscolo-cc -o ./data/raw --parquet-dir ./data/parquet --start 2010-01 --end 2012-12 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

frame = df.read_dbc("data/siscolo-cc/201001/siscolo-cc_201001-sp@20220817.dbc", dataset="siscolo-cc")
print(frame.shape)
print(frame.columns)

print(frame.group_by('co_adeq_ma').len().sort('len', descending=True).head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SISCAN/SISCOLO4/Dados`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **INCA — Sistema de Informação do Câncer (SISCAN)**: https://www.gov.br/inca/pt-br/assuntos/gestor-e-profissional-de-saude/siscan
- **Portaria GM/MS nº 3.394/2013** — institui o SISCAN.
- **Pacote de tabulação no FTP**: `TAB_SISCOLO4.zip` (inclui o dicionário de variáveis e arquivos `.cnv`/`.def` para tabulação).
- **PCDaS / Fiocruz**: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde** (DATASUS): https://wiki.saude.gov.br/
