---
dataset:
  id: sinan-varc
  fonte: datasus
  titulo: Varicela
  resumo: O sinan-varc contém os microdados das notificações de casos suspeitos/descartados de Varicela (CID-10 B01) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde.
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de varicela
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 43
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Varicela (`sinan-varc`)

## Resumo

O `sinan-varc` contém os microdados das notificações de casos suspeitos/descartados de Varicela (CID-10 B01) registrados no Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a ficha individual de notificação de um caso, em leiaute compacto da ficha básica de notificação (42 colunas no arquivo verificado), cobrindo identificação do caso, pessoa, endereço, classificação final, critério, autoctonia e trabalho. É a base de morbidade de varicela no país, publicada no FTP exclusivamente em consolidações preliminares (não há bases `FINAIS` para o agravo) — leiaute e política de notificação refletem que a varicela é notificada de forma universal apenas em situações de surto e/ou óbito.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2007 a 2026 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 20 arquivos (~35,9 MB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim — todos os arquivos estão em `PRELIM`; `meta.py` também consulta `FINAIS`, que hoje não contém arquivos do agravo
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `VARC` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `VARC` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `VARCBR07.dbc` — `VARC` é o prefixo do agravo, `BR` indica a consolidação nacional de todo o país e `07` é o ano de notificação (2007). Não há arquivos em `FINAIS` para o agravo: toda a série (2007 a 2026) está em `PRELIM` (ex.: `VARCBR26.dbc`, atualização de 01/10/2026).
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-varc/<ano>/sinan-varc_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-varc/2026/sinan-varc_preliminar_2026-br@20261001.dbc`; arquivos preliminares recebem o sufixo `-preliminar` no nome do dataset.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` (definições/tabulações do Sinan Net e Online) e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais).

## Conteúdo

A varicela (catapora) é agravo de notificação compulsória em situações de surto e/ou óbito desde o início da vigilância nacional brasileira (Lei nº 6.259/1975 e Decreto nº 78.231/1976), e seu acompanhamento analítico é responsabilidade da Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) em conjunto com o GT-SINAN e o Programa Nacional de Imunizações — o registro de casos é fundamental para a avaliação da vacinação programática do calendário do PNI e a gestão das formas graves em imunossuprimidos. A base alimenta a vigilância do excesso de morbidade sazonal (pico no outono/inverno), a investigação de formas graves e de surtos em escolas e demais locais de convivência.

O evento gerador deste dataset é a **Ficha de Notificação de Varicela** do SINAN (ficha básica, no padrão gvIMS do SINAN). A notificação é individual, com o campo `ID_AGRAVO` marcando o CID-10 B01, data dos primeiros sintomas e demografia do caso — não há blocos laboratoriais complexos nem ficha de investigação epidemiológica dedicada como nas fichas de agravos de notificação universal. A unidade de análise é o caso notificado, e o encerramento ocorre com classificação final (confirmado/descartado) e critério de confirmação (laboratorial ou clínico-epidemiológico, mais comum em surtos).

A série histórica inicia em **2007** (implantação nacional do Sinan Net): não há bases anteriores no FTP para esse agravo. A base é publicada e revisada no ciclo de atualização corrente — todas as consolidações estão em `PRELIM`. Mudanças recentes de instrumento refletem a institucionalização da notificação de surtos e óbitos (com alinhamento ao Guia de Vigilância e às notas técnicas da vigilância de doenças inume-preventíveis da CGVDI/DPNI sobre o manejo da varicela), mantendo o leiaute compacto da ficha básica e facilitando a comparação ao longo de toda a série.

Aplicações analíticas típicas: curvas epidêmicas por semana de início dos sintomas (`SEM_PRI`); distribuição por faixa etária e sexo; surtos detectados por município/UF (`ID_MUNICIP`, `SG_UF_NOT`); letalidade em casos notificados com `DT_OBITO` (raro, mas crítico); casos associados à fonte de infecção fora do município de residência (`COUFINF`/`COMUNINF`); e, como não há bloco de antecedentes vacinais na ficha, estudos de efetividade da vacina consomem esta base em conjunto com os registros do PNI (SI-PNI).

### Cobertura observada

