---
dataset:
  id: sisprenatal-pn
  fonte: datasus
  titulo: Pré-Natal
  resumo: 'Pré-Natal do DATASUS: um registro de acompanhamento de gestante.'
  orgao: Ministério da Saúde — DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SISPRENATAL/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2012-01
    fim: 2014-12
  unidade: um registro de acompanhamento de gestante
  granularidade:
    espacial: município de residência da gestante e da unidade de saúde; um arquivo por UF
    temporal: competência (mês)
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e competência mensal
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 38
  unidades_de_medida:
    qt_cons: quantidade
  dados_pessoais:
  - coluna: nu_cns
    categoria: Cartão Nacional de Saúde (CNS)
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Pré-Natal (`sisprenatal-pn`)

## Resumo

Microdados do SISPRENATAL (Sistema de Monitoramento e Avaliação do Pré-Natal, Parto, Puerpério e Criança) do Ministério da Saúde, com registros de acompanhamento de gestantes no SUS entre 2012 e 2014. A unidade de registro é o acompanhamento da gestante, por UF e mês.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** Não aplicável (o catálogo `meta.docs` não define diretório de documentação para este sistema)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SISPRENATAL/201201_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SISPRENATAL/201201_/Dados` | `PN` | `uf_year2_month_pattern` — UF (2 letras) + ano (2 dígitos) + mês (2 dígitos) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `PNSP1201.dbc` — `PN` (pré-natal) + `SP` (UF) + `12` (ano 2012) + `01` (mês).
- **No armazenamento local do `datasus-fetcher`**: `data/sisprenatal-pn/<AAAAMM>/sisprenatal-pn_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sisprenatal-pn/202401/sisprenatal-pn_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação: nenhum arquivo catalogado em `documentation/sisprenatal.json` (não há `meta.docs` para `sisprenatal`); o dicionário de variáveis está dentro do pacote de tabulação listado abaixo.
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/sisprenatal.json`):
    - `/dissemin/publicos/SISPRENATAL/201201_/Auxiliar/TAB_SISPRENATAL.zip` (3.8 MB)

## Conteúdo

O SISPRENATAL foi criado pelo Ministério da Saúde para acompanhar a implementação do Programa de Humanização no Pré-Natal e Nascimento (PHPN, Portaria GM/MS nº 569/2000) e, depois, da Rede Cegonha (2011), registrando o cadastro da gestante, as consultas, os exames e a imunização do pré-natal, além de dados do parto e do puerpério. Sua gestão cabe à área técnica de saúde da mulher (SAPS/MS), com o DATASUS como desenvolvedor.

O instrumento de coleta é a ficha de cadastramento da gestante e as fichas de acompanhamento do pré-natal, digitadas pelas unidades de saúde no sistema. A unidade de análise é a gestante acompanhada (ou o evento de acompanhamento, conforme o arquivo mensal), o que implica atenção a duplicidades entre meses.

A versão disponibilizada no FTP cobre janeiro/2012 a dezembro/2014 (36 competências, 27 UF, ~232 MB), a fase final do sistema legado antes da migração para os sistemas de informação da atenção básica (e-SUS AB/SISAB) e para a estratégia de pré-natal via cadastros ambulatoriais. A cobertura é parcial: municípios que não digitavam no SISPRENATAL ficam fora ou subrepresentados.

Aplicações: proporção de gestantes com 6 ou mais consultas (adequação do pré-natal), início precoce do pré-natal (1º trimestre), realização de exames de rotina (sífilis, HIV), imunização antitetânica e realização de consulta puerperal; análises de qualidade do pré-natal comparadas aos dados do SINASC (`sinasc-dn`).

### Cobertura observada

- Índice do FTP (2026-10): 944 arquivos, de 2012-01 a 2014-12, 27 UF(s) com arquivos, última atualização em 2015-01-06.
- Conversão local de amostras (3 arquivo(s) Parquet, de 2012-02 a 2014-03), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Nomes verificados contra o arquivo real `PNSP1408.dbc` (36 colunas). Não há municípios de residência da gestante, apenas o da UBS.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `NU_ANO_GES` | String (4) | Ano da gestação. |
| `DT_ATEND` | String `AAAAMM` | Competência do atendimento. |
| `CO_UF_IBGE` | String (2) | UF (código IBGE). |
| `CO_MUN_UBS` | String (IBGE, 6) | Município da unidade básica de saúde. |
| `CO_PAIS` | String (3) | País da gestante. |
| `NU_GESTA` / `CO_GESTANT` | String | Número da gestação e identificador da gestante no sistema. |
| `NU_CNS` / `NU_NIS` / `NU_NIS_REP` | String (15) | Cartão Nacional de Saúde e NIS da gestante e do responsável (dados pessoais: tratar conforme a LGPD). |
| `NU_IDADE` | String (15) | Idade da gestante. |
| `DS_ZONA` | String (50) | Zona de residência (descrição). |
| `CO_ESC_GP` / `CO_RAC_GP` / `CO_ETN_GP` / `CO_STF_GP` | String | Escolaridade, raça, etnia e situação familiar da gestante. |
| `DT_DUM` / `DT_DPP` | String `AAAAMMDD` | Data da última menstruação e data provável do parto. |
| `DT_INC` | String `AAAAMMDD` | Data de inclusão do registro. |
| `CO_TPO_GRA` | String (10) | Tipo de gravidez. |
| `ST_GRA_ANT` / `ST_GRA_PLA` / `ST_AUX_DSL` / `ST_GESTAC` | String (1) | Indicadores: gravidez anterior, planejada, auxílio e situação da gestação. |
| `QT_AB_ECT` / `QT_AB_GER` / `QT_AB_MOL` | String (3) | Histórico de abortamentos: ectópicos, gerais e molares. |
| `QT_MOR_APS` / `QT_MOR_PS` / `QT_NSC_MOR` / `QT_NSC_VIV` | String (3) | Mortes (antes e após o primeiro semestre de vida), nascidos mortos e nascidos vivos anteriores. |
| `QT_PRT_CIR` / `QT_PRT_FOR` / `QT_PRT_VAG` | String (3) | Partos anteriores: cesáreos, fórceps e vaginais. |
| `QT_CONS` / `QT_CONSULT` | Inteiro / String (3) | Número de consultas de pré-natal (mesma informação em duas colunas). |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `nu_ano_ges` | `NU_ANO_GES` | texto | Ano da gestação (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_atend` | `DT_ATEND` | data | Data do atendimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_uf_ibge` | `CO_UF_IBGE` | texto | UF do atendimento (código IBGE) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_gesta` | `NU_GESTA` | texto | Número de gestações da gestante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_gestant` | `CO_GESTANT` | texto | Código da gestante (identificador codificado) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pais` | `CO_PAIS` | texto | Código do país de nascimento da gestante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_cns` | `NU_CNS` | texto | Número do Cartão Nacional de Saúde da gestante (codificado) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_idade` | `NU_IDADE` | texto | Idade da gestante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_nis` | `NU_NIS` | texto | Número de Identificação Social (NIS) da gestante (codificado) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_nis_rep` | `NU_NIS_REP` | texto | Número de Identificação Social (NIS) do responsável (codificado) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ds_zona` | `DS_ZONA` | texto | Zona de residência (urbana ou rural) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `qt_ab_ect` | `QT_AB_ECT` | texto | Quantidade de abortos por gravidez ectópica (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `qt_ab_ger` | `QT_AB_GER` | texto | Quantidade de abortos (geral) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `qt_ab_mol` | `QT_AB_MOL` | texto | Quantidade de abortos por gravidez molar (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `qt_mor_aps` | `QT_MOR_APS` | texto | Quantidade de filhos mortos após o parto (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `qt_mor_ps` | `QT_MOR_PS` | texto | Quantidade de filhos mortos antes do parto (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `qt_nsc_mor` | `QT_NSC_MOR` | texto | Quantidade de nascidos mortos (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `qt_nsc_viv` | `QT_NSC_VIV` | texto | Quantidade de nascidos vivos (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `qt_prt_cir` | `QT_PRT_CIR` | texto | Quantidade de partos cirúrgicos (cesáreas) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `qt_prt_for` | `QT_PRT_FOR` | texto | Quantidade de partos com fórceps (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `qt_prt_vag` | `QT_PRT_VAG` | texto | Quantidade de partos vaginais (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `st_aux_dsl` | `ST_AUX_DSL` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `st_gra_ant` | `ST_GRA_ANT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `st_gra_pla` | `ST_GRA_PLA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `dt_dum` | `DT_DUM` | texto | Data da última menstruação (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_dpp` | `DT_DPP` | texto | Data provável do parto (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_tpo_gra` | `CO_TPO_GRA` | texto | Tipo de gravidez (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_esc_gp` | `CO_ESC_GP` | texto | Escolaridade da gestante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_rac_gp` | `CO_RAC_GP` | texto | Raça/cor da gestante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_etn_gp` | `CO_ETN_GP` | texto | Etnia da gestante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_stf_gp` | `CO_STF_GP` | texto | Situação familiar da gestante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_mun_ubs` | `CO_MUN_UBS` | texto | Município da unidade básica de saúde (código IBGE) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `qt_cons` | `QT_CONS` | inteiro | Quantidade de consultas (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `qt_consult` | `QT_CONSULT` | texto | Quantidade de consultas de pré-natal (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `st_gestac` | `ST_GESTAC` | texto | Situação da gestação (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_inc` | `DT_INC` | texto | Data de inclusão do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sisprenatal-pn`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 1, inteiro: 1, texto: 36.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sisprenatal-pn.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sisprenatal-pn").glob("**/*.parquet"))
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
datasus-fetcher list sisprenatal-pn

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sisprenatal-pn -o ./data --start 2024-01 --end 2024-12 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sisprenatal-pn
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SISPRENATAL/201201_/Dados`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Ministério da Saúde — Programa de Humanização no Pré-Natal e Nascimento (PHPN)**, Portaria GM/MS nº 569/2000, e Rede Cegonha (Portaria GM/MS nº 1.459/2011).
- **Pacote de tabulação no FTP**: `TAB_SISPRENATAL.zip` (inclui o dicionário de variáveis e arquivos de conversão).
- **PCDaS / Fiocruz**: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde** (DATASUS): https://wiki.saude.gov.br/
