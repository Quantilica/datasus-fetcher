"""Low-level reader and conversion functions for DATASUS microdata."""

from __future__ import annotations

import logging
import struct
import tempfile
from collections.abc import Callable, Iterator
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

# fastdbf materializa o arquivo inteiro em ``to_arrow()`` e o pico de memória fica em
# cerca de 12x o tamanho do .dbf (medido em 2026-10-13: 529 MiB de .dbf -> 6,4 GB).
# Acima de ``2 * DBF_CHUNK_BYTES`` o arquivo é lido em pedaços desse tamanho.
DBF_CHUNK_BYTES = 32 * 2**20


def _iter_dbf_chunks(dbf_path: Path, chunk_bytes: int, tmp_dir: Path) -> Iterator[Path]:
    """Divide um .dbf em .dbf menores (mesmo cabeçalho, menos registros).

    O formato dBASE tem cabeçalho de tamanho fixo (bytes 8-9), registros de tamanho fixo
    (bytes 10-11) e a contagem de registros nos bytes 4-7. Cada pedaço copia o cabeçalho
    com a contagem ajustada, uma fatia contígua de registros e o terminador ``0x1A``.
    Os arquivos são gravados em ``tmp_dir`` e removidos assim que o chamador avança.

    Args:
        dbf_path: Arquivo .dbf de origem.
        chunk_bytes: Tamanho alvo, em bytes de registros, de cada pedaço.
        tmp_dir: Pasta temporária para os pedaços.

    Yields:
        Caminho de cada pedaço, em ordem.
    """
    with open(dbf_path, "rb") as src:
        header = src.read(32)
        n_records = struct.unpack("<I", header[4:8])[0]
        header_len, record_len = struct.unpack("<HH", header[8:12])
        src.seek(0)
        full_header = src.read(header_len)
        per_chunk = max(1, chunk_bytes // max(record_len, 1))
        done = 0
        index = 0
        while done < n_records:
            count = min(per_chunk, n_records - done)
            piece = tmp_dir / f"{dbf_path.stem}.{index:05d}.dbf"
            with open(piece, "wb") as out:
                out.write(full_header[:4] + struct.pack("<I", count) + full_header[8:])
                src.seek(header_len + done * record_len)
                remaining = count * record_len
                while remaining:
                    block = src.read(min(remaining, 8 * 2**20))
                    if not block:
                        raise ValueError(
                            f"{dbf_path} termina antes dos {n_records} registros"
                        )
                    out.write(block)
                    remaining -= len(block)
                out.write(b"\x1a")
            yield piece
            piece.unlink(missing_ok=True)
            done += count
            index += 1


def _read_dbf_fastdbf(dbf_path: Path) -> pl.DataFrame:
    import fastdbf
    import polars as pl

    with fastdbf.Table(str(dbf_path)).open("r") as table:
        return _normalize_frame(pl.from_arrow(table.to_arrow()))


def _read_dbf_dbfread(dbf_path: Path, encoding: str) -> pl.DataFrame:
    """Lê um .dbf com dbfread (Python puro): lento e pesado, mas tolerante."""
    import polars as pl

    try:
        import dbfread
    except ImportError as err:
        raise ImportError(
            "Leitura de arquivos DBF requer extras de análise: "
            "uv add 'datasus-fetcher[analysis]' "
            "--index https://index.quantilica.com/simple/"
        ) from err

    table = dbfread.DBF(
        str(dbf_path),
        encoding=encoding,
        ignore_missing_memofile=True,
        char_decode_errors="replace",
    )
    # Mesmo formato do fastdbf: nomes em maiúsculas e coluna ``_deleted``. O dbfread já
    # descarta os registros deletados, então a coluna é sempre falsa.
    cols: dict[str, list] = {field.name: [] for field in table.fields}
    for rec in table:
        for k, v in rec.items():
            cols[k].append(v)
    if not cols or all(len(v) == 0 for v in cols.values()):
        return pl.DataFrame()
    frame = pl.DataFrame(
        {name.upper(): values for name, values in cols.items()},
        infer_schema_length=None,
    )
    return frame.with_columns(pl.lit(False).alias("_deleted"))


def _read_dbf_piece(piece: Path, encoding: str) -> pl.DataFrame:
    """Lê um .dbf (ou um pedaço dele) com fastdbf e, se falhar, com dbfread.

    Um campo numérico com lixo (por exemplo ``"2165198310000EP3170"`` num SIA-PA)
    faz o fastdbf levantar ``DbfFormatError``. Como o fallback vale só para o
    pedaço que falhou, o custo do dbfread fica limitado a ele.
    """
    try:
        return _read_dbf_fastdbf(piece)
    except Exception as exc:
        logger.debug("fastdbf falhou em %s (%s), usando dbfread", piece.name, exc)
        return _read_dbf_dbfread(piece, encoding)


def _dbf_frames(
    src: Path, encoding: str, chunk_bytes: int | None
) -> Iterator[pl.DataFrame]:
    """Gera os DataFrames brutos de um .dbf (um só, ou um por pedaço)."""
    if chunk_bytes is None or src.stat().st_size <= 2 * chunk_bytes:
        yield _read_dbf_piece(src, encoding)
        return
    with tempfile.TemporaryDirectory(prefix="dbf-chunks-") as tmp:
        for piece in _iter_dbf_chunks(src, chunk_bytes, Path(tmp)):
            yield _read_dbf_piece(piece, encoding)


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


def read_dbf(
    dbf_path: Path | str,
    encoding: str = "latin1",
    chunk_bytes: int | None = DBF_CHUNK_BYTES,
    transform: Callable[[pl.DataFrame], pl.DataFrame] | None = None,
) -> pl.DataFrame:
    """Read a .dbf file into a Polars DataFrame.

    Tries fastdbf (Rust + Apache Arrow) first, falling back to dbfread (pure
    Python) for maximum portability. fastdbf builds the whole Arrow table at once and
    peaks at roughly 12x the .dbf size in memory, so files larger than
    ``2 * chunk_bytes`` are read in pieces of about ``chunk_bytes`` and concatenated;
    the peak then follows the chunk plus the final DataFrame. The fallback is per
    piece: one malformed record only sends its own piece to dbfread.

    Args:
        dbf_path: Path to the .dbf file.
        encoding: Character encoding for text fields (defaults to 'latin1').
        chunk_bytes: Piece size, in bytes of records, for the fastdbf path.
            ``None`` reads the whole file at once.
        transform: Optional function applied to each raw piece before the pieces
            are concatenated (for example ``wrangle_datasus``). Typing each piece
            early keeps the peak well below an all-string frame of the whole file.

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

    frames = []
    for raw in _dbf_frames(src, encoding, chunk_bytes):
        frame = transform(raw) if transform is not None else raw
        if frame.width:
            frames.append(frame)
    if not frames:
        return pl.DataFrame()
    return pl.concat(frames, how="diagonal_relaxed") if len(frames) > 1 else frames[0]


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

    def wrangle(frame: pl.DataFrame) -> pl.DataFrame:
        return wrangle_datasus(
            frame,
            dataset=dataset,
            lowercase=lowercase,
            extra_columns=extra_columns,
        )

    transform = wrangle if clean else None
    if keep_dbf:
        dbf_path = decompress_dbc(src)
        return read_dbf(dbf_path, encoding=encoding, transform=transform)

    with tempfile.NamedTemporaryFile(suffix=".dbf", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        decompress_dbc(src, tmp_path)
        return read_dbf(tmp_path, encoding=encoding, transform=transform)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def write_parquet(
    df: pl.DataFrame,
    dest_path: Path | str,
    compression: str = "zstd",
    source_path: Path | str | None = None,
) -> Path:
    """Save a Polars DataFrame to a Parquet file atomically with metadata.

    When ``source_path`` is given (or a ``.manifest.json`` sidecar exists next
    to the raw file), the ``quantilica.*`` provenance keys are injected into
    the Parquet file-level metadata.

    Args:
        df: Polars DataFrame to save.
        dest_path: Destination path for the Parquet file.
        compression: Compression algorithm ('zstd', 'snappy', 'lz4', 'uncompressed').
        source_path: Raw .dbc/.dbf whose ``.manifest.json`` sidecar provides
            the provenance. Defaults to None (no provenance recorded).

    Returns:
        Path to the saved Parquet file.
    """
    dest = Path(dest_path)
    dest.parent.mkdir(parents=True, exist_ok=True)
    metadata: dict[str, str] = {}
    if source_path is not None:
        try:
            from quantilica.analytics.writer import manifest_to_metadata
            from quantilica.core.manifests import read_manifest_sidecar
        except ImportError:  # quantilica-analytics ausente: sem proveniência
            logger.debug("quantilica-analytics ausente; sem metadados quantilica.*")
        else:
            metadata.update(manifest_to_metadata(read_manifest_sidecar(source_path)))
    df.write_parquet(
        dest,
        compression=compression,
        statistics=True,
        metadata=metadata or None,
    )
    logger.debug("Parquet salvo em %s (%d linhas)", dest, len(df))
    return dest
