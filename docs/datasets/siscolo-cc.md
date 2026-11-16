---
dataset:
  id: siscolo-cc
  fonte: datasus
  titulo: Citopatológico de Colo de Útero
  resumo: 'Citopatológico de Colo de Útero do DATASUS: um exame citopatológico do colo do útero.'
  orgao: Ministério da Saúde — Instituto Nacional de Câncer (INCA) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SISCAN/SISCOLO4/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2006-01
    fim: 2015-10
  unidade: um exame citopatológico do colo do útero
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
    colunas: 104
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Citopatológico de Colo de Útero (`siscolo-cc`)

## Resumo

Microdados do SISCOLO (INCA/DATASUS) com os laudos citopatológicos do colo do útero realizados no SUS entre 2006 e 2015, por UF e mês. Cada linha representa um exame citopatológico.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** Não aplicável (o catálogo `meta.docs` não define diretório de documentação para este sistema)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SISCAN/SISCOLO4/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SISCAN/SISCOLO4/Dados` | `CC` | `uf_year2_month_pattern` — UF (2 letras) + ano (2 dígitos) + mês (2 dígitos) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `CCSP1001.dbc` — `CC` (citopatológico) + `SP` (UF) + `10` (ano 2010) + `01` (mês).
- **No armazenamento local do `datasus-fetcher`**: `data/siscolo-cc/<AAAAMM>/siscolo-cc_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/siscolo-cc/202401/siscolo-cc_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação: nenhum arquivo catalogado em `documentation/siscolo.json` (não há `meta.docs` para `siscolo`); o dicionário de variáveis está dentro do pacote de tabulação listado abaixo.
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/siscolo.json`):
    - `/dissemin/publicos/SISCAN/SISCOLO4/Auxiliar/TAB_SISCOLO4.zip` (1.7 MB)

## Conteúdo

O SISCOLO (Sistema de Informações do Câncer do Colo do Útero) e o SISMAMA (Sistema de Informação do Câncer de Mama) foram criados pelo Instituto Nacional de Câncer (INCA) e pelo DATASUS para apoiar o monitoramento e a gestão dos programas nacionais de controle dos cânceres do colo do útero e de mama, registrando os exames de rastreamento e de confirmação diagnóstica realizados no SUS. A partir de 2013 ambos foram substituídos gradualmente pelo Sistema de Informação do Câncer (SISCAN), implantado pela Portaria GM/MS nº 3.394/2013 em plataforma web; no FTP, os arquivos do SISCOLO e do SISMAMA ficam sob `SISCAN/` e cobrem apenas o período em que os sistemas legados estavam em uso. Cobertura no FTP: janeiro/2006 a outubro/2015, 27 UF, mensal.

Este dataset contém os laudos de exames citopatológicos (Papanicolaou) do colo do útero, usados no rastreamento organizado da população feminina de 25 a 64 anos; a unidade de análise é o exame (um laudo por linha, não uma mulher). O instrumento de coleta é o requisição/laudo do exame citopatológico, digitado pelos laboratórios no SISCOLO.

Indicadores: cobertura do rastreamento, razão de exames citopatológicos em mulheres de 25–64 anos, percentual de amostras insatisfatórias, percentual de exames alterados (ASC-US, LSIL, HSIL…) e positividade. Uma mulher pode aparecer em vários exames; o rastreamento individual exige vinculação por identificador, quando disponível.

Volume expressivo (~2,5 GB, 2.858 arquivos) em razão do número de exames; prefira recortes por UF e período.

### Cobertura observada

- Índice do FTP (2026-10): 2858 arquivos, de 2006-01 a 2015-10, 27 UF(s) com arquivos, última atualização em 2022-08-17.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2006-05 a 2015-02), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Nomes verificados contra o arquivo real `CCRJ1503.dbc` (102 colunas; resultado do exame citopatológico do colo do útero). Cada linha é um registro agregado de exames da competência, por isso há muitos contadores (`String` de 8 caracteres).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CO_US` / `CO_US_UF` / `CO_US_IBGE` | String | Unidade solicitante: código, UF e município (IBGE, 7). |
| `CO_CNES` | String (CNES, 7) | CNES do estabelecimento. |
| `REGUS` / `REGRESID` / `REGLAB` | String | Indicadores de região da unidade, da residência e do laboratório. |
| `CO_PAC_UF` / `CO_PAC_IBG` | String | UF e município (IBGE, 7) de residência da paciente. |
| `ANO_COMP` / `DT_ID_COMP` | String | Ano e competência (`AAAAMM`) do registro. |
| `CO_FX_ETAR` | String | Faixa etária da paciente. |
| `DINTCOLETA` / `DINTRESULT` / `DINTTEMPEX` | String | Intervalos (categorizados) entre coleta, resultado e tempo de exame. |
| `QTDEXA` | String | Quantidade de exames do registro. |
| `CO_PAC_IDA` | String (3) | Idade da paciente. |
| `CO_PAC_ESC` / `CO_PAC_RAC` | String | Escolaridade e raça/cor da paciente. |
| `CO_RES_NOR` | String | Indicador de residência (campo do layout). |
| `CLABIBGE` / `CLABUF` | String | Município (IBGE, 7) e UF do laboratório. |
| `CO_ATI_ESC` / `CO_ATI_GLA` / `CO_ATI_IND` / `CO_CEL_ESC` / `CO_CEL_GLA` / `CO_NEO_MAL` | String | Indicadores de atipias e neoplasia maligna nas células escamosas e glandulares. |
| `CO_AMOSTRA` / `CO_ADEQ_MA` | String | Indicador de amostra e adequabilidade do material (satisfatória/insatisfatória). |
| `CO_BEN_INF` / `CO_BEN_MET` / `CO_BEN_REP` / `CO_BEN_ATR` / `CO_BEN_RAD` / `CO_BEN_OUT` | String | Alterações benignas: inflamação, metaplasia, reparação, atrofia, radiação e outras. |
| `CO_MIC_LAC` / `CO_MIC_COC` / `CO_MIC_CHL` / `CO_MIC_ACT` / `CO_MIC_BAC` / `CO_MIC_TRI` / `CO_MIC_HER` / `CO_MIC_CAN` / `CO_MIC_GAR` / `CO_MIC_OUT` | String | Microbiologia: Lactobacillus, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, herpes, Candida, Gardnerella e outros. |
| `CO_ANM_PRE` / `DT_ANM_PRE` | String | Exame citopatológico anterior e ano de realização. |
| `ST_MON_EXT` / `TEMPCITANT` | String | Indicadores de monitoramento externo e tempo desde a citologia anterior. |
| `QUANTEXAME` / `REPREZT` / `RESNORM` / `POSNAONEO` / `LESALTGRA` / `PSNAONPLA` / `NLSALTGRA` / `PSNNPLA` / `NALTGRA` / `LBGRAU` / `LAGRAU` / `LAGRAUMI`` | String (8) | Contadores agregados por registro de resultados (representatividade, normal, lesões de baixo e alto grau etc.). |
| `CARCINO` / `C_EPI_ESCA` / `C_EPI_GLAN` / `CO_EPI_MET` / `ADENCARCIN` / `DENCARCINV` / `OUTNEO` / `ALTERADO` / `CVCIONAL` / `MEIOLIQU` | String (8) | Contadores de carcinomas epiteliais, adenocarcinomas, outras neoplasias e demais resultados. |
| `AMOSREJAUS` / `AMOSREJDAN` / `AMOSREJALH` / `AMOSREJOUT` / `REJEITADA` / `SATISFACT` / `INSATSFAC` / `CO_INSA_AC` / `CO_INSA_SA` / `CO_INSA_PI` / `CO_INSA_AR` / `CO_INSA_CO` / `CO_INSA_SU` / `CO_INSA_OU` | String (8) | Contadores de amostras rejeitadas, satisfatórias e insatisfatórias, com motivos. |
| `CBEMINFLA` / `CBEMMETAS` / `CBEMREPAR` / `CBEMATROF` / `CBEMRADI` / `CBEMOUT` / `CMICLACT` / `CMICCOCO` / `CMICCHLA` / `CMICACTI` / `CMICBACI` / `CMICTRICO` / `CMICHERP` / `CMICCAND` / `CMICGARD` / `CMICOUT`` | String (8) | Contadores agregados de alterações benignas e microbiologia. |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_us` | `CO_US` | texto | Código da unidade de saúde solicitante do exame (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_us_uf` | `CO_US_UF` | texto | UF da unidade de saúde solicitante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_us_ibge` | `CO_US_IBGE` | texto | Município da unidade de saúde solicitante (código IBGE) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `regus` | `REGUS` | texto | Região de saúde da unidade solicitante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_ibg` | `CO_PAC_IBG` | texto | Município de residência da paciente (código IBGE) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_uf` | `CO_PAC_UF` | texto | UF de residência da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_esc` | `CO_PAC_ESC` | texto | Escolaridade da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_res_nor` | `CO_RES_NOR` | texto | Campo do laudo do SISCOLO (`CO_RES_NOR`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_pac_ida` | `CO_PAC_IDA` | texto | Idade da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `regresid` | `REGRESID` | texto | Região de saúde de residência da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_cnes` | `CO_CNES` | texto | Código CNES do estabelecimento responsável pelo laudo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `clabibge` | `CLABIBGE` | texto | Município do laboratório (código IBGE) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `clabuf` | `CLABUF` | texto | UF do laboratório (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `reglab` | `REGLAB` | texto | Região de saúde do laboratório (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_id_comp` | `DT_ID_COMP` | texto | Competência da data do laudo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ano_comp` | `ANO_COMP` | texto | Ano da competência do laudo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_fx_etar` | `CO_FX_ETAR` | texto | Faixa etária da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_rac` | `CO_PAC_RAC` | texto | Raça/cor da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_ati_esc` | `CO_ATI_ESC` | texto | Campo do laudo do SISCOLO (`CO_ATI_ESC`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_ati_gla` | `CO_ATI_GLA` | texto | Campo do laudo do SISCOLO (`CO_ATI_GLA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_ati_ind` | `CO_ATI_IND` | texto | Campo do laudo do SISCOLO (`CO_ATI_IND`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_cel_esc` | `CO_CEL_ESC` | texto | Campo do laudo do SISCOLO (`CO_CEL_ESC`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_cel_gla` | `CO_CEL_GLA` | texto | Campo do laudo do SISCOLO (`CO_CEL_GLA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_neo_mal` | `CO_NEO_MAL` | texto | Campo do laudo do SISCOLO (`CO_NEO_MAL`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_amostra` | `CO_AMOSTRA` | texto | Campo do laudo do SISCOLO (`CO_AMOSTRA`); sem dicionário oficial no FTP | — | todos |
| `co_adeq_ma` | `CO_ADEQ_MA` | texto | Campo do laudo do SISCOLO (`CO_ADEQ_MA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_ben_inf` | `CO_BEN_INF` | texto | Alteração celular benigna ou resultado benigno do laudo (SISCOLO); campo `CO_BEN_INF` | — | todos |
| `co_ben_met` | `CO_BEN_MET` | texto | Alteração celular benigna ou resultado benigno do laudo (SISCOLO); campo `CO_BEN_MET` | — | todos |
| `co_ben_rep` | `CO_BEN_REP` | texto | Alteração celular benigna ou resultado benigno do laudo (SISCOLO); campo `CO_BEN_REP` | — | todos |
| `co_ben_atr` | `CO_BEN_ATR` | texto | Alteração celular benigna ou resultado benigno do laudo (SISCOLO); campo `CO_BEN_ATR` | — | todos |
| `co_ben_rad` | `CO_BEN_RAD` | texto | Alteração celular benigna ou resultado benigno do laudo (SISCOLO); campo `CO_BEN_RAD` | — | todos |
| `co_ben_out` | `CO_BEN_OUT` | texto | Alteração celular benigna ou resultado benigno do laudo (SISCOLO); campo `CO_BEN_OUT` | — | todos |
| `co_mic_lac` | `CO_MIC_LAC` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CO_MIC_LAC`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `co_mic_coc` | `CO_MIC_COC` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CO_MIC_COC`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `co_mic_chl` | `CO_MIC_CHL` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CO_MIC_CHL`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `co_mic_act` | `CO_MIC_ACT` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CO_MIC_ACT`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `co_mic_bac` | `CO_MIC_BAC` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CO_MIC_BAC`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `co_mic_tri` | `CO_MIC_TRI` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CO_MIC_TRI`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `co_mic_her` | `CO_MIC_HER` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CO_MIC_HER`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `co_mic_can` | `CO_MIC_CAN` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CO_MIC_CAN`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `co_mic_gar` | `CO_MIC_GAR` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CO_MIC_GAR`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `co_mic_out` | `CO_MIC_OUT` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CO_MIC_OUT`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `co_anm_pre` | `CO_ANM_PRE` | texto | Campo do laudo do SISCOLO (`CO_ANM_PRE`); sem dicionário oficial no FTP | — | todos |
| `dt_anm_pre` | `DT_ANM_PRE` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `st_mon_ext` | `ST_MON_EXT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `tempcitant` | `TEMPCITANT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `dintcoleta` | `DINTCOLETA` | texto | Dias entre a coleta e o recebimento da amostra (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dintresult` | `DINTRESULT` | texto | Dias entre o recebimento e o resultado (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dinttempex` | `DINTTEMPEX` | texto | Dias entre a coleta e o resultado (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `qtdexa` | `QTDEXA` | texto | Quantidade de exames do registro (agregação) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `reprezt` | `REPREZT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `resnorm` | `RESNORM` | texto | Resultado dentro dos limites da normalidade (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `posnaoneo` | `POSNAONEO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `lesaltgra` | `LESALTGRA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `psnaonpla` | `PSNAONPLA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `nlsaltgra` | `NLSALTGRA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `psnnpla` | `PSNNPLA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `naltgra` | `NALTGRA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `lbgrau` | `LBGRAU` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `lagrau` | `LAGRAU` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `lagraumi` | `LAGRAUMI` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `carcino` | `CARCINO` | texto | Campo do laudo do SISCOLO (`CARCINO`); sem dicionário oficial no FTP | — | todos |
| `c_epi_esca` | `C_EPI_ESCA` | texto | Campo do laudo do SISCOLO (`C_EPI_ESCA`); sem dicionário oficial no FTP | — | todos |
| `c_epi_glan` | `C_EPI_GLAN` | texto | Campo do laudo do SISCOLO (`C_EPI_GLAN`); sem dicionário oficial no FTP | — | todos |
| `co_epi_met` | `CO_EPI_MET` | texto | Campo do laudo do SISCOLO (`CO_EPI_MET`); sem dicionário oficial no FTP | — | todos |
| `adencarcin` | `ADENCARCIN` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `dencarcinv` | `DENCARCINV` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `outneo` | `OUTNEO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `alterado` | `ALTERADO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `cvcional` | `CVCIONAL` | texto | Campo do laudo do SISCOLO (`CVCIONAL`); sem dicionário oficial no FTP | — | todos |
| `meioliqu` | `MEIOLIQU` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `amosrejaus` | `AMOSREJAUS` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `amosrejdan` | `AMOSREJDAN` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `amosrejalh` | `AMOSREJALH` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `amosrejout` | `AMOSREJOUT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `rejeitada` | `REJEITADA` | texto | Amostra rejeitada (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `satisfact` | `SATISFACT` | texto | Amostra satisfatória para avaliação (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `insatsfac` | `INSATSFAC` | texto | Amostra insatisfatória para avaliação (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_insa_ac` | `CO_INSA_AC` | texto | Campo do laudo do SISCOLO (`CO_INSA_AC`); sem dicionário oficial no FTP | — | todos |
| `co_insa_sa` | `CO_INSA_SA` | texto | Campo do laudo do SISCOLO (`CO_INSA_SA`); sem dicionário oficial no FTP | — | todos |
| `co_insa_pi` | `CO_INSA_PI` | texto | Campo do laudo do SISCOLO (`CO_INSA_PI`); sem dicionário oficial no FTP | — | todos |
| `co_insa_ar` | `CO_INSA_AR` | texto | Campo do laudo do SISCOLO (`CO_INSA_AR`); sem dicionário oficial no FTP | — | todos |
| `co_insa_co` | `CO_INSA_CO` | texto | Campo do laudo do SISCOLO (`CO_INSA_CO`); sem dicionário oficial no FTP | — | todos |
| `co_insa_su` | `CO_INSA_SU` | texto | Campo do laudo do SISCOLO (`CO_INSA_SU`); sem dicionário oficial no FTP | — | todos |
| `co_insa_ou` | `CO_INSA_OU` | texto | Campo do laudo do SISCOLO (`CO_INSA_OU`); sem dicionário oficial no FTP | — | todos |
| `cbeminfla` | `CBEMINFLA` | texto | Campo do laudo do SISCOLO (`CBEMINFLA`); sem dicionário oficial no FTP | — | todos |
| `cbemmetas` | `CBEMMETAS` | texto | Campo do laudo do SISCOLO (`CBEMMETAS`); sem dicionário oficial no FTP | — | todos |
| `cbemrepar` | `CBEMREPAR` | texto | Campo do laudo do SISCOLO (`CBEMREPAR`); sem dicionário oficial no FTP | — | todos |
| `cbematrof` | `CBEMATROF` | texto | Campo do laudo do SISCOLO (`CBEMATROF`); sem dicionário oficial no FTP | — | todos |
| `cbemradi` | `CBEMRADI` | texto | Campo do laudo do SISCOLO (`CBEMRADI`); sem dicionário oficial no FTP | — | todos |
| `cbemout` | `CBEMOUT` | texto | Campo do laudo do SISCOLO (`CBEMOUT`); sem dicionário oficial no FTP | — | todos |
| `cmiclact` | `CMICLACT` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CMICLACT`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `cmiccoco` | `CMICCOCO` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CMICCOCO`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `cmicchla` | `CMICCHLA` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CMICCHLA`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `cmicacti` | `CMICACTI` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CMICACTI`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `cmicbaci` | `CMICBACI` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CMICBACI`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `cmictrico` | `CMICTRICO` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CMICTRICO`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `cmicherp` | `CMICHERP` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CMICHERP`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `cmiccand` | `CMICCAND` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CMICCAND`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `cmicgard` | `CMICGARD` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CMICGARD`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `cmicout` | `CMICOUT` | texto | Pesquisa de microbiologia no exame (SISCOLO); campo `CMICOUT`: presença do microrganismo indicado pelo nome (lactobacilos, cocos, Chlamydia, Actinomyces, bacilos, Trichomonas, Herpes, Candida, Gardnerella, outros) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `quantexame` | `QUANTEXAME` | texto | Quantidade de exames do registro (agregação) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2011-05 a 2015-02 |

## No lake

- **Dataset no lake:** `datasus/siscolo-cc`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): texto: 104.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `siscolo-cc.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- **Colunas que não existem em todo o período:** 1 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/siscolo-cc").glob("**/*.parquet"))
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
datasus-fetcher list siscolo-cc

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync siscolo-cc -o ./data --start 2024-01 --end 2024-12 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset siscolo-cc
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SISCAN/SISCOLO4/Dados`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **INCA — Sistema de Informação do Câncer (SISCAN)**: https://www.gov.br/inca/pt-br/assuntos/gestor-e-profissional-de-saude/siscan
- **Portaria GM/MS nº 3.394/2013** — institui o SISCAN.
- **Pacote de tabulação no FTP**: `TAB_SISCOLO4.zip` (inclui o dicionário de variáveis e arquivos `.cnv`/`.def` para tabulação).
- **PCDaS / Fiocruz**: https://pcdas.icict.fiocruz.br/
- **Wiki Saúde** (DATASUS): https://wiki.saude.gov.br/
