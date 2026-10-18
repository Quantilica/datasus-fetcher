# `sinan-ment` — Transtornos Mentais Relacionados ao Trabalho (SINAN)

Notificações de transtornos mentais e do comportamento relacionados ao trabalho, registradas no SINAN. Cada linha representa uma ficha de investigação de um caso de sofrimento ou adoecimento mental associado a fatores psicossociais e organizacionais do trabalho.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-ment` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido) |
| **Particionamento** | `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2006 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 21 arquivos (~1,9 MB) |
| **Arquivos preliminares** | Sim (diretório PRELIM, 2023–2026; Finais até 2022) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

Os transtornos mentais relacionados ao trabalho (TMRT) integram a lista de Doenças e Agravos Relacionados ao Trabalho (DART) de notificação compulsória no SUS, sob a coordenação da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) e operacionalização da RENAST/CEREST. A notificação compulsória decorre da Portaria MS nº 777/2004 e da Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V; Portaria GM/MS nº 217/2023).

O evento gerador é todo transtorno mental (CID-10 F00–F99), bem como os códigos Z73.0 (esgotamento/burnout), R40–R46 (alterações do comportamento e sintomas) e Z55–Z65 (problemas relacionados a circunstâncias socioeconômicas e psicossociais), quando relacionados ao trabalho. A causalidade é multifatorial e mediada por fatores psicossociais (sobrecarga, assédio, metas abusivas, jornadas exaustivas, violência no trabalho). A unidade de análise é o caso notificado (um registro por ficha), com ocupação (CBO), situação no mercado de trabalho, tempo de exposição e dados da empresa contratante (CNAE, CNPJ/CPF).

O instrumento é a *Ficha de Investigação — Transtornos Mentais Relacionados ao Trabalho*, que registra a relação do agravo com o trabalho, o nexo (referido ou comprovado), condições de trabalho e organização (como exposição a situações de violência, pressão, monotonia, jornada), sinais e sintomas e uso de substâncias. A série no FTP inicia em 2006; os dados de 2023 em diante estão em PRELIM e sujeitos a revisão.

Principais usos: vigilância de TMRT por ramo (CNAE) e ocupação (CBO), monitoramento de afastamentos e incapacidades por sofrimento mental, identificação de setores com riscos psicossociais elevados (bancários, teleatendimento, saúde, educação, segurança pública) e base para ações de VISAT e de reabilitação profissional.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `MENT` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `MENT` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `MENTBR24.dbc`, em que `MENT` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024, preliminar).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-ment/<partição>/sinan-ment_br_2006_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`DRT Transtornos Mentais Relacionados ao Trabalho`) é distribuído no Portal SINAN; não há PDF por agravo no FTP.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Os campos abaixo seguem o dicionário de dados do SINAN Net. A ficha é específica do agravo e os leiautes variam entre anos, portanto o conjunto exato de colunas deve ser conferido nos cabeçalhos do `.dbf` e no dicionário do ano. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `NU_NOTIFIC` | String | Número da notificação (identificador da ficha na unidade notificadora; preservar como texto). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado (transtorno mental relacionado ao trabalho). |
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
| `NEXO_TRAB` | String | Relação do agravo com o trabalho (1 sim, 2 não, 9 ignorado) / nexo referido ou comprovado. |
| `TEMPO_EXP` | String | Tempo de exposição à situação de risco. |
| `USO_SUBST` | String | Uso de substância psicoativa (1 álcool, 2 outras drogas, 3 álcool e outras, 4 não, 9 ignorado). *Nome a conferir no dicionário.* |
| `CLASSI_FIN` | String | Classificação final (1 confirmado). |
| `EVOLUCAO` | String | Evolução do caso (cura, cura não confirmada, incapacidade temporária/parcial/total, óbito pela doença, óbito por outra causa, outro, ignorado). |
| `CAT` | String | Foi emitida a Comunicação de Acidente do Trabalho (CAT)? (1 sim, 2 não, 3 não se aplica, 9 ignorado). |
| `DT_ENCERRA` | Data (AAAAMMDD) | Data de encerramento da investigação. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios (`ID_MUNICIP`, `ID_MN_RESI`) usam código IBGE de 6 dígitos; `ID_UNIDADE` é CNES de 7 dígitos; `SG_UF_NOT` é código IBGE de 2 dígitos. `ID_AGRAVO` (CID-10), `CBO`/`ID_OCUPA_N` (6 dígitos), `CNAE` (7 dígitos) e `NU_NOTIFIC` devem ficar como `String`, mantendo zeros à esquerda (`zfill`).
- **Datas e competências**: datas `DT_*` são gravadas em `AAAAMMDD` nos DBF e convertidas para `pl.Date`; `SEM_NOT` é semana epidemiológica `AAAASS` e permanece texto. A idade em `NU_IDADE_N` está codificada (`TNNN`) e deve ser decodificada antes de calcular faixas etárias.
- **Valores ausentes e sentinelas**: o SINAN usa `9`, `99`, `999` e `I` (ignorado) como categorias válidas; elas **não** são nulos automáticos. Espaços em branco e `""` viram nulos, e registros marcados como excluídos no dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: o estabelecimento do nexo causal é o ponto mais sensível da ficha e a subnotificação é alta, com grande variação entre estados e entre serviços de saúde; muitos casos são classificados com Z-codes. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. Arquivos do diretório PRELIM (2023+) são preliminares; deduplique por `NU_NOTIFIC` + `ID_UNIDADE` + `NU_ANO` ao combinar as duas fontes.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-ment
quantilica datasus list sinan-ment

# 2. Baixar microdados de sinan-ment (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-ment -o ./data --start 2015 --end 2022 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-ment -o ./data --docs --aux --start 2015 --end 2022 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-ment -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2022 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/MENTBR22.dbc", dataset="sinan-ment")

# Notificações por UF e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Nexo com o trabalho e principais CIDs notificados
print(frame.group_by("nexo_trab").agg(pl.len().alias("n")).sort("n", descending=True))
print(frame.group_by("id_agravo").agg(pl.len().alias("n")).sort("n", descending=True).head())
print(resumo.head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (DRT Transtornos Mentais Relacionados ao Trabalho): https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Saúde do Trabalhador: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- RENAST — Rede Nacional de Atenção Integral à Saúde do Trabalhador: https://www.gov.br/saude/pt-br/composicao/svsa/saude-do-trabalhador/renast
