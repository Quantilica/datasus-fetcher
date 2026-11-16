---
dataset:
  id: sih-rj
  fonte: datasus
  titulo: RJ - AIH Rejeitadas
  resumo: 'RJ - AIH Rejeitadas do DATASUS: uma AIH rejeitada no processamento, em uma competência.'
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2008-01
    fim: em-curso
  unidade: uma AIH rejeitada no processamento, em uma competência
  granularidade:
    espacial: estabelecimento (CNES) e município de residência do paciente; um arquivo por UF
    temporal: dia da internação e da saída; competência de processamento (mês)
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e competência mensal
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 93
  unidades_de_medida:
    uti_mes_in: dias
    uti_mes_an: dias
    uti_mes_al: dias
    uti_mes_to: dias
    uti_int_in: dias
    uti_int_an: dias
    uti_int_al: dias
    uti_int_to: dias
    diar_acom: dias
    qt_diarias: dias
    val_sh: R$ (reais)
    val_sp: R$ (reais)
    val_sadt: R$ (reais)
    val_rn: R$ (reais)
    val_acomp: R$ (reais)
    val_ortp: R$ (reais)
    val_sangue: R$ (reais)
    val_sadtsr: R$ (reais)
    val_transp: R$ (reais)
    val_obsang: R$ (reais)
    val_ped1ac: R$ (reais)
    val_tot: R$ (reais)
    val_uti: R$ (reais)
    us_tot: US$ (dólares)
    rubrica: 'número inteiro: contagem ou código numérico (ver Descrição)'
    idade: 'número inteiro: contagem ou código numérico (ver Descrição)'
    dias_perm: dias
    tot_pt_sp: 'número inteiro: contagem ou código numérico (ver Descrição)'
    num_filhos: 'número inteiro: contagem ou código numérico (ver Descrição)'
    sequencia: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: cep
    categoria: CEP
  - coluna: nasc
    categoria: data de nascimento
  - coluna: cpf_aut
    categoria: CPF
  - coluna: gestor_cpf
    categoria: CPF
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# RJ - AIH Rejeitadas (`sih-rj`)

## Resumo

`sih-rj` contém as **AIH Rejeitadas** no processamento do SIH/SUS: cada linha é uma Autorização de Internação Hospitalar apresentada pelo hospital que **não foi aprovada** para pagamento na competência, com o mesmo leiaute do arquivo RD acrescido de campos de situação e bloqueio. Permite auditar glosas, qualidade do faturamento e o volume de internações não pagas.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/SIHSUS/200801_/Doc`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SIHSUS/200801_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SIHSUS/200801_/Dados` | `RJ` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `RJSP2401.dbc` — `RJ` (AIH Rejeitada) + `SP` (UF) + `24` (ano 2024) + `01` (mês de competência). Disponível apenas no diretório `200801_`.
- **No armazenamento local do `datasus-fetcher`**: `data/sih-rj/<AAAAMM>/sih-rj_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sih-rj/202401/sih-rj_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/IT_SIHSUS_1603.pdf` (Informe Técnico do SIHSUS, 57 KB, 2016) é o dicionário oficial de variáveis; `Auxiliar/TAB_SIH.zip` (~6,1 MB, tabelas e conversores `.cnv`/`.def` atuais) e as versões históricas `TAB_SIH_199201-199712.zip`, `TAB_SIH_199801-200307.zip` e `TAB_SIH_200308-200712.zip` trazem as tabelas de procedimentos, CID e códigos usadas em cada fase.

## Conteúdo

O Sistema de Informações Hospitalares do SUS (SIH/SUS) é gerido pelo Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES), com processamento e disseminação a cargo do DATASUS — e tem como finalidade operacionalizar o pagamento das internações realizadas em hospitais públicos e privados conveniados ao SUS. Por ser um sistema de faturamento, cobre apenas a assistência financiada pelo SUS (não inclui saúde suplementar nem internações particulares) e é a principal fonte nacional para estudar morbidade hospitalar, perfil assistencial e gasto hospitalar.

O evento gerador é a **apresentação de uma AIH que falha nas críticas do processamento** (inconsistência cadastral, procedimento incompatível com CID/sexo/idade, teto financeiro, duplicidade, entre outras). A unidade de análise é a **AIH rejeitada por competência**. Cada hospital preenche a Autorização de Internação Hospitalar (AIH) e a remete mensalmente ao gestor municipal/estadual, que a valida e a envia ao DATASUS para processamento na competência (`ANO_CMPT`/`MES_CMPT`). O processamento classifica cada AIH como aprovada (arquivo RD), rejeitada (RJ/ER) e detalha os atos profissionais (SP). O motivo detalhado da rejeição não está no RJ: ele é registrado, por AIH, no arquivo `sih-er` (campo `CO_ERRO`), que pode ser ligado ao RJ por `N_AIH`/`AIH`, `CNES` e competência.

