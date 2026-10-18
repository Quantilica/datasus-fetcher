# `sismama-cm` — Citopatológico de Mama

Microdados do SISMAMA (INCA/DATASUS) com os exames citopatológicos de mama realizados no SUS entre 2009 e 2015, por UF e mês. Cada linha representa um exame.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sismama` — SISMAMA: Sistema de Informações de Cânceres de Mama |
| **Código no `datasus-fetcher`** | `sismama-cm` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal |
| **Cobertura temporal no FTP** | 2009-01 a 2015-07 (conforme `index.json`) |
| **Volume aproximado no FTP** | 1675 arquivos (~5,0 MB); 27 UF(s) na partição; última atualização 2022-08-31 |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | Não aplicável (o catálogo `meta.docs` não define diretório de documentação para este sistema) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SISCAN/SISMAMA/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O SISCOLO (Sistema de Informações do Câncer do Colo do Útero) e o SISMAMA (Sistema de Informação do Câncer de Mama) foram criados pelo Instituto Nacional de Câncer (INCA) e pelo DATASUS para apoiar o monitoramento e a gestão dos programas nacionais de controle dos cânceres do colo do útero e de mama, registrando os exames de rastreamento e de confirmação diagnóstica realizados no SUS. A partir de 2013 ambos foram substituídos gradualmente pelo Sistema de Informação do Câncer (SISCAN), implantado pela Portaria GM/MS nº 3.394/2013 em plataforma web; no FTP, os arquivos do SISCOLO e do SISMAMA ficam sob `SISCAN/` e cobrem apenas o período em que os sistemas legados estavam em uso. Cobertura no FTP: janeiro/2009 a julho/2015, 27 UF, mensal.

Este dataset contém os exames citopatológicos de mama (punção aspirativa por agulha fina e citologia de secreção), realizados na investigação diagnóstica de lesões palpáveis ou suspeitas; a unidade de análise é o exame. O instrumento é a requisição/laudo citopatológico de mama, preenchido pelos laboratórios no SISMAMA.

Indicadores: percentual de exames suspeitos ou positivos, percentual de amostras insatisfatórias e fluxo da investigação (citologia → histopatologia). O volume é pequeno (~5 MB), pois o exame é restrito à investigação diagnóstica; a mamografia de rastreamento não está neste dataset.

No fluxo do SISMAMA, o citopatológico antecede a confirmação histopatológica (`sismama-hm`).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SISCAN/SISMAMA/Dados` | `CM` | `uf_year2_month_pattern` — UF (2 letras) + ano (2 dígitos) + mês (2 dígitos) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `CMSP1001.dbc` — `CM` (citopatológico de mama) + `SP` (UF) + `10` (ano 2010) + `01` (mês).
- **No armazenamento local do `datasus-fetcher`**: `data/sismama-cm/<AAAAMM>/sismama-cm_<AAAAMM>-<uf>@<AAAAMMDD>.dbc` (ex.: `data/sismama-cm/201001/sismama-cm_201001-sp@20220817.dbc`).
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação: nenhum arquivo catalogado em `documentation/sismama.json` (não há `meta.docs` para `sismama`); o dicionário de variáveis está dentro do pacote de tabulação listado abaixo.
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/sismama.json`):
    - `/dissemin/publicos/SISCAN/SISMAMA/Auxiliar/TAB_SISMAMA.zip` (3.2 MB)

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Nomes verificados contra o arquivo real `CMSP1501.dbc` (54 colunas; resultado do exame citopatológico de mama). Cada linha é um registro agregado de exames da competência.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CO_PAC_UF` / `CO_PAC_IBG` | String | UF e município (IBGE, 7) de residência da paciente. |
| `CO_US_UF` / `CO_US_IBGE` / `CO_US` / `CO_CNES` | String | UF, município (IBGE, 7), código e CNES da unidade solicitante. |
| `PRESTUF` / `PRESTMUN` | String | UF e município do prestador do serviço. |
| `REGUS` / `REGRESID` / `REGLAB` | String | Indicadores de região da unidade, da residência e do laboratório. |
| `ANO_COMP` / `DT_ID_COMP` | String | Ano e competência (`AAAAMM`) do registro. |
| `CO_FX_ETAR` | String | Faixa etária da paciente. |
| `CO_PAC_ESC` / `CO_PAC_SEX` / `CO_PAC_RAC` | String | Escolaridade, sexo e raça/cor da paciente. |
| `DINTCOLETA` / `DINTRESULT` / `DINTTEMPEX` | String | Intervalos (categorizados) entre coleta, resultado e tempo de exame. |
| `QUANTEXAME` | String (8) | Quantidade de exames do registro. |
| `CANMPACANC` | String | Paciente com câncer de mama prévio (indicador). |
| `CO_CLI_DES` / `CO_CLI_NOD` / `CCLIMATMAM` / `CCLIMATDPC` | String | Dados clínicos: descarga papilar, nódulo e achados de mama/densidade. |
| `CO_RES_ADE` / `PRESULPAAF` | String | Adequabilidade do material e resultado da PAAF. |
| `CRESBENIG` / `CRESMALIIN` / `CRESSUSMAL` / `CRESPOSMAL` / `CRESDERPAP` | String | Resultado do exame citopatológico: benigno, maligno indeterminado, suspeito, positivo e derrame papilar. |
| `PBENMASTIT` / `PBENABSUBA` / `PBENFIBROA` / `PBENNECGOR` / `PBENCONDFI` / `PBENLESEPI` / `PBENOUTRAS` | String (8) | Contadores de achados benignos (mastite, abscesso subareolar, fibroadenoma, necrose gordurosa, condição fibrocística, lesão epitelial e outras). |
| `PMALINTUMP` / `PMALINTUMF` / `PMALINOUTR` / `PSUSLEJPCA` / `PSUSOUTROS` / `PPOSMACDUC` / `PPOSMACLOB` / `PPOSMACOUT` | String (8) | Contadores de achados malignos, suspeitos e positivos (carcinoma ductal, lobular e outros). |
| `DEMATACELU` / `DENEGMALIG` / `DEMALIINDT` / `DEPOSMALIG` / `DELESMALIG` / `DEPROCINFL` | String (8) | Contadores de derrame papilar e processo inflamatório (material acelular, negativo, indeterminado, positivo etc.). |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CO_US_IBGE`, `CO_PAC_IBG`, `PRESTMUN`, `CO_CNES` e `CO_US` devem permanecer `String` (os campos caractere do DBF são lidos como texto), preservando zeros à esquerda; os códigos de município têm 7 caracteres (IBGE com dígito verificador).
- **Datas e competências**: `DT_ID_COMP` é a competência (`AAAAMM`) e `ANO_COMP` o ano; não há colunas de data completa neste arquivo.
- **Valores ausentes e sentinelas**: o `wrangle_datasus` faz `strip` das strings e converte `""` e sentinelas em nulo. Códigos categóricos de "ignorado" (por exemplo `9`) **não** viram nulo automaticamente. Registros marcados como excluídos no dBASE (`_deleted`) são removidos.

Um registro não equivale a uma mulher: deduplique para cobertura populacional. O arquivo inclui `CO_PAC_SEX`, pois pode haver registros de homens. O sistema legado foi substituído pelo SISCAN.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sismama-cm
quantilica datasus list sismama-cm

# 2. Baixar microdados de sismama-cm com recorte adequado à partição (uf / yearmonth)
quantilica datasus sync sismama-cm -o ./data --start 2010-01 --end 2012-12 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sismama-cm -o ./data --start 2010-01 --end 2012-12 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sismama-cm -o ./data/raw --parquet-dir ./data/parquet --start 2010-01 --end 2012-12 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

frame = df.read_dbc("data/sismama-cm/201001/sismama-cm_201001-sp@20220817.dbc", dataset="sismama-cm")
print(frame.shape)
print(frame.columns)

print(frame.group_by('co_res_ade').len().sort('len', descending=True).head(10))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SISCAN/SISMAMA/Dados`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **INCA — Sistema de Informação do Câncer (SISCAN)**: https://www.gov.br/inca/pt-br/assuntos/gestor-e-profissional-de-saude/siscan
- **Portaria GM/MS nº 3.394/2013** — institui o SISCAN.
- **Pacote de tabulação no FTP**: `TAB_SISMAMA.zip` (inclui o dicionário de variáveis e arquivos `.cnv`/`.def` para tabulação).
- **PCDaS / Fiocruz**: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde** (DATASUS): https://wiki.saude.gov.br/
