---
dataset:
  id: sinan-pest
  fonte: datasus
  titulo: Peste
  resumo: O sinan-pest contém os microdados das notificações e investigações de casos de Peste (CID-10 A20) registrados no Sistema de Informação de Agravos de Notificação (SINAN).
  orgao: Ministério da Saúde — Secretaria de Vigilância em Saúde e Ambiente (SVSA), GT-SINAN
  pagina_oficial: ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '2007'
    fim: em-curso
  unidade: uma ficha de notificação/investigação de peste
  granularidade:
    espacial: município de notificação e de residência do paciente; arquivo nacional
    temporal: data da notificação e de início dos sintomas; arquivo anual
  formato_bruto: DBC (DBF comprimido com PKWARE DCL), codificação latin1, um arquivo nacional (`BR`) por ano; o ano corrente fica em diretório de preliminares
  lake:
    estado: convertido
    particoes:
    - ano
    chave: []
    colunas: 54
  unidades_de_medida:
    nu_idade_n: 'número inteiro: contagem ou código numérico (ver Descrição)'
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Peste (`sinan-pest`)

## Resumo

O `sinan-pest` contém os microdados das notificações e investigações de casos de Peste (CID-10 A20) registrados no Sistema de Informação de Agravos de Notificação (SINAN). Cada registro representa a ficha individual de notificação/investigação de um caso suspeito ou confirmado de peste humana (formas bubônica, pulmonar ou septicêmica), digitado no SINAN Net/Sinan Online. A peste é de notificação compulsória imediata e permanece na lista nacional por sua relevância histórica e pelo risco de reativação nos bolsões naturais de roedores silvestres — especialmente os focos do semiárido nordestino.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.dbc` (comprimido dBASE, descompactável nativamente em Rust)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (arquivos consolidados anuais, praticamente sempre `br`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 2007 a 2025 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 19 arquivos (~42,8 KB)
- **Arquivos preliminares** (índice de 2026-10, conforme a página anterior): Sim (diretório `PRELIM`)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/DOCS`
- **Tabelas auxiliares no FTP** (índice de 2026-10, conforme a página anterior): `/dissemin/publicos/SINAN/AUXILIAR`

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `PEST` | UF + AA (2 dígitos; na prática consolidações `BR` anuais) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `PEST` | UF + AA (2 dígitos) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `PESTBR07.dbc` — prefixo `PEST`, `BR` (consolidação nacional) e `07` (ano 2007), até `PESTBR24.dbc` (2024); o arquivo do ano corrente fica em `PRELIM` (ex.: `PESTBR25.dbc`). A série é minúscula: ~42 kB no total, refletindo poucas notificações.
- **No armazenamento local do `datasus-fetcher`**: caminho padronizado `data/sinan-pest/<ano>/sinan-pest_<período>-<uf>@<AAAAMMDD>.dbc`, por exemplo `data/sinan-pest/2024/sinan-pest_2024-br@20260212.dbc`; arquivos preliminares recebem o sufixo `-preliminar`.
- **Documentação e Tabelas Auxiliares associadas**: em `SINAN/DOCS`: `Docs_TAB_SINAN.zip` e os PDFs de acesso/conversão/tabulação (`POP_I`, `POP_II`, `POP_III`); em `SINAN/AUXILIAR`: `TAB_SINANNET.zip`, `TAB_SINANONLINE.zip` e `POPT_Estimativa_TCU_2019_Sinan.zip`.

## Conteúdo

A peste é uma zoonose infecciosa causada pela bactéria *Yersinia pestis*, transmitida ao homem por pulgas de roedores. No Brasil, persiste a vigilância da peste nos focos naturais consolidados pela literatura técnica: planalto da Borborema (Paraíba, Pernambuco e Alagoas), serra da Ibiapaba e Chapada do Araripe (Ceará), credo do Sudoeste da Bahia e planaltos do Piauí/Pernambuco. Nestes ecossistemas, roedores silvestres e comensais infectados e suas pulgas mantêm o potencial de reativação, ainda que casos humanos confirmados sejam raríssimos nas últimas décadas. A vigilância é da SVSA/MS, com o agravo constando da lista de notificação compulsória imediata da Portaria SVS/MS nº 5/2006 e da consolidação vigente (Portaria GM/MS nº 204/2016).

