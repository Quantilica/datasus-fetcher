"""Convert raw DATASUS microdata (DBC/DBF) into the Hive-partitioned lake.

Each raw DBC/DBF lands in
``<lake>/datasus/<dataset_id>/[ano=<ano>/][mes=<mes>/]<dataset_id>_<ano><mes>.parquet``

The DATASUS publishes one file per state and period, most of them tiny: the files
of a period share one Parquet, with the state as the ``uf`` column (the rows are
sorted by it) and the raw file's key in ``_origem``.
as ``<file_key>.parquet``. Columns are cleaned and normalized with lowercase names,
while partition columns are encoded in directory structure according to the Hive
partitioning contract.
"""

from __future__ import annotations

import itertools
import logging
import os
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any

try:
    import polars as pl
    from quantilica.analytics.lake import (
        LAKE_SCRATCH_ENV,
        ORIGIN_COLUMN,
        GroupMember,
        LakeError,
        LakeWriter,
    )
    from quantilica.core.lake import (
        DatasetDescriptor,
        partition_types_for,
        select_current,
    )
except ImportError as exc:
    raise ImportError(
        "datasus_fetcher.lake requer o extra 'analysis': "
        "uv add 'datasus-fetcher[analysis]' "
        "--index https://index.quantilica.com/simple/"
    ) from exc

from datasus_fetcher import __version__, lake_bases, meta, reader
from datasus_fetcher.wrangling import parse_filename_metadata

if TYPE_CHECKING:
    from quantilica.core.lake import Planned

logger = logging.getLogger(__name__)

# The writer's refusals for members whose columns or types differ all point to
# its ``schema`` argument; the other ``LakeError`` (rows that do not add up, a
# file that is not the group) are not a reason to rewrite the period.
_SCHEMA_HINT = "`schema`"

SOURCE_ID = "datasus"


@dataclass
class ConvertResult:
    """Counts of a conversion run; ``errors`` holds one message per failure."""

    converted: int = 0
    skipped: int = 0
    errors: list[str] = field(default_factory=list)
    #: Períodos que o escritor recusou por esquema e foram regravados membro a membro.
    fallbacks: int = 0


def resolve_dataset_id(path: Path, meta_dict: dict[str, Any]) -> str | None:
    """Resolve the canonical dataset identifier for a given file."""
    # 1. Parent directory is a known dataset
    if path.parent.name in meta.datasets:
        return path.parent.name

    # 2. Grandparent directory is a known dataset
    if path.parent.parent.name in meta.datasets:
        return path.parent.parent.name

    # 3. Parsed metadata dataset
    ds = meta_dict.get("dataset")
    if ds in meta.datasets:
        return ds

    # 4. Map sim-do -> sim-do-cid09 or sim-do-cid10
    if ds == "sim-do":
        ano = meta_dict.get("ano", 2000)
        return "sim-do-cid10" if ano >= 1996 else "sim-do-cid09"
    if ds == "sinasc":
        return "sinasc-dn"

    return ds


def route_file(path: Path) -> tuple[str | None, dict[str, Any]]:
    """Dataset e metadados de um arquivo bruto, pelo nome e pela pasta.

    É o roteamento único de :meth:`LakeConverter.convert` e
    :meth:`LakeConverter.inventory`.
    """
    meta_dict = parse_filename_metadata(path)
    return resolve_dataset_id(path, meta_dict), meta_dict


def _is_sidecar(path: Path) -> bool:
    """Se o arquivo é sidecar de manifest ou resto ``.tmp``, não dado bruto."""
    return path.name.endswith((".manifest.json", ".tmp"))


def resolve_partitions(meta_dict: dict[str, Any]) -> tuple[list[str], dict[str, str]]:
    """Determine partition keys and their formatted values."""
    keys: list[str] = []
    values: dict[str, str] = {}

    if "uf" in meta_dict and meta_dict["uf"]:
        keys.append("uf")
        values["uf"] = str(meta_dict["uf"]).lower()

    if "ano" in meta_dict and meta_dict["ano"]:
        keys.append("ano")
        values["ano"] = f"{int(meta_dict['ano']):04d}"

    if "mes" in meta_dict and meta_dict["mes"]:
        keys.append("mes")
        values["mes"] = f"{int(meta_dict['mes']):02d}"

    return keys, values


@dataclass
class _Group:
    """Raw files that share one grouped Parquet (one dataset, one period)."""

    dataset_id: str
    group: str
    partitions: dict[str, str]
    writer: LakeWriter
    files: list[tuple[Path, dict[str, str]]] = field(default_factory=list)


