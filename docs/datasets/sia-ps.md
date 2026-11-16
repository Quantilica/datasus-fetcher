---
dataset:
  id: sia-ps
  fonte: datasus
  titulo: Psicossocial
  resumo: sia-ps contém os registros Psicossociais do SIA/SUS, originados do Registro das Ações Ambulatoriais de Saúde — RAAS-PSI
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2012-11
    fim: em-curso
  unidade: um registro da RAAS psicossocial (ação de atenção psicossocial a um paciente)
  granularidade:
    espacial: estabelecimento (CNES) e município de atendimento e de residência; um arquivo por UF
    temporal: competência (mês) e data do atendimento
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e competência mensal (a produção ambulatorial de UFs grandes pode vir em partes com sufixo de letra)
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 47
  dados_pessoais:
  - coluna: cnpjcpf
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  - coluna: cns_pac
    categoria: Cartão Nacional de Saúde (CNS)
  - coluna: dtnasc
    categoria: data de nascimento
  - coluna: sit_rua
    categoria: situação de rua (dado sensível)
  eras:
  - desde: 2012-11
    mudanca: início da RAAS psicossocial no FTP
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Psicossocial (`sia-ps`)

## Resumo

`sia-ps` contém os registros **Psicossociais** do SIA/SUS, originados do Registro das Ações Ambulatoriais de Saúde — RAAS-PSI: cada linha é uma ação de atenção psicossocial prestada a um paciente (identificado por CNS codificado) em CAPS e demais pontos da Rede de Atenção Psicossocial, com dados de diagnóstico, origem do paciente, situação de rua, uso de drogas, local de realização e quantidade de atendimentos.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf / yearmonth`
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2012-11 a 2026-07 (conforme `index.json`; 27 UFs com arquivos; última atualização no FTP em 2026-09-14)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 4.394 arquivos (~3,3 GB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Não
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SIASUS/200801_/Doc`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SIASUS/200801_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `PS` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `PSSP2401.dbc` — `PS` (Psicossocial / RAAS-PSI) + `SP` (UF) + `24` (ano) + `01` (mês).
- **No armazenamento local do `datasus-fetcher`**: `data/sia-ps/<AAAAMM>/sia-ps_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sia-ps/202401/sia-ps_sp_202401_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## Conteúdo

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **registro de atendimento psicossocial** na RAAS (Registro das Ações Ambulatoriais de Saúde), módulo Atenção Psicossocial (RAAS-PSI), preenchido por CAPS, serviços residenciais terapêuticos, unidades de acolhimento e ambulatórios de saúde mental. A unidade de análise é o **registro de ação por paciente, procedimento e período** (`DT_INICIO`–`DT_FIM`), com `QTDATE` (quantidade de atendimentos) e `QTDPCN` (quantidade de pacientes) no leiaute.

O RAAS foi instituído em 2012 para substituir a produção em BPA/APAC de CAPS, no contexto da Rede de Atenção Psicossocial (Portaria GM/MS nº 3.088/2011). O inventário do FTP começa em 2012-11 e segue até 2026-07 (27 UFs, ~3,3 GB). Em relação ao PA, o PS oferece vínculo com a pessoa (CNS), situação de rua (`SIT_RUA`), tipo de droga (`TP_DROGA`) e `DESTINOPAC`, informações inexistentes no BPA-C.

Aplicações: perfil dos usuários de CAPS por diagnóstico (`CIDPRI`), sexo, idade e raça/cor; uso de substâncias (`TP_DROGA`) e população em situação de rua (`SIT_RUA`); origem e destino dos pacientes (`ORIGEM_PAC`, `DESTINOPAC`); cobertura de CAPS por município; intensidade do cuidado (atendimentos por paciente) e continuidade do tratamento; avaliação da desinstitucionalização e da articulação com a Atenção Básica (`COB_ESF`, `CNES_ESF`).

### Cobertura observada

- Índice do FTP (2026-10): 4421 arquivos, de 2012-11 a 2026-08, 27 UF(s) com arquivos, última atualização em 2026-10-30.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2012-12 a 2026-02), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Eras

- **2012-11**: início da RAAS psicossocial no FTP

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

46 colunas no arquivo de 2024-01 (`PSAC2401.dbc`), com leiaute distinto das APACs (sem prefixo `AP_`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES_EXEC` | String (7) | CNES do estabelecimento executor (CAPS ou outro serviço). |
| `GESTAO / UFMUN` | String (6) | Código do gestor e município do estabelecimento. |
| `DT_PROCESS` | String (AAAAMM) | Competência de processamento. |
| `DT_ATEND` | String (AAAAMM) | Competência do atendimento. |
| `CNS_PAC` | String (cifrado) | CNS do paciente, codificado pelo DATASUS no DBF. |
| `DTNASC / IDADEPAC / TPIDADEPAC` | String AAAAMMDD / String / String | Data de nascimento; idade e unidade da idade do paciente. |
| `SEXOPAC / RACACOR / ETNIA` | String | Sexo (`M`/`F`), raça/cor e etnia. |
| `MUNPAC` | String (6) | Município de residência do paciente. |
| `CIDPRI / CIDASSOC` | String (CID-10) | Diagnóstico principal e associado (p.ex. `F192`). |
| `ORIGEM_PAC / DESTINOPAC` | String | Origem do paciente (demanda espontânea, UBS, internação…) e destino após o atendimento. |
| `DT_INICIO / DT_FIM / INICIO / FIM` | String AAAAMMDD | Início e fim do acompanhamento/registro. |
| `PA_PROC_ID` | String (10) | Procedimento SIGTAP realizado. |
| `PA_QTDPRO / PA_QTDAPR` | String | Quantidade produzida e aprovada (note: `String` no DBF). |
| `SIT_RUA / TP_DROGA / LOC_REALIZ` | String | Situação de rua (`S`/`N`), tipo de droga (`A` álcool, `C` crack, `O` outras…) e local de realização (`C` CAPS, território…). |
| `QTDATE / QTDPCN / PERMANEN` | String | Quantidade de atendimentos, de pacientes e permanência no serviço. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `cnes_exec` | `CNES_EXEC` | texto | Código do SCNES do Estabelecimento de Saúde | — | todos |
| `gestao` | `GESTAO` | texto | Código da Unidade da Federação + Código do Município (IBGE) do Gestor, ou UF0000 se o estabelecimento estiver sob Gestão Estadual | — | todos |
| `condic` | `CONDIC` | texto | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado | — | todos |
| `ufmun` | `UFMUN` | texto | Código da Unidade da Federação + Código do Município onde está localizado o estabelecimento | — | todos |
| `tpups` | `TPUPS` | texto | Tipo de do Estabelecimento | — | todos |
| `tippre` | `TIPPRE` | texto | Tipo de Prestador | — | todos |
| `mn_ind` | `MN_IND` | texto | Estabelecimento Mantido / Individual | — | todos |
| `cnpjcpf` | `CNPJCPF` | texto | CNPJ do Estabelecimento executante | — | todos |
| `cnpjmnt` | `CNPJMNT` | texto | CNPJ da Mantenedora do Estabelecimento ou zeros, caso não a tenha | — | todos |
| `dt_process` | `DT_PROCESS` | data | Ano e mês de Processamento da produção (AAAAMM) | — | todos |
| `dt_atend` | `DT_ATEND` | data | Ano e mês do Atendimento (AAAAMM) | — | todos |
| `cns_pac` | `CNS_PAC` | texto | Número do CNS (Cartão Nacional de Saúde) do paciente (criptografia) | — | todos |
| `dtnasc` | `DTNASC` | texto | Data de nascimento do paciente | — | todos |
| `tpidadepac` | `TPIDADEPAC` | texto | Tipo da Idade do paciente em anos, meses ou dias. Calculado a partir da data de nascimento | — | todos |
| `idadepac` | `IDADEPAC` | texto | Idade do paciente | — | todos |
| `nacion_pac` | `NACION_PAC` | texto | Nacionalidade do paciente | — | todos |
| `sexopac` | `SEXOPAC` | texto | Sexo do paciente | — | todos |
| `racacor` | `RACACOR` | texto | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação | — | todos |
| `etnia` | `ETNIA` | texto | Conteúdo definido conforme Portaria SAS Nº 508, de 28 de Setembro de 2010. Anexo I. Preencher somente se o campo RACACOR for 05 - Indígena. A partir da competência Out/2010. | — | todos |
| `munpac` | `MUNPAC` | texto | Código da Unidade da Federação + Código do Município de residência do paciente ou do estabelecimento, caso não se tenha a identificação do paciente, o que ocorre no (BPA) | — | todos |
| `mot_cob` | `MOT_COB` | texto | Motivo de Saída/Permanência | — | todos |
| `dt_motcob` | `DT_MOTCOB` | texto | Data da ocorrência no caso de alta, transferência ou óbito | — | todos |
| `catend` | `CATEND` | texto | Caráter de Atendimento | — | todos |
| `cidpri` | `CIDPRI` | texto | CID Principal | — | todos |
| `cidassoc` | `CIDASSOC` | texto | CID Causas Associadas | — | todos |
| `origem_pac` | `ORIGEM_PAC` | texto | Origem do paciente | — | todos |
| `dt_inicio` | `DT_INICIO` | texto | Data de Início do Atendimento (DDMMAAAA) | — | todos |
| `dt_fim` | `DT_FIM` | texto | Data de Fim do Atendimento (DDMMAAAA) | — | todos |
| `cob_esf` | `COB_ESF` | texto | Indica se a região de atendimento do paciente tem cobertura de Estratégia Saúde da Família | — | todos |
| `cnes_esf` | `CNES_ESF` | texto | Código do SCNES do Estabelecimento de Saúde Unidade da Saúde da Família da região | — | todos |
| `destinopac` | `DESTINOPAC` | texto | Destino do paciente | — | todos |
| `pa_proc_id` | `PA_PROC_ID` | texto | Código do Procedimento Ambulatorial | — | todos |
| `pa_qtdpro` | `PA_QTDPRO` | texto | Quantidade Produzida (APRESENTADA) | — | todos |
| `pa_qtdapr` | `PA_QTDAPR` | texto | Quantidade Aprovada do procedimento | — | todos |
| `pa_srv` | `PA_SRV` | texto | Serviço Especializado | — | todos |
| `pa_class_s` | `PA_CLASS_S` | texto | Código da classificação do serviço especializado (CNES), no formato serviço+classificação (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `sit_rua` | `SIT_RUA` | texto | Situação de Rua (S- SIM, N - NÃO) | — | todos |
| `tp_droga` | `TP_DROGA` | texto | TIPO DE DROGA (A - Álcool, C - Crack, O - Outros) | — | todos |
| `loc_realiz` | `LOC_REALIZ` | texto | Local de Realização (C – CAPS, T - Território) | — | todos |
| `inicio` | `INICIO` | texto | Data de Início do Atendimento (DDMMAAAA) | — | todos |
| `fim` | `FIM` | texto | Data de Fim do Atendimento (DDMMAAAA) | — | todos |
| `permanen` | `PERMANEN` | texto | Permanência em Atendimento | — | todos |
| `qtdate` | `QTDATE` | texto | Quantidade de Atendimentos | — | todos |
| `qtdpcn` | `QTDPCN` | texto | Quantidade de pacientes | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `nat_jur` | `NAT_JUR` | texto | Código da Natureza Jurídica | — | 2019-11 a 2026-02 |

## No lake

- **Dataset no lake:** `datasus/sia-ps`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 2, texto: 45.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sia-ps.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) em alguns arquivos o cabeçalho DBF traz o nome do campo `TIPPRE` com espaços à direita (`'TIPPRE  '`) — aplique `strip()` aos nomes das colunas antes de selecionar; (ii) `PA_QTDPRO`/`PA_QTDAPR` são texto: use `cast(pl.Int64, strict=False)`; (iii) o CNS é codificado e serve apenas para contar pacientes distintos; (iv) um mesmo paciente tem várias linhas por competência (uma por procedimento/dia). (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 1 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sia-ps/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "mes", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "mes", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sia-ps
quantilica datasus list sia-ps

# 2. Baixar microdados de sia-ps com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sia-ps -o ./data --start 2024-01 --end 2024-12 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sia-ps -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sia-ps -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-12 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sia-ps/202401").glob("sia-ps_ac_202401_*.dbc"))
# clean=False para preservar DT_PROCESS/DT_ATEND (AAAAMM), que o saneamento padrão anularia
ps = df.read_dbc(arquivo, clean=False).rename(str.lower).filter(~pl.col("_deleted"))
ps = ps.with_columns(
    pl.col("dt_process").str.to_date("%Y%m", strict=False).alias("competencia"),
    pl.col("qtdate").cast(pl.Int64, strict=False),
)

# Atendimentos por CID principal e pacientes distintos
q = ps.group_by("cidpri").agg(
    pl.col("qtdate").sum().alias("atendimentos"),
    pl.col("cns_pac").n_unique().alias("pacientes"),
)
print(q.sort("atendimentos", descending=True).head(10))
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
- **Portaria GM/MS nº 3.088/2011** — institui a Rede de Atenção Psicossocial (RAPS): https://bvsms.saude.gov.br/bvs/saudelegis/gm/2011/prt3088_23_12_2011_rep.html
