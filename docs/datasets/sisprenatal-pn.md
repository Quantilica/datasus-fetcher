# `sisprenatal-pn` — Pré-Natal (SISPRENATAL)

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
| **Volume aproximado no FTP** | 944 arquivos (~232.4 MB); 27 UF(s) na partição; última atualização 2015-01-06 |
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

**Atenção**: os nomes de coluna são representativos do dicionário do sistema, mas o layout do DBF não foi inspecionado diretamente. Confirme em `TAB_SISPRENATAL.zip` ou com `frame.columns`.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `MUN_RES / COD_MUN` | String (IBGE, 6) | Município de residência da gestante. |
| `CNES / UNIDADE` | String (CNES, 7) | Unidade de saúde que realizou o atendimento. |
| `DT_CADASTRO / DT_DUM` | Data | Data do cadastro no pré-natal e data da última menstruação (DUM). |
| `IDADE` | Inteiro | Idade da gestante. |
| `RISCO` | String | Classificação de risco da gestação. |
| `CONSULTAS` | Inteiro | Número de consultas de pré-natal realizadas. |
| `DT_CONSULTA` | Data | Data da consulta de pré-natal. |
| `EXAMES (VDRL, HIV, GLICEMIA, ...)` | String | Exames de rotina do pré-natal e respectivos resultados. |
| `VACINA_ANTITETANICA` | String | Status de imunização antitetânica. |
| `DT_PARTO / CONSULTA_PUERPERAL` | Data / String | Data do parto e realização da consulta puerperal. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CODMUNRES`, `CODMUNOCOR` e `CODMUNNASC` devem ser tratados como `String`; a base usa o código IBGE de 6 dígitos (sem dígito verificador) — mantenha o texto original e use `zfill(6)` apenas se algum arquivo trouxer o código truncado. `CAUSABAS`, `LINHAA`–`LINHAD` e `LINHAII` (CID-10 ou CID-9 conforme o período) e `OCUP`/`CODOCUPMAE` (CBO) são códigos e nunca devem ser convertidos para número. No `wrangle_datasus`, `CODMUNRES` não consta em `CODE_COLUMNS`, mas permanece `String` porque campos caractere do DBF são lidos como texto; `CAUSABAS` e `CAUSABAS_O` constam em `CODE_COLUMNS` e são preservados como `String` limpa.
- **Datas e competências**: nos DBF do SIM e do SINASC as datas (`DTOBITO`, `DTNASC`, `DTCADASTRO`, `DTRECEBIM`, `DTINVESTIG`) vêm como texto `DDMMAAAA`, e `HORAOBITO`/`HORANASC` como `HHMM`. Os nomes sem sublinhado **não** estão em `DATE_COLUMNS` (que cobre `DT_OBITO`, `DT_NASC` etc.), portanto permanecem `String`; converta explicitamente com `pl.col("dtobito").str.to_date("%d%m%Y", strict=False)`.
- **Valores ausentes e sentinelas**: o `wrangle_datasus` faz `strip` das strings e converte em nulo os sentinelas `""`, `" "`, `"999999"`, `"99999999"` e `"00000000"` (data zerada). Códigos categóricos de "ignorado" (`9`, `99`, `999`) **não** viram nulo automaticamente e precisam ser tratados conforme o dicionário de cada variável. Colunas listadas em `INTEGER_COLUMNS` (`IDADE`, `SEXO`, `ESTCIV`, `GRAVIDEZ`, `GESTACAO`, `PARTO`, `CONSULTAS`, `QTDFILVIVO`, `QTDFILMORT`, `ANO`, `MES`) são convertidas para `Int64` com `strict=False`: valores não numéricos (como `M`/`F`/`I` em layouts antigos) viram nulo. Registros com marcador de exclusão dBASE (`_deleted`) são removidos e a coluna é descartada.
Os registros são mensais e uma mesma gestante pode aparecer em vários meses: deduplique antes de calcular indicadores por gestante. Municípios que não digitaram no sistema aparecem como lacuna, e não como zero. Os códigos de município, CNES e exame permanecem `String`; use `frame.columns` para confirmar o layout real.

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
print(frame.columns)  # confirme o nome real das colunas: o layout não foi inspecionado diretamente

print(frame.group_by("consultas").len().sort("consultas"))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SISPRENATAL/201201_/Dados`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde — Programa de Humanização no Pré-Natal e Nascimento (PHPN)**, Portaria GM/MS nº 569/2000, e Rede Cegonha (Portaria GM/MS nº 1.459/2011).
- **Pacote de tabulação no FTP**: `TAB_SISPRENATAL.zip` (inclui o dicionário de variáveis e arquivos de conversão).
- **PCDaS / Fiocruz**: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde** (DATASUS): https://wiki.saude.gov.br/
