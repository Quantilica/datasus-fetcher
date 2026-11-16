---
dataset:
  id: cih-cr
  fonte: datasus
  titulo: Comunicação de Internação Hospitalar
  resumo: cih-cr contém a Comunicação de Internação Hospitalar (CIH)
  orgao: Ministério da Saúde — DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/CIH/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2008-01
    fim: 2011-04
  unidade: uma internação comunicada (CIH) por um estabelecimento, em uma competência
  granularidade:
    espacial: estabelecimento e município de residência do paciente; um arquivo por UF
    temporal: dia da internação e da saída; competência (mês)
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e competência mensal
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 29
  unidades_de_medida:
    dias_perm: dias
  dados_pessoais:
  - coluna: nasc
    categoria: data de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Comunicação de Internação Hospitalar (`cih-cr`)

## Resumo

`cih-cr` contém a **Comunicação de Internação Hospitalar (CIH)**: cada linha é uma internação ocorrida em estabelecimento de saúde que **não é remunerada por AIH do SUS** (por exemplo, hospitais próprios ou filantrópicos que informam a produção ao gestor), registrada para dar visibilidade à totalidade das internações do território. Cobre apenas o período 2008–2011 no FTP.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (dBASE comprimido com PKWARE DCL/blast, descompactado nativamente pelo `datasus-fetcher`)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf / yearmonth`
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2008-01 a 2011-04 (conforme `index.json`; 24 UFs com arquivos; última atualização no FTP em 2017-07-06)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 868 arquivos (~165,1 MB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Não
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): Não aplicável
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/CIH/200801_201012/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CIH/200801_201012/Dados` | `CR` | UF (2 letras minúsculas/maiúsculas, inclui `br`) + AA (ano, 2 dígitos) + MM (mês, `01`–`12`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `CRSP0801.dbc` — `CR` (Comunicação de Internação Hospitalar) + `SP` (UF) + `08` (ano 2008) + `01` (mês de competência). Exemplo real de menor porte: `CRAC0801.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cih-cr/<AAAAMM>/cih-cr_<uf>_<AAAAMM>_<AAAAMMDD>.dbc`, por exemplo `data/cih-cr/200801/cih-cr_sp_200801_20261018.dbc` (o sufixo `AAAAMMDD` é a data do download).
- **Documentação e Tabelas Auxiliares associadas**: o grupo `cih` **não possui diretório de documentação** em `meta.docs` (sem Informe Técnico próprio no FTP); o leiaute é semelhante ao do SIH/RD (consulte `IT_SIHSUS_1603.pdf` em `SIHSUS/200801_/Doc`). Em `Auxiliar/` há `TAB_CIH.zip` (~15,3 MB, tabelas e conversores `.cnv`/`.def` de procedimento, CID e municípios).

## Conteúdo

O Sistema de Comunicação de Informação Hospitalar (CIH) foi criado pelo Ministério da Saúde/DATASUS para complementar o SIH/SUS, captando internações que não geram pagamento via AIH — por exemplo, as realizadas em hospitais sob outra forma de financiamento ou convênio — e que, sem a CIH, ficariam invisíveis nas estatísticas hospitalares. É gerido pela SAES/MS com processamento do DATASUS.

O evento gerador é a **internação hospitalar comunicada** pelo estabelecimento ao gestor por meio do leiaute CIH, com variáveis análogas às da AIH (paciente, município de residência, procedimento, diagnóstico principal e secundário, datas, tempo de permanência, óbito). A unidade de análise é a **internação comunicada por competência**. Não há valores financeiros (`VAL_*`) nem número de AIH, pois a CIH não é um instrumento de faturamento.

O inventário do FTP cobre apenas 2008-01 a 2011-04 (24 UFs com arquivos, ~165 MB, última atualização em 2017). O sistema foi sucedido pelo CIHA (`ciha`, a partir de 2011-01), que amplia a comunicação para o atendimento ambulatorial; por isso a CIH é um dataset **descontinuado**, com leiaute reduzido de 28 colunas e sem campos de valor. Os dados de CIH foram usados para melhorar a completude de internações hospitalares nos municípios que não registravam AIH.

Aplicações: completar o panorama de internações em municípios com hospitais fora do faturamento por AIH; análise de causas de internação (CID-10 do `DIAG_PRINC`), permanência e mortalidade hospitalar da rede não-SUS comunicante; estudos de oferta e fluxo de pacientes (`MUNIC_RES` vs. `MUNIC_MOV`); e como ponte histórica para a série do `ciha` (2011 em diante).

### Cobertura observada

- Índice do FTP (2026-10): 868 arquivos, de 2008-01 a 2011-04, 24 UF(s) com arquivos, última atualização em 2017-07-06.
- Conversão local de amostras (4 arquivo(s) Parquet, de 2008-02 a 2011-04), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

28 colunas no arquivo de 2008-01 (`CRAC0801.dbc`); a CIH não traz campos de valor financeiro nem número de AIH.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `ANO_CMPT / MES_CMPT` | String (4 / 2) | Ano e mês da competência da comunicação. |
| `ESPEC` | String | Especialidade do leito. |
| `CGC_HOSP` | String (14) | CNPJ do hospital comunicante. |
| `CNES` | String (7) | Código CNES do estabelecimento. |
| `MUNIC_RES / MUNIC_MOV` | String (6) | Município de residência do paciente e do estabelecimento (IBGE 6 dígitos). |
| `NASC / IDADE / COD_IDADE` | String AAAAMMDD / Int / String | Data de nascimento, idade e unidade (`2` dias, `3` meses, `4` anos). |
| `SEXO` | Inteiro | Sexo (`1` masculino, `3` feminino, `0`/`9` ignorado). |
| `PROC_REA` | String (10) | Procedimento realizado na internação (SIGTAP). |
| `DT_INTER / DT_SAIDA` | String AAAAMMDD → `pl.Date` | Datas de internação e saída. |
| `DIAG_PRINC / DIAG_SECUN` | String (CID-10) | Diagnósticos principal e secundário. |
| `DIAS_PERM` | Inteiro | Dias de permanência. |
| `UTI_MES_TO / UTI_INT_TO` | Inteiro | Dias de UTI no mês e na internação. |
| `COBRANCA / NATUREZA / GESTAO` | String | Motivo de saída/cobrança, natureza do hospital e tipo de gestão. |
| `MORTE` | Inteiro | Indicador de óbito. |
| `CAR_INT / FONTE / HOMONIMO / NACIONAL` | String | Caráter da internação, fonte da informação, indicador de homônimo e nacionalidade. |

## Variáveis

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
| `dt_inter` | `DT_INTER` | data | Data de internação (AAAAMMDD, convertida para data) | — | todos |
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
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/cih-cr`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 2, inteiro: 1, texto: 26.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `cih-cr.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- (i) é uma série **encerrada** e pequena; (ii) não substitui o SIH — não há identificador de AIH, portanto não é possível deduplicar contra o `sih-rd` pelo número; (iii) `CGC_HOSP` e `CNES` identificam o hospital, mas a cobertura varia por UF (24 UFs com arquivo); (iv) a CIH foi sucedida pelo `ciha` a partir de 2011-01 — há sobreposição em 2011-01 a 2011-04, cuja deduplicação deve ser feita por hospital+competência. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/cih-cr/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "mes", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "mes", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cih-cr
quantilica datasus list cih-cr

# 2. Baixar microdados de cih-cr com recorte adequado à partição (uf + yearmonth)
quantilica datasus sync cih-cr -o ./data --start 2008-01 --end 2011-04 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cih-cr -o ./data --start 2008-01 --end 2011-04 --regions sp rj --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline cih-cr -o ./data/raw --parquet-dir ./data/parquet --start 2008-01 --end 2011-04 --regions sp rj
```

> O grupo `cih` não possui diretório de documentação mapeado em `meta.docs`; por isso a flag `--docs` foi omitida acima.

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from pathlib import Path

arquivo = next(Path("./data/cih-cr/200801").glob("cih-cr_sp_200801_*.dbc"))
cr = df.read_dbc(arquivo, dataset="cih-cr")

# Internações comunicadas por diagnóstico principal e permanência média
q = (
    cr.with_columns(pl.col("diag_princ").str.slice(0, 3).alias("cid3"))
    .group_by("cid3")
    .agg(
        pl.len().alias("internacoes"),
        pl.col("dias_perm").mean().alias("permanencia_media"),
    )
    .sort("internacoes", descending=True)
)
print(q.head(10))
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CIH/200801_201012/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Informe Técnico SIHSUS** (leiaute de referência): `ftp://ftp.datasus.gov.br/dissemin/publicos/SIHSUS/200801_/Doc/IT_SIHSUS_1603.pdf`
- **Tabelas auxiliares CIH**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CIH/200801_201012/Auxiliar/TAB_CIH.zip`
- **Biblioteca Virtual em Saúde do Ministério da Saúde** (normas e manuais do SIH/SIA/CIHA): https://bvsms.saude.gov.br/
- **PCDaS/Fiocruz**: https://pcdas.icict.fiocruz.br/
