---
dataset:
  id: cnes-sr
  fonte: datasus
  titulo: Serviço Especializado
  resumo: 'Serviço Especializado do DATASUS: um serviço especializado e sua classificação em um estabelecimento, em uma competência.'
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2005-08
    fim: em-curso
  unidade: um serviço especializado e sua classificação em um estabelecimento, em uma competência
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
  dados_pessoais:
  - coluna: cpf_cnpj
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Serviço Especializado (`cnes-sr`)

## Resumo

O `cnes-sr` contém os microdados do arquivo de **Serviço Especializado** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra os serviços especializados ofertados pelos estabelecimentos. Cada registro (linha) representa um **serviço/classificação** (`SERV_ESP` + `CLASS_SR`) oferecido por um estabelecimento, em uma competência mensal, com a caracterização do serviço e a indicação do tipo de atendimento (ambulatorial/hospitalar e SUS/não SUS). É a base para mapear a oferta de serviços especializados, de referência e de alta complexidade.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/SR` | `SR` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `SRSP2401.dbc` — `SR` (Serviço Especializado), `SP` (UF), `24` (ano), `01` (mês). Há também `SRBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-sr/<AAAAMM>/cnes-sr_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/cnes-sr/202401/cnes-sr_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Serviço Especializado — SR*.dbf") e `TAB_CNES.zip` (tabelas de serviços/classificações).

## Conteúdo

O arquivo `SR` integra o CNES (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015), mantido pelo Ministério da Saúde/DATASUS e alimentado pelos estabelecimentos no SCNES. Os serviços especializados cadastrados são a base para habilitar o estabelecimento a ofertar determinados procedimentos e para a organização da Rede de Atenção à Saúde (RAS), incluindo serviços de referência (oncologia, cardiologia, nefrologia, saúde mental, reabilitação, entre outros).

O **evento gerador** é a declaração dos serviços na FCES/SCNES a cada competência. A **unidade de análise é o serviço/classificação de um estabelecimento na competência** (`CNES` + `SERV_ESP` + `CLASS_SR` + `COMPETEN`). `SERV_ESP` é o código do serviço especializado e `CLASS_SR` a classificação dentro do serviço (usando `999` quando inexistente). O campo `CARACTER` caracteriza o serviço e `AMB_HOSP` indica se o atendimento é ambulatorial SUS, ambulatorial não SUS, hospitalar SUS ou hospitalar não SUS. `CNESTERC` referencia o CNES de um estabelecimento terceiro quando o serviço é prestado por terceiros.

A série histórica no FTP começa em agosto de 2005. As tabelas de serviços e classificações evoluíram com as portarias do Ministério da Saúde (recomposições periódicas das tabelas de serviços/classificações, como a Portaria SAS/MS nº 154/2008). Não há diretório preliminar.

Aplicações analíticas típicas: distribuição regional de serviços especializados e de alta complexidade, identificação de estabelecimentos de referência, análise da oferta de serviços por tipo de atendimento (SUS vs. não SUS), apoio à regulação e à pactuação de referências e integração com SIA/SIH para verificar a oferta declarada versus a produção realizada.

### Cobertura observada

