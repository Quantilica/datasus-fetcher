from importlib.metadata import PackageNotFoundError, version

from quantilica.core.logging import get_logger

try:
    __version__ = version("datasus-fetcher")
except PackageNotFoundError:
    __version__ = "0.0.0"

logger = get_logger(__name__)

from .reader import decompress_dbc

try:
    import polars  # noqa: F401

    try:
        import fastdbf  # noqa: F401
    except ImportError:
        import dbfread  # noqa: F401

    from .reader import read_dbc, read_dbf, wrangle_datasus, write_parquet
    from .wrangling import convert_directory, convert_file, parse_filename_metadata

    _HAS_ANALYTICS = True
except ImportError:
    _HAS_ANALYTICS = False
    read_dbc = None
    read_dbf = None
    wrangle_datasus = None
    write_parquet = None
    convert_file = None
    convert_directory = None
    parse_filename_metadata = None

__all__ = [
    "__version__",
    "decompress_dbc",
    "_HAS_ANALYTICS",
]

if _HAS_ANALYTICS:
    __all__.extend(
        [
            "read_dbc",
            "read_dbf",
            "wrangle_datasus",
            "write_parquet",
            "convert_file",
            "convert_directory",
            "parse_filename_metadata",
        ]
    )
