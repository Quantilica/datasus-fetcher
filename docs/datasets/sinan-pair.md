# `sinan-pair` — Perda auditiva por ruído relacionado ao trabalho

Notificações de Perda Auditiva Induzida por Ruído (PAIR) relacionada ao trabalho, registradas no SINAN. Cada linha representa uma ficha de investigação de um caso de hipoacusia neurossensorial causada pela exposição ocupacional a níveis elevados de pressão sonora.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-pair` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido) |
| **Particionamento** | `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2006 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 21 arquivos (~585 KB) |
| **Arquivos preliminares** | Sim (diretório PRELIM, 2023–2026; Finais até 2022) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A PAIR integra a lista de Doenças e Agravos Relacionados ao Trabalho (DART) de notificação compulsória no SUS, sob a coordenação da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) e operacionalização da RENAST/CEREST. A notificação compulsória decorre da Portaria MS nº 777/2004 e da Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V; Portaria GM/MS nº 217/2023).

O evento gerador é a perda auditiva neurossensorial, geralmente bilateral, irreversível e gradual, causada pela exposição continuada a níveis elevados de ruído no ambiente de trabalho (CID-10 H83.3, com quadros classificáveis em H90–H91). É uma das doenças ocupacionais mais prevalentes no Brasil, associada a setores como metalurgia, têxtil, construção civil, mineração e agroindústria. A unidade de análise é o caso notificado (um registro por ficha), com ocupação (CBO), situação no mercado de trabalho e dados da empresa contratante (CNAE, CNPJ/CPF).

O instrumento é a *Ficha de Investigação — Perda Auditiva Induzida por Ruído*, que registra a exposição a ruído (tempo de exposição, uso de proteção auditiva), a avaliação audiológica (audiometria, limiares por frequência, classificação de Schilling/NR-7) e a conduta. A série no FTP inicia em 2006; os dados de 2023 em diante estão em PRELIM e sujeitos a revisão.

