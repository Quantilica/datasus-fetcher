---
dataset:
  id: sinan-espo
  fonte: datasus
  titulo: Esporotricose (Epizootia)
  resumo: O sinan-espo contém os registros de notificação de epizootias e casos animais de Esporotricose (dermatofitose por *Sporothrix* spp., transmissível de felinos a humanos) registrados no módulo específico do Sistema de Informação de Agravos de Notificação (SINAN)
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2013'
    fim: '2022'
  unidade: uma ficha de notificação/investigação de esporotricose (Epizootia)
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 19
  unidades_de_medida:
    id_notific: 'número inteiro: contagem ou código numérico (ver Descrição)'
    nu_ano: 'número inteiro: contagem ou código numérico (ver Descrição)'
    especie: 'número inteiro: contagem ou código numérico (ver Descrição)'
    g_d: 'número inteiro: contagem ou código numérico (ver Descrição)'
    g_m: 'número inteiro: contagem ou código numérico (ver Descrição)'
    c_d: 'número inteiro: contagem ou código numérico (ver Descrição)'
    c_m: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Esporotricose (Epizootia) (`sinan-espo`)

## Resumo

O `sinan-espo` contém os registros de **notificação de epizootias e casos animais** de Esporotricose (dermatofitose por *Sporothrix* spp., transmissível de felinos a humanos) registrados no módulo específico do Sistema de Informação de Agravos de Notificação (SINAN) do Ministério da Saúde. Cada registro (linha) representa a notificação consolidada de ocorrência de esporotricose em animais (com destaque para felinos, principal reservatório dos surtos urbanos), registrada por unidades de saúde e serviços de zoonoses e digitada no SINAN Net — leiaute compacto de 17 colunas com identificação da notificação, período (semana/mês), local (UF/município), zona e ambiente de ocorrência (`TP_ZN_OCO`/`TP_AMB_OCO`), espécie animal (`ESPECIE`) e indicadores de ocorrência em gatos (`G_D`/`G_M`) e cães (`C_D`/`C_M`) — suporte à Vigilância Integrada em Zoonoses (esporotricose felina/canina e notificação humana) instituída pela Nota Técnica nº 60/2023-CGZV/DEDT.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2013 a 2022, apenas em `FINAIS` (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 10 arquivos (~0,4 MB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim — `meta.py` também consulta `PRELIM`, mas hoje o diretório não contém arquivos do agravo (toda a série está em `FINAIS`)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ESPO` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ESPO` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `ESPOBR22.dbc` — `ESPO` é o prefixo do agravo (Esporotricose), `BR` indica a consolidação nacional de todo o país e `22` é o ano de notificação (2022). O agravo publica apenas em `FINAIS`, de 2013 a 2022 (sem `PRELIM`), com atualizações em 08–18/01/2024.
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-espo/<ano>/sinan-espo_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-espo/2022/sinan-espo_2022-br@20240108.dbc`.
- **Documentação e Tabelas Auxiliares associadas**: no diretório `SINAN/DOCS` estão `Docs_TAB_SINAN.zip` e as instruções POP_I/II/III de acesso, descompactação e tabulação; em `SINAN/AUXILIAR` estão `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip` (denominadores populacionais). A normatização do agravo está na **Nota Técnica nº 60/2023-CGZV/DEDT** (Vigilância da Esporotricose).

## Conteúdo

A esporotricose é uma zoonose micótica em expansão no Brasil, associada à transmissão preferencial por felinos domiciliados e errantes (*Sporothrix brasiliensis*), com surtos urbanos reiteradamente descritos desde os anos 1990 (notadamente no Rio de Janeiro). Em 2023, a vigilância do agravo foi normatizada pela **Nota Técnica nº 60/2023-CGZV/DEDT** (Coordenação-Geral de Vigilância das Zoonoses e Doenças de Transmissão Veterinária/DEDT/SVSA), que institui a vigilância integrada de esporotricose em humanos e animais — as epizootias em felinos e cães passam a ser registradas em módulo próprio do SINAN, em regra pelos serviços de zoonoses e pelas unidades de saúde

O evento gerador deste dataset é a ficha de notificação de esporotricose animal do SINAN (módulo de epizootias, referenciado pela Nota Técnica do agravo). Cada registro é uma notificação consolidada por município-semana, com: identificação da notificação (`ID_NOTIFIC`, sequencial), ano (`NU_ANO`), data de notificação e de digitação (`DT_NOTIFIC`, `DT_DIGITA`), UF e município (`SG_UF_NOT`, `ID_MUNICIP`), semanas epidemiológicas de notificação e de início da epizootia (`SEM_NOT`, `SEM_PRI`), data de início da epizootia (`DT_INI_EPI`), zona da ocorrência (`TP_ZN_OCO`: urbana, rural, periurbana, ignorado), ambiente onde ocorreu a epizootia (`TP_AMB_OCO`: 1 - Domicílio, 2 - Parque, praça ou zoológico, 3 - Área Silvestre, 4 - Reserva Ecológica, 5 - Outro, com descrição em `DS_OUT_AMB`), espécie animal afetada (`ESPECIE`, código conforme dicionário — nos dados observados, o valor 1 concentra a vigilância de felinos) e presença de animais sintomáticos/óbitos por espécie: gatos (`G_D` = doentes, `G_M` = mortos) e cães (`C_D` = doentes, `C_M` = mortos), campos binários/contagem conforme a ficha. A unidade de análise é a notificação de epizootia/caso animal.

A série histórica é curta e recente: o FTP contém apenas as bases `FINAIS` de **2013 a 2022** (10 arquivos, sem diretório `PRELIM`), com última atualização em 08/01/2024 (dois arquivos reenviados em 18/01/2024). O volume inicial é minúsculo (arquivo de 2013 com poucas dezenas de registros, concentrados em municípios do Rio de Janeiro — `SG_UF_NOT` 33) e cresce ao longo dos anos: a vigilância de esporotricose animal (notificação por município/felino) se expande nacionalmente nos anos seguintes, via serviços de zoonoses/CIEVS (módulo de "Sistemas Auxiliares" do SINAN — Epizootias).

Aplicações analíticas típicas: evolução do número de notificações por ano/UF (`NU_ANO`, `SG_UF_NOT`); distribuição de zona e ambiente (`TP_ZN_OCO`, `TP_AMB_OCO`) — perfil urbano/domiciliar da esporotricose felina; espécie e indicadores por espécie (`ESPECIE`, gatos vs cães em `G_D`/`C_D`); sazonalidade por semana epidemiológica (`SEM_NOT`, `SEM_PRI`); e correlação com casos humanos de esporotricose em municípios com notificação ativa (vigilância integrada NT 60/2023).

### Cobertura observada

- Índice do FTP (2026-10): 10 arquivos, de 2013 a 2022, 1 UF(s) com arquivos, última atualização em 2024-01-18.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2013 a 2022), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

Schema extraído de `ESPOBR13.dbc` (17 colunas depois de remover `_deleted`).

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `ID_NOTIFIC` | Inteiro | Número sequencial da notificação de epizootia/caso animal |
| `NU_ANO` | Inteiro | Ano da notificação |
| `DT_NOTIFIC` / `DT_DIGITA` | Data (`AAAAMMDD`) | Data da notificação e de digitação no SINAN |
| `SG_UF_NOT` / `ID_MUNICIP` | String 2/6 | Código das UF (IBGE) e de município (IBGE) de notificação |
| `SEM_NOT` / `SEM_PRI` | String `AAAASS` | Semanas epidemiológicas de notificação e de início da epizootia |
| `DT_INI_EPI` | Data (`AAAAMMDD`) | Data do início da epizootia (não deve ser maior que a data de notificação) |
| `TP_ZN_OCO` | String (1) | Zona onde ocorreu a epizootia: 1 - Urbana, 2 - Rural, 3 - Periurbana, 9 - Ignorado |
| `TP_AMB_OCO` | String (1) | Ambiente onde ocorreu a epizootia: 1 - Domicílio, 2 - Parque/praça/zoológico, 3 - Área Silvestre, 4 - Reserva Ecológica, 5 - Outro |
| `DS_OUT_AMB` | String (30) | Descrição do outro ambiente (habilitado se `TP_AMB_OCO` = 5) |
| `ESPECIE` | Inteiro | Espécie animal notificada (código conforme ficha; nos dados observados o valor 1 concentra a vigilância de felinos) |
| `G_D` / `G_M` | String (1) | Presença/ocorrência de gatos doentes e de gatos mortos |
| `C_D` / `C_M` | String (1) | Presença/ocorrência de cães doentes e de cães mortos |

## Variáveis

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `id_notific` | `ID_NOTIFIC` | inteiro | Código (tipo, identificação ou classificação) registrado na ficha de Esporotricose (Epizootia) (`ID_NOTIFIC`); o dicionário consultado não define o campo isoladamente | — | todos |
| `nu_ano` | `NU_ANO` | inteiro | (campo interno). Ano da notificação | — | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação. co_municipio_not ificacao | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno). ds_semana_notifi cacao | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno). ds_semana_sinto ma | — | todos |
| `dt_ini_epi` | `DT_INI_EPI` | data | Data de início da epizootia (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tp_zn_oco` | `TP_ZN_OCO` | texto | Zona de ocorrência da epizootia (urbana, rural ou periurbana) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tp_amb_oco` | `TP_AMB_OCO` | texto | Ambiente de ocorrência da epizootia (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ds_out_amb` | `DS_OUT_AMB` | texto | Descrição de outro ambiente de ocorrência da epizootia (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `especie` | `ESPECIE` | inteiro | Espécie do animal (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `g_d` | `G_D` | inteiro | Número de animais doentes (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `g_m` | `G_M` | inteiro | Número de animais mortos (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `c_d` | `C_D` | inteiro | Número de animais doentes (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `c_m` | `C_M` | inteiro ou texto | Número de animais mortos (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-espo`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 3, inteiro: 7, texto: 10.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-espo.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- base de **notificação de epizootia/casos animais** — não há registros individuais de pacientes, dados clínicos, exames ou desfechos humanos neste dataset (casos humanos de esporotricose migraram para vigilância integrada à parte, via NT 60/2023); cobertura restrita a `FINAIS` 2013–2022 sem arquivos preliminares; e os campos `G_D`/`G_M`/`C_D`/`C_M` frequentemente vêm em branco (ex.: em `ESPOBR13.dbc` `C_D`/`C_M` vazios), exigindo tratamento cuidadoso de nulos para não confundir "sem info" com "não ocorreu". (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Tipo que varia entre períodos:** `c_m` aparecem com mais de um tipo nas amostras (por exemplo, inteiro em alguns períodos e texto em outros); leia a coluna `Tipo` do dicionário e converta explicitamente antes de empilhar períodos. Evidência: conversão local de amostras em 2026-11-16, `datasus-fetcher` 0.19.0.
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-espo/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-espo
quantilica datasus list sinan-espo

# 2. Baixar microdados de sinan-espo com recorte adequado à partição do dataset
# (SINAN usa uf+year com consolidações BR anuais)
quantilica datasus sync sinan-espo -o ./data --start 2013 --end 2022 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-espo -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-espo -o ./data/raw --parquet-dir ./data/parquet --start 2013
```

### Em Python e Polars

```python
import polars as pl

from datasus_fetcher.reader import read_dbc

# Descompacta o .dbc via extensão nativa em Rust e lê o .dbf tratado com polars
qdf = read_dbc("data/sinan-espo/2022/sinan-espo_2022-br@20240108.dbc", clean=True)

# Notificações por UF e zona de ocorrência
zonas = qdf.group_by(["sg_uf_not", "tp_zn_oco"]).len().sort("sg_uf_not")
print(zonas)

# Ambientes onde ocorreram as epizootias de esporotricose
amb = qdf.group_by("tp_amb_oco").len().sort("tp_amb_oco")
print(amb)

# Municípios com mais notificações no arquivo
mun = qdf.group_by("id_municip").len().sort("len", descending=True)
print(mun.head(10))
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Epizootias/Esporotricose (Sistemas Auxiliares do SINAN)**: https://portalsinan.saude.gov.br
- **Nota Técnica nº 60/2023-CGZV/DEDT** (Vigilância da Esporotricose, humana e em animais — CGZV/DEDT/SESSAS/MS)
- **Portaria GM/MS nº 204/2016** (consolidação da notificação compulsória do SUS), Lei nº 6.259/1975 e Decreto nº 78.231/1976
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
- **Guia de Vigilância em Saúde (SVSA/MS, Ed. atual)** — capítulo de micose cutânea/dermatofitoses e vigilância de zoonoses (zoonoses urbanas)
