---
dataset:
  id: sia-atd
  fonte: datasus
  titulo: APAC de Tratamento Dialítico
  resumo: 'APAC de Tratamento Dialítico do DATASUS: uma APAC de tratamento dialítico, por competência.'
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2014-08
    fim: em-curso
  unidade: uma APAC de tratamento dialítico, por competência
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
    colunas: 67
  unidades_de_medida:
    ap_vl_ap: R$ (reais)
  dados_pessoais:
  - coluna: ap_cnpjcpf
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  - coluna: ap_cnspcn
    categoria: Cartão Nacional de Saúde (CNS)
  - coluna: ap_ceppcn
    categoria: CEP
  eras:
  - desde: 2014-08
    mudanca: início da APAC de tratamento dialítico, que substitui `sia-an`
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# APAC de Tratamento Dialítico (`sia-atd`)

## Resumo

`sia-atd` contém as **APAC de Tratamento Dialítico** do SIA/SUS: cada linha é a cobrança mensal de uma APAC de terapia renal substitutiva (hemodiálise e diálise peritoneal), com indicadores laboratoriais e de qualidade da diálise. Substitui, a partir de 2014-08, a antiga APAC de Nefrologia (`sia-an`).

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/SIASUS/200801_/Doc`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SIASUS/200801_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `ATD` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `ATDSP2401.dbc` — `ATD` (APAC de Tratamento Dialítico) + `SP` (UF) + `24` + `01`. Prefixo de 3 letras.
- **No armazenamento local do `datasus-fetcher`**: `data/sia-atd/<AAAAMM>/sia-atd_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sia-atd/202401/sia-atd_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## Conteúdo

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é o **tratamento dialítico de pacientes com doença renal crônica**, autorizado por APAC específica criada na reorganização de 2014. A unidade de análise é a **APAC por competência**. A Autorização de Procedimentos de Alta Complexidade/Custo (APAC) é o instrumento de autorização e cobrança de procedimentos ambulatoriais de alta complexidade ou de uso continuado: o tratamento é autorizado por um gestor com validade de até três competências, e cada mês de cobrança gera uma linha no arquivo. A chave do registro é o número da APAC (`AP_AUTORIZ`, 13 dígitos) combinado com a competência (`AP_CMP`/`AP_MVM`); a APAC subsequente de um mesmo tratamento referencia a anterior em `AP_APACANT`. Os campos `ATD_*` registram hemoglobina, fósforo, Kt/V semanal (`ATD_KTVSEM`), taxa de redução da ureia (`ATD_TRU`), albumina, paratormônio (`ATD_PTH`), sorologias (HIV, HCV, HBsAg), acesso vascular (`ATD_ACEVAS`) e intercorrências (`ATD_INTERC`, `ATD_SEPERI`).

No FTP cobre 2014-08 a 2026-07 (27 UFs, ~1,05 GB). Em 2014 foi reorganizada a Linha de Cuidado da Doença Renal Crônica, com criação de APAC específicas (diálise e fístula) em substituição à APAC de nefrologia (`sia-an`, até 2014-10). A base continua ativa e é a principal fonte administrativa da terapia renal substitutiva no SUS.

Aplicações: prevalência de pacientes em diálise por UF/serviço; indicadores de qualidade (Kt/V, TRU, hemoglobina, fósforo, PTH, albumina) conforme metas regulatórias; proporção de acesso vascular definitivo; cobertura de sorologias; gasto com TRS; e série histórica concatenando `sia-an` (2008–2014) e `sia-atd` (2014 em diante).

### Cobertura observada

- Índice do FTP (2026-10): 3911 arquivos, de 2014-08 a 2026-08, 27 UF(s) com arquivos, última atualização em 2026-10-30.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2014-11 a 2026-08), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Eras

- **2014-08**: início da APAC de tratamento dialítico, que substitui `sia-an`

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

