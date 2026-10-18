# `sinan-viol` — Violência doméstica, sexual e/ou outras violências

Notificações de violência interpessoal e autoprovocada (incluindo tentativas de suicídio), de notificação compulsória no SINAN. Cada linha representa uma ficha de notificação/investigação de um caso de violência doméstica, sexual, física, psicológica ou outras formas, atendido em serviços de saúde.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-viol` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido) |
| **Particionamento** | `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2009 a 2025 (conforme `index.json`) |
| **Volume aproximado no FTP** | 17 arquivos (~326 MB) |
| **Arquivos preliminares** | Sim (diretório PRELIM, 2025; Finais até 2024) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

A notificação de violências é compulsória e imediata em todo o território nacional, conforme a Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023). A vigilância é coordenada pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS), em articulação com a área de Vigilância de Violências e Acidentes (VIVA). A notificação de violência contra crianças, adolescentes, mulheres e pessoas idosas decorre de marcos legais como o ECA (Lei nº 8.069/1990), a Lei Maria da Penha (Lei nº 11.340/2006) e o Estatuto da Pessoa Idosa (Lei nº 10.741/2003).

O evento gerador é qualquer caso suspeito ou confirmado de violência interpessoal (doméstica/intrafamiliar, comunitária) ou autoprovocada, incluindo a violência física, psicológica/moral, sexual, tortura, tráfico de seres humanos, violência financeira/econômica, trabalho infantil, intervenção legal e negligência/abandono. O CID-10 utilizado abrange o Capítulo XX (V01–Y98), com destaque para agressões (X85–Y09) e lesões autoprovocadas (X60–X84). A unidade de análise é o caso notificado (um registro por ficha).

O instrumento é a *Ficha de Notificação/Investigação Individual — Violência Interpessoal/Autoprovocada*, que registra dados da pessoa atendida, local de ocorrência, lesões e partes do corpo atingidas, meios de agressão, formas de violência, dados do autor provável da agressão e grau de parentesco. A série no FTP inicia em 2009 (implantação do Sinan Net para violência) e o ano de 2025 está em PRELIM, sujeito a revisão.

