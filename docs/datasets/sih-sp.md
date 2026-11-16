---
dataset:
  id: sih-sp
  fonte: datasus
  titulo: SP - Serviços Profissionais
  resumo: 'SP - Serviços Profissionais do DATASUS: um serviço profissional (ato) lançado em uma AIH aprovada.'
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 1997-06
    fim: em-curso
  unidade: um serviço profissional (ato) lançado em uma AIH aprovada
  granularidade:
    espacial: estabelecimento (CNES) e município de residência do paciente; um arquivo por UF
    temporal: dia da internação e da saída; competência de processamento (mês)
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e competência mensal
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 41
  unidades_de_medida:
    sp_aa: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_mm: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_cgchosp: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_naih: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_procrea: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_dtinter: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_dtsaida: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_num_pr: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_tipo: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_cpfcgc: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_atoprof: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_tp_ato: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_qtd_ato: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_ptsp_nf: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_valato: R$ (reais)
    sequencia: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sp_qt_proc: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: sp_cpfcgc
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  eras:
  - desde: 2008-01
    mudanca: Tabela Unificada (SIGTAP) e novo diretório/leiaute (`200801_`)
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# SP - Serviços Profissionais (`sih-sp`)

## Resumo

`sih-sp` contém os **Serviços Profissionais** do SIH/SUS: cada linha é um ato profissional ou serviço (procedimento, quantidade e valor) lançado dentro de uma AIH aprovada, com o profissional/estabelecimento executor e o município do hospital e do paciente. Complementa o RD detalhando a composição do valor de serviços profissionais (`VAL_SP`) por AIH.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/SIHSUS/200801_/Doc`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SIHSUS/200801_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIHSUS/199201_200712/Dados` | `SP` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |
| `/dissemin/publicos/SIHSUS/200801_/Dados` | `SP` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `SPSP2401.dbc` — `SP` (Serviços Profissionais) + `SP` (UF) + `24` (ano) + `01` (mês de competência). Atenção: prefixo e UF podem coincidir (`SPSP…`), o que é esperado.
- **No armazenamento local do `datasus-fetcher`**: `data/sih-sp/<AAAAMM>/sih-sp_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sih-sp/202401/sih-sp_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/IT_SIHSUS_1603.pdf` (Informe Técnico do SIHSUS, 57 KB, 2016) é o dicionário oficial de variáveis; `Auxiliar/TAB_SIH.zip` (~6,1 MB, tabelas e conversores `.cnv`/`.def` atuais) e as versões históricas `TAB_SIH_199201-199712.zip`, `TAB_SIH_199801-200307.zip` e `TAB_SIH_200308-200712.zip` trazem as tabelas de procedimentos, CID e códigos usadas em cada fase.

## Conteúdo

O Sistema de Informações Hospitalares do SUS (SIH/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES), com processamento e disseminação a cargo do DATASUS — e tem como finalidade operacionalizar o pagamento das internações realizadas em hospitais públicos e privados conveniados ao SUS. Por ser um sistema de faturamento, cobre apenas a assistência financiada pelo SUS (não inclui saúde suplementar nem internações particulares) e é a principal fonte nacional para estudar morbidade hospitalar, perfil assistencial e gasto hospitalar.

O evento gerador são os **atos profissionais registrados na AIH** (cirurgias, anestesias, partos, consultas e outros procedimentos remunerados como serviço profissional, além de procedimentos especiais). A unidade de análise é o **ato/serviço profissional por AIH** — uma AIH pode ter dezenas de linhas, ligadas ao RD por `SP_NAIH` = `N_AIH`, `SP_CNES` = `CNES` e à competência. Cada hospital preenche a Autorização de Internação Hospitalar (AIH) e a remete mensalmente ao gestor municipal/estadual, que a valida e a envia ao DATASUS para processamento na competência (`ANO_CMPT`/`MES_CMPT`). O processamento classifica cada AIH como aprovada (arquivo RD), rejeitada (RJ/ER) e detalha os atos profissionais (SP).

O FTP traz o SP em duas séries (1992–2007 e 2008 em diante), com início efetivo do inventário em 1997-06. O arquivo é o maior do SIH (~57 GB para 9.466 arquivos), porque replica o detalhamento por ato. Com a Tabela Unificada/SIGTAP (2008) o campo `SP_ATOPROF` passou a usar códigos de procedimento de 10 dígitos e foram incluídos campos de complexidade (`SP_COMPLEX`), financiamento (`SP_FINANC`/`SP_CO_FAEC`) e CBO/documento do profissional (`SP_PF_CBO`, `SP_PF_DOC`).

Usos principais: análise do gasto com serviços profissionais por procedimento, especialidade (CBO) e hospital; produção por tipo de ato (cirurgias, partos, anestesia); verificação de pontos (`SP_PTSP`) e valor unitário dos atos; estudos de remuneração e de cobertura de especialidades; e reconciliação com `VAL_SP` do RD. Não contém dados clínicos do paciente além de `SP_CIDPRI`/`SP_CIDSEC` e das datas da AIH.