66 colunas no arquivo de 2024-01 (`ATDAC2401.dbc`).

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
| `ATD_CARACT` | String | Caráter do atendimento/tratamento dialítico. |
| `ATD_DTPDR / ATD_DTCLI` | String AAAAMMDD | Datas de referência do tratamento (início da terapia e de ingresso na clínica; ver Informe Técnico). |
| `ATD_ACEVAS` | String | Acesso vascular utilizado. |
| `ATD_HB / ATD_FOSFOR / ATD_PTH / ATD_ALBUMI` | String | Hemoglobina, fósforo, paratormônio e albumina. |
| `ATD_KTVSEM / ATD_TRU` | String | Kt/V semanal e taxa de redução da ureia. |
| `ATD_HIV / ATD_HCV / ATD_HBSAG` | String (`S`/`N`) | Sorologias. |
| `ATD_SITTRA / ATD_INTERC / ATD_SEPERI` | String | Situação de transplante e intercorrências/separação do tratamento (domínios do Informe Técnico). |

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
| `atd_caract` | `ATD_CARACT` | texto | Característica do tratamento | — | todos |
| `atd_dtpdr` | `ATD_DTPDR` | texto | Data (AAAAMMDD) do início da primeira dialise | — | todos |
| `atd_dtcli` | `ATD_DTCLI` | texto | Data (AAAAMMDD) do início da dialise nesta clinica | — | todos |
| `atd_acevas` | `ATD_ACEVAS` | texto | Acesso Vascular | — | todos |
| `atd_maisne` | `ATD_MAISNE` | texto | Acompanhado há mais de um ano com nefrologia (S - Sim, N - Não, I - Ignorado) | — | todos |
| `atd_sitini` | `ATD_SITINI` | texto | Situação Inicial | — | todos |
| `atd_sittra` | `ATD_SITTRA` | texto | Situação de transplante (1 - Apto, 2 - Inapto, 3 - Recusa, 4 - N/A caso novo, com menos de 90 dias de tratamento) | — | todos |
| `atd_seapto` | `ATD_SEAPTO` | texto | Se Apto a transplante (1 - Inscrito na CNCDO, 2 - Em processo de avaliação transplantante no centro transplantador, 3 - Sem encaminhamento, 4 - Aguardando agendamento de consulta no centro transplantador) | — | todos |
| `atd_hb` | `ATD_HB` | texto | HB (hemoglobina) | — | todos |
| `atd_fosfor` | `ATD_FOSFOR` | texto | Fósforo | — | todos |
| `atd_ktvsem` | `ATD_KTVSEM` | texto | Kt/v Semanal | — | todos |
| `atd_tru` | `ATD_TRU` | texto | TRU (taxa de redução de ureia) | — | todos |
| `atd_albumi` | `ATD_ALBUMI` | texto | Albumina | — | todos |
| `atd_pth` | `ATD_PTH` | texto | PTH (hormônio da paratireoide) | — | todos |
| `atd_hiv` | `ATD_HIV` | texto | Indicativo de presença de anticorpos de HIV (P - Positivo; N - Negativo) | — | todos |
| `atd_hcv` | `ATD_HCV` | texto | Indicativo de presença de anticorpos de HCV (P - Positivo; N - Negativo) | — | todos |
| `atd_hbsag` | `ATD_HBSAG` | texto | Indicativo de HBsAg (P - Positivo; N - Negativo) | — | todos |
| `atd_interc` | `ATD_INTERC` | texto | Usuário internado, com data de início no mês vigente, para tratamento de intercorrência clínica? (S – Sim, N - Não, I - Ignorado) | — | todos |
| `atd_seperi` | `ATD_SEPERI` | texto | Se em Diálise Peritoneal, houve peritonite diagnosticada no mês vigente? (S - Sim, N - Não, I - Ignorado) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `ap_natjur` | `AP_NATJUR` | texto | Código da Natureza Jurídica | — | 2018-02 a 2026-08 |

## No lake

- **Dataset no lake:** `datasus/sia-atd`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): decimal(20,2): 1, texto: 66.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sia-atd.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) para séries anteriores a 2014-08 use `sia-an`; na janela 2014-08 a 2014-10 ambos coexistem; (ii) valores laboratoriais `0` ou vazio significam "não informado" e devem ser tratados como `null` antes de calcular médias; (iii) a descrição dos campos `ATD_*` baseia-se nos nomes e no Informe Técnico — valide os domínios; (iv) `AP_TPAPAC` distingue APAC inicial de continuidade. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 1 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sia-atd").glob("**/*.parquet"))
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
datasus-fetcher list sia-atd

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sia-atd -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sia-atd
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
