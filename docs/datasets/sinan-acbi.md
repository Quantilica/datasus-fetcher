# `sinan-acbi` — Acidente de trabalho com material biológico

Notificações de acidentes de trabalho em que o trabalhador foi exposto, de forma direta ou indireta, a material biológico (orgânico) potencialmente contaminado por patógenos, registradas no SINAN. Cada linha representa uma ficha de investigação de acidente com material biológico, alimentada por serviços de saúde públicos e privados de todos os portes.

## Ficha Técnica

| Atributo | Valor |
|---|---|
| **Sistema / Grupo** | `sinan` — SINAN: Sistema de Informação de Agravos de Notificação |
| **Código no `datasus-fetcher`** | `sinan-acbi` |
| **Formato dos arquivos** | `.dbc` (dBASE comprimido) |
| **Particionamento** | `uf`, `year` (no FTP há apenas arquivos nacionais `BR`: `partition_n_ufs` = 1) |
| **Periodicidade** | Anual |
| **Cobertura temporal no FTP** | 2006 a 2026 (conforme `index.json`) |
| **Volume aproximado no FTP** | 21 arquivos (~54,1 MB) |
| **Arquivos preliminares** | Sim (diretório PRELIM, 2023–2026; Finais até 2022) |
| **Documentação oficial no FTP** | `/dissemin/publicos/SINAN/DOCS` |
| **Tabelas auxiliares no FTP** | `/dissemin/publicos/SINAN/AUXILIAR` |

## 1. Contexto Institucional e Epidemiológico

O agravo integra a vigilância em Saúde do Trabalhador do Sistema Único de Saúde, coordenada pela Secretaria de Vigilância em Saúde e Ambiente (SVSA/MS) por meio da Coordenação-Geral de Vigilância em Saúde do Trabalhador e da Trabalhadora. A notificação compulsória dos acidentes com exposição a material biológico foi estabelecida pela Portaria MS nº 777/2004 e consolidada pela Portaria de Consolidação nº 4/2017 (Anexo V), operacionalizada na Rede Nacional de Atenção Integral à Saúde do Trabalhador (RENAST) e nos Centros de Referência em Saúde do Trabalhador (CEREST).

O evento gerador é o acidente de trabalho com exposição percutânea, mucosa, pele íntegra ou não íntegra a sangue e outros fluidos orgânicos, por material perfurocortante ou não; a unidade de análise é o trabalhador acidentado notificado (um registro por ficha), independentemente do vínculo empregatício. O instrumento é a *Ficha de Investigação — Acidente de Trabalho com Exposição à Material Biológico* (CID-10 Z20.9), que cobre dados gerais, notificação individual, residência, antecedentes epidemiológicos (ocupação, situação no mercado de trabalho, tempo na ocupação), dados da empresa contratante (CNAE, CNPJ/CPF) e dados específicos do acidente e do paciente-fonte.

A série publicada no FTP inicia em 2006, com implantação nacional do Sinan Net. Os arquivos de 2023 a 2026 estão no diretório PRELIM (dados preliminares, sujeitos a revisão até o fechamento), enquanto as competências até 2022 estão em FINAIS. Por ser uma base sentinela da RENAST, a cobertura depende da capilaridade dos serviços notificadores, com subnotificação conhecida em estados menos estruturados.

Principais usos: perfil de exposição ocupacional por categoria profissional e CBO, avaliação de adesão a protocolos de profilaxia pós-exposição (HIV, hepatites B e C), monitoramento de uso de EPI, acompanhamento sorológico e cálculo de taxas de incidência de acidentes biológicos em profissionais de saúde.

