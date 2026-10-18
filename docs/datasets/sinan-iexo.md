# `sinan-iexo` — Intoxicação Exógena

Notificações de intoxicações exógenas por agentes químicos, medicamentos, drogas de abuso, metais, agrotóxicos e outros, registradas no SINAN. Cada linha representa uma ficha de investigação de um caso de intoxicação por substância exógena, incluindo exposições ocupacionais, acidentais e intencionais.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-iexo` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido) |
| **Particionamento** | `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2006 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 21 arquivos (~200,0 MB) |
| **Arquivos preliminares** | Sim (diretório PRELIM, 2023–2026; Finais até 2022) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A intoxicação exógena é agravo de notificação compulsória na Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V; Portaria GM/MS nº 217/2023), sob a coordenação da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS). Quando relacionada ao trabalho, integra também a lista de Doenças e Agravos Relacionados ao Trabalho (DART), sendo de investigação obrigatória pelos CEREST/RENAST; a notificação ocupacional decorre da Portaria MS nº 777/2004.

O evento gerador é todo quadro de intoxicação resultante da exposição a substâncias químicas (medicamentos, agrotóxicos, metais, solventes, produtos de limpeza, drogas de abuso, substâncias usadas como arma química e outras), com CID-10 T36–T65 (destacando-se T65.9). A exposição pode ser aguda ou crônica e ocupacional ou não ocupacional. A unidade de análise é o caso notificado (um registro por ficha), com ocupação (CBO) e identificação da fonte de exposição.

O instrumento é a *Ficha de Investigação — Intoxicação Exógena*, que registra o grupo do agente tóxico, o princípio ativo, a via de exposição, a circunstância (habitual, ocupacional, acidental, intencional/suicida, uso de medicamento, abuso de drogas, ignorada), a classificação final (intoxicação confirmada, só exposição, reação adversa, surto), o critério de confirmação e a evolução (cura, óbito por intoxicação, óbito por outras causas, sequela). A série no FTP inicia em 2006; os dados de 2023 em diante estão em PRELIM e sujeitos a revisão.