Principais usos: dimensionamento e caracterização da violência no país, monitoramento de casos por faixa etária e sexo, vigilância de violência sexual e de violência contra grupos vulneráveis, apoio à rede de proteção e à formulação de políticas públicas de prevenção.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `VIOL` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `VIOL` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `VIOLBR24.dbc`, em que `VIOL` é o prefixo do agravo, `BR` indica a base nacional (arquivo único por ano para o Brasil) e `24` é o ano com 2 dígitos (2024). O arquivo preliminar mais recente é `VIOLBR25.dbc`.
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-viol/<partição>/sinan-viol_br_2009_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP.
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`): `Docs_TAB_SINAN.zip` (~65 MB), `POP_I_Acesso_a_Microdados_5.pdf`, `POP_II_Descompactacao_expansao_conversao_3.pdf`, `POP_III_Instalacao_do_tabulador_TabWin_3.pdf`.
  - Tabelas auxiliares (`/SINAN/AUXILIAR`): `TAB_SINANNET.zip` (~44 MB), `TAB_SINANONLINE.zip` (~240 KB), `POPT_Estimativa_TCU_2019_Sinan.zip`.
  - O dicionário desta base (`Violência Interpessoal/Autoprovocada`) é distribuído no Portal SINAN e no VIVA; não há PDF por agravo no FTP.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo `VIOLBR09.dbc` (leiaute do SINAN Net; fichas e leiautes podem variar entre anos, por isso a lista reflete esse arquivo). Os arquivos públicos não trazem identificadores individuais como número da notificação (`NU_NOTIFIC`) nem data de nascimento completa. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (registro da ficha de notificação individual). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado. |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | String | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE). |
| `DT_OCOR` | Data (AAAAMMDD) | Data da ocorrência da violência. |
| `SEM_PRI` | String | Semana epidemiológica da ocorrência (AAAASS). |
| `ANO_NASC` | String | Ano de nascimento (o arquivo público não traz a data de nascimento completa). |
| `NU_IDADE_N` | Inteiro | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade. |
| `SG_UF` | String | UF de residência (código IBGE de 2 dígitos). |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `NDUPLIC` | String | Indicador de duplicidade da ficha. |
| `DT_INVEST` | Data (AAAAMMDD) | Data da investigação. |
| `ID_OCUPA_N` | String | Ocupação do trabalhador (CBO 2002, 6 dígitos). |
| `SIT_CONJUG` | String | Situação conjugal. |
| `DEF_TRANS` | String | Pessoa com deficiência/transtorno (geral). |
| `DEF_FISICA` | String | Deficiência física. |
| `DEF_MENTAL` | String | Deficiência mental. |
| `DEF_VISUAL` | String | Deficiência visual. |
| `DEF_AUDITI` | String | Deficiência auditiva. |
| `TRAN_MENT` | String | Transtorno mental. |
| `TRAN_COMP` | String | Transtorno de comportamento. |
| `SG_UF_OCOR` | String | UF de ocorrência da violência. |
| `ID_MN_OCOR` | String | Município de ocorrência da violência (código IBGE). |
| `HORA_OCOR` | String | Hora da ocorrência. |
| `LOCAL_OCOR` | String | Local de ocorrência (descrição de outros em `LOCAL_ESPE`). |
| `OUT_VEZES` | String | A violência ocorreu outras vezes. |
| `LES_AUTOP` | String | Lesão autoprovocada (distingue violência autoprovocada). |
| `VIOL_FISIC` | String | Violência física. |
| `VIOL_PSICO` | String | Violência psicológica/moral. |
| `VIOL_TORT` | String | Tortura. |
| `VIOL_SEXU` | String | Violência sexual. |
| `VIOL_TRAF` | String | Tráfico de seres humanos. |
| `VIOL_FINAN` | String | Violência financeira/econômica. |
| `VIOL_NEGLI` | String | Negligência/abandono. |
| `VIOL_INFAN` | String | Trabalho infantil. |
| `VIOL_LEGAL` | String | Intervenção legal. |
| `VIOL_OUTR` | String | Outra violência (descrição em `VIOL_ESPEC`). |
| `AG_FORCA` | String | Meio de agressão: força corporal/espancamento. |
| `AG_ENFOR` | String | Meio de agressão: enforcamento. |
| `AG_OBJETO` | String | Meio de agressão: objeto contundente. |
| `AG_CORTE` | String | Meio de agressão: objeto perfurocortante. |
| `AG_QUENTE` | String | Meio de agressão: substância/objeto quente. |
| `AG_ENVEN` | String | Meio de agressão: envenenamento. |
| `AG_FOGO` | String | Meio de agressão: arma de fogo. |
| `AG_AMEACA` | String | Meio de agressão: ameaça. |
| `AG_OUTROS` | String | Outro meio de agressão (descrição em `AG_ESPEC`). |
| `SEX_ASSEDI` | String | Violência sexual: assédio sexual. |
| `SEX_ESTUPR` | String | Violência sexual: estupro. |
| `SEX_PUDOR` | String | Violência sexual: atentado violento ao pudor. |
| `SEX_PORNO` | String | Violência sexual: pornografia infantil. |
| `SEX_EXPLO` | String | Violência sexual: exploração sexual. |
| `SEX_OUTRO` | String | Violência sexual: outra (descrição em `SEX_ESPEC`). |
| `LESAO_NAT` | String | Natureza da lesão. |
| `LESAO_CORP` | String | Parte do corpo atingida. |
| `NUM_ENVOLV` | String | Número de envolvidos. |
| `REL_PAI` | String | Autor: pai. |
| `REL_MAE` | String | Autor: mãe. |
| `REL_PAD` | String | Autor: padrasto. |
| `REL_CONJ` | String | Autor: cônjuge. |
| `REL_EXCON` | String | Autor: ex-cônjuge. |
| `REL_NAMO` | String | Autor: namorado(a). |
| `REL_EXNAM` | String | Autor: ex-namorado(a). |
| `REL_FILHO` | String | Autor: filho(a). |
| `REL_DESCO` | String | Autor: desconhecido. |
| `REL_IRMAO` | String | Autor: irmão(ã). |
| `REL_CONHEC` | String | Autor: amigo/conhecido. |
| `REL_CUIDA` | String | Autor: cuidador(a). |
| `REL_PATRAO` | String | Autor: patrão/chefe. |
| `REL_INST` | String | Autor: pessoa com relação institucional. |
| `REL_POL` | String | Autor: policial/agente da lei. |
| `REL_PROPRI` | String | Autor: próprio. |
| `REL_OUTROS` | String | Autor: outro vínculo (descrição em `REL_ESPEC`). |
| `AUTOR_SEXO` | String | Sexo do provável autor. |
| `AUTOR_ALCO` | String | Suspeita de uso de álcool pelo provável autor. |
| `ENC_SAUDE` | String | Encaminhamento: rede de saúde. |
| `ENC_TUTELA` | String | Encaminhamento: conselho tutelar. |
| `ENC_DEAM` | String | Encaminhamento: delegacia da mulher (DEAM). |
| `ENC_DELEG` | String | Encaminhamento: delegacia. |
| `ENC_MPU` | String | Encaminhamento: Ministério Público. |
| `ENC_CREAS` | String | Encaminhamento: CREAS. |
| `ENC_IML` | String | Encaminhamento: IML. |
| `ENC_OUTR` | String | Encaminhamento: outros (descrição em `ENC_ESPEC`). |
| `REL_TRAB` | String | Violência relacionada ao trabalho. |
| `CIRC_LESAO` | String | Circunstância da lesão (CID-10, causa externa). |
| `CLASSI_FIN` | String | Classificação final do caso. |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito, quando aplicável. |
| `REL_MAD` | String | Autor: madrasta. |
| `TPUNINOT` | String | Tipo de unidade notificadora. |
| `ORIENT_SEX` | String | Orientação sexual. |
| `IDENT_GEN` | String | Identidade de gênero. |
| `VIOL_MOTIV` | String | Motivação da violência. |
| `CICL_VID` | String | Ciclo de vida. |
| `DT_ENCERRA` | Data (AAAAMMDD) | Data de encerramento da investigação. |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios (`ID_MUNICIP`, `ID_MN_RESI`) usam código IBGE de 6 dígitos; `ID_UNIDADE` é CNES de 7 dígitos; `SG_UF_NOT` é código IBGE de 2 dígitos. `ID_AGRAVO` (CID-10), devem ficar como `String`, mantendo zeros à esquerda (`zfill`).
- **Datas e competências**: datas `DT_*` são gravadas em `AAAAMMDD` nos DBF e convertidas para `pl.Date`; `SEM_NOT` é semana epidemiológica `AAAASS` e permanece texto. A idade em `NU_IDADE_N` está codificada (`TNNN`) e deve ser decodificada antes de calcular faixas etárias.
- **Valores ausentes e sentinelas**: o SINAN usa `9`, `99`, `999` e `I` (ignorado) como categorias válidas; elas **não** são nulos automáticos. Espaços em branco e `""` viram nulos, e registros marcados como excluídos no dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: os campos de forma de violência são múltiplos (uma ficha pode ter mais de uma marcada) e devem ser tratados como flags independentes; a presença de `LES_AUTOP` distingue violência autoprovocada de interpessoal. A notificação depende de atendimento em serviço de saúde, o que implica subnotificação importante, especialmente em violência psicológica e em áreas sem rede de proteção estruturada. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. O arquivo de 2025 é preliminar; como `NU_NOTIFIC` não consta dos arquivos públicos, deduplique por combinação de campos (ex.: `ID_UNIDADE`, `DT_NOTIFIC`, `ID_MN_RESI`, `ANO_NASC`, `CS_SEXO`) ao combinar as fontes.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-viol
quantilica datasus list sinan-viol

# 2. Baixar microdados de sinan-viol (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-viol -o ./data --start 2015 --end 2022 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-viol -o ./data --docs --aux --start 2015 --end 2022 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-viol -o ./data/raw --parquet-dir ./data/parquet --start 2015 --end 2022 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/VIOLBR22.dbc", dataset="sinan-viol")

# Notificações por UF e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Formas de violência mais notificadas
print(frame.group_by("viol_fisic").agg(pl.len().alias("n")).sort("n", descending=True))
print(frame.group_by("viol_sexu").agg(pl.len().alias("n")).sort("n", descending=True))
print(resumo.head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (Violência Interpessoal/Autoprovocada): https://portalsinan.saude.gov.br/
- VIVA — Vigilância de Violências e Acidentes (SVSA/MS): https://www.gov.br/saude/pt-br/composicao/svsa/vigilancia-de-violencias-e-acidentes-viva
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Violências: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
