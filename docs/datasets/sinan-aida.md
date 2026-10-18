# `sinan-aida` — AIDS em Adultos (SINAN)

Notificações de casos de síndrome da imunodeficiência adquirida (AIDS) em indivíduos com 13 anos ou mais, registradas no SINAN. Cada linha representa uma ficha de notificação/investigação de um caso de AIDS em adulto, segundo critérios de definição de caso do Ministério da Saúde.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-aida` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido) |
| **Particionamento** | `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2007 a 2024 (conforme `index.json`) |
| **Volume aproximado no FTP** | 18 arquivos (~18.9 MB) |
| **Arquivos preliminares** | Sim (diretório PRELIM) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A AIDS é de notificação compulsória em todo o território nacional desde a Portaria nº 542/1986, e a vigilância é coordenada pelo Departamento de HIV/Aids, Tuberculose, Hepatites Virais e Infecções Sexualmente Transmissíveis (DATHI) da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS). A notificação alimenta o SINAN, que consolida os dados de estados e municípios; os dados disponíveis no FTP do DATASUS correspondem ao SINAN Net (a partir de 2007), com fichas de adultos separadas das de crianças (`sinan-aidc`).

O evento gerador é o diagnóstico de AIDS segundo os critérios vigentes (CDC adaptado, Rio de Janeiro/Caracas ou critério de óbito), registrado na ficha de investigação do agravo; a unidade de análise é o caso notificado (um registro por ficha), não o indivíduo único, pois duplicidades entre sistemas são tratadas em rotinas de relacionamento (SINAN, SISCEL/SICLOM e SIM). Os campos cobrem identificação, residência, antecedentes e categoria de exposição, critério de definição, classificação final e evolução.

Os dados começam em 2007 no FTP, com a base nacional anual (`BR`). A notificação de infecção pelo HIV (`sinan-hiva`) tornou-se compulsória em 2013-2014, o que alterou a leitura da série: a AIDS passa a representar a fase avançada, e não mais a porta de entrada da vigilância. Os arquivos mais recentes (dir. PRELIM) são preliminares e sujeitos a revisão até o fechamento do ano.