Principais usos: vigilância de intoxicações ocupacionais por ramo (CNAE) e ocupação (CBO), monitoramento de agrotóxicos e de acidentes com produtos químicos, análise de tentativas de autoextermínio, vigilância de surtos e embasamento de ações de VISAT e de regulação de produtos.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `IEXO` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `IEXO` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `IEXOBR24.dbc`, em que `IEXO` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024, preliminar).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-iexo/<partição>/sinan-iexo_br_2006_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`, `Nota_Tecnica_Intoxicacao_Exogena.pdf` (nota técnica específica do agravo).
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`DRT Intoxicação Exógena` / IEXO) é distribuído no Portal SINAN; a nota técnica no FTP complementa as orientações de preenchimento.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo `IEXOBR07.dbc` (leiaute do SINAN Net; fichas e leiautes podem variar entre anos, por isso a lista reflete esse arquivo). Os arquivos públicos não trazem identificadores individuais como número da notificação (`NU_NOTIFIC`) nem data de nascimento completa. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

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
| `DT_SIN_PRI` | Data (AAAAMMDD) | Data dos primeiros sintomas. |
| `SEM_PRI` | String | Semana epidemiológica dos primeiros sintomas (AAAASS). |
| `ANO_NASC` | String | Ano de nascimento (o arquivo público não traz a data de nascimento completa). |
| `NU_IDADE_N` | Inteiro | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade. |
| `SG_UF` | String | UF de residência (código IBGE de 2 dígitos). |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `DT_INVEST` | Data (AAAAMMDD) | Data da investigação. |
| `ID_OCUPA_N` | String | Ocupação do trabalhador (CBO 2002, 6 dígitos). |
| `SIT_TRAB` | String | Situação no mercado de trabalho. |
| `LOC_EXPO` | String | Local de ocorrência da exposição (descrição de outros em `LOC_EXP_DE`). |
| `CNAE` | String | Atividade econômica da empresa contratante (CNAE). |
| `PAIS_EXP` | String | País de ocorrência da exposição. |
| `AGENTE_TOX` | String | Classificação do agente tóxico (grupo). |
| `COAGTOXMA1` | Inteiro | Código do agente tóxico (1º) segundo a tabela de agentes tóxicos. |
| `COAGTOXMA2` | Inteiro | Código do agente tóxico (2º). |
| `COAGTOXMA3` | Inteiro | Código do agente tóxico (3º). |
| `AGENTE_1` | String | Nome do agente tóxico (1º; texto livre). |
| `AGENTE_2` | String | Nome do agente tóxico (2º; texto livre). |
| `AGENTE_3` | String | Nome do agente tóxico (3º; texto livre). |
| `P_ATIVO_1` | String | Princípio ativo (1º; texto livre). |
| `P_ATIVO_2` | String | Princípio ativo (2º; texto livre). |
| `P_ATIVO_3` | String | Princípio ativo (3º; texto livre). |
| `UTILIZACAO` | String | Utilização do agente (descrição em `UTIL_DESC`). |
| `ATIVIDA_1` | String | Atividade relacionada à exposição (1ª). |
| `ATIVIDA_2` | String | Atividade relacionada à exposição (2ª). |
| `ATIVIDA_3` | String | Atividade relacionada à exposição (3ª). |
| `VIA_1` | String | Via de exposição (1ª). |
| `VIA_2` | String | Via de exposição (2ª). |
| `VIA_3` | String | Via de exposição (3ª). |
| `CIRCUNSTAN` | String | Circunstância da exposição/intoxicação (descrição de outras em `CIRCUN_DES`). |
| `DOENCA_TRA` | String | Doença relacionada ao trabalho. |
| `TPEXP` | String | Tipo de exposição (aguda, crônica etc.). |
| `TPATENDE` | String | Tipo de atendimento. |
| `HOSPITAL` | String | Hospitalização (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `DTINTERNA` | Data (AAAAMMDD) | Data da internação. |
| `UF_HOSP` | String | UF do hospital. |
| `MUN_HOSP` | String | Município do hospital. |
| `CLASSI_FIN` | String | Classificação final do caso. |
| `DIAG_CONF` | String | Diagnóstico confirmado (CID-10). |
| `CRITERIO` | String | Critério de confirmação. |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito, quando aplicável. |
| `CAT` | String | Foi emitida a Comunicação de Acidente do Trabalho (CAT)? |
| `DT_ENCERRA` | Data (AAAAMMDD) | Data de encerramento da investigação. |
| `LAVOURA` | String | Tipo de lavoura (texto livre). |
| `INTOX_CHUM` | String | Intoxicação por chumbo (marcação). |
| `INTOX_MERC` | String | Intoxicação por mercúrio (marcação). |
| `INTOX_META` | String | Intoxicação por outro metal (marcação). |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios (`ID_MUNICIP`, `ID_MN_RESI`) usam código IBGE de 6 dígitos; `ID_UNIDADE` é CNES de 7 dígitos; `SG_UF_NOT` é código IBGE de 2 dígitos. `ID_AGRAVO` (CID-10), `ID_OCUPA_N` (CBO 2002, 6 dígitos), `CNAE`, devem ficar como `String`, mantendo zeros à esquerda (`zfill`).
- **Datas e competências**: datas `DT_*` são gravadas em `AAAAMMDD` nos DBF e convertidas para `pl.Date`; `SEM_NOT` é semana epidemiológica `AAAASS` e permanece texto. A idade em `NU_IDADE_N` está codificada (`TNNN`) e deve ser decodificada antes de calcular faixas etárias.
- **Valores ausentes e sentinelas**: o SINAN usa `9`, `99`, `999` e `I` (ignorado) como categorias válidas; elas **não** são nulos automáticos. Espaços em branco e `""` viram nulos, e registros marcados como excluídos no dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: é uma das maiores bases do SINAN e inclui grande volume de casos não ocupacionais (medicamentos, tentativas de autoextermínio, acidentes domésticos); filtre por `CIRCUNSTAN`/`SIT_TRAB`/`CNAE` para análises ocupacionais. Os agentes tóxicos podem ser registrados com granularidade variável (nome do princípio ativo é texto livre, sujeito a inconsistências) e há múltiplos campos de agente. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. Arquivos do diretório PRELIM (2023+) são preliminares; como `NU_NOTIFIC` não consta dos arquivos públicos, deduplique por combinação de campos (ex.: `ID_UNIDADE`, `DT_NOTIFIC`, `ID_MN_RESI`, `ANO_NASC`, `CS_SEXO`) ao combinar as duas fontes.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-iexo
quantilica datasus list sinan-iexo

# 2. Baixar microdados de sinan-iexo (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-iexo -o ./data --start 2020 --end 2022 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-iexo -o ./data --docs --aux --start 2020 --end 2022 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-iexo -o ./data/raw --parquet-dir ./data/parquet --start 2020 --end 2022 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/IEXOBR22.dbc", dataset="sinan-iexo")

# Notificações por UF e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Circunstância da exposição e classificação final
print(frame.group_by("circunstan").agg(pl.len().alias("n")).sort("n", descending=True))
print(frame.group_by("classi_fin").agg(pl.len().alias("n")).sort("n", descending=True))
print(resumo.head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (Intoxicação Exógena): https://portalsinan.saude.gov.br/
- Nota Técnica sobre Intoxicação Exógena (FTP DATASUS, `/SINAN/DOCS`): `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DOCS/Nota_Tecnica_Intoxicacao_Exogena.pdf`
- Guia de Vigilância em Saúde (SVSA/MS): https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- RENAST — Rede Nacional de Atenção Integral à Saúde do Trabalhador: https://www.gov.br/saude/pt-br/composicao/svsa/saude-do-trabalhador/renast
