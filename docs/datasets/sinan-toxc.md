# `sinan-toxc` — Toxoplasmose Congênita (SINAN)

Notificações de toxoplasmose congênita registradas no SINAN. Cada linha representa uma ficha de notificação de um caso suspeito ou confirmado de toxoplasmose em recém-nascido ou criança com infecção adquirida na gestação.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-toxc` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido) |
| **Particionamento** | `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2019 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 8 arquivos (~1.1 MB) |
| **Arquivos preliminares** | Sim (diretório PRELIM) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A toxoplasmose gestacional e congênita foi incluída na Lista Nacional de Notificação Compulsória por ato do Ministério da Saúde em 2020 (Portaria GM/MS nº 264/2020), e a vigilância é coordenada pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS). As duas fichas são separadas: `sinan-toxg` (gestante) e `sinan-toxc` (criança).

O evento gerador é a suspeita ou o diagnóstico de infecção congênita pelo *Toxoplasma gondii*, notificado em ficha de investigação, com campos de sinais clínicos (alterações oculares, neurológicas), exames sorológicos e de imagem, tratamento e evolução. A unidade de análise é o caso notificado da criança.

O FTP traz oito arquivos nacionais anuais, de 2019 a 2026 (cerca de 1,1 MB). Como a obrigatoriedade é recente, a série ainda é curta e sujeita a subnotificação; registros de 2019 vêm de estados que já notificavam antes da portaria.

Usos: estimativa de incidência de toxoplasmose congênita por mil nascidos vivos, perfil clínico e desfecho, e avaliação da cadeia pré-natal (triagem, tratamento e acompanhamento da gestante em `sinan-toxg`).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `TOXC` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `TOXC` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `TOXCBR26.dbc`, em que `TOXC` é o prefixo do agravo, `BR` indica a base nacional (o SINAN publica um único arquivo por ano para o Brasil) e `26` é o ano com 2 dígitos (2026).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-toxc/<partição>/sinan-toxc_br_2026_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
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
  - O dicionário de dados desta base (`Ficha de Investigação Toxoplasmose Congênita; Nota_Tecnica_Toxoplasmose.pdf`) está contido em `Docs_TAB_SINAN.zip`; os dicionários por agravo não são publicados como arquivos separados.

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

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios (`ID_MUNICIP`, `ID_MN_RESI`) usam código IBGE de 6 dígitos (sem dígito verificador) e `ID_UNIDADE` é CNES de 7 dígitos; `SG_UF`/`SG_UF_NOT` são códigos IBGE de 2 dígitos. `ID_AGRAVO` (CID-10) e `NU_NOTIFIC` devem ficar como `String`, mantendo zeros à esquerda (`zfill`).
- **Datas e competências**: datas `DT_*` são gravadas em `AAAAMMDD` nos DBF e convertidas para `pl.Date`; `SEM_NOT` é semana epidemiológica `AAAASS` e permanece texto. A idade em `NU_IDADE_N` está codificada (`TNNN`) e deve ser decodificada antes de calcular faixas etárias.
- **Valores ausentes e sentinelas**: o SINAN usa `9`, `99`, `999` e `I` (ignorado) como categorias válidas no dicionário; elas **não** são nulos automáticos e a decisão de tratá-las como ausente cabe à análise. Espaços em branco e `""` viram nulos, e registros marcados como excluídos no dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: Série curta e dados do ano corrente (2026) preliminares. Cruzar com `sinan-toxg` por UF/ano, e não por identificador de pessoa, pois não há vinculação mãe-filho pública. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (UF de notificação) ou `SG_UF`/`ID_MN_RESI` (residência) conforme a pergunta, pois os dois podem diferir. Arquivos do diretório PRELIM são preliminares e substituídos pelos finais; deduplique por `NU_NOTIFIC` + `ID_UNIDADE` + `NU_ANO` ao combinar as duas fontes.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-toxc
quantilica datasus list sinan-toxc

# 2. Baixar microdados de sinan-toxc (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-toxc -o ./data --start 2024 --end 2026 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-toxc -o ./data --docs --aux --start 2024 --end 2026 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-toxc -o ./data/raw --parquet-dir ./data/parquet --start 2024 --end 2026 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/TOXCBR26.dbc", dataset="sinan-toxc")

# Contagem de notificações por UF de notificação e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Distribuição por cs_raca, nu_ano
print(frame.group_by("cs_raca").agg(pl.len().alias("n")).sort("n", descending=True))
print(resumo.head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Nota Técnica de Toxoplasmose (DATASUS/SINAN): ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DOCS/Nota_Tecnica_Toxoplasmose.pdf
- Guia de Vigilância em Saúde (SVSA/MS): https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
