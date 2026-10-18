# `sismama-hm` — Histopatológico de Mama (SISMAMA)

Microdados do SISMAMA (INCA/DATASUS) com os laudos histopatológicos de mama realizados no SUS entre 2009 e 2015, por UF e mês. Cada linha é um laudo histopatológico.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sismama` — SISMAMA: Sistema de Informações de Cânceres de Mama |
| **Código no `datasus-fetcher`** | `sismama-hm` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`) |
| **Particionamento** | `uf / yearmonth` |
| **Periodicidade** | Mensal |
| **Cobertura temporal no FTP** | 2009-01 a 2015-07 (conforme `index.json`) |
| **Volume aproximado no FTP** | 1674 arquivos (~5.9 MB); 27 UF(s) na partição; última atualização 2022-08-31 |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | Não aplicável (o catálogo `meta.docs` não define diretório de documentação para este sistema) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SISCAN/SISMAMA/Auxiliar` |

## 1. Contexto Institucional e Epidemiológico

O SISCOLO (Sistema de Informações do Câncer do Colo do Útero) e o SISMAMA (Sistema de Informação do Câncer de Mama) foram criados pelo Instituto Nacional de Câncer (INCA) e pelo DATASUS para apoiar o monitoramento e a gestão dos programas nacionais de controle dos cânceres do colo do útero e de mama, registrando os exames de rastreamento e de confirmação diagnóstica realizados no SUS. A partir de 2013 ambos foram substituídos gradualmente pelo Sistema de Informação do Câncer (SISCAN), implantado pela Portaria GM/MS nº 3.394/2013 em plataforma web; no FTP, os arquivos do SISCOLO e do SISMAMA ficam sob `SISCAN/` e cobrem apenas o período em que os sistemas legados estavam em uso. Cobertura no FTP: janeiro/2009 a julho/2015, 27 UF, mensal.

Este dataset reúne os laudos histopatológicos de mama, incluindo biópsias e peças cirúrgicas, com dados de diagnóstico, estadiamento patológico e margens; a unidade de análise é o laudo. O instrumento é a requisição/laudo histopatológico de mama, preenchido pelos laboratórios no SISMAMA.

Indicadores: proporção de lesões malignas entre as biópsias, distribuição por tipo histológico, tamanho tumoral e acometimento linfonodal ao diagnóstico, que servem como proxy de estadiamento.

Sucede o `sismama-cm` na confirmação diagnóstica; volume pequeno (~6 MB).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SISCAN/SISMAMA/Dados` | `HM` | `uf_year2_month_pattern` — UF (2 letras) + ano (2 dígitos) + mês (2 dígitos) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `HMSP1001.dbc` — `HM` (histopatológico de mama) + `SP` (UF) + `10` (ano 2010) + `01` (mês).
- **No armazenamento local do `datasus-fetcher`**: `data/sismama-hm/<AAAAMM>/sismama-hm_<AAAAMM>-<uf>@<AAAAMMDD>.dbc` (ex.: `data/sismama-hm/201001/sismama-hm_201001-sp@20220817.dbc`).
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação: nenhum arquivo catalogado em `documentation/sismama.json` (não há `meta.docs` para `sismama`); o dicionário de variáveis está dentro do pacote de tabulação listado abaixo.
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/sismama.json`):
    - `/dissemin/publicos/SISCAN/SISMAMA/Auxiliar/TAB_SISMAMA.zip` (3.2 MB)

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

**Atenção**: os nomes de coluna abaixo são os mais prováveis conforme o dicionário do sistema, mas o layout do DBF não foi inspecionado diretamente neste levantamento. Confirme em `TAB_SISCOLO4.zip`/`TAB_SISMAMA.zip` ou com `frame.columns` antes de usar.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `MUN_RES / COD_MUN` | String (IBGE, 6) | Município de residência da mulher. |
| `CNES / UNIDADE` | String (CNES, 7) | Unidade solicitante. |
| `IDADE` | Inteiro | Idade da paciente. |
| `DT_COLETA / DT_RESULT` | Data | Datas da coleta e do resultado. |
| `TIPO_PROC` | String | Procedimento: biópsia por agulha grossa, cirúrgica, mastectomia, quadrantectomia etc. |
| `DIAGNOSTICO` | String | Diagnóstico histopatológico: benigno, carcinoma in situ, carcinoma invasor, etc. |
| `TAMANHO_TUMOR` | Float / String | Tamanho do tumor (cm), quando informado. |
| `LINFONODOS` | String | Status dos linfonodos axilares, quando informado. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CODMUNRES`, `CODMUNOCOR` e `CODMUNNASC` devem ser tratados como `String`; a base usa o código IBGE de 6 dígitos (sem dígito verificador) — mantenha o texto original e use `zfill(6)` apenas se algum arquivo trouxer o código truncado. `CAUSABAS`, `LINHAA`–`LINHAD` e `LINHAII` (CID-10 ou CID-9 conforme o período) e `OCUP`/`CODOCUPMAE` (CBO) são códigos e nunca devem ser convertidos para número. No `wrangle_datasus`, `CODMUNRES` não consta em `CODE_COLUMNS`, mas permanece `String` porque campos caractere do DBF são lidos como texto; `CAUSABAS` e `CAUSABAS_O` constam em `CODE_COLUMNS` e são preservados como `String` limpa.
- **Datas e competências**: nos DBF do SIM e do SINASC as datas (`DTOBITO`, `DTNASC`, `DTCADASTRO`, `DTRECEBIM`, `DTINVESTIG`) vêm como texto `DDMMAAAA`, e `HORAOBITO`/`HORANASC` como `HHMM`. Os nomes sem sublinhado **não** estão em `DATE_COLUMNS` (que cobre `DT_OBITO`, `DT_NASC` etc.), portanto permanecem `String`; converta explicitamente com `pl.col("dtobito").str.to_date("%d%m%Y", strict=False)`.
- **Valores ausentes e sentinelas**: o `wrangle_datasus` faz `strip` das strings e converte em nulo os sentinelas `""`, `" "`, `"999999"`, `"99999999"` e `"00000000"` (data zerada). Códigos categóricos de "ignorado" (`9`, `99`, `999`) **não** viram nulo automaticamente e precisam ser tratados conforme o dicionário de cada variável. Colunas listadas em `INTEGER_COLUMNS` (`IDADE`, `SEXO`, `ESTCIV`, `GRAVIDEZ`, `GESTACAO`, `PARTO`, `CONSULTAS`, `QTDFILVIVO`, `QTDFILMORT`, `ANO`, `MES`) são convertidas para `Int64` com `strict=False`: valores não numéricos (como `M`/`F`/`I` em layouts antigos) viram nulo. Registros com marcador de exclusão dBASE (`_deleted`) são removidos e a coluna é descartada.
As colunas de código (município, CNES do laboratório/unidade, CID-O) devem permanecer `String`. Os sentinelas padrão são anulados pelo `wrangle_datasus`, mas códigos de "ignorado/não informado" próprios do sistema não são. Os arquivos usam UF de **residência** ou de **atendimento** conforme o campo; verifique antes de agregar por UF. Alguns campos tumorais podem vir como texto livre ou com unidades diferentes; trate `TAMANHO_TUMOR` com cuidado antes de converter para número. O dataset cobre apenas 2009–2015.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sismama-hm
quantilica datasus list sismama-hm

# 2. Baixar microdados de sismama-hm com recorte adequado à partição (uf / yearmonth)
quantilica datasus sync sismama-hm -o ./data --start 2010-01 --end 2012-12 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sismama-hm -o ./data --start 2010-01 --end 2012-12 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sismama-hm -o ./data/raw --parquet-dir ./data/parquet --start 2010-01 --end 2012-12 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

frame = df.read_dbc("data/sismama-hm/201001/sismama-hm_201001-sp@20220817.dbc", dataset="sismama-hm")
print(frame.shape)
print(frame.columns)  # confirme o nome real das colunas: o layout não foi inspecionado diretamente

print(frame.group_by('diagnostico').len().sort('len', descending=True).head(10))
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
