# `sinan-rota` — Rotavírus

O `sinan-rota` contém os microdados das notificações e investigações epidemiológicas de casos de Rotavírus (Ficha de Vigilância de Rotavírus, CID-10 A08.0) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de rotavirose — fezes coletadas para pesquisa do rotavírus — preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. É a base de vigilância sentinela da doença diarréica por rotavírus, com 73 colunas na série atual: quadro clínico diarreico/vomitivo (com contagem de episódios e duração), alimentação do lactente (leite materno/formula), a vacinação (VOP/VORH, rotavírus — doses, lotes e fabricante), genotipagem de rotavírus (sorotipos G e P), outros enterovírus/bactérias/parasitas e identificação de surtos.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-rota` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (bases `FINAIS` históricas e anos recentes apenas em `PRELIM`) |
| **Cobertura temporal no FTP** | 2009 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 18 arquivos (~1,4 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A vigilância do rotavírus é operada pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) por meio da vigilância sentinela de gastroenterites (unidades sentinelas de vigilância de rotavírus e laboratórios de referência da Fiocruz), com registro no SINAN desde 2009, em ligação com a rede de vigilância sentinela de rotavírus criada em apoio à introdução da vacina oral de rotavírus humano (VORH) no PNI, em 2006. A base é instrumento central para monitoramento da carga de doença, da circulação de genotipos (G/P) e da efetividade da vacina nos serviços sentinelas. Cada caso é um registro de vigilância sentinela (coleta de fezes de gastroenterites agudas em unidades hospitalares e ambulatórios selecionados) — os totais não representam a incidência endêmica nacional.

O evento gerador deste dataset é a **Ficha de Vigilância de Rotavírus** do SINAN (ficha de rotavírus, integrada ao PNI e com Nota Técnica própria do DATASUS/SVSA). A notificação nasce com a suspeição clínica de gastroenterite aguda em criança (diarreia com sangue, frequência de episódios, febre, vômitos) e a coleta de fezes para pesquisa de rotavírus. A investigação é completada com os dados de alimentação do lactente (`LEITE`, `TIPO_LEITE`), o histórico de vacinação contra rotavírus (doses com lote e fabricante: `VACINA`, `DT_1VAC`, `LOTE1`, `LAB_PROD1`, `DT_2VAC`), o resultado da pesquisa de antígeno/Ac nas fezes (`ROTA_R`, `DT_FEZES`), a genotipagem do vírus (G/P: `GENOT_G`, `GENOT_P`), a pesquisa de co-infecções (`OUT_VIRUS`, `BACTERIA`, `PARASITA`) e o vínculo a surto (`CASO_ISOLA`, `SURTO`).

A série histórica inicia em **2009**: o FTP contém a primeira consolidação em `FINAIS` (2009 a 2024) e os anos de 2025 a 2026 apenas em `PRELIM`. O instrumento é complementado na documentação do FTP pela **Nota Técnica do Rotavírus** (`Nota_Tecnica_Rotavirus.pdf`, no diretório `SINAN/DOCS`), que detalha a definição de caso, as coletas e o encerramento — vigilância sentinela com o rotavírus como causa principal de diarreia em menores de 5 anos, com a vacinação introduzida em 2006 no calendário do PNI.

Aplicações analíticas típicas: percentual de casos positivos para rotavírus nas unidades sentinelas (`ROTA_R`); distribuição de genotipos G/P (`GENOT_G`, `GENOT_P`) e co-infecções com outros vírus/bactérias (`OUT_VIRUS`, `BACTERIA`, `PARASITA`); efetividade vacinal (comparar casos vacinados/não vacinados e doses/lotes `DT_1VAC`/`DT_2VAC`); análise de surtos (`SURTO`) e a casuística por faixa etária (`NU_IDADE_N`) e tipo de alimentação (`LEITE`, `TIPO_LEITE`); o monitoramento da circulação viral e da emergência de novos genotipos — informação central do comitê de vigilância de rotavírus e opções vacinais no calendário.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ROTA` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ROTA` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `ROTABR25.dbc` — `ROTA` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). A série em `FINAIS` começa em 2009 e vai até 2024; os anos de 2025 e 2026 estão apenas em `PRELIM` (ex.: `ROTABR26.dbc`, atualização de 30/04/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-rota/<ano>/sinan-rota_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-rota/2026/sinan-rota_preliminar_2026-br@20260430.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip`, as instruções POP_I/II/III de acesso/descompactação e a **`Nota_Tecnica_Rotavirus.pdf`** (nota técnica específica do agravo); em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `ROTABR25.dbc` (73 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CS_SUSPEIT` / `CS_MENING` | Inteiro | Caso suspeito de rotavirose e manifestações associadas (síndromes agudas) |
| `DT_NOTIFIC` / `SEM_NOT` / `NU_ANO` | Data / Inteiro | Data, semana epidemiológica e ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `DT_SIN_PRI` / `SEM_PRI` | Data / Inteiro | Data e semana de início dos sintomas |
| `NU_IDADE_N` / `CS_SEXO` | Inteiro/String | Idade decomposta por unidade e sexo (casos concentrados em menores de 5 anos) |
| `VOMITO` / `N_VOMITO` / `D_VOMITO` | Inteiro | Vômito presente, número de episódios e duração (dias) |
| `FEBRE` / `T_FEBRE` | Inteiro | Febre presente e duração |
| `DIARREIA` / `N_DIAR` / `D_DIAR` | Inteiro | Diarreia presente, número de episódios e duração (dias) |
| `SANG` | Inteiro | Diarreia com sangue |
| `LEITE` / `TIPO_LEITE` | Inteiro | Tipo de alimentação: leite materno, fórmula (tipo registrado) |
| `VACINA` / `DT_1VAC` / `LOTE1` / `LAB_PROD1` | Inteiro/Data/String | Histórico de vacinação contra rotavírus (VOP/VORH): doses, data da 1ª dose, lote e fabricante |
| `DT_2VAC` / `LOTE2` / `LAB_PROD2` | Data/String | Data, lote e fabricante da 2ª dose |
| `VOP_VORH` / `DT_VOP` | Inteiro/Data | Dose de rotavírus VOP/VORH aplicada e data |
| `DT_FEZES` | Data (`AAAAMMDD`) | Data de coleta de fezes para laboratório |
| `ROTA_R` | Inteiro | Pesquisa de rotavírus nas fezes: resultado (positivo/negativo/em processamento/não realizado) |
| `GENOT_G` / `GENOT_P` | String | Genotipo G e P do rotavírus identificado (tipagem molecular) |
| `OUT_VIRUS` / `NOME_VIRUS` | Inteiro/String | Concomitância de outros vírus e nome do vírus |
| `BACTERIA` / `NOME_BACT` | Inteiro/String | Co-infecção bacteriana e nome |
| `PARASITA` / `NOME_PARAS` | Inteiro/String | Co-infecção parasitária e nome |
| `MEDICAMENT` / `OUT_MEDIC` / `DT_ENVIO` / `ACONDIC` | Inteiro/Data | Medicação prévia, outra medicação, data de envio da amostra e condições de acondicionamento |
| `CLASSI_FIN` | Inteiro | Classificação final do caso |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte |
| `CASO_ISOLA` / `SURTO` | Inteiro | O caso é isolado ou vinculado a surto (1 - Sim, 2 - Não) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito por rotavirose, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` / `DT_ENCERRA` / `DT_DIGITA` | Data (`AAAAMMDD`) | Data do óbito, de encerramento e de digitação |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE, `String` com `zfill`), `ID_UNIDADE` (CNES), `ID_OCUPA_N` (CBO); códigos de classificação (`CLASSI_FIN`, `CRITERIO`, `EVOLUCAO`) só viram categóricos após mapeamento explícito.
- **Datas e competências**: `DT_NOTIFIC`, `DT_SIN_PRI`, `DT_1VAC`, `DT_2VAC`, `DT_VOP`, `DT_FEZES`, `DT_ENVIO`, `DT_OBITO` e `DT_ENCERRA` vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`); `SEM_NOT`/`SEM_PRI` são semanas epidemiológicas `AAAASS`.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: a base é de **vigilância sentinela** (unidades selecionadas), não universal — os totais não representam a incidência nacional; a genotipagem (`GENOT_G`/`GENOT_P`) é registrada em poucos casos (requer vínculo a laboratório de referência), com frequentes resultados "não realizado"; a efetividade vacinal exige a lógica de doses/lotes e fabricante por dose (`LOTE1`/`LOTE2`, `LAB_PROD1/2`); e há casos com "outros vírus" (`OUT_VIRUS`) investigados como outras etiologias de diarreia.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-rota
quantilica datasus list sinan-rota

# 2. Baixar microdados de sinan-rota com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-rota -o ./data --start 2009 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-rota -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-rota -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-rota/2025/sinan-rota_preliminar_2025-br@20260430.dbc", clean=True)

# Positividade de rotavírus nas fezes coletadas (vigilância sentinela)
posit = qdf.filter(pl.col("rota_r") == 1).group_by("nu_ano").len().sort("nu_ano")
print(posit)

# Genotipos identificados nas amostras positivas
geno = qdf.filter(
    pl.col("rota_r") == 1
).group_by(["genot_g", "genot_p"]).len().sort("genot_g")
print(geno)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Rotavírus (ficha e dicionário de dados)**: https://portalsinan.saude.gov.br
- **Nota Técnica do DATASUS/SVSA sobre Rotavírus** (`Nota_Tecnica_Rotavirus.pdf`, disponível em `SINAN/DOCS`)
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de gastroenterites por rotavírus e vigilância sentinela de doença diarréica aguda
