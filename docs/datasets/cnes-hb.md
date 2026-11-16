---
dataset:
  id: cnes-hb
  fonte: datasus
  titulo: Habilitação
  resumo: 'Habilitação do DATASUS: uma habilitação concedida a um estabelecimento, em uma competência.'
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2007-03
    fim: em-curso
  unidade: uma habilitação concedida a um estabelecimento, em uma competência
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
    colunas: 34
  unidades_de_medida:
    nuleitos: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: cpf_cnpj
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  - coluna: cod_cep
    categoria: CEP
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Habilitação (`cnes-hb`)

## Resumo

O `cnes-hb` contém os microdados do arquivo de **Habilitações** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra as habilitações de serviços dos estabelecimentos. Cada registro (linha) representa uma **habilitação concedida** a um estabelecimento, em uma competência, com o grupo de habilitação (`SGRUPHAB`), o período de vigência (`CMPT_INI`/`CMPT_FIM`) e a portaria que a concedeu. É a base que materializa as habilitações de alta complexidade e de serviços especializados previstas em portarias específicas do Ministério da Saúde.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/HB` | `HB` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `HBSP2401.dbc` — `HB` (Habilitações), `SP` (UF), `24` (ano), `01` (mês). Há também `HBBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-hb/<AAAAMM>/cnes-hb_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/cnes-hb/202401/cnes-hb_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Habilitações — HB*.dbf") e `TAB_CNES.zip` (tabela de grupos de habilitação e portarias).

## Conteúdo

O arquivo `HB` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS. As habilitações registram o reconhecimento formal, por portaria, de que um estabelecimento atende aos requisitos para ofertar serviços específicos — por exemplo, Unidade de Alta Complexidade em Oncologia (UNACON/CACON), Centro de Referência em Saúde do Trabalhador (CEREST), habilitação em alta complexidade cardiovascular, nefrologia, fisioterapia, entre outras.

O **evento gerador** é a concessão/mantenação da habilitação, refletida no SCNES a cada competência. A **unidade de análise é a habilitação de um estabelecimento na competência** (`CNES` + `SGRUPHAB` + `COMPETEN`). O código `SGRUPHAB` (4 dígitos) identifica o grupo/subgrupo de habilitação conforme a tabela de domínio do CNES; `CMPT_INI` e `CMPT_FIM` delimitam a validade da habilitação; `DTPORTAR`/`PORTARIA`/`MAPORTAR` documentam a portaria concessora; e `NULEITOS` registra a quantidade de leitos associada quando aplicável.

A série histórica no FTP começa em março de 2007. Como as habilitações dependem de portarias específicas que são publicadas e revogadas ao longo do tempo, a base funciona como um retrato mensal das habilitações vigentes. Não há diretório preliminar.

Aplicações analíticas típicas: mapeamento de estabelecimentos habilitados por tipo de serviço, distribuição regional de referências de alta complexidade, acompanhamento temporal de concessões e revogações de habilitações, apoio à regulação regional e à verificação de pré-requisitos para procedimentos de alta complexidade e custeio.

### Cobertura observada

- Índice do FTP (2026-10): 6345 arquivos, de 2007-03 a 2026-09, 27 UF(s) com arquivos, última atualização em 2026-10-15.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007-11 a 2026-01), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `SGRUPHAB` | String (4) | Código da habilitação (grupo/subgrupo) |
| `CMPT_INI` / `CMPT_FIM` | String (`AAAAMM`) | Competência inicial / final de vigência da habilitação |
| `DTPORTAR` | String (10) | Data da portaria (formato de data) |
| `PORTARIA` | String (50) | Identificação da portaria concessora |
| `MAPORTAR` | String (`AAAAMM`) | Data da portaria formatada como competência |
| `NULEITOS` | Inteiro | Quantidade de leitos associada à habilitação |
| `TP_PREST` | String (2) | Tipo de prestador |
| `VINC_SUS` | String (2) | Vínculo com o SUS: 1 - Sim, 0 - Não |
| `NAT_JUR` | String (4) | Natureza jurídica |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `TERCEIRO` | String (1) | O estabelecimento é terceiro: 1 - Sim, 0 - Não |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

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
| `nuleitos` | `NULEITOS` | inteiro | Quantidade de leitos | — | todos |
| `competen` | `COMPETEN` | texto | Ano e Mês de competência da informação (AAAAMM) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `nat_jur` | `NAT_JUR` | texto | Natureza Jurídica Regras Contratuais - Nomenclatura (RC*.dbf ) | — | 2013-01 a 2026-01 |

## No lake

- **Dataset no lake:** `datasus/cnes-hb`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): inteiro: 1, texto: 33.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `cnes-hb.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- as habilitações têm vigência, de modo que o recorte de um estabelecimento "habilitado" em determinada competência exige checar `CMPT_INI`/`CMPT_FIM`; um mesmo CNES pode acumular várias habilitações; o leiaute `HB` compartilha o bloco de habilitação com os arquivos `RC`, `GM`, `EE`, `EF` e `IN`, cujo significado difere apenas no contexto; e `PORTARIA`/`DTPORTAR` podem conter erros de digitação, exigindo tratamento textual. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 1 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/cnes-hb").glob("**/*.parquet"))
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
datasus-fetcher list cnes-hb

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync cnes-hb -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset cnes-hb
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/HB`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout HB) e `TAB_CNES.zip`
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