O RJ existe no FTP somente a partir de 2008-01, na estrutura do SIH com Tabela Unificada (SIGTAP); não há RJ para o período 1992–2007. As colunas de valores e diagnóstico seguem o RD, porém sem os diagnósticos secundários adicionais (`DIAGSEC1–9`) e sem os campos de repasse (`VAL_SH_FED`…), e com três campos extras de situação (`ST_SITUAC`, `ST_BLOQ`, `ST_MOT_BLO`). Uma AIH rejeitada pode ser corrigida e reapresentada, voltando como aprovada (RD) em competência posterior.

Aplicações: taxa de rejeição/glosa por hospital, município e gestor (RJ ÷ (RD + RJ)); valor financeiro retido (`VAL_TOT` das AIH rejeitadas); identificação de hospitais com maior inconsistência de faturamento; análise de causas de rejeição quando combinado com `sih-er`; auditoria e controle e avaliação de contratos; e estimativa de subnotificação de internações quando se compara a produção apresentada com a aprovada.

### Cobertura observada

- Índice do FTP (2026-10): 5913 arquivos, de 2008-01 a 2026-09, 27 UF(s) com arquivos, última atualização em 2026-11-10.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2008-04 a 2026-03), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

91 colunas no arquivo de 2024-01 (`RJAC2401.dbc`); o leiaute coincide com o do RD, exceto pelas colunas de situação/bloqueio.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `UF_ZI` | String (6) | Código do gestor/UF de gestão do estabelecimento. |
| `ANO_CMPT / MES_CMPT` | String | Competência de processamento em que a AIH foi rejeitada. |
| `N_AIH` | String (13) | Número da AIH rejeitada (chave de ligação com `sih-er`). |
| `CNES` | String (7) | Estabelecimento que apresentou a AIH. |
| `MUNIC_RES / MUNIC_MOV` | String (6) | Município de residência do paciente e do estabelecimento. |
| `NASC / IDADE / COD_IDADE / SEXO` | String / Int / String / Int | Dados demográficos do paciente informados na AIH. |
| `DT_INTER / DT_SAIDA` | `pl.Date` | Datas de internação e saída informadas. |
| `PROC_SOLIC / PROC_REA` | String (10) | Procedimento SIGTAP solicitado e realizado. |
| `DIAG_PRINC / DIAG_SECUN` | String (CID-10) | Diagnósticos informados. |
| `VAL_SH / VAL_SP / VAL_TOT` | Float | Valores calculados da AIH que **não foram pagos** (R$). |
| `COBRANCA` | String | Motivo de saída/cobrança informado na AIH. |
| `ST_SITUAC` | String | Situação da AIH no processamento (códigos do Informe Técnico do SIHSUS). |
| `ST_BLOQ / ST_MOT_BLO` | String | Indicador e motivo de bloqueio da AIH. |
| `SEQUENCIA / REMESSA` | Inteiro / String | Sequência do registro e nome da remessa (`HE<gestor>…<AAAAMM>.DTS`) enviada pelo gestor; útil para rastrear o lote de origem. |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `uf_zi` | `UF_ZI` | texto | Município Gestor. | — | todos |
| `ano_cmpt` | `ANO_CMPT` | texto | Ano de processamento da AIH, no formato aaaa. | — | todos |
| `mes_cmpt` | `MES_CMPT` | texto | Mês de processamento da AIH, no formato mm. | — | todos |
| `espec` | `ESPEC` | texto | Especialidade do Leito | — | todos |
| `cgc_hosp` | `CGC_HOSP` | texto | CNPJ do Estabelecimento. | — | todos |
| `n_aih` | `N_AIH` | texto | Número da AIH. | — | todos |
| `ident` | `IDENT` | texto | Identificação do tipo da AIH. | — | todos |
| `cep` | `CEP` | texto | CEP do paciente. | — | todos |
| `munic_res` | `MUNIC_RES` | texto | Município de Residência do Paciente | — | todos |
| `nasc` | `NASC` | texto | Data de nascimento do paciente (aaaammdd). | — | todos |
| `sexo` | `SEXO` | texto | Sexo do paciente. | — | todos |
| `uti_mes_in` | `UTI_MES_IN` | inteiro | Zerado | — | todos |
| `uti_mes_an` | `UTI_MES_AN` | inteiro | Zerado | — | todos |
| `uti_mes_al` | `UTI_MES_AL` | inteiro | Zerado | — | todos |
| `uti_mes_to` | `UTI_MES_TO` | inteiro | Quantidade de dias de UTI no mês. | — | todos |
| `marca_uti` | `MARCA_UTI` | texto | Indica qual o tipo de UTI utilizada pelo paciente. | — | todos |
| `uti_int_in` | `UTI_INT_IN` | inteiro | Zerado | — | todos |
| `uti_int_an` | `UTI_INT_AN` | inteiro | Zerado | — | todos |
| `uti_int_al` | `UTI_INT_AL` | inteiro | Zerado | — | todos |
| `uti_int_to` | `UTI_INT_TO` | inteiro | Quantidade de diárias em unidade intermediaria. | — | todos |
| `diar_acom` | `DIAR_ACOM` | inteiro | Quantidade de diárias de acompanhante. | — | todos |
| `qt_diarias` | `QT_DIARIAS` | inteiro | Quantidade de diárias. | — | todos |
| `proc_solic` | `PROC_SOLIC` | texto | Procedimento solicitado. | — | todos |
| `proc_rea` | `PROC_REA` | texto | Procedimento realizado. | — | todos |
| `val_sh` | `VAL_SH` | decimal(13,2) | Valor de serviços hospitalares. | — | todos |
| `val_sp` | `VAL_SP` | decimal(13,2) | Valor de serviços profissionais. | — | todos |
| `val_sadt` | `VAL_SADT` | decimal(13,2) | Zerado | — | todos |
| `val_rn` | `VAL_RN` | decimal(13,2) | Zerado | — | todos |
| `val_acomp` | `VAL_ACOMP` | decimal(13,2) | Zerado | — | todos |
| `val_ortp` | `VAL_ORTP` | decimal(13,2) | Zerado | — | todos |
| `val_sangue` | `VAL_SANGUE` | decimal(13,2) | Zerado | — | todos |
| `val_sadtsr` | `VAL_SADTSR` | decimal(11,2) | Zerado | — | todos |
| `val_transp` | `VAL_TRANSP` | decimal(13,2) | Zerado | — | todos |
| `val_obsang` | `VAL_OBSANG` | decimal(11,2) | Zerado | — | todos |
| `val_ped1ac` | `VAL_PED1AC` | decimal(11,2) | Zerado | — | todos |
| `val_tot` | `VAL_TOT` | decimal(14,2) | Valor total da AIH. | — | todos |
| `val_uti` | `VAL_UTI` | decimal(8,2) | Valor de UTI. | — | todos |
| `us_tot` | `US_TOT` | decimal(10,2) | Valor total, em dólar. | — | todos |
| `dt_inter` | `DT_INTER` | data | Data de internação (AAAAMMDD, convertida para data); o informe técnico a grafa `DI_INTER` | — | todos |
| `dt_saida` | `DT_SAIDA` | data | Data de saída, no formato aaaammdd. | — | todos |
| `diag_princ` | `DIAG_PRINC` | texto | Código do diagnóstico principal (CID10). | — | todos |
| `diag_secun` | `DIAG_SECUN` | texto | Código do diagnostico secundário (CID10). Preenchido com zeros a partir de 201501. | — | todos |
| `cobranca` | `COBRANCA` | texto | Motivo de Saída/Permanência | — | todos |
| `natureza` | `NATUREZA` | texto | Natureza jurídica do hospital (com conteúdo até maio/12). Era utilizada a classificação de Regime e Natureza. | — | todos |
| `gestao` | `GESTAO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `rubrica` | `RUBRICA` | inteiro | Zerado | — | todos |
| `ind_vdrl` | `IND_VDRL` | texto | Indica exame VDRL. | — | todos |
| `munic_mov` | `MUNIC_MOV` | texto | Município do Estabelecimento. | — | todos |
| `cod_idade` | `COD_IDADE` | texto | Unidade de medida da idade. | — | todos |
| `idade` | `IDADE` | inteiro | Idade. | — | todos |
| `dias_perm` | `DIAS_PERM` | inteiro | Dias de Permanência. | — | todos |
| `morte` | `MORTE` | texto | Indica Óbito | — | todos |
| `nacional` | `NACIONAL` | texto | Código da nacionalidade do paciente. | — | todos |
| `num_proc` | `NUM_PROC` | texto | Zerado | — | todos |
| `car_int` | `CAR_INT` | texto | Caráter da internação. | — | todos |
| `tot_pt_sp` | `TOT_PT_SP` | inteiro | Zerado | — | todos |
| `cpf_aut` | `CPF_AUT` | texto | Zerado | — | todos |
| `homonimo` | `HOMONIMO` | texto | Indicador se o paciente da AIH é homônimo do paciente de outra AIH. | — | todos |
| `num_filhos` | `NUM_FILHOS` | inteiro | Número de filhos do paciente. | — | todos |
| `instru` | `INSTRU` | texto | Grau de instrução do paciente. | — | todos |
| `cid_notif` | `CID_NOTIF` | texto | CID de Notificação. | — | todos |
| `contracep1` | `CONTRACEP1` | texto | Tipo de contraceptivo utilizado. | — | todos |
| `contracep2` | `CONTRACEP2` | texto | Segundo tipo de contraceptivo utilizado. | — | todos |
| `gestrisco` | `GESTRISCO` | texto | Indicador se é gestante de risco. | — | todos |
| `insc_pn` | `INSC_PN` | texto | Número da gestante no pré-natal. | — | todos |
| `seq_aih5` | `SEQ_AIH5` | texto | Sequencial de longa permanência (AIH tipo 5). | — | todos |
| `cbor` | `CBOR` | texto | Ocupação do paciente, segundo a Classificação Brasileira de Ocupações – CBO. | — | todos |
| `cnaer` | `CNAER` | texto | Código de acidente de trabalho. | — | todos |
| `vincprev` | `VINCPREV` | texto | Vínculo com a Previdência. | — | todos |
| `gestor_cod` | `GESTOR_COD` | texto | Motivo de autorização da AIH pelo Gestor. | — | todos |
| `gestor_tp` | `GESTOR_TP` | texto | Tipo de gestor. | — | todos |
| `gestor_cpf` | `GESTOR_CPF` | texto | Número do CPF do Gestor. | — | todos |
| `gestor_dt` | `GESTOR_DT` | texto | Data da autorização dada pelo Gestor (aaaammdd). | — | todos |
| `cnes` | `CNES` | texto | Código CNES do hospital. | — | todos |
| `cnpj_mant` | `CNPJ_MANT` | texto | CNPJ da mantenedora. | — | todos |
| `infehosp` | `INFEHOSP` | texto | Status de infecção hospitalar. | — | todos |
| `cid_asso` | `CID_ASSO` | texto | CID causa. | — | todos |
| `cid_morte` | `CID_MORTE` | texto | CID da morte. | — | todos |
| `complex` | `COMPLEX` | texto | Complexidade. | — | todos |
| `financ` | `FINANC` | texto | Tipo de financiamento. | — | todos |
| `faec_tp` | `FAEC_TP` | texto | Subtipo de financiamento FAEC. | — | todos |
| `regct` | `REGCT` | texto | Regra contratual. | — | todos |
| `raca_cor` | `RACA_COR` | texto | Raça/Cor do paciente. | — | todos |
| `etnia` | `ETNIA` | texto | Etnia do paciente, se raça cor for indígena. | — | todos |
| `st_situac` | `ST_SITUAC` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `st_bloq` | `ST_BLOQ` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `st_mot_blo` | `ST_MOT_BLO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `sequencia` | `SEQUENCIA` | inteiro | Sequencial da AIH na remessa. | — | todos |
| `remessa` | `REMESSA` | texto | Número da remessa. | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `nat_jur` | `NAT_JUR` | texto | Natureza jurídica do Estabelecimento, conforme a Comissão Nacional de Classificação - CONCLA | — | 2014-06 a 2026-03 |
| `fonte_orc` | `FONTE_ORC` | texto | Fonte orçamentária do pagamento (campo presente só nas partições mais recentes) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | só em 2026-03 |