Principais usos: taxa de detecção de AIDS por 100 mil habitantes, razão de sexos, perfil por raça/cor, escolaridade e categoria de exposição, mortalidade e letalidade (combinando com o SIM) e monitoramento de diagnóstico tardio, usados nos Boletins Epidemiológicos de HIV/Aids do MS.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `AIDA` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `AIDA` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `AIDABR24.dbc`, em que `AIDA` é o prefixo do agravo, `BR` indica a base nacional (o SINAN publica um único arquivo por ano para o Brasil) e `24` é o ano com 2 dígitos (2024).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-aida/<partição>/sinan-aida_br_2024_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`):
  - `Docs_TAB_SINAN.zip` — pacote de documentação e dicionários para tabulação (~65 MB)
  - `Nota_Tecnica_Toxoplasmose.pdf` — nota técnica sobre toxoplasmose
  - `POP_I_Acesso_a_Microdados_5.pdf` — POP I: acesso a microdados
  - `POP_II_Descompactacao_expansao_conversao_3.pdf` — POP II: descompactação, expansão e conversão (.dbc → .dbf)
  - `POP_III_Instalacao_do_tabulador_TabWin_3.pdf` — POP III: instalação do TabWin
  - `Nota_Tecnica_Intoxicacao_Exogena.pdf` — nota técnica de intoxicação exógena (agravo de outro dataset do mesmo grupo)
  - Tabelas auxiliares (`/SINAN/AUXILIAR`):
  - `TAB_SINANNET.zip` — tabelas de conversão/tabulação (.cnv, .def) do SINAN Net (~44 MB)
  - `TAB_SINANONLINE.zip` — tabelas do SINAN Online (~240 KB)
  - `POPT_Estimativa_TCU_2019_Sinan.zip` — estimativas populacionais TCU 2019 para uso no SINAN
  - O dicionário de dados desta base (`Ficha de Investigação AIDS Adulto`) está contido em `Docs_TAB_SINAN.zip`; os dicionários por agravo não são publicados como arquivos separados.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Os campos abaixo seguem o dicionário de dados do SINAN Net. A ficha é específica do agravo e os leiautes variam entre anos, portanto o conjunto exato de colunas deve ser conferido nos cabeçalhos do `.dbf` e no dicionário do ano. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `NU_NOTIFIC` | String | Número da notificação (identificador da ficha na unidade notificadora; preservar como texto). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado. |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | Inteiro | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE, 6 dígitos). |
| `ID_UNIDADE` | String | Código CNES da unidade de saúde notificadora (7 dígitos). |
| `DT_NASC` | Data (AAAAMMDD) | Data de nascimento. |
| `NU_IDADE_N` | Inteiro codificado | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `SG_UF` | String | UF de residência. |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `CLASSI_FIN` | String | Classificação final do caso (confirmado/descartado ou categoria específica do agravo). |
| `EVOLUCAO` | String | Evolução do caso (cura, óbito pelo agravo, óbito por outras causas, ignorado). |
| `DT_ENCERRA` | Data (AAAAMMDD) | Data de encerramento da investigação. |
| `CRITERIO` | String | Critério de definição de caso de AIDS (CDC adaptado, Rio de Janeiro/Caracas ou óbito). *Nome e domínio devem ser conferidos no dicionário da ficha vigente.* |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios (`ID_MUNICIP`, `ID_MN_RESI`) usam código IBGE de 6 dígitos (sem dígito verificador) e `ID_UNIDADE` é CNES de 7 dígitos; `SG_UF`/`SG_UF_NOT` são códigos IBGE de 2 dígitos. `ID_AGRAVO` (CID-10) e `NU_NOTIFIC` devem ficar como `String`, mantendo zeros à esquerda (`zfill`).
- **Datas e competências**: datas `DT_*` são gravadas em `AAAAMMDD` nos DBF e convertidas para `pl.Date`; `SEM_NOT` é semana epidemiológica `AAAASS` e permanece texto. A idade em `NU_IDADE_N` está codificada (`TNNN`) e deve ser decodificada antes de calcular faixas etárias.
- **Valores ausentes e sentinelas**: o SINAN usa `9`, `99`, `999` e `I` (ignorado) como categorias válidas no dicionário; elas **não** são nulos automáticos e a decisão de tratá-las como ausente cabe à análise. Espaços em branco e `""` viram nulos, e registros marcados como excluídos no dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: Os arquivos `AIDA` contêm apenas pessoas com 13 anos ou mais; menores de 13 anos estão em `sinan-aidc`. Os campos de exposição, critério e evolução têm códigos que variaram entre versões da ficha (2007 vs. versão atual); consultar o dicionário do ano. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (UF de notificação) ou `SG_UF`/`ID_MN_RESI` (residência) conforme a pergunta, pois os dois podem diferir. Arquivos do diretório PRELIM são preliminares e substituídos pelos finais; deduplique por `NU_NOTIFIC` + `ID_UNIDADE` + `NU_ANO` ao combinar as duas fontes.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-aida
quantilica datasus list sinan-aida

# 2. Baixar microdados de sinan-aida (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-aida -o ./data --start 2022 --end 2024 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-aida -o ./data --docs --aux --start 2022 --end 2024 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-aida -o ./data/raw --parquet-dir ./data/parquet --start 2022 --end 2024 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/AIDABR24.dbc", dataset="sinan-aida")

# Contagem de notificações por UF de notificação e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Distribuição por cs_sexo, cs_raca
print(frame.group_by("cs_sexo").agg(pl.len().alias("n")).sort("n", descending=True))
print(resumo.head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo HIV/aids: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Boletim Epidemiológico de HIV/Aids (DATHI/SVSA): https://www.gov.br/aids/pt-br/centrais-de-conteudo/boletins-epidemiologicos
- Indicadores e dados básicos de HIV/aids: http://indicadores.aids.gov.br/