- Índice do FTP (2026-10): 20 arquivos, de 2007 a 2026, 1 UF(s) com arquivos, última atualização em 2026-10-01.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2007 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `VARCBR07.dbc` (42 colunas depois de remover `_deleted`) — leiaule compacto, baseado na ficha básica de notificação do SINAN.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual, 3 - Surto e outros) |
| `ID_AGRAVO` | String | Código do agravo conforme CID-10 (B01) |
| `DT_NOTIFIC` | Data (`AAAAMMDD`) | Data de preenchimento da ficha de notificação |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano da notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_REGIONA` | String (7) | Código do município de referência regional |
| `ID_UNIDADE` | String (7) | Código CNES da unidade de saúde notificadora |
| `DT_SIN_PRI` / `SEM_PRI` | Data / Inteiro | Data e semana epidemiológica de início dos sintomas |
| `ANO_NASC` | Inteiro | Ano de nascimento do paciente |
| `NU_IDADE_N` | Inteiro composto | Idade (o primeiro dígito indica a unidade: dia/mês/ano) |
| `CS_SEXO` / `CS_GESTANT`/`CS_RACA`/`CS_ESCOL_N` | String/Inteiro | Sexo, gestação (feminino), raça/cor e escolaridade |
| `SG_UF` / `ID_MN_RESI` / `ID_RG_RESI` / `ID_PAIS` | String | UF, município, regional e país de residência |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação do caso |
| `ID_OCUPA_N` | String (6) | Código CBO da ocupação do paciente |
| `CLASSI_FIN` | Inteiro | Classificação final do caso (confirmado/descartado) |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte (laboratorial, clínico-epidemiológico ou em investigação) |
| `TPAUTOCTO` | Inteiro | O caso é autóctone do município de residência (1 - Sim, 2 - Não, 3 - Indeterminado) |
| `COUFINF`/`COPAISINF`/`COMUNINF` | String | UF, país e município prováveis da fonte de infecção |
| `DOENCA_TRA` | Inteiro | Doença relacionada ao trabalho (1 - Sim, 2 - Não, 9 - Ignorado) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` / `DT_ENCERRA` / `DT_DIGITA` | Data (`AAAAMMDD`) | Data do óbito, de encerramento do caso e de digitação |
| `MIGRADO_W` / `TP_SISTEMA` / `TPUNINOT` | Inteiro | Indicadores do sistema de origem (registro migrado do Sinan-Windows) e da unidade notificadora |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo. Tabela de agravos do sistema com códigos (classificação internacional de doenças –CID 10) e nomes dos agravos classificados como notificação compulsória ( nacional, estadual ou municipal) e as síndromes ( febre hemorragia aguda;respiratória aguda; diarréia aguda; sanguinolenta; | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno). ds_semana_notifi cacao | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação. co_municipio_not ificacao | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora. co_unidade_notifi cacao | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico. dt_diagnostico_si ntoma | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno). ds_semana_sinto ma | — | todos |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência. co_municipio_res idencia | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil). co_pais_residenc ia | — | todos |
| `nduplic_n` | `NDUPLIC_N` | texto | Não Listar/ Não Contar. 0 ou branco – Não identificado 1 – Não é duplicidade (não listar) 2 – Duplicidade (não contar) | — | todos |
| `in_vincula` | `IN_VINCULA` | texto | Vinculação. 0 ou branco – Não Vinculado 1 – Vinculado | — | todos |
| `dt_invest` | `DT_INVEST` | data | Data da investigação. data de início da investigação do caso | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação. Ocupação do indivíduo que sofreu o agravo | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação final. tp_classificacao_f inal | — | todos |
| `criterio` | `CRITERIO` | texto | Critério confirmação. tp_criterio_confir macao | — | todos |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é. Tp_autoctone_re | 1 – Sim | todos |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o paciente foi provavelmente infectado | — | todos |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente infectado | — | todos |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). co_municipio_inf eccao | — | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho. st_doenca_trabal ho | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso. tp_evolucao_cas o | — | todos |
| `dt_obito` | `DT_OBITO` | data | Data de óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | encerramento | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `cs_flxret` | `CS_FLXRET` | texto | Fluxo de retorno. Identifica se o registro está habilitado ou foi enviado pelo fluxo de retorno para o município de residência | 0 - Não 1 - habilitado para envio. 2 - enviado | todos |
| `flxrecebi` | `FLXRECEBI` | texto | Recebida por fluxo de retorno (campo interno). Colocar a estrutura do nº atribuído pelo sistema | — | todos |
| `migrado_w` | `MIGRADO_W` | texto | Identifica migração (campo interno). Identifica se o registro é oriundo da rotina de migração da base Windows | 1- migrado do Sinan Windows | todos |
| `tp_sistema` | `TP_SISTEMA` | texto | Sistema de origem do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tpuninot` | `TPUNINOT` | texto | Tipo da unidade notificadora (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-varc`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 6, inteiro: 1, texto: 36.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-varc.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- toda a série está em `PRELIM` (sem consolidações `FINAIS` publicadas), com risco maior de revisão retroativa dos dados; o leiaute é o da ficha básica de notificação (sem bloco laboratorial e sem registro detalhado de doses da vacina), o que limita estudos de efetividade vacinal a partir desta base isolada; e, por se tratar de notificação compulsória restrita a surtos e/ou óbitos, a base é sensível ao comportamento de notificação de surtos — não representa a incidência endêmica da doença. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-varc/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-varc
quantilica datasus list sinan-varc

# 2. Baixar microdados de sinan-varc com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-varc -o ./data --start 2007 --end 2026 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-varc -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-varc -o ./data/raw --parquet-dir ./data/parquet --start 2010
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc(
    "data/sinan-varc/2007/sinan-varc_preliminar_2007-br@20240522.dbc", clean=True
)

# Distribuição das notificações por ano de notificação e sexo
print(qdf.group_by(["nu_ano", "cs_sexo"]).len().sort(["nu_ano", "cs_sexo"]))

# Casos com evolução fatal
obitos = qdf.filter(pl.col("evolucao") == 2)
print(obitos.select(["nu_ano", "sg_uf_not", "dt_obito"]))
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Varicela (ficha de notificação)**: https://portalsinan.saude.gov.br
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de varicela/doenças exantemáticas; Notas técnicas da CGVDI/DPNI sobre notificação de surtos e manejo de casos de varicela
