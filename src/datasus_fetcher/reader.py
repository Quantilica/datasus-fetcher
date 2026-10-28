"""Low-level reader and conversion functions for DATASUS microdata."""

from __future__ import annotations

import logging
import struct
import tempfile
from collections.abc import Callable, Iterator
from dataclasses import dataclass
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

DBF_FIELD_TERMINATOR = 0x0D


@dataclass(frozen=True)
class DbfField:
    """One field descriptor of a dBASE header."""

    name: str
    type: str
    length: int
    decimals: int


def _dbf_fields(header: bytes) -> list[DbfField]:
    """Parse the field descriptors (32 bytes each, from byte 32 up to ``0x0D``)."""
    header_len = struct.unpack("<H", header[8:10])[0]
    fields = []
    pos = 32
    # Só descritores inteiros: há arquivos sem o 0x0D (ver _fix_field_displacements).
    while pos + 32 < header_len and header[pos] != DBF_FIELD_TERMINATOR:
        desc = header[pos : pos + 32]
        name = desc[:11].split(b"\0", 1)[0].decode("ascii").strip().upper()
        fields.append(DbfField(name, chr(desc[11]), desc[16], desc[17]))
        pos += 32
    return fields


def _with_field_offsets(header: bytes) -> bytes:
    """Return the header with each field's offset (bytes 12-15) filled in.

    The DATASUS .dbf files leave every field offset as zero. fastdbf reads each
    field from that offset, so every field came out read from the start of the
    record (``DT_INTER=' 1200002'``, ``VAL_TOT`` of 1.2 trillion, ``SEXO``
    empty). The offsets are the running sum of the field lengths after the
    one-byte deletion flag.

    Raises:
        ValueError: If the field lengths do not add up to the record length.
    """
    header_len, record_len = struct.unpack("<HH", header[8:12])
    fixed = bytearray(header)
    offset = 1  # byte de deleção
    pos = 32
    while pos < header_len and fixed[pos] != DBF_FIELD_TERMINATOR:
        fixed[pos + 12 : pos + 16] = struct.pack("<I", offset)
        offset += fixed[pos + 16]
        pos += 32
    if offset != record_len:
        raise ValueError(
            f"Campos somam {offset} bytes por registro, cabeçalho declara {record_len}"
        )
    return bytes(fixed)


# Registros comparados com o dbfread em cada pedaço lido pelo fastdbf.
DBF_SANITY_ROWS = 50


def _fix_field_displacements(header: bytes) -> bytes:
    """Grava nos descritores de campo o deslocamento de cada campo no registro.

    Os bytes 12-15 de cada descritor de 32 bytes são "reservados" no dBASE III, mas o
    FoxPro os usa como deslocamento do campo dentro do registro, e o fastdbf (0.5.2)
    confia neles. Os arquivos do DATASUS deixam esses bytes zerados, então o fastdbf
    lia todos os campos a partir do byte 0 do registro (o byte de deleção) e devolvia
    valores deslocados em silêncio (``DTOBITO=" 1207052"`` em vez de ``"07052022"``).
    Aqui o deslocamento é recalculado como ``1 + soma dos tamanhos anteriores`` (o
    byte 0 é o marcador de deleção), o que não altera a leitura pelo dbfread.

    Alguns arquivos (CNES-ST desde 2019-12) trazem ``0x00`` no lugar do terminador
    ``0x0D`` dos descritores, no último byte do cabeçalho; sem ele, o dbfread lê o
    início dos registros como mais um campo. O terminador é reposto.

    Args:
        header: Cabeçalho completo do .dbf (``header_len`` bytes).

    Returns:
        Cópia do cabeçalho com os deslocamentos corrigidos.
    """
    fixed = bytearray(header)
    pos = 1
    off = 32
    while off + 32 <= len(fixed) and fixed[off] != DBF_FIELD_TERMINATOR:
        fixed[off + 12 : off + 16] = struct.pack("<I", pos)
        pos += fixed[off + 16]
        off += 32
    if off == len(fixed) - 1 and fixed[off] == 0:
        fixed[off] = DBF_FIELD_TERMINATOR
    return bytes(fixed)


