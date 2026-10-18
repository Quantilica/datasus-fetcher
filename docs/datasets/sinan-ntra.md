# `sinan-ntra` — Notificação Individual de Tracoma (SINAN)

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

Os campos abaixo seguem o dicionário de dados do SINAN Net. A ficha é específica do agravo e os leiautes variam entre anos, portanto o conjunto exato de colunas deve ser conferido nos cabeçalhos do `.dbf` e no dicionário do ano. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `NU_NOTIFIC` | String | Número da notificação (identificador da ficha na unidade notificadora; preservar como texto). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado (A71; formas oculares em H13.1). |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `DT_SIN_PRI` | Data (AAAAMMDD) | Data dos primeiros sintomas. |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | Inteiro | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE, 6 dígitos). |
| `ID_UNIDADE` | String | Código CNES da unidade de saúde notificadora (7 dígitos). |
| `DT_NASC` | Data (AAAAMMDD) | Data de nascimento. |
| `NU_IDADE_N` | Inteiro codificado | Idade no formato `TNNN` (unidade = hora/dia/mês/ano + 3 dígitos). |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `ZONA` | String | Zona de residência (1 urbana, 2 rural, 3 periurbana, 9 ignorado). |
| `FORMA_CLIN` | String | Forma clínica (TF folicular, TI inflamatório intenso, TS cicatricial, TT trichiasis, CO opacificação da córnea). *Nome a conferir no dicionário.* |
| `EXAME_LAB` | String | Resultado de exame laboratorial (1 positivo, 2 negativo, 3 não realizado, 9 ignorado). *Nome a conferir no dicionário.* |
| `TRATAMENTO` | String | Tratamento realizado (1 sim, 2 não, 9 ignorado). |
| `CIRURGIA` | String | Encaminhamento para cirurgia (TT/CO) (1 sim, 2 não, 9 ignorado). |
| `CLASSI_FIN` | String | Classificação final (1 confirmado, 2 descartado, 9 ignorado). |
| `EVOLUCAO` | String | Evolução do caso (cura, melhora, óbito, ignorado). *Nome a conferir no dicionário.* |
| `DT_ENCERRA` | Data (AAAAMMDD) | Data de encerramento da investigação. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios (`ID_MUNICIP`, `ID_MN_RESI`) usam código IBGE de 6 dígitos; `ID_UNIDADE` é CNES de 7 dígitos; `SG_UF_NOT` é código IBGE de 2 dígitos. `ID_AGRAVO` (CID-10) e `NU_NOTIFIC` devem ficar como `String`, mantendo zeros à esquerda (`zfill`).
- **Datas e competências**: datas `DT_*` são gravadas em `AAAAMMDD` nos DBF e convertidas para `pl.Date`; `SEM_NOT` é semana epidemiológica `AAAASS` e permanece texto. A idade em `NU_IDADE_N` está codificada (`TNNN`) e deve ser decodificada antes de calcular faixas etárias.
- **Valores ausentes e sentinelas**: o SINAN usa `9`, `99`, `999` e `I` (ignorado) como categorias válidas; elas **não** são nulos automáticos. Espaços em branco e `""` viram nulos, e registros marcados como excluídos no dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: este dataset contém a **notificação individual** de casos; o **inquérito** populacional de tracoma (busca ativa) está no dataset separado `sinan-trac`. O tracoma é frequentemente investigado em inquéritos escolares e domiciliares, o que gera diferenças nos denominadores. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. Arquivos do diretório PRELIM (2025+) são preliminares; deduplique por `NU_NOTIFIC` + `ID_UNIDADE` + `NU_ANO` ao combinar as fontes.

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
