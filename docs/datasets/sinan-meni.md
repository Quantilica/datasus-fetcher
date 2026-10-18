# `sinan-meni` — Meningite

O `sinan-meni` contém os microdados das notificações e investigações epidemiológicas de casos de Meningite (CID-10 A39, G00, G01, A87, G03 e correlatos) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito de meningite, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. Com 132 colunas no leiaute v5.0 é uma das fichas mais extensas do SINAN, cobrindo detalhadamente sinais e sintomas, o extenso bloco laboratorial (punção liquórica, culturas, contraimunoeletroforese/CIE, aglutinação em látex, isolamento viral e PCR) e a classificação final da etiologia — meningocócica, tuberculosa, asséptica, por outras bactérias ou por outra etiologia.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-meni` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (bases `FINAIS` históricas e anos recentes apenas em `PRELIM`) |
| **Cobertura temporal no FTP** | 2007 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 20 arquivos (~49,2 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A meningite é agravo de notificação compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, e atualmente consta da Lista Nacional de Agravos de Notificação Compulsória consolidada na Portaria GM/MS nº 204/2016. O seguimento da vigilância é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), em articulação com o GT-SINAN e a rede de laboratórios centrais (LACEN e laboratórios de referência nacional, como o Instituto Adolfo Lutz e o FioCruz/RJ), dando suporte à vigilância laboratorial integrada e à avaliação das estratégias de vacinação do PNI (meningocócica C/ACWY/B, pneumocócica e Hib). Como a síndrome pode ser causada por múltiplos agentes (bactérias, vírus, fungos e o bacilo da tuberculose), o SINAN exige o encerramento do caso com a etiologia confirmada por meio do bloco laboratorial — daí a extensão da ficha.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Meningite** do SINAN. A notificação nasce com a suspeição clínica (cefaléia, febre, vômitos, convulsões, rigidez de nuca, sinal de Kernig/Brudzinski, abaulamento de fontanela, coma, petéquias) e é completada com resultados do líquido cefalorraquidiano (aspecto, células, bioquímica) e dos exames microbiológicos por amostra biológica (coprocultura, LATEX aglutinação, CIE, isolamento viral e PCR). A unidade de análise é o caso notificado, com a etiologia definida no encerramento quando aplicável — a investigação orienta ainda a quimioprofilaxia de comunicantes nos casos de doença meningocócica.

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. O leiaute manteve-se estável ao longo da série, com revisões pontuais do dicionário (versão revisada em julho/2010) e mudanças de instrumento menos frequentes do que em outras fichas do SINAN, o que facilita a comparabilidade longitudinal. Os campos de antecedentes de vacinação (`ANT_BCG`, `ANT_CONJ_C`, `ANT_TRIPLI`, `ANT_HEMO_T`, `ANT_PNEUMO`) registram dose, lote e data da última dose, permitindo a avaliação de falhas vacinais no suporte das doenças penetrante dos eventos à admissão das fichas de eventos adversos das vacinas de PNI.

Aplicações analíticas típicas: incidência de meningite meningocócica e meningococcemia por faixa etária e UF (base dos dossiês de vacinação ACWY e B); distribuição de etiologias confirmadas (`CON_DIAGES`, `CLA_ME_BAC`/`CLA_ME_ASS`/`CLA_ME_ETI`); formas assépticas virais e tuberculosa; letalidade e hospitalização; percentual de casos com critério laboratorial de confirmação (culturas, LATEX e PCR por líquor e sangue); cobertura de quimioprofilaxia de comunicantes (`MED_NUCOMU`, `MED_QUIMIO`) e curvas epidêmicas por semana de início dos sintomas (`SEM_PRI`).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `MENI` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `MENI` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `MENIBR25.dbc` — `MENI` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). As consolidações até 2022 estão em `FINAIS` e os anos de 2023 a 2026 estão apenas em `PRELIM` (ex.: `MENIBR26.dbc`, atualização de 21/09/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-meni/<ano>/sinan-meni_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-meni/2026/sinan-meni_preliminar_2026-br@20260921.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `MENIBR25.dbc` (132 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CS_MENING` | Inteiro | Tipo de meningite notificada/investigada conforme Quadro I do dicionário (meningococcemia, meningite meningocócica, tuberculosa asséptica, por outras bactérias etc.) |
| `DT_NOTIFIC` / `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de notificação e data de início dos sintomas (base das curvas epidêmicas com `SEM_NOT`/`SEM_PRI`) |
| `NU_ANO` | Inteiro | Ano da notificação |
| `ID_MUNICIP` / `ID_MN_RESI` | String (6/7) | Códigos IBGE de município de notificação e residência |
| `ID_UNIDADE` | String (7) | Código CNES da unidade notificadora |
| `ANT_AC`/`ANT_CONJ_C`/`ANT_TRIPLI`/`ANT_HEMO_T`/`ANT_PNEUMO` | Inteiro | Antecedentes de vacinação: meningocócica C, conjugada, tríplice bacteriana, Hib (Hemófilo tipo B), pneumocócica (com doses, lote e datas `ANT_DOSE_*`/`ANT_DTUL_*`) |
| `ANT_AIDS`/`ANT_IMUNO`/`ANT_TUBE`/`ANT_TRAUMA`/`ANT_INF_HO` | Inteiro | Antecedentes associados: AIDS, imunodepressão, tuberculose, trauma/extracção, infecção hospitalar, cirurgia prévia, uso de drogas imunossupressoras |
| `CLI_CEFALE`/`CLI_FEBRE`/`CLI_VOMITO`/`CLI_CONVUL`/`CLI_RIGIDE`/`CLI_KERNIG`/`CLI_ABAULA`/`CLI_COMA`/`CLI_PETEQU` | Inteiro | Sinais e sintomas: cefaléia, febre, vômitos, convulsões, rigidez de nuca, Kernig, abaulamento de fontanela, coma e outras manifestações clínicas |
| `ATE_HOSPIT`/`ATE_INTERN` | Inteiro | Hospitalização (local e se houve internação) |
| `LAB_PUNCAO` / `LAB_DTPUNC` | Inteiro / Data | Punção liquórica realizada e data da coleta do líquor |
| `LAB_ASPECT` | Inteiro | Aspecto do líquor (hábito e da investigação: normal, turbido, hemorrágico, coleções fibrinosas) |
| `LAB_CTLIQU`/`LAB_CTLESA`/`LAB_CTSANG`/`LAB_CTESCA` | Inteiro | Culturas (líquor, lesão, sangue, escarro): amostra coletada, em processamento, resultado ou não realizado |
| `LAB_BCLIQU`/`LAB_BCSANG` | Inteiro | Bacterioscopia: 1 = Positiva, 2 = Negativa, 3 = Em processamento, 4 = Não realizado |
| `LAB_AGLIQU`/`LAB_AGSANG` | Inteiro | Aglutinação ou LATEX (líquor, sangue): agente etiológico identificado segundo Quadro X |
| `LAB_ISLIQU`/`LAB_ISFEZE` | Inteiro | Isolamento viral (líquor, fezes): agente etiológico segundo Quadro XI |
| `LAB_PCLIQU`/`LAB_PCLESA`/`LAB_PCSANG`/`LAB_PCESCA` | Inteiro | PCR (líquor, lesão petequial, sangue, escarro): agente etiológico segundo Quadro XII |
| `LAB_HEMA`/`LAB_NEUTRO`/`LAB_GLICO`/`LAB_PROT`/`LAB_CLOR` | Inteiro | Exame do líquor: hemácias/mm3, neutrófilos (%), glicorraquia, proteinorraquia, clororraquia |
| `CLASSI_FIN` | Inteiro | Classificação do caso: 1 - Confirmado, 2 - Descartado |
| `CON_DIAGES` | Inteiro | Se confirmado, especifique a etiologia: 1 - Meningococcemia, 2 - Meningite Meningocócica, 3 - Meningite Meningocócica com Meningococcemia, 4 - Meningite Tuberculosa, 5 - Meningite por outras bactérias, 6 - Meningite não especificada, 7 - Meningite Asséptica, 8 - Meningite por outra etiologia |
| `CLA_ME_BAC`/`CLA_ME_ASS`/`CLA_ME_ETI` | String (4) | Detalhamento da etiologia nos casos 5 (outras bactérias — Quadro II), 7 (asséptica — Quadro III) e 8 (outra etiologia) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial; 2 - Clínico; 3 - Clínico laboratorial aplicado em inquéritos epidemiológicos) |
| `MED_NUCOMU`/`MED_QUIMIO`/`MED_DT_QUI` | Inteiro/Data | Comunicantes identificados, quimioprofilaxia realizada e data do esquema DIM/QP |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito, 3 - Óbito atribuído a outra causa, 9 - Ignorado) |
| `DT_OBITO` / `DT_ENCERRA` | Data (`AAAAMMDD`) | Data do óbito e de encerramento do caso |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE, `String` com `zfill`), `ID_UNIDADE` (CNES), `ID_OCUPA_N` (CBO); códigos de classificação (`CLASSI_FIN`, `CON_DIAGES`, `CLA_ME_*`, `CRITERIO`, `EVOLUCAO`) só viram categóricos após mapeamento explícito, inclusive com a regra do dicionário de complementar zero à esquerda quando digitado com 1 dígito.
- **Datas e competências**: todas as datas (`DT_NOTIFIC`, `DT_SIN_PRI`, `DT_INVEST`, `LAB_DTPUNC`, `DT_OBITO`, `DT_ENCERRA`, `DT_DIGITA` e as datas de dose/suprimento `ANT_DTUL_*`, `MED_DT_QUI`) vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`); `SEM_NOT`/`SEM_PRI` são semanas epidemiológicas `AAAASS`.
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`), datas vazias/espaços em branco e o literal `00000000` viram nulo por `SENTINEL_NULLS`; registros com marcador lógico dBASE `_deleted` são removidos.
- **Particularidades do dataset**: os campos de etiologia detalhada (`CLA_ME_*`) usam códigos dos Quadros anexos ao dicionário (Quadro II para bactérias, Quadro III para meningite asséptica e Quadros de agentes para isolamento/LATEX/CIE/PCR) e devem ser interpretados em conjunto com `CON_DIAGES`; os campos `LAB_*` registram tanto a coleta da amostra quanto o resultado do exame, o que exige leitura cuidadosa por material biológico; a série inicia em 2007 (não há bases do Sinan-Windows para esse agravo no FTP), facilitando a comparabilidade; e nos registros com `MIGRADO_W` há possíveis informações parciais.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-meni
quantilica datasus list sinan-meni

# 2. Baixar microdados de sinan-meni com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-meni -o ./data --start 2007 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-meni -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-meni -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-meni/2025/sinan-meni_preliminar_2025-br@20250521.dbc", clean=True)

# Casos confirmados de doença meningocócica (etiologias 1 a 3 do CON_DIAGES)
meningo = qdf.filter(
    pl.col("classi_fin") == 1,
    pl.col("con_diages").is_in([1, 2, 3]),
)
print(meningo.group_by("nu_ano").len().sort("nu_ano"))

# Percentual de confirmados com critério laboratorial (crítico a capacidade diagnóstica)
lab = meningo.group_by("criterio").len().sort("criterio")
print(lab)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`

- Portal de Transferência de Arquivos do DATASUS: https://datasus.saude.gov.br/transferencia-de-arquivos/
- TabNet DATASUS: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- Portal SINAN — Meningite (ficha e dicionário de dados v5.0 e REV. julho/2010): https://portalsinan.saude.gov.br
- Portaria GM/MS nº 204/2016 (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- PCDaS/Fiocruz — SINAN: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- Guia de Vigilância em Saúde (SVSA/MS, Ed. atual) — capítulo de doença meningocócica e meningites; Manual dos Serviços de Saúde (MS) sobre manejo e vigilância de meningites
