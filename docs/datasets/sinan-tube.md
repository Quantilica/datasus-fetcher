# `sinan-tube` — Tuberculose

O `sinan-tube` contém os microdados das notificações e investigações epidemiológicas de casos de Tuberculose (CID-10 A15 a A19) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha de notificação/investigação de um caso suspeito ou confirmado de tuberculose, preenchida pelas unidades de saúde de todo o país e digitada nos módulos Sinan Windows, Sinan Net e Sinan Online. É a maior base de morbidade de doença infecciosa crônica do Brasil, com dezenas de campos que cobrem o diagnóstico, a forma clínica, a rede de exames bacteriológicos (baciloscopias, culturas e testes moleculares), o esquema terapêutico e o acompanhamento mensal do paciente até o encerramento do caso.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-tube` |
| **Formato dos arquivos** | `.dbc` (comprimido dBASE, descompactável nativamente em Rust) |
| **Particionamento** | `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`) |
| **Periodicidade** | Anual (bases `FINAIS` históricas e anos recentes apenas em `PRELIM`) |
| **Cobertura temporal no FTP** | 2001 a 2025 (conforme `index.json`) |
| **Volume aproximado no FTP** | 25 arquivos (~113,3 MB) |
| **Arquivos preliminares** | Sim (diretório `PRELIM`) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A tuberculose é uma doença de alta relevância para o sistema de vigilância brasileiro, que a monitora por meio da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) e do GT-SINAN. A notificação é compulsória desde a Lei nº 6.259/1975 e o Decreto nº 78.231/1976, e hoje integra a Lista Nacional de Agravos de Notificação Compulsória consolidada na Portaria GM/MS nº 204/2016. O Brasil integra os 30 países prioritários da OMS para tuberculose, e esta base é o instrumento oficial para dimensionar a incidência anual (por 100 mil habitantes, com as estimativas populacionais TCU), a distribuição das formas clínicas, os agravos associados (HIV/AIDS, diabetes, alcoolismo, tabagismo, uso de outras drogas), as populações-chave (privadas de liberdade, população em situação de rua, profissionais de saúde, imigrantes e beneficiários de programas sociais) e os desfechos do tratamento (cura, abandono, óbito, falência e a incorporação da tuberculose drogarresistente).

O evento gerador deste dataset é a **Ficha de Notificação/Investigação de Tuberculose** do SINAN (ficha consolidada v5.0, atual para o regime terapêutico introduzido em 2019). Cada notificação nasce quando o profissional de saúde suspeita de tuberculose (sintomático respiratório com tosse há mais de 15 dias ou caso confirmado por baciloscopia, cultura ou teste molecular rápido) e é completada ao longo da investigação com dados clínicos, laboratoriais, terapêuticos e de acompanhamento mensal até o encerramento (cura, abandono, óbito, transferência ou mudança de diagnóstico). A unidade de análise é o caso notificado (paciente), não o óbito nem a internação, que ficam no SIM e no SIH/SIA.

A série histórica registra três fases do sistema de informação: de **2001 a 2006** os dados provêm do Sinan-Windows (com o campo `MIGRADO_W` distinguindo registros migrados para o Sinan Net); de **2007 em diante**, as bases provêm do Sinan Net e, mais recentemente, do **Sinan Online**, com a mesma base disseminada. O instrumento de coleta foi atualizado de forma relevante ao longo do tempo: a ficha atual incorpora dígitos de acompanhamento mensal das baciloscopias ao longo do tratamento (`BACILOSC_1` a `BACILOSC_6`), controle da situação de encerramento (`SITUA_9_M`, `SITUA_12_M`, `SITUA_ENCE`), registro do teste molecular rápido e de sensibilidade (`TEST_MOLEC`, `TEST_SENSI`), da terapia antirretroviral (`ANT_RETRO`) e das cinco populações-chave (`POP_LIBER`, `POP_RUA`, `POP_SAUDE`, `POP_IMIG`, `BENEF_GOV`).

Aplicações analíticas típicas: incidência anual de casos confirmados por faixa etária e sexo; distribuição das formas pulmonares versus extrapulmonares (`FORMA`, `EXTRAPU1_N`, `EXTRAPU2_N`) e o percentual de casos pulmonares com baciloscopia positiva (`BACILOSC_E`); percentual de casos com HIV testado e positivo (`HIV`); monitoramento do esquema terapêutico (drogas prescritas e regime, com data de início em `DT_INIC_TR`); detecção de tuberculose drogarresistente; e indicadores de acompanhamento como o total de contatos examinados (`NU_COMU_EX`), o percentual de tratamento supervisionado (`TRATSUP_AT`) e e a situação de encerramento (`SITUA_ENCE`), que mede cura, abandono e óbito do programa.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `TUBE` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `TUBE` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `TUBEBR22.dbc` — `TUBE` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `22` é o ano de notificação (2022). Na prática, as consolidações até 2019 estão em `FINAIS` e os anos de 2020 a 2025 estão apenas em `PRELIM` (ex.: `TUBEBR25.dbc`), ainda sujeitos a revisão.
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-tube/<ano>/sinan-tube_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-tube/2025/sinan-tube_preliminar_2025-br@20260507.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções de acesso e conversão (`POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`); em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Schema extraído de `TUBEBR22.dbc` (95 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual, 3 - Surto e outros) |
| `ID_AGRAVO` | String | Código do agravo conforme CID-10 (A15 a A19) |
| `DT_NOTIFIC` | Data (`AAAAMMDD`) | Data de preenchimento da ficha de notificação |
| `NU_ANO` | Inteiro | Ano da notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_MN_RESI` | String (6/7) | Código IBGE do município de residência do caso |
| `DT_DIAG` | Data (`AAAAMMDD`) | Data do diagnóstico do caso |
| `NU_IDADE_N` | Inteiro composto | Idade (o primeiro dígito indica a unidade: dia/mês/ano) |
| `CS_SEXO` | String (1) | Sexo do paciente (M/F/I - Ignorado) |
| `TRATAMENTO` | Inteiro | Tipo de entrada: 1 - Novo, 2 - Recidiva, 3 - Reingresso após abandono, 4 - Não sabe, 5 - Transferência, 6 - Pós-óbito |
| `INSTITUCIO` | Inteiro | Instituição que realizou o diagnóstico/notificação |
| `RAIOX_TORA` | Inteiro | Resultado da radiografia de tórax (positivo/negativo/não realizado) |
| `TESTE_TUBE` | Inteiro | Resultado do teste tuberculínico (PPD) |
| `FORMA` | Inteiro | Forma clínica: 1 - Pulmonar, 2 - Extrapulmonar, 3 - Pulmonar e extrapulmonar |
| `EXTRAPU1_N` / `EXTRAPU2_N` | Inteiro | Localização extrapulmonar primária e secundária (pleural, ganglionar, óssea, neurológica/genitourinária e outras) |
| `BACILOSC_E` / `BACILOS_E2` | Inteiro | Baciloscopias de escarro no diagnóstico: 1 - Positiva, 2 - Negativa, 3 - Não realizada, 4 - Não se aplica |
| `CULTURA_ES` / `CULTURA_OU` | Inteiro | Cultura de escarro e de outro material (positiva/negativa, sensibilidade à ação de antibacilares) |
| `HIV` | Inteiro | Situação de HIV (1 - Positivo, 2 - Negativo, 3 - Em andamento, 4 - Não realizado) |
| `AGRAV*` | Inteiro | Agravos comórbidos e fatores de risco: `AGRAVDIABE` (diabetes), `AGRAVALCOO` (alcoolismo), `AGRAVDROGA` (outras drogas), `AGRAVTABAC` (tabagismo), `AGRAVAIDS` (AIDS), `AGRAVDOENC` (outras doenças), `AGRAVOUTRA` (outros) |
| `DT_INIC_TR` | Data (`AAAAMMDD`) | Data de início do esquema terapêutico |
| `RIFAMPICIN`/`ISONIAZIDA`/`ETAMBUTOL`/`ESTREPTOMI`/`PIRAZINAMI`/`ETIONAMIDA` | Inteiro | Drogas preconizadas no esquema terapêutico (1 - Usou, 2 - Não usou) |
| `TEST_MOLEC` | Inteiro | Teste Molecular Rápido TB (TMR-TB): 1 - Detectável sensível à rifampicina, 2 - Detectável resistente à rifampicina, 3 - Não detectável, 4 - Inconclusivo, 5 - Não realizado |
| `TEST_SENSI` | Inteiro | Teste de sensibilidade (resistente a antibacilares, como isoniazida ou rifampicina) |
| `POP_LIBER`/`POP_RUA`/`POP_SAUDE`/`POP_IMIG`/`BENEF_GOV` | Inteiro | Populações-chave: 1 - Sim, 2 - Não, 3 - Ignorado (privada de liberdade, em situação de rua, profissional de saúde, imigrante, beneficiária de programa social) |
| `BACILOSC_1` a `BACILOSC_6` | Inteiro | Baciloscopias de escarro de acompanhamento (meses 1 a 6): positividade/negatividade parcial na série |
| `SITUA_9_M` / `SITUA_12_M` / `SITUA_ENCE` | Inteiro | Situação de encerramento no 9º mês, no 12º mês e ao fim do esquema: 1 - Cura, 2 - Abandono, 3 - Óbito por TB, 4 - Óbito por outras causas, 5 - Transferência, 6 - Mudança de diagnóstico, 7 - TB-DR, 8 - Mudança de Esquema, 9 - Falência, 10 - Abandono Primário |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `NU_COMU_EX` | Inteiro | Total de contatos examinados na investigação e acompanhamento |
| `TRANSF`/`UF_TRANSF`/`MUN_TRANSF` | Inteiro / String | Registro de transferência de caso entre municípios (1 - Sim) e destino (UF, município) |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: `ID_MUNICIP` e `ID_MN_RESI` (IBGE: 6 ou 7 dígitos — manter como `String` com `zfill`), `ID_OCUPA_N` (CBO de 6 dígitos) e códigos de classificação (`FORMA`, `TRATAMENTO`, `SITUA_ENCE`) devem permanecer texto/código, nunca convertidos a inteiro sem mapeamento prévio.
- **Datas e competências**: `DT_NOTIFIC`, `DT_DIAG`, `DT_INIC_TR`, `DT_MUDANCA`, `DT_ENCERRA` e datas de acompanhamento vêm como `AAAAMMDD` no DBF e são convertidas para `pl.Date` pelo saneamento canônico (`wrangle_datasus`).
- **Valores ausentes e sentinelas**: no DBF, códigos ignorados (`9`, `99`, `999999`), datas vazias/espaços em branco e o literal `00000000` são convertidos para nulo por `SENTINEL_NULLS`; registros com marcador lógico de exclusão dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: as bases até 2019 estão em `FINAIS` e os anos 2020 a 2025 apenas em `PRELIM` (sujeitos a revisão); o leiaute da ficha foi atualizado ao longo do tempo (inclusão de `POP_*`, `TEST_MOLEC`, `TEST_SENSI`, `ANT_RETRO`), o que exige tratamento granular por ano e, em alguns registros, valores nulos em campos novos; `NU_IDADE_N` requer decomposição do primeiro dígito (unidade: dia/mês/ano) antes de comparações; os campos de identificação de transferência (`TRANSF`, `UF_TRANSF`, `MUN_TRANSF`, `MIGRADO_W`) indicam movimentação de casos entre unidades/territórios e persistem no DBF para acesso a detalhes de investigação.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-tube
quantilica datasus list sinan-tube

# 2. Baixar microdados de sinan-tube com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-tube -o ./data --start 2001 --end 2025 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-tube -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-tube -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-tube/2022/sinan-tube_2022-br@20240710.dbc", clean=True)

# Casos pulmonares com baciloscopia de diagnóstico positiva (TB pulmonar bacilífera)
pulmonar_bac_pos = qdf.filter(
    (pl.col("forma") == 1) & (pl.col("bacilosc_e") == 1)
)
print(pulmonar_bac_pos.group_by("nu_ano").len().sort("nu_ano"))

# Situação de encerramento: cura (1), abandono (2), óbito por TB (3) e outras causas (4)
encerr = (
    pulmonar_bac_pos.group_by(["situa_ence", "nu_ano"])
    .len()
    .sort(["nu_ano", "situa_ence"])
)
print(encerr)
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Tuberculose (ficha e dicionário de dados v5.0)**: https://portalsinan.saude.gov.br (documentos em `images/documentos/Agravos/Tuberculose`)
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de tuberculose e Manual de Recomendações para o Controle da Tuberculose no Brasil