O evento gerador é a **Ficha de Investigação da Peste** do SINAN (ficha `Peste_v5`), preenchida diante do caso suspeito — pessoa com febre aguda acompanhada de linfadenopatia dolorosa (bubão), pneumonia grave com insuficiência respiratória rápida ou septicemia, com vínculo epidemiológico com área de foco — e concluída com exames laboratoriais (coloração de esfregaço/bisnaga, cultivo, serologia anti-F1 e PCR conforme disponibilidade) e o desfecho. A unidade de análise é o caso suspeito/confirmado individual, em número muito pequeno no Brasil (a base publica poucas notificações por ano).

Marcos do sistema: a ficha v5 data do período SINAN Net (2005-2006) e a vigilância integra o monitoramento de roedores e pulgas nos focos, além da notificação negativa anual dos municípios dos bolsões. Como o volume de casos humanos é mínimo, a base praticamente registra investigações de casos suspeitos, mantidas para assegurar a continuidade do estado de vigilância da peste no país.

Aplicações analíticas: monitoramento da endemicidade e da reativação nos bolsões naturais, descrição de casos confirmados (formas clínicas, letalidade), e verificação da operacionalidade da notificação negativa nos municípios sob vigilância.

### Cobertura observada

- Índice do FTP (2026-10): 19 arquivos, de 2007 a 2025, 1 UF(s) com arquivos, última atualização em 2026-02-12.
- Conversão local de amostras (3 arquivo(s) Parquet, de 2007 a 2016), feita em 2026-11-16 com o `datasus-fetcher` 0.19.0: serve de base ao esquema de referência. Períodos fora das amostras podem ter colunas que não aparecem aqui.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String / Inteiro | Tipo de notificação (2 - Individual) |
| `ID_AGRAVO` | String | Agravo notificado (Peste — CID-10 A20) |
| `DT_NOTIF` | Data (`AAAAMMDD`) | Data da notificação (campo-chave; compulsória imediata) |
| `SEM_NOT` | Inteiro (`AAAASS`) | Semana epidemiológica da notificação |
| `NU_ANO` | Inteiro | Ano de notificação |
| `SG_UF_NOT` | String (2) | UF do município de notificação |
| `ID_MUNICIP` | String (6/7) | Código IBGE do município de notificação |
| `ID_UNIDADE` | String (7) | CNES da unidade notificadora |
| `DT_SIN_PRI` | Data (`AAAAMMDD`) | Data de início dos sintomas |
| `SEM_PRI` | Inteiro (`AAAASS`) | Semana epidemiológica de início dos sintomas |
| `CS_SEXO` | String (1) | Sexo (M/F/I) |
| `NU_IDADE_N` | Inteiro composto | Idade com dígito de unidade na primeira posição |
| `ID_MN_RESI` | String (6/7) | Município de residência (IBGE) |
| `DT_INVEST` | Data (`AAAAMMDD`) | Data da investigação |
| `CLASSI_FIN` | Inteiro | Classificação final (1 - Confirmado, 5 - Descartado; dicionário específico do agravo) |
| `CRITERIO` | Inteiro | Critério de confirmação (1 - Laboratorial, 2 - Clínico-epidemiológico, 3 - Em investigação) |
| `EVOLUCAO` | Inteiro | Evolução (1 - Cura, 2 - Óbito pelo agravo, 3 - Óbito por outras causas, 9 - Ignorado) |
| `DT_OBITO` | Data (`AAAAMMDD`) | Data do óbito |
| `DT_ENCERRA` | Data (`AAAAMMDD`) | Data de encerramento do caso |
| `HOSPITAL` | Inteiro | Hospitalização (1 - Sim, 2 - Não, 9 - Ignorado) |

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
| `nu_idade_n` | `NU_IDADE_N` | inteiro | Idade. A composição da variável obedece o seguinte critério: 1o | — | todos |
| `cs_sexo` | `CS_SEXO` | texto | Sexo. M- Masculino F- Feminino I- Ignorado | — | todos |
| `cs_gestant` | `CS_GESTANT` | texto | Gestante. Gestante 1. 1º Trimestre 2. 2º Trimestre 3. 3º Trimestre 4. Idade gestacional ignorada 5. Não 6. Não se aplica 9. Ignorado | — | todos |
| `cs_raca` | `CS_RACA` | texto | Raça/Cor. Considera-se cor ou raça declarada pela pessoa. 1. branca 2. preta 3. amarela (pessoa que se declarou de raça amarela) 4. parda (pessoa que se declarou mulata, cabocla, cafuza, mameluca ou mestiça de preto com pessoa de outra cor ou raça) 5. indígena (pessoa que se declarou indígena ou índia) | 1- branca 2- preta 3- amarela 4- parda 5- indígena 9 Ignorado | todos |
| `cs_escol_n` | `CS_ESCOL_N` | texto | Escolaridade. 43 Analfabeto 1. 1ª a 4ª série incompleta do EF 2. 4ª série completa do EF ( antigo 1° grau) 3. 5ª à 8ª série incompleta do EF (antigo ginásio ou 1° grau) 4. Ensino fundamental completo (antigo ginásio ou 1° grau) 5. Ensino médio incompleto (antigo colegial ou 2° grau) 6. Ensino médio completo (antigo colegial ou 2° grau) 7. Educação superior incompleta 8. Educação superior completa 9. Ignorado 10. N... | — | todos |
| `sg_uf` | `SG_UF` | texto | UF. Sigla da Unidade Federada de residência do paciente por ocasião da notificação. A sigla é uma variável que está associada ao código na tabela | — | todos |
| `id_mn_resi` | `ID_MN_RESI` | texto | Município de residência. co_municipio_res idencia | — | todos |
| `id_rg_resi` | `ID_RG_RESI` | texto | (campo interno). Regional de saúde onde está localizado o município de residência do paciente por ocasião da notificação | — | todos |
| `id_pais` | `ID_PAIS` | texto | País (se residente fora do Brasil). co_pais_residenc ia | — | todos |
| `dt_invest` | `DT_INVEST` | data | Data da Investigação. Data em que ocorreu a investigação – informar a data da 1ª visita ao paciente | — | todos |
| `id_ocupa_n` | `ID_OCUPA_N` | texto | Ocupação/Ramo de atividade econômica. Informar a atividade exercida pelo paciente no setor formal, informal ou autônomo ou sua última atividade exercida quando paciente for desempregado. O ramo de atividade econômica do | — | todos |
| `co_risco` | `CO_RISCO` | texto | A ocorrência cumpre condições básicas de risco ? | 1-Sim 2-Não 9-Ignorado | todos |
| `epi_peste` | `EPI_PESTE` | texto | O caso está associado a eventos positivos de importância epidemiológica para Peste ? | 1-Sim 2-Não 9-Ignorado | todos |
| `com_pest` | `COM_PEST` | texto | Os sinais e sintomas são compatíveis com a definição de caso ? | 1-Sim 2-Não 9-Ignorado | todos |
| `sin_gang` | `SIN_GANG` | texto | Sintomatologia específica ganglionar. st_sintomatologia_gangli onar | 1-Sim 2-Não 9-Ignorado | todos |
| `sin_pulm` | `SIN_PULM` | texto | Manifestação clínica registrada na ficha de Peste (`SIN_PULM`); o dicionário consultado não define o campo isoladamente | — | todos |
| `tratado` | `TRATADO` | texto | Caso Tratado | 1-Sim 2-Não 9-Ignorado | todos |
| `criterio` | `CRITERIO` | texto | Critério de confirmação/descarte | 1-Laboratorial 2-Clínico 3-Indeterminado | todos |
| `classi_fin` | `CLASSI_FIN` | texto | Classificação Final | 1- Confirmado 2- Descartado | todos |
| `con_gravid` | `CON_GRAVID` | texto | Gravidade | 1. Benigno/ ambulatorial 2. Moderado 3. Grave | todos |
| `coufinf` | `COUFINF` | texto | UF (provável da fonte de infecção). Sigla da unidade federada onde o paciente foi provavelmente infectado | — | todos |
| `copaisinf` | `COPAISINF` | texto | País (provável da fonte de infecção). País onde o paciente foi provavelmente infectado | — | todos |
| `comuninf` | `COMUNINF` | texto | Município (provável da fonte de infecção). Código do município onde o paciente foi provavelmente infectado. O nome está associado | — | todos |
| `doenca_tra` | `DOENCA_TRA` | texto | Doença relacionada ao trabalho. Se o paciente adquiriu a doença em decorrência das condições/situação do trabalho | 1-Sim; 2-Não; 9-Ignorado | todos |
| `evolucao` | `EVOLUCAO` | texto | Evolução do caso | 1-Cura 2-Óbito por peste 3-Obito por outras causas 9-Ignorado | todos |
| `dt_encerra` | `DT_ENCERRA` | data | Data do Encerramento. Data do encerramento do processo de investigação do caso | — | todos |
| `dt_digita` | `DT_DIGITA` | data | Data de digitação. Data de Digitação da primeira inclusão da notificação no sistema | — | todos |
| `dt_obito` | `DT_OBITO` | data | Data de óbito | — | todos |
| `con_classi` | `CON_CLASSI` | texto | Classificação da forma clínica | 1. Forma bubônica 2. Forma pneumônica 3. Forma septicêmica 4 outra | todos |
| `lab_esfr` | `LAB_ESFR` | texto | Exame Bacteriológico Esfregaço | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | todos |
| `dt_s1` | `DT_S1` | data | Data da Coleta S1 | — | todos |
| `lab_hemo` | `LAB_HEMO` | texto | Exame Bacteriológico Hemocultura | 1-Positivo 2-Negativo 3-Inconclusivo 4-Não realizado | todos |
| `dt_s2` | `DT_S2` | data | Data da Coleta S2 | — | todos |
| `elisa1` | `ELISA1` | texto | Resultado da Sorologia para ELISA – S1 | 1-Reagente 2-Não-Reagente 3-Inconclusivo 4-Não realizado | todos |
| `elisa2` | `ELISA2` | texto | Resultado da Sorologia para ELISA – S2 | 1-Reagente 2-Não-Reagente 3-Inconclusivo 4-Não realizado | todos |
| `hemo_igm` | `HEMO_IGM` | texto | Resultado da Hemoaglutinação - IgM | 1-Reagente 2-Não-Reagente 3-Inconclusivo 4-Não realizado | todos |
| `hemo_igg` | `HEMO_IGG` | texto | Resultado da Hemoaglutinação - IgG | 1-Reagente 2-Não-Reagente 3-Inconclusivo 4-Não realizado | todos |
| `igm_t1` | `IGM_T1` | texto | Resultado da Hemoaglutinação – IgM Título | — | todos |
| `igg_t2` | `IGG_T2` | texto | Resultado da Hemoaglutinação – IgG Título | — | todos |
| `co_focal` | `CO_FOCAL` | texto | Instituído controle focal? | 1-Sim 2-Não 9-Ignorado | todos |
| `tpautocto` | `TPAUTOCTO` | texto | O caso é Autóctone de residência?. Indica se o caso é autóctone do município de residência | 1 – Sim 2 – Não 3 – Indeterminado | todos |
| `uf` | — | texto | UF do arquivo de origem (sigla em minúsculas, `br` para arquivos nacionais), gravada pelo conversor; as linhas do período saem ordenadas por ela | sigla da UF | todos |
| `_origem` | — | texto | Chave do arquivo bruto que originou a linha (nome do arquivo no FTP, sem o carimbo de data), gravada pelo conversor | texto | todos |

