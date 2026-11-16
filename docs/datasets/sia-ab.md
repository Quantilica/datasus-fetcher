---
dataset:
  id: sia-ab
  fonte: datasus
  titulo: APAC de Acompanhamento a Cirurgia Bariátrica
  resumo: sia-ab registra as APAC de Acompanhamento a Cirurgia Bariátrica do SIA/SUS
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2008-01
    fim: em-curso
  unidade: uma APAC de acompanhamento a cirurgia bariátrica, por competência
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
    colunas: 60
  unidades_de_medida:
    ap_vl_ap: R$ (reais)
  dados_pessoais:
  - coluna: ap_cnpjcpf
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  - coluna: ap_cnspcn
    categoria: Cartão Nacional de Saúde (CNS)
  - coluna: ap_ceppcn
    categoria: CEP
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# APAC de Acompanhamento a Cirurgia Bariátrica (`sia-ab`)

## Resumo

`sia-ab` registra as **APAC de Acompanhamento a Cirurgia Bariátrica** do SIA/SUS: cada linha é a cobrança mensal de uma APAC de seguimento de pacientes operados de obesidade grave, com os dados cadastrais da APAC e campos específicos (IMC, procedimento e data da cirurgia, AIH da cirurgia, tempo de acompanhamento).

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf / yearmonth`
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2008-01 a 2025-07 (conforme `index.json`; 18 UFs com arquivos; última atualização no FTP em 2026-02-10)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 635 arquivos (~16,1 MB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Não
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SIASUS/200801_/Doc`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SIASUS/200801_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `AB` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `ABSP2401.dbc` — `AB` (APAC de Acompanhamento a Cirurgia Bariátrica) + `SP` (UF) + `24` (ano) + `01` (mês). Disponível em `200801_/Dados`.
- **No armazenamento local do `datasus-fetcher`**: `data/sia-ab/<AAAAMM>/sia-ab_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/sia-ab/201001/sia-ab_sp_201001_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## Conteúdo

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **acompanhamento ambulatorial pré e pós-operatório da cirurgia bariátrica** realizada pelo SUS, autorizado por APAC (laudo para APAC no estabelecimento habilitado). A unidade de análise é a **APAC por competência**. A Autorização de Procedimentos de Alta Complexidade/Custo (APAC) é o instrumento de autorização e cobrança de procedimentos ambulatoriais de alta complexidade ou de uso continuado: o tratamento é autorizado por um gestor com validade de até três competências, e cada mês de cobrança gera uma linha no arquivo. A chave do registro é o número da APAC (`AP_AUTORIZ`, 13 dígitos) combinado com a competência (`AP_CMP`/`AP_MVM`); a APAC subsequente de um mesmo tratamento referencia a anterior em `AP_APACANT`. Os campos `AB_*` ligam a APAC à internação cirúrgica (`AB_NUMAIH`, `AB_PROCAIH`, `AB_DTCIRUR`) do SIH e registram o IMC (`AB_IMC`) e o tempo de acompanhamento (`AB_MESACOM`, `AB_ANOACOM`).

No FTP o dataset cobre 2008-01 a 2025-07 e tem arquivos para 18 UFs (inventário do FTP; as demais UFs não têm arquivos publicados). A reorganização da linha de cuidado da obesidade e da cirurgia bariátrica pelo Ministério da Saúde em 2013 (Portarias GM/MS nº 424 e nº 425/2013) levou à criação da APAC específica de acompanhamento **pós-**operatório, publicada no FTP como `sia-abo` desde 2014-01; o `sia-ab` permanece como série mais antiga e de menor volume (~16 MB no total). Os campos `AB_PRCAIH2…6`/`AB_T_PRC2…6` só existem nos leiautes recentes.

Aplicações: volume de pacientes em acompanhamento por serviço e UF; perfil de IMC e idade dos operados; tempo entre a cirurgia (`AB_DTCIRUR`) e o início do acompanhamento; elo com internações do SIH para analisar complicações e reoperações (`AB_NUMAIH2`, `AB_DTCIRG2`); avaliação do cumprimento do seguimento recomendado e do gasto com a linha de cuidado da obesidade.

### Cobertura observada

- Índice do FTP (2026-10): 635 arquivos, de 2008-01 a 2025-07, 18 UF(s) com arquivos, última atualização em 2026-02-10.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2008-08 a 2025-06), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

58 colunas no arquivo de 2010-01 (`ABSP1001.dbc`): 47 campos comuns de APAC (`AP_*`) mais os campos `AB_*`.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `AP_MVM / AP_CMP` | String (AAAAMM) | Mês de movimentação (processamento) e mês de competência da APAC. |
| `AP_AUTORIZ` | String (13) | Número da APAC (chave do tratamento); `AP_APACANT` aponta a APAC anterior do mesmo paciente/tratamento. |
| `AP_CODUNI` | String (7) | Código CNES do estabelecimento executor. |
| `AP_GESTAO / AP_UFMUN` | String (6) | Código do gestor e município do estabelecimento (IBGE 6 dígitos). |
| `AP_PRIPAL` | String (10) | Procedimento principal SIGTAP da APAC. |
| `AP_VL_AP` | Float | Valor (R$) aprovado da APAC na competência. |
| `AP_CNSPCN` | String (cifrado) | CNS do paciente — gravado de forma codificada pelo DATASUS no DBF; usar apenas como chave de pareamento, não como CNS legível. |
| `AP_SEXO / AP_COIDADE / AP_NUIDADE` | String | Sexo (`M`/`F`); unidade da idade (`4` = anos) e idade. |
| `AP_RACACOR / AP_ETNIA` | String | Raça/cor (`01`–`05`, `99`) e etnia indígena. |
| `AP_MUNPCN / AP_CEPPCN` | String (6 / 8) | Município de residência e CEP do paciente. |
| `AP_DTINIC / AP_DTFIM` | String AAAAMMDD | Início e fim da validade da APAC no período. |
| `AP_DTSOLIC / AP_DTAUT` | String AAAAMMDD | Datas de solicitação e de autorização. |
| `AP_CIDPRI / AP_CIDSEC / AP_CIDCAS` | String (CID-10) | Diagnóstico principal, secundário e causas associadas (`0000` = não informado). |
| `AP_MOTSAI / AP_OBITO / AP_ALTA / AP_TRANSF / AP_PERMAN / AP_ENCERR` | String | Motivo de saída/cobrança e indicadores de óbito, alta, transferência, permanência e encerramento (flags `0`/`1`). |
| `AP_TPATEN / AP_TPAPAC` | String | Tipo de atendimento e tipo da APAC (`1` inicial, `2` continuidade, `3` única). |
| `AP_NATJUR / AP_TPUPS / AP_TIPPRE` | String | Natureza jurídica, tipo de unidade e tipo de prestador do estabelecimento. |
| `AB_IMC` | String/Inteiro | Índice de massa corporal do paciente informado na APAC. |
| `AB_PROCAIH / AB_NUMAIH / AB_DTCIRUR` | String / String / AAAAMMDD | Procedimento SIGTAP, número da AIH e data da cirurgia bariátrica que originou o acompanhamento. |
| `AB_NUMAIH2 / AB_DTCIRG2` | String / AAAAMMDD | AIH e data de uma segunda cirurgia (reoperação), quando houver. |
| `AB_MESACOM / AB_ANOACOM` | String | Mês e ano de acompanhamento pós-operatório. |
| `AB_PONTBAR / AB_TABBARR` | String | Campos de pontuação/escala do paciente (ver Informe Técnico SIASUS). |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `ap_mvm` | `AP_MVM` | texto | Data de Processamento / Movimento (AAAAMM) | — | todos |
| `ap_condic` | `AP_CONDIC` | texto | Sigla do Tipo de Gestão no qual o Estado ou Município está habilitado | — | todos |
| `ap_gestao` | `AP_GESTAO` | texto | Código da Unidade de Federação + Código do Município de Gestão, ou UF0000 se o estabelecimento está sob Gestão Estadual | — | todos |
| `ap_coduni` | `AP_CODUNI` | texto | Código do Estabelecimento no CNES (Cadastro Nacional de Estabelecimentos de Saúde) | — | todos |
| `ap_autoriz` | `AP_AUTORIZ` | texto | Número da APAC. Lei de formação: UFAATsssssssd, onde: UF – Unid. da Federação, AA – ano, T – tipo, sssssss – sequencial, d – dígito | — | todos |
| `ap_cmp` | `AP_CMP` | texto | Data de Atendimento ao paciente / Competência (AAAAMM) | — | todos |
| `ap_pripal` | `AP_PRIPAL` | texto | Procedimento Principal da APAC | — | todos |
| `ap_vl_ap` | `AP_VL_AP` | decimal(20,2) | Valor Total da APAC Aprovado | — | todos |
| `ap_ufmun` | `AP_UFMUN` | texto | Código da Unidade da Federação + Código do Município do Estabelecimento | — | todos |
| `ap_tpups` | `AP_TPUPS` | texto | Tipo de Estabelecimento | — | todos |
| `ap_tippre` | `AP_TIPPRE` | texto | Tipo de Prestador | — | todos |
| `ap_mn_ind` | `AP_MN_IND` | texto | Estabelecimento Mantido / Individual | — | todos |
| `ap_cnpjcpf` | `AP_CNPJCPF` | texto | CNPJ do Estabelecimento executante | — | todos |
| `ap_cnpjmnt` | `AP_CNPJMNT` | texto | CNPJ da Mantenedora do estabelecimento ou zeros, caso não a tenha | — | todos |
| `ap_cnspcn` | `AP_CNSPCN` | texto | Número do CNS (Cartão Nacional de Saúde) do paciente | — | todos |
| `ap_coidade` | `AP_COIDADE` | texto | Código da Idade do paciente | — | todos |
| `ap_nuidade` | `AP_NUIDADE` | texto | Número da Idade | — | todos |
| `ap_sexo` | `AP_SEXO` | texto | Sexo do paciente | — | todos |
| `ap_racacor` | `AP_RACACOR` | texto | Raça/Cor do paciente: 01 - Branca, 02 - Preta, 03 - Parda, 04 - Amarela, 05 - Indígena, 99 - Sem informação | — | todos |
| `ap_munpcn` | `AP_MUNPCN` | texto | Código da Unidade de Federação + Código Município de Residência do paciente | — | todos |
| `ap_ufnacio` | `AP_UFNACIO` | texto | Código da Nacionalidade do paciente | — | todos |
| `ap_ceppcn` | `AP_CEPPCN` | texto | CEP do endereço do paciente | — | todos |
| `ap_ufdif` | `AP_UFDIF` | texto | Indica se a UF de residência do paciente é diferente da UF de localização do estabelecimento: 0 = mesma UF; 1 = UF diferente | — | todos |
| `ap_mndif` | `AP_MNDIF` | texto | Indica se o município de residência do paciente é diferente do município de localização do estabelecimento: 0 = mesmo município; 1 = município diferente | — | todos |
| `ap_dtinic` | `AP_DTINIC` | texto | Data de INÍCIO validade (AAAAMMDD) | — | todos |
| `ap_dtfim` | `AP_DTFIM` | texto | Data de FIM validade (AAAAMMDD) | — | todos |
| `ap_tpaten` | `AP_TPATEN` | texto | Tipo de Atendimento de APAC | — | todos |
| `ap_tpapac` | `AP_TPAPAC` | texto | Indica se a APAC é 1 - inicial, 2 - continuidade, 3 - única | — | todos |
| `ap_motsai` | `AP_MOTSAI` | texto | Motivo de Saída e Permanência | — | todos |
| `ap_obito` | `AP_OBITO` | texto | Indicador de Óbito | — | todos |
| `ap_encerr` | `AP_ENCERR` | texto | Indicador de Encerramento | — | todos |
| `ap_perman` | `AP_PERMAN` | texto | Indicador de Permanência | — | todos |
| `ap_alta` | `AP_ALTA` | texto | Indicador de Alta | — | todos |
| `ap_transf` | `AP_TRANSF` | texto | Indicador de Transferência | — | todos |
| `ap_dtocor` | `AP_DTOCOR` | texto | Data de Ocorrência que substitui a data de FIM de validade | — | todos |
| `ap_codemi` | `AP_CODEMI` | texto | Código do Órgão emissor | — | todos |
| `ap_catend` | `AP_CATEND` | texto | Caráter do Atendimento | — | todos |
| `ap_apacant` | `AP_APACANT` | texto | Número APAC Anterior | — | todos |
| `ap_unisol` | `AP_UNISOL` | texto | Código do Estabelecimento solicitante no CNES (Cadastro Nacional de Estabelecimentos de Saúde) | — | todos |
| `ap_dtsolic` | `AP_DTSOLIC` | texto | Data da Solicitação (AAAAMMDD) | — | todos |
| `ap_dtaut` | `AP_DTAUT` | texto | Data da Autorização (AAAAMMDD) | — | todos |
| `ap_cidcas` | `AP_CIDCAS` | texto | CID Causas Associadas | — | todos |
| `ap_cidpri` | `AP_CIDPRI` | texto | CID Principal | — | todos |
| `ap_cidsec` | `AP_CIDSEC` | texto | CID Secundário | — | todos |
| `ap_etnia` | `AP_ETNIA` | texto | Etnia do paciente | — | todos |
| `ab_imc` | `AB_IMC` | texto | IMC do paciente | — | todos |
| `ab_procaih` | `AB_PROCAIH` | texto | Procedimento do AIH | — | todos |
| `ab_dtcirur` | `AB_DTCIRUR` | texto | Data da Cirurgia | — | todos |
| `ab_numaih` | `AB_NUMAIH` | texto | Número da AIH | — | todos |
| `ab_prcaih2` | `AB_PRCAIH2` | texto | Procedimento do AIH | — | todos |
| `ab_prcaih3` | `AB_PRCAIH3` | texto | Procedimento do AIH | — | todos |
| `ab_numaih2` | `AB_NUMAIH2` | texto | Número da AIH | — | todos |
| `ab_dtcirg2` | `AB_DTCIRG2` | texto | Data da Cirurgia | — | todos |
| `ab_mesacom` | `AB_MESACOM` | texto | Número em MESES de Acompanhamento | — | todos |
| `ab_anoacom` | `AB_ANOACOM` | texto | Ano de Acompanhamento | — | todos |
| `ab_pontbar` | `AB_PONTBAR` | texto | Pontuação de Baros12 | — | todos |
| `ab_tabbarr` | `AB_TABBARR` | texto | Tabela de Baros | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `ap_natjur` | `AP_NATJUR` | texto | Código da Natureza Jurídica | — | 2025-06 a 2025-06 |

## No lake

- **Dataset no lake:** `datasus/sia-ab`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): decimal(20,2): 1, texto: 59.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sia-ab.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) as colunas `AB_*` pertencem apenas a esta APAC e não existem em outros arquivos do SIA; (ii) combine com `sih-rd` pelo número da AIH (`AB_NUMAIH` ↔ `N_AIH`) para estudar a internação cirúrgica; (iii) o mesmo paciente aparece em várias competências — use `AP_AUTORIZ` e o CNS codificado (`AP_CNSPCN`) para contar pacientes distintos, e `AP_TPAPAC` para identificar APAC inicial/continuidade; (iv) apenas 18 UFs têm arquivos publicados; a ausência de uma UF não deve ser lida como zero casos. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 1 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sia-ab/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "mes", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "mes", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sia-ab
quantilica datasus list sia-ab

# 2. Baixar microdados de sia-ab com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync sia-ab -o ./data --start 2024-01 --end 2025-07 --regions sp mg

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sia-ab -o ./data --start 2024-01 --end 2025-07 --regions sp mg --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sia-ab -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2025-07 --regions sp mg
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/sia-ab/201001").glob("sia-ab_sp_201001_*.dbc"))
ab = df.read_dbc(arquivo, dataset="sia-ab")

# Pacientes em acompanhamento por estabelecimento e IMC médio
resumo = (
    ab.group_by("ap_coduni")
    .agg(
        pl.len().alias("apacs"),
        pl.col("ab_imc").cast(pl.Float64, strict=False).mean().alias("imc_medio"),
    )
    .sort("apacs", descending=True)
)
print(resumo.head(10))
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