## 2. Metadados Técnicos no FTP DATASUS

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/dissemin/publicos/SINAN/DADOS/FINAIS` | `ACBI` | UF + AA (`uf_year2_pattern`) | `dbc` | Não |
| `/dissemin/publicos/SINAN/DADOS/PRELIM` | `ACBI` | UF + AA (`uf_year2_pattern`) | `dbc` | Sim |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo `ACBIBR24.dbc`, em que `ACBI` é o prefixo do agravo, `BR` indica a base nacional (o SINAN publica um único arquivo por ano para o Brasil) e `24` é o ano com 2 dígitos (2024, preliminar).
- **No armazenamento local do `datasus-fetcher`**: `data/sinan-acbi/<partição>/sinan-acbi_br_2006_<AAAAMMDD>.dbc`, em que `<AAAAMMDD>` é a data de modificação do arquivo no FTP; arquivos preliminares seguem a mesma árvore, diferenciados pelo diretório de origem.
- **Documentação e tabelas auxiliares associadas** (grupo `sinan`, compartilhadas por todos os agravos):
  - Documentação (`/SINAN/DOCS`):
    - `Docs_TAB_SINAN.zip` — pacote de documentação e dicionários para tabulação (~65 MB)
    - `POP_I_Acesso_a_Microdados_5.pdf` — POP I: acesso a microdados
    - `POP_II_Descompactacao_expansao_conversao_3.pdf` — POP II: descompactação, expansão e conversão (.dbc → .dbf)
    - `POP_III_Instalacao_do_tabulador_TabWin_3.pdf` — POP III: instalação do TabWin
    - `Nota_Tecnica_Doenca_de_Creutzfeldt-Jakob(DCJ).pdf` — nota técnica sobre DCJ
  - Tabelas auxiliares (`/SINAN/AUXILIAR`):
    - `TAB_SINANNET.zip` — tabelas de conversão/tabulação (.cnv, .def) do SINAN Net (~44 MB)
    - `TAB_SINANONLINE.zip` — tabelas do SINAN Online (~240 KB)
    - `POPT_Estimativa_TCU_2019_Sinan.zip` — estimativas populacionais TCU 2019 para uso no SINAN
  - O dicionário desta base (`DRT Acidente Trabalho Biológico`) é distribuído no Portal SINAN e referenciado em `Docs_TAB_SINAN.zip`; não há PDF por agravo no FTP.

## 3. Principais Variáveis e Qualidade dos Dados

### Variáveis-Chave dos Microdados

Os nomes de coluna abaixo foram verificados diretamente no cabeçalho do arquivo `ACBIBR10.dbc` (leiaute do SINAN Net; fichas e leiautes podem variar entre anos, por isso a lista reflete esse arquivo). Os arquivos públicos não trazem identificadores individuais como número da notificação (`NU_NOTIFIC`) nem data de nascimento completa. Por padrão, `wrangle_datasus` converte os nomes de coluna para minúsculas.

| Coluna (DBF) | Tipo / Formato | Descrição |
|---|---|---|
| `TP_NOT` | String | Tipo de notificação (registro da ficha de notificação individual). |
| `ID_AGRAVO` | String | Código CID-10 do agravo notificado. |
| `DT_NOTIFIC` | Data (AAAAMMDD) | Data da notificação. |
| `SEM_NOT` | String | Semana epidemiológica da notificação (AAAASS). |
| `NU_ANO` | String | Ano da notificação. |
| `SG_UF_NOT` | String | UF de notificação (código IBGE de 2 dígitos). |
| `ID_MUNICIP` | String | Município de notificação (código IBGE). |
| `ID_UNIDADE` | String | Código CNES da unidade de saúde notificadora (7 dígitos). |
| `DT_ACID` | Data (AAAAMMDD) | Data do acidente. |
| `SEM_ACID` | String | Semana epidemiológica do acidente (AAAASS). |
| `ANO_NASC` | String | Ano de nascimento (o arquivo público não traz a data de nascimento completa). |
| `NU_IDADE_N` | Inteiro | Idade no formato `TNNN`: primeiro dígito = unidade (1 hora, 2 dia, 3 mês, 4 ano) e três dígitos = valor. |
| `CS_SEXO` | String | Sexo (M, F, I = ignorado). |
| `CS_RACA` | String | Raça/cor (1 branca, 2 preta, 3 amarela, 4 parda, 5 indígena, 9 ignorado). |
| `CS_ESCOL_N` | String | Escolaridade. |
| `SG_UF` | String | UF de residência (código IBGE de 2 dígitos). |
| `ID_MN_RESI` | String | Município de residência (código IBGE, 6 dígitos). |
| `ID_OCUPA_N` | String | Ocupação do trabalhador (CBO 2002, 6 dígitos). |
| `SIT_TRAB` | String | Situação no mercado de trabalho. |
| `CNAE` | String | Atividade econômica da empresa contratante (CNAE). |
| `PERCUTANEA` | String | Exposição percutânea (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `PELE_INTEG` | String | Exposição em pele íntegra (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `PELE_NAO_I` | String | Exposição em pele não íntegra (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `OUTRO_EXP` | String | Outro tipo de exposição (descrição em `OUT_EXP_DE`). |
| `MAT_ORG` | String | Material orgânico envolvido (descrição de outros em `MAT_ORG_DE`). |
| `TIPO_ACID` | String | Circunstância do acidente. |
| `AGENTE` | String | Agente (objeto) causador do acidente. |
| `LUVA` | String | Uso de luvas (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `AVENTAL` | String | Uso de avental (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `OCULOS` | String | Uso de óculos (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `MASCARA` | String | Uso de máscara (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `FACIAL` | String | Uso de protetor facial (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `BOTA` | String | Uso de botas (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `VACINA` | String | Trabalhador vacinado contra hepatite B. |
| `ANTI_HIV` | String | Resultado do anti-HIV do trabalhador no momento do acidente. |
| `HBSAG` | String | Resultado do HBsAg do trabalhador. |
| `ANTI_HBS` | String | Resultado do anti-HBs do trabalhador. |
| `ANTI_HCV` | String | Resultado do anti-HCV do trabalhador. |
| `FONTE` | String | Paciente-fonte conhecido. |
| `FO_HBSAG` | String | HBsAg do paciente-fonte. |
| `FO_ANT_HIV` | String | Anti-HIV do paciente-fonte. |
| `FO_ANT_HBC` | String | Anti-HBc do paciente-fonte. |
| `FO_ANT_HCV` | String | Anti-HCV do paciente-fonte. |
| `SEM_QUIMIO` | String | Sem quimioprofilaxia (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `RECUSA_QUI` | String | Recusa da quimioprofilaxia (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |
| `AZT3TC` | String | Esquema de quimioprofilaxia AZT+3TC. |
| `AZT3TC_IND` | String | Esquema AZT+3TC+indinavir. |
| `AZT3TC_NFV` | String | Esquema AZT+3TC+nelfinavir. |
| `IMU_HEP_B` | String | Imunoglobulina humana anti-hepatite B. |
| `VAC_HEP_B` | String | Vacinação contra hepatite B após o acidente. |
| `OUTRO_ARV` | String | Outro esquema antirretroviral (descrição em `OUT_ARV_ES`). |
| `EVOLUCAO` | String | Evolução do caso. |
| `DT_OBITO` | Data (AAAAMMDD) | Data do óbito, quando aplicável. |
| `CAT` | String | Foi emitida a Comunicação de Acidente do Trabalho (CAT)? |
| `MUCOSA` | String | Exposição em mucosa (marcação da ficha (padrão SINAN: 1 sim, 2 não, 9 ignorado)). |

### Observações de Tratamento e Saneamento (`wrangle_datasus`)

- **Preservação de códigos estruturados**: municípios (`ID_MUNICIP`, `ID_MN_RESI`) usam código IBGE de 6 dígitos; `ID_UNIDADE` é CNES de 7 dígitos; `SG_UF_NOT` é código IBGE de 2 dígitos. `ID_AGRAVO` (CID-10), `ID_OCUPA_N` (CBO 2002, 6 dígitos), `CNAE`, devem ficar como `String`, mantendo zeros à esquerda (`zfill`).
- **Datas e competências**: datas `DT_*` são gravadas em `AAAAMMDD` nos DBF e convertidas para `pl.Date`; `SEM_NOT` é semana epidemiológica `AAAASS` e permanece texto. A idade em `NU_IDADE_N` está codificada (`TNNN`) e deve ser decodificada antes de calcular faixas etárias.
- **Valores ausentes e sentinelas**: o SINAN usa `9`, `99`, `999`, `99` e `I` (ignorado) como categorias válidas no dicionário; elas **não** são nulos automáticos e a decisão de tratá-las como ausente cabe à análise. Espaços em branco e `""` viram nulos, e registros marcados como excluídos no dBASE (`_deleted`) são removidos.
- **Particularidades do dataset**: a tabela `1` do SINAN tem apenas o agravo específico, mas os campos de ocupação e CNAE podem vir incompletos em notificações de baixa qualidade; o profissional de saúde é a categoria predominante, e o `ID_OCUPA_N` deve ser agregado por grandes grupos. `ID_AGRAVO` é sempre `Z20.9`. Os arquivos `BR` reúnem todas as UFs; use `SG_UF_NOT` (notificação) ou `ID_MN_RESI` (residência) conforme a pergunta. Arquivos do diretório PRELIM (2023+) são preliminares e substituídos pelos finais; como `NU_NOTIFIC` não consta dos arquivos públicos, deduplique por combinação de campos (ex.: `ID_UNIDADE`, `DT_NOTIFIC`, `ID_MN_RESI`, `ANO_NASC`, `CS_SEXO`) ao combinar as duas fontes.

## 4. Exemplos Práticos

### Via CLI (`quantilica datasus` / `datasus-fetcher`)

```bash
# 1. Inspecionar arquivos, volume e cobertura disponíveis no FTP para sinan-acbi
quantilica datasus list sinan-acbi

