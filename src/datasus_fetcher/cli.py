"""CLI fina para datasus-fetcher (delega para o plugin Typer)."""

from __future__ import annotations

import sys

from .plugin import _systems_to_datasets, app, resolve_dataset_targets


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


def main(argv: list[str] | None = None) -> None:
    """Main entry point for the CLI.

    Args:
        argv (list[str] | None, optional): The command line arguments. Defaults to None.
    """
    from . import __version__

    if argv and "--version" in argv:
        print(f"datasus-fetcher {__version__}")
        return

    try:
        app(argv)
    except SystemExit as exc:
        if exc.code not in (0, None):
            raise
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.", file=sys.stderr)
        sys.exit(130)


if __name__ == "__main__":
    main()