def _has_wrong_displacements(dbf_path: Path) -> bool:
    """Indica se os deslocamentos gravados no cabeçalho divergem do layout real."""
    with open(dbf_path, "rb") as src:
        header = src.read(32)
        if len(header) < 32:
            return False
        header_len = struct.unpack("<H", header[8:10])[0]
        src.seek(0)
        full_header = src.read(header_len)
    return _fix_field_displacements(full_header) != full_header


def _iter_dbf_chunks(dbf_path: Path, chunk_bytes: int, tmp_dir: Path) -> Iterator[Path]:
    """Divide um .dbf em .dbf menores (mesmo cabeçalho, menos registros).

    O formato dBASE tem cabeçalho de tamanho fixo (bytes 8-9), registros de tamanho fixo
    (bytes 10-11) e a contagem de registros nos bytes 4-7. Cada pedaço copia o cabeçalho
    com a contagem ajustada (e os deslocamentos de campo corrigidos, ver
    :func:`_fix_field_displacements`), uma fatia contígua de registros e o terminador
    ``0x1A``. Os arquivos são gravados em ``tmp_dir`` e removidos assim que o chamador
    avança.

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
        full_header = _fix_field_displacements(src.read(header_len))
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


def _datasus_field_parser(dbfread: Any) -> type:
    """``FieldParser`` do dbfread que lê como nula a data só de ``*``, espaço ou ``0``.

    O SINAN grava ``********`` (ou ``      **``) em campos ``D`` sem data; o dbfread
    e o fastdbf recusam o arquivo inteiro. Outros valores inválidos seguem erro.
    """

    class _DatasusFieldParser(dbfread.FieldParser):
        def parseD(self, field, data):  # noqa: N802 - nome do dbfread
            try:
                return super().parseD(field, data)
            except ValueError:
                if not data.strip(b" *0"):
                    return None
                raise

    return _DatasusFieldParser


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
        parserclass=_datasus_field_parser(dbfread),
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


def _same_value(a: Any, b: Any) -> bool:
    """Compara um valor do fastdbf com o do dbfread, tolerando tipo e espaços."""
    import datetime as dt
    from decimal import Decimal

    if a is None or b is None:
        return (a is None or a == "") and (b is None or b == "")
    if isinstance(a, int | float | Decimal) and isinstance(b, int | float | Decimal):
        return float(a) == float(b)
    if isinstance(a, dt.date) or isinstance(b, dt.date):
        return a == b
    return str(a).strip() == str(b).strip()


def _fastdbf_mismatch(
    frame: pl.DataFrame, piece: Path, encoding: str, rows: int
) -> str | None:
    """Confere as primeiras ``rows`` linhas do fastdbf contra o dbfread.

    Barato (o dbfread lê os registros sob demanda) e pega deslocamento de colunas,
    que não levanta exceção. Registros deletados são ignorados nos dois lados.

    Returns:
        Descrição da primeira divergência, ou ``None`` se tudo bate.
    """
    from itertools import islice

    try:
        import dbfread
    except ImportError:
        return None

    table = dbfread.DBF(
        str(piece),
        encoding=encoding,
        ignore_missing_memofile=True,
        char_decode_errors="replace",
    )
    try:
        reference = list(islice(iter(table), rows))
    except Exception as exc:  # o dbfread também não lê: nada a comparar
        logger.debug("dbfread falhou na checagem de %s (%s)", piece.name, exc)
        return None
    sample = frame
    if "_deleted" in frame.columns:
        sample = frame.filter(~frame["_deleted"].fill_null(False))
    sample = sample.head(len(reference))
    if sample.height != len(reference):
        return f"{sample.height} linhas no fastdbf, {len(reference)} no dbfread"
    for field in table.field_names:
        name = field.upper()
        if name not in sample.columns:
            return f"coluna {name} ausente no fastdbf"
        values = sample[name].to_list()
        for i, (got, rec) in enumerate(zip(values, reference, strict=True)):
            if not _same_value(got, rec[field]):
                return f"{name}[{i}]: fastdbf={got!r} dbfread={rec[field]!r}"
    return None


def _exact_decimals(frame: pl.DataFrame, fields: list[DbfField]) -> pl.DataFrame:
    """Turn numeric fields with decimal places into exact ``Decimal`` columns.

    Both backends parse ``N``/``F`` fields with decimals into ``Float64``. The
    shortest text of each float is the decimal written in the file (fields
    have at most 20 characters), so it is cast to ``Decimal(length, decimals)``
    through that text, never through the binary value.

    Raises:
        ValueError: If a value does not fit the declared field size.
    """
    import polars as pl

    for field in fields:
        if field.type not in "NF" or not field.decimals or field.name not in frame:
            continue
        text = pl.col(field.name).cast(pl.Float64).round(field.decimals).cast(pl.String)
        dtype = pl.Decimal(precision=min(field.length, 38), scale=field.decimals)
        try:
            frame = frame.with_columns(text.cast(dtype, strict=True).alias(field.name))
        except pl.exceptions.InvalidOperationError:
            # O texto cabe no campo, mas não na precisão declarada: "3415.0" num
            # N(6,3) (PESO do SINAN). A escala é mantida; só a precisão cresce.
            wide = pl.Decimal(precision=38, scale=field.decimals)
            try:
                frame = frame.with_columns(
                    text.cast(wide, strict=True).alias(field.name)
                )
            except pl.exceptions.InvalidOperationError as exc:
                raise ValueError(
                    f"Valor fora do tamanho declarado no cabeçalho: {exc}"
                ) from exc
    return frame


def _read_dbf_piece(
    piece: Path, encoding: str, sanity_rows: int = DBF_SANITY_ROWS
) -> pl.DataFrame:
    """Lê um .dbf (ou um pedaço dele) com fastdbf e, se falhar, com dbfread.

    Um campo numérico com lixo (por exemplo ``"2165198310000EP3170"`` num SIA-PA)
    faz o fastdbf levantar ``DbfFormatError``. Como o fallback vale só para o
    pedaço que falhou, o custo do dbfread fica limitado a ele. Erros silenciosos
    também caem no dbfread: as primeiras ``sanity_rows`` linhas do fastdbf são
    comparadas com as do dbfread e, se divergirem, o pedaço é relido com o dbfread
    e um aviso é registrado.
    """
    with open(piece, "rb") as src:
        head = src.read(32)
        header_len = struct.unpack("<H", head[8:10])[0]
        fields = _dbf_fields(head + src.read(header_len - 32))
    try:
        frame = _read_dbf_fastdbf(piece)
    except Exception as exc:
        logger.debug("fastdbf falhou em %s (%s), usando dbfread", piece.name, exc)
        frame = _read_dbf_dbfread(piece, encoding)
    else:
        if sanity_rows > 0:
            mismatch = _fastdbf_mismatch(frame, piece, encoding, sanity_rows)
            if mismatch is not None:
                logger.warning(
                    "fastdbf divergiu do dbfread em %s (%s); usando dbfread",
                    piece.name,
                    mismatch,
                )
                frame = _read_dbf_dbfread(piece, encoding)
    return _exact_decimals(frame, fields)


def _dbf_frames(
    src: Path, encoding: str, chunk_bytes: int | None
) -> Iterator[pl.DataFrame]:
    """Gera os DataFrames brutos de um .dbf (um só, ou um por pedaço).

    Arquivos pequenos com deslocamentos de campo zerados no cabeçalho (o caso do
    DATASUS) passam por uma cópia temporária única com o cabeçalho corrigido, pois o
    fastdbf lê os campos nas posições gravadas ali.
    """
    size = src.stat().st_size
    if chunk_bytes is None or size <= 2 * chunk_bytes:
        if not _has_wrong_displacements(src):
            yield _read_dbf_piece(src, encoding)
            return
        chunk_bytes = max(size, 1)
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
    Python) for maximum portability. fastdbf reads each field at the displacement
    stored in its descriptor, which DATASUS files leave zeroed; the header is
    rewritten with the real displacements in a temporary copy before fastdbf sees
    it, and the first rows of every piece are checked against dbfread (a mismatch
    logs a warning and rereads the piece with dbfread). fastdbf builds the whole
    Arrow table at once and peaks at roughly 12x the .dbf size in memory, so files
    larger than ``2 * chunk_bytes`` are read in pieces of about ``chunk_bytes`` and
    concatenated; the peak then follows the chunk plus the final DataFrame. The
    fallback is per piece: one malformed record only sends its own piece to dbfread.

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
        # Arquivo sem registros (o DATASUS publica meses vazios): zero linhas, mas
        # com as colunas do cabeçalho e os tipos que os leitores dariam a elas.
        empty = _empty_frame(src)
        return transform(empty) if transform is not None else empty
    return pl.concat(frames, how="diagonal_relaxed") if len(frames) > 1 else frames[0]


def _empty_frame(dbf_path: Path) -> pl.DataFrame:
    """DataFrame sem linhas com os campos declarados no cabeçalho do .dbf.

    Os tipos seguem o que o fastdbf e o :func:`_exact_decimals` produzem para um
    arquivo com registros: ``C`` texto, ``N`` sem casas ``Int64``, ``N``/``F`` com
    casas ``Decimal``, ``F`` sem casas ``Float64``, ``D`` data e ``L`` booleano,
    mais a coluna ``_deleted``.
    """
    import polars as pl

    with open(dbf_path, "rb") as src:
        head = src.read(32)
        header_len = struct.unpack("<H", head[8:10])[0]
        fields = _dbf_fields(head + src.read(header_len - 32))
    schema = {}
    for field in fields:
        if field.type in "NF" and field.decimals:
            dtype = pl.Decimal(precision=min(field.length, 38), scale=field.decimals)
        elif field.type == "N":
            dtype = pl.Int64
        elif field.type == "F":
            dtype = pl.Float64
        elif field.type == "D":
            dtype = pl.Date
        elif field.type == "L":
            dtype = pl.Boolean
        else:
            dtype = pl.String
        schema[field.name] = dtype
    schema["_deleted"] = pl.Boolean  # como o fastdbf (e _read_dbf_dbfread) entregam
    return pl.DataFrame(schema=schema)


# Datasets cujas datas de 8 dígitos são DDMMAAAA (as do SIM ficam texto, ver constants).
DDMMYYYY_DATASETS = frozenset({"resp"})


def _parse_date(expr: pl.Expr, dataset: str | None) -> pl.Expr:
    """Data de um campo texto, pelo formato que o DATASUS usa em cada caso.

    - 8 dígitos: ``AAAAMMDD`` (``DDMMAAAA`` nos ``DDMMYYYY_DATASETS``);
    - 6 dígitos no SIH (até meados dos anos 1990): ``AAMMDD``;
    - 6 dígitos nos demais (competência do SIA-PS, SIA-SAD, SISPRENATAL): ``AAAAMM``,
      lido como o dia 1º do mês.

    O que não casar vira nulo aqui, e a checagem estrita de ``wrangle_datasus``
    transforma isso em erro.
    """
    import polars as pl

    text = expr.cast(pl.String)
    size = text.str.len_chars()
    eight = "%d%m%Y" if dataset in DDMMYYYY_DATASETS else "%Y%m%d"
    if dataset is not None and dataset.startswith("sih"):
        six = text.str.to_date("%y%m%d", strict=False)
    else:
        six = (text + "01").str.to_date("%Y%m%d", strict=False)
    return (
        pl.when(size == 8)
        .then(text.str.to_date(eight, strict=False))
        .when(size == 6)
        .then(six)
        .otherwise(None)
    )


def wrangle_datasus(
    df: pl.DataFrame,
    dataset: str | None = None,
    lowercase: bool = True,
    extra_columns: dict[str, Any] | None = None,
) -> pl.DataFrame:
    """Apply canonical wrangling rules to raw DATASUS DataFrames.

    - Trims whitespace from string columns.
    - Converts legacy sentinel values ("", "NA", "999999", etc.) to null.
    - Preserves administrative/diagnostic and categorical code columns as
      clean strings with leading zeros.
    - Parses YYYYMMDD date columns (``DATE_COLUMNS``) to pl.Date. Columns
      that already arrive as dates (``D`` fields of the .dbf, as in the SINAN)
      are kept; datetimes are truncated to the date. The SIM DDMMYYYY date
      fields stay as text: some are partial (see constants).
    - Keeps exact ``Decimal`` monetary columns (numeric DBF fields with
      decimals, see ``read_dbf``); text monetary columns become pl.Float64.
    - Converts counts to pl.Int64.
    - Lowercases column names for modern analytical querying.
    - Appends optional partition metadata columns (e.g. uf, ano, mes).

    Conversions are strict: a value that is not a sentinel and does not parse
    raises ``ValueError`` (naming the column and showing examples) instead of
    becoming null.

    Args:
        df: Input raw Polars DataFrame.
        dataset: Dataset identifier (e.g. 'sih-rd', 'sim-do') for specialized
            schema logic.
        lowercase: Whether to convert all column names to lowercase.
        extra_columns: Optional dictionary of literal columns to add
            (e.g. partition keys).

    Returns:
        Cleaned and strictly typed Polars DataFrame.

    Raises:
        ValueError: If a date, monetary or count value does not parse.
    """
    import polars as pl

    if df.is_empty():
        return df

    exprs: list[pl.Expr] = []
    cleaned: list[pl.Expr] = []
    converted: dict[str, str] = {}  # coluna de saída -> coluna de entrada
    sentinels = list(SENTINEL_NULLS)

    for col in df.columns:
        u_col = col.upper()
        expr = pl.col(col)
        dtype = df[col].dtype

        # Sanitizar strings e sentinelas
        if dtype == pl.String:
            expr = expr.str.strip_chars()
            expr = pl.when(expr.is_in(sentinels)).then(None).otherwise(expr)
        cleaned.append(expr.alias(col))
        target_name = col.lower() if lowercase else col

        if u_col in CODE_COLUMNS:
            # Preservar estritamente como string UTF-8 limpa
            expr = expr.cast(pl.String)
        elif u_col in DATE_COLUMNS:
            if dtype == pl.Date or dtype == pl.Null:
                # Campo tipo D do .dbf (SINAN): o leitor já entrega data.
                expr = expr.cast(pl.Date)
            elif isinstance(dtype, pl.Datetime):
                expr = expr.dt.date()
            else:
                expr = _parse_date(expr, dataset)
                converted[target_name] = col
        elif u_col in FLOAT_COLUMNS:
            if isinstance(dtype, pl.Decimal):
                pass  # já exato (read_dbf)
            elif dtype == pl.String:
                expr = expr.str.replace(",", ".").cast(pl.Float64, strict=False)
                converted[target_name] = col
            else:
                expr = expr.cast(pl.Float64)
        elif u_col in INTEGER_COLUMNS:
            expr = expr.cast(pl.Int64, strict=False)
            converted[target_name] = col

        exprs.append(expr.alias(target_name))

    result = df.select(exprs)

    # Conversão estrita: o que não era nulo (nem sentinela) e virou nulo é erro.
    if converted:
        before = df.select(cleaned)
        problems = []
        for target, source in converted.items():
            lost = before[source].is_not_null() & result[target].is_null()
            if lost.any():
                examples = before.filter(lost)[source].unique().head(5).to_list()
                problems.append(
                    f"{source}: {int(lost.sum())} valor(es), ex. {examples}"
                )
        if problems:
            raise ValueError("Valores fora do formato esperado: " + "; ".join(problems))

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
