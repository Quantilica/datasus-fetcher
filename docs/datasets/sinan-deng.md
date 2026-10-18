# `sinan-deng` — Dengue

O `sinan-deng` contém os microdados das notificações e investigações epidemiológicas de casos de Dengue (CID-10 A90) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de dengue, preenchida pelas unidades de saúde de todo o país e digitada no SINAN Net/Sinan Online. É uma das maiores bases de dados de morbidade do sistema de saúde brasileiro e centraliza o monitoramento das arboviroses urbanas transmitidas pelo *Aedes aegypti*.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-deng` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 2000 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 27 arquivos (~1,02 GB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A dengue é a arbovirose de maior impacto no Brasil e o SINAN que a monitora é gerido pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), por meio da respectiva área da vigilância de arboviroses e do GT-SINAN. A doença integra a Lista Nacional de Doenças e Agravos de Notificação Compulsória (hoje consolidada na Portaria GM/MS nº 204/2016, atualizada por normas posteriores, como a Portaria GM/MS nº 10.175/2026). A base alimenta o diagnóstico dinâmico da situação epidemiológica municipal, estadual e nacional, orienta a mobilização de planos de contingência durante epidemias sazonais e dimensiona a carga de doença anual — o Brasil é um dos países com maior número de casos de dengue do mundo.

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Dengue** do SINAN. Cada notificação individual nasce no momento da suspeição (febre de 2 a 7 dias acompanhada de, pelo menos, mais dois sintomas definidores (náuseas/vômitos, exantema, mialgias, cefaléia, dor retroorbital, petéquias ou leucopenia)) e é completada ao longo da investigação com dados clínicos, laboratoriais, de internação e de conclusão (classificação final, critério de confirmação, evolução e desfecho). A unidade de análise é o caso suspeito/confirmado notificado, não o óbito nem a internação (que ficam no SIM e no SIH/SIA).

A série histórica registra três fases do sistema de informação, conforme notas técnicas oficiais: de **2000 a 2006** os dados provêm do SINAN-Windows; de **2007 a 2013**, do SINAN Net; e **de 2014 em diante**, do SINAN Net e do **Sinan Online** (notificação em tempo real, mesma base disseminada). Houve também mudanças relevantes do instrumento de coleta: a ficha revisada de dengue incorporou a nova classificação da OMS (separando "Dengue", "Dengue com sinais de alarme" e "Dengue grave" no lugar de "Febre Hemorrágica do Dengue"/"Síndrome do Choque do Dengue") e, a partir de 2016, a ficha de investigação tornou-se unificada para Dengue e Febre de Chikungunya (`Ficha_DENGCHIK`, SVS 14/03/2016), com o campo `ID_AGRAVO` distinguindo os dois agravos na mesma estrutura.

Aplicações analíticas típicas: incidência anual de casos confirmados (por 100 mil habitantes, contra a estimativa populacional TCU), distribuição por faixa etária, sexo, raça/cor e gestação, incidência específica de dengue com sinais de alarme e dengue grave, taxa de letalidade (óbitos por casos confirmados), curvas epidémicas por semana de início dos sintomas (`DT_SIN_PRI`/`SEM_PRI`), desempenho da vigilância (proporção de usados com critério laboratorial, oportunidade de encerramento) e mapeamento de municípios prioritários para controle vetorial.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `DENG` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `DENG` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `DENGBR25.dbc` — `DENG` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `25` é o ano de notificação (2025). Em anos recentes apenas o arquivo nacional `BR` é publicado; o equivalente preliminar do ano corrente aparece em `PRELIM` (ex.: `DENGBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-deng/<ano>/sinan-deng_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-deng/2025/sinan-deng_2025-br@20260721.dbc`; arquivos preliminares recebem o sufixo do dataset `-preliminar` no nome.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` (pacote de documentação/tabulações do SINAN) e as instruções de acesso e conversão (`POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`); em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (dicionários/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (1 - Negativa, 2 - Individual, 3 - Surto e outros) |
| `ID_AGRAVO` | String | Código do agravo conforme CID-10 (A90 - Dengue; distinguindo Chikungunya na ficha unificada) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data de preenchimento da ficha de notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação, derivada de `DT_NOTIF` |
| `NU_ANO` | Inteiro | Ano da notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | Código CNES da unidade de saúde (ou fonte) notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data dos primeiros sintomas da doença (usada nas curvas epidémicas) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `NU_NOTIFIC` | String (7) | Número da notificação (identificador do registro no terminal digitador) |
| `CS_SEXO` | String (1) | Sexo do paciente (M/F/I - Ignorado) |
| `NU_IDADE_N` | Inteiro composto | Idade (o primeiro dígito indica a unidade: dia/mês/ano; ex.: `4` + idade em anos) |
| `CS_GESTANTE` | Inteiro | Estado gestacional (1 a 4 conforme grupo gestacional; 9 - Ignorado) |
| `ID_MN_RESI` | String (6/7) | Código IBGE do município de residência (vs. município de notificação) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `ANT_VAC` | Inteiro | Antecedente de vacinação contra dengue (ficha unificada recente) |
| `CLASSI_FIN` | Inteiro | Classificação final: 5 - Descartado, 10 - Dengue, 11 - Dengue com sinais de alarme, 12 - Dengue grave, 13 - Chikungunya (ficha unificada) |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte (1 - Laboratório, 2 - Clínico Epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito por dengue, 3 - Óbito por outras causas, 4 - Óbito em investigação, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE: 6 dígitos na série antiga, 7 dígitos após 2000 — manter como `String` com `zfill`), `ID_UNIDADE` (CNES de 7 dígitos), `ID_OCUPA_C` (CBO de 6 dígitos) e `NU_NOTIFIC` devem permanecer texto, nunca inteiros. Códigos de classificação (`CLASSI_FIN`, `CRITERIO`, `EVOLUCAO`) só viram categóricos após mapeamento explícito.
- **Datas e competências**: `DT_NOTIF`, `DT_SIN_PRI`, `DT_INVEST`, `DT_OBITO` e `DT_ENCERRA` vêm como `AAAAMMDD` no DBF e são convertidos para `pl.Date` pelo saneamento canônico (`wrangle_datasus`); `SEM_NOT`/`SEM_PRI` são semanas epidemiológicas `AAAASS` e devem permanecer inteiras.
- **Valores ausentes e sentinelas**: no DBF, códigos ignorados (`9`, `99`, `999999`), datas vazias/espaços em branco e o literal `00000000` são convertidos para nulo por `SENTINEL_NULLS`; registros com marcador lógico de exclusão dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: os arquivos do FTP são consolidações nacionais anuais `BR` (`:n_files` pequeno, ~27), a última série de cada ciclo ainda pode estar em `PRELIM` e sujeita a revisão; a ficha unificada Dengue/Chikungunya (desde 2016) exige filtrar por `ID_AGRAVO`/`CLASSI_FIN` para recortar apenas dengue; `CLASSI_FIN` teve categorias históricas distintas (1 - Dengue clássico, 2 - Dengue com complicações, 3 - FHD, 4 - SCD) antes de 2010, o que exige mapeamentos diferentes por período; a idade em `NU_IDADE_N` requer decomposição do primeiro dígito (unidade) antes de comparações; e duplicidades de notificação devem ser verificadas por `NU_NOTIFIC` + município + paciente antes de cálculo de incidência.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-deng
quantilica datasus list sinan-deng

# 2. Baixar microdados de sinan-deng com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-deng -o ./data --start 2010 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-deng -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-deng -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/sinan-deng/2025/sinan-deng_2025-br@20260721.dbc", clean=True)

# Visão geral: casos confirmados de dengue (classificação final tanto em versões antigas quanto novas)
confirmados = qdf.filter(
    pl.col("classi_fin").is_in([1, 2, 3, 4, 10, 11, 12])
)
print(confirmados.group_by("nu_ano").len().sort("nu_ano"))

# Curva epidêmica por semana epidemiológica de início dos sintomas
epi = (
    confirmados.group_by(["sem_pri", "nu_ano"])
    .len()
    .sort(["nu_ano", "sem_pri"])
)
print(epi)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Dengue/Chikungunya (fichas, dicionários e preenchimento)**: https://portalsinan.saude.gov.br/sinan-dengue-chikungunya e https://portalsinan.saude.gov.br/images/documentos/Agravos/Dengue/DIC_DADOS_ONLINE.pdf
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS) e Portaria GM/MS nº 10.175/2026 (atualização da Lista Nacional)
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulos de dengue e de arboviroses
