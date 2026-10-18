# `sinan-acgr` — Acidente de trabalho

Notificações de acidentes de trabalho graves e fatais — aqueles que resultam em óbito, mutilação, internação ou que ocorrem com menores de 18 anos — registrados no SINAN. Cada linha representa uma ficha de investigação de acidente de trabalho, com dados do trabalhador, da empresa contratante e da lesão.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-acgr` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido) |
| **Particionamento** | `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2006 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 21 arquivos (~176,9 MB) |
| **Arquivos preliminares** | Sim (diretório PRELIM, 2023–2026; Finais até 2022) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

O agravo integra a vigilância em Saúde do Trabalhador do SUS, sob responsabilidade da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), operacionalizada pela Rede Nacional de Atenção Integral à Saúde do Trabalhador (RENAST) e pelos Centros de Referência em Saúde do Trabalhador (CEREST). A notificação compulsória foi estabelecida pela Portaria MS nº 777/2004 e consolidada na Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V).

O evento gerador é todo acidente de trabalho por causas não naturais (Capítulo XX da CID-10, V01 a Y98), típico ou de trajeto, que provoque lesão corporal ou perturbação funcional com perda/redução da capacidade para o trabalho, hospitalização ou morte. Consideram-se graves os acidentes fatais, com mutilações (poli traumatismos, amputações, esmagamentos, TCE, fratura de coluna, lesão medular, trauma visceral, eletrocussão, asfixia, queimaduras e aborto) e os ocorridos com menores de 18 anos. A unidade de análise é o trabalhador acidentado notificado (um registro por ficha), com o CID-10 da causa (V01–Y98) e o CID-10 da lesão registrados separadamente.

O instrumento é a *Ficha de Investigação — Acidente de Trabalho Grave* (CID-10 Y96), que cobre identificação, residência, antecedentes ocupacionais (CBO, situação no mercado de trabalho, tempo na ocupação), dados da empresa contratante (CNPJ/CPF, CNAE, terceirização), características do acidente (hora, horas após a jornada, local, tipo, veículo, outros trabalhadores atingidos) e conclusão (diagnóstico, regime de tratamento, evolução e CAT). A série no FTP inicia em 2006, no bojo da implantação nacional do SINAN Net; dados de 2023 em diante estão em PRELIM e sujeitos a revisão.