## No lake

- **Dataset no lake:** `datasus/sinan-pest`, particionado por `ano` (diretórios `chave=valor`). A UF do arquivo de origem vai na coluna `uf` (as linhas do período saem ordenadas por ela) e o nome do arquivo bruto, na coluna `_origem`; os arquivos de uma mesma partição compartilham um Parquet.
- **Chave:** sem chave natural declarada. Nenhuma combinação de colunas foi conferida como única nas amostras; para tirar duplicatas, defina a chave por consulta (ver Cuidados de uso).
- **Tipos nas amostras** (número de colunas): data: 8, inteiro: 1, texto: 45.
- **Transformações do conversor** (`datasus-fetcher` 0.19.0, `wrangle_datasus` e `LakeConverter`): nomes de coluna em minúsculas; textos aparados (espaços das pontas saem); valores de preenchimento (texto vazio, `NA`, `null`, `None` e códigos como `999999` e `00000000`, conforme a lista `SENTINEL_NULLS` do pacote) viram nulo; colunas de código (CID, CNES, município, procedimento, CEP, número de AIH e semelhantes) ficam como texto, preservando zeros à esquerda; colunas de data no formato `AAAAMMDD` viram data (valores inválidos interrompem a conversão em vez de virarem nulo); valores monetários com casas decimais ficam como decimal exato; registros marcados como excluídos no DBF são descartados; arquivos DBC sem nenhuma linha não passam pela limpeza (ver Cuidados de uso).
- **Colunas renomeadas por colidir com partição** (SINAN): `UF` vira `uf_hospital`.
- **Esquema de referência:** `sinan-pest.schema.json`, gerado por conversão local de amostras. Tipos listados com mais de um valor variam entre partições.

