---
dataset:
  id: siscolo-hc
  fonte: datasus
  titulo: Histopatológico de Colo de Útero
  resumo: 'Histopatológico de Colo de Útero do DATASUS: um laudo histopatológico do colo do útero.'
  orgao: Ministério da Saúde — Instituto Nacional de Câncer (INCA) e DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SISCAN/SISCOLO4/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: mensal (um arquivo por UF e competência)
  cobertura:
    inicio: 2006-01
    fim: 2015-10
  unidade: um laudo histopatológico do colo do útero
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
    colunas: 117
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Histopatológico de Colo de Útero (`siscolo-hc`)

## Resumo

Microdados do SISCOLO (INCA/DATASUS) com os laudos histopatológicos do colo do útero realizados no SUS entre 2006 e 2015, por UF e mês. Cada linha é um laudo histopatológico.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Não
- **Documentação oficial no FTP:** Não aplicável (o catálogo `meta.docs` não define diretório de documentação para este sistema)
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SISCAN/SISCOLO4/Auxiliar`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SISCAN/SISCOLO4/Dados` | `HC` | `uf_year2_month_pattern` — UF (2 letras) + ano (2 dígitos) + mês (2 dígitos) | `dbc` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: `HCSP1001.dbc` — `HC` (histopatológico) + `SP` (UF) + `10` (ano 2010) + `01` (mês).
- **No armazenamento local do `datasus-fetcher`**: `data/siscolo-hc/<AAAAMM>/siscolo-hc_<AAAAMM>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/siscolo-hc/202401/siscolo-hc_202401-sp@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**:
  - Documentação: nenhum arquivo catalogado em `documentation/siscolo.json` (não há `meta.docs` para `siscolo`); o dicionário de variáveis está dentro do pacote de tabulação listado abaixo.
  - Tabelas auxiliares (`datasus-metadata/metadata/auxiliary/siscolo.json`):
    - `/dissemin/publicos/SISCAN/SISCOLO4/Auxiliar/TAB_SISCOLO4.zip` (1.7 MB)

## Conteúdo

O SISCOLO (Sistema de Informações do Câncer do Colo do Útero) e o SISMAMA (Sistema de Informação do Câncer de Mama) foram criados pelo Instituto Nacional de Câncer (INCA) e pelo DATASUS para apoiar o monitoramento e a gestão dos programas nacionais de controle dos cânceres do colo do útero e de mama, registrando os exames de rastreamento e de confirmação diagnóstica realizados no SUS. A partir de 2013 ambos foram substituídos gradualmente pelo Sistema de Informação do Câncer (SISCAN), implantado pela Portaria GM/MS nº 3.394/2013 em plataforma web; no FTP, os arquivos do SISCOLO e do SISMAMA ficam sob `SISCAN/` e cobrem apenas o período em que os sistemas legados estavam em uso. Cobertura no FTP: janeiro/2006 a outubro/2015, 27 UF, mensal.

Este dataset reúne os laudos histopatológicos do colo do útero, que confirmam o diagnóstico após citologia alterada ou colposcopia; a unidade de análise é o laudo (peça ou biópsia), não a mulher. O instrumento é a requisição/laudo histopatológico preenchido pelos laboratórios no SISCOLO.

Indicadores: proporção de lesões intraepiteliais de alto grau (NIC II/III) e de carcinoma entre as biópsias, tempo entre citologia alterada e confirmação (quando houver vinculação) e seguimento de mulheres com exame alterado.

Complementa `siscolo-cc` na confirmação diagnóstica, sendo o segundo passo do fluxo de rastreamento.

### Cobertura observada

- Índice do FTP (2026-10): 2858 arquivos, de 2006-01 a 2015-10, 27 UF(s) com arquivos, última atualização em 2022-08-17.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2006-02 a 2015-08), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Nomes verificados contra o arquivo real `HCSP1505.dbc` (115 colunas; resultado do exame histopatológico do colo do útero). Muitos campos são contadores agregados (`String` de 8 caracteres).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `CO_US` / `CO_US_UF` / `CO_US_IBGE` | String | Unidade solicitante: código, UF e município (IBGE, 7). |
| `CO_CNES` | String (CNES, 7) | CNES do estabelecimento. |
| `REGUS` / `REGRESID` / `REGLAB` | String | Indicadores de região da unidade, da residência e do laboratório. |
| `CO_PAC_UF` / `CO_PAC_IBG` | String | UF e município (IBGE, 7) de residência da paciente. |
| `ANO_COMP` / `DT_ID_COMP` | String | Ano e competência (`AAAAMM`) do registro. |
| `CO_FX_ETAR` | String | Faixa etária da paciente. |
| `DINTCOLETA` / `DINTRESULT` / `DINTTEMPEX` | String | Intervalos (categorizados) entre coleta, resultado e tempo de exame. |
| `DT_PAC_NAS` | String `DD/MM/AAAA` | Data de nascimento da paciente. |
| `CO_PAC_IDA` | String (3) | Idade da paciente. |
| `CO_PAC_ESC` / `CO_PAC_RAC` | String | Escolaridade e raça/cor da paciente. |
| `CLABIBGE` / `CLABUF` / `CLABCID` | String | Município (IBGE, 7), UF e nome da cidade do laboratório. |
| `CO_CIT_ESC` / `CO_CIT_GLA` / `CO_CIT_IND` / `O_CIT_ESCA` / `O_CIT_GLAN` / `CO_COLP` / `CO_RES_TIP` / `CO_RES_LOC` | String | Citologia prévia (escamosa, glandular, indeterminada), colposcopia e tipo/local do resultado. |
| `CO_BEN_CER` / `CO_BEN_ALT` / `CO_NEO_NIC` / `CO_NEO_ADE` / `CO_DIF_GRA` | String | Diagnóstico histopatológico: alterações benignas, NIC, adenocarcinoma e grau de diferenciação. |
| `CO_EXTEN_P` / `CO_EXTEN_V` / `O_EXTEN_PE` / `O_EXTEN_PA` / `CO_EXTEN_C` / `O_EXTEN_VA` / `CO_MARG`` | String | Extensão da lesão e margens. |
| `CO_RES_FRA` / `CO_RES_TAM` / `O_RES_TAM2` / `CO_RES_MAR` | String | Fragmentos, tamanhos da peça e margens cirúrgicas. |
| `DT_HIS_EXA` / `DT_HIS_REC` | String `DD/MM/AAAA` | Datas do exame e do recebimento do histopatológico. |
| `CO_MAT_INS` / `CO_CTRL_FR` / `CO_CTRL_BL` | String | Material insatisfatório e controles de fragmentos e blocos. |
| `QTDEXA` | String (8) | Quantidade de exames do registro. |
| `ESCAMOSA` / `PNEOPLA` / `GPNNEOP` / `GNALTGRAU` / `INDPNAONEO` / `CITINDALGR` / `ESCLIPBX` / `ESCINALT` / `ESCIEMCINV` / `ESCCARINVA` / `ADENOINSUT` / `ADENCARCIN` / `CIT_OUTNEO`` | String (8) | Contadores de resultados citológicos (escamosos, glandulares, neoplasias). |
| `CCOLDEFAUL` / `CCOLNORMAL` / `CCOLANORMA` / `CCOLINSATI` / `CO_COLP_PO` / `O_COLP_POS` / `CO_COLP_BI` / `CO_COLP_CU` / `CO_COLP_EX` / `CO_COLP_RE` / `O_COLP_BIO`` | String (8) | Contadores de colposcopia (normal, anormal, insatisfatória, biópsia, curetagem etc.). |
| `CRESBIOPSI` / `CRESCONIZA` / `CRESHISSIM` / `CRESPANHIS` / `CRESOUTROS` / `CRESECTO` / `CRESENDO` / `CRESJUNC`` | String (8) | Contadores por tipo de procedimento/resultado (biópsia, conização, histerectomia etc.). |
| `CO_BEN_MET` / `CO_BEN_POL` / `CBENCERVI` / `CBENALTER` | String (8) | Contadores de alterações benignas (metaplasia, pólipo, cervicite e outras). |
| `NICDLEVE` / `NICDMODE` / `NICDACENT` / `NICCARCMIN` / `NICEPIINVA` / `NICIMPAVAL` / `NICVERRUCO` / `NICNAOCERA` / `NEOINSUTU` / `NEOMUCINO` / `NEOVILOGL` / `DS_NEO_OUT` | String (8) | Contadores de NIC e neoplasias por tipo. |
| `CDIFGRAU` / `CDIFMODDIF` / `CDIFPOUDIF` / `CDIFINDFER` / `CDIEXAMINS` / `C_EXT_VASC` / `C_EXT_PERI` / `C_EXT_PARA` / `C_EXT_CORP` / `C_EXT_VAGI` / `CO_EXTEN_L` / `O_EXTEN_LI` / `CMARLIVRE` / `CMARCOMPRO` / `CMARIMPAVA`` | String (8) | Contadores de diferenciação, extensão (vascular, perineural, paramétrio, corpo, vagina) e margens. |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_us` | `CO_US` | texto | Código da unidade de saúde solicitante do exame (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_us_uf` | `CO_US_UF` | texto | UF da unidade de saúde solicitante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_us_ibge` | `CO_US_IBGE` | texto | Município da unidade de saúde solicitante (código IBGE) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `regus` | `REGUS` | texto | Região de saúde da unidade solicitante (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_ibg` | `CO_PAC_IBG` | texto | Município de residência da paciente (código IBGE) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_uf` | `CO_PAC_UF` | texto | UF de residência da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_pac_esc` | `CO_PAC_ESC` | texto | Escolaridade da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_pac_nas` | `DT_PAC_NAS` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `co_pac_ida` | `CO_PAC_IDA` | texto | Idade da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `regresid` | `REGRESID` | texto | Região de saúde de residência da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_cnes` | `CO_CNES` | texto | Código CNES do estabelecimento responsável pelo laudo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `clabibge` | `CLABIBGE` | texto | Município do laboratório (código IBGE) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `clabuf` | `CLABUF` | texto | UF do laboratório (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `clabcid` | `CLABCID` | texto | Campo do laudo do SISCOLO (`CLABCID`); sem dicionário oficial no FTP | — | todos |
| `reglab` | `REGLAB` | texto | Região de saúde do laboratório (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `dt_id_comp` | `DT_ID_COMP` | texto | Competência da data do laudo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ano_comp` | `ANO_COMP` | texto | Ano da competência do laudo (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_fx_etar` | `CO_FX_ETAR` | texto | Faixa etária da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `co_cit_esc` | `CO_CIT_ESC` | texto | Campo do laudo do SISCOLO (`CO_CIT_ESC`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_cit_gla` | `CO_CIT_GLA` | texto | Campo do laudo do SISCOLO (`CO_CIT_GLA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_cit_ind` | `CO_CIT_IND` | texto | Campo do laudo do SISCOLO (`CO_CIT_IND`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `o_cit_esca` | `O_CIT_ESCA` | texto | Campo do laudo do SISCOLO (`O_CIT_ESCA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `o_cit_glan` | `O_CIT_GLAN` | texto | Campo do laudo do SISCOLO (`O_CIT_GLAN`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_colp` | `CO_COLP` | texto | Campo do laudo do SISCOLO (`CO_COLP`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_res_tip` | `CO_RES_TIP` | texto | Campo do laudo do SISCOLO (`CO_RES_TIP`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_res_loc` | `CO_RES_LOC` | texto | Campo do laudo do SISCOLO (`CO_RES_LOC`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_ben_cer` | `CO_BEN_CER` | texto | Alteração celular benigna ou resultado benigno do laudo (SISCOLO); campo `CO_BEN_CER` | — | todos |
| `co_ben_alt` | `CO_BEN_ALT` | texto | Alteração celular benigna ou resultado benigno do laudo (SISCOLO); campo `CO_BEN_ALT` | — | todos |
| `co_neo_nic` | `CO_NEO_NIC` | texto | Campo do laudo do SISCOLO (`CO_NEO_NIC`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_neo_ade` | `CO_NEO_ADE` | texto | Campo do laudo do SISCOLO (`CO_NEO_ADE`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_dif_gra` | `CO_DIF_GRA` | texto | Campo do laudo do SISCOLO (`CO_DIF_GRA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_exten_p` | `CO_EXTEN_P` | texto | Campo do laudo do SISCOLO (`CO_EXTEN_P`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_exten_v` | `CO_EXTEN_V` | texto | Campo do laudo do SISCOLO (`CO_EXTEN_V`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `o_exten_pe` | `O_EXTEN_PE` | texto | Campo do laudo do SISCOLO (`O_EXTEN_PE`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `o_exten_pa` | `O_EXTEN_PA` | texto | Campo do laudo do SISCOLO (`O_EXTEN_PA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_exten_c` | `CO_EXTEN_C` | texto | Campo do laudo do SISCOLO (`CO_EXTEN_C`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `o_exten_va` | `O_EXTEN_VA` | texto | Campo do laudo do SISCOLO (`O_EXTEN_VA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_marg` | `CO_MARG` | texto | Campo do laudo do SISCOLO (`CO_MARG`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_res_fra` | `CO_RES_FRA` | texto | Campo do laudo do SISCOLO (`CO_RES_FRA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_res_tam` | `CO_RES_TAM` | texto | Campo do laudo do SISCOLO (`CO_RES_TAM`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `o_res_tam2` | `O_RES_TAM2` | texto | Campo do laudo do SISCOLO (`O_RES_TAM2`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_res_mar` | `CO_RES_MAR` | texto | Campo do laudo do SISCOLO (`CO_RES_MAR`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `dt_his_exa` | `DT_HIS_EXA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `dt_his_rec` | `DT_HIS_REC` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `co_mat_ins` | `CO_MAT_INS` | texto | Campo do laudo do SISCOLO (`CO_MAT_INS`); sem dicionário oficial no FTP | — | todos |
| `co_ctrl_fr` | `CO_CTRL_FR` | texto | Campo do laudo do SISCOLO (`CO_CTRL_FR`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_ctrl_bl` | `CO_CTRL_BL` | texto | Campo do laudo do SISCOLO (`CO_CTRL_BL`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `qtdexa` | `QTDEXA` | texto | Quantidade de exames do registro (agregação) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `escamosa` | `ESCAMOSA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `pneopla` | `PNEOPLA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `gpnneop` | `GPNNEOP` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `gnaltgrau` | `GNALTGRAU` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `indpnaoneo` | `INDPNAONEO` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `citindalgr` | `CITINDALGR` | texto | Campo do laudo do SISCOLO (`CITINDALGR`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `esclipbx` | `ESCLIPBX` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `escinalt` | `ESCINALT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `esciemcinv` | `ESCIEMCINV` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `esccarinva` | `ESCCARINVA` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `adenoinsut` | `ADENOINSUT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `adencarcin` | `ADENCARCIN` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `cit_outneo` | `CIT_OUTNEO` | texto | Campo do laudo do SISCOLO (`CIT_OUTNEO`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `ccoldefaul` | `CCOLDEFAUL` | texto | Campo do laudo do SISCOLO (`CCOLDEFAUL`); sem dicionário oficial no FTP | — | todos |
| `ccolnormal` | `CCOLNORMAL` | texto | Campo do laudo do SISCOLO (`CCOLNORMAL`); sem dicionário oficial no FTP | — | todos |
| `ccolanorma` | `CCOLANORMA` | texto | Campo do laudo do SISCOLO (`CCOLANORMA`); sem dicionário oficial no FTP | — | todos |
| `ccolinsati` | `CCOLINSATI` | texto | Campo do laudo do SISCOLO (`CCOLINSATI`); sem dicionário oficial no FTP | — | todos |
| `co_colp_po` | `CO_COLP_PO` | texto | Campo do laudo do SISCOLO (`CO_COLP_PO`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `o_colp_pos` | `O_COLP_POS` | texto | Campo do laudo do SISCOLO (`O_COLP_POS`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_colp_bi` | `CO_COLP_BI` | texto | Campo do laudo do SISCOLO (`CO_COLP_BI`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_colp_cu` | `CO_COLP_CU` | texto | Campo do laudo do SISCOLO (`CO_COLP_CU`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_colp_ex` | `CO_COLP_EX` | texto | Campo do laudo do SISCOLO (`CO_COLP_EX`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_colp_re` | `CO_COLP_RE` | texto | Campo do laudo do SISCOLO (`CO_COLP_RE`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `o_colp_bio` | `O_COLP_BIO` | texto | Campo do laudo do SISCOLO (`O_COLP_BIO`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cresbiopsi` | `CRESBIOPSI` | texto | Campo do laudo do SISCOLO (`CRESBIOPSI`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cresconiza` | `CRESCONIZA` | texto | Campo do laudo do SISCOLO (`CRESCONIZA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `creshissim` | `CRESHISSIM` | texto | Campo do laudo do SISCOLO (`CRESHISSIM`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `crespanhis` | `CRESPANHIS` | texto | Campo do laudo do SISCOLO (`CRESPANHIS`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cresoutros` | `CRESOUTROS` | texto | Campo do laudo do SISCOLO (`CRESOUTROS`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cresecto` | `CRESECTO` | texto | Campo do laudo do SISCOLO (`CRESECTO`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cresendo` | `CRESENDO` | texto | Campo do laudo do SISCOLO (`CRESENDO`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cresjunc` | `CRESJUNC` | texto | Campo do laudo do SISCOLO (`CRESJUNC`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_ben_met` | `CO_BEN_MET` | texto | Alteração celular benigna ou resultado benigno do laudo (SISCOLO); campo `CO_BEN_MET` | — | todos |
| `co_ben_pol` | `CO_BEN_POL` | texto | Alteração celular benigna ou resultado benigno do laudo (SISCOLO); campo `CO_BEN_POL` | — | todos |
| `cbencervi` | `CBENCERVI` | texto | Alteração celular benigna ou resultado benigno do laudo (SISCOLO); campo `CBENCERVI` | — | todos |
| `cbenalter` | `CBENALTER` | texto | Alteração celular benigna ou resultado benigno do laudo (SISCOLO); campo `CBENALTER` | — | todos |
| `nicdleve` | `NICDLEVE` | texto | Campo do laudo do SISCOLO (`NICDLEVE`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `nicdmode` | `NICDMODE` | texto | Campo do laudo do SISCOLO (`NICDMODE`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `nicdacent` | `NICDACENT` | texto | Campo do laudo do SISCOLO (`NICDACENT`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `niccarcmin` | `NICCARCMIN` | texto | Campo do laudo do SISCOLO (`NICCARCMIN`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `nicepiinva` | `NICEPIINVA` | texto | Campo do laudo do SISCOLO (`NICEPIINVA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `nicimpaval` | `NICIMPAVAL` | texto | Campo do laudo do SISCOLO (`NICIMPAVAL`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `nicverruco` | `NICVERRUCO` | texto | Campo do laudo do SISCOLO (`NICVERRUCO`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `nicnaocera` | `NICNAOCERA` | texto | Campo do laudo do SISCOLO (`NICNAOCERA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `neoinsutu` | `NEOINSUTU` | texto | Campo do laudo do SISCOLO (`NEOINSUTU`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `neomucino` | `NEOMUCINO` | texto | Campo do laudo do SISCOLO (`NEOMUCINO`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `neovilogl` | `NEOVILOGL` | texto | Campo do laudo do SISCOLO (`NEOVILOGL`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `ds_neo_out` | `DS_NEO_OUT` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `cdifgrau` | `CDIFGRAU` | texto | Campo do laudo do SISCOLO (`CDIFGRAU`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cdifmoddif` | `CDIFMODDIF` | texto | Campo do laudo do SISCOLO (`CDIFMODDIF`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cdifpoudif` | `CDIFPOUDIF` | texto | Campo do laudo do SISCOLO (`CDIFPOUDIF`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cdifindfer` | `CDIFINDFER` | texto | Campo do laudo do SISCOLO (`CDIFINDFER`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cdiexamins` | `CDIEXAMINS` | texto | Campo do laudo do SISCOLO (`CDIEXAMINS`); sem dicionário oficial no FTP | — | todos |
| `c_ext_vasc` | `C_EXT_VASC` | texto | Campo do laudo do SISCOLO (`C_EXT_VASC`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `c_ext_peri` | `C_EXT_PERI` | texto | Campo do laudo do SISCOLO (`C_EXT_PERI`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `c_ext_para` | `C_EXT_PARA` | texto | Campo do laudo do SISCOLO (`C_EXT_PARA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `c_ext_corp` | `C_EXT_CORP` | texto | Campo do laudo do SISCOLO (`C_EXT_CORP`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `c_ext_vagi` | `C_EXT_VAGI` | texto | Campo do laudo do SISCOLO (`C_EXT_VAGI`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `co_exten_l` | `CO_EXTEN_L` | texto | Campo do laudo do SISCOLO (`CO_EXTEN_L`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `o_exten_li` | `O_EXTEN_LI` | texto | Campo do laudo do SISCOLO (`O_EXTEN_LI`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cmarlivre` | `CMARLIVRE` | texto | Campo do laudo do SISCOLO (`CMARLIVRE`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cmarcompro` | `CMARCOMPRO` | texto | Campo do laudo do SISCOLO (`CMARCOMPRO`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `cmarimpava` | `CMARIMPAVA` | texto | Campo do laudo do SISCOLO (`CMARIMPAVA`) sobre achados do exame (atipias, células, neoplasias, extensão, margens ou resultados); sem dicionário oficial no FTP | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |
| `dintcoleta` | `DINTCOLETA` | texto | Dias entre a coleta e o recebimento da amostra (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2009-08 a 2015-08 |
| `dintresult` | `DINTRESULT` | texto | Dias entre o recebimento e o resultado (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2009-08 a 2015-08 |
| `dinttempex` | `DINTTEMPEX` | texto | Dias entre a coleta e o resultado (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2009-08 a 2015-08 |
| `co_pac_rac` | `CO_PAC_RAC` | texto | Raça/cor da paciente (inferido do nome do campo; sem definição na documentação oficial consultada) | — | 2011-11 a 2015-08 |

## No lake

- **Dataset no lake:** `datasus/siscolo-hc`, particionado por `ano`, `mes` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): texto: 117.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Esquema de referência:** `siscolo-hc.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- **Colunas que não existem em todo o período:** 4 colunas aparecem só em parte das amostras (a coluna `Período` do dicionário dá o intervalo amostrado); consultas sobre vários períodos devem tolerar colunas ausentes (ex.: `pl.scan_parquet(..., missing_columns="insert")` ou `diagonal_relaxed`). Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas linhas há por período e por UF do arquivo de origem? (confere a cobertura do lake antes de qualquer análise)

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/siscolo-hc").glob("**/*.parquet"))
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
datasus-fetcher list siscolo-hc

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync siscolo-hc -o ./data --start 2024-01 --end 2024-12 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset siscolo-hc
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
