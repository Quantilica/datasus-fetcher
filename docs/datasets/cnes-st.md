# `cnes-st` — Estabelecimentos

O `cnes-st` contém os microdados do arquivo de **Estabelecimentos** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), o cadastro oficial e obrigatório de todos os estabelecimentos de saúde — públicos, privados e conveniados — que realizam ações e serviços de saúde no território nacional. Cada registro (linha) representa um estabelecimento de saúde identificado pelo número nacional CNES, em uma determinada competência (mês/ano) e UF. É a tabela-raiz do CNES: todas as demais tabelas (profissionais, leitos, equipamentos, serviços, equipes) referenciam o `CNES` nela cadastrado.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `cnes` — CNES: Cadastro Nacional de Estabelecimentos de Saúde |
| **Código no `datasus-fetcher`** | `cnes-st` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `yearmonth` (um arquivo por UF e competência mensal, além da consolidação `br`) |
| **Periodicidade** | Mensal (extração por competência) |
| **Cobertura temporal no FTP** | 2005-08 a 2026-09 (conforme `index.json`) |
| **Volume aproximado no FTP** | 6858 arquivos (~3,4 GB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`) |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`) |

## 1. Contexto Institucional e Epidemiológico

O CNES é gerido pelo Ministério da Saúde por intermédio da Secretaria Executiva/DATASUS (Divisão de Disseminação de Informações em Saúde — DIDIS) e da Coordenação-Geral de Sistemas de Informação da então SAS. O cadastro foi criado pela Portaria SAS/MS nº 403/2000, teve a Ficha Cadastral dos Estabelecimentos de Saúde (FCES) aprovada pela Portaria SAS/MS nº 511/2000 e foi reinstituído como sistema de informação oficial pela Portaria GM/MS nº 1.646/2015. Sua manutenção é responsabilidade compartilhada dos gestores estaduais e municipais de saúde, com alimentação continuada pelos próprios estabelecimentos no SCNES (Sistema do Cadastro Nacional de Estabelecimentos de Saúde). O CNES é o vértice de integração dos sistemas de informação do SUS: seus códigos alimentam SIH, SIA, SINAN, SINASC, RNDS e os demais cadastros nacionais.

O **evento gerador** deste dataset é o cadastro/atualização mensal do estabelecimento na FCES, por meio do aplicativo SCNES ou de *webservices*. A **unidade de análise é o estabelecimento de saúde em uma competência** (`CNES` + `COMPETEN`). Um mesmo CNES pode aparecer em várias competências (série histórica de sua situação cadastral) e a extração mensal funciona como um retrato da rede assistencial naquele mês. O arquivo `ST` concentra os atributos de identificação, localização, natureza jurídica, esfera administrativa, tipo de unidade, vínculo com o SUS, habilitações de gestão e capacidade física básica (instalações e leitos) do estabelecimento.

A série histórica do FTP começa em agosto de 2005 (base `200508_`). Ao longo do tempo houve incorporação de campos e mudanças de leiaute documentadas na `IT_CNES` — por exemplo a introdução do campo `NAT_JUR` (natureza jurídica padronizada) e indicadores de gestão (`GESPRG*`), da `DT_ATUA` (competência da última atualização informada pelo estabelecimento) e de blocos de requisitos de hemoterapia, radioterapia e quimioterapia nos arquivos complementares. Não há diretório preliminar: os arquivos são publicados já consolidados por competência.

