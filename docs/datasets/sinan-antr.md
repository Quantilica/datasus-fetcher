# `sinan-antr` — Atendimento Antirrábico

O `sinan-antr` contém os microdados dos atendimentos antirrábicos humanos registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação de um atendimento antirrábico humano (CID-10 W64 — "exposição a vírus da raiva"), a ficha de "acidente por animal potencialmente transmissor de raiva" ou de atendimento profilático, digitado no SINAN Net/Sinan Online pelas unidades de saúde que prestam o atendimento. O agravo é de notificação compulsória: todo acidente por animal potencialmente transmissor da raiva deve ser notificado, independentemente da indicação de vacina ou soro.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-antr` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 2006 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 21 arquivos (~513 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

O atendimento antirrábico é a ponta do programa de profilaxia da raiva humana, gerido pela SVSA/MS: todo acidente com animal potencialmente transmissor da raiva (mordedura, arranhadura, lambedura) tem notificação compulsória (Portaria SVS/MS nº 104/2011; Portaria de Consolidação GM/MS nº 204/2016), inclusive acidentes em que o animal é cão ou gato em observação. A sistemática substituiu o antigo SISANTO (sistema dedicado de atendimento antirrábico) e atualmente é alimentada pela **Ficha de Investigação Atendimento Antirrábico Humano** do SINAN (ficha `anti_rabico_v5`, com dicionário `DIC_DADOS_anti_rabico_v5.1`). O volume é alto em todas as UFs — dezenas de milhares de atendimentos anuais — porque envolve profilaxia pré-exposição (vacinadores de produtos animais) e pós-exposição de todo o território.

O evento gerador é a ficha de atendimento antirrábico humano, composta pelo bloco de notificação individual (dados gerais padrão do SINAN) e por dados complementares: tipo de exposição (mordedura, arranhadura, lambedura, contato indireto), localização do ferimento, animal agressor (espécie, passível de observação, situação final do animal após o período observado), tratamento indicado (1 - Pré-exposição, 2 - Dispensa de tratamento, 3 - Observação do animal, 4/5/6 - Soro, vacina, soro + vacina, 7 - Reexposição), doses aplicadas, laboratório produtor da vacina/soro e evento adverso. A unidade de análise é o atendimento/notificação individual — não o caso de raiva humana (que deve estudado no dataset `sinan-raiv`).

A implantação no SINAN data das décadas (dados liberalizados de 2006 em diante no FTP com a base nacional `BR`); a migração do SISANTO para o SINAN consolidou o registro único entre atendimento profilático pós-exposição e pré-exposição, com acompanhamento do esquema profilático por ficha ou transferência vertical entre atendimentos do mesmo paciente.

Aplicações analíticas: volume e distribuição de atendimentos antirrábicos por UF/município, perfil de exposição (tipo de exposição, espécie de animal agressor, condição do animal), razões de esquema aplicado vs. indicado, doses aplicadas e eventos adversos, monitoramento da vigilância passiva (animais observados), e análise de integração com epizootias e casos humanos de raiva (`sinan-raiv`).

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ANTR` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ANTR` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `ANTRBR06.dbc` — prefixo `ANTR`, `BR` (consolidação nacional) e `06` (ano 2006, início da série disponível), até `ANTRBR24.dbc` (2024); os anos recentes ficam em `PRELIM` (ex.: `ANTRBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-antr/<ano>/sinan-antr_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-antr/2020/sinan-antr_2020-br@20260611.dbc`; arquivos preliminares recebem o sufixo `-preliminar`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Atendimento Antirrábico Humano — CID-10 W64) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora/unidade de atendimento |
| `DT_ATEND` | Data (`AAAAMMDD`) | Data do atendimento (primeiro atendimento antirrábico) |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `ID_OCUPA_C` | String (6) | Ocupação do paciente, em código CBO (atividades de risco, ex.: profissionais de zoonoses e veterinária) |
| `ID_MN_RESI` | String (6/7) | Município de residência do paciente (IBGE) |
| `SG_UF_ATEND` | String (2) | UF da unidade de atendimento antirrábico |
| `CLASSI_FIN` | Inteiro | Classificação final/condição (conforme dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação/despistos quando aplicável |
| `EVOLUCAO` | Inteiro | Evolução/desfecho do atendimento (conforme dicionário do agravo) |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: manter `ID_MUNICIP`, `ID_MN_RESI` (IBGE 6/7 dígitos), `ID_UNIDADE` (CNES) e `ID_OCUPA_C` (CBO) como texto com `zfill`; códigos de tratamento (pré/pós-exposição, soro/vacina) e espécie do animal agressor mapeados como categóricos apenas ao fim do saneamento.
- **Datas e competências**: `DT_NOTIF`, `DT_ATEND` e `DT_ENCERRA` em `AAAAMMDD` convertidos para `pl.Date`; semanas epidemiológicas permanecem inteiras.
- **Valores ausentes e sentinelas**: células em branco, datas `00000000`, códigos `9`/`99`/`999999`/`99999999` normalizados para nulo por `SENTINEL_NULLS`; registros com marcador de exclusão dBASE (`_deleted`) descartados.
- **Particularidades do dataset**: volume muito alto (21 consolidações anuais, ~513 MB) — atenção ao registro múltiplo de fichas do mesmo paciente ao longo do esquema profilático (a mesma pessoa pode ter vários atendimentos; use `NU_NOTIFIC`, a transferência vertical de lote e `DT_NOTIF` para ordenação); o esquema pode ser interrompido/encerrado antes do fim (ex.: animal observado sadio após 90 dias); cães e gatos em observação geram atendimentos de observação/dispensa sem aplicação de vacina; partes consideráveis dos registros misturam profilaxia pré-exposição (ocupacional) com pós-exposição, que exigem tratamento distinto nas análises.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-antr
quantilica datasus list sinan-antr

# 2. Baixar microdados de sinan-antr com recorte adequado à partição do dataset
quantilica datasus sync sinan-antr -o ./data --start 2010 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-antr -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-antr -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de atendimentos antirrábicos já tratado
qdf = read_dbc("data/sinan-antr/2020/sinan-antr_2020-br@20260611.dbc", clean=True)

# Volume de atendimentos por ano e UF
print(
    qdf.group_by("nu_ano", "sg_uf_not")
    .len()
    .sort(["nu_ano", "sg_uf_not"])
)

# Distribuição por município de residência mais frequente
print(
    qdf.group_by("id_mn_resi")
    .len()
    .sort("len", descending=True)
    .head(20)
)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Atendimento Antirrábico (ficha, instrucional, dicionário)**: https://portalsinan.saude.gov.br/atendimento-antirrabico
- **Ficha de Investigação Atendimento Antirrábico Humano (anti_rabico_v5)**: http://portalsinan.saude.gov.br/images/documentos/Agravos/Atendimento%20Anti-rabico/anti_rabico_v5.pdf
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo raiva / profilaxia antirrábica
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
