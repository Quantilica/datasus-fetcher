# `sinan-pfan` — Paralisia Flácida Aguda

O `sinan-pfan` contém os microdados das notificações e investigações epidemiológicas de casos de Paralisia Flácida Aguda (PFA, CID-10 A80, G99.8 e correlatos) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha de notificação/investigação de um caso suspeito de PFA, em todos os menores de 15 anos com paralisia flácida aguda ou pessoas de qualquer idade com suspeita de poliomielite. É a base central da vigilância de poliomielite no Brasil, com o leiaute mais extenso do lote (178 colunas na ficha v5.0, revisão abril/2012): investigação clínica detalhada (força muscular e tônus por membro, sensibilidade por região, reflexos), amostras de fezes/liquor, diagnóstico laboratorial (isolamento de poliovírus e diferenciação intraespecífica para vírus selvagem e vírus derivado de cepa vacinal — PVDV) e a avaliação de sequelas a 60 dias.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-pfan` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (bases `FINAIS` históricas e anos recentes apenas em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 20 arquivos (~1,4 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A paralisia flácida aguda é agravo de notificação compulsória universal para menores de 15 anos (e qualquer idade com suspeita de poliomielite, A80) desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, com regulamentação hoje consolidada na Portaria GM/MS nº 204/2016. A vigilância é operada pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) em articulação com o GT-SINAN, os Comitês Regionais e o laboratório nacional de referência da OMS (Fiocruz/RJ), com o objetivo de certificar a interrupção da transmissão do poliovírus selvagem e do vírus derivado de cepa vacinal (VDPV). A base alimenta os indicadores oficiais acordados com a OMS: taxa de notificação mínima de 1 caso de PFA por 100 mil menores de 15 anos, percentual de casos com investigação completa, percentual de casos com coleta adequada de amostras (2 amostras de fezes em até 14 dias), investigação de sequelas a 60 dias e resposta rápida na eventual hipótese de reintrodução do poliovírus (alerta máximo da saúde global).

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Paralisia Flácida Aguda** do SINAN. A notificação nasce com o caso suspeito (paralisia flácida aguda de início súbito em menores de 15 anos, ou pessoa de qualquer idade com suspeita de poliomielite) e é completada com a investigação clínica pormenorizada (força muscular e tônus por membro, sensibilidade, reflexos e raio X), as duas coletas de fezes e liquor para cultura/estudos laboratoriais (`LAB_*`), o antecedente de vacinação (VOP/IPV, doses e datas), o seguimento ao 60º dia da evolução (força muscular e revisão das sequelas: `EVOR_*`, `EVOR1_DT_R`) e a classificação final (confirmado, compatível, associado à vacina, descartado ou confirmado PVDV). A unidade de análise é o caso notificado.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. O instrumento é revisado periodicamente (rev. abril/2012) e acompanhou as mudanças das estratégias da OPAS/OMS para a verificação da interrupção da transmissão do poliovírus — inclusive a diferenciação entre vírus selvagem, vírus derivado de cepa vacinal (PVDV) e outros agentes diagnosticados como síndrome de Guillain-Barré (o CID do caso descartado `CON_DESCAR`), com blocos clínicos, laboratoriais, de seguimento e de diagnóstico distribuídos ao longo da ficha estruturada.

Aplicações analíticas típicas: monitoramento da incidência de PFA (casos notificados por 100 mil menores de 15 anos, comparado às metas da OMS); distribuição das classificações finais (confirmado, compatível, associado à vacina, descartado e confirmado PVDV); percentual de casos com coletas exitosas (2 amostras de fezes coletadas em até 14 dias, `LAB_DT_F1`/`LAB_DT_F2`); percentual de casos com seguimento ao 60º dia (`EVOR1_DT_R`) e sequelas classificadas; diagnóstico dos CID-10 dos casos descartados (`CON_DESCAR`, com predomínio da síndrome de Guillain-Barré — G61.0); e vigilância de eventual reintrodução do poliovírus selvagem ou vírus derivado de cepa vacinal (VDPV).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `PFAN` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `PFAN` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `PFANBR25.dbc` — `PFAN` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As consolidações até 2022 estão em `FINAIS` e os anos de 2023 a 2026 estão apenas em `PRELIM` (ex.: `PFANBR26.dbc`, atualização de 21/09/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-pfan/<ano>/sinan-pfan_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-pfan/2026/sinan-pfan_preliminar_2026-br@20260921.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `PFANBR25.dbc` (178 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `NU_IDADE_N` / `CS_SEXO` | Inteiro/String | Idade decomposta por unidade e sexo (casos de menores de 15 anos e outras idades com suspeita de pólio) |
| `DTPRICONS` | Data (`AAAAMMDD`) | Data da primeira consulta pelo serviço de saúde por motivo da paralisia |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `ANT_VACINA` / `ANT_DOSES` / `ANT_DT_VAC` / `ANT_30_DIA` | Inteiro/Data | Antecedentes de vacinação contra poliomielite (dose aplicada, nº de doses, data e vacinação nos 30 dias anteriores) |
| `CLI_FEBRE`/`CLI_DIARRE`/`CLI_DORES`/`CLI_VOMITO`/`CLI_CEFALE`/`CLI_OUTROS` | Inteiro | Sintomas prodrômicos: febre, diarreia, dores, vômitos, cefaléia e outros |
| `CLI_AGUDA`/`CLI_FLACID`/`CLI_ASSIME`/`CLI_PROGRE`/`CLI_ASCEND`/`CLI_DESCEN` | Inteiro | Características da paralisia: início agudo, flacidez, assimetria, progressão ascendente/descendente |
| `CLI_F_MIE`/`CLI_F_MSE`/`CLI_F_MID`/`CLI_F_MSD` | Inteiro | Força muscular por membro (membro inferior esquerdo/direito, superior esquerdo/direito) |
| `LOCA_MIE_N`/`LOCA_MSE_N`/`LOCA_MID_N`/`LOCA_MSD_N` | Inteiro | Localização da fraqueza por membro (nº do segmento acometido) |
| `CLI_RESPIR`/`CLI_CERVIC`/`CLI_FACE`/`CLI_KERNIG`/`CLI_NUCA`/`CLI_BRUDZ`/`CLI_CONTAT` | Inteiro | Comprometimento respiratório, cervical, facial; sinal de Kernig/Brudzinski; rigidez de nuca; contato com casos de PFA |
| `CLI_INJECA`/`CLI_LOCAL` | Inteiro | Piora após injeção aplicada no membro paralisado |
| `CLI_A_*` | Inteiro | Bloco de avaliação clínico-neuromuscular por membro: força, tônus, sensibilidade e reflexos (campos `CLI_A_F*`, `CLI_A_T*`, `CLI_A_S*`, `CLI_AQ_*`, `CLI_PAT*`, `CLI_BIC*`, `CLI_TRIE*` etc.) |
| `ATE_HIPOTE`/`ATE_HOSP`/`ATE_DT_INT`/`ATE_UF`/`ATE_MUNICI` | Inteiro/Data/String | Hospitalização, data, UF e município da internação |
| `LAB_DT_F1`/`LAB_DT_F2` | Data | Datas de coleta das amostras de fezes |
| `LAB_RES_F1`/`LAB_RES_F2`/`LAB_RES_F3` | Inteiro | Resultados do isolamento de poliovírus nas amostras de fezes |
| `LAB_DT_L_1`/`LAB_L_CEL1`/`LAB_L_LIN1`/`LAB_L_PRO1`/`LAB_L_GLI1`/`LAB_L_CL1` | Data/Inteiro | Liquor: data da coleta, células, linfócitos, proteínas, glicose e cloro |
| `LAB_E_D_1`/`LAB_CELEBR`/`LAB_MEDULA`/`LAB_INTEST` | Data/Inteiro | Exames complementares: eletromiografia, biópsia cerebral, medula espinal e intestino |
| `LAB_DT_R1`/`LAB_DT_C1`/`LAB_RESULT` | Data/Inteiro | Revisão das amostras não-coletadas/exames e resultado conclusivo |
| `EVOR_*`/`EVOR1_DT_R` | Inteiro/Data | Acompanhamento da 60ª dia: força muscular por membro (`EVOR_F_*`), tônus (`EVOR_A_*`), sensibilidade por região (`EVOR_S_*`/`REFR_*`) e data da revisão |
| `CLASSI_FIN` | Inteiro | Classificação final: 1 - Confirmado, 2 - Compatível, 3 - Associado à vacina, 4 - Descartado, 5 - Confirmado PVDV |
| `CRITERIO` | Inteiro | Critério de classificação: 1 - Laboratorial, 2 - Clínico Epidemiológico, 3 - Perda de Seguimento, 4 - Óbito, 5 - Evolução |
| `CON_DESCAR` | String (5) | CID-10 do caso descartado (ex.: síndrome de Guillain-Barré — G61.0) |
| `EVOLUCAO` | Inteiro | Evolução do caso: 1 - Cura com sequela, 2 - Cura sem sequela, 3 - Óbito por PFA/Pólio, 4 - Óbito por outras causas, 9 - Ignorado |
| `DT_OBITO` / `DT_ENCERRA` | Data (`AAAAMMDD`) | Data do óbito e de encerramento da investigação |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE, `String` com `zfill`), `ID_UNIDADE` (CNES), `ID_OCUPA_N` (CBO); códigos de classificação (`CLASSI_FIN`, `CRITERIO`, `EVOLUCAO`) só viram categóricos após mapeamento explícito.
- **Datas e competências**: todas as datas (`DT_NOTIFIC`, `DT_SIN_PRI`, `DTPRICONS`, `DT_INVEST`, `LAB_DT_F1/F2`, `LAB_DT_L_1`, `EVOR1_DT_R`, `DT_OBITO`, `DT_ENCERRA`) vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`); `SEM_NOT`/`SEM_PRI` são semanas epidemiológicas `AAAASS`.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: o caso confirmado exige 2 amostras de fezes (data de coleta até 14 dias do início da paralisia, `LAB_DT_F1`/`LAB_DT_F2`); os campos de evolução a 60 dias (`EVOR_*`) sustentam o critério "perda de seguimento" (`CRITERIO` = 3); o CID do caso descartado (`CON_DESCAR`) segue a tabela anexa da ficha (dentre elas, a síndrome de Guillain-Barré); e a força/sensibilidade é registrada por membro em blocos separados (`CLI_*` no diagnóstico e `EVOR_*`/`REFR_*` no seguimento), o que exige agregação cuidadosa para indicadores de paralisia residual.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-pfan
quantilica datasus list sinan-pfan

# 2. Baixar microdados de sinan-pfan com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-pfan -o ./data --start 2007 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-pfan -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-pfan -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-pfan/2025/sinan-pfan_preliminar_2025-br@20250921.dbc", clean=True)

# Distribuição da classificação final dos casos (1-Confirmado, 2-Compatível, 3-Associado à vacina, 4-Descartado, 5-Confirmado PVDV)
print(qdf.group_by("classi_fin").len().sort("classi_fin"))

# CIDs dos casos descartados (ex.: síndrome de Guillain-Barré)
descartes = qdf.filter(pl.col("classi_fin") == 4).group_by("con_descar").len().sort("con_descar")
print(descartes)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Paralisia Flácida Aguda/Poliomielite (ficha e dicionário v5.0)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de paralisia flácida aguda/poliomielite; Diretrizes da OPAS/OMS para a vigilância e resposta rápida a HVDPV
