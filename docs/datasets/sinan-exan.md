# `sinan-exan` — Doenças exantemáticas

O `sinan-exan` contém os microdados das notificações e investigações epidemiológicas de casos suspeitos de doenças exantemáticas (sarampo, CID-10 B05, e rubéola, CID-10 B06) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de sarampo ou rubéola, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. Com 108 colunas no leiaute da ficha v5.0 (revisão março/2012), a ficha unificada cobre o quadro clínico (febre, exantema, tosse, coriza, conjuntivite, artralgia, linfadenopatia retroauricular), o histórico vacinal, o esquema de bloqueio vacinal e as coletas seriadas de sorologias (IgM/IgG em amostras 1 e 2 e repetição), sustentando os programas de eliminação do sarampo e da vigilância da síndrome da rubéola congênita (SRC).

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-exan` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2007 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 20 arquivos (~15,3 MB) |
| **Arquivos preliminares** | Sim — todos os arquivos estão em `PRELIM`; `meta.py` também consulta `FINAIS`, que hoje não contém arquivos do agravo |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

Sarampo e rubéola são agravos de notificação compulsória universal (Lei nº 6.259/1975 e Decreto nº 78.231/1976, hoje na Portaria GM/MS nº 204/2016), monitorados pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) por meio da vigilância de doenças exantemáticas — instrumento central dos programas de eliminação do sarampo e da vigilância da síndrome da rubéola congênita (SRC), com suporte dos laboratórios de referência (Fiocruz/RJ e Adolfo Lutz). Toda pessoa com febre + exantema + tosse/coriza/conjuntivite deve ser notificada e investigada dentro de 48 horas, com bloqueio vacinal dos contatos e coletas laboratoriais, para que o Brasil demonstre manutenção da eliminação do sarampo certificada — a base detecta casos importados, cadenas de transmissão endêmica e surtos.

O evento gerador deste dataset é a **Ficha de Notificação Individual das Doenças Exantemáticas** (sarampo/rubéola; ficha v5.0). A notificação nasce com a suspeição clínica (febre + exantema maculopapular + tosse, coriza ou conjuntivite) e é completada com o contato com caso suspeito até 23 dias antes (`CS_FONTE`), o bloqueio vacinal (`CS_VACINAL`), as coletas de amostras ('1ª e 2ª sorologias: `DT_COL_1`, `DT_COL_2`, resultantes `ID_S1_IGM/ID_S1_IGG`, `ID_S2_*`, repetição `ID_RE_*`) e, quando encerrado, a etiologia final (sarampo/rubéola/descartado). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. A base é publicada em consolidações revisadas periodicamente — todas estão em `PRELIM`. O instrumento unificou as fichas antigas de sarampo e rubéola em uma única ficha de doenças exantemáticas, no contexto da eliminação formal da rubéola nas Américas (2009) e da manutenção do certificado de eliminação do sarampo — a base é essencial para detectar casos importados e surtos de sarampo, como as grandes ondas registradas em 2018 e posteriormente.

Aplicações analíticas típicas: monitoramento de casos suspeitos e confirmados de sarampo por classificação (`CLASSI_FIN` 1/2 vs descartados), percentual de casos com IgM reagente (`ID_S1_IGM`), cumprimento do prazo de investigação em 48 horas (diferença entre `DT_NOTIFIC` e `DT_INVEST`) e realização de bloqueio vacinal dos contos dientes (`CS_VACINAL`); vigilância da rubéola de mulheres em idade fértil e das SRC gestantes pelo árvore de investigação do grupo de casos compatíveis; e análise de casos importados pela fonte de infecção (`COUFINF`/`COPAISINF`).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `EXAN` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `EXAN` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `EXANBR25.dbc` — `EXAN` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). Não há arquivos em `FINAIS` para o agravo: toda a série (2007 a 2026) está em `PRELIM` (ex.: `EXANBR26.dbc`, atualização de 23/09/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-exan/<ano>/sinan-exan_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-exan/2026/sinan-exan_preliminar_2026-br@20260923.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `EXANBR25.dbc` (108 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CS_SUSPEIT` | Inteiro | Tipo de caso: suspeito de sarampo, rubéola ou caso compatível com doença exantemática |
| `DT_NOTIFIC` / `SEM_NOT` / `NU_ANO` | Data / Inteiro | Data, semana epidemiológica e ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `ID_UNIDADE` | String (7) | Código CNES da unidade notificadora |
| `DT_SIN_PRI` / `SEM_PRI` | Data / Inteiro | Data e semana de início dos sintomas |
| `NU_IDADE_N` / `CS_SEXO` / `CS_RACA` / `CS_ESCOL_N` | Inteiro/String | Idade decomposta por unidade, sexo, raça/cor e escolaridade |
| `CS_VACINA` / `DT_DOSE_N` | Inteiro / Data | Tomou vacina dupla ou triviral (1 - Sim, 2 - Não, 9 - Ignorado) e data da última dose |
| `CS_FONTE` | Inteiro | Contato com caso suspeito/confirmado de sarampo ou rubéola até 23 dias antes do início dos sintomas (domicílio, creche/escola, posto de saúde/hospital, outro Estado/Município) |
| `DT_FEBRE` / `DT_INICIO_` | Data (`AAAAMMDD`) | Data do início da febre e do exantema |
| `ID_TOSSE`/`ID_CORIZA`/`ID_CONJUNT`/`ID_ARTRALG`/`ID_GANGLIO`/`ID_RETRO` | Inteiro | Sinais e sintomas: tosse, coriza, conjuntivite, artralgia, linfadenopatias gerais e retroauriculares |
| `ID_HOSPIT` / `DT_INTERNA` / `UF_H` / `NM_MUN_HOS` | Inteiro/Data/String | Hospitalização, data da internação e local |
| `DT_COL_1` / `DT_COL_2` | Data | Datas das coletas de sangue (1ª e 2ª amostras para sorologia) |
| `ID_S1_IGM`/`ID_S1_IGG`/`ID_S2_IGM`/`ID_S2_IGG` | Inteiro | Resultados de IgM e IgG na 1ª e 2ª amostras (positivo/negativo/inconclusivo/não realizado) |
| `ID_S1_IGM_`/`ID_S1_IGG_`/`ID_S2_*`/`ID_RE_*` | Inteiro | Resultados complementares/repetidos das sorologias (menciona o laboratório de referência) |
| `TPEXANTE` | Inteiro | Situação da investigação de doença exantemática |
| `ID_SANGUE`/`ID_URINA`/`ID_SECRECA`/`ID_LIQUOR` | Inteiro | Coleta de outros materiais (sangue, urina, secreção, líquor) |
| `ID_ETIOLOG` / `ETIOL_OUTR` | Inteiro/String | Outra etiologia investigada e descrição (ex.: dengue, parvovírus B19, enterovírus) |
| `CS_VACINAL` | Inteiro | Bloqueio vacinal realizado (todos vacinados, parte vacinados, sem história de contato, não realizado) |
| `MENOR_5ANO`/`DE5A14ANOS`/`DE15A39ANO`/`INT_TEMPO` | Inteiro | Bloqueios vacinais por grupos etários e intervalo entre início dos sintomas e notificação |
| `CLASSI_FIN` | Inteiro | Classificação final: 1 - Sarampo, 2 - Rubéola, 3 - Descartado |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte: 1 - Laboratorial, 2 - Vínculo Epidemiológico, 3 - Clínico, 4 - Data da última dose da vacina |
| `CS_DESCART` | Inteiro | Motivo do descarte (ex.: exame IgM negativo, vacinados sem exame, conf. exantemático com outra etiologia) |
| `COUFINF`/`COPAISINF`/`COMUNINF` | String | UF, país e município prováveis da fonte de infecção (autoctonia/importação) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito por doença exantemática, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` / `DT_ENCERRA` / `DT_DESC*` | Data (`AAAAMMDD`) | Datas do óbito, de encerramento e das despesas relacionadas à comunicação de surtos |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE, `String` com `zfill`), `ID_UNIDADE` (CNES), `ID_OCUPA_N` (CBO); códigos de classificação (`CLASSI_FIN`, `CRITERIO`, `EVOLUCAO`) só viram categóricos após mapeamento explícito, com a atenção para 1 = Sarampo e 2 = Rubéola (não "confirmado/descartado" como em outras fichas).
- **Datas e competências**: todas as datas (`DT_NOTIFIC`, `DT_SIN_PRI`, `DT_FEBRE`, `DT_INICIO_`, `DT_COL_1/2`, `DT_DOSE_N`, `DT_OBITO`, `DT_ENCERRA`) vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`); `SEM_NOT`/`SEM_PRI` são semanas epidemiológicas `AAAASS`.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: os fluxos de sorologia em cadeia (1ª amostra, 2ª amostra e repetida) devem ser interpretados por amostra no cálculo de confirmados; o descarte tem motivo codificado (`CS_DESCART`) e datas específicas (`DT_DESC*`); toda a série está em `PRELIM`, com dados sujeitos a revisão; e, diferentemente das demais fichas do SINAN, `CLASSI_FIN` = 1 significa Sarampo e 2 significa Rubéola (a opção de descartado é 3).

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-exan
quantilica datasus list sinan-exan

# 2. Baixar microdados de sinan-exan com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-exan -o ./data --start 2007 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-exan -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-exan -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-exan/2025/sinan-exan_preliminar_2025-br@20250923.dbc", clean=True)

# Distribuição das notificações por classificação final (1-Sarampo, 2-Rubéola, 3-Descartado) por ano
print(qdf.group_by(["classi_fin", "nu_ano"]).len().sort(["nu_ano", "classi_fin"]))

# Casos confirmados com critério de confirmação (1-Laboratorial, 2-Vínculo, 3-Clínico)
saralpo = qdf.filter(pl.col("classi_fin") == 1).group_by("criterio").len().sort("criterio")
print(saralpo)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Doenças Exantemáticas (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulos de sarampo, rubéola e síndrome da rubéola congênita; Plano Nacional de Solução de Surtos do MS (manual do sistema de notificação e vigilância do sarampo)
