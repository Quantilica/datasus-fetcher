# `sinan-pneu` — Pneumoconioses Relacionadas ao Trabalho (SINAN)

Notificações de pneumoconioses — doenças respiratórias causadas pela inalação de poeiras minerais ou orgânicas no ambiente de trabalho — registradas no SINAN. Cada linha representa uma ficha de investigação de um caso de pneumoconiose ocupacional.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-pneu` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido) |
| **Particionamento** | `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2006 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 21 arquivos (~377 KB) |
| **Arquivos preliminares** | Sim (diretório PRELIM, 2023–2026; Finais até 2022) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

As pneumoconioses integram a lista de Doenças e Agravos Relacionados ao Trabalho (DART) de notificação compulsória no SUS, sob a coordenação da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) e operacionalização da RENAST/CEREST. A notificação compulsória decorre da Portaria MS nº 777/2004 e da Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V; Portaria GM/MS nº 217/2023).

O evento gerador é todo quadro de fibrose pulmonar ou doença respiratória causada pela inalação de poeiras minerais ou orgânicas, com destaque para asbestose (Amianto), silicose, pneumoconiose do trabalhador do carvão e pneumoconioses por poeiras mistas (CID-10 J60–J65). A exposição ocorre em mineração, construção civil, metalurgia, siderurgia, cerâmica, cimento e agricultura. A unidade de análise é o caso notificado (um registro por ficha), com ocupação (CBO), situação no mercado de trabalho e dados da empresa contratante (CNAE, CNPJ/CPF).

O instrumento é a *Ficha de Investigação — Pneumoconioses Relacionadas ao Trabalho*, que registra o tipo de pneumoconiose, o agente de exposição, o tempo de exposição, os exames (radiografia de tórax segundo a classificação OIT/BI-RADS de pneumoconiose, espirometria) e a conduta. A série no FTP inicia em 2006; os dados de 2023 em diante estão em PRELIM e sujeitos a revisão.

Principais usos: vigilância de pneumoconioses por ramo (CNAE) e ocupação (CBO), monitoramento de programas de proteção respiratória, apoio à caracterização de nexo para fins previdenciários e embasamento de ações de VISAT e de restrição/interdição de exposições.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `PNEU` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `PNEU` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `PNEUBR24.dbc`, em que `PNEU` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024, preliminar).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-pneu/<partição>/sinan-pneu_br_2006_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`DRT Pneumoconioses Relacionadas ao Trabalho`) é distribuído no Portal SINAN; não há PDF por agravo no FTP.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Os campos abaixo seguem o dicionário de dados do SINAN Net. A ficha é específica do agravo e os leiautes variam entre anos, portanto o conjunto exato de colunas deve ser conferido nos cabeçalhos do `.dbf` e no dicionário do ano. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `NU_NOTIFIC` | String | Número da notificação (identificador da ficha na unidade notificadora; preservar como texto). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado (J60–J65: pneumoconiose). |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `DT_SIN_PRI` / `DT_DIAG` | Data (AAAAMMDD) | Data dos primeiros sintomas / data do diagnóstico (agravo crônico: data do diagnóstico). |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | Inteiro | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE, 6 dígitos). |
| `ID_UNIDADE` | String | Código CNES da unidade de saúde notificadora (7 dígitos). |
| `DT_NASC` | Data (AAAAMMDD) | Data de nascimento. |
| `NU_IDADE_N` | Inteiro codificado | Idade no formato `TNNN` (unidade = hora/dia/mês/ano + 3 dígitos). |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `ID_OCUPA_N` | String | Ocupação (CBO 2002, 6 dígitos) do trabalhador. |
| `SIT_TRAB` | String | Situação no mercado de trabalho (1 a 12, 99 ignorado). |
| `CNAE` / `ATIV_ECO` | String | Atividade econômica da empresa contratante (CNAE). *Nome a conferir no dicionário.* |
| `TIPO_PNEU` | String | Tipo de pneumoconiose (asbestose, silicose, do carvão, poeiras mistas, outras). *Nome a conferir no dicionário.* |
| `AGENTE_EXP` | String | Agente de exposição (amianto, sílica, carvão, poeiras mistas, outros). |
| `TEMPO_EXP` | String | Tempo de exposição ao agente. |
| `RX_TORAX` | String | Resultado da radiografia de tórax (OIT: sugestivo de pneumoconiose). *Nome a conferir no dicionário.* |
| `CLASSI_FIN` | String | Classificação final (1 confirmado). |
| `EVOLUCAO` | String | Evolução do caso (cura, cura não confirmada, incapacidade temporária/parcial/total, óbito pela doença, óbito por outra causa, outro, ignorado). |
| `CAT` | String | Foi emitida a Comunicação de Acidente do Trabalho (CAT)? (1 sim, 2 não, 3 não se aplica, 9 ignorado). |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito, quando aplicável. |
| `DT_ENCERRA` | Data (AAAAMMDD) | Data de encerramento da investigação. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios (`ID_MUNICIP`, `ID_MN_RESI`) usam código IBGE de 6 dígitos; `ID_UNIDADE` é CNES de 7 dígitos; `SG_UF_NOT` é código IBGE de 2 dígitos. `ID_AGRAVO` (CID-10), `CBO`/`ID_OCUPA_N` (6 dígitos), `CNAE` (7 dígitos) e `NU_NOTIFIC` devem ficar como `String`, mantendo zeros à esquerda (`zfill`).
- **Datas e competências**: datas `DT_*` são gravadas em `AAAAMMDD` nos DBF e convertidas para `pl.Date`; `SEM_NOT` é semana epidemiológica `AAAASS` e permanece texto. A idade em `NU_IDADE_N` está codificada (`TNNN`) e deve ser decodificada antes de calcular faixas etárias.
- **Valores ausentes e sentinelas**: o SINAN usa `9`, `99`, `999` e `I` (ignorado) como categorias válidas; elas **não** são nulos automáticos. Espaços em branco e `""` viram nulos, e registros marcados como excluídos no dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: a latência longa e o nexo dependente de leitura radiológica padronizada (OIT) tornam a base pequena e sujeita a subnotificação; o tipo de pneumoconiose pode não ser codificado de forma padronizada entre anos. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. Arquivos do diretório PRELIM (2023+) são preliminares; deduplique por `NU_NOTIFIC` + `ID_UNIDADE` + `NU_ANO` ao combinar as duas fontes.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-pneu
quantilica datasus list sinan-pneu

# 2. Baixar microdados de sinan-pneu (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-pneu -o ./data --start 2015 --end 2022 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-pneu -o ./data --docs --aux --start 2015 --end 2022 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-pneu -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2022 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/PNEUBR22.dbc", dataset="sinan-pneu")

# Notificações por UF e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Tipos de pneumoconiose e agentes de exposição mais frequentes
print(frame.group_by("id_agravo").agg(pl.len().alias("n")).sort("n", descending=True).head())
print(frame.group_by("id_ocupa_n").agg(pl.len().alias("n")).sort("n", descending=True).head())
print(resumo.head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (DRT Pneumoconioses Relacionadas ao Trabalho): https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Saúde do Trabalhador: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- RENAST — Rede Nacional de Atenção Integral à Saúde do Trabalhador: https://www.gov.br/saude/pt-br/composicao/svsa/saude-do-trabalhador/renast