Principais usos: incidência e mortalidade por acidentes de trabalho graves, análise por ramo de atividade econômica (CNAE) e ocupação (CBO), avaliação da emissão de CAT, identificação de setores críticos para intervenção de VISAT (Vigilância em Saúde do Trabalhador) e apoio à rede sentinela.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ACGR` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ACGR` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `ACGRBR24.dbc`, em que `ACGR` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024, preliminar).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-acgr/<partição>/sinan-acgr_br_2006_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`, `Nota_Tecnica_Doenca_de_Creutzfeldt-Jakob(DCJ).pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`DRT Acidente Trabalho Grave`) é distribuído no Portal SINAN; não há PDF por agravo no FTP.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo `ACGRBR09.dbc` (leiaute do SINAN Net; fichas e leiautes podem variar entre anos, por isso a lista reflete esse arquivo). Os arquivos públicos não trazem identificadores individuais como número da notificação (`NU_NOTIFIC`) nem data de nascimento completa. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

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
| `DT_ACID` | Data (AAAAMMDD) | Data do acidente. |
| `SEM_ACID` | String | Semana epidemiológica do acidente (AAAASS). |
| `ANO_NASC` | String | Ano de nascimento (o arquivo público não traz a data de nascimento completa). |
| `NU_IDADE_N` | Inteiro | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade. |
| `SG_UF` | String | UF de residência (código IBGE de 2 dígitos). |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `ID_OCUPA_N` | String | Ocupação do trabalhador (CBO 2002, 6 dígitos). |
| `SIT_TRAB` | String | Situação no mercado de trabalho. |
| `LOCAL_ACID` | String | Local onde ocorreu o acidente. |
| `CNAE` | String | Atividade econômica da empresa contratante (CNAE). |
| `CNAE_PRIN` | String | CNAE da atividade principal da empresa. |
| `HORA_ACID` | String | Hora do acidente. |
| `MIN_ACID` | String | Minuto do acidente. |
| `HORA_JOR` | String | Hora da jornada de trabalho em que ocorreu o acidente. |
| `MIN_JOR` | String | Minuto da jornada de trabalho. |
| `UF_ACID` | String | UF de ocorrência do acidente. |
| `MUN_ACID` | String | Município de ocorrência do acidente. |
| `CID_ACID` | String | Código CID-10 da causa externa do acidente. |
| `TIPO_ACID` | String | Tipo de acidente (típico ou de trajeto). |
| `MAIS_TRAB` | String | Acidente atingiu mais de um trabalhador. |
| `NU_TRAB` | String | Número de trabalhadores atingidos. |
| `ATENDE_MED` | String | Houve atendimento médico. |
| `DT_ATENDE` | Data (AAAAMMDD) | Data do atendimento médico. |
| `UF_ATENDE` | String | UF da unidade de atendimento. |
| `MUN_ATENDE` | String | Município da unidade de atendimento. |
| `UNI_ATENDE` | String | Código CNES da unidade de atendimento. |
| `PART_CORP1` | String | Parte do corpo atingida (1ª). |
| `PART_CORP2` | String | Parte do corpo atingida (2ª). |
| `PART_CORP3` | String | Parte do corpo atingida (3ª). |
| `CID_LESAO` | String | Código CID-10 da lesão (diagnóstico). |
| `REGIME` | String | Regime de tratamento (hospitalar, ambulatorial ou ambos). |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito, quando aplicável. |
| `CAT` | String | Foi emitida a Comunicação de Acidente do Trabalho (CAT)? |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios (`ID_MUNICIP`, `ID_MN_RESI`) usam código IBGE de 6 dígitos; `ID_UNIDADE` é CNES de 7 dígitos; `SG_UF_NOT` é código IBGE de 2 dígitos. `ID_AGRAVO` (CID-10), `ID_OCUPA_N` (CBO 2002, 6 dígitos), `CNAE`, devem ficar como `String`, mantendo zeros à esquerda (`zfill`).
- **Datas e competências**: datas `DT_*` são gravadas em `AAAAMMDD` nos DBF e convertidas para `pl.Date`; `SEM_NOT` é semana epidemiológica `AAAASS` e permanece texto. A idade em `NU_IDADE_N` está codificada (`TNNN`) e deve ser decodificada antes de calcular faixas etárias.
- **Valores ausentes e sentinelas**: o SINAN usa `9`, `99`, `999` e `I` (ignorado) como categorias válidas; elas **não** são nulos automáticos. Espaços em branco e `""` viram nulos, e registros marcados como excluídos no dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: este dataset cobre apenas acidentes graves/fatais; acidentes com material biológico estão em `sinan-acbi` e acidentes leves não são notificados no SINAN. O `CID_ACID` (causa, V01–Y98) não deve ser confundido com o diagnóstico da lesão (campo de diagnóstico, CID-10 de lesão). Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. Arquivos do diretório PRELIM (2023+) são preliminares; como `NU_NOTIFIC` não consta dos arquivos públicos, deduplique por combinação de campos (ex.: `ID_UNIDADE`, `DT_NOTIFIC`, `ID_MN_RESI`, `ANO_NASC`, `CS_SEXO`) ao combinar as duas fontes.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-acgr
quantilica datasus list sinan-acgr

# 2. Baixar microdados de sinan-acgr (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-acgr -o ./data --start 2020 --end 2022 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-acgr -o ./data --docs --aux --start 2020 --end 2022 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-acgr -o ./data/raw --parquet-dir ./data/parquet --start 2020 --end 2022 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/ACGRBR22.dbc", dataset="sinan-acgr")

# Notificações por UF e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Tipos de acidente e evolução
print(frame.group_by("tipo_acid").agg(pl.len().alias("n")).sort("n", descending=True))
print(frame.group_by("evolucao").agg(pl.len().alias("n")).sort("n", descending=True))
print(resumo.head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (DRT Acidente de Trabalho Grave): https://portalsinan.saude.gov.br/drt-acidente-de-trabalho-grave
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Saúde do Trabalhador: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- RENAST — Rede Nacional de Atenção Integral à Saúde do Trabalhador: https://www.gov.br/saude/pt-br/composicao/svsa/saude-do-trabalhador/renast
