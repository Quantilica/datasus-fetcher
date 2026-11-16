---
dataset:
  id: base-territorial
  fonte: datasus
  titulo: Base Territorial
  resumo: 'Base Territorial do DATASUS: uma entidade territorial (tabelas `tb_*`) ou um vínculo município–recorte (tabelas `rl_*`).'
  orgao: Ministério da Saúde — DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/territorio/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: por versão publicada (sem periodicidade regular)
  cobertura:
    inicio: '2023'
    fim: em-curso
  unidade: uma entidade territorial (tabelas `tb_*`) ou um vínculo município–recorte (tabelas `rl_*`)
  granularidade:
    espacial: UF e município
    temporal: versão (mês de publicação)
  formato_bruto: ZIP
  lake:
    estado: parcial
    particoes: []
    chave: []
    colunas: null
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Base Territorial (`base-territorial`)

## Resumo

O `base-territorial` contém as **tabelas territoriais de referência** do DATASUS, que descrevem a divisão político-administrativa e sanitária do Brasil: unidades da federação, municípios, regiões e microrregiões de saúde, macrorregiões, regiões metropolitanas, distritos sanitários, territórios da cidadania e a relação entre municípios e cada um desses recortes. Cada registro (linha) é uma entidade territorial ou um vínculo município–recorte, em uma **versão mensal** do cadastro. É a base de apoio para padronizar e cruzar códigos territoriais usados em todos os sistemas de informação do SUS.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.zip` (contendo tabelas `.dbf`, `.csv`, `.xml` e `.txt` de layout)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `version` (versão mensal, ex.: `2026-06`)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): Versões mensais; versão mais recente `2026-06` (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 21 arquivos versionados (~33 MB)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/territorio/doc` (`bases_territoriais.pdf`, `registro_de_alteracoes.pdf`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/territorio/tabelas` | (vazio) | `<MM>-base_territorial_<mês><AA>.zip` (por versão mensal) | `zip` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `06-base_territorial_jun26.zip` (em `/territorio/tabelas/2026/`) — `06` é o mês, `base_territorial` o assunto, `jun26` o mês abreviado e ano. Dentro do ZIP há os arquivos `tb_*.dbf/csv/xml/txt` e `rl_*.dbf/csv/xml/txt` e os respectivos `*_layout.txt` (definição de colunas).
- **No armazenamento local do `datasus-fetcher`**: como o particionamento é por versão, o arquivo vai para `data/base-territorial/base-territorial_<versão>@<AAAAMMDD>.zip`, por exemplo `data/base-territorial/base-territorial_2026-06@20260624.zip`.
- **Documentação e Tabelas Auxiliares associadas**: em `/territorio/doc` estão `bases_territoriais.pdf` (descrição das tabelas e relacionamentos) e `registro_de_alteracoes.pdf` (histórico de mudanças). Não há pacote de auxiliares separado — as tabelas territoriais são o próprio conteúdo do ZIP.

## Conteúdo

A Base Territorial é mantida pelo **Ministério da Saúde/DATASUS** e consolida, em um formato único e versionado, a divisão territorial usada pelos sistemas de informação em saúde. Ela reúne tabelas de **domínio territorial** (`tb_*`), como `tb_uf`, `tb_municip`, `tb_regiao`, `tb_regsaud`, `tb_macsaud`, `tb_regmetr`, `tb_micibge`, `tb_divadm`, `tb_pndr`, `tb_dsei` e `tb_terrcid`, e tabelas de **relacionamento** (`rl_*`) que associam cada município aos recortes aos quais pertence.

O **evento gerador** é a atualização periódica (mensal) do cadastro territorial quando há criação, extinção ou alteração de municípios e mudanças nos recortes de saúde (regiões/macrorregiões de saúde, regiões metropolitanas, PNDR, territórios da cidadania). A **unidade de análise varia conforme a tabela**: para `tb_*`, é uma entidade territorial (ex.: um município em `tb_municip`); para `rl_*`, é um vínculo (ex.: a associação `CO_MUNICIP` → `CO_REGSAUD`). A competência mês/ano aparece no nome do arquivo e nos metadados da versão.

A série é **versionada por competência** (não é uma série histórica de dados, e sim sucessivas versões do cadastro). As versões são organizadas por ano em `/territorio/tabelas/<ano>/`, com o nome `MM-base_territorial_<mês><AA>.zip`. O documento `registro_de_alteracoes.pdf` registra as mudanças entre versões. Não há diretório preliminar.

Aplicações analíticas típicas: padronização de códigos de município (6 e 7 dígitos) e de UF, enriquecimento de bases de saúde com atributos territoriais (capital, Amazônia Legal, semiárido, faixa de fronteira, município de extrema pobreza), mapeamento de municípios para regiões de saúde e macrorregiões, e construção de agregações regionais para indicadores.

### Variáveis de uso mais frequente (resumo da versão anterior desta página)

| Tabela (DBF) | Coluna | Tipo / Formato | Descrição |
|---|---|---|---|
| `tb_municip` | `CO_MUNICIP` | String (6) | Código IBGE do município (sem dígito verificador) |
| `tb_municip` | `CO_MUNICDV` | String (7) | Código IBGE do município (com dígito verificador) |
| `tb_municip` | `CO_UF` / `CO_REGIAO` | String (2/1) | UF e macrorregião do município |
| `tb_municip` | `IN_CAPITAL` / `IN_AMAZLEG` / `IN_SEMIAR` | String (1) | Indicadores: capital, Amazônia Legal, semiárido |
| `tb_municip` | `NU_LATITUD` / `NU_LONGIT` / `NU_AREA` | Float | Latitude, longitude, altitude e área do município |
| `tb_uf` | `CO_UF` / `DS_SIGLA` / `DS_NOME` | String | Código, sigla e nome da UF |
| `tb_regsaud` / `tb_macsaud` | `CO_REGSAUD` / `CO_MACSAUD`, `DS_NOME` | String | Região e macrorregião de saúde |
| `rl_municip_regsaud` | `CO_MUNICIP`, `CO_REGSAUD` | String | Relacionamento município → região de saúde |
| `rl_municip_macsaud` | `CO_MUNICIP`, `CO_MACSAUD` | String | Relacionamento município → macrorregião de saúde |
| `rl_municip_divadm` | `CO_MUNICIP`, `CO_DIVADM` | String | Relacionamento município → divisão administrativa estadual |
| `tb_divadm` / `tb_dsei` | `CO_DIVADM` / `CO_DSEI`, `DS_NOME` | String | Divisão administrativa estadual / distrito sanitário especial indígena |

## Variáveis

O ZIP mais recente da base territorial vira um dataset do lake por tabela (`base-territorial-<tabela>`, com `_` trocado por `-`). Cada tabela abaixo tem o dicionário das colunas do lake (esquema de amostra: `base-territorial-tb-municip` e demais, versão 2026-06 do ZIP).

### Tabela `rl_municip_divadm` (dataset `base-territorial-rl-municip-divadm`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_municip` | `CO_MUNICIP` | texto | Código IBGE do município, sem o dígito de controle (6 dígitos) | — | todos |
| `co_divadm` | `CO_DIVADM` | texto | Código da divisão administrativa estadual | — | todos |

### Tabela `rl_municip_dsei` (dataset `base-territorial-rl-municip-dsei`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_municip` | `CO_MUNICIP` | texto | Código IBGE do município, sem o dígito de controle (6 dígitos) | — | todos |
| `co_dsei` | `CO_DSEI` | texto | Código do Distrito Sanitário Especial Indígena (DSEI) | — | todos |

### Tabela `rl_municip_macsaud` (dataset `base-territorial-rl-municip-macsaud`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_municip` | `CO_MUNICIP` | texto | Código IBGE do município, sem o dígito de controle (6 dígitos) | — | todos |
| `co_macsaud` | `CO_MACSAUD` | texto | Código da macrorregião de saúde | — | todos |

### Tabela `rl_municip_micibge` (dataset `base-territorial-rl-municip-micibge`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_municip` | `CO_MUNICIP` | texto | Código IBGE do município, sem o dígito de controle (6 dígitos) | — | todos |
| `co_micibge` | `CO_MICIBGE` | texto | Código da microrregião do IBGE | — | todos |

### Tabela `rl_municip_pndr` (dataset `base-territorial-rl-municip-pndr`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_municip` | `CO_MUNICIP` | texto | Código IBGE do município, sem o dígito de controle (6 dígitos) | — | todos |
| `co_pndr` | `CO_PNDR` | texto | Código do recorte da Política Nacional de Desenvolvimento Regional (PNDR) | — | todos |

### Tabela `rl_municip_regmetr` (dataset `base-territorial-rl-municip-regmetr`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_municip` | `CO_MUNICIP` | texto | Código IBGE do município, sem o dígito de controle (6 dígitos) | — | todos |
| `co_regmet` | `CO_REGMET` | texto | Código da região metropolitana | — | todos |

### Tabela `rl_municip_regsaud` (dataset `base-territorial-rl-municip-regsaud`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_municip` | `CO_MUNICIP` | texto | Código IBGE do município, sem o dígito de controle (6 dígitos) | — | todos |
| `co_regsaud` | `CO_REGSAUD` | texto | Código da região de saúde | — | todos |

### Tabela `rl_municip_terrcid` (dataset `base-territorial-rl-municip-terrcid`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_municip` | `CO_MUNICIP` | texto | Código IBGE do município, sem o dígito de controle (6 dígitos) | — | todos |
| `co_terrcid` | `CO_TERRCID` | texto | Código do território da cidadania | — | todos |

### Tabela `rl_regsaud_macsaud` (dataset `base-territorial-rl-regsaud-macsaud`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_regsaud` | `CO_REGSAUD` | texto | Código da região de saúde | — | todos |
| `co_macrorr` | `CO_MACRORR` | texto | Código da macrorregião de saúde ao qual a região de saúde pertence | — | todos |

### Tabela `tb_divadm` (dataset `base-territorial-tb-divadm`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_divadm` | `CO_DIVADM` | texto | Código da divisão administrativa estadual | — | todos |
| `co_status` | `CO_STATUS` | texto | Situação do registro (por exemplo, ATIVO, EXTINT, TRANSF ou IGNOR) | — | todos |
| `ds_nome` | `DS_NOME` | texto | Nome do registro | — | todos |
| `ds_nomepad` | `DS_NOMEPAD` | texto | Nome padronizado, sem acentuação e em letras maiúsculas | — | todos |
| `ds_abrev` | `DS_ABREV` | texto | Nome abreviado | — | todos |
| `nu_ordem` | `NU_ORDEM` | texto | Ordem de apresentação do registro nos arquivos de conversão | — | todos |

### Tabela `tb_divadmant` (dataset `base-territorial-tb-divadmant`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_divadm` | `CO_DIVADM` | texto | Código da divisão administrativa estadual | — | todos |
| `co_status` | `CO_STATUS` | texto | Situação do registro (por exemplo, ATIVO, EXTINT, TRANSF ou IGNOR) | — | todos |
| `ds_nome` | `DS_NOME` | texto | Nome do registro | — | todos |
| `ds_nomepad` | `DS_NOMEPAD` | texto | Nome padronizado, sem acentuação e em letras maiúsculas | — | todos |
| `ds_abrev` | `DS_ABREV` | texto | Nome abreviado | — | todos |
| `nu_ordem` | `NU_ORDEM` | texto | Ordem de apresentação do registro nos arquivos de conversão | — | todos |

### Tabela `tb_dsei` (dataset `base-territorial-tb-dsei`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_dsei` | `CO_DSEI` | texto | Código do Distrito Sanitário Especial Indígena (DSEI) | — | todos |
| `ds_nome` | `DS_NOME` | texto | Nome do registro | — | todos |
| `ds_nomepad` | `DS_NOMEPAD` | texto | Nome padronizado, sem acentuação e em letras maiúsculas | — | todos |
| `co_sede` | `CO_SEDE` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |

### Tabela `tb_macsaud` (dataset `base-territorial-tb-macsaud`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_macsaud` | `CO_MACSAUD` | texto | Código da macrorregião de saúde | — | todos |
| `co_status` | `CO_STATUS` | texto | Situação do registro (por exemplo, ATIVO, EXTINT, TRANSF ou IGNOR) | — | todos |
| `ds_nome` | `DS_NOME` | texto | Nome do registro | — | todos |
| `ds_nomepad` | `DS_NOMEPAD` | texto | Nome padronizado, sem acentuação e em letras maiúsculas | — | todos |
| `ds_abrev` | `DS_ABREV` | texto | Nome abreviado | — | todos |
| `nu_ordem` | `NU_ORDEM` | texto | Ordem de apresentação do registro nos arquivos de conversão | — | todos |

### Tabela `tb_micibge` (dataset `base-territorial-tb-micibge`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_micibge` | `CO_MICIBGE` | texto | Código da microrregião do IBGE | — | todos |
| `co_status` | `CO_STATUS` | texto | Situação do registro (por exemplo, ATIVO, EXTINT, TRANSF ou IGNOR) | — | todos |
| `ds_nome` | `DS_NOME` | texto | Nome do registro | — | todos |
| `ds_nomepad` | `DS_NOMEPAD` | texto | Nome padronizado, sem acentuação e em letras maiúsculas | — | todos |
| `ds_abrev` | `DS_ABREV` | texto | Nome abreviado | — | todos |
| `nu_ordem` | `NU_ORDEM` | texto | Ordem de apresentação do registro nos arquivos de conversão | — | todos |

### Tabela `tb_mis` (dataset `base-territorial-tb-mis`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_mis` | `CO_MIS` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `nome_mis` | `NOME_MIS` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `co_munic_i` | `CO_MUNIC_I` | texto | Sem descrição na documentação oficial consultada; o nome é o do campo no arquivo de origem | — | todos |
| `nu_ordem` | `NU_ORDEM` | texto | Ordem de apresentação do registro nos arquivos de conversão | — | todos |

### Tabela `tb_municip` (dataset `base-territorial-tb-municip`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_municip` | `CO_MUNICIP` | texto | Código IBGE do município, sem o dígito de controle (6 dígitos) | — | todos |
| `co_municdv` | `CO_MUNICDV` | texto | Código IBGE do município, com o dígito de controle (7 dígitos) | — | todos |
| `co_status` | `CO_STATUS` | texto | Situação do registro (por exemplo, ATIVO, EXTINT, TRANSF ou IGNOR) | — | todos |
| `co_tipo` | `CO_TIPO` | texto | Tipo da unidade (por exemplo, MUNIC, DISFED, DISEST, TERRIT ou IGNOR em municípios) | — | todos |
| `ds_nome` | `DS_NOME` | texto | Nome do registro | — | todos |
| `uf` | `UF` | texto | UF do município (sigla ou código, conforme a versão do arquivo) (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `macrorregi` | `MACRORREGI` | texto | Macrorregião (do IBGE) do município (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |
| `ds_nomepad` | `DS_NOMEPAD` | texto | Nome padronizado, sem acentuação e em letras maiúsculas | — | todos |
| `ds_observ` | `DS_OBSERV` | texto | Observações (nome antigo, situação da transferência etc.) | — | todos |
| `co_regiao` | `CO_REGIAO` | texto | Código da região do país em que o registro está localizado | — | todos |
| `co_uf` | `CO_UF` | texto | Código da unidade da federação (2 dígitos, padrão IBGE) | — | todos |
| `co_alter` | `CO_ALTER` | texto | Códigos alternativos usados para o município, separados por vírgula ou em faixa | — | todos |
| `co_alterdv` | `CO_ALTERDV` | texto | Códigos alternativos, com o dígito verificador | — | todos |
| `in_capital` | `IN_CAPITAL` | texto | Capital: F federal; E estadual; N não é capital | — | todos |
| `in_amazleg` | `IN_AMAZLEG` | texto | Faz parte da Amazônia Legal (S ou N) | — | todos |
| `in_semiar` | `IN_SEMIAR` | texto | Faz parte do Semiárido (S ou N) | — | todos |
| `in_frontzn` | `IN_FRONTZN` | texto | Faz parte da zona de fronteira (S ou N) | — | todos |
| `dt_instal` | `DT_INSTAL` | texto | Ano de instalação do município (não disponível para todos) | — | todos |
| `dt_extin` | `DT_EXTIN` | texto | Ano de extinção ou transferência do município | — | todos |
| `co_sucess` | `CO_SUCESS` | texto | Código do registro sucessor ao extinto ou transferido | — | todos |
| `nu_ordem` | `NU_ORDEM` | texto | Ordem de apresentação do registro nos arquivos de conversão | — | todos |
| `nu_ordmap` | `NU_ORDMAP` | texto | Ordem de apresentação do registro nos arquivos de conversão para mapas | — | todos |
| `nu_latitud` | `NU_LATITUD` | texto | Latitude da sede do município | — | todos |
| `nu_longit` | `NU_LONGIT` | texto | Longitude da sede do município | — | todos |
| `nu_altitud` | `NU_ALTITUD` | texto | Altitude, em metros, da sede do município | — | todos |
| `nu_area` | `NU_AREA` | texto | Área, em quilômetros quadrados | — | todos |

### Tabela `tb_pndr` (dataset `base-territorial-tb-pndr`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_pndr` | `CO_PNDR` | texto | Código do recorte da Política Nacional de Desenvolvimento Regional (PNDR) | — | todos |
| `ds_nome` | `DS_NOME` | texto | Nome do registro | — | todos |
| `ds_nomepad` | `DS_NOMEPAD` | texto | Nome padronizado, sem acentuação e em letras maiúsculas | — | todos |
| `co_status` | `CO_STATUS` | texto | Situação do registro (por exemplo, ATIVO, EXTINT, TRANSF ou IGNOR) | — | todos |
| `nu_ordmap` | `NU_ORDMAP` | inteiro | Ordem de apresentação do registro nos arquivos de conversão para mapas | — | todos |

### Tabela `tb_regiao` (dataset `base-territorial-tb-regiao`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_regiao` | `CO_REGIAO` | texto | Código da região do país em que o registro está localizado | — | todos |
| `no_regiao` | `NO_REGIAO` | texto | Nome da região do país | — | todos |
| `sg_regiao` | `SG_REGIAO` | texto | Sigla da região do país | — | todos |
| `st_registr` | `ST_REGISTR` | texto | Situação do registro da região (inferido do nome do campo; sem definição na documentação oficial consultada) | — | todos |

### Tabela `tb_regmetr` (dataset `base-territorial-tb-regmetr`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_regmetr` | `CO_REGMETR` | texto | Código da região metropolitana | — | todos |
| `co_status` | `CO_STATUS` | texto | Situação do registro (por exemplo, ATIVO, EXTINT, TRANSF ou IGNOR) | — | todos |
| `co_tipo` | `CO_TIPO` | texto | Tipo da unidade (por exemplo, MUNIC, DISFED, DISEST, TERRIT ou IGNOR em municípios) | — | todos |
| `ds_nome` | `DS_NOME` | texto | Nome do registro | — | todos |
| `ds_nomepad` | `DS_NOMEPAD` | texto | Nome padronizado, sem acentuação e em letras maiúsculas | — | todos |
| `ds_abrev` | `DS_ABREV` | texto | Nome abreviado | — | todos |
| `nu_ordem` | `NU_ORDEM` | texto | Ordem de apresentação do registro nos arquivos de conversão | — | todos |

### Tabela `tb_regsaud` (dataset `base-territorial-tb-regsaud`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_regsaud` | `CO_REGSAUD` | texto | Código da região de saúde | — | todos |
| `co_status` | `CO_STATUS` | texto | Situação do registro (por exemplo, ATIVO, EXTINT, TRANSF ou IGNOR) | — | todos |
| `ds_nome` | `DS_NOME` | texto | Nome do registro | — | todos |
| `ds_nomepad` | `DS_NOMEPAD` | texto | Nome padronizado, sem acentuação e em letras maiúsculas | — | todos |
| `ds_abrev` | `DS_ABREV` | texto | Nome abreviado | — | todos |
| `nu_ordem` | `NU_ORDEM` | texto | Ordem de apresentação do registro nos arquivos de conversão | — | todos |

### Tabela `tb_terrcid` (dataset `base-territorial-tb-terrcid`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_terrcid` | `CO_TERRCID` | texto | Código do território da cidadania | — | todos |
| `ds_nome` | `DS_NOME` | texto | Nome do registro | — | todos |
| `ds_nomepad` | `DS_NOMEPAD` | texto | Nome padronizado, sem acentuação e em letras maiúsculas | — | todos |
| `co_status` | `CO_STATUS` | texto | Situação do registro (por exemplo, ATIVO, EXTINT, TRANSF ou IGNOR) | — | todos |
| `nu_ordmap` | `NU_ORDMAP` | inteiro | Ordem de apresentação do registro nos arquivos de conversão para mapas | — | todos |

### Tabela `tb_uf` (dataset `base-territorial-tb-uf`)

| Coluna no lake | Na fonte | Tipo | Descrição | Unidade / códigos | Período |
|---|---|---|---|---|---|
| `co_uf` | `CO_UF` | texto | Código da unidade da federação (2 dígitos, padrão IBGE) | — | todos |
| `ds_sigla` | `DS_SIGLA` | texto | Sigla da unidade da federação | — | todos |
| `co_status` | `CO_STATUS` | texto | Situação do registro (por exemplo, ATIVO, EXTINT, TRANSF ou IGNOR) | — | todos |
| `ds_nome` | `DS_NOME` | texto | Nome do registro | — | todos |
| `ds_nomepad` | `DS_NOMEPAD` | texto | Nome padronizado, sem acentuação e em letras maiúsculas | — | todos |
| `co_sucess` | `CO_SUCESS` | texto | Código do registro sucessor ao extinto ou transferido | — | todos |
| `co_regiao` | `CO_REGIAO` | texto | Código da região do país em que o registro está localizado | — | todos |
| `nu_area` | `NU_AREA` | texto | Área, em quilômetros quadrados | — | todos |

## No lake

- **Estado `parcial`:** os datasets do lake são `datasus/base-territorial-<tabela>` (não há `datasus/base-territorial`). Só o ZIP de carimbo mais recente é convertido; as versões anteriores são ignoradas (`superado` no inventário).
- Cada tabela é gravada sem partição, com a coluna `uf` e a `_origem` ausentes (tabelas de domínio). Tipos: as amostras da conversão mostram todas as colunas como texto (`large_string`) e `nu_ordmap` das tabelas `pndr` e `terrcid` como inteiro; nas tabelas em DBF os tipos vêm declarados, nas em CSV tudo vem como texto.
- Esquemas de referência: não há `base-territorial.schema.json`, porque o id declarado pelo conversor (`base-territorial`) não existe como dataset do lake; o esquema de cada tabela fica nos arquivos `base-territorial-<tabela>.schema.json` desta pasta.

## Cuidados de uso

- Misturar versões do ZIP gera inconsistências; fixe uma versão (texto da versão anterior desta página).
- O conversor lê só a versão mais recente: se a análise precisar de uma versão específica, converta o ZIP dela separadamente.

## Exemplos

### Consulta sobre o lake (polars)

Quantos municípios ativos há por UF na base territorial?

```python
import polars as pl

(
    pl.scan_parquet("lake/datasus/base-territorial-tb-municip/*.parquet")
    .filter(pl.col("co_status") == "ATIVO")
    .group_by("co_uf")
    .agg(pl.len().alias("municipios"))
    .sort("co_uf")
    .collect()
)
```

### Pela linha de comando (`datasus-fetcher`)

```bash
# o que o FTP publica para o dataset (arquivos e tamanho)
datasus-fetcher list base-territorial

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync base-territorial -o ./data --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset base-territorial
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/territorio/tabelas`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **Documentação `bases_territoriais.pdf` e `registro_de_alteracoes.pdf`**: `ftp://ftp.datasus.gov.br/territorio/doc`
- **IBGE — Divisão Político-Administrativa e malha territorial**: https://www.ibge.gov.br/geociencias/organizacao-do-territorio.html
- **PCDaS/Fiocruz — Bases territoriais**: https://pcdas.icict.fiocruz.br/
