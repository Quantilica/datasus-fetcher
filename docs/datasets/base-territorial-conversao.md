# `base-territorial-conversao` — Base Territorial - Conversão

O `base-territorial-conversao` contém as **tabelas de conversão** (`.cnv`) entre códigos territoriais usados pelos sistemas de informação do DATASUS e os códigos da Base Territorial. Cada arquivo `.cnv` é um mapeamento de uma UF (ou do Brasil) que permite traduzir códigos antigos/legados de município, região de saúde, macrorregião, microrregião IBGE, região metropolitana, divisão administrativa e distritos sanitários indígenas para os códigos vigentes. É ferramenta essencial para compatibilizar séries históricas com a divisão territorial atual.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `base-territorial` — Base Territorial |
| **Código no `datasus-fetcher`** | `base-territorial-conversao` |
| **Formato dos arquivos** | `.zip` (contendo arquivos `.cnv`) |
| **Particionamento** | `uf` (um ZIP por UF, além de `br` e `todos` consolidados) |
| **Periodicidade** | Versionada (atualizada conforme mudanças territoriais) |
| **Cobertura temporal no FTP** | Sem recorte temporal (versão corrente; 28 UFs/consolidados) |
| **Volume aproximado no FTP** | 28 arquivos (~21,1 MB) |
| **Arquivos preliminares** | Não |
| **Documentação oficial no FTP** | `/territorio/doc` (`bases_territoriais.pdf`, `registro_de_alteracoes.pdf`) |
| **Tabelas auxiliares no FTP** | Não aplicável |

## 1. Contexto Institucional e Epidemiológico

As tabelas de conversão fazem parte do conjunto da **Base Territorial** mantida pelo **Ministério da Saúde/DATASUS**. Elas resolvem um problema central da análise de dados em saúde: os códigos territoriais mudam ao longo do tempo (criação, fusão e desmembramento de municípios; reorganização de regiões de saúde; alterações de divisão administrativa), enquanto as bases históricas mantêm os códigos originais. Sem conversão, séries longas ficariam inconsistentes.

O **evento gerador** é a publicação, pelo DATASUS, dos arquivos de conversão atualizados conforme a Base Territorial. A **unidade de análise é a linha de conversão**, que associa um código de origem a um código de destino segundo um recorte (município, região de saúde, macrorregião etc.). O particionamento é por **UF** (arquivo `<uf>_cnv.zip`), havendo também `br_cnv.zip` e `todos_cnv.zip` consolidando o país. Cada ZIP contém variantes: sem sufixo (tabela base), `*c.cnv` (cadastro/consolidado), `*mun.cnv` (por município) e `*n.cnv` (nomes/atributos), conforme o recorte — por exemplo `sp_municip.cnv`, `sp_regsaud.cnv`, `SP_regsaudmun.cnv`, `sp_macsaudn.cnv`.

Não há recorte temporal no índice (a versão é a corrente) nem diretório preliminar. Os arquivos `.cnv` são no formato texto indexado do TabWin (semelhante a um DBF de tabela de domínio), com pares de códigos/descrições.