## No lake

- **Dataset no lake:** `datasus/sih-rj`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 2, decimal(10,2): 1, decimal(11,2): 3, decimal(13,2): 8, decimal(14,2): 1, decimal(8,2): 1, inteiro: 16, texto: 61.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sih-rj.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) o RJ **não** contém o motivo da rejeição — junte com `sih-er` pelo número da AIH, CNES e competência; (ii) a mesma AIH pode ser rejeitada em mais de uma competência e depois aprovada, então deduplique antes de calcular taxas; (iii) os valores representam o que o hospital apresentou e **não foi pago**, não despesa do SUS; (iv) `ST_SITUAC`/`ST_BLOQ`/`ST_MOT_BLO` seguem tabelas de domínio do SIHSUS presentes em `TAB_SIH.zip`. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 2 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sih-rj").glob("**/*.parquet"))
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
datasus-fetcher list sih-rj

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sih-rj -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sih-rj
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIHSUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/IT_SIHSUS_1603.pdf`
- **Manual Técnico Operacional do SIH/SUS (SAES/MS)** — disponíveis na Biblioteca Virtual em Saúde do Ministério da Saúde: https://bvsms.saude.gov.br/
- **SIGTAP — Tabela de Procedimentos, Medicamentos e OPM do SUS**: http://sigtap.datasus.gov.br/
- **PCDaS/Fiocruz** (SIH/SUS para pesquisa): https://pcdas.icict.fiocruz.br/