# 2. Baixar microdados de sinan-acbi (partição uf + year; no SINAN a UF é sempre BR)
quantilica datasus sync sinan-acbi -o ./data --start 2020 --end 2022 --regions BR

# 3. Baixar microdados acompanhados da documentação oficial e tabelas auxiliares
quantilica datasus sync sinan-acbi -o ./data --docs --aux --start 2020 --end 2022 --regions BR

# 4. Pipeline completo: download, descompactação nativa em Rust e conversão para Parquet tratado
quantilica datasus pipeline sinan-acbi -o ./data/raw --parquet-dir ./data/parquet --start 2020 --end 2022 --regions BR
```

### Em Python e Polars

```python
import datasus_fetcher as df
import polars as pl
from datasus_fetcher.reader import read_dbc

# Leitura direta de um .dbc nacional (descompacta, lê e aplica o saneamento padrão)
frame = read_dbc("data/raw/ACBIBR22.dbc", dataset="sinan-acbi")

# Notificações por UF de notificação e ano
resumo = (
    frame.group_by("sg_uf_not", "nu_ano")
    .agg(pl.len().alias("notificacoes"))
    .sort("sg_uf_not", "nu_ano")
)

# Ocupações (CBO) mais frequentes entre os acidentados
print(frame.group_by("id_ocupa_n").agg(pl.len().alias("n")).sort("n", descending=True).head())
print(resumo.head())
```

## 5. Referências Oficiais

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/dissemin/publicos/SINAN/DADOS/`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Portal SINAN (Ministério da Saúde)**: https://portalsinan.saude.gov.br/
- Ficha e dicionário do agravo (DRT Acidente de Trabalho Biológico): https://portalsinan.saude.gov.br/
- Guia de Vigilância em Saúde (SVSA/MS), capítulo Saúde do Trabalhador: https://www.gov.br/saude/pt-br/centrais-de-conteudo/publicacoes/svsa/guia-de-vigilancia-em-saude
- Lista Nacional de Notificação Compulsória (Portaria de Consolidação nº 4/2017, Anexo V, atualizada pela Portaria GM/MS nº 217/2023 e pela Portaria GM/MS nº 5.201/2024): https://www.gov.br/saude/pt-br/composicao/svsa
- RENAST — Rede Nacional de Atenção Integral à Saúde do Trabalhador: https://www.gov.br/saude/pt-br/composicao/svsa/saude-do-trabalhador/renast
