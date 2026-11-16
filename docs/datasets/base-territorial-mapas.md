---
dataset:
  id: base-territorial-mapas
  fonte: datasus
  titulo: Base Territorial - Mapas
  resumo: 'Base Territorial - Mapas do DATASUS: um mapa digital em formato TabWin (`.MAP`), por UF e ano de referência.'
  orgao: Ministério da Saúde — DATASUS
  pagina_oficial: ftp://ftp.datasus.gov.br/territorio/
  licenca: 'Sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016 (declaração do próprio fetcher, `FetcherInfo.licenca`); os informes técnicos do DATASUS citam o art. 8º da LAI (transparência ativa): https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm'
  periodicidade: anual (um arquivo por UF ou nacional, por ano)
  cobertura:
    inicio: '1991'
    fim: em-curso
  unidade: um mapa digital em formato TabWin (`.MAP`), por UF e ano de referência
  granularidade:
    espacial: UF e município
    temporal: versão (mês de publicação)
  formato_bruto: ZIP
  lake:
    estado: so-bruto
    particoes: []
    chave: []
    colunas: null
  dados_pessoais: nenhum
  eras: []
  revisado_em: '2026-11-16'
  versao_fetcher: 0.19.0
---

# Base Territorial - Mapas (`base-territorial-mapas`)

## Resumo

O `base-territorial-mapas` contém os **mapas digitais em formato TabWin (`.MAP`)** da divisão territorial brasileira, usados para a representação cartográfica dos dados de saúde. Cada ZIP reúne, para uma UF (ou o Brasil) e um ano de referência, um conjunto de arquivos `.MAP` correspondentes aos recortes territoriais — município, região de saúde, macrorregião de saúde, microrregião IBGE, região metropolitana e divisão administrativa. É a base cartográfica que permite gerar mapas temáticos (por município ou região) no TabWin e em apps compatíveis.

## Ficha técnica

<!-- gerado:ficha -->

## Origem e coleta

- **Formato dos arquivos** (índice de 2026-10, conforme a página anterior): `.zip` (contendo arquivos `.MAP` do TabWin)
- **Particionamento** (índice de 2026-10, conforme a página anterior): `uf`, `year` (um ZIP por UF e ano de referência)
- **Cobertura temporal no FTP** (índice de 2026-10, conforme a página anterior): 1991 a 2025 (conforme `index.json`)
- **Volume aproximado no FTP** (índice de 2026-10, conforme a página anterior): 111 arquivos (~143 MB, 28 UFs/consolidados)
- **Documentação oficial no FTP** (índice de 2026-10, conforme a página anterior): `/territorio/doc` (`bases_territoriais.pdf`, `registro_de_alteracoes.pdf`)

### Diretórios e Padrões de Arquivos (`meta.py`)

| Diretório FTP (`dir`) | Prefixo (`filename_prefix`) | Padrão (`filename_pattern`) | Extensão | Preliminar |
|---|---|---|---|---|
| `/territorio/mapas` | (vazio) | `<uf>_mapas_<AAAA>` (ex.: `es_mapas_2025`, `br_mapas_2013`) | `zip` | Não |

### Nomenclatura e Armazenamento Local

- **No servidor FTP (`ftp.datasus.gov.br`)**: exemplo real `es_mapas_2025.zip` — `es` é a UF, `mapas` o assunto e `2025` o ano de referência da malha. Contém `es_regsaud.MAP`, `es_divadm.MAP`, `es_macsaud.MAP`, `es_micibge.MAP`, `es_municip.MAP` e `es_regmetr.MAP`. Há também arquivos `br_mapas_<ano>.zip` (malha nacional de 1991 a 2025) e códigos de UF/"mrco"/"mrne" para malhas regionais.
- **No armazenamento local do `datasus-fetcher`**: `data/base-territorial-mapas/2025/base-territorial-mapas_2025-es@20260918.zip`.
- **Documentação e Tabelas Auxiliares associadas**: `bases_territoriais.pdf` e `registro_de_alteracoes.pdf` em `/territorio/doc`; para converter/visualizar os `.MAP`, é necessário o aplicativo **TabWin** do DATASUS.

## Conteúdo

Os mapas integram a **Base Territorial** mantida pelo **Ministério da Saúde/DATASUS** e servem de suporte cartográfico à análise e à disseminação dos dados de saúde. São a versão geográfica dos recortes territoriais: permitem que sistemas como o TabWin associem códigos de município/região a polígonos, viabilizando mapas de taxas, coberturas e indicadores.

O **evento gerador** é a atualização das malhas territoriais quando há mudanças na divisão político-administrativa (Censos, contagens e revisões da malha municipal do IBGE; criação/desmembramento de municípios; redefinição de regiões de saúde). A **unidade de análise é o conjunto de arquivos `.MAP` de uma UF em um ano**. Os anos disponíveis correspondem a marcos da malha do IBGE: **1991, 1994, 1997, 2001, 2005, 2013 e 2025** (algumas UFs não têm todos os anos). Cada ZIP contém arquivos como `<uf>_municip.MAP`, `<uf>_regsaud.MAP`, `<uf>_macsaud.MAP`, `<uf>_micibge.MAP`, `<uf>_regmetr.MAP` e `<uf>_divadm.MAP`.

Não há diretório preliminar. Os arquivos `.MAP` são binários proprietários do TabWin e exigem esse aplicativo (ou conversão) para uso; o DATASUS também disponibiliza os shapes equivalentes em outros portais.

Aplicações analíticas típicas: geração de mapas temáticos de indicadores de saúde no TabWin, análise espacial da distribuição de doenças e da oferta de serviços, apoio à regionalização e à vigilância em saúde e produção de mapas para relatórios e boletins.

## Variáveis

Não se aplica: o dataset reúne arquivos de mapa em formato TabWin (`.MAP`, polígonos), que o conversor não lê. Não há esquema de referência nem dicionário de colunas.

## No lake

O dataset está só no bruto: o conversor ignora os ZIPs de mapas (`nao_tabular` no inventário). Não há `datasus/base-territorial-mapas` no lake.

## Cuidados de uso

- Os `.MAP` só abrem no TabWin ou em ferramentas que leiam o formato; para análise geográfica em Python, use as malhas do IBGE. (Observação operacional, não verificada contra os arquivos.)

## Exemplos

### Pela linha de comando (`datasus-fetcher`)

```bash
# o que o FTP publica para o dataset (arquivos e tamanho)
datasus-fetcher list base-territorial-mapas

# baixa um recorte, com a documentação oficial e as tabelas auxiliares (`--dry-run` só lista)
datasus-fetcher sync base-territorial-mapas -o ./data --start 2020 --end 2024 --docs --aux

# converte o que foi baixado para o lake (Parquet particionado)
datasus-fetcher convert -i ./data -o ./lake --dataset base-territorial-mapas
```

## Referências

- **Servidor FTP do DATASUS**: `ftp://ftp.datasus.gov.br/territorio/mapas`
- **Portal de Transferência de Arquivos do DATASUS**: https://datasus.saude.gov.br/transferencia-de-arquivos/
- **TabNet DATASUS**: https://datasus.saude.gov.br/informacoes-de-saude-tabnet/
- **TabWin/DATASUS** (aplicativo que lê os arquivos `.MAP`)
- **Documentação `bases_territoriais.pdf` e `registro_de_alteracoes.pdf`**: `ftp://ftp.datasus.gov.br/territorio/doc`
- **IBGE — Malhas territoriais**: https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais.html