## Cuidados de uso

- volume minúsculo (~42 kB em 19 consolidações) — quase todas as fichas correspondem a casos investigados nos bolsões; maior parte das fichas corresponde a casos descartados e poucos confirmados; atenção ao município provável de infecção ao usar as colunas de residência, pois a exposição de campo pode ocorrer em município diverso do de notificação. (texto da versão anterior desta página; não reconferido nesta revisão.)
- **Dado pessoal:** as colunas listadas em `dados_pessoais` no cabeçalho são o inventário por nome de coluna; atributos demográficos e territoriais (sexo, raça/cor, idade, município de residência) não entram na lista, mas combinados podem identificar uma pessoa.
- **Arquivos DBC vazios:** um arquivo sem nenhuma linha escapa da limpeza do conversor e grava as colunas com os nomes originais em maiúsculas, mais `_deleted`, no Parquet daquele período; filtre arquivos com zero linhas antes de empilhar partições. Verificado na conversão de amostras em 2026-11-16 (achado do conversor; não corrigido aqui).

## Exemplos

### Consulta sobre o lake (polars)

Quantas fichas foram notificadas por ano de notificação e UF de notificação?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/sinan-pest/**/*.parquet", hive_partitioning=True)
    .group_by("ano", "sg_uf_not")
    .agg(pl.len().alias("fichas"))
    .sort("ano", "sg_uf_not")
    .collect()
)
```

O caminho `lake/` é a raiz do lake (a pasta que contém `datasus/`). A consulta foi executada sobre a conversão local de amostras de 2026-11-16.

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-pest
quantilica datasus list sinan-pest

# 2. Baixar microdados de sinan-pest com recorte adequado à partição do dataset
quantilica datasus sync sinan-pest -o ./data --start 2007 --end 2024 --regions br

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-pest -o ./data --docs --aux

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-pest -o ./data/raw --parquet-dir ./data/parquet --start 2007
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# A base de peste é pequena; abaixo, uma leitura consolidada com polars
qdf = read_dbc("data/sinan-pest/2024/sinan-pest_2024-br@20260212.dbc", clean=True)

# Distribuição dos casos por classificação final e ano
print(qdf.group_by("nu_ano", "classi_fin").len().sort(["nu_ano", "classi_fin"]))

# UF de notificação dos casos registrados
print(qdf.group_by("sg_uf_not").len().sort("len", descending=True))
```
## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/FINAIS` e `.../SINAN/DADOS/PRELIM`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN — Peste**: https://portalsinan.saude.gov.br/peste
- **Portaria GM/MS nº 204/2016** e **Guia de Vigilância em Saúde (SVSA/MS)** — capítulo Peste
- **PCDaS/Fiocruz — SINAN**: https://pcdas.icict.fiocruz.br/conteudo/tecnico/sinan
