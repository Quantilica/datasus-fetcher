"""Low-level reader and conversion functions for DATASUS microdata."""

from __future__ import annotations

import logging
import tempfile
from pathlib import Path
from typing import TYPE_CHECKING, Any

from .constants import (
    CODE_COLUMNS,
    DATE_COLUMNS,
    FLOAT_COLUMNS,
    INTEGER_COLUMNS,
    SENTINEL_NULLS,
)

if TYPE_CHECKING:
    import polars as pl

logger = logging.getLogger(__name__)


def _normalize_frame(result: pl.DataFrame | pl.Series) -> pl.DataFrame:
    """Normalizar o retorno de backends Arrow para DataFrame.

    Versões novas do fastdbf devolvem ``StructArray`` em ``to_arrow()``, e
    ``pl.from_arrow`` converte para ``Series`` de structs (uma linha lógica
    por registro, sem ``.columns``) em vez de ``DataFrame``. Sem isso,
    ``wrangle_datasus`` explode com ``'Series' object has no attribute
    'columns'`` só no ambiente com deps latest (CI conjunto), nunca no
    workspace pinnado.

    Args:
        result: Saída de ``pl.from_arrow`` (DataFrame ou Series).

    Returns:
        DataFrame com uma coluna por campo (unnest no caso struct).
    """
    import polars as pl

    if isinstance(result, pl.DataFrame):
        return result
    frame = result.to_frame()
    if result.dtype == pl.Struct:
        frame = frame.unnest(result.name)
    return frame


def decompress_dbc(dbc_path: Path | str, dbf_path: Path | str | None = None) -> Path:
    """Decompress a .dbc file (PKWARE DCL implode) to a .dbf file.

    Uses the native Rust extension (_datasus_dbc), running at native CPU speed
    and releasing the Python GIL during decompression.

    Args:
        dbc_path: Path to the input .dbc file.
        dbf_path: Path for the output .dbf file. If None, uses the same path
            with a '.dbf' extension.

    Returns:
        Path to the decompressed .dbf file.
    """
    from . import _datasus_dbc

    src = Path(dbc_path)
    if not src.exists():
        raise FileNotFoundError(f"Arquivo .dbc não encontrado: {src}")

    if dbf_path is None:
        dest = src.with_suffix(".dbf")
    else:
        dest = Path(dbf_path)

    dest.parent.mkdir(parents=True, exist_ok=True)
    logger.debug("Descompactando %s -> %s via Rust nativo", src, dest)
    _datasus_dbc.decompress(str(src), str(dest))
    return dest


def read_dbf(dbf_path: Path | str, encoding: str = "latin1") -> pl.DataFrame:
    """Read a .dbf file into a Polars DataFrame.

    Tries fastdbf (Rust + Apache Arrow zero-copy) first, falling back to
    dbfread (pure Python) for maximum portability.

    Args:
        dbf_path: Path to the .dbf file.
        encoding: Character encoding for text fields (defaults to 'latin1').

    Returns:
        polars.DataFrame containing the raw records.

    Raises:
        ImportError: If analytics dependencies are not installed.
        FileNotFoundError: If the .dbf file does not exist.
    """
    import polars as pl

    src = Path(dbf_path)
    if not src.exists():
        raise FileNotFoundError(f"Arquivo .dbf não encontrado: {src}")

    # 1. Tentar leitura rápida via fastdbf
    try:
        import fastdbf

        with fastdbf.Table(str(src)).open("r") as table:
            arrow_table = table.to_arrow()
            return _normalize_frame(pl.from_arrow(arrow_table))
    except Exception as exc:
        logger.debug("fastdbf falhou (%s), tentando fallback com dbfread", exc)

    # 2. Fallback via dbfread
    try:
        import dbfread

        table = dbfread.DBF(
            str(src),
            encoding=encoding,
            ignore_missing_memofile=True,
            char_decode_errors="replace",
        )
        cols: dict[str, list] = {field.name: [] for field in table.fields}
        for rec in table:
            for k, v in rec.items():
                cols[k].append(v)
        if not cols or all(len(v) == 0 for v in cols.values()):
            return pl.DataFrame()
        return pl.DataFrame(cols, infer_schema_length=None)
    except ImportError as err:
        raise ImportError(
            "Leitura de arquivos DBF requer extras de análise: "
            "pip install datasus-fetcher[analytics]"
        ) from err