Aplicações analíticas típicas: dimensionamento da rede assistencial (número de estabelecimentos por tipo, esfera e natureza jurídica), cobertura de atenção básica e de serviços especializados, distribuição territorial da oferta de leitos e equipamentos, identificação de estabelecimentos com/sem vínculo SUS, base para cálculo de cobertura de equipes de atenção básica e para vinculação de profissionais, internações (SIH) e procedimentos ambulatoriais (SIA).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/ST` | `ST` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `STSP2401.dbc` — `ST` identifica o arquivo de Estabelecimentos, `SP` a Unidade da Federação, `24` o ano e `01` o mês da competência. Também existem arquivos `STBR<AA><MM>.dbc` (consolidação nacional).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/cnes-st/<YYYY-MM>/cnes-st_<YYYYMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/cnes-st/2024-01/cnes-st_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `CNES/200508_/doc` está a Nota Técnica de layout `IT_CNES_1706.pdf` (dicionário oficial de todos os arquivos CNES); em `CNES/200508_/Auxiliar` está `TAB_CNES.zip`, pacote com as tabelas de domínio (tipos de unidade, natureza jurídica, esfera administrativa, habilitações, serviços/classificações, CBO, etc.) usadas na tabulação.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde (chave primária) |
| `CODUFMUN` | String (7) | Código do município do estabelecimento: UF + MUNIC (sem dígito verificador) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `CPF_CNPJ` | String (14) | CPF (pessoa física) ou CNPJ (pessoa jurídica) do estabelecimento |
| `PF_PJ` | String (1) | Indicador de pessoa: 1 - Física, 3 - Jurídica |
| `NIV_DEP` | String (1) | Grau de dependência: 1 - Individual, 3 - Mantida |
| `TP_UNID` | String (2) | Código do tipo de unidade/estabelecimento |
| `ESFERA_A` | String (2) | Código da esfera administrativa (federal, estadual, municipal, privada) |
| `NATUREZA` | String (2) | Código da natureza da organização |
| `NAT_JUR` | String (4) | Natureza jurídica padronizada do estabelecimento |
| `VINC_SUS` | String (1) | Vínculo com o SUS: 1 - Sim, 0 - Não |
| `TPGESTAO` | String (1) | Tipo de gestão de saúde do estabelecimento |
| `REGSAUDE` / `MICR_REG` | String (4/6) | Código da região e da microrregião de saúde (NOAS) |
| `TP_PREST` | String (2) | Tipo de prestador |
| `DT_ATUA` | String (`AAAAMM`) | Competência da última atualização informada pelo estabelecimento |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CNES` (7 dígitos), `CODUFMUN` (UF+6) e demais códigos administrativos (`TP_UNID`, `ESFERA_A`, `NATUREZA`, `NAT_JUR`, `TP_PREST`, `REGSAUDE`) devem permanecer como `String` com zeros à esquerda (`zfill`), nunca convertidos a inteiro; `COD_CEP` e `CPF_CNPJ` também são texto.
- **Datas e competências**: `COMPETEN` e `DT_ATUA` vêm como `AAAAMM` (não são convertidos automaticamente pelo saneamento, que trata apenas `AAAAMMDD`); devem ser tratados como competência textual ou convertidos manualmente para período.
- **Valores ausentes e sentinelas**: espaços em branco, `""`, `999999`, `00000000` e códigos ignorados (`9`, `99`) são convertidos para nulo por `SENTINEL_NULLS`; registros com marcador lógico de exclusão dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: a extração é um *snapshot* mensal, portanto para uma foto vigente use a competência mais recente e para séries históricas conte CNES distintos por competência; o campo `CODUFMUN` tem 7 caracteres (UF+6) mas o município é frequentemente referenciado com 6 dígitos + dígito verificador em outras bases, exigindo padronização; existe tanto arquivo por UF quanto `BR` consolidado, o que pode gerar duplicidade se ambos forem baixados; e campos de capacidade física (`QTLEITP1..3`, `QTINST*`) refletem o autocadastro do estabelecimento e exigem validação cruzada com os arquivos `LT` e `EQ`.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-st
quantilica datasus list cnes-st

# 2. Baixar microdados de cnes-st com recorte adequado à partição do dataset
# (CNES usa uf+yearmonth; --start/--end no formato YYYYMM)
quantilica datasus sync cnes-st -o ./data --start 2024-01 --end 2024-12 --regions sp rj mg

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-st -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline cnes-st -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-st/2024-01/cnes-st_202401-sp@20261015.dbc", clean=True)

# Quantidade de estabelecimentos com vínculo SUS por tipo de unidade
sus = (
    qdf.filter(pl.col("vinc_sus") == "1")
    .group_by("tp_unid")
    .agg(pl.len().alias("estabelecimentos"))
    .sort("estabelecimentos", descending=True)
)
print(sus)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/ST`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica de layout `IT_CNES_1706.pdf`** e pacote `TAB_CNES.zip` (tabelas de domínio) no FTP DATASUS
- **Portaria GM/MS nº 1.646/2015** (institui o CNES) e Portaria SAS/MS nº 511/2000 (aprova a FCES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
