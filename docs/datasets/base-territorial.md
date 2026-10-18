# `base-territorial` — Base Territorial

O `base-territorial` contém as **tabelas territoriais de referência** do DATASUS, que descrevem a divisão político-administrativa e sanitária do Brasil: unidades da federação, municípios, regiões e microrregiões de saúde, macrorregiões, regiões metropolitanas, distritos sanitários, territórios da cidadania e a relação entre municípios e cada um desses recortes. Cada registro (linha) é uma entidade territorial ou um vínculo município–recorte, em uma **versão mensal** do cadastro. É a base de apoio para padronizar e cruzar códigos territoriais usados em todos os sistemas de informação do SUS.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `base-territorial` — Base Territorial |
| **Código no `datasus-fetcher`** | `base-territorial` |
| **Formato dos arquivos** | `.zip` (contendo tabelas `.dbf`, `.csv`, `.xml` e `.txt` de layout) |
| **Particionamento** | `version` (versão mensal, ex.: `2026-06`) |
| **Periodicidade** | Mensal (versionada por competência) |
| **Cobertura temporal no FTP** | Versões mensais; versão mais recente `2026-06` (conforme `index.json`) |
| **Volume aproximado no FTP** | 21 arquivos versionados (~33 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/territorio/doc` (`bases_territoriais.pdf`, `registro_de_alteracoes.pdf`) |
| **Tabelas auxiliares no FTP** | Não aplicável |

## 1. Contexto Institucional e Epidemiológico

A Base Territorial é mantida pelo **Ministério da Saúde/DATASUS** e consolida, em um formato único e versionado, a divisão territorial usada pelos sistemas de informação em saúde. Ela reúne tabelas de **domínio territorial** (`tb_*`), como `tb_uf`, `tb_municip`, `tb_regiao`, `tb_regsaud`, `tb_macsaud`, `tb_regmetr`, `tb_micibge`, `tb_divadm`, `tb_pndr`, `tb_dsei` e `tb_terrcid`, e tabelas de **relacionamento** (`rl_*`) que associam cada município aos recortes aos quais pertence.

O **evento gerador** é a atualização periódica (mensal) do cadastro territorial quando há criação, extinção ou alteração de municípios e mudanças nos recortes de saúde (regiões/macrorregiões de saúde, regiões metropolitanas, PNDR, territórios da cidadania). A **unidade de análise varia conforme a tabela**: para `tb_*`, é uma entidade territorial (ex.: um município em `tb_municip`); para `rl_*`, é um vínculo (ex.: a associação `CO_MUNICIP` → `CO_REGSAUD`). A competência mês/ano aparece no nome do arquivo e nos metadados da versão.

A série é **versionada por competência** (não é uma série histórica de dados, e sim sucessivas versões do cadastro). As versões são organizadas por ano em `/territorio/tabelas/<ano>/`, com o nome `MM-base_territorial_<mês><AA>.zip`. O documento `registro_de_alteracoes.pdf` registra as mudanças entre versões. Não há diretório preliminar.

Aplicações analíticas típicas: padronização de códigos de município (6 e 7 dígitos) e de UF, enriquecimento de bases de saúde com atributos territoriais (capital, Amazônia Legal, semiárido, faixa de fronteira, município de extrema pobreza), mapeamento de municípios para regiões de saúde e macrorregiões, e construção de agregações regionais para indicadores.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/territorio/tabelas` | (vazio) | `<MM>-base_territorial_<mês><AA>.zip` (por versão mensal) | `zip` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `06-base_territorial_jun26.zip` (em `/territorio/tabelas/2026/`) — `06` é o mês, `base_territorial` o assunto, `jun26` o mês abreviado e ano. Dentro do ZIP há os arquivos `tb_*.dbf/csv/xml/txt` e `rl_*.dbf/csv/xml/txt` e os respectivos `*_layout.txt` (definição de colunas).
- **No armazenamento local do `datasus-fetcher`**: como o particionamento é por versão, o arquivo vai para `data/base-territorial/base-territorial_<versão>@<AAAAMMDD>.zip`, por exemplo `data/base-territorial/base-territorial_2026-06@20260624.zip`.
- **Documentação e Tabelas Auxiliares associadas**: em `/territorio/doc` estão `bases_territoriais.pdf` (descrição das tabelas e relacionamentos) e `registro_de_alteracoes.pdf` (histórico de mudanças). Não há pacote de auxiliares separado — as tabelas territoriais são o próprio conteúdo do ZIP.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Tabela (DBF) | Coluna | Tipo / Formato | Descrição |
|---|---|---|---|
| `tb_municip` | `CO_MUNICIP` | String (6) | Código IBGE do município (sem dígito verificador) |
| `tb_municip` | `CO_MUNICDV` | String (7) | Código IBGE do município (com dígito verificador) |
| `tb_municip` | `CO_UF` / `CO_REGIAO` | String (2/1) | UF e macrorregião do município |
| `tb_municip` | `IN_CAPITAL` / `IN_AMAZLEG` / `IN_SEMIAR` | String (1) | Indicadores: capital, Amazônia Legal, semiárido |
| `tb_municip` | `NU_LATITUD` / `NU_LONGIT` / `NU_AREA` | Float | Latitude, longitude, altitude e área do município |
| `tb_uf` | `CO_UF` / `DS_SIGLA` / `DS_NOME` | String | Código, sigla e nome da UF |
| `tb_regsaud` / `tb_macsaud` | `CO_REGSAUD` / `CO_MACSAUD`, `DS_NOME` | String | Região e macrorregião de saúde |
| `rl_municip_regsaud` | `CO_MUNICIP`, `CO_REGSAUD` | String | Relacionamento município → região de saúde |
| `rl_municip_macsaud` | `CO_MUNICIP`, `CO_MACSAUD` | String | Relacionamento município → macrorregião de saúde |
| `rl_municip_divadm` | `CO_MUNICIP`, `CO_DIVADM` | String | Relacionamento município → divisão administrativa estadual |
| `tb_divadm` / `tb_dsei` | `CO_DIVADM` / `CO_DSEI`, `DS_NOME` | String | Divisão administrativa estadual / distrito sanitário especial indígena |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `CO_MUNICIP` (6), `CO_MUNICDV` (7), `CO_UF` (2), `CO_REGSAUD`/`CO_MACSAUD`/`CO_REGMETR`/`CO_MICIBGE` (5) e `CO_DIVADM`/`CO_PNDR`/`CO_DSEI`/`CO_TERRCID` (3/4) devem permanecer `String` com zeros à esquerda.
- **Datas e competências**: as datas de instalação/extinção (`DT_INSTAL`, `DT_EXTIN`) são `AAAAMM`; não há datas `AAAAMMDD` convertidas pela rotina padrão.
- **Valores ausentes e sentinelas**: os ZIPs contêm tabelas já normalizadas; campos como `NU_LATITUD`/`NU_LONGIT` podem vir vazios ou `0000000000`, exigindo tratamento.
- **Particularidades do dataset**: como a base é **versionada**, é preciso escolher uma versão de referência e mantê-la fixa ao longo de uma análise (misturar versões gera inconsistências); as tabelas são entregues em quatro formatos (`dbf`, `csv`, `xml`, `txt`), dos quais o `csv` com separador `;` é o mais simples de ler sem dependências; `IN_*` são flags `1/0`; e o relacionamento `CO_MUNICIP`→recortes muda entre versões quando há reorganização regional.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar versões disponíveis da Base Territorial
quantilica datasus list base-territorial

# 2. Baixar microdados (partition version; selecione a versão desejada)
quantilica datasus sync base-territorial -o ./data --start 2026-01 --end 2026-06

# 3. Baixar microdados acompanhados da documentação oficial
quantilica datasus sync base-territorial -o ./data --docs

# 4. Pipeline completo: download, extração do .zip e conversão das tabelas para Parquet
quantilica datasus pipeline base-territorial -o ./data/raw --parquet-dir ./data/parquet
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

munic = pl.read_csv("data/raw/base-territorial/base-territorial_2026-06/tb_municip.csv",
                    separator=";", infer_schema_length=0)

# Municípios por UF com indicador de capital
resumo = (
    municip.group_by("CO_UF")
    .agg([
        pl.len().alias("municipios"),
        pl.col("IN_CAPITAL").filter(pl.col("IN_CAPITAL") == "1").len().alias("capitais"),
    ])
)
print(resumo)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/territorio/tabelas`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Documentação `bases_territoriais.pdf` e `registro_de_alteracoes.pdf`**: `ftp://ftp.datasus.gov.br/territorio/doc`
- **IBGE — Divisão Político-Administrativa e malha territorial**: https://www.ibge.gov.br/geociencias/organizacao-do-territorio.html
- **PCDaS/Fiocruz — Bases territoriais**: https://pcdas.icict.fiocruz.br/
