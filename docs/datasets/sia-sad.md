---
dataset:
  id: sia-sad
  fonte: datasus
  titulo: Atenção Domiciliar
  resumo: 'Atenção Domiciliar do DATASUS: um registro da RAAS de atenção domiciliar.'
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2012-04
    fim: 2018-10
  unidade: um registro da RAAS de atenção domiciliar
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
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Atenção Domiciliar (`sia-sad`)

## Resumo

`sia-sad` reúne os registros de **Atenção Domiciliar** do SIA/SUS, originados da RAAS-AD (Registro das Ações Ambulatoriais de Saúde — Atenção Domiciliar) entre 2012 e 2018: cada linha é uma ação de assistência domiciliar a um paciente (CNS codificado), com equipe, CID, origem do paciente e quantidades.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/SIASUS/200801_/Doc`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SIASUS/200801_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `SAD` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `SADSP1401.dbc` — `SAD` (Atenção Domiciliar / RAAS-AD) + `SP` (UF) + `14` (ano 2014) + `01` (mês). Prefixo de 3 letras.
- **No armazenamento local do `datasus-fetcher`**: `data/sia-sad/<AAAAMM>/sia-sad_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sia-sad/202401/sia-sad_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## Conteúdo

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **atendimento domiciliar** prestado por equipes do Programa Melhor em Casa (EMAD/EMAP) e serviços de atenção domiciliar, registrado na RAAS-AD. A unidade de análise é o **registro de ação por paciente, procedimento e período** (`DT_INICIO`–`DT_FIM`), com `QTDATE` e `QTDPCN`; os campos `PA_EQUIPE`/`PA_TP_EQP` identificam a equipe e `PA_CID` o CID do atendimento.

O FTP só traz competências de 2012-04 a 2018-10 (25 UFs, ~53 MB; última atualização em 2020): é um dataset **descontinuado** na publicação do SIA. A atenção domiciliar foi regulamentada pelo SUS a partir da Portaria GM/MS nº 2.527/2011 e redefinida na Portaria GM/MS nº 825/2016 (Programa Melhor em Casa). Depois de 2018 os registros não são mais publicados neste arquivo; consulte o `sia-pa` e o e-SUS/SISAB para a atenção domiciliar mais recente.

Aplicações: cobertura e produção de equipes de atenção domiciliar por município; perfil dos usuários (CID, idade, sexo); substituição de internações por atendimento domiciliar (cruzar com `sih-rd`); intensidade do cuidado; distribuição de EMAD/EMAP; e avaliação do Programa Melhor em Casa.

### Cobertura observada

- Índice do FTP (2026-10): 1088 arquivos, de 2012-04 a 2018-10, 25 UF(s) com arquivos, última atualização em 2020-01-10.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2012-07 a 2018-01), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

44 colunas no arquivo de 2014-01 (`SADAC1401.dbc`), com o mesmo leiaute-base do `sia-ps` e campos próprios de equipe.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES_EXEC` | String (7) | CNES do estabelecimento executor. |
| `GESTAO / UFMUN` | String (6) | Código do gestor e município do estabelecimento. |
| `DT_PROCESS / DT_ATEND` | String (AAAAMM) | Competência de processamento e do atendimento. |
| `CNS_PAC` | String (cifrado) | CNS do paciente, codificado. |
| `DTNASC / IDADEPAC / TPIDADEPAC` | String | Data de nascimento (`AAAAMMDD`), idade e unidade da idade. |
| `SEXOPAC / RACACOR` | String | Sexo (`M`/`F`) e raça/cor. |
| `MUNPAC` | String (6) | Município de residência do paciente. |
| `CIDPRI / CIDASSOC / PA_CID` | String (CID-10) | Diagnóstico principal, associado e CID do atendimento. |
| `ORIGEM_PAC / DESTINOPAC` | String | Origem do paciente e destino após a atenção domiciliar. |
| `DT_INICIO / DT_FIM` | String AAAAMMDD | Início e fim da assistência. |
| `PA_PROC_ID` | String (10) | Procedimento SIGTAP (visita domiciliar, atendimento fisioterapêutico, etc.). |
| `PA_QTDPRO / PA_QTDAPR` | String | Quantidade produzida e aprovada. |
| `PA_EQUIPE / PA_TP_EQP` | String | Equipe (INE) e tipo de equipe (EMAD, EMAP). |
| `QTDATE / QTDPCN` | String | Quantidade de atendimentos e de pacientes. |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `cnes_exec` | `CNES_EXEC` | texto | Código do SCNES do Estabelecimento de Saúde | — | todos |
| `gestao` | `GESTAO` | texto | Código da Unidade da Federação + Código do Município (IBGE) do Gestor, ou UF0000 se o estabelecimento estiver sob Gestão Estadual | — | todos |
| `condic` | `CONDIC` | texto | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado | — | todos |
| `ufmun` | `UFMUN` | texto | Código da Unidade da Federação + Código do Município onde está localizado o estabelecimento | — | todos |
| `tpups` | `TPUPS` | texto | Tipo de do Estabelecimento | — | todos |
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
| `pa_equipe` | `PA_EQUIPE` | texto | Código da Equipe (somente para o Instrumento de registro RAAS) | — | todos |
| `pa_tp_eqp` | `PA_TP_EQP` | texto | Tipo de Equipe (somente para o Instrumento de registro RAAS) | — | todos |
| `pa_cid` | `PA_CID` | texto | CID do Procedimento | — | todos |
| `inicio` | `INICIO` | texto | Data de Início do Atendimento (DDMMAAAA) | — | todos |
| `fim` | `FIM` | texto | Data de Fim do Atendimento (DDMMAAAA) | — | todos |
| `permanen` | `PERMANEN` | texto | Permanência em Atendimento | — | todos |
| `qtdate` | `QTDATE` | texto | Quantidade de Atendimentos | — | todos |
| `qtdpcn` | `QTDPCN` | texto | Quantidade de pacientes | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `co_ine` | `CO_INE` | texto | Código INE (Identificador Nacional de Equipes) da equipe que prestou o atendimento (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2015-02 a 2018-01 |
| `nat_jur` | `NAT_JUR` | texto | Código da Natureza Jurídica | — | 2017-03 a 2018-01 |

## No lake

- **Dataset no lake:** `datasus/sia-sad`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 2, texto: 45.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sia-sad.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) série **encerrada** em 2018-10; (ii) 25 UFs com arquivos; (iii) `PA_QTDPRO`/`PA_QTDAPR`/`QTDATE`/`QTDPCN` são texto — converta para `Int64`; (iv) o CNS é codificado, serve apenas para contar pacientes distintos. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 2 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sia-sad").glob("**/*.parquet"))
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
datasus-fetcher list sia-sad

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sia-sad -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sia-sad
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
- **Portarias GM/MS nº 2.527/2011 e nº 825/2016** (Atenção Domiciliar / Programa Melhor em Casa), na Biblioteca Virtual em Saúde: https://bvsms.saude.gov.br/
