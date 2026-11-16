---
dataset:
  id: sia-acf
  fonte: datasus
  titulo: APAC Confeção de Fístula Arteriovenosa
  resumo: 'APAC Confeção de Fístula Arteriovenosa do DATASUS: uma APAC de confecção de fístula arteriovenosa.'
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2014-08
    fim: em-curso
  unidade: uma APAC de confecção de fístula arteriovenosa
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
    colunas: 58
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

# APAC Confeção de Fístula Arteriovenosa (`sia-acf`)

## Resumo

`sia-acf` contém as **APAC de Confecção de Fístula Arteriovenosa** do SIA/SUS: cada linha é a cobrança de uma APAC para a confecção/revisão de acesso vascular (fístula arteriovenosa) de pacientes em terapia renal substitutiva, com campos clínicos do procedimento (duplex, uso prévio de cateter, complicações).

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/SIASUS/200801_/Doc`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SIASUS/200801_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIASUS/200801_/Dados` | `ACF` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `ACFSP2401.dbc` — `ACF` (APAC Confecção de Fístula Arteriovenosa) + `SP` (UF) + `24` + `01`.
- **No armazenamento local do `datasus-fetcher`**: `data/sia-acf/<AAAAMM>/sia-acf_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sia-acf/202401/sia-acf_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Informe_Tecnico_SIASUS_2019_07.pdf` (~1,1 MB, julho/2019) descreve o leiaute dos arquivos do SIA; `Auxiliar/TAB_SIA.zip` (~73,8 MB, tabelas SIGTAP e conversores) e as versões históricas `TAB_SIA_199407-199910.zip`, `TAB_SIA_199911-200307.zip` e `TAB_SIA_200308-200712.zip` cobrem as fases anteriores à Tabela Unificada.

## Conteúdo

O Sistema de Informações Ambulatoriais do SUS (SIA/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) —, com processamento e disseminação a cargo do DATASUS. Sua finalidade é registrar, validar e remunerar a produção ambulatorial financiada pelo SUS (consultas, exames, terapias, procedimentos de média e alta complexidade, medicamentos do componente especializado e ações de reabilitação), permitindo ao gestor acompanhar a oferta, a cobertura e o gasto ambulatorial por estabelecimento, município e procedimento.

O evento gerador é a **cirurgia ambulatorial de confecção de fístula arteriovenosa (FAV)** para hemodiálise, autorizada por APAC específica. A unidade de análise é a **APAC por competência**. A Autorização de Procedimentos de Alta Complexidade/Custo (APAC) é o instrumento de autorização e cobrança de procedimentos ambulatoriais de alta complexidade ou de uso continuado: o tratamento é autorizado por um gestor com validade de até três competências, e cada mês de cobrança gera uma linha no arquivo. A chave do registro é o número da APAC (`AP_AUTORIZ`, 13 dígitos) combinado com a competência (`AP_CMP`/`AP_MVM`); a APAC subsequente de um mesmo tratamento referencia a anterior em `AP_APACANT`. Os campos `ACF_*` registram achados do pré e pós-operatório: realização de duplex, uso prévio de cateter, FAV prévia, flebite, hematoma, diâmetro de veia/artéria, frêmito e pulso.

No FTP cobre 2014-08 a 2026-07 (27 UFs). A APAC específica foi criada na reorganização da assistência à doença renal crônica de 2014, simultaneamente à APAC de Tratamento Dialítico (`sia-atd`, também a partir de 2014-08), que sucedeu a antiga APAC de Nefrologia (`sia-an`, até 2014-10). Só existem 57 colunas e o volume é pequeno (~32 MB).

Aplicações: acesso vascular definitivo vs. cateter na terapia renal substitutiva; taxa de FAV por UF/serviço; complicações pós-operatórias (hematoma, flebite); tempo entre início da diálise e confecção da fístula (cruzando com `sia-atd`); gasto com acesso vascular e qualidade do cuidado nefrológico.

### Cobertura observada

- Índice do FTP (2026-10): 3795 arquivos, de 2014-08 a 2026-08, 27 UF(s) com arquivos, última atualização em 2026-10-30.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2014-10 a 2026-06), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

57 colunas no arquivo de 2024-01 (`ACFAC2401.dbc`).

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
| `ACF_DUPLEX` | String (`S`/`N`) | Realização de duplex (ultrassom Doppler) de mapeamento vascular. |
| `ACF_USOCAT` | String (`S`/`N`) | Uso prévio de cateter para diálise. |
| `ACF_PREFAV` | String (`S`/`N`) | Existência de fístula arteriovenosa prévia. |
| `ACF_FLEBIT / ACF_HEMATO` | String (`S`/`N`) | Ocorrência de flebite e de hematoma. |
| `ACF_VEIAVI / ACF_VEIDIA / ACF_ARTDIA` | String | Veia utilizada e diâmetros (mm, em faixas) de veia e artéria (ver Informe Técnico). |
| `ACF_PULSO / ACF_FREMIT` | String | Pulso e frêmito da fístula após a cirurgia. |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

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
| `acf_duplex` | `ACF_DUPLEX` | texto | Duplex prévio (S - Sim, N - Não) | — | todos |
| `acf_usocat` | `ACF_USOCAT` | texto | Uso do cateter venoso ou outros acessos venosos prévios (S - Sim, N - Não) | — | todos |
| `acf_prefav` | `ACF_PREFAV` | texto | FAV prévia (S - Sim, N - Não) | — | todos |
| `acf_flebit` | `ACF_FLEBIT` | texto | Flebites (S - Sim, N - Não) | — | todos |
| `acf_hemato` | `ACF_HEMATO` | texto | Hematomas (S - Sim, N - Não) | — | todos |
| `acf_veiavi` | `ACF_VEIAVI` | texto | Veia visível (S - Sim, N - Não) | — | todos |
| `acf_pulso` | `ACF_PULSO` | texto | Presença de pulso (S - Sim, N - Não) | — | todos |
| `acf_veidia` | `ACF_VEIDIA` | texto | Diâmetro da veia (em mm) | — | todos |
| `acf_artdia` | `ACF_ARTDIA` | texto | Diâmetro da artéria (em mm) | — | todos |
| `acf_fremit` | `ACF_FREMIT` | texto | Frêmito - Vibração perceptível pelo tato | — | todos |
| `ap_natjur` | `AP_NATJUR` | texto | Código da Natureza Jurídica | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sia-acf`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): decimal(20,2): 1, texto: 57.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sia-acf.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) as descrições dos campos `ACF_*` foram interpretadas a partir dos nomes e do Informe Técnico do SIASUS; valide os domínios (`S`/`N` ou faixas numéricas) antes de usar como indicadores; (ii) a coluna `AP_TIPPRE` aparece com grafia diferente de `AP_TPPRE` em alguns leiautes — normalize nomes ao empilhar anos; (iii) os campos `AP_DTOCOR`/`AP_APACANT` seguem o mesmo padrão de APAC; (iv) como o dataset é pequeno, a leitura de todo o histórico para uma UF é viável em memória. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sia-acf").glob("**/*.parquet"))
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
datasus-fetcher list sia-acf

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sia-acf -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sia-acf
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIASUS (jul/2019)**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIASUS/200801_/Doc/Informe_Tecnico_SIASUS_2019_07.pdf`
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **Manual Técnico Operacional do SIA/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz** (Plataforma de Ciência de Dados aplicada à Saúde), que disponibiliza o SIA/SUS para pesquisa: https://pcdas.icict.fiocruz.br/
