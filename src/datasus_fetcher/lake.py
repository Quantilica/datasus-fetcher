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

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any

try:
    import polars as pl
    from quantilica.analytics.lake import LakeError, LakeWriter
    from quantilica.core.lake import DatasetDescriptor
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

SOURCE_ID = "datasus"


@dataclass
class ConvertResult:
    """Counts of a conversion run; ``errors`` holds one message per failure."""

    converted: int = 0
    skipped: int = 0
    errors: list[str] = field(default_factory=list)


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

        allowed = set(datasets) if datasets else None
        writers: dict[str, LakeWriter] = {}
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
                        partition_types={k: "varchar" for k in partition_keys},
                    ),
                    force=force,
                )

            writer = writers[dataset_id]

            try:
                # Decodificar um DBC custa caro; o arquivo já presente no lake com
                # o mesmo sha256 é pulado antes da leitura.
                if writer.is_current_member(
                    path, group_key=group, partitions=partition_values
                ):
                    result.skipped += 1
                    continue
                if path.suffix.lower() == ".dbc":
                    df = reader.read_dbc(
                        path, clean=True, dataset=dataset_id, lowercase=True
                    )
                else:
                    df = reader.read_dbf(
                        path,
                        transform=lambda f, ds=dataset_id: reader.wrangle_datasus(
                            f, dataset=ds, lowercase=True
                        ),
                    )

                written = writer.write_member(
                    df,
                    path,
                    group_key=group,
                    partitions=partition_values,
                    member_columns=member,
                    converter=f"datasus-fetcher {__version__}",
                )
            except (LakeError, OSError, pl.exceptions.PolarsError, Exception) as exc:
                message = str(exc).strip()
                first_line = message.splitlines()[0] if message else repr(exc)
                result.errors.append(f"{path.name}: {first_line}")
                continue

            if written.status == "skipped":
                result.skipped += 1
            else:
                result.converted += 1

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

    def inventory(self, input_dir: Path) -> list[Planned]:
        """Um ``Planned`` por arquivo bruto: o dataset ou o motivo de ignorar.

        Reaproveita o roteamento de :meth:`convert` (``route_file`` e a escolha
        do ZIP territorial mais recente) numa única varredura de ``input_dir``,
        sem abrir nenhum arquivo:

        - ``.dbc``/``.dbf``: o dataset de ``route_file`` (sem dataset
          identificável, o item fica sem destino nem motivo, como o erro de
          ``convert``);
        - ``.zip`` de base auxiliar (população do IBGE, base territorial,
          conversão do TabWin): o dataset da pasta; os ZIPs de ``base-territorial``
          anteriores ao mais recente vêm como ``"superado"``;
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
        for path in files:
            suffix = path.suffix.lower()
            if suffix in {".dbc", ".dbf"}:
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

        latest = lake_bases.latest_territorial(base_zips)
        for path, dataset_id, _ in base_zips:
            superseded = dataset_id == lake_bases.TERRITORIAL and path != latest
            planned[zip_slots[path]] = (
                Planned(path, skip_reason="superado")
                if superseded
                else Planned(path, dataset=dataset_id)
            )
        return [item for item in planned if item is not None]


converter = LakeConverter()
