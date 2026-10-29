"""Bases auxiliares do DATASUS distribuídas em ZIP, para o lake.

- ``base-populacional-ibge-pop*``: um DBF de população por ano (``uf=br/ano=``).
- ``base-territorial``: tabelas de referência (``tb_municip``, ``rl_municip_*``...);
  só o ZIP mais recente vale, e cada tabela vira o dataset
  ``base-territorial-<tabela>``.
- ``base-territorial-conversao``: arquivos ``.cnv`` do TabWin (categorias e os
  códigos de cada uma), uma linha por código, particionados por UF.

Os mapas (``base-territorial-mapas``, ``.MAP``) são polígonos e ficam fora.
"""

from __future__ import annotations

import re
import tempfile
import zipfile
from collections.abc import Callable
from pathlib import Path
from typing import Any

import polars as pl
from quantilica.analytics.lake import LakeWriter
from quantilica.core.lake import DatasetDescriptor

from datasus_fetcher import __version__, reader

SOURCE_ID = "datasus"
POPULACIONAL = "base-populacional-ibge-"
TERRITORIAL = "base-territorial"
CONVERSAO = "base-territorial-conversao"

_UF = re.compile(r"_(?P<uf>[a-z]{2})@", re.IGNORECASE)
_STAMP = re.compile(r"@(?P<stamp>\d{8})")
# Linha de um .cnv: sequência nas 7 primeiras colunas (às vezes precedida de um
# marcador de subtotal, "  1   2"), descrição e, no fim, os códigos de tamanho L
# (do cabeçalho "<categorias> <L>"), com vírgulas e faixas "a-b".
_CNV_HEAD = re.compile(r"^\s*[A-Za-z]?\s*\d+\s+(?P<size>\d+)")
# Layout com subtotal: "      1      3     ..... RIO BRANCO" (a sequência vem
# antes dos pontos de indentação).
_CNV_SEQ_BEFORE_DOTS = re.compile(r"^\s*(?P<seq>\d+)\s+(?=\.)")
_MAX_RANGE = 100_000


def is_base_zip(dataset_id: str | None) -> bool:
    """Se o ZIP pertence a uma das bases tratadas aqui."""
    if not dataset_id:
        return False
    return dataset_id.startswith(POPULACIONAL) or dataset_id in (TERRITORIAL, CONVERSAO)


def expand_codes(field: str) -> list[str]:
    """Códigos de uma linha ``.cnv``: ``"120001,120005-120007"`` vira cinco códigos.

    Faixas entre números do mesmo tamanho são expandidas com zeros à esquerda;
    o resto fica como veio.
    """
    codes: list[str] = []
    for token in filter(None, field.split(",")):
        start, sep, end = token.partition("-")
        if (
            sep
            and start.isdigit()
            and end.isdigit()
            and len(start) == len(end)
            and 0 <= int(end) - int(start) <= _MAX_RANGE
        ):
            codes.extend(
                str(n).zfill(len(start)) for n in range(int(start), int(end) + 1)
            )
        else:
            codes.append(token)
    return codes