Principais usos: monitoramento de PAIR por ramo (CNAE) e ocupação (CBO), avaliação de programas de conservação auditiva (PCA), apoio à caracterização de nexo para fins previdenciários e embasamento de ações de VISAT e de interdição/intervenção em ambientes ruidosos.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `PAIR` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `PAIR` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `PAIRBR24.dbc`, em que `PAIR` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024, preliminar).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-pair/<partição>/sinan-pair_br_2006_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`DRT Perda Auditiva Induzida por Ruído`) é distribuído no Portal SINAN; não há PDF por agravo no FTP.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo `PAIRBR26.dbc` (leiaute do SINAN Net; fichas e leiautes podem variar entre anos, por isso a lista reflete esse arquivo). Os arquivos públicos não trazem identificadores individuais como número da notificação (`NU_NOTIFIC`) nem data de nascimento completa. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (registro da ficha de notificação individual). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado. |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | String | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE). |
| `ID_UNIDADE` | String | Código CNES da unidade de saúde notificadora (7 dígitos). |
| `DT_DIAG` | Data (AAAAMMDD) | Data do diagnóstico. |
| `SEM_DIAG` | String | Semana epidemiológica do diagnóstico (AAAASS). |
| `ANO_NASC` | String | Ano de nascimento (o arquivo público não traz a data de nascimento completa). |
| `NU_IDADE_N` | Inteiro | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade. |
| `SG_UF` | String | UF de residência (código IBGE de 2 dígitos). |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `ID_OCUPA_N` | String | Ocupação do trabalhador (CBO 2002, 6 dígitos). |
| `SIT_TRAB` | String | Situação no mercado de trabalho. |
| `CNAE` | String | Atividade econômica da empresa contratante (CNAE). |
| `HIPERTEN` | String | Doença preexistente: hipertensão. |
| `TUBE` | String | Doença preexistente: tuberculose. |
| `DIABETES` | String | Doença preexistente: diabetes. |
| `ASMA` | String | Doença preexistente: asma. |
| `HANSENIASE` | String | Doença preexistente: hanseníase. |
| `MENTAL` | String | Doença preexistente: transtorno mental. |
| `OUT_AGRAVO` | String | Doença preexistente: outro agravo (descrição em `AGRAVO_DES`). |
| `TPRUIDO` | String | Tipo de ruído a que o trabalhador é exposto. |
| `SOLVENTE` | String | Exposição a solventes. |
| `GASES` | String | Exposição a gases. |
| `METAL` | String | Exposição a metais. |
| `MEDICA` | String | Uso de medicamentos ototóxicos. |
| `RUIDO_OUT` | String | Outra exposição (descrição em `RUI_OUTDES`). |
| `ZUMBIDO` | String | Sintoma: zumbido. |
| `CEFALEIA` | String | Sintoma: cefaleia. |
| `TONTURA` | String | Sintoma: tontura. |
| `FALA` | String | Sintoma: alteração da fala/comunicação. |
| `OUTRO_SIN` | String | Outro sintoma. |
| `DIAG_ESP` | String | Diagnóstico específico (CID-10). |
| `AFASTAMENT` | String | Houve afastamento do trabalho. |
| `TRAB_DOE` | String | Outros trabalhadores com a mesma doença no local de trabalho. |
| `AFAST_RISC` | String | Conduta: afastamento do local de risco. |
| `INDIVIDUAL` | String | Conduta: ação individual. |
| `MUDA_TRAB` | String | Conduta: mudança de função/posto de trabalho. |
| `NENHUM` | String | Conduta: nenhuma ação. |
| `COLETIVA` | String | Conduta: ação coletiva. |
| `AFAST_TRAB` | String | Conduta: afastamento do trabalho. |
| `CONDUTA` | String | Conduta adotada (marcação geral da ficha). |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito, quando aplicável. |
| `CAT` | String | Foi emitida a Comunicação de Acidente do Trabalho (CAT)? |
| `AGRAVO_DES` | String | Descrição textual de outro agravo preexistente. |
| `CONDUTA_DE` | String | Descrição textual de outra conduta. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios (`ID_MUNICIP`, `ID_MN_RESI`) usam código IBGE de 6 dígitos; `ID_UNIDADE` é CNES de 7 dígitos; `SG_UF_NOT` é código IBGE de 2 dígitos. `ID_AGRAVO` (CID-10), `ID_OCUPA_N` (CBO 2002, 6 dígitos), `CNAE`, devem ficar como `String`, mantendo zeros à esquerda (`zfill`).
- **Datas e competências**: datas `DT_*` são gravadas em `AAAAMMDD` nos DBF e convertidas para `pl.Date`; `SEM_NOT` é semana epidemiológica `AAAASS` e permanece texto. A idade em `NU_IDADE_N` está codificada (`TNNN`) e deve ser decodificada antes de calcular faixas etárias.
- **Valores ausentes e sentinelas**: o SINAN usa `9`, `99`, `999` e `I` (ignorado) como categorias válidas; elas **não** são nulos automáticos. Espaços em branco e `""` viram nulos, e registros marcados como excluídos no dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: a notificação da PAIR depende fortemente da existência de programas de conservação auditiva e de serviços de medicina do trabalho, com subnotificação elevada e longos períodos de latência; os limiares audiométricos detalhados não estão no SINAN e podem exigir a fonte original (ficha/laudo). Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. Arquivos do diretório PRELIM (2023+) são preliminares; como `NU_NOTIFIC` não consta dos arquivos públicos, deduplique por combinação de campos (ex.: `ID_UNIDADE`, `DT_NOTIFIC`, `ID_MN_RESI`, `ANO_NASC`, `CS_SEXO`) ao combinar as duas fontes.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-pair
quantilica datasus list sinan-pair

# 2. Baixar microdados de sinan-pair (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-pair -o ./data --start 2015 --end 2022 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-pair -o ./data --docs --aux --start 2015 --end 2022 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-pair -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2022 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/PAIRBR22.dbc", dataset="sinan-pair")

# Notificações por UF e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Ocupações mais afetadas e uso de proteção auditiva
print(frame.group_by("id_ocupa_n").agg(pl.len().alias("n")).sort("n", descending=True).head())
print(frame.group_by("tpruido").agg(pl.len().alias("n")).sort("n", descending=True))
print(resumo.head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (DRT Perda Auditiva Induzida por Ruído): https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Saúde do Trabalhador: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- RENAST — Rede Nacional de Atenção Integral à Saúde do Trabalhador: https://www.gov.br/saude/pt-br/composicao/svsa/saude-do-trabalhador/renast
