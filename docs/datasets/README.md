# Datasets do DATASUS — Índice Geral

Este é o **índice geral da documentação** dos **113 datasets** de microdados do [DATASUS](https://datasus.saude.gov.br) suportados pelo [`datasus-fetcher`](../../README.md). Cada dataset listado abaixo possui uma página própria com ficha técnica, contexto institucional, variáveis, regras de saneamento e exemplos de uso; o código do dataset é um link direto para essa página.

## Arquitetura dos microdados no FTP DATASUS

O DATASUS disponibiliza seus microdados brutos em um servidor FTP público (`ftp.datasus.gov.br`), sob a raiz `/dissemin/publicos/`. Nessa árvore, **cada sistema de informação de saúde ocupa um diretório próprio** — por exemplo `SIHSUS/` (SIH), `SIASUS/` (SIA), `SIM/`, `SINAN/`, `CNES/` — e, dentro dele, os arquivos são **particionados** tipicamente por **UF** e por **período** (competência mensal `AAAAMM` ou ano `AAAA`). É comum haver séries separadas em subdiretórios distintos (ex.: `199201_200712/` e `200801_/` no SIH), recortes de dados **finais** e **preliminares**, e pastas `Doc/` (dicionários e manuais) e `Auxiliar/` (tabelas de referência: CID, municípios, procedimentos, CBO etc.).

Os arquivos de microdados são distribuídos no formato **`.dbc`** — um dBASE comprimido com o algoritmo PKWARE DCL (blast) — além de alguns conjuntos auxiliares em `.zip` (bases populacionais e territoriais, dicionários e tabelas). O **`datasus-fetcher`** traduz essa árvore do FTP em um catálogo de datasets nomeados e estáveis (`meta.py`), registrando para cada um os diretórios FTP, o **prefixo** dos nomes de arquivo, o **padrão de nomes**, a **partição** e a **periodicidade**. A ferramenta então baixa os arquivos em paralelo, descompacta os `.dbc` **nativamente em Rust** e, opcionalmente, converte os microdados para **Parquet** tratado (com saneamento de sentinelas nulos, preservação de zeros à esquerda em códigos e tipagem de datas).

As páginas deste índice descrevem os datasets em termos de dados, variáveis e qualidade; os volumes e as coberturas temporais são consolidados a partir do índice de metadados [`datasus-metadata/metadata/index.json`](https://github.com/Quantilica/datasus-metadata) (posição de **outubro de 2026**), que reflete o estado atual do FTP e pode avançar em relação às estatísticas históricas do [`README.md`](../../README.md#datasets-disponíveis).

## Como ler as tabelas

| Coluna | Descrição |
|---|---|
| **Dataset** | Código estável do dataset no `datasus-fetcher`; link para a página detalhada. |
| **Nome oficial** | Denominação do conjunto de dados conforme documentado pelo DATASUS/sistema de origem. |
| **Prefixo FTP** | Prefixo dos nomes de arquivo no servidor (ex.: `RD`, `DENG`); pode haver mais de um ao longo da série histórica. |
| **Partição** | Chaves de organização dos arquivos no FTP (`uf`, `year`, `yearmonth`, `version`, ...). |
| **Cobertura temporal** | Período com arquivos publicados no FTP (do `index.json`); `—` quando não há recorte temporal. |
| **Arquivos** | Número de arquivos atualmente publicados no FTP (`n_files`). |
| **Tamanho** | Volume total dos arquivos no FTP (`total_size`). |

## Visão geral dos sistemas

O catálogo cobre **16 sistemas** de informação e **113 datasets**.

| Sistema | Nome completo | Datasets | Formato | Periodicidade |
|---|---|---:|---|---|
| [`base-populacional-ibge`](#base-populacional-ibge) | Base Populacional - IBGE | 3 | `zip` | Anual |
| [`base-territorial`](#base-territorial) | Base Territorial | 3 | `zip` | Anual / Irregular |
| [`cih`](#cih) | CIH: Sistema de Comunicação de Informação Hospitalar | 1 | `dbc` | Mensal |
| [`ciha`](#ciha) | CIHA: Sistema de Comunicação de Informação Hospitalar e Ambulatorial | 1 | `dbc` | Mensal |
| [`cnes`](#cnes) | CNES: Cadastro Nacional de Estabelecimentos de Saúde | 13 | `dbc` | Mensal |
| [`pce`](#pce) | PCE: Programa de Controle da Esquistossomose | 1 | `dbc` | Anual |
| [`po`](#po) | PO: Painel de Oncologia | 1 | `dbc` | Anual |
| [`resp`](#resp) | RESP: Notificações de casos suspeitos de SCZ | 1 | `dbc` | Anual |
| [`sia`](#sia) | SIA: Sistema de Informações Ambulatoriais | 12 | `dbc` | Mensal |
| [`sih`](#sih) | SIH: Sistema de Informação Hospitalar | 4 | `dbc` | Mensal |
| [`sim`](#sim) | SIM: Sistema de Informação de Mortalidade | 10 | `dbc` | Anual |
| [`sinan`](#sinan) | SINAN: Sistema de Informação de Agravos de Notificação | 56 | `dbc` | Anual |
| [`sinasc`](#sinasc) | SINASC: Sistema de Informação de Nascidos Vivos | 2 | `dbc` | Anual |
| [`siscolo`](#siscolo) | SISCOLO: Sistema de Informações de Cânceres de Colo de Útero | 2 | `dbc` | Mensal |
| [`sismama`](#sismama) | SISMAMA: Sistema de Informações de Cânceres de Mama | 2 | `dbc` | Mensal |
| [`sisprenatal`](#sisprenatal) | SISPRENATAL: Sistema de Monitoramento e Avaliação do Pré-Natal, Parto, Puepério e Criança | 1 | `dbc` | Mensal |

**Total: 184.657 arquivos em 415,2 GB** (somatório dos 113 datasets).

---

<a id="base-populacional-ibge"></a>

## base-populacional-ibge — Base Populacional - IBGE

3 datasets · 92 arquivos · 250,3 MB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`base-populacional-ibge-pop`](./base-populacional-ibge-pop.md) | POP - Censo e Estimativas | `POP` | uf / year | 1980 a 2012 | 33 | 157,7 MB |
| [`base-populacional-ibge-pops`](./base-populacional-ibge-pops.md) | POPS - Estimativas por Sexo e Idade | `POPS` | uf / year | 2000 a 2025 | 26 | 90,0 MB |
| [`base-populacional-ibge-popt`](./base-populacional-ibge-popt.md) | POPT - Estimativas TCU | `POPT` | uf / year | 1992 a 2025 | 33 | 2,6 MB |

<a id="base-territorial"></a>

## base-territorial — Base Territorial

3 datasets · 160 arquivos · 205,0 MB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`base-territorial`](./base-territorial.md) | Base Territorial | — | version | — | 21 | 34,4 MB |
| [`base-territorial-conversao`](./base-territorial-conversao.md) | Base Territorial - Conversão | — | uf | — | 28 | 21,1 MB |
| [`base-territorial-mapas`](./base-territorial-mapas.md) | Base Territorial - Mapas | — | uf / year | 1991 a 2025 | 111 | 149,5 MB |

<a id="cih"></a>

## cih — CIH: Sistema de Comunicação de Informação Hospitalar

1 dataset · 868 arquivos · 165,1 MB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`cih-cr`](./cih-cr.md) | Comunicação de Internação Hospitalar | `CR` | uf / yearmonth | 2008-01 a 2011-04 | 868 | 165,1 MB |

<a id="ciha"></a>

## ciha — CIHA: Sistema de Comunicação de Informação Hospitalar e Ambulatorial

1 dataset · 4.802 arquivos · 5,7 GB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`ciha`](./ciha.md) | Sistema de Comunicação de Informação Hospitalar e Ambulatorial | `CIHA` | uf / yearmonth | 2011-01 a 2026-07 | 4.802 | 5,7 GB |

<a id="cnes"></a>

## cnes — CNES: Cadastro Nacional de Estabelecimentos de Saúde

13 datasets · 81.148 arquivos · 54,5 GB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`cnes-dc`](./cnes-dc.md) | Dados Complementares | `DC` | uf / yearmonth | 2005-08 a 2026-09 | 6.858 | 128,0 MB |
| [`cnes-ee`](./cnes-ee.md) | Estabelecimento de Ensino | `EE` | uf / yearmonth | 2007-03 a 2021-07 | 3.201 | 4,6 MB |
| [`cnes-ef`](./cnes-ef.md) | Estabelecimento Filantrópico | `EF` | uf / yearmonth | 2007-03 a 2026-09 | 5.874 | 11,5 MB |
| [`cnes-ep`](./cnes-ep.md) | Equipes | `EP` | uf / yearmonth | 2007-04 a 2026-09 | 6.318 | 610,9 MB |
| [`cnes-eq`](./cnes-eq.md) | Equipamentos | `EQ` | uf / yearmonth | 2005-08 a 2026-09 | 6.857 | 1,6 GB |
| [`cnes-gm`](./cnes-gm.md) | Gestão e Metas | `GM` | uf / yearmonth | 2007-03 a 2026-09 | 5.975 | 13,8 MB |
| [`cnes-hb`](./cnes-hb.md) | Habilitação | `HB` | uf / yearmonth | 2007-03 a 2026-09 | 6.345 | 146,9 MB |
| [`cnes-in`](./cnes-in.md) | Incentivos | `IN` | uf / yearmonth | 2007-10 a 2026-09 | 6.060 | 46,2 MB |
| [`cnes-lt`](./cnes-lt.md) | Leitos | `LT` | uf / yearmonth | 2005-10 a 2026-09 | 6.804 | 150,5 MB |
| [`cnes-pf`](./cnes-pf.md) | Profissional | `PF` | uf / yearmonth | 2005-08 a 2026-09 | 6.858 | 46,7 GB |
| [`cnes-rc`](./cnes-rc.md) | Regra Contratual | `RC` | uf / yearmonth | 2007-03 a 2026-09 | 6.284 | 81,8 MB |
| [`cnes-sr`](./cnes-sr.md) | Serviço Especializado | `SR` | uf / yearmonth | 2005-08 a 2026-09 | 6.856 | 1,7 GB |
| [`cnes-st`](./cnes-st.md) | Estabelecimentos | `ST` | uf / yearmonth | 2005-08 a 2026-09 | 6.858 | 3,4 GB |

<a id="pce"></a>

## pce — PCE: Programa de Controle da Esquistossomose

1 dataset · 460 arquivos · 15,5 MB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`pce`](./pce.md) | Programa de Controle da Esquistossomose | `PCE` | uf / year | 1995 a 2026 | 460 | 15,5 MB |

<a id="po"></a>

## po — PO: Painel de Oncologia

1 dataset · 14 arquivos · 203,3 MB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`po`](./po.md) | Painel de Oncologia | `PO` | uf / year | 2013 a 2026 | 14 | 203,3 MB |

<a id="resp"></a>

## resp — RESP: Notificações de casos suspeitos de SCZ

1 dataset · 280 arquivos · 3,5 MB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`resp`](./resp.md) | Notificações de casos suspeitos de SCZ | `RESP` | uf / year | 2015 a 2024 | 280 | 3,5 MB |

<a id="sia"></a>

## sia — SIA: Sistema de Informações Ambulatoriais

12 datasets · 51.769 arquivos · 250,5 GB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`sia-ab`](./sia-ab.md) | APAC de Acompanhamento a Cirurgia Bariátrica | `AB` | uf / yearmonth | 2008-01 a 2025-07 | 635 | 16,1 MB |
| [`sia-abo`](./sia-abo.md) | APAC Acompanhamento Pós Cirurgia Bariátrica | `ABO` | uf / yearmonth | 2014-01 a 2026-07 | 1.607 | 38,6 MB |
| [`sia-acf`](./sia-acf.md) | APAC Confeção de Fístula Arteriovenosa | `ACF` | uf / yearmonth | 2014-08 a 2026-07 | 3.768 | 32,3 MB |
| [`sia-ad`](./sia-ad.md) | APAC de Laudos Diversos | `AD` | uf / yearmonth | 2008-01 a 2026-07 | 6.019 | 3,2 GB |
| [`sia-am`](./sia-am.md) | APAC de Medicamentos | `AM` | uf / yearmonth | 2008-01 a 2026-07 | 5.957 | 18,6 GB |
| [`sia-an`](./sia-an.md) | APAC de Nefrologia | `AN` | uf / yearmonth | 2008-01 a 2014-10 | 2.145 | 458,8 MB |
| [`sia-aq`](./sia-aq.md) | APAC de Quimioterapia | `AQ` | uf / yearmonth | 2008-01 a 2026-07 | 5.979 | 5,1 GB |
| [`sia-ar`](./sia-ar.md) | APAC de Radioterapia | `AR` | uf / yearmonth | 2008-01 a 2026-07 | 5.465 | 358,5 MB |
| [`sia-atd`](./sia-atd.md) | APAC de Tratamento Dialítico | `ATD` | uf / yearmonth | 2014-08 a 2026-07 | 3.884 | 1,1 GB |
| [`sia-pa`](./sia-pa.md) | Produção Ambulatorial | `PA` | uf / yearmonth | 1994-07 a 2026-07 | 10.828 | 218,2 GB |
| [`sia-ps`](./sia-ps.md) | Psicossocial | `PS` | uf / yearmonth | 2012-11 a 2026-07 | 4.394 | 3,3 GB |
| [`sia-sad`](./sia-sad.md) | Atenção Domiciliar | `SAD` | uf / yearmonth | 2012-04 a 2018-10 | 1.088 | 53,4 MB |

<a id="sih"></a>

## sih — SIH: Sistema de Informação Hospitalar

4 datasets · 31.522 arquivos · 83,9 GB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`sih-er`](./sih-er.md) | ER - AIH Rejeitadas com código de erro | `ER` | uf / yearmonth | 2011-01 a 2026-08 | 4.958 | 321,3 MB |
| [`sih-rd`](./sih-rd.md) | RD - AIH Reduzida | `RD` | uf / yearmonth | 1992-01 a 2026-08 | 11.211 | 25,6 GB |
| [`sih-rj`](./sih-rj.md) | RJ - AIH Rejeitadas | `RJ` | uf / yearmonth | 2008-01 a 2026-08 | 5.887 | 945,8 MB |
| [`sih-sp`](./sih-sp.md) | SP - Serviços Profissionais | `SP` | uf / yearmonth | 1997-06 a 2026-08 | 9.466 | 57,0 GB |

<a id="sim"></a>

## sim — SIM: Sistema de Informação de Mortalidade

10 datasets · 1.518 arquivos · 6,5 GB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`sim-do-cid09`](./sim-do-cid09.md) | Declarações de Óbito CID-9 | `DOR` | uf / year | 1979 a 1995 | 466 | 757,3 MB |
| [`sim-do-cid10`](./sim-do-cid10.md) | Declarações de Óbito CID-10 | `DO` | uf / year | 1996 a 2026 | 868 | 5,2 GB |
| [`sim-doext-cid09`](./sim-doext-cid09.md) | Declarações de Óbito Externas CID-9 | `DOEXT` | year | 1979 a 1995 | 17 | 44,0 MB |
| [`sim-doext-cid10`](./sim-doext-cid10.md) | Declarações de Óbito Externas CID-10 | `DOEXT` | year | 1996 a 2025 | 30 | 301,2 MB |
| [`sim-dofet-cid09`](./sim-dofet-cid09.md) | Declarações de Óbito Fetais CID-9 | `DOFET` | year | 1979 a 1995 | 17 | 24,1 MB |
| [`sim-dofet-cid10`](./sim-dofet-cid10.md) | Declarações de Óbito Fetais CID-10 | `DOFET` | year | 1996 a 2025 | 30 | 68,7 MB |
| [`sim-doinf-cid09`](./sim-doinf-cid09.md) | Declarações de Óbito Infantis CID-9 | `DOINF` | year | 1979 a 1995 | 17 | 60,8 MB |
| [`sim-doinf-cid10`](./sim-doinf-cid10.md) | Declarações de Óbito Infantis CID-10 | `DOINF` | year | 1996 a 2025 | 30 | 103,1 MB |
| [`sim-domat-cid10`](./sim-domat-cid10.md) | Declarações de Óbitos Maternos CID-10 | `DOMAT` | year | 1996 a 2025 | 30 | 4,6 MB |
| [`sim-dorext-cid10`](./sim-dorext-cid10.md) | Mortalidade de Residentes no Exterior CID-10 | `DOREXT` | year | 2013 a 2025 | 13 | 0,6 MB |

<a id="sinan"></a>

## sinan — SINAN: Sistema de Informação de Agravos de Notificação

56 datasets · 1.082 arquivos · 3,3 GB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`sinan-acbi`](./sinan-acbi.md) | Acidente de trabalho com material biológico | `ACBI` | uf / year | 2006 a 2026 | 21 | 56,7 MB |
| [`sinan-acgr`](./sinan-acgr.md) | Acidente de trabalho | `ACGR` | uf / year | 2006 a 2026 | 21 | 185,4 MB |
| [`sinan-aida`](./sinan-aida.md) | AIDS em adultos | `AIDA` | uf / year | 2007 a 2024 | 18 | 18,9 MB |
| [`sinan-aidc`](./sinan-aidc.md) | AIDS em crianças | `AIDC` | uf / year | 2007 a 2024 | 18 | 0,4 MB |
| [`sinan-anim`](./sinan-anim.md) | Acidente por Animais Peçonhentos | `ANIM` | uf / year | 2007 a 2026 | 20 | 206,6 MB |
| [`sinan-antr`](./sinan-antr.md) | Atendimento Antirrábico | `ANTR` | uf / year | 2006 a 2026 | 21 | 512,9 MB |
| [`sinan-botu`](./sinan-botu.md) | Botulismo | `BOTU` | uf / year | 2007 a 2026 | 20 | 0,2 MB |
| [`sinan-canc`](./sinan-canc.md) | Câncer relacionado ao trabalho | `CANC` | uf / year | 2007 a 2026 | 20 | 0,6 MB |
| [`sinan-chag`](./sinan-chag.md) | Doença de Chagas Aguda | `CHAG` | uf / year | 2000 a 2025 | 26 | 5,1 MB |
| [`sinan-chik`](./sinan-chik.md) | Febre de Chikungunya | `CHIK` | uf / year | 2014 a 2026 | 13 | 99,2 MB |
| [`sinan-cole`](./sinan-cole.md) | Cólera | `COLE` | uf / year | 2007 a 2025 | 18 | 49,4 KB |
| [`sinan-coqu`](./sinan-coqu.md) | Coqueluche | `COQU` | uf / year | 2007 a 2026 | 20 | 10,8 MB |
| [`sinan-deng`](./sinan-deng.md) | Dengue | `DENG` | uf / year | 2000 a 2026 | 27 | 1,1 GB |
| [`sinan-derm`](./sinan-derm.md) | Dermatoses ocupacionais | `DERM` | uf / year | 2006 a 2026 | 21 | 0,7 MB |
| [`sinan-dift`](./sinan-dift.md) | Difteria | `DIFT` | uf / year | 2007 a 2026 | 20 | 0,2 MB |
| [`sinan-espo`](./sinan-espo.md) | Esporotricose (Epizootia) | `ESPO` | uf / year | 2013 a 2022 | 10 | 0,4 MB |
| [`sinan-esqu`](./sinan-esqu.md) | Esquistossomose | `ESQU` | uf / year | 2007 a 2026 | 20 | 8,4 MB |
| [`sinan-exan`](./sinan-exan.md) | Doenças exantemáticas | `EXAN` | uf / year | 2007 a 2026 | 20 | 15,3 MB |
| [`sinan-fmac`](./sinan-fmac.md) | Febre Maculosa | `FMAC` | uf / year | 2007 a 2026 | 20 | 6,2 MB |
| [`sinan-ftif`](./sinan-ftif.md) | Febre Tifoide | `FTIF` | uf / year | 2007 a 2026 | 20 | 0,8 MB |
| [`sinan-hans`](./sinan-hans.md) | Hanseníase | `HANS` | uf / year | 2001 a 2026 | 26 | 60,9 MB |
| [`sinan-hant`](./sinan-hant.md) | Hantavirose | `HANT` | uf / year | 1999 a 2026 | 28 | 2,3 MB |
| [`sinan-hepa`](./sinan-hepa.md) | Hepatites Virais | `HEPA` | uf / year | 2007 a 2023 | 17 | 28,3 MB |
| [`sinan-hiva`](./sinan-hiva.md) | HIV em adultos | `HIVA` | uf / year | 2007 a 2024 | 18 | 17,6 MB |
| [`sinan-hivc`](./sinan-hivc.md) | HIV em crianças | `HIVC` | uf / year | 2007 a 2024 | 18 | 0,2 MB |
| [`sinan-hive`](./sinan-hive.md) | HIV em crianças expostas | `HIVE` | uf / year | 2015 a 2024 | 10 | 1,1 MB |
| [`sinan-hivg`](./sinan-hivg.md) | HIV em gestante | `HIVG` | uf / year | 2007 a 2024 | 18 | 3,8 MB |
| [`sinan-iexo`](./sinan-iexo.md) | Intoxicação Exógena | `IEXO` | uf / year | 2006 a 2026 | 21 | 209,5 MB |
| [`sinan-leiv`](./sinan-leiv.md) | Leishmaniose Visceral | `LEIV` | uf / year | 2000 a 2025 | 26 | 13,4 MB |
| [`sinan-lept`](./sinan-lept.md) | Leptospirose | `LEPT` | uf / year | 2000 a 2026 | 27 | 31,8 MB |
| [`sinan-lerd`](./sinan-lerd.md) | LER/Dort | `LERD` | uf / year | 2006 a 2026 | 21 | 8,5 MB |
| [`sinan-ltan`](./sinan-ltan.md) | Leishmaniose Tegumentar Americana | `LTAN` | uf / year | 2000 a 2025 | 26 | 38,8 MB |
| [`sinan-mala`](./sinan-mala.md) | Malária | `MALA` | uf / year | 2004 a 2026 | 23 | 2,9 MB |
| [`sinan-meni`](./sinan-meni.md) | Meningite | `MENI` | uf / year | 2007 a 2026 | 20 | 49,2 MB |
| [`sinan-ment`](./sinan-ment.md) | Transtornos mentais relacionados ao trabalho | `MENT` | uf / year | 2006 a 2026 | 21 | 2,0 MB |
| [`sinan-ntra`](./sinan-ntra.md) | Notificação de Tracoma | `NTRA` | uf / year | 2010 a 2026 | 17 | 0,8 MB |
| [`sinan-pair`](./sinan-pair.md) | Perda auditiva por ruído relacionado ao trabalho | `PAIR` | uf / year | 2006 a 2026 | 21 | 0,6 MB |
| [`sinan-pest`](./sinan-pest.md) | Peste | `PEST` | uf / year | 2007 a 2025 | 19 | 42,8 KB |
| [`sinan-pfan`](./sinan-pfan.md) | Paralisia Flácida Aguda | `PFAN` | uf / year | 2007 a 2026 | 20 | 1,4 MB |
| [`sinan-pneu`](./sinan-pneu.md) | Pneumoconioses relacionadas ao trabalho | `PNEU` | uf / year | 2006 a 2026 | 21 | 0,4 MB |
| [`sinan-raiv`](./sinan-raiv.md) | Raiva | `RAIV` | uf / year | 2007 a 2026 | 20 | 0,2 MB |
| [`sinan-rota`](./sinan-rota.md) | Rotavírus | `ROTA` | uf / year | 2009 a 2026 | 18 | 1,4 MB |
| [`sinan-sdta`](./sinan-sdta.md) | Surto Doenças Transmitidas por Alimentos | `SDTA` | uf / year | 2007 a 2024 | 17 | 1,2 MB |
| [`sinan-sifa`](./sinan-sifa.md) | Sífilis Adquirida | `SIFA` | uf / year | 2010 a 2025 | 16 | 36,5 MB |
| [`sinan-sifc`](./sinan-sifc.md) | Sífilis Congênita | `SIFC` | uf / year | 2007 a 2025 | 19 | 15,1 MB |
| [`sinan-sifg`](./sinan-sifg.md) | Sífilis em Gestante | `SIFG` | uf / year | 2007 a 2025 | 19 | 22,9 MB |
| [`sinan-src`](./sinan-src.md) | Síndrome da Rubéola Congênita | `SRC` | uf / year | 2007 a 2026 | 20 | 0,2 MB |
| [`sinan-teta`](./sinan-teta.md) | Tétano Acidental | `TETA` | uf / year | 2007 a 2026 | 20 | 0,8 MB |
| [`sinan-tetn`](./sinan-tetn.md) | Tétano Neonatal | `TETN` | uf / year | 2014 a 2026 | 13 | 34,6 KB |
| [`sinan-toxc`](./sinan-toxc.md) | Toxoplasmose Congênita | `TOXC` | uf / year | 2019 a 2026 | 8 | 1,1 MB |
| [`sinan-toxg`](./sinan-toxg.md) | Toxoplasmose Gestacional | `TOXG` | uf / year | 2019 a 2026 | 8 | 3,2 MB |
| [`sinan-trac`](./sinan-trac.md) | Inquérito de Tracoma | `TRAC` | uf / year | 2009 a 2026 | 18 | 1,8 MB |
| [`sinan-tube`](./sinan-tube.md) | Tuberculose | `TUBE` | uf / year | 2001 a 2025 | 25 | 113,3 MB |
| [`sinan-varc`](./sinan-varc.md) | Varicela | `VARC` | uf / year | 2007 a 2026 | 20 | 35,9 MB |
| [`sinan-viol`](./sinan-viol.md) | Violência doméstica, sexual e/ou outras violências | `VIOL` | uf / year | 2009 a 2025 | 17 | 326,2 MB |
| [`sinan-zika`](./sinan-zika.md) | Zika Vírus | `ZIKA` | uf / year | 2015 a 2026 | 12 | 14,2 MB |

<a id="sinasc"></a>

## sinasc — SINASC: Sistema de Informação de Nascidos Vivos

2 datasets · 933 arquivos · 7,2 GB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`sinasc-dn`](./sinasc-dn.md) | Declarações de nascidos vivos | `DNR`, `DN` | uf / year | 1994 a 2026 | 922 | 7,2 GB |
| [`sinasc-dnex`](./sinasc-dnex.md) | Declarações de nascidos vivos no exterior | `DNEX` | year | 2014 a 2024 | 11 | 0,6 MB |

<a id="siscolo"></a>

## siscolo — SISCOLO: Sistema de Informações de Cânceres de Colo de Útero

2 datasets · 5.716 arquivos · 2,5 GB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`siscolo-cc`](./siscolo-cc.md) | Citopatológico de Colo de Útero | `CC` | uf / yearmonth | 2006-01 a 2015-10 | 2.858 | 2,5 GB |
| [`siscolo-hc`](./siscolo-hc.md) | Histopatológico de Colo de Útero | `HC` | uf / yearmonth | 2006-01 a 2015-10 | 2.858 | 40,8 MB |

<a id="sismama"></a>

## sismama — SISMAMA: Sistema de Informações de Cânceres de Mama

2 datasets · 3.349 arquivos · 11,0 MB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`sismama-cm`](./sismama-cm.md) | Citopatológico de Mama | `CM` | uf / yearmonth | 2009-01 a 2015-07 | 1.675 | 5,0 MB |
| [`sismama-hm`](./sismama-hm.md) | Histopatológico de Mama | `HM` | uf / yearmonth | 2009-01 a 2015-07 | 1.674 | 5,9 MB |

<a id="sisprenatal"></a>

## sisprenatal — SISPRENATAL: Sistema de Monitoramento e Avaliação do Pré-Natal, Parto, Puepério e Criança

1 dataset · 944 arquivos · 232,4 MB.

| Dataset | Nome oficial | Prefixo FTP | Partição | Cobertura temporal | Arquivos | Tamanho |
|---|---|---|---|---|---:|---:|
| [`sisprenatal-pn`](./sisprenatal-pn.md) | Pré-Natal | `PN` | uf / yearmonth | 2012-01 a 2014-12 | 944 | 232,4 MB |

---

## Veja também

- [`datasus-fetcher` — README principal](../../README.md)
- [Guia de uso da CLI e da API Python](../../README.md#cli)
- [Índice de metadados do DATASUS](https://github.com/Quantilica/datasus-metadata)

