# `siscolo-hc` — Histopatológico de Colo de Útero

Microdados do SISCOLO (INCA/DATASUS) com os laudos histopatológicos do colo do útero realizados no SUS entre 2006 e 2015, por UF e mês. Cada linha é um laudo histopatológico.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `siscolo` — SISCOLO: Sistema de Informações de Cânceres de Colo de Útero |
| **Código no `datasus-fetcher`** | `siscolo-hc` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal |
| **Cobertura temporal no FTP** | 2006-01 a 2015-10 (conforme `index.json`) |
| **Volume aproximado no FTP** | 2858 arquivos (~40,8 MB); 27 UF(s) na partição; última atualização 2022-08-17 |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | Não aplicável (o catálogo `meta.docs` não define diretório de documentação para este sistema) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SISCAN/SISCOLO4/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O SISCOLO (Sistema de Informações do Câncer do Colo do Útero) e o SISMAMA (Sistema de Informação do Câncer de Mama) foram criados pelo Instituto Nacional de Câncer (INCA) e pelo DATASUS para apoiar o monitoramento e a gestão dos programas nacionais de controle dos cânceres do colo do útero e de mama, registrando os exames de rastreamento e de confirmação diagnóstica realizados no SUS. A partir de 2013 ambos foram substituídos gradualmente pelo Sistema de Informação do Câncer (SISCAN), implantado pela Portaria GM/MS nº 3.394/2013 em plataforma web; no FTP, os arquivos do SISCOLO e do SISMAMA ficam sob `SISCAN/` e cobrem apenas o período em que os sistemas legados estavam em uso. Cobertura no FTP: janeiro/2006 a outubro/2015, 27 UF, mensal.

Este dataset reúne os laudos histopatológicos do colo do útero, que confirmam o diagnóstico após citologia alterada ou colposcopia; a unidade de análise é o laudo (peça ou biópsia), não a mulher. O instrumento é a requisição/laudo histopatológico preenchido pelos laboratórios no SISCOLO.

Indicadores: proporção de lesões intraepiteliais de alto grau (NIC II/III) e de carcinoma entre as biópsias, tempo entre citologia alterada e confirmação (quando houver vinculação) e seguimento de mulheres com exame alterado.