### Cobertura observada

- Índice do FTP (2026-10): 9492 arquivos, de 1997-06 a 2026-09, 27 UF(s) com arquivos, última atualização em 2026-11-10.
- Conversão local de amostras (5 arquivo(s) Parquet, de 1997-07 a 2026-08), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Eras

- **2008-01**: Tabela Unificada (SIGTAP) e novo diretório/leiaute (`200801_`)

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

37 colunas no arquivo de 2024-01 (`SPAC2401.dbc`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `SP_GESTOR` | String (6) | Código do gestor responsável pelo estabelecimento. |
| `SP_UF` | String (2) | Código IBGE da UF do estabelecimento (p.ex. `12` = Acre). |
| `SP_AA / SP_MM` | String | Ano e mês da competência. |
| `SP_CNES` | String (7) | Estabelecimento (CNES) que realizou a internação. |
| `SP_NAIH` | String (13) | Número da AIH a que o ato pertence (chave para o RD). |
| `SP_PROCREA` | String (10) | Procedimento principal realizado na AIH. |
| `SP_DTINTER / SP_DTSAIDA` | String AAAAMMDD | Datas de internação e saída da AIH. |
| `SP_ATOPROF` | String (10) | Código SIGTAP do ato profissional executado. |
| `SP_QTD_ATO / SP_QT_PROC` | Inteiro | Quantidade do ato e de procedimentos. |
| `SP_PTSP` | String | Pontos de serviços profissionais do ato. |
| `SP_VALATO` | Float | Valor (R$) do ato profissional. |
| `SP_M_HOSP / SP_M_PAC` | String (6) | Município do hospital e município de residência do paciente. |
| `SP_PF_CBO` | String (6) | CBO da ocupação do profissional que executou o ato. |
| `SP_PF_DOC / SP_PJ_DOC` | String | Documento do profissional (pessoa física, CPF/CNS) e da pessoa jurídica (CNPJ); dados pessoais, tratar conforme a LGPD. |
| `SP_CIDPRI / SP_CIDSEC` | String (CID-10) | Diagnóstico principal e secundário da AIH. |
| `SP_COMPLEX / SP_FINANC / SP_CO_FAEC` | String | Complexidade, tipo de financiamento e subtipo FAEC do ato. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `sp_uf` | `SP_UF` | texto | Unidade da Federação. | — | todos |
| `sp_aa` | `SP_AA` | inteiro ou texto | Ano da internação. | — | todos |
| `sp_mm` | `SP_MM` | inteiro ou texto | Mês da internação. | — | todos |
| `sp_cgchosp` | `SP_CGCHOSP` | inteiro | CNPJ do hospital (estabelecimento onde a AIH foi realizada) | — | 1997-07 a 2006-01 |
| `sp_naih` | `SP_NAIH` | inteiro ou texto | Número da AIH. | — | todos |
| `sp_procrea` | `SP_PROCREA` | inteiro ou texto | Procedimento principal realizado na AIH. | — | todos |
| `sp_dtinter` | `SP_DTINTER` | inteiro ou texto | Data da internação. | — | todos |
| `sp_dtsaida` | `SP_DTSAIDA` | inteiro ou texto | Data de saída. | — | todos |
| `sp_num_pr` | `SP_NUM_PR` | inteiro ou texto | Zerado | — | todos |
| `sp_tipo` | `SP_TIPO` | inteiro ou texto | Zerado | — | todos |
| `sp_cpfcgc` | `SP_CPFCGC` | inteiro ou texto | CNES, CPF ou CNPJ do prestador do serviço do ato profissional. | — | todos |
| `sp_atoprof` | `SP_ATOPROF` | inteiro ou texto | Procedimento referente ao ato profissional. | — | todos |
| `sp_tp_ato` | `SP_TP_ATO` | inteiro ou texto | Zerado. | — | todos |
| `sp_qtd_ato` | `SP_QTD_ATO` | inteiro | Quantidade de atos profissionais. | — | todos |
| `sp_ptsp_nf` | `SP_PTSP_NF` | inteiro | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | 1997-07 a 2006-01 |
| `sp_valato` | `SP_VALATO` | decimal(14,2) | Valor do ato profissional. | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `sp_gestor` | `SP_GESTOR` | texto | Unidade de Federação + Código Município de Gestão ou UF0000 se o Estabelecimento Executante está sob Gestão Estadual. | — | 2012-10 a 2026-08 |
| `sp_cnes` | `SP_CNES` | texto | Código do CNES do Estabelecimento de Saúde executante da AIH. | — | 2012-10 a 2026-08 |
| `sp_ptsp` | `SP_PTSP` | texto | Quantidade de pontos. | — | 2012-10 a 2026-08 |
| `sp_nf` | `SP_NF` | texto | Nota fiscal do material empregado quando órtese/prótese, quando não, o campo representa a data do ato. | — | 2012-10 a 2026-08 |
| `sp_m_hosp` | `SP_M_HOSP` | texto | Município de localização do Estabelecimento Executante da AIH. | — | 2012-10 a 2026-08 |
| `sp_m_pac` | `SP_M_PAC` | texto | Município de residência do paciente. | — | 2012-10 a 2026-08 |
| `sp_des_hos` | `SP_DES_HOS` | texto | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento. | — | 2012-10 a 2026-08 |
| `sp_des_pac` | `SP_DES_PAC` | texto | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento. | — | 2012-10 a 2026-08 |
| `sp_complex` | `SP_COMPLEX` | texto | Complexidade do ato profissional. | — | 2012-10 a 2026-08 |
| `sp_financ` | `SP_FINANC` | texto | Tipo de financiamento do ato profissional. | — | 2012-10 a 2026-08 |
| `sp_co_faec` | `SP_CO_FAEC` | texto | Tipo de financiamento (04-FAEC) + Subtipo de financiamento relacionado ao tipo de financiamento (04-FAEC) do ato profissional. | — | 2012-10 a 2026-08 |
| `sp_pf_cbo` | `SP_PF_CBO` | texto | Código de Ocupação Brasileira do Profissional que realizou o ato ou “00000” caso não tenha sido. | — | 2012-10 a 2026-08 |
| `sp_pf_doc` | `SP_PF_DOC` | texto | Documento de pessoa jurídica. | — | 2012-10 a 2026-08 |
| `sp_pj_doc` | `SP_PJ_DOC` | texto | Documento de pessoa física. | — | 2012-10 a 2026-08 |
| `in_tp_val` | `IN_TP_VAL` | texto | Tipo de valor: 1 - SP /2 –SH. | — | 2012-10 a 2026-08 |
| `sequencia` | `SEQUENCIA` | inteiro | Código sequencial. | — | 2012-10 a 2026-08 |
| `remessa` | `REMESSA` | texto | Nome da remessa. | — | 2012-10 a 2026-08 |
| `serv_cla` | `SERV_CLA` | texto | Serviço/Classificação. | — | 2012-10 a 2026-08 |
| `sp_cidpri` | `SP_CIDPRI` | texto | CID Principal. | — | 2012-10 a 2026-08 |
| `sp_cidsec` | `SP_CIDSEC` | texto | CID Secundário. | — | 2012-10 a 2026-08 |
| `sp_qt_proc` | `SP_QT_PROC` | inteiro | Quantidade de procedimentos realizados. | — | 2012-10 a 2026-08 |
| `sp_u_aih` | `SP_U_AIH` | texto | Indicador único da AIH. Contabiliza a AIH sem repetições. | — | 2012-10 a 2026-08 |
| `fonte_orc` | `FONTE_ORC` | texto | Fonte orçamentária do pagamento (campo presente só nas partições mais recentes) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2026-08 |

## No lake

- **Dataset no lake:** `datasus/sih-sp`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): decimal(14,2): 1, inteiro: 16, texto: 35.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sih-sp.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) é um arquivo **muito grande** — prefira filtrar por UF/mês e usar leitura em pedaços/Parquet; (ii) o grão é o ato, então some `SP_VALATO` por `SP_NAIH` antes de comparar com `VAL_SP` do RD; (iii) `SP_PF_DOC` identifica pessoas físicas — não publique sem anonimização; (iv) atos de AIH tipo 5 repetem-se por competência. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Tipo que varia entre períodos:** `sp_aa`, `sp_mm`, `sp_naih`, `sp_procrea`, `sp_dtinter`, `sp_dtsaida`, `sp_num_pr`, `sp_tipo`, `sp_cpfcgc`, `sp_atoprof`, `sp_tp_ato` aparecem com mais de um tipo nas amostras (por exemplo, inteiro em alguns períodos e texto em outros); leia a coluna `Tipo` do dicionário e converta explicitamente antes de empilhar períodos. Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Colunas que não existem em todo o período:** 25 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sih-sp").glob("**/*.parquet"))
dados = pl.concat(  # períodos diferentes têm colunas e tipos diferentes
    [pl.scan_parquet(a, hive_partitioning=True) for a in arquivos],
    how="diagonal_relaxed",
)

(
    dados.group_by("ano", "mes", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "mes", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Pela linha de comando (`datasus-fetcher`)

```bash
# o que o FTP publica para o dataset (arquivos e tamanho)
datasus-fetcher list sih-sp

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sih-sp -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sih-sp
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIHSUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/IT_SIHSUS_1603.pdf`
- **Manual Técnico Operacional do SIH/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **PCDaS/Fiocruz** (SIH/SUS para pesquisa): https://pcdas.icict.fiocruz.br/
