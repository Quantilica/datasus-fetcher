---
dataset:
  id: sismama-hm
  fonte: datasus
  titulo: Histopatológico de Mama
  resumo: Microdados do SISMAMA (INCA/DATASUS) com os laudos histopatológicos de mama realizados no SUS entre 2009 e 2015, por UF e mês.
  orgao: Ministério da Saúde — Instituto Nacional de Câncer (INCA) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SISCAN/SISMAMA/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2009-01
    fim: 2015-07
  unidade: um laudo histopatológico de mama
  granularidade:
    espacial: município de residência da paciente e da unidade de saúde; um arquivo por UF
    temporal: competência (mês)
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo por UF e competência mensal
  lake:
    estado: convertido
    particoes:
    - ano
    - mes
    chave: []
    colunas: 57
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Histopatológico de Mama (`sismama-hm`)

## Resumo

Microdados do SISMAMA (INCA/DATASUS) com os laudos histopatológicos de mama realizados no SUS entre 2009 e 2015, por UF e mês. Cada linha é um laudo histopatológico.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (dBASE comprimido no formato DATASUS; descompactado nativamente em Rust para `.dbf`)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf / yearmonth`
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2009-01 a 2015-07 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 1674 arquivos (~5,9 MB); 27 UF(s) na partição; última atualização 2022-08-31
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Não
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): Não aplicável (o catálogo `meta.docs` não define diretório de documentação para este sistema)
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SISCAN/SISMAMA/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SISCAN/SISMAMA/Dados` | `HM` | `uf_year2_month_pattern` — UF (2 letras) + ano (2 dígitos) + mês (2 dígitos) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `HMSP1001.dbc` — `HM` (histopatológico de mama) + `SP` (UF) + `10` (ano 2010) + `01` (mês).
- **No armazenamento local do `datasus-fetcher`**: `data/sismama-hm/<AAAAMM>/sismama-hm_<AAAAMM>-<uf>@<AAAAMMDD>.dbc` (ex.: `data/sismama-hm/201001/sismama-hm_201001-sp@20220817.dbc`).
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação: nenhum arquivo catalogado em `documentation/sismama.json` (não há `meta.docs` para `sismama`); o dicionário de variáveis está dentro do pacote de tabulação listado abaixo.
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/sismama.json`):
    - `/dissemin/publicos/SISCAN/SISMAMA/Auxiliar/TAB_SISMAMA.zip` (3.2 MB)

## Conteúdo

O SISCOLO (Sistema de Informações do Câncer do Colo do Útero) e o SISMAMA (Sistema de Informação do Câncer de Mama) foram criados pelo Instituto Nacional de Câncer (INCA) e pelo DATASUS para apoiar o monitoramento e a gestão dos programas nacionais de controle dos cânceres do colo do útero e de mama, registrando os exames de rastreamento e de confirmação diagnóstica realizados no SUS. A partir de 2013 ambos foram substituídos gradualmente pelo Sistema de Informação do Câncer (SISCAN), implantado pela Portaria GM/MS nº 3.394/2013 em plataforma web; no FTP, os arquivos do SISCOLO e do SISMAMA ficam sob `SISCAN/` e cobrem apenas o período em que os sistemas legados estavam em uso. Cobertura no FTP: janeiro/2009 a julho/2015, 27 UF, mensal.

Este dataset reúne os laudos histopatológicos de mama, incluindo biópsias e peças cirúrgicas, com dados de diagnóstico, estadiamento patológico e margens; a unidade de análise é o laudo. O instrumento é a requisição/laudo histopatológico de mama, preenchido pelos laboratórios no SISMAMA.

Indicadores: proporção de lesões malignas entre as biópsias, distribuição por tipo histológico, tamanho tumoral e acometimento linfonodal ao diagnóstico, que servem como proxy de estadiamento.

Sucede o `sismama-cm` na confirmação diagnóstica; volume pequeno (~6 MB).

### Cobertura observada

- Índice do FTP (2026-10): 1674 arquivos, de 2009-01 a 2015-07, 27 UF(s) com arquivos, última atualização em 2022-08-31.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2009-12 a 2015-01), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Nomes verificados contra o arquivo real `HMSP1505.dbc` (55 colunas; resultado do exame histopatológico de mama). Cada linha é um registro agregado de exames da competência.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CO_PAC_UF` / `CO_PAC_IBG` | String | UF e município (IBGE, 7) de residência da paciente. |
| `CO_US_UF` / `CO_US_IBGE` / `CO_US` / `CO_CNES` | String | UF, município (IBGE, 7), código e CNES da unidade solicitante. |
| `PRESTUF` / `PRESTMUN` | String | UF e município do prestador do serviço. |
| `REGUS` / `REGRESID` / `REGLAB` | String | Indicadores de região da unidade, da residência e do laboratório. |
| `ANO_COMP` / `DT_ID_COMP` | String | Ano e competência (`AAAAMM`) do registro. |
| `CO_FX_ETAR` | String | Faixa etária da paciente. |
| `CO_PAC_ESC` / `CO_PAC_SEX` / `CO_PAC_RAC` | String | Escolaridade, sexo e raça/cor da paciente. |
| `DINTCOLETA` / `DINTRESULT` / `DINTTEMPEX` | String | Intervalos (categorizados) entre coleta, resultado e tempo de exame. |
| `QUANTEXAME` | String (8) | Quantidade de exames do registro. |
| `CCLITPEXA` / `CCLITANT` / `CCLIDIAGIM` / `CCLILOCA` | String | Dados clínicos: tipo de exame, antecedentes, diagnóstico por imagem e localização. |
| `CHISLINFCO` / `CHISRECES` / `CHISRECPR` | String | Histórico de linfonodos comprometidos e recidivas. |
| `C_CLI_TCAN` / `C_CLI_DETE` / `CO_CLI_MAM` / `CO_CLI_TAM` / `CO_TAM_TUM` / `C_CLI_LINF` / `CCLIMATPRO` | String | Dados clínicos do tumor: tipo de câncer, detecção, mama, tamanho e linfonodos. |
| `CRESPROCIR` / `CO_RES_ADE` / `CMICMICRCA` | String | Procedimento cirúrgico, adequabilidade do material (texto) e microcalcificações. |
| `C_NEO_MALI` / `CO_HIS_GRA` / `CO_HIS_MAR` | String | Neoplasia maligna, grau histológico e margens. |
| `LESBENIGIN` / `CNEOMALIG` / `CBENHIPSAT` / `CBENHIPCAT` / `CBENLOBCAT` / `CBENADENOS` / `CBENESDERO` / `CBENFIBROC` / `CBENFIBROA` / `CBENSOLITA` / `CBENMULTI` / `CBENFLORID` / `CBENMASTIT` / `CBENOUTROS` | String (8) | Contadores de lesões benignas (hiperplasias, adenose, esclerose, fibrose, fibroadenoma, papiloma, mastite e outras) e neoplasias malignas. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_pac_uf` | `CO_PAC_UF` | texto | UF de residência da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_us_uf` | `CO_US_UF` | texto | UF da unidade de saúde solicitante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_ibg` | `CO_PAC_IBG` | texto | Município de residência da paciente (código IBGE) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_us_ibge` | `CO_US_IBGE` | texto | Município da unidade de saúde solicitante (código IBGE) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_us` | `CO_US` | texto | Código da unidade de saúde solicitante do exame (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_cnes` | `CO_CNES` | texto | Código CNES do estabelecimento responsável pelo laudo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `prestuf` | `PRESTUF` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `prestmun` | `PRESTMUN` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `regus` | `REGUS` | texto | Região de saúde da unidade solicitante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `regresid` | `REGRESID` | texto | Região de saúde de residência da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `reglab` | `REGLAB` | texto | Região de saúde do laboratório (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ano_comp` | `ANO_COMP` | texto | Ano da competência do laudo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_id_comp` | `DT_ID_COMP` | texto | Competência da data do laudo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_fx_etar` | `CO_FX_ETAR` | texto | Faixa etária da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_esc` | `CO_PAC_ESC` | texto | Escolaridade da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_sex` | `CO_PAC_SEX` | texto | Sexo da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_rac` | `CO_PAC_RAC` | texto | Raça/cor da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `cclitpexa` | `CCLITPEXA` | texto | Campo do laudo do SISMAMA (`CCLITPEXA`); sem dicionário oficial no FTP | — | todos |
| `cclitant` | `CCLITANT` | texto | Campo do laudo do SISMAMA (`CCLITANT`); sem dicionário oficial no FTP | — | todos |
| `cclidiagim` | `CCLIDIAGIM` | texto | Campo do laudo do SISMAMA (`CCLIDIAGIM`); sem dicionário oficial no FTP | — | todos |
| `ccliloca` | `CCLILOCA` | texto | Campo do laudo do SISMAMA (`CCLILOCA`); sem dicionário oficial no FTP | — | todos |
| `chislinfco` | `CHISLINFCO` | texto | Campo do laudo do SISMAMA (`CHISLINFCO`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `chisreces` | `CHISRECES` | texto | Campo do laudo do SISMAMA (`CHISRECES`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `chisrecpr` | `CHISRECPR` | texto | Campo do laudo do SISMAMA (`CHISRECPR`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `c_cli_tcan` | `C_CLI_TCAN` | texto | Campo do laudo do SISMAMA (`C_CLI_TCAN`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `c_cli_dete` | `C_CLI_DETE` | texto | Campo do laudo do SISMAMA (`C_CLI_DETE`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_cli_mam` | `CO_CLI_MAM` | texto | Campo do laudo do SISMAMA (`CO_CLI_MAM`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_cli_tam` | `CO_CLI_TAM` | texto | Campo do laudo do SISMAMA (`CO_CLI_TAM`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_tam_tum` | `CO_TAM_TUM` | texto | Campo do laudo do SISMAMA (`CO_TAM_TUM`); sem dicionário oficial no FTP | — | todos |
| `c_cli_linf` | `C_CLI_LINF` | texto | Campo do laudo do SISMAMA (`C_CLI_LINF`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cclimatpro` | `CCLIMATPRO` | texto | Campo do laudo do SISMAMA (`CCLIMATPRO`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `dintcoleta` | `DINTCOLETA` | texto | Dias entre a coleta e o recebimento da amostra (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dintresult` | `DINTRESULT` | texto | Dias entre o recebimento e o resultado (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dinttempex` | `DINTTEMPEX` | texto | Dias entre a coleta e o resultado (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `cresprocir` | `CRESPROCIR` | texto | Campo do laudo do SISMAMA (`CRESPROCIR`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_res_ade` | `CO_RES_ADE` | texto | Campo do laudo do SISMAMA (`CO_RES_ADE`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cmicmicrca` | `CMICMICRCA` | texto | Pesquisa de microbiologia no exame (SISMAMA); campo `CMICMICRCA`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `c_neo_mali` | `C_NEO_MALI` | texto | Campo do laudo do SISMAMA (`C_NEO_MALI`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_his_gra` | `CO_HIS_GRA` | texto | Campo do laudo do SISMAMA (`CO_HIS_GRA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_his_mar` | `CO_HIS_MAR` | texto | Campo do laudo do SISMAMA (`CO_HIS_MAR`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `quantexame` | `QUANTEXAME` | texto | Quantidade de exames do registro (agregação) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `lesbenigin` | `LESBENIGIN` | texto | Campo do laudo do SISMAMA (`LESBENIGIN`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cneomalig` | `CNEOMALIG` | texto | Campo do laudo do SISMAMA (`CNEOMALIG`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cbenhipsat` | `CBENHIPSAT` | texto | Alteração celular benigna ou resultado benigno do laudo (SISMAMA); campo `CBENHIPSAT` | — | todos |
| `cbenhipcat` | `CBENHIPCAT` | texto | Alteração celular benigna ou resultado benigno do laudo (SISMAMA); campo `CBENHIPCAT` | — | todos |
| `cbenlobcat` | `CBENLOBCAT` | texto | Alteração celular benigna ou resultado benigno do laudo (SISMAMA); campo `CBENLOBCAT` | — | todos |
| `cbenadenos` | `CBENADENOS` | texto | Alteração celular benigna ou resultado benigno do laudo (SISMAMA); campo `CBENADENOS` | — | todos |
| `cbenesdero` | `CBENESDERO` | texto | Alteração celular benigna ou resultado benigno do laudo (SISMAMA); campo `CBENESDERO` | — | todos |
| `cbenfibroc` | `CBENFIBROC` | texto | Alteração celular benigna ou resultado benigno do laudo (SISMAMA); campo `CBENFIBROC` | — | todos |
| `cbenfibroa` | `CBENFIBROA` | texto | Alteração celular benigna ou resultado benigno do laudo (SISMAMA); campo `CBENFIBROA` | — | todos |
| `cbensolita` | `CBENSOLITA` | texto | Alteração celular benigna ou resultado benigno do laudo (SISMAMA); campo `CBENSOLITA` | — | todos |
| `cbenmulti` | `CBENMULTI` | texto | Alteração celular benigna ou resultado benigno do laudo (SISMAMA); campo `CBENMULTI` | — | todos |
| `cbenflorid` | `CBENFLORID` | texto | Alteração celular benigna ou resultado benigno do laudo (SISMAMA); campo `CBENFLORID` | — | todos |
| `cbenmastit` | `CBENMASTIT` | texto | Alteração celular benigna ou resultado benigno do laudo (SISMAMA); campo `CBENMASTIT` | — | todos |
| `cbenoutros` | `CBENOUTROS` | texto | Alteração celular benigna ou resultado benigno do laudo (SISMAMA); campo `CBENOUTROS` | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sismama-hm`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): texto: 57.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sismama-hm.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sismama-hm/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "mes", "uf")
    .agg(pl.len().alias("linhas"))
    .sort("ano", "mes", "uf")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

> `quantilica datasus <subcomando>` e `datasus-fetcher <subcomando>` são equivalentes.

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sismama-hm
quantilica datasus list sismama-hm

# 2. Baixar microdados de sismama-hm com recorte adequado à partição (uf / yearmonth)
quantilica datasus sync sismama-hm -o ./data --start 2010-01 --end 2012-12 --regions sp rj

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sismama-hm -o ./data --start 2010-01 --end 2012-12 --regions sp rj --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sismama-hm -o ./data/raw --parquet-dir ./data/parquet --start 2010-01 --end 2012-12 --regions sp rj
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl

frame = df.read_dbc(
    "data/sismama-hm/201001/sismama-hm_201001-sp@20220817.dbc", dataset="sismama-hm"
)
print(frame.shape)
print(frame.columns)

print(
    frame.group_by("cclilo ca".replace(" ", ""))
    .len()
    .sort("len", descending=True)
    .head(10)
)
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SISCAN/SISMAMA/Dados`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **INCA — Sistema de Informação do Câncer (SISCAN)**: https://www.gov.br/inca/pt-br/assuntos/gestor-e-profissional-de-saude/siscan
- **Portaria GM/MS nº 3.394/2013** — institui o SISCAN.
- **Pacote de tabulação no FTP**: `TAB_SISMAMA.zip` (inclui o dicionário de variáveis e arquivos `.cnv`/`.def` para tabulação).
- **PCDaS / Fiocruz**: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde** (DATASUS): https://wiki.saude.gov.br/