class _MemberFailed(Exception):  # noqa: N818
    """A raw file of the group could not be decoded (carries the file)."""

    def __init__(self, path: Path, cause: BaseException) -> None:
        super().__init__(str(cause))
        self.path = path
        self.cause = cause


def _first_line(exc: BaseException) -> str:
    message = str(exc).strip()
    return message.splitlines()[0] if message else repr(exc)


def _decode(path: Path, dataset_id: str) -> pl.DataFrame:
    """Rows of one raw DBC/DBF, cleaned and with lowercase column names."""
    if path.suffix.lower() == ".dbc":
        return reader.read_dbc(path, clean=True, dataset=dataset_id, lowercase=True)
    return reader.read_dbf(
        path,
        transform=lambda f, ds=dataset_id: reader.wrangle_datasus(
            f, dataset=ds, lowercase=True
        ),
    )


class LakeConverter:
    """Converter registered under the ``quantilica.lake`` entry point."""

    source_id = SOURCE_ID

    def datasets(self) -> list[str]:
        """Dataset ids this converter writes to the lake."""
        return sorted(meta.datasets.keys())

    def convert(
        self,
        input_dir: Path,
        lake_dir: Path,
        *,
        datasets: list[str] | None = None,
        force: bool = False,
    ) -> ConvertResult:
        """Convert raw DBC and DBF files into ``lake_dir``.

        Args:
            input_dir: Root directory containing raw DATASUS files.
            lake_dir: Root of the lake.
            datasets: Optional list of dataset ids to convert; None converts all.
            force: Reconvert even if sha256 already matches in the lake.

        Returns:
            ConvertResult: Files converted, skipped, and error messages.
        """
        input_dir = Path(input_dir)
        lake_dir = Path(lake_dir)
        result = ConvertResult()
        if input_dir.is_file():
            files = [input_dir] if input_dir.suffix.lower() in {".dbc", ".dbf"} else []
        elif input_dir.is_dir():
            files = sorted(
                p
                for p in input_dir.rglob("*")
                if p.is_file() and p.suffix.lower() in {".dbc", ".dbf", ".zip"}
            )
        else:
            result.errors.append(f"arquivo ou diretório '{input_dir}' não existe")
            return result

        # Duas versões do mesmo bruto na pasta (``X@d1.dbc`` e ``X@d2.dbc``) têm a
        # mesma chave de membro: vale a mais nova e a antiga nem é decodificada.
        if input_dir.is_dir():
            tabular = [p for p in files if p.suffix.lower() in {".dbc", ".dbf"}]
            current = set(select_current(tabular))
            files = [p for p in files if p not in tabular or p in current]

        allowed = set(datasets) if datasets else None
        writers: dict[str, LakeWriter] = {}
        groups: dict[tuple, _Group] = {}
        base_zips: list[tuple[Path, str, dict[str, Any]]] = []

        for path in files:
            dataset_id, meta_dict = route_file(path)
            if path.suffix.lower() == ".zip":
                # Só as bases auxiliares vêm em ZIP; os demais (mapas) ficam fora.
                if lake_bases.is_base_zip(dataset_id) and (
                    allowed is None or dataset_id in allowed
                ):
                    base_zips.append(
                        (path, dataset_id, resolve_partitions(meta_dict)[1])
                    )
                continue
            if not dataset_id:
                result.errors.append(
                    f"{path.name}: não foi possível identificar dataset"
                )
                continue

            if allowed is not None and dataset_id not in allowed:
                continue

            partition_keys, partition_values, member, group = (
                lake_bases.group_partitions(dataset_id, *resolve_partitions(meta_dict))
            )

            if dataset_id not in writers:
                writers[dataset_id] = LakeWriter(
                    lake_dir / SOURCE_ID / dataset_id,
                    DatasetDescriptor(
                        source_id=SOURCE_ID,
                        dataset_id=dataset_id,
                        alias=dataset_id,
                        partition_keys=partition_keys,
                        partition_types=partition_types_for(partition_keys),
                    ),
                    force=force,
                )

            slot = (dataset_id, group, tuple(partition_values.items()))
            if slot not in groups:
                groups[slot] = _Group(
                    dataset_id, group, partition_values, writers[dataset_id]
                )
            groups[slot].files.append((path, member))

        for item in groups.values():
            self._write_group(item, result)

        def writer_for(dataset_id: str, keys: list[str]) -> LakeWriter:
            key = f"{dataset_id}:{','.join(keys)}"
            if key not in writers:
                writers[key] = LakeWriter(
                    lake_dir / SOURCE_ID / dataset_id,
                    lake_bases.descriptor(dataset_id, keys),
                    force=force,
                )
            return writers[key]

        lake_bases.convert_base_zips(base_zips, writer_for, result)
        return result

    @staticmethod
    def _write_group(item: _Group, result: ConvertResult) -> None:
        """Write the grouped Parquet of a period without holding it in memory.

        Each raw file that has to be written is decoded on its own, written to a
        temporary Parquet and released before the next one is read; a file that
        cannot be decoded is reported and left out *before* the writer starts, so
        no decode is repeated. ``LakeWriter.write_group`` then merges the
        temporary files in DuckDB, spilling to disk, and writes the period's file
        once, sorted by the member columns and ``_origem``, as ``write_member``
        left it; each temporary file is removed as soon as the writer has copied
        it. The peak follows the largest raw file, never the period (``sia-pa``:
        52 million rows by 62 columns in a month).

        The rows a file had in the Parquet stay if it is left out
        (``prune=False``), as do members whose raw file is gone. A period the
        writer refuses because the members' columns or types differ is rewritten
        member by member, which merges them by column name as before, and is
        counted in ``result.fallbacks``; any other refusal (rows that do not add
        up, a file that is not the group) is an error of the period.
        """
        converter_tag = f"datasus-fetcher {__version__}"
        remaining = list(item.files)
        scratch = os.environ.get(LAKE_SCRATCH_ENV)
        if scratch:
            Path(scratch).mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(
            prefix="datasus-members-", dir=scratch or None
        ) as tmp:
            stage = Path(tmp)
            staged: dict[Path, Path] = {}

            counter = itertools.count()
            asked: list[Path] = []

            def decode(path: Path) -> Path:
                """The member's rows as a temporary Parquet (decoded once)."""
                if path in staged:
                    return staged[path]
                out = stage / f"{next(counter):06d}.parquet"
                try:
                    frame = _decode(path, item.dataset_id)
                    frame.write_parquet(out, compression="lz4")
                except Exception as exc:
                    out.unlink(missing_ok=True)
                    raise _MemberFailed(path, exc) from exc
                staged[path] = out
                return out

            def release(path: Path) -> Path:
                # The writer copied the member it asked for last before asking
                # for this one: its temporary file is no longer needed.
                for done in asked:
                    staged.pop(done).unlink(missing_ok=True)
                asked.clear()
                out = decode(path)
                asked.append(path)
                return out

            # Decode up front what the writer would ask for, so a bad file is
            # dropped now and the writer runs once.
            for path, _member in list(remaining):
                try:
                    if item.writer.is_current_member(
                        path, group_key=item.group, partitions=item.partitions
                    ):
                        continue
                    decode(path)
                except _MemberFailed as failed:
                    result.errors.append(
                        f"{failed.path.name}: {_first_line(failed.cause)}"
                    )
                    remaining = [(p, m) for p, m in remaining if p != failed.path]
                except Exception as exc:
                    result.errors.append(f"{path.name}: {_first_line(exc)}")
                    remaining = [(p, m) for p, m in remaining if p != path]

            while remaining:
                members = [
                    GroupMember(path, data=lambda path=path: release(path), columns=m)
                    for path, m in remaining
                ]
                try:
                    written = item.writer.write_group(
                        item.group,
                        members,
                        partitions=item.partitions,
                        converter=converter_tag,
                        prune=False,
                        sort_by=[*remaining[0][1], ORIGIN_COLUMN],
                    )
                except _MemberFailed as failed:
                    # Only a file the up-front pass saw as current but the writer
                    # did not (its member columns changed) can fail here.
                    result.errors.append(
                        f"{failed.path.name}: {_first_line(failed.cause)}"
                    )
                    remaining = [(p, m) for p, m in remaining if p != failed.path]
                    continue
                except LakeError as exc:
                    if _SCHEMA_HINT not in str(exc):
                        result.errors.append(f"{item.group}: {_first_line(exc)}")
                        return
                    logger.warning(
                        "lake: group %s refused (%s); writing it member by member",
                        item.group,
                        _first_line(exc),
                    )
                    result.fallbacks += 1
                    LakeConverter._write_members(item, remaining, converter_tag, result)
                    return
                except (OSError, pl.exceptions.PolarsError, Exception) as exc:
                    result.errors.append(f"{item.group}: {_first_line(exc)}")
                    return
                done = len(written.written)
                result.converted += done
                result.skipped += len(members) - done
                return

    @staticmethod
    def _write_members(
        item: _Group,
        files: list[tuple[Path, dict[str, str]]],
        converter_tag: str,
        result: ConvertResult,
    ) -> None:
        """Write the group one raw file at a time (``write_member``)."""
        for path, member in files:
            try:
                # Decodificar um DBC custa caro; o arquivo já presente no lake com
                # o mesmo sha256 é pulado antes da leitura.
                if item.writer.is_current_member(
                    path, group_key=item.group, partitions=item.partitions
                ):
                    result.skipped += 1
                    continue
                written = item.writer.write_member(
                    _decode(path, item.dataset_id),
                    path,
                    group_key=item.group,
                    partitions=item.partitions,
                    member_columns=member,
                    converter=converter_tag,
                )
            except (LakeError, OSError, pl.exceptions.PolarsError, Exception) as exc:
                result.errors.append(f"{path.name}: {_first_line(exc)}")
                continue
            if written.status == "skipped":
                result.skipped += 1
            else:
                result.converted += 1

    def inventory(self, input_dir: Path) -> list[Planned]:
        """Um ``Planned`` por arquivo bruto: o dataset ou o motivo de ignorar.

        Reaproveita o roteamento de :meth:`convert` (``route_file`` e a escolha
        do ZIP territorial mais recente) numa única varredura de ``input_dir``,
        sem abrir nenhum arquivo:

        - ``.dbc``/``.dbf``: o dataset de ``route_file`` (sem dataset
          identificável, o item fica sem destino nem motivo, como o erro de
          ``convert``); as versões anteriores de um mesmo bruto
          (``X@20260906.dbc`` ao lado de ``X@20261016.dbc``) vêm como
          ``"superado"``;
        - ``.zip`` de base auxiliar (população do IBGE, base territorial,
          conversão do TabWin): o dataset da pasta; as versões anteriores do mesmo
          ZIP (população e conversão) e os ZIPs de ``base-territorial`` anteriores
          ao mais recente vêm como ``"superado"``;
        - qualquer outro arquivo (mapas, ZIPs de mapas, ``.cnv``, ``.def``,
          documentação): ``"nao_tabular"``.

        Sidecars ``*.manifest.json`` e restos ``*.tmp`` não entram.

        Args:
            input_dir: Raiz dos arquivos brutos (a mesma de ``convert``).

        Returns:
            list[Planned]: Um item por arquivo, em ordem de caminho.
        """
        # Import local: o core publicado antes do contrato não tem ``Planned``.
        from quantilica.core.lake import Planned

        input_dir = Path(input_dir)
        if input_dir.is_file():
            files = [input_dir]
        elif input_dir.is_dir():
            files = sorted(
                p for p in input_dir.rglob("*") if p.is_file() and not _is_sidecar(p)
            )
        else:
            return []

        planned: list[Planned | None] = []
        base_zips: list[tuple[Path, str, None]] = []
        zip_slots: dict[Path, int] = {}
        tabular = [p for p in files if p.suffix.lower() in {".dbc", ".dbf"}]
        vigentes = set(select_current(tabular)) if not input_dir.is_file() else None
        for path in files:
            suffix = path.suffix.lower()
            if suffix in {".dbc", ".dbf"}:
                if vigentes is not None and path not in vigentes:
                    planned.append(Planned(path, skip_reason="superado"))
                    continue
                dataset_id, _ = route_file(path)
                planned.append(Planned(path, dataset=dataset_id))
            elif suffix == ".zip" and not input_dir.is_file():
                dataset_id, _ = route_file(path)
                if lake_bases.is_base_zip(dataset_id):
                    base_zips.append((path, dataset_id, None))
                    zip_slots[path] = len(planned)
                    planned.append(None)
                else:
                    planned.append(Planned(path, skip_reason="nao_tabular"))
            else:
                planned.append(Planned(path, skip_reason="nao_tabular"))

        vigentes_bases = lake_bases.current_zips(base_zips)
        for path, dataset_id, _ in base_zips:
            superseded = path not in vigentes_bases
            planned[zip_slots[path]] = (
                Planned(path, skip_reason="superado")
                if superseded
                else Planned(path, dataset=dataset_id)
            )
        return [item for item in planned if item is not None]


converter = LakeConverter()
