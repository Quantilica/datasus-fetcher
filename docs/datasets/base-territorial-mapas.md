# `base-territorial-mapas` — Base Territorial - Mapas

O `base-territorial-mapas` contém os **mapas digitais em formato TabWin (`.MAP`)** da divisão territorial brasileira, usados para a representação cartográfica dos dados de saúde. Cada ZIP reúne, para uma UF (ou o Brasil) e um ano de referência, um conjunto de arquivos `.MAP` correspondentes aos recortes territoriais — município, região de saúde, macrorregião de saúde, microrregião IBGE, região metropolitana e divisão administrativa. É a base cartográfica que permite gerar mapas temáticos (por município ou região) no TabWin e em apps compatíveis.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `base-territorial` — Base Territorial |
| **Código no `datasus-fetcher`** | `base-territorial-mapas` |
| **Formato dos arquivos** | `.zip` (contendo arquivos `.MAP` do TabWin) |
| **Particionamento** | `uf`, `year` (um ZIP por UF e ano de referência) |
| **Periodicidade** | Anual / versionada (malhas de 1991, 1994, 1997, 2001, 2005, 2013 e 2025) |
| **Cobertura temporal no FTP** | 1991 a 2025 (conforme `index.json`) |
| **Volume aproximado no FTP** | 111 arquivos (~143 MB, 28 UFs/consolidados) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/territorio/doc` (`bases_territoriais.pdf`, `registro_de_alteracoes.pdf`) |
| **Tabelas auxiliares no FTP** | Não aplicável |

## 1. Contexto Institucional e Epidemiológico

Os mapas integram a **Base Territorial** mantida pelo **Ministério da Saúde/DATASUS** e servem de suporte cartográfico à análise e à disseminação dos dados de saúde. São a versão geográfica dos recortes territoriais: permitem que sistemas como o TabWin associem códigos de município/região a polígonos, viabilizando mapas de taxas, coberturas e indicadores.

O **evento gerador** é a atualização das malhas territoriais quando há mudanças na divisão político-administrativa (Censos, contagens e revisões da malha municipal do IBGE; criação/desmembramento de municípios; redefinição de regiões de saúde). A **unidade de análise é o conjunto de arquivos `.MAP` de uma UF em um ano**. Os anos disponíveis correspondem a marcos da malha do IBGE: **1991, 1994, 1997, 2001, 2005, 2013 e 2025** (algumas UFs não têm todos os anos). Cada ZIP contém arquivos como `<uf>_municip.MAP`, `<uf>_regsaud.MAP`, `<uf>_macsaud.MAP`, `<uf>_micibge.MAP`, `<uf>_regmetr.MAP` e `<uf>_divadm.MAP`.

Não há diretório preliminar. Os arquivos `.MAP` são binários proprietários do TabWin e exigem esse aplicativo (ou conversão) para uso; o DATASUS também disponibiliza os shapes equivalentes em outros portais.

Aplicações analíticas típicas: geração de mapas temáticos de indicadores de saúde no TabWin, análise espacial da distribuição de doenças e da oferta de serviços, apoio à regionalização e à vigilância em saúde e produção de mapas para relatórios e boletins.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/territorio/mapas` | (vazio) | `<uf>_mapas_<AAAA>` (ex.: `es_mapas_2025`, `br_mapas_2013`) | `zip` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `es_mapas_2025.zip` — `es` é a UF, `mapas` o assunto e `2025` o ano de referência da malha. Contém `es_regsaud.MAP`, `es_divadm.MAP`, `es_macsaud.MAP`, `es_micibge.MAP`, `es_municip.MAP` e `es_regmetr.MAP`. Há também arquivos `br_mapas_<ano>.zip` (malha nacional de 1991 a 2025) e códigos de UF/"mrco"/"mrne" para malhas regionais.
- **No armazenamento local do `datasus-fetcher`**: `data/base-territorial-mapas/2025/base-territorial-mapas_2025-es@20260918.zip`.
- **Documentação e Tabelas Auxiliares associadas**: `bases_territoriais.pdf` e `registro_de_alteracoes.pdf` em `/territorio/doc`; para converter/visualizar os `.MAP`, é necessário o aplicativo **TabWin** do DATASUS.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Os arquivos `.MAP` **não são tabelas** com colunas/variáveis como um DBF; são estruturas binárias de polígonos indexados por código geográfico. Os "atributos" relevantes são os **códigos territoriais de ligação** usados para casar o mapa com as tabelas:

| Arquivo (`.MAP`) | Chave de ligação | Descrição |
|---|---|---|
| `<uf>_municip.MAP` | Código de município | Polígonos dos municípios da UF |
| `<uf>_regsaud.MAP` | Código de região de saúde | Polígonos das regiões de saúde |
| `<uf>_macsaud.MAP` | Código de macrorregião de saúde | Polígonos das macrorregiões |
| `<uf>_micibge.MAP` | Código de microrregião IBGE | Polígonos das microrregiões |
| `<uf>_regmetr.MAP` | Código de região metropolitana | Polígonos das regiões metropolitanas |
| `<uf>_divadm.MAP` | Código de divisão administrativa | Polígonos da divisão administrativa estadual |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: como os `.MAP` se ligam a código de município/UF/região, os códigos usados nas tabelas de dados (6/7 dígitos para município, 2 para UF, 5 para região de saúde) devem permanecer `String` com zeros à esquerda para que o casamento mapa↔dado funcione.
- **Datas e competências**: o "ano" da malha está no nome do arquivo (não é uma coluna interna), refletindo o ano da divisão territorial usada.
- **Valores ausentes e sentinelas**: não aplicável a dados tabulares; eventuais divergências de malha entre anos devem ser resolvidas escolhendo a malha compatível com a data dos dados.
- **Particularidades do dataset**: `.MAP` é formato binário proprietário — sem o TabWin (ou uma rotina de conversão) não é legível; a malha muda de ano para ano (municípios criados/extintos alteram os polígonos), portanto o mapa deve ser compatível com a versão dos dados; algumas UFs não possuem todos os anos; e há malhas nacionais (`br_mapas_*`) e regionais (`mrco`, `mrne`) para análises agregadas.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para base-territorial-mapas
quantilica datasus list base-territorial-mapas

# 2. Baixar mapas de UFs e anos específicos (partition uf+year)
quantilica datasus sync base-territorial-mapas -o ./data --start 2025 --end 2025 --regions es sp

# 3. Baixar microdados acompanhados da documentação oficial
quantilica datasus sync base-territorial-mapas -o ./data --docs --start 2025 --end 2025

# 4. Pipeline completo: download e extração dos .MAP
quantilica datasus pipeline base-territorial-mapas -o ./data/raw --parquet-dir ./data/parquet --start 2025 --end 2025
```

### Em Python e Polars

```python
import zipfile
import polars as pl

# Lista os arquivos .MAP disponíveis sem extrair
with zipfile.ZipFile("data/raw/base-territorial-mapas/2025/es_mapas_2025.zip") as z:
    print(pl.Series("mapas", [n for n in z.namelist() if n.upper().endswith(".MAP")]))
# A visualização/análise espacial é feita no TabWin do DATASUS (formato binário proprietário).
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/territorio/mapas`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **TabWin/DATASUS** (aplicativo que lê os arquivos `.MAP`)
- **Documentação `bases_territoriais.pdf` e `registro_de_alteracoes.pdf`**: `ftp://ftp.datasus.gov.br/territorio/doc`
- **IBGE — Malhas territoriais**: https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais.html
