---
dataset:
  id: ciha
  fonte: datasus
  titulo: Sistema de Comunicação de Informação Hospitalar e Ambulatorial
  resumo: 'Sistema de Comunicação de Informação Hospitalar e Ambulatorial do DATASUS: um atendimento (internação ou ambulatorial) comunicado por um estabelecimento, em uma competência.'
  orgao: Ministério da Saúde — DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/CIHA/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2011-01
    fim: em-curso
  unidade: um atendimento (internação ou ambulatorial) comunicado por um estabelecimento, em uma competência
  granularidade:
    espacial: estabelecimento e município de residência do paciente; um arquivo por UF
    temporal: dia do atendimento e da saída; competência (mês)
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e competência mensal
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 32
  unidades_de_medida:
    dias_perm: dias
  dados_pessoais:
  - coluna: nasc
    categoria: data de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Sistema de Comunicação de Informação Hospitalar e Ambulatorial (`ciha`)

## Resumo

`ciha` é o **Sistema de Comunicação de Informação Hospitalar e Ambulatorial (CIHA)**: cada linha é um atendimento (internação ou ambulatorial) realizado em estabelecimento que não fatura pelo SIH/SIA do SUS, comunicado mensalmente ao DATASUS para que o gestor conheça a totalidade da produção do território. É o sucessor do CIH (2008–2011) e cobre de 2011-01 em diante.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** `/dissemin/publicos/CIHA/201101_/Doc`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/CIHA/201101_/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CIHA/201101_/Dados` | `CIHA` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `CIHASP2401.dbc` — `CIHA` (prefixo do sistema, 4 letras) + `SP` (UF) + `24` (ano 2024) + `01` (mês de competência).
- **No armazenamento local do `datasus-fetcher`**: `data/ciha/<AAAAMM>/ciha_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/ciha/202401/ciha_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: `Doc/Layout_Arquivos_CIHA.pdf` (leiaute oficial, 10 KB, 2014) descreve os campos; `Auxiliar/TAB_CIHA.zip` (~68,8 MB, tabelas de procedimento, CID, município e conversores `.cnv`).

## Conteúdo

O CIHA é mantido pelo Ministério da Saúde/DATASUS (SAES) como **complemento ao SIH e ao SIA** para estabelecimentos que realizam atendimentos mas não são remunerados por esses sistemas (hospitais e ambulatórios privados, filantrópicos com outras formas de contratação, serviços próprios de entes federados, de universidades e de forças armadas, entre outros). Sua finalidade é dar visibilidade, para planejamento e regulação, à oferta assistencial que fica fora do faturamento do SUS.

O evento gerador é o **atendimento comunicado** (internação ou procedimento ambulatorial) pelo estabelecimento ao gestor, no leiaute do CIHA. A unidade de análise é o **atendimento comunicado por competência**: para internações há `DT_SAIDA`, `DIAS_PERM` e `MORTE`; para o ambulatório há `QT_PROC` (quantidade do procedimento). O campo `MODALIDADE` distingue a modalidade de atendimento, `FONTE` indica a fonte do dado e `CGC_CONSOR` identifica consórcio intermunicipal quando aplicável.

O inventário do FTP cobre 2011-01 a 2026-07 (26 UFs, ~5,7 GB, 4.802 arquivos). O CIHA nasceu como evolução do CIH (`cih-cr`), incorporando o atendimento ambulatorial. O leiaute tem 31 colunas, parecido com o do SIH/RD mas sem campos de valor financeiro e com `DT_ATEND` (data do atendimento) no lugar de `DT_INTER`. A tabela de procedimentos acompanha a SIGTAP (`PROC_REA`, 10 dígitos) e o CID é o CID-10.

Aplicações: ampliar a cobertura das estatísticas de morbidade hospitalar e de produção ambulatorial com os estabelecimentos não-SUS; estimar a oferta total de serviços e a ocupação da rede privada; análise de fluxos de pacientes (`MUNIC_RES` vs. `MUNIC_MOV`); perfil de diagnósticos (`DIAG_PRINC`) e permanência; e subsídio à regulação e ao planejamento regional, em conjunto com o CNES.

### Cobertura observada

- Índice do FTP (2026-10): 4843 arquivos, de 2011-01 a 2026-09, 26 UF(s) com arquivos, última atualização em 2026-11-13.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2011-10 a 2026-08), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

