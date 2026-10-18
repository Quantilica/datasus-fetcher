# `sinan-hiva` — HIV em adultos

Notificações de infecção pelo HIV em indivíduos com 13 anos ou mais, registradas no SINAN. Cada linha representa uma ficha de notificação/investigação de infecção pelo HIV em adulto, independentemente da presença de AIDS.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-hiva` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido) |
| **Particionamento** | `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2007 a 2024 (conforme `index.json`) |
| **Volume aproximado no FTP** | 18 arquivos (~17,6 MB) |
| **Arquivos preliminares** | Sim (diretório PRELIM) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A infecção pelo HIV em adultos, gestantes e crianças expostas passou a ser de notificação compulsória em 2013-2014 (Portaria SVS/MS nº 29/2013), consolidada depois na Portaria de Consolidação GM/MS nº 4/2017 e na lista nacional vigente. A vigilância é conduzida pelo DATHI/SVSA e permite identificar a infecção antes do estágio de AIDS.

O evento gerador é o diagnóstico laboratorial de infecção pelo HIV, notificado em ficha de investigação própria no SINAN. A unidade de análise é a notificação do caso, e os campos incluem dados sociodemográficos, categoria de exposição, resultado de exames, classificação e encerramento. Notificações de gestantes (`sinan-hivg`), crianças expostas (`sinan-hive`) e crianças infectadas (`sinan-hivc`) têm bases separadas.

O arquivo no FTP cobre 2007 a 2024, mas a notificação nacional efetiva só se consolida a partir de 2014. Os anos anteriores trazem registros esparsos, vindos de estados que notificavam antes da obrigatoriedade, e não podem ser lidos como série de incidência.

Usos: taxa de detecção de HIV, perfil sociodemográfico e de exposição, diagnóstico tardio, linkagem com sistemas laboratoriais (SISCEL) e de medicamentos (SICLOM) e planejamento da resposta ao HIV.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `HIVA` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `HIVA` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `HIVABR24.dbc`, em que `HIVA` é o prefixo do agravo, `BR` indica a base nacional (o SINAN publica um único arquivo por ano para o Brasil) e `24` é o ano com 2 dígitos (2024).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-hiva/<partição>/sinan-hiva_br_2024_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
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
  - O dicionário de dados desta base (`Ficha de Investigação HIV Adulto`) está contido em `Docs_TAB_SINAN.zip`; os dicionários por agravo não são publicados como arquivos separados.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo real `HIVABR24.dbc` do FTP (campos da ficha do SINAN Net; o leiaute pode variar entre anos). Os microdados públicos não trazem número de notificação nem data de nascimento completa, apenas campos não identificáveis. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (individual ou negativa). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado. |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `NU_ANO` | Inteiro | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE). |
| `ID_REGIONA` | String | Regional de saúde de notificação. |
| `DT_DIAG` | Data (AAAAMMDD) | Data do diagnóstico. |
| `SEM_DIAG` | String | Semana epidemiológica do diagnóstico (AAAASS). |
| `NU_IDADE_N` | Inteiro codificado | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_GESTANT` | String | Gestante (trimestre de gestação ou não gestante, conforme a ficha). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade (código da ficha do SINAN). |
| `SG_UF` | String | UF de residência. |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `ID_RG_RESI` | String | Regional de saúde de residência. |
| `ID_PAIS` | String | País de residência. |
| `ID_OCUPA_N` | String | Ocupação (CBO, 6 dígitos). |
| `ANT_TRASMI` | String | Antecedente epidemiológico: categoria de transmissão informada. |
| `ANT_DROGA` | String | Antecedente de uso de drogas injetáveis. |
| `ANTTRANS_M` | String | Antecedente de transmissão: transfusão/hemoderivados. |
| `ANT_ACIDEN` | String | Antecedente de acidente com material biológico. |
| `LAB_TRIAGE` | String | Realização de teste de triagem laboratorial. |
| `DTTRIAGEM` | Data (AAAAMMDD) | Data do teste de triagem. |
| `LAB_CONFIR` | String | Realização de teste confirmatório. |
| `DT_CONFIRM` | Data (AAAAMMDD) | Data do teste confirmatório. |
| `TPRAPIDO1` | String | Resultado do 1º teste rápido. |
| `ANT_TUBERC` | String | Sinal/sintoma ou doença indicativa: tuberculose. |
| `DEF_DIAGNO` | String | Doença definidora diagnosticada. |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito. |
| `CRITERIO` | String | Critério de definição de caso (código de 3 caracteres). |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios (`ID_MUNICIP`, `ID_MN_RESI`) usam código IBGE de 6 dígitos (sem dígito verificador); `SG_UF`/`SG_UF_NOT` são códigos IBGE de 2 dígitos. `ID_AGRAVO` (CID-10) deve ficar como `String`, mantendo zeros à esquerda (`zfill`).
- **Datas e competências**: datas `DT_*` são gravadas em `AAAAMMDD` nos DBF e convertidas para `pl.Date`; `SEM_NOT` é semana epidemiológica `AAAASS` e permanece texto. A idade em `NU_IDADE_N` está codificada (`TNNN`) e deve ser decodificada antes de calcular faixas etárias.
- **Valores ausentes e sentinelas**: o SINAN usa `9`, `99`, `999` e `I` (ignorado) como categorias válidas no dicionário; elas **não** são nulos automáticos e a decisão de tratá-las como ausente cabe à análise. Espaços em branco e `""` viram nulos, e registros marcados como excluídos no dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: Registros anteriores a 2014 não representam a incidência real, pois a notificação ainda não era obrigatória. Pessoas menores de 13 anos estão em `sinan-hivc`; gestantes vivendo com HIV em `sinan-hivg`. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (UF de notificação) ou `SG_UF`/`ID_MN_RESI` (residência) conforme a pergunta, pois os dois podem diferir. Arquivos do diretório PRELIM são preliminares e substituídos pelos finais; prefira sempre os arquivos finais quando o mesmo ano existir nas duas fontes, evitando somar PRELIM e FINAIS.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-hiva
quantilica datasus list sinan-hiva

# 2. Baixar microdados de sinan-hiva (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-hiva -o ./data --start 2022 --end 2024 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-hiva -o ./data --docs --aux --start 2022 --end 2024 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-hiva -o ./data/raw --parquet-dir ./data/parquet --start 2022 --end 2024 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/HIVABR24.dbc", dataset="sinan-hiva")

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
- Guia de Vigilância em Saúde (SVSA/MS): https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Boletim Epidemiológico de HIV/Aids: https://www.gov.br/aids/pt-br/centrais-de-conteudo/boletins-epidemiologicos
- Indicadores e dados básicos de HIV/aids: http://indicadores.aids.gov.br/
