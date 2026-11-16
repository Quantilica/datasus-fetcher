---
dataset:
  id: sismama-cm
  fonte: datasus
  titulo: Citopatológico de Mama
  resumo: 'Citopatológico de Mama do DATASUS: um exame citopatológico de mama.'
  orgao: Ministério da Saúde — Instituto Nacional de Câncer (INCA) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SISCAN/SISMAMA/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2009-01
    fim: 2015-07
  unidade: um exame citopatológico de mama
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
    colunas: 56
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Citopatológico de Mama (`sismama-cm`)

## Resumo

Microdados do SISMAMA (INCA/DATASUS) com os exames citopatológicos de mama realizados no SUS entre 2009 e 2015, por UF e mês. Cada linha representa um exame.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** Não aplicável (o catálogo `meta.docs` não define diretório de documentação para este sistema)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SISCAN/SISMAMA/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SISCAN/SISMAMA/Dados` | `CM` | `uf_year2_month_pattern` — UF (2 letras) + ano (2 dígitos) + mês (2 dígitos) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `CMSP1001.dbc` — `CM` (citopatológico de mama) + `SP` (UF) + `10` (ano 2010) + `01` (mês).
- **No armazenamento local do `datasus-fetcher`**: `data/sismama-cm/<AAAAMM>/sismama-cm_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sismama-cm/202401/sismama-cm_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação: nenhum arquivo catalogado em `documentation/sismama.json` (não há `meta.docs` para `sismama`); o dicionário de variáveis está dentro do pacote de tabulação listado abaixo.
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/sismama.json`):
    - `/dissemin/publicos/SISCAN/SISMAMA/Auxiliar/TAB_SISMAMA.zip` (3.2 MB)

## Conteúdo

O SISCOLO (Sistema de Informações do Câncer do Colo do Útero) e o SISMAMA (Sistema de Informação do Câncer de Mama) foram criados pelo Instituto Nacional de Câncer (INCA) e pelo DATASUS para apoiar o monitoramento e a gestão dos programas nacionais de controle dos cânceres do colo do útero e de mama, registrando os exames de rastreamento e de confirmação diagnóstica realizados no SUS. A partir de 2013 ambos foram substituídos gradualmente pelo Sistema de Informação do Câncer (SISCAN), implantado pela Portaria GM/MS nº 3.394/2013 em plataforma web; no FTP, os arquivos do SISCOLO e do SISMAMA ficam sob `SISCAN/` e cobrem apenas o período em que os sistemas legados estavam em uso. Cobertura no FTP: janeiro/2009 a julho/2015, 27 UF, mensal.

Este dataset contém os exames citopatológicos de mama (punção aspirativa por agulha fina e citologia de secreção), realizados na investigação diagnóstica de lesões palpáveis ou suspeitas; a unidade de análise é o exame. O instrumento é a requisição/laudo citopatológico de mama, preenchido pelos laboratórios no SISMAMA.

Indicadores: percentual de exames suspeitos ou positivos, percentual de amostras insatisfatórias e fluxo da investigação (citologia → histopatologia). O volume é pequeno (~5 MB), pois o exame é restrito à investigação diagnóstica; a mamografia de rastreamento não está neste dataset.

No fluxo do SISMAMA, o citopatológico antecede a confirmação histopatológica (`sismama-hm`).

### Cobertura observada

- Índice do FTP (2026-10): 1675 arquivos, de 2009-01 a 2015-07, 27 UF(s) com arquivos, última atualização em 2022-08-31.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2009-09 a 2015-07), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Nomes verificados contra o arquivo real `CMSP1501.dbc` (54 colunas; resultado do exame citopatológico de mama). Cada linha é um registro agregado de exames da competência.

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
| `CANMPACANC` | String | Paciente com câncer de mama prévio (indicador). |
| `CO_CLI_DES` / `CO_CLI_NOD` / `CCLIMATMAM` / `CCLIMATDPC` | String | Dados clínicos: descarga papilar, nódulo e achados de mama/densidade. |
| `CO_RES_ADE` / `PRESULPAAF` | String | Adequabilidade do material e resultado da PAAF. |
| `CRESBENIG` / `CRESMALIIN` / `CRESSUSMAL` / `CRESPOSMAL` / `CRESDERPAP` | String | Resultado do exame citopatológico: benigno, maligno indeterminado, suspeito, positivo e derrame papilar. |
| `PBENMASTIT` / `PBENABSUBA` / `PBENFIBROA` / `PBENNECGOR` / `PBENCONDFI` / `PBENLESEPI` / `PBENOUTRAS` | String (8) | Contadores de achados benignos (mastite, abscesso subareolar, fibroadenoma, necrose gordurosa, condição fibrocística, lesão epitelial e outras). |
| `PMALINTUMP` / `PMALINTUMF` / `PMALINOUTR` / `PSUSLEJPCA` / `PSUSOUTROS` / `PPOSMACDUC` / `PPOSMACLOB` / `PPOSMACOUT` | String (8) | Contadores de achados malignos, suspeitos e positivos (carcinoma ductal, lobular e outros). |
| `DEMATACELU` / `DENEGMALIG` / `DEMALIINDT` / `DEPOSMALIG` / `DELESMALIG` / `DEPROCINFL` | String (8) | Contadores de derrame papilar e processo inflamatório (material acelular, negativo, indeterminado, positivo etc.). |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_pac_uf` | `CO_PAC_UF` | texto | UF de residência da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_us_uf` | `CO_US_UF` | texto | UF da unidade de saúde solicitante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_ibg` | `CO_PAC_IBG` | texto | Município de residência da paciente (código IBGE) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_us_ibge` | `CO_US_IBGE` | texto | Município da unidade de saúde solicitante (código IBGE) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_us` | `CO_US` | texto | Código da unidade de saúde solicitante do exame (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_cnes` | `CO_CNES` | texto | Código CNES do estabelecimento responsável pelo laudo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `prestuf` | `PRESTUF` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `regus` | `REGUS` | texto | Região de saúde da unidade solicitante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `regresid` | `REGRESID` | texto | Região de saúde de residência da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `reglab` | `REGLAB` | texto | Região de saúde do laboratório (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ano_comp` | `ANO_COMP` | texto | Ano da competência do laudo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `prestmun` | `PRESTMUN` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `dt_id_comp` | `DT_ID_COMP` | texto | Competência da data do laudo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_fx_etar` | `CO_FX_ETAR` | texto | Faixa etária da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_esc` | `CO_PAC_ESC` | texto | Escolaridade da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_sex` | `CO_PAC_SEX` | texto | Sexo da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_rac` | `CO_PAC_RAC` | texto | Raça/cor da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `canmpacanc` | `CANMPACANC` | texto | Campo do laudo do SISMAMA (`CANMPACANC`); sem dicionário oficial no FTP | — | todos |
| `co_cli_des` | `CO_CLI_DES` | texto | Campo do laudo do SISMAMA (`CO_CLI_DES`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_cli_nod` | `CO_CLI_NOD` | texto | Campo do laudo do SISMAMA (`CO_CLI_NOD`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cclimatmam` | `CCLIMATMAM` | texto | Campo do laudo do SISMAMA (`CCLIMATMAM`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cclimatdpc` | `CCLIMATDPC` | texto | Campo do laudo do SISMAMA (`CCLIMATDPC`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `dintcoleta` | `DINTCOLETA` | texto | Dias entre a coleta e o recebimento da amostra (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dintresult` | `DINTRESULT` | texto | Dias entre o recebimento e o resultado (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dinttempex` | `DINTTEMPEX` | texto | Dias entre a coleta e o resultado (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_res_ade` | `CO_RES_ADE` | texto | Campo do laudo do SISMAMA (`CO_RES_ADE`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `presulpaaf` | `PRESULPAAF` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `cresbenig` | `CRESBENIG` | texto | Campo do laudo do SISMAMA (`CRESBENIG`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cresmaliin` | `CRESMALIIN` | texto | Campo do laudo do SISMAMA (`CRESMALIIN`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cressusmal` | `CRESSUSMAL` | texto | Campo do laudo do SISMAMA (`CRESSUSMAL`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cresposmal` | `CRESPOSMAL` | texto | Campo do laudo do SISMAMA (`CRESPOSMAL`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cresderpap` | `CRESDERPAP` | texto | Campo do laudo do SISMAMA (`CRESDERPAP`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `quantexame` | `QUANTEXAME` | texto | Quantidade de exames do registro (agregação) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `pbenmastit` | `PBENMASTIT` | texto | Campo do laudo do SISMAMA (`PBENMASTIT`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `pbenabsuba` | `PBENABSUBA` | texto | Campo do laudo do SISMAMA (`PBENABSUBA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `pbenfibroa` | `PBENFIBROA` | texto | Campo do laudo do SISMAMA (`PBENFIBROA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `pbennecgor` | `PBENNECGOR` | texto | Campo do laudo do SISMAMA (`PBENNECGOR`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `pbencondfi` | `PBENCONDFI` | texto | Campo do laudo do SISMAMA (`PBENCONDFI`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `pbenlesepi` | `PBENLESEPI` | texto | Campo do laudo do SISMAMA (`PBENLESEPI`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `pbenoutras` | `PBENOUTRAS` | texto | Campo do laudo do SISMAMA (`PBENOUTRAS`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `pmalintump` | `PMALINTUMP` | texto | Campo do laudo do SISMAMA (`PMALINTUMP`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `pmalintumf` | `PMALINTUMF` | texto | Campo do laudo do SISMAMA (`PMALINTUMF`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `pmalinoutr` | `PMALINOUTR` | texto | Campo do laudo do SISMAMA (`PMALINOUTR`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `psuslejpca` | `PSUSLEJPCA` | texto | Campo do laudo do SISMAMA (`PSUSLEJPCA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `psusoutros` | `PSUSOUTROS` | texto | Campo do laudo do SISMAMA (`PSUSOUTROS`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `pposmacduc` | `PPOSMACDUC` | texto | Campo do laudo do SISMAMA (`PPOSMACDUC`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `pposmaclob` | `PPOSMACLOB` | texto | Campo do laudo do SISMAMA (`PPOSMACLOB`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `pposmacout` | `PPOSMACOUT` | texto | Campo do laudo do SISMAMA (`PPOSMACOUT`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `dematacelu` | `DEMATACELU` | texto | Campo do laudo do SISMAMA (`DEMATACELU`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `denegmalig` | `DENEGMALIG` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `demaliindt` | `DEMALIINDT` | texto | Campo do laudo do SISMAMA (`DEMALIINDT`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `deposmalig` | `DEPOSMALIG` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `delesmalig` | `DELESMALIG` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `deprocinfl` | `DEPROCINFL` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sismama-cm`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): texto: 56.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `sismama-cm.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sismama-cm").glob("**/*.parquet"))
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
datasus-fetcher list sismama-cm

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sismama-cm -o ./data --start 2024-01 --end 2024-12 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sismama-cm
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
