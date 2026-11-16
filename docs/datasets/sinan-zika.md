---
dataset:
  id: sinan-zika
  fonte: datasus
  titulo: Zika Vírus
  resumo: 'Zika Vírus do DATASUS: uma ficha de notificação/investigação de zika Vírus.'
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2015'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de zika Vírus
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 40
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais:
  - coluna: ano_nasc
    categoria: ano de nascimento
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Zika Vírus (`sinan-zika`)

## Resumo

O `sinan-zika` contém os microdados das notificações e investigações epidemiológicas de casos de Zika vírus (CID-10 A92.8 — "outros febres virais transmitidas por artrópodes") registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de zika (exantemático), digitada no SINAN Net/Sinan Online. A série começa em 2015, quando a circulação do vírus foi identificada no Brasil durante a emergência associada à microcefalia e à síndrome congênita do vírus zika.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Arquivos preliminares:** Sim (diretório `PRELIM`)
- **Documentação oficial no FTP:** `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP:** `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ZIKA` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ZIKA` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `ZIKABR16.dbc` — prefixo `ZIKA`, `BR` (consolidação nacional) e `16` (ano 2016); a série vai de `ZIKABR15.dbc` até `ZIKABR25.dbc`, com o ano corrente em `PRELIM` (ex.: `ZIKABR26.dbc`).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-zika/<AAAA>/sinan-zika_<AAAA>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-zika/2024/sinan-zika_2024-br@20261016.dbc` (o sufixo `@AAAAMMDD` é a data do arquivo no FTP; arquivos preliminares levam `-preliminar` no nome do dataset).
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e PDFs de acesso/descompactação/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## Conteúdo

A zika é uma arbovirose urbana transmitida pelo `Aedes aegypti` (e também por via sexual), gerida pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS). A emergência sanitária de 2015-2016 — caracterizada pela associação entre a infecção pelo vírus Zika na gestação e a microcefalia e demais anomalias congênitas, além da síndrome de Guillain-Barré — levou à formalização da doença como evento de notificação compulsória consolidada na Portaria GM/MS nº 204/2016 (lista posteriormente atualizada, ex.: Portaria GM/MS nº 10.175/2026). O dataset fornece a base de notificação individual para monitorar a transmissão, os casos em gestantes e as complicações neurológicas.

O evento gerador é a **Ficha de Notificação/Investigação de Zika** do SINAN. Em 2015/2016 a notificação usou a ficha de febre rash viral/exantemática com módulo de conclusão Zika e, a partir da versão de 2016, a ficha única de dengue/chikungunya/zika do Sinan Online (`ID_AGRAVO` distinguindo o agravo). A unidade de análise é o caso suspeito/confirmado de zika, definido por exantema maculopapular associado a febre, conjuntivite não pruriginosa ou poliúrtia/polyarthralgia conforme a definição de caso vigente, em pessoa residente ou procedente de área com transmissão — não o nascido vivo com anomalia congênita nem o caso de microcefalia (que são monitorados em sistemas próprios como RESP/SINASC).

Marcos de evolução do leiaute: 2015 — primeiras notificações na ficha de febre rash viral com conclusão Zika; 2016 — ficha unificada de arboviroses e plena implantação do Sinan Online Gotas. Como consequência, os campos de investigação específica de zika (sinais e sintomas, complicações neurológicas como Guillain-Barré) só existem na ficha mais recente e, no leiaute antigo, permanecem em branco.

Aplicações analíticas: coeficiente de incidência de zika por 100 mil habitantes, proporção de casos entre gestantes e mulheres em idade fértil, monitoramento de complicações neurológicas pós-infecciosas, análise da concorrência espacial com dengue e chikungunya e estruturação de estudos de coorte da síndrome congênita associada ao vírus zika.

### Cobertura observada

- Índice do FTP (2026-10): 12 arquivos, de 2015 a 2026, 1 UF(s) com arquivos, última atualização em 2026-11-10.
- Conversão local de amostras (5 arquivo(s) Parquet, de 2015 a 2026), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo na ficha unificada (Zika — CID-10 A92.8) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas (exantema + febre/conjuntivite/outras) |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `CS_GESTANTE` | Inteiro | Estado gestacional — crucial para o monitoramento de gestantes |
| `ID_MN_RESI` | String (6/7) | Município de residência do paciente (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `CLASSI_FIN` | Inteiro | Classificação final (confirmação/descarte/inconclusivo da zika conforme o dicionário do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação/descarte (1 - Laboratório, 2 - Clínico Epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução do caso (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

## Variáveis

Descrições tiradas do informe técnico ou do dicionário de dados do DATASUS quando o campo consta do documento; textos marcados "inferido do nome do campo" não têm definição oficial; "Sem descrição na documentação oficial consultada" é lacuna a preencher. `Tipo` e `Período` vêm do esquema de referência (conversão local de amostras): `Período` é o intervalo de partições amostradas em que a coluna existe, e `todos` significa todas as amostras. `Na fonte` é o nome do campo no DBF.

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `tp_not` | `TP_NOT` | texto | Tipo de Notificação. Identifica o tipo da notificação | 1 – Negativa 2 – Individual 3 – Surto 4 – Agregado | todos |
| `id_agravo` | `ID_AGRAVO` | texto | Agravo/doença. Especifica a suspeição do agravo | 1-Dengue 2-Chikungunya | todos |
| `dt_notific` | `DT_NOTIFIC` | data | Data da Notificação. Data de preenchimento da ficha de notificação | — | todos |
| `sem_not` | `SEM_NOT` | texto | Semana epidemiológic a da notificação (campo interno) | — | todos |
| `nu_ano` | `NU_ANO` | texto | (campo interno). Ano da notificação | — | todos |
| `sg_uf_not` | `SG_UF_NOT` | texto | UF de Notificação. Sigla da Unidade Federativa onde está localizada a unidade de saúde (ou outra fonte notificadora) que realizou a notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_municip` | `ID_MUNICIP` | texto | Município de Notificação | — | todos |
| `id_regiona` | `ID_REGIONA` | texto | (campo interno). Regional de saúde onde está localizado o município da unidade de saúde ou outra fonte notificadora | — | todos |
| `id_unidade` | `ID_UNIDADE` | texto | Unidade de saúde ou outra fonte notificadora | — | todos |
| `dt_sin_pri` | `DT_SIN_PRI` | data | Data dos primeiros sintomas / Diagnóstico | — | todos |
| `sem_pri` | `SEM_PRI` | texto | Semana epidemiológic a dos primeiros sintomas/ diagnósticos. (campo interno) | — | todos |
| `ano_nasc` | `ANO_NASC` | texto | Ano de nascimento do paciente (campo do SINAN-Windows) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil) | — | todos |
| `nduplic_n` | `NDUPLIC_N` | texto | Não Listar/ Não Contar. 0 ou branco – Não identificado 1 – Não é duplicidade (não listar) 2 – Duplicidade (não contar) | — | todos |
| `in_vincula` | `IN_VINCULA` | texto | Vinculação. 0 ou branco – Não Vinculado 1 – Vinculado | — | todos |
| `dt_invest` | `DT_INVEST` | data | Data da Investigação. Informar a data da investigação | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/ramo de atividade econômica. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo de atividade econômica do paciente refere-se as atividades econômicas desenvolvidas nos processos de produção do setor primário (agricultura e extrativismo); secundário (indústria) ou terciário (serviços e comércio) | — | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação. VARCHAR (1) | 5-Descartado 10-Dengue 11-Dengue com sinais de alarme 12-Dengue grave 13-Chikungunya | todos |
| `criterio` | `CRITERIO` | texto | Critério De Confirmação/Descarte. o | 1-Laboratório 2-Clínico Epidemiológico 3-Em investigação | todos |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência? | 1 – Sim 2 – Não 3 – Indeterminado | todos |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o paciente foi provavelmente infectado | — | todos |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente infectado | — | todos |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). o | — | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho | 1 – Sim 2 – Não 9 – Ignorado | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução Do Caso. VARCHAR (1) | 1- cura 2- óbito pelo agravo 3- óbito por outras causas 4- óbito em investigação 9- ignorado | todos |
| `dt_obito` | `DT_OBITO` | data | Data do Óbito. Informar a data do óbito | — | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data Do Encerramento. Informar a data do encerramento do caso | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `tp_sistema` | `TP_SISTEMA` | texto | Sistema de origem do registro (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `tpuninot` | `TPUNINOT` | texto | Tipo da unidade notificadora (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-zika`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 6, inteiro: 1, texto: 33.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-zika.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- volume pequeno (12 consolidações `BR` anuais, ~14 MB) — a notificação de zika decai após a epidemia de 2015-2016, mas casos suspeitos continuam sendo registrados; parte dos casos pode estar embutida na ficha unificada de dengue/chikungunya, exigindo filtro por `ID_AGRAVO` para recompor a base; grande proporção de confirmação clínico-epidemiológica exige cautela com `CLASSI_FIN`; gestantes merecem atenção especial via `CS_GESTANTE` e o arquivo do ano corrente em `PRELIM` é sujeito a revisão. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano e UF de notificação?

```python
from pathlib import Path

import polars as pl

arquivos = sorted(Path("lake/datasus/sinan-zika").glob("**/*.parquet"))
dados = pl.concat(  # períodos diferentes têm colunas e tipos diferentes
    [pl.scan_parquet(a, hive_partitioning=True) for a in arquivos],
    how="diagonal_relaxed",
)

(
    dados.group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Pela linha de comando (`datasus-fetcher`)

```bash
# o que o FTP publica para o dataset (arquivos e tamanho)
datasus-fetcher list sinan-zika

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync sinan-zika -o ./data --start 2020 --end 2024 --regions br --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset sinan-zika
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Nota técnica SINAN – Dengue/Chikungunya/Zika (Sinan Online)**: https://sistemas.saude.rj.gov.br/tabnetbd/Sinan/NT_dengue_chik_zika.pdf
- **Portal SINAN — Dengue/Chikungunya/Zika (fichas e dicionários)**: https://portalsinan.saude.gov.br/sinan-dengue-chikungunya
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde** (SVSA/MS, capítulo Zika e síndrome congênita)
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
