---
dataset:
  id: cnes-ef
  fonte: datasus
  titulo: Estabelecimento Filantrópico
  resumo: O cnes-ef contém os microdados do arquivo de Estabelecimento Filantrópico do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra a condição de filantropia dos estabelecimentos de saúde.
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2007-03
    fim: em-curso
  unidade: um registro de filantropia de um estabelecimento, em uma competência
  granularidade:
    espacial: estabelecimento de saúde (CNES) e município; um arquivo por UF
    temporal: competência (mês)
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e competência mensal
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 33
  dados_pessoais:
  - coluna: cpf_cnpj
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  - coluna: cod_cep
    categoria: CEP
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Estabelecimento Filantrópico (`cnes-ef`)

## Resumo

O `cnes-ef` contém os microdados do arquivo de **Estabelecimento Filantrópico** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra a condição de filantropia dos estabelecimentos de saúde. Cada registro (linha) representa um **registro de filantropia** (`SGRUPHAB`) de um estabelecimento, em uma competência, com vigência e portaria. Identifica entidades beneficentes de assistência social na área da saúde (CEBAS-Saúde), relevantes para a certificação e para a imunidade/isenção de contribuições.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2007-03 a 2026-09 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 5874 arquivos (~11 MB, 25 UFs)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Não
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`)
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/EF` | `EF` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `EFSP2401.dbc` — `EF` (Estabelecimento Filantrópico), `SP` (UF), `24` (ano), `01` (mês). Há também `EFBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-ef/2024-01/cnes-ef_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Estabelecimento Filantrópico — EF*.dbf") e `TAB_CNES.zip`.

## Conteúdo

O arquivo `EF` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS. A condição de estabelecimento filantrópico é relevante porque entidades beneficentes certificadas (CEBAS-Saúde, concedido pelo Ministério da Saúde) têm tratamento tributário específico e são parceiras importantes do SUS, sobretudo em hospitais de referência.

O **evento gerador** é o registro/atualização da condição de filantropia no SCNES a cada competência. A **unidade de análise é o registro de filantropia de um estabelecimento na competência** (`CNES` + `SGRUPHAB` + `COMPETEN`), com vigência em `CMPT_INI`/`CMPT_FIM` e a portaria em `PORTARIA`/`DTPORTAR`/`MAPORTAR`. Compartilha o bloco de habilitação/portaria com os arquivos `HB`, `GM`, `RC`, `EE` e `IN`. A cobertura aparece com 25 UFs (sem arquivos para algumas UFs, o que reflete a inexistência de estabelecimentos filantrópicos cadastrados em todas as competências).

A série histórica no FTP começa em março de 2007. Não há diretório preliminar.

Aplicações analíticas típicas: identificação de entidades filantrópicas que ofertam serviços ao SUS, análise da participação filantrópica na rede hospitalar, apoio à certificação/renovação do CEBAS-Saúde e estudos sobre a composição público-privada da oferta assistencial.

### Cobertura observada

- Índice do FTP (2026-10): 5874 arquivos, de 2007-03 a 2026-09, 25 UF(s) com arquivos, última atualização em 2026-10-15.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007-12 a 2026-06), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `SGRUPHAB` | String (4) | Código do grupo de habilitação/filantropia |
| `CMPT_INI` / `CMPT_FIM` | String (`AAAAMM`) | Competência inicial / final de vigência |
| `DTPORTAR` | String (10) | Data da portaria |
| `PORTARIA` | String (50) | Identificação da portaria |
| `MAPORTAR` | String (`AAAAMM`) | Data da portaria formatada como competência |
| `TP_PREST` | String (2) | Tipo de prestador |
| `VINC_SUS` | String (2) | Vínculo com o SUS: 1 - Sim, 0 - Não |
| `NAT_JUR` | String (4) | Natureza jurídica |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `TPGESTAO` | String (1) | Tipo de gestão de saúde |
| `TERCEIRO` | String (1) | O estabelecimento é terceiro: 1 - Sim, 0 - Não |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `cnes` | `CNES` | texto | Número nacional do estabelecimento de saúde | — | todos |
| `codufmun` | `CODUFMUN` | texto | Código do município do estabelecimento UF+ MUNIC (sem dígito) | — | todos |
| `regsaude` | `REGSAUDE` | texto | Código da região de saúde | — | todos |
| `micr_reg` | `MICR_REG` | texto | Código da micro-região de saúde | — | todos |
| `distrsan` | `DISTRSAN` | texto | Código do distrito sanitário | — | todos |
| `distradm` | `DISTRADM` | texto | Código do distrito administrativo | — | todos |
| `tpgestao` | `TPGESTAO` | texto | Gestão de saúde | — | todos |
| `pf_pj` | `PF_PJ` | texto | Indicador de pessoa: 1-Física 3-Jurídica | — | todos |
| `cpf_cnpj` | `CPF_CNPJ` | texto | CPF do Estabelecimento, caso pessoa física OU CNPJ, caso pessoa jurídica | — | todos |
| `niv_dep` | `NIV_DEP` | texto | Grau de dependência: 1-Individual 3-Mantida | — | todos |
| `cnpj_man` | `CNPJ_MAN` | texto | CNPJ da mantenedora do Estabelecimento | — | todos |
| `esfera_a` | `ESFERA_A` | texto | Código da esfera administrativa | — | todos |
| `retencao` | `RETENCAO` | texto | Código de retenção de tributos | — | todos |
| `atividad` | `ATIVIDAD` | texto | Código da atividade de ensino | — | todos |
| `natureza` | `NATUREZA` | texto | Código da natureza da organização | — | todos |
| `clientel` | `CLIENTEL` | texto | Código de fluxo da clientela | — | todos |
| `tp_unid` | `TP_UNID` | texto | Tipo de unidade (Estabelecimento) | — | todos |
| `turno_at` | `TURNO_AT` | texto | Código de turno de atendimento | — | todos |
| `niv_hier` | `NIV_HIER` | texto | Código do nível de hierarquia | — | todos |
| `terceiro` | `TERCEIRO` | texto | O estabelecimento é terceiro: 1-Sim 0-Não 2-não | — | todos |
| `cod_cep` | `COD_CEP` | texto | CEP do estabelecimento | — | todos |
| `vinc_sus` | `VINC_SUS` | texto | Vínculo com SUS: 1-Sim 0-Não | — | todos |
| `tp_prest` | `TP_PREST` | texto | Tipo de Prestador | — | todos |
| `sgruphab` | `SGRUPHAB` | texto | Código da habilitação | — | todos |
| `cmpt_ini` | `CMPT_INI` | texto | Competência inicial | — | todos |
| `cmpt_fim` | `CMPT_FIM` | texto | Competência final | — | todos |
| `dtportar` | `DTPORTAR` | texto | Data da portaria | — | todos |
| `portaria` | `PORTARIA` | texto | Portaria | — | todos |
| `maportar` | `MAPORTAR` | texto | Campo DT_PORTARIA formatado como AAAAMM | — | todos |
| `competen` | `COMPETEN` | texto | Ano e Mês de competência da informação (AAAAMM) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `nat_jur` | `NAT_JUR` | texto | Natureza Jurídica de Incentivos - Nomenclatura (IN*.dbf ) DESCRIÇÃO | — | 2013-12 a 2026-06 |

## No lake

- **Dataset no lake:** `datasus/cnes-ef`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): texto: 33.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `cnes-ef.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- cobertura parcial de UFs (algumas não possuem estabelecimentos filantrópicos na competência); leiaute quase idêntico a `HB`, `GM`, `RC`, `EE` e `IN`; vigência deve ser considerada para saber quais estabelecimentos eram filantrópicos em cada competência; e a interpretação de `SGRUPHAB` exige as tabelas de domínio. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 1 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/cnes-ef/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "mes", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "mes", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-ef
quantilica datasus list cnes-ef

# 2. Baixar microdados de cnes-ef (uf+yearmonth)
quantilica datasus sync cnes-ef -o ./data --start 2024-01 --end 2024-12 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-ef -o ./data --docs --aux --start 2024-01 --end 2024-12

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-ef -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-ef/2024-01/cnes-ef_202401-sp@20261015.dbc", clean=True)

# Estabelecimentos filantrópicos cadastrados na competência
print(qdf.select(pl.col("cnes").n_unique().alias("estabelecimentos_filantropicos")))
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/EF`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout EF) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **Certificação de Entidades Beneficentes de Assistência Social na área da Saúde (CEBAS-Saúde)**
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
