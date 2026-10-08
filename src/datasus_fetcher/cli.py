"""CLI fina para datasus-fetcher (delega para o plugin Typer)."""

from __future__ import annotations

import sys

from datasus_fetcher.targets import (
    _systems_to_datasets as _systems_to_datasets,
)
from datasus_fetcher.targets import (
    parse_systems as parse_systems,
)
from datasus_fetcher.targets import (
    resolve_dataset_targets as resolve_dataset_targets,
)
from datasus_fetcher.targets import (
    resolve_targets as resolve_targets,
)

_HOST_MODULES = {"typer", "rich", "quantilica"}

try:
    from .plugin import app
except ImportError as exc:  # host (typer/rich/quantilica-cli) ausente
    if (exc.name or "").split(".")[0] not in _HOST_MODULES:
        raise
    app = None
    _PLUGIN_ERROR = exc
else:
    _PLUGIN_ERROR = None


def main(argv: list[str] | None = None) -> None:
    """Ponto de entrada da CLI.

    Args:
        argv (list[str] | None): Argumentos (None usa ``sys.argv[1:]``).
    """
    from . import __version__

    if argv is None:
        argv = sys.argv[1:]
    if "--version" in argv:
        print(f"datasus-fetcher {__version__}")
        return

    if app is None:
        print(
            "Erro: CLI requer 'typer' e 'rich' (via quantilica-cli). "
            'Instale via "quantilica install datasus". '
            f"Detalhe: {_PLUGIN_ERROR}",
            file=sys.stderr,
        )
        raise SystemExit(1)

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
