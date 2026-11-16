---
dataset:
  id: cnes-pf
  fonte: datasus
  titulo: Profissional
  resumo: O cnes-pf contém os microdados do arquivo de Profissionais do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra os vínculos dos profissionais de saúde com os estabelecimentos cadastrados.
  orgao: Ministério da Saúde — Secretaria de Atenção Especializada à Saúde (SAES) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2005-08
    fim: em-curso
  unidade: um vínculo profissional–estabelecimento–ocupação (CBO), em uma competência
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
    colunas: 42
  unidades_de_medida:
    horaoutr: 'número inteiro: contagem ou código numérico (ver Descrição)'
    horahosp: 'número inteiro: contagem ou código numérico (ver Descrição)'
    hora_amb: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: cpf_cnpj
    categoria: CPF ou CNPJ (do estabelecimento ou do prestador; pode ser CPF de pessoa física)
  - coluna: cpf_prof
    categoria: CPF
  - coluna: nomeprof
    categoria: nome do profissional de saúde
  - coluna: cns_prof
    categoria: Cartão Nacional de Saúde (CNS)
  - coluna: cpfunico
    categoria: CPF
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Profissional (`cnes-pf`)

## Resumo

O `cnes-pf` contém os microdados do arquivo de **Profissionais** do Cadastro Nacional de Estabelecimentos de Saúde (CNES), que registra os vínculos dos profissionais de saúde com os estabelecimentos cadastrados. Cada registro (linha) representa um **vínculo profissional–estabelecimento–ocupação (CBO)** em uma competência mensal, descrevendo a ocupação exercida, o vínculo empregatício com o SUS, a carga horária e o conselho de classe. É a maior base do CNES em volume e a principal fonte para dimensionar a força de trabalho em saúde no Brasil.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `yearmonth` (um arquivo por UF e competência mensal, além de `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2005-08 a 2026-09 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 6858 arquivos (~46,7 GB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Não
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/CNES/200508_/doc` (`IT_CNES_1706.pdf`)
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/CNES/200508_/Auxiliar` (`TAB_CNES.zip`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/CNES/200508_/Dados/PF` | `PF` | UF + AA + MM (ex.: `SP2401`) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `PFSP2401.dbc` — `PF` (Profissionais), `SP` (UF), `24` (ano), `01` (mês). Há também `PFBR<AA><MM>.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/cnes-pf/2024-01/cnes-pf_202401-sp@20261015.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: `IT_CNES_1706.pdf` (seção "Layout dos arquivos de Profissionais — PF*.dbf") e o pacote de domínios `TAB_CNES.zip` (que inclui a tabela de CBO e de conselhos).

## Conteúdo

O arquivo `PF` integra o CNES, sistema oficial mantido pelo Ministério da Saúde (Secretaria Executiva/DATASUS) e alimentado continuamente pelos estabelecimentos de saúde por meio do SCNES, sob responsabilidade dos gestores estaduais e municipais (Portarias SAS/MS nº 403/2000 e nº 511/2000; Portaria GM/MS nº 1.646/2015). Ele materializa a dimensão "trabalhadores" do cadastro e é a base para políticas de gestão do trabalho e da educação na saúde, para a vinculação de produção assistencial (SIH/SIA) e para a identificação de profissionais habilitados.

O **evento gerador** é a declaração mensal dos profissionais vinculados ao estabelecimento na FCES/SCNES. A **unidade de análise é o vínculo** identificado pela terna `CNES` + `CPF_PROF` (ou `CNS_PROF`) + `CBO` + `VINCULAC`, em cada competência. Um mesmo profissional pode ter vários vínculos (em um ou vários estabelecimentos), com diferentes ocupações (CBO) e cargas horárias. O arquivo traz o nome (`NOMEPROF`), o CBO, o CNS, o conselho de classe (`CONSELHO`/`REGISTRO`), os indicadores de vínculo com o SUS (`VINCUL_C`, `VINCUL_A`, `VINCUL_N`) e a carga horária decomposta (hospitalar, ambulatorial e outras).

A nomenclatura histórica reflete sucessivas ampliações: a padronização de CNS e CPF, a introdução de `CPF_UNICO`/`CBO_UNICO` (contadores de unicidade) e o campo `UFMUNRES` (município de residência do profissional). Não há diretório preliminar. O volume é muito alto porque inclui todas as ocupações de nível superior, técnico e médio vinculadas a cada estabelecimento, mês a mês.

Aplicações analíticas típicas: número de médicos, enfermeiros, técnicos e demais profissionais por município/UF, razão profissional por habitante, carga horária média, identificação de profissionais SUS vs. não SUS, planejamento de recursos humanos, estudos de fixação/rotatividade e vinculação de registros de produção (por exemplo, CBO do executante em SIA/SIH).

### Cobertura observada

- Índice do FTP (2026-10): 6858 arquivos, de 2005-08 a 2026-09, 27 UF(s) com arquivos, última atualização em 2026-10-15.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2005-08 a 2026-02), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CNES` | String (7) | Número nacional do estabelecimento de saúde |
| `CODUFMUN` | String (6) | Código do município do estabelecimento (UF + MUNIC, sem dígito) |
| `COMPETEN` | String (`AAAAMM`) | Ano e mês de competência da informação |
| `CPF_PROF` | String (11) | CPF do profissional (ou `99999999999` se não informado) |
| `CNS_PROF` | String (15) | Cartão Nacional de Saúde do profissional |
| `NOMEPROF` | String (60) | Nome do profissional |
| `CBO` | String (6) | Código da ocupação/especialidade (CBO) |
| `CONSELHO` | String (2) | Código do conselho de classe |
| `REGISTRO` | String (13) | Número do registro no conselho de classe |
| `VINCULAC` | String (6) | Vínculo empregatício (código composto) |
| `VINCUL_C` / `VINCUL_A` / `VINCUL_N` | String (1) | Vínculo: contratado SUS / autônomo SUS / não identificado |
| `PROF_SUS` / `PROFNSUS` | String (1) | Caracterização do profissional que realiza atendimento SUS / não SUS |
| `HORA_AMB` / `HORAHOSP` / `HORAOUTR` | String (3) | Carga horária ambulatorial / hospitalar / outras |
| `UFMUNRES` | String (8) | UF + município de residência do profissional |
| `NAT_JUR` | String (4) | Natureza jurídica do estabelecimento |

## Variáveis

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
| `cpf_cnpj` | `CPF_CNPJ` | texto | CPF do Estabelecimento, caso pessoa física ou CNPJ, caso pessoa jurídica | — | todos |
| `niv_dep` | `NIV_DEP` | texto | Grau de dependência, onde: 1-Individual 3-Mantida | — | todos |
| `cnpj_man` | `CNPJ_MAN` | texto | CNPJ da mantenedora do estabelecimento | — | todos |
| `esfera_a` | `ESFERA_A` | texto | Código da esfera administrativa | — | todos |
| `atividad` | `ATIVIDAD` | texto | Código da atividade de ensino | — | todos |
| `retencao` | `RETENCAO` | texto | Código de retenção de tributos | — | todos |
| `natureza` | `NATUREZA` | texto | Código da natureza da organização | — | todos |
| `clientel` | `CLIENTEL` | texto | Código de fluxo da clientela | — | todos |
| `tp_unid` | `TP_UNID` | texto | Tipo de unidade (estabelecimento) | — | todos |
| `turno_at` | `TURNO_AT` | texto | Código de turno de atendimento | — | todos |
| `niv_hier` | `NIV_HIER` | texto | Código do nível de hierarquia | — | todos |
| `terceiro` | `TERCEIRO` | texto | O estabelecimento é terceiro: 1-Sim 0-Não 2-não | — | todos |
| `cpf_prof` | `CPF_PROF` | texto | CPF do Profissional ou caso “99999999999” caso não seja preenchido. Contador de CPF ÚNICO do Profissional | — | todos |
| `cbo` | `CBO` | texto | deve ser “1”. Código da especialidade do profissional | — | todos |
| `cbounico` | `CBOUNICO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `nomeprof` | `NOMEPROF` | texto | Nome do profissional | — | todos |
| `cns_prof` | `CNS_PROF` | texto | CNS do profissional ou “999999999999999” caso não seja preenchido. | — | todos |
| `conselho` | `CONSELHO` | texto | Código do conselho de classe | — | todos |
| `registro` | `REGISTRO` | texto | Número do registro no conselho de classe | — | todos |
| `vinculac` | `VINCULAC` | texto | Vínculo empregatício com o estabelecimento: | — | todos |
| `vincul_c` | `VINCUL_C` | texto | Vínculo empregatício com o estabelecimento: Contratado SUS | — | todos |
| `vincul_a` | `VINCUL_A` | texto | Vínculo empregatício com o estabelecimento: Autônomo SUS | — | todos |
| `vincul_n` | `VINCUL_N` | texto | Vínculo empregatício com o estabelecimento: Vínculo não identificado (registros de profissionais não SUS e outras situações anômalas) | — | todos |
| `horaoutr` | `HORAOUTR` | inteiro | Carga horária não ambulatorial, nem hospitalar | — | todos |
| `horahosp` | `HORAHOSP` | inteiro | Carga horária HOSPITALAR | — | todos |
| `hora_amb` | `HORA_AMB` | inteiro | Carga horária AMBULATORIAL | — | todos |
| `competen` | `COMPETEN` | texto | Ano e Mês de competência da informação (AAAAMM) | — | todos |
| `prof_sus` | `PROF_SUS` | texto | Caracterização do PROFISSIONAL que realiza ATENDIMENTO SUS | — | todos |
| `profnsus` | `PROFNSUS` | texto | Caracterização do PROFISSIONAL que realiza ATENDIMENTO NÃO SUS | — | todos |
| `cpfunico` | `CPFUNICO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `ufmunres` | `UFMUNRES` | texto | Código da UF + município de residência do profissional (sem dígito) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `nat_jur` | `NAT_JUR` | texto | Natureza Jurídica de Leitos - Nomenclatura (LT*.dbf) | — | 2016-01 a 2026-02 |

## No lake

- **Dataset no lake:** `datasus/cnes-pf`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): inteiro: 3, texto: 39.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `cnes-pf.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- como um profissional pode ter múltiplos vínculos e CBOs, contagens de "profissionais" exigem deduplicação por `CPF_PROF`/`CNS_PROF`; cargas horárias são texto e podem ultrapassar limites plausíveis (validação recomendada); os campos `CPF_UNICO`/`CBO_UNICO` ajudam a detectar duplicidades; e por ser a maior tabela do CNES (~43,5 GB), o processamento deve ser particionado por UF/competência e convertido a Parquet para análises. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Colunas que não existem em todo o período:** 1 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/cnes-pf/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "mes", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "mes", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para cnes-pf
quantilica datasus list cnes-pf

# 2. Baixar microdados de cnes-pf (uf+yearmonth); restrinja UF e período pelo volume
quantilica datasus sync cnes-pf -o ./data --start 2024-01 --end 2024-03 --regions sp

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync cnes-pf -o ./data --docs --aux --start 2024-01 --end 2024-03

# 4. Pipeline completo até Parquet tratado
quantilica datasus pipeline cnes-pf -o ./data/raw --parquet-dir ./data/parquet --start 2024-01 --end 2024-03
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

qdf = read_dbc("data/cnes-pf/2024-01/cnes-pf_202401-sp@20261015.dbc", clean=True)

# Médicos distintos (CBO inicia com 225) vinculados ao SUS
medicos = qdf.filter(
    pl.col("cbo").str.starts_with("2254") & (pl.col("prof_sus") == "1")
).select(pl.col("cpf_prof").n_unique().alias("medicos_sus"))
print(medicos)
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/Dados/PF`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **CNES — site oficial e Wiki CNES**: https://cnes.datasus.gov.br/ e https://wiki.saude.gov.br/cnes/
- **Nota Técnica `IT_CNES_1706.pdf`** (layout PF) e `TAB_CNES.zip` (tabela CBO e conselhos)
- **Portaria GM/MS nº 1.646/2015** (institui o CNES)
- **PCDaS/Fiocruz — CNES**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/cnes
