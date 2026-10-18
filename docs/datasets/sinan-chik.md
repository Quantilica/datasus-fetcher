# `sinan-chik` — Febre de Chikungunya

O `sinan-chik` contém os microdados das notificações e investigações epidemiológicas de casos de Febre de Chikungunya (CID-10 A92.0) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de chikungunya, digitada no SINAN Net/Sinan Online pelas unidades notificadoras. A base cobre a experiência brasileira completa da doença, pois os primeiros casos autóctones do país foram detectados em 2014, marco inicial da série no FTP.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-chik` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (consolidação final por ano, com atualizações em `PRELIM`) |
| **Cobertura temporal no FTP** | 2014 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 13 arquivos (~95 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A febre de Chikungunya é transmitida pelos mosquitos `Aedes aegypti` e `Aedes albopictus`, causada pelo arbovírus CHIKV (família Togaviridae, gênero Alphavirus). A vigilância do agravo é gerida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), que coordena a resposta a epidemias com picos massivos nas regiões Nordeste e Sudeste. O agravo passou a ser de notificação compulsória a partir da introdução no país em 2014 e está consolidado na Portaria GM/MS nº 204/2016. O dataset é o insumo oficial para coeficientes de incidência, letalidade e monitoramento da fase crônica da doença.

O evento gerador é a **Ficha de Notificação de Conclusão de Febre de Chikungunya do SINAN**, implantada em 2014 e, desde 2016, unificada com a ficha de dengue (`Ficha_DENGCHIK`, SVS 14/03/2016) e a possibilidade de registro do campo `ID_AGRAVO` com "2-Chikungunya" (A92.0). Com isso, um mesmo leiaute DBF abriga dengue e chikungunya, sendo nécessaire filtrar o agravo para isolar os casos de chikungunya. A unidade de análise é o caso suspeito/confirmado notificado individualmente (a definição de caso suspeito envolve febre e artralgia intensa de início agudo em área com transmissão).

A série histórica registra as fases do SINAN: notificação inicial pela ficha específica de 2014 e, de 2016 em diante, o mesmo instrumento unificado do Sinan Online (fases do sistema: 2000-2006 SINAN-Windows, 2007-2013 SINAN Net, 2014+ SINAN Net/Online). A introdução do vírus ocorreu em 2014 (primeiros casos autóctones na região Norte/Nordeste) e as regiões tropicais rapidamente concentraram os maiores números; episódios epidêmicos posteriores ressaltaram a carga de artralgia crônica incapacitante e seus impactos sobre a produtividade e a rede assistencial.

Aplicações analíticas: coeficiente de incidência anual por 100 mil habitantes, proporção de casos com artralgias crónicas, letalidade da fase aguda, distribuição por faixa de idade/sexo, monitoramento de coinfecções com dengue e zika no mesmo território, e avaliação da incorporação da vacina contra chikungunya em territórios prioritários.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `CHIK` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `CHIK` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `CHIKBR14.dbc` — prefixo `CHIK`, `BR` (consolidação nacional) e `14` (ano 2014, primeiro da série) até `CHIKBR25.dbc` (2025); o ano corrente fica em `PRELIM` (ex.: `CHIKBR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-chik/<ano>/sinan-chik_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-chik/2025/sinan-chik_2025-br@20261013.dbc`; o arquivo preliminar é nomeado com o sufixo do dataset `-preliminar`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (dicionários e tabulações do Sinan Net/Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominador populacional).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual para casos de chikungunya) |
| `ID_AGRAVO` | String | Agravo na ficha unificada — identifica a suspeição de chikungunya (A92.0) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade de saúde notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (febre de início súbito + artralgia intensa) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação (obrigatório, >= data de notificação) |
| `CLASSI_FIN` | Inteiro | Classificação final: 5 - Descartado, 13 - Chikungunya (ficha unificada) |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte (1 - Laboratório, 2 - Clínico Epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 4 - Óbito em investigação, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP`/`ID_MN_RESI` (IBGE 6-7 dígitos) e `ID_UNIDADE` (CNES) como `String` com `zfill`; nunca converter códigos de classificação (`CLASSI_FIN`, `CRITERIO`, `EVOLUCAO`) para numérico antes do mapeamento de rótulos.
- **Datas e competências**: `DT_NOTIF`, `DT_SIN_PRI`, `DT_INVEST`, `DT_OBITO` e `DT_ENCERRA` em `AAAAMMDD` no DBF, convertidos para `pl.Date`; semanas (`SEM_NOT`, `SEM_PRI`) permanecem inteiras (formato `AAAASS`).
- **Valores ausentes e sentinelas**: códigos ignorados (`9`, `99`, `999999`, `99999999`), datas `00000000` e cadenas em branco tratados como nulo por `SENTINEL_NULLS`; registros com marcador de exclusão dBASE (`_deleted`) são descartados.
- **Particularidades do dataset**: há transição de leiaute de ficha — entre 2014 e 2015 a notificação usa a ficha específica de chikungunya e, a partir de 2016, a ficha unificada Dengue/Chikungunya (casos notificados pelo instrumento antigo têm os campos novos de investigação preenchidos com categorias padrão, como 2 - Não); o volume é alto e concentrado em 13 consolidações `BR` anuais, com o arquivo do ano corrente em `PRELIM` ainda sujeito a revisão; a filtragem por `ID_AGRAVO`/`CLASSI_FIN` é obrigatória para separar chikungunya de dengue no mesmo leiaute.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-chik
quantilica datasus list sinan-chik

# 2. Baixar microdados de sinan-chik com recorte adequado à partição do dataset
quantilica datasus sync sinan-chik -o ./data --start 2015 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-chik -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-chik -o ./data/raw --parquet-dir ./data/parquet --start 2015
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Lê o arquivo consolidado de chikungunya já tratado
qdf = read_dbc("data/sinan-chik/2025/sinan-chik_2025-br@20261013.dbc", clean=True)

# Casos confirmados de febre de Chikungunya por ano e UF
confirmados = qdf.filter(pl.col("classi_fin") == 13)
resumo = (
    confirmados.group_by("nu_ano", "sg_uf_not")
    .len()
    .sort(["nu_ano", "sg_uf_not"])
)
print(resumo)

# Letalidade: proporção de casos confirmados que evoluíram para óbito pelo agravo
letalidade = confirmados.group_by("nu_ano").agg(
    n=pl.len(),
    obitos=(pl.col("evolucao") == 2).sum(),
)
print(letalidade.with_columns( (pl.col("obitos") / pl.col("n")).alias("let") ))
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Dengue/Chikungunya**: https://portalsinan.saude.gov.br/sinan-dengue-chikungunya
- **Ficha e dicionário de dados da ficha unificada**: https://portalsinan.saude.gov.br/images/documentos/Agravos/Dengue/Ficha_DENGCHIK_FINAL.pdf
- **Portaria GM/MS nº 204/2016** (notificação compulsória) e **Guia de Vigilância em Saúde** (SVSA/MS, capítulo de chikungunya)
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