Aplicações analíticas típicas: compatibilizar bases de SIH/SIA/SINAN/SIM com a malha municipal vigente, remapear municípios extintos para seus sucessores, agregar produção/procedimentos aos recortes regionais atuais, apoiar estudos de série histórica municipal e converter códigos legados usados por versões antigas dos sistemas.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/territorio/conversoes` | (vazio) | `<uf>_cnv` (ex.: `sp_cnv`, `br_cnv`, `todos_cnv`) | `zip` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `sp_cnv.zip` — `sp` é a UF e `cnv` indica conversões. Contém arquivos como `sp_divadm.cnv`, `sp_municip.cnv`, `SP_macsaud.cnv`, `sp_regsaud.cnv`, `SP_regsaudmun.cnv`, `sp_regmetr.cnv`, `sp_micibge.cnv`, `sp_municgestor.cnv`. Existem também `br_cnv.zip` e `todos_cnv.zip`.
- **No armazenamento local do `datasus-fetcher`**: como o particionamento é por UF, o arquivo vai para `data/base-territorial-conversao/base-territorial-conversao_<uf>@<AAAAMMDD>.zip`, por exemplo `data/base-territorial-conversao/base-territorial-conversao_sp@20261015.zip`.
- **Documentação e Tabelas Auxiliares associadas**: `bases_territoriais.pdf` e `registro_de_alteracoes.pdf` em `/territorio/doc` explicam a estrutura das conversões e o histórico de mudanças territoriais. As conversões também são acompanhadas pelos pacotes de auxiliares dos sistemas produtores (ex.: `TAB_POP.zip`, `tab_pce.zip`, `tabresp.zip`), que repetem conversões de município/região.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Arquivo (`.cnv`) | Conteúdo | Descrição |
|---|---|---|
| `<uf>_municip.cnv` | Código e nome de município | Conversão de código antigo para município vigente |
| `<uf>_regsaud.cnv` | Código e nome de região de saúde | Mapeamento para regiões de saúde atuais |
| `SP_<uf>_macsaud.cnv` | Código de macrorregião de saúde | Mapeamento para macrorregiões |
| `<uf>_regmetr.cnv` | Código de região metropolitana | Mapeamento para regiões metropolitanas |
| `<uf>_micibge.cnv` | Código de microrregião IBGE | Mapeamento para microrregiões IBGE |
| `<uf>_divadm.cnv` | Código de divisão administrativa | Mapeamento da divisão administrativa estadual |
| `<uf>_municgestor.cnv` | Município gestor | Município responsável pela gestão de saúde da localidade |
| `<uf>_*mun.cnv` | Variante por município | Relaciona cada município aos códigos do recorte |

Os `.cnv` seguem o formato texto indexado do TabWin (tipicamente `chave;descrição`), com campos equivalentes a "código" e "nome", mas a estrutura exata varia por arquivo e por versão.

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: todos os códigos de município (6/7 dígitos), UF (2), região/macrorregião de saúde (5), microrregião (`CO_MICIBGE`, 5) e divisão administrativa (4) devem permanecer `String` com zeros à esquerda — jamais convertidos a inteiro.
- **Datas e competências**: os `.cnv` não possuem datas; a versão é implícita pela data de publicação do arquivo.
- **Valores ausentes e sentinelas**: entradas de conversão podem apontar para código inexistente/`9999...` quando não há correspondência; tratar como não mapeado.
- **Particularidades do dataset**: os `.cnv` **não são DBF** e exigem leitura própria (parser TabWin) ou conversão prévia; existem múltiplas variantes por recorte no mesmo ZIP (`*`, `*c`, `*mun`, `*n`) com significados distintos; a conversão é **muitos-para-um** (vários códigos antigos convergem para um novo município em fusões) e pode ser **um-para-muitos** em desmembramentos, exigindo definir a regra de rateio; e, por ser versionada, recomenda-se fixar a versão usada na análise.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para base-territorial-conversao
quantilica datasus list base-territorial-conversao

# 2. Baixar conversões de UFs específicas (partition uf)
quantilica datasus sync base-territorial-conversao -o ./data --regions sp rj mg

# 3. Baixar microdados acompanhados da documentação oficial
quantilica datasus sync base-territorial-conversao -o ./data --docs --regions sp

# 4. Pipeline completo: download e extração dos .cnv
quantilica datasus pipeline base-territorial-conversao -o ./data/raw --parquet-dir ./data/parquet --regions sp
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
import zipfile, io

with zipfile.ZipFile("data/raw/base-territorial-conversao/sp_cnv.zip") as z:
    raw = z.read("sp_municip.cnv").decode("latin1")

# O .cnv é um texto indexado (chave;descrição) do TabWin
linhas = [l.split(";")[:2] for l in raw.splitlines() if l.strip()]
print(pl.DataFrame(linhas, schema=["chave", "descricao"], orient="row").head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/territorio/conversoes`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Documentação `bases_territoriais.pdf` e `registro_de_alteracoes.pdf`**: `ftp://ftp.datasus.gov.br/territorio/doc`
- **IBGE — Divisão Político-Administrativa**: https://www.ibge.gov.br/geociencias/organizacao-do-territorio.html
- **TabWin — formato de conversão `.cnv`** (aplicativo oficial do DATASUS)