Complementa `siscolo-cc` na confirmação diagnóstica, sendo o segundo passo do fluxo de rastreamento.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SISCAN/SISCOLO4/Dados` | `HC` | `uf_year2_month_pattern` — UF (2 letras) + ano (2 dígitos) + mês (2 dígitos) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `HCSP1001.dbc` — `HC` (histopatológico) + `SP` (UF) + `10` (ano 2010) + `01` (mês).
- **No armazenamento local do `datasus-fetcher`**: `data/siscolo-hc/<AAAAMM>/siscolo-hc_<AAAAMM>-<uf>@<AAAAMMDD>.dbc` (ex.: `data/siscolo-hc/201001/siscolo-hc_201001-sp@20220817.dbc`).
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação: nenhum arquivo catalogado em `documentation/siscolo.json` (não há `meta.docs` para `siscolo`); o dicionário de variáveis está dentro do pacote de tabulação listado abaixo.
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/siscolo.json`):
    - `/dissemin/publicos/SISCAN/SISCOLO4/Auxiliar/TAB_SISCOLO4.zip` (1.7 MB)

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Nomes verificados contra o arquivo real `HCSP1505.dbc` (115 colunas; resultado do exame histopatológico do colo do útero). Muitos campos são contadores agregados (`String` de 8 caracteres).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CO_US` / `CO_US_UF` / `CO_US_IBGE` | String | Unidade solicitante: código, UF e município (IBGE, 7). |
| `CO_CNES` | String (CNES, 7) | CNES do estabelecimento. |
| `REGUS` / `REGRESID` / `REGLAB` | String | Indicadores de região da unidade, da residência e do laboratório. |
| `CO_PAC_UF` / `CO_PAC_IBG` | String | UF e município (IBGE, 7) de residência da paciente. |
| `ANO_COMP` / `DT_ID_COMP` | String | Ano e competência (`AAAAMM`) do registro. |
| `CO_FX_ETAR` | String | Faixa etária da paciente. |
| `DINTCOLETA` / `DINTRESULT` / `DINTTEMPEX` | String | Intervalos (categorizados) entre coleta, resultado e tempo de exame. |
| `DT_PAC_NAS` | String `DD/MM/AAAA` | Data de nascimento da paciente. |
| `CO_PAC_IDA` | String (3) | Idade da paciente. |
| `CO_PAC_ESC` / `CO_PAC_RAC` | String | Escolaridade e raça/cor da paciente. |
| `CLABIBGE` / `CLABUF` / `CLABCID` | String | Município (IBGE, 7), UF e nome da cidade do laboratório. |
| `CO_CIT_ESC` / `CO_CIT_GLA` / `CO_CIT_IND` / `O_CIT_ESCA` / `O_CIT_GLAN` / `CO_COLP` / `CO_RES_TIP` / `CO_RES_LOC` | String | Citologia prévia (escamosa, glandular, indeterminada), colposcopia e tipo/local do resultado. |
| `CO_BEN_CER` / `CO_BEN_ALT` / `CO_NEO_NIC` / `CO_NEO_ADE` / `CO_DIF_GRA` | String | Diagnóstico histopatológico: alterações benignas, NIC, adenocarcinoma e grau de diferenciação. |
| `CO_EXTEN_P` / `CO_EXTEN_V` / `O_EXTEN_PE` / `O_EXTEN_PA` / `CO_EXTEN_C` / `O_EXTEN_VA` / `CO_MARG`` | String | Extensão da lesão e margens. |
| `CO_RES_FRA` / `CO_RES_TAM` / `O_RES_TAM2` / `CO_RES_MAR` | String | Fragmentos, tamanhos da peça e margens cirúrgicas. |
| `DT_HIS_EXA` / `DT_HIS_REC` | String `DD/MM/AAAA` | Datas do exame e do recebimento do histopatológico. |
| `CO_MAT_INS` / `CO_CTRL_FR` / `CO_CTRL_BL` | String | Material insatisfatório e controles de fragmentos e blocos. |
| `QTDEXA` | String (8) | Quantidade de exames do registro. |
| `ESCAMOSA` / `PNEOPLA` / `GPNNEOP` / `GNALTGRAU` / `INDPNAONEO` / `CITINDALGR` / `ESCLIPBX` / `ESCINALT` / `ESCIEMCINV` / `ESCCARINVA` / `ADENOINSUT` / `ADENCARCIN` / `CIT_OUTNEO`` | String (8) | Contadores de resultados citológicos (escamosos, glandulares, neoplasias). |
| `CCOLDEFAUL` / `CCOLNORMAL` / `CCOLANORMA` / `CCOLINSATI` / `CO_COLP_PO` / `O_COLP_POS` / `CO_COLP_BI` / `CO_COLP_CU` / `CO_COLP_EX` / `CO_COLP_RE` / `O_COLP_BIO`` | String (8) | Contadores de colposcopia (normal, anormal, insatisfatória, biópsia, curetagem etc.). |
| `CRESBIOPSI` / `CRESCONIZA` / `CRESHISSIM` / `CRESPANHIS` / `CRESOUTROS` / `CRESECTO` / `CRESENDO` / `CRESJUNC`` | String (8) | Contadores por tipo de procedimento/resultado (biópsia, conização, histerectomia etc.). |
| `CO_BEN_MET` / `CO_BEN_POL` / `CBENCERVI` / `CBENALTER` | String (8) | Contadores de alterações benignas (metaplasia, pólipo, cervicite e outras). |
| `NICDLEVE` / `NICDMODE` / `NICDACENT` / `NICCARCMIN` / `NICEPIINVA` / `NICIMPAVAL` / `NICVERRUCO` / `NICNAOCERA` / `NEOINSUTU` / `NEOMUCINO` / `NEOVILOGL` / `DS_NEO_OUT` | String (8) | Contadores de NIC e neoplasias por tipo. |
| `CDIFGRAU` / `CDIFMODDIF` / `CDIFPOUDIF` / `CDIFINDFER` / `CDIEXAMINS` / `C_EXT_VASC` / `C_EXT_PERI` / `C_EXT_PARA` / `C_EXT_CORP` / `C_EXT_VAGI` / `CO_EXTEN_L` / `O_EXTEN_LI` / `CMARLIVRE` / `CMARCOMPRO` / `CMARIMPAVA`` | String (8) | Contadores de diferenciação, extensão (vascular, perineural, paramétrio, corpo, vagina) e margens. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CO_US_IBGE`, `CO_PAC_IBG`, `CLABIBGE`, `CO_CNES` e `CO_US` devem permanecer `String` (os campos caractere do DBF são lidos como texto), preservando zeros à esquerda; os códigos de município têm 7 caracteres (IBGE com dígito verificador).
- **Datas e competências**: `DT_ID_COMP` é a competência (`AAAAMM`) e `ANO_COMP` o ano; `DT_PAC_NAS`, `DT_HIS_EXA` e `DT_HIS_REC` vêm como texto `DD/MM/AAAA` e devem ser convertidas explicitamente (`str.to_date("%d/%m/%Y", strict=False)`).
- **Valores ausentes e sentinelas**: o `wrangle_datasus` faz `strip` das strings e converte `""` e sentinelas em nulo. Códigos categóricos de "ignorado" (por exemplo `9`) **não** viram nulo automaticamente. Registros marcados como excluídos no dBASE (`_deleted`) são removidos.

Um registro não equivale a uma mulher: para cobertura populacional é necessário deduplicar. Verifique se o filtro por UF usa a residência (`CO_PAC_UF`) ou a unidade (`CO_US_UF`). Como o sistema legado foi substituído pelo SISCAN, os dados cobrem somente 2006–2015.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para siscolo-hc
quantilica datasus list siscolo-hc

# 2. Baixar microdados de siscolo-hc com recorte adequado à partição (uf / yearmonth)
quantilica datasus sync siscolo-hc -o ./data --start 2010-01 --end 2012-12 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync siscolo-hc -o ./data --start 2010-01 --end 2012-12 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline siscolo-hc -o ./data/raw --parquet-dir ./data/parquet --start 2010-01 --end 2012-12 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

frame = df.read_dbc("data/siscolo-hc/201001/siscolo-hc_201001-sp@20220817.dbc", dataset="siscolo-hc")
print(frame.shape)
print(frame.columns)

print(frame.group_by('co_cit_esc').len().sort('len', descending=True).head(10))
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