31 colunas no arquivo de 2024-01 (`CIHAAC2401.dbc`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `ANO_CMPT / MES_CMPT` | String (4 / 2) | Ano e mês da competência da comunicação. |
| `ESPEC` | String | Especialidade do leito/atendimento. |
| `CGC_HOSP` | String (14) | CNPJ do estabelecimento comunicante. |
| `CNES` | String (7) | Código CNES do estabelecimento. |
| `MUNIC_RES / MUNIC_MOV` | String (6) | Município de residência do paciente e do estabelecimento. |
| `NASC / IDADE / COD_IDADE` | String AAAAMMDD / Int / String | Data de nascimento, idade e unidade da idade. |
| `SEXO` | Inteiro | Sexo (`1` masculino, `3` feminino, `0`/`9` ignorado). |
| `PROC_REA / QT_PROC` | String (10) / Inteiro | Procedimento realizado (SIGTAP) e quantidade. |
| `DT_ATEND / DT_SAIDA` | String AAAAMMDD → `pl.Date` | Datas do atendimento/internação e da saída. |
| `DIAG_PRINC / DIAG_SECUN` | String (CID-10) | Diagnósticos principal e secundário. |
| `DIAS_PERM` | Inteiro | Dias de permanência (internações). |
| `UTI_MES_TO / UTI_INT_TO` | Inteiro | Dias de UTI no mês e na internação. |
| `MORTE` | Inteiro | Indicador de óbito. |
| `CAR_INT / COBRANCA / NATUREZA / GESTAO` | String | Caráter do atendimento, motivo de saída/cobrança, natureza e gestão do estabelecimento. |
| `FONTE / CGC_CONSOR / MODALIDADE / HOMONIMO` | String | Fonte da informação, CNPJ do consórcio, modalidade do atendimento e indicador de homônimo. |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `ano_cmpt` | `ANO_CMPT` | texto | de Informações do de Informação Hospitalar e (CIHA) de Informação de – CIHA dos arquivos CIHA*.dbf DESCRIÇÃO Ano de competência da CIH, formato AA | — | todos |
| `mes_cmpt` | `MES_CMPT` | texto | Mês de competência da CIH, formato MM | — | todos |
| `espec` | `ESPEC` | texto | (Vazio) | — | todos |
| `cgc_hosp` | `CGC_HOSP` | texto | CNPJ do Estabelecimento de Saúde | — | todos |
| `munic_res` | `MUNIC_RES` | texto | Município de residência | — | todos |
| `nasc` | `NASC` | texto | Data de nascimento do paciente | — | todos |
| `sexo` | `SEXO` | texto | Sexo do paciente | — | todos |
| `uti_mes_to` | `UTI_MES_TO` | texto | (zerado) | — | todos |
| `uti_int_to` | `UTI_INT_TO` | texto | Total de dias de UTI intermediária durante a internação | — | todos |
| `proc_rea` | `PROC_REA` | texto | Procedimento realizado | — | todos |
| `qt_proc` | `QT_PROC` | texto | Quantidade de procedimento | — | todos |
| `dt_atend` | `DT_ATEND` | data | Data do atendimento, formato AAAAMMDD | — | todos |
| `dt_saida` | `DT_SAIDA` | data | Data de saída, formato AAAAMMDD | — | todos |
| `diag_princ` | `DIAG_PRINC` | texto | Diagnóstico principal, segundo a CID-10 | — | todos |
| `diag_secun` | `DIAG_SECUN` | texto | Diagnóstico secundário, segundo a CID-10 | — | todos |
| `cobranca` | `COBRANCA` | texto | Motivo da cobrança | — | todos |
| `natureza` | `NATUREZA` | texto | Natureza da relação do hospital com o SUS | — | todos |
| `gestao` | `GESTAO` | texto | Indica o tipo de gestão do hospital | — | todos |
| `munic_mov` | `MUNIC_MOV` | texto | Código do município onde se localiza o hospital Unidade de medida da idade: | — | todos |
| `cod_idade` | `COD_IDADE` | texto | 0 – ignorada 2 – dias 3 – meses 4 – anos 5 – anos (mais de 100) | — | todos |
| `idade` | `IDADE` | texto | Idade, na unidade do campo COD_IDADE | — | todos |
| `dias_perm` | `DIAS_PERM` | inteiro | Dias de permanência | — | todos |
| `morte` | `MORTE` | texto | Indica se o paciente teve saída com morte: 0– Não 1 – Sim | — | todos |
| `nacional` | `NACIONAL` | texto | (Vazio) | — | todos |
| `car_int` | `CAR_INT` | texto | (Vazio) | — | todos |
| `homonimo` | `HOMONIMO` | texto | (Vazio) | — | todos |
| `cnes` | `CNES` | texto | Código CNES do estabelecimento | — | todos |
| `fonte` | `FONTE` | texto | Fonte da remuneração | — | todos |
| `cgc_consor` | `CGC_CONSOR` | texto | CNPJ do consórcio intermunicipal de saúde, quando aplicável | — | todos |
| `modalidade` | `MODALIDADE` | texto | Modalidade do atendimento de Saúde em Saúde (DIDIS) do link Fale conosco. | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/ciha`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 2, inteiro: 1, texto: 29.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `ciha.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) mistura internação e atendimento ambulatorial — distinga-os por `MODALIDADE` e pela presença de `DIAS_PERM`/`DT_SAIDA`; (ii) não há `N_AIH` nem valores financeiros; (iii) apenas 26 UFs com arquivos; a participação varia entre estados e muda ao longo do tempo (o envio é obrigatório para estabelecimentos fora do SIH/SIA, mas a adesão não é uniforme); (iv) não some `ciha` a `sih-rd` sem verificar se o estabelecimento (`CNES`) já fatura no SIH, para evitar dupla contagem. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/ciha").glob("**/*.parquet"))
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
datasus-fetcher list ciha

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync ciha -o ./data --start 2024-01 --end 2024-12 --regions sp rj --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset ciha
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CIHA/201101_/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Layout oficial do CIHA**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CIHA/201101_/Doc/Layout_Arquivos_CIHA.pdf`
- **Tabelas auxiliares CIHA**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CIHA/201101_/Auxiliar/TAB_CIHA.zip`
- **Biblioteca Virtual em Saúde do Ministério da Saúde** (normas e manuais do SIH/SIA/CIHA): https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz**: https://pcdas.icict.fiocruz.br/