def wrangle_datasus(
    df: pl.DataFrame,
    dataset: str | None = None,
    lowercase: bool = True,
    extra_columns: dict[str, Any] | None = None,
) -> pl.DataFrame:
    """Apply canonical wrangling rules to raw DATASUS DataFrames.

    - Trims whitespace from string columns.
    - Converts legacy sentinel values ("", "NA", "999999", etc.) to null.
    - Preserves administrative/diagnostic code columns as clean strings with
      leading zeros.
    - Parses date columns (DT_*) from YYYYMMDD to pl.Date.
    - Converts monetary and floating-point columns to pl.Float64.
    - Converts counts and integer columns to pl.Int64.
    - Lowercases column names for modern analytical querying.
    - Appends optional partition metadata columns (e.g. uf, ano, mes).

    Args:
        df: Input raw Polars DataFrame.
        dataset: Dataset identifier (e.g. 'sih-rd', 'sim-do') for specialized
            schema logic.
        lowercase: Whether to convert all column names to lowercase.
        extra_columns: Optional dictionary of literal columns to add
            (e.g. partition keys).

    Returns:
        Cleaned and strictly typed Polars DataFrame.
    """
    import polars as pl

    if df.is_empty():
        return df

    exprs: list[pl.Expr] = []
    sentinels = list(SENTINEL_NULLS)

    for col in df.columns:
        u_col = col.upper()
        expr = pl.col(col)
        dtype = df[col].dtype

        # Sanitizar strings e sentinelas
        if dtype == pl.String:
            expr = expr.str.strip_chars()
            expr = pl.when(expr.is_in(sentinels)).then(None).otherwise(expr)

        if u_col in CODE_COLUMNS:
            # Preservar estritamente como string UTF-8 limpa
            expr = expr.cast(pl.String)
        elif u_col in DATE_COLUMNS:
            # Converter YYYYMMDD para Date
            expr = (
                expr.cast(pl.String)
                .str.strip_chars()
                .str.to_date("%Y%m%d", strict=False)
            )
        elif u_col in FLOAT_COLUMNS:
            # Converter monetários / floats
            if dtype == pl.String:
                expr = (
                    expr.str.strip_chars()
                    .str.replace(",", ".")
                    .cast(pl.Float64, strict=False)
                )
            else:
                expr = expr.cast(pl.Float64, strict=False)
        elif u_col in INTEGER_COLUMNS:
            # Converter contagens para Int64
            expr = expr.cast(pl.Int64, strict=False)

        target_name = col.lower() if lowercase else col
        exprs.append(expr.alias(target_name))

    result = df.select(exprs)

    # Descartar registros marcados como deletados no formato dBase
    del_cols = [c for c in result.columns if c.lower() == "_deleted"]
    if del_cols:
        del_c = del_cols[0]
        if result[del_c].dtype == pl.Boolean:
            result = result.filter(~pl.col(del_c))
        result = result.drop(del_c)

    if extra_columns:
        extra_exprs = [
            pl.lit(val).alias(k.lower() if lowercase else k)
            for k, val in extra_columns.items()
            if (k.lower() if lowercase else k) not in result.columns
        ]
        if extra_exprs:
            result = result.with_columns(extra_exprs)

    return result


def read_dbc(
    dbc_path: Path | str,
    keep_dbf: bool = False,
    encoding: str = "latin1",
    clean: bool = True,
    dataset: str | None = None,
    lowercase: bool = True,
    extra_columns: dict[str, Any] | None = None,
) -> pl.DataFrame:
    """Decompress, read, and optionally wrangle a .dbc file directly into a DataFrame.

    Args:
        dbc_path: Path to the .dbc file.
        keep_dbf: If True, keeps the intermediate decompressed .dbf file.
        encoding: Character encoding for text fields.
        clean: If True, applies canonical wrangle_datasus transformations.
        dataset: Dataset identifier for specialized rules.
        lowercase: Whether to lowercase column names.
        extra_columns: Optional literal columns to append (e.g. partition keys).

    Returns:
        Loaded (and wrangled) Polars DataFrame.
    """
    src = Path(dbc_path)
    if keep_dbf:
        dbf_path = decompress_dbc(src)
        df = read_dbf(dbf_path, encoding=encoding)
    else:
        with tempfile.NamedTemporaryFile(suffix=".dbf", delete=False) as tmp:
            tmp_path = Path(tmp.name)
        try:
            decompress_dbc(src, tmp_path)
            df = read_dbf(tmp_path, encoding=encoding)
        finally:
            if tmp_path.exists():
                tmp_path.unlink()

    if clean:
        df = wrangle_datasus(
            df,
            dataset=dataset,
            lowercase=lowercase,
            extra_columns=extra_columns,
        )

    return df


def write_parquet(
    df: pl.DataFrame,
    dest_path: Path | str,
    compression: str = "zstd",
) -> Path:
    """Save a Polars DataFrame to a Parquet file atomically with metadata.

    Args:
        df: Polars DataFrame to save.
        dest_path: Destination path for the Parquet file.
        compression: Compression algorithm ('zstd', 'snappy', 'lz4', 'uncompressed').

    Returns:
        Path to the saved Parquet file.
    """
    dest = Path(dest_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    df.write_parquet(dest, compression=compression, statistics=True)
    logger.debug("Parquet salvo em %s (%d linhas)", dest, len(df))
    return dest
