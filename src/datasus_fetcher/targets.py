"""Resolução de datasets/sistemas alvo do datasus-fetcher.

Este módulo concentra os helpers puros (sem Typer/Rich) que expandem
``--system`` em datasets e mesclam datasets posicionais com sistemas.
Tanto o plugin Typer (``plugin.py``) quanto a CLI fina (``cli.py``)
importam daqui — ``cli.py`` nunca é importado pelo ``plugin.py``.
"""

from __future__ import annotations

from datasus_fetcher import meta


def _systems_to_datasets(systems: list[str] | None) -> list[str] | None:
    """Expands ``--system`` values (case-insensitive, comma-separated) to datasets.

    Args:
        systems (list[str] | None): Raw ``--system`` option values.

    Returns:
        list[str] | None: Unique dataset IDs, or None when nothing requested.

    Raises:
        ValueError: On an unrecognized system/dataset name.
    """
    if not systems:
        return None
    items: list[str] = []
    for chunk in systems:
        items.extend(piece.strip() for piece in chunk.split(",") if piece.strip())
    if not items:
        return None
    try:
        return meta.expand_systems(items)
    except KeyError as exc:
        raise ValueError(str(exc.args[0])) from exc


def resolve_dataset_targets(
    datasets: list[str] | None, systems: list[str] | None
) -> list[str] | None:
    """Merges positional datasets with ``--system`` resolution.

    Args:
        datasets (list[str] | None): Positional dataset IDs.
        systems (list[str] | None): Dataset IDs expanded from ``--system``.

    Returns:
        list[str] | None: Effective target datasets; None means 'all'.
    """
    if systems:
        merged = list(systems)
        if datasets:
            known = set(systems)
            for dataset in datasets:
                if dataset.lower() not in known:
                    merged.append(dataset)
        return merged
    return datasets


def parse_systems(system_args: list[str] | None) -> list[str] | None:
    """Normalizes ``--system`` CLI values into dataset IDs.

    Accepts multiple occurrences (``-s sim -s sinasc``) and comma-separated
    values (``--system sim,sinasc``), case-insensitive. Returns None when no
    systems were requested (keeps positional datasets behavior untouched).

    Args:
        system_args (list[str] | None): Raw ``--system`` values.

    Returns:
        list[str] | None: Dataset IDs, or None if no systems were requested.

    Raises:
        SystemExit: On an unrecognized system/dataset name.
    """
    try:
        return _systems_to_datasets(system_args)
    except Exception as exc:
        raise SystemExit(str(exc)) from exc


def resolve_targets(
    datasets: list[str] | None, systems: list[str] | None
) -> list[str] | None:
    """Merges positional datasets and ``--system`` resolution into targets.

    Args:
        datasets (list[str] | None): Positional dataset IDs from the CLI.
        systems (list[str] | None): Dataset IDs already expanded from systems.

    Returns:
        list[str] | None: Effective target datasets; None means 'all'.
    """
    return resolve_dataset_targets(datasets, systems)