- Índice do FTP (2026-10): 6856 arquivos, de 2005-08 a 2026-09, 27 UF(s) com arquivos, última atualização em 2026-10-15.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2005-08 a 2026-01), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `SERV_ESP` | String (3) | Código do serviço especializado |
| `CLASS_SR` | String (3) | Código da classificação do serviço (ou `999` se inexistente) |
| `SRVUNICO` | String (3) | Código do serviço especializado único |
| `CARACTER` | String (1) | Caracterização do serviço |
| `AMB_HOSP` | String (4) | Ambulatorial/hospitalar e SUS/não SUS (1 - Sim, 0 - Não) |
| `CNESTERC` | String (7) | CNES do estabelecimento terceiro |
| `NAT_JUR` | String (4) | Natureza jurídica |
| `TP_UNID` | String (2) | Tipo de unidade (estabelecimento) |
| `TPGESTAO` | String (1) | Tipo de gestão de saúde |
| `NIV_DEP` | String (1) | Grau de dependência: 1 - Individual, 3 - Mantida |
| `TERCEIRO` | String (1) | O estabelecimento é terceiro: 1 - Sim, 0 - Não |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `cnes` | `CNES` | texto | Número nacional do estabelecimento de saúde | — | todos |
| `codufmun` | `CODUFMUN` | texto | Código do município do estabelecimento UF+ MUNIC (sem dígito) | — | todos |
| `serv_esp` | `SERV_ESP` | texto | Código do serviço especializado | — | todos |
| `class_sr` | `CLASS_SR` | texto | Código da classificação do serviço ou ‘999’, caso INEXISTENTE | — | todos |
| `srvunico` | `SRVUNICO` | texto | Código do serviço especializado ÚNICO (O PREENCHIMENTO deste campo acontece somente uma vez por chave única CNES + SERV_ESP) | — | todos |
| `regsaude` | `REGSAUDE` | texto | Código da região de saúde | — | todos |
| `micr_reg` | `MICR_REG` | texto | Código da micro-região de saúde | — | todos |
| `distrsan` | `DISTRSAN` | texto | Código do distrito sanitário | — | todos |
| `distradm` | `DISTRADM` | texto | Código do distrito administrativo | — | todos |
| `tpgestao` | `TPGESTAO` | texto | Gestão de saúde | — | todos |
| `pf_pj` | `PF_PJ` | texto | Indicador de pessoa: 1-Física 3-Jurídica | — | todos |
| `cpf_cnpj` | `CPF_CNPJ` | texto | CPF do Estabelecimento, caso pessoa física ou CNPJ, caso pessoa jurídica | — | todos |
| `niv_dep` | `NIV_DEP` | texto | Grau de dependência, onde: 1-Individual 3-Mantida | — | todos |
| `esfera_a` | `ESFERA_A` | texto | Código da esfera administrativa | — | todos |
| `atividad` | `ATIVIDAD` | texto | Código da atividade de ensino | — | todos |
| `retencao` | `RETENCAO` | texto | Código de retenção de tributos | — | todos |
| `natureza` | `NATUREZA` | texto | Código da natureza da organização | — | todos |
| `clientel` | `CLIENTEL` | texto | Código de fluxo da clientela | — | todos |
| `tp_unid` | `TP_UNID` | texto | Tipo de unidade (Estabelecimento) | — | todos |
| `turno_at` | `TURNO_AT` | texto | Código de turno de atendimento | — | todos |
| `niv_hier` | `NIV_HIER` | texto | Código do nível de hierarquia | — | todos |
| `terceiro` | `TERCEIRO` | texto | O estabelecimento é terceiro: 1-Sim 0-Não | — | todos |
| `cnpj_man` | `CNPJ_MAN` | texto | CNPJ da mantenedora do estabelecimento | — | todos |
| `caracter` | `CARACTER` | texto | Caracterização do serviço | — | todos |
| `amb_nsus` | `AMB_NSUS` | texto | Serviço ofertado no atendimento ambulatorial não SUS (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `amb_sus` | `AMB_SUS` | texto | Serviço ofertado no atendimento ambulatorial SUS (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `hosp_nsus` | `HOSP_NSUS` | texto | Serviço ofertado no atendimento hospitalar não SUS (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `hosp_sus` | `HOSP_SUS` | texto | Serviço ofertado no atendimento hospitalar SUS (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `competen` | `COMPETEN` | texto | Ano e Mês de competência da informação (AAAAMM) | — | todos |
| `contsrvu` | `CONTSRVU` | texto | INDICADOR de serviço especializado ÚNICO | — | todos |
| `cnesterc` | `CNESTERC` | texto | Número nacional do estabelecimento de saúde TERCEIRO | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `nat_jur` | `NAT_JUR` | texto | Natureza Jurídica de Equipes - Nomenclatura (EP*.dbf) | — | 2016-01 a 2026-01 |

## No lake

- **Dataset no lake:** `datasus/cnes-sr`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): texto: 34.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `cnes-sr.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- como um estabelecimento pode ofertar vários serviços/classificações, a contagem de "serviços" exige agrupar por `SERV_ESP`; `AMB_HOSP` é um código de 4 caracteres que representa combinações de flags e precisa de dicionário; códigos de serviço são recompostos por portaria periodicamente, exigindo mapeamentos históricos; e `CNESTERC` revela arranjos de terceirização que devem ser considerados ao atribuir produção ao estabelecimento. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 1 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/cnes-sr").glob("**/*.parquet"))
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
datasus-fetcher list cnes-sr

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync cnes-sr -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset cnes-sr
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/SR`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout SR) e `TAB_CNES.zip`
- **Portaria SAS/MS nº 154/2008** (recomposição da Tabela de Serviços/Classificações) e **Portaria GM/MS nº 1.646/2015**
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