def read_cnv(text: str, table: str) -> pl.DataFrame:
    """Linhas de um arquivo de conversão do TabWin, uma por código.

    Linhas sem códigos no fim (títulos de grupo) ficam de fora.
    """
    rows: dict[str, list[Any]] = {
        "tabela": [],
        "sequencia": [],
        "nivel": [],
        "descricao": [],
        "codigo": [],
    }
    lines = text.splitlines()
    head = _CNV_HEAD.match(lines[0]) if lines else None
    if head is None:
        raise ValueError(f"{table}: cabeçalho .cnv inválido")
    size = int(head["size"])
    tail = re.compile(
        rf"^(?P<desc>.*?)\s+(?P<codes>\d{{{size}}}(?:[-,]\d{{{size}}})*)\s*$"
    )
    for line in lines[1:]:
        numbers = line[:7].split()
        rest = line[7:]
        inner = _CNV_SEQ_BEFORE_DOTS.match(rest)
        if inner is not None:
            numbers, rest = [inner["seq"]], rest[inner.end() :]
        match = tail.match(rest)
        if not numbers or not numbers[-1].isdigit() or match is None:
            continue
        desc = match["desc"].strip()
        stripped = desc.lstrip(".")
        for code in expand_codes(match["codes"]):
            rows["tabela"].append(table)
            rows["sequencia"].append(int(numbers[-1]))
            rows["nivel"].append((len(desc) - len(stripped)) // 4)
            rows["descricao"].append(stripped.strip())
            rows["codigo"].append(code)
    return pl.DataFrame(
        rows,
        schema={
            "tabela": pl.String,
            "sequencia": pl.Int64,
            "nivel": pl.Int64,
            "descricao": pl.String,
            "codigo": pl.String,
        },
    )


def _stamp(path: Path) -> str:
    match = _STAMP.search(path.name)
    return match["stamp"] if match else ""


def convert_base_zips(
    zips: list[tuple[Path, str, dict[str, Any]]],
    writer_for: Callable[[str, list[str]], LakeWriter],
    result: Any,
) -> None:
    """Converte os ZIPs das bases auxiliares.

    Args:
        zips: ``(caminho, dataset, partições)`` de cada ZIP.
        writer_for: Devolve o ``LakeWriter`` de um dataset com as chaves dadas.
        result: ``ConvertResult`` do conversor (contagens e erros).
    """
    converter = f"datasus-fetcher {__version__}"
    territorial = [z for z in zips if z[1] == TERRITORIAL]
    latest = max(territorial, key=lambda z: _stamp(z[0]), default=None)
    for path, dataset_id, partitions in zips:
        try:
            if dataset_id.startswith(POPULACIONAL):
                _populacional(
                    path, dataset_id, partitions, writer_for, result, converter
                )
            elif dataset_id == CONVERSAO:
                _conversao(path, writer_for, result, converter)
            elif latest is not None and path == latest[0]:
                _territorial(path, writer_for, result, converter)
        except Exception as exc:  # noqa: BLE001 - registra e segue
            message = str(exc).strip()
            first = message.splitlines()[0] if message else repr(exc)
            result.errors.append(f"{path.name}: {first}")


def _count(written: Any, result: Any) -> None:
    if written.status == "skipped":
        result.skipped += 1
    else:
        result.converted += 1


def _populacional(path, dataset_id, partitions, writer_for, result, converter):
    writer = writer_for(dataset_id, list(partitions))
    if writer.is_current(path, partitions=partitions):
        result.skipped += 1
        return
    with zipfile.ZipFile(path) as archive, tempfile.TemporaryDirectory() as tmp:
        # Até 2024 o ZIP traz o .dbf; o de 2025 traz o .dbc (POPTBR25.dbc).
        member = next(
            (n for n in archive.namelist() if n.lower().endswith((".dbf", ".dbc"))),
            None,
        )
        if member is None:
            raise ValueError("ZIP sem .dbf nem .dbc")
        dbf = Path(archive.extract(member, tmp))
        if dbf.suffix.lower() == ".dbc":
            dbf = reader.decompress_dbc(dbf, dbf.with_suffix(".dbf"))
        df = reader.read_dbf(
            dbf,
            transform=lambda f: reader.wrangle_datasus(
                f, dataset=dataset_id, lowercase=True
            ),
        )
    _count(
        writer.write_polars(df, path, partitions=partitions, converter=converter),
        result,
    )


def _conversao(path, writer_for, result, converter):
    match = _UF.search(path.name)
    partitions = {"uf": match["uf"].lower()} if match else {}
    writer = writer_for(CONVERSAO, list(partitions))
    if writer.is_current(path, partitions=partitions):
        result.skipped += 1
        return
    frames = []
    with zipfile.ZipFile(path) as archive:
        for name in sorted(archive.namelist()):
            if not name.lower().endswith(".cnv"):
                continue
            text = archive.read(name).decode("latin-1")
            frames.append(read_cnv(text, Path(name).stem.lower()))
    if not frames:
        raise ValueError("ZIP sem .cnv")
    df = pl.concat(frames)
    _count(
        writer.write_polars(df, path, partitions=partitions, converter=converter),
        result,
    )


def _territorial(path, writer_for, result, converter):
    with zipfile.ZipFile(path) as archive, tempfile.TemporaryDirectory() as tmp:
        tables: dict[str, str] = {}
        for name in archive.namelist():
            stem, suffix = Path(name).stem.lower(), Path(name).suffix.lower()
            if "_layout" in stem or suffix not in (".dbf", ".csv"):
                continue
            # O DBF tem os tipos declarados; o CSV só quando não há DBF.
            if suffix == ".dbf" or stem not in tables:
                tables[stem] = name
        for stem, name in sorted(tables.items()):
            dataset_id = f"{TERRITORIAL}-{stem.replace('_', '-')}"
            writer = writer_for(dataset_id, [])
            local = Path(archive.extract(name, tmp))
            if local.suffix.lower() == ".dbf":
                df = reader.read_dbf(
                    local,
                    transform=lambda f: reader.wrangle_datasus(f, lowercase=True),
                )
            else:
                df = pl.read_csv(
                    local, separator=";", encoding="latin-1", infer_schema_length=0
                )
            written = writer.write_polars(
                df, path, file_key_name=stem, converter=converter
            )
            _count(written, result)


def descriptor(dataset_id: str, keys: list[str]) -> DatasetDescriptor:
    """Descritor de um dataset das bases auxiliares."""
    return DatasetDescriptor(
        source_id=SOURCE_ID,
        dataset_id=dataset_id,
        alias=dataset_id,
        partition_keys=keys,
        partition_types={k: "varchar" for k in keys},
    )
