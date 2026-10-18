# `sinan-ntra` — Notificação de Tracoma

Notificações individuais de casos de tracoma, de notificação compulsória no SINAN. Cada linha representa uma ficha de notificação/investigação de um caso de tracoma (conjuntivite e ceratoconjuntivite por *Chlamydia trachomatis*), atendido em serviços de saúde.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-ntra` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido) |
| **Particionamento** | `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2010 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 17 arquivos (~768 KB) |
| **Arquivos preliminares** | Sim (diretório PRELIM, 2025–2026; Finais até 2024) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

O tracoma é uma doença ocular inflamatória crônica causada pela bactéria *Chlamydia trachomatis*, classificada pela OMS como doença tropical negligenciada (DTN) e incluída entre as metas de eliminação como problema de saúde pública até 2030. No Brasil, é agravo de notificação compulsória conforme a Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023) e integra o Programa de Vigilância e Controle do Tracoma da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS).

O evento gerador é todo caso suspeito ou confirmado de tracoma, tipicamente em populações de baixa renda, áreas rurais, periferias urbanas e comunidades ribeirinhas, associado a condições precárias de saneamento, aglomeração e higiene. O diagnóstico é clínico-oftalmológico (classificação OMS: TF, TI, TS, TT, CO) e pode ser confirmado por exame laboratorial. A unidade de análise é o caso notificado (um registro por ficha).

O instrumento é a *Ficha de Notificação/Investigação Individual — Tracoma*, que registra a forma clínica (tracoma folicular TF, inflamatório intenso TI, cicatricial TS, trichiasis tracomatoso TT, opacificação da córnea CO), dados de exames, tratamento realizado e encaminhamento para cirurgia (quando indicado) e investigação de comunicantes. A série no FTP inicia em 2010; os dados de 2025 e 2026 estão em PRELIM e sujeitos a revisão.

Principais usos: vigilância da forma e distribuição do tracoma, monitoramento de indicadores de eliminação (prevalência de TF em crianças de 1 a 9 anos), avaliação de campanhas de tratamento em massa com azitromicina e embasamento de ações de saneamento e educação em saúde.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `NTRA` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `NTRA` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `NTRABR24.dbc`, em que `NTRA` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-ntra/<partição>/sinan-ntra_br_2010_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`Notificação Individual de Tracoma`) é distribuído no Portal SINAN; não há PDF por agravo no FTP.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

As colunas abaixo foram extraídas do cabeçalho do arquivo mais recente (`NTRABR26.dbc`). Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação do inquérito. |
| `NU_ANO` | String | Ano da notificação. |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado (A71). |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE, 7 dígitos). |
| `ID_UNIDADE` | String | Código CNES da unidade notificadora (7 dígitos). |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `ID_REGIONA` | String | Código da regional de saúde. |
| `CS_INQUERI` | String | Tipo de inquérito realizado. |
| `NU_CASOEXA` | Inteiro | Número de casos examinados. |
| `NU_CASOPOS` | Inteiro | Número de casos positivos. |
| `DT_DIGITA` | Data (AAAAMMDD) | Data de digitação do registro. |
| `DT_TRANSUS` / `DT_TRANSDM` / `DT_TRANSSM` / `DT_TRANSRM` / `DT_TRANSRS` / `DT_TRANSSE` | Data (AAAAMMDD) | Datas de transferência do registro entre as esferas do SINAN (US, distrital/municipal, estadual/regional, federal). |
| `NU_LOTE_V` / `NU_LOTE_H` | String | Números dos lotes de transferência vertical e horizontal. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: o município (`ID_MUNICIP`) usa código IBGE de 7 dígitos; `ID_UNIDADE` é CNES de 7 dígitos; `SG_UF_NOT` é código IBGE de 2 dígitos. `ID_AGRAVO` (CID-10) deve ficar como `String`, mantendo zeros à esquerda (`zfill`).
- **Datas e competências**: datas `DT_*` são gravadas em `AAAAMMDD` nos DBF e convertidas para `pl.Date`; `SEM_NOT` é semana epidemiológica `AAAASS` e permanece texto. 
- **Valores ausentes e sentinelas**: o SINAN usa `9`, `99`, `999` e `I` (ignorado) como categorias válidas; elas **não** são nulos automáticos. Espaços em branco e `""` viram nulos, e registros marcados como excluídos no dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: o layout é compacto e traz contagens por notificação de inquérito (`NU_CASOEXA` examinados, `NU_CASOPOS` positivos), sem dados individuais de pacientes; o detalhamento por forma clínica está no dataset `sinan-trac`. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT`. Arquivos do diretório PRELIM são preliminares; deduplique ao combinar as fontes.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-ntra
quantilica datasus list sinan-ntra

# 2. Baixar microdados de sinan-ntra (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-ntra -o ./data --start 2015 --end 2022 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-ntra -o ./data --docs --aux --start 2015 --end 2022 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-ntra -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2022 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/NTRABR22.dbc", dataset="sinan-ntra")

# Notificações por UF e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Formas clínicas e zona de residência
print(frame.group_by("forma_clin").agg(pl.len().alias("n")).sort("n", descending=True))
print(frame.group_by("zona").agg(pl.len().alias("n")).sort("n", descending=True))
print(resumo.head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (Notificação Individual de Tracoma): https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Tracoma: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- OMS — Eliminação do tracoma como problema de saúde pública (metas 2030): https://www.who.int/health-topics/trachoma
