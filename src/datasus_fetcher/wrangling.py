"""High-level batch conversion and wrangling routines for DATASUS microdata."""

from __future__ import annotations

import concurrent.futures
import logging
import re
from pathlib import Path
from typing import Any

from . import reader

logger = logging.getLogger(__name__)

# Heuristic dataset prefixes
_DATASET_PREFIXES = {
    "rd": "sih-rd",
    "rj": "sih-rj",
    "sp": "sih-sp",
    "er": "sih-er",
    "do": "sim-do",
    "dn": "sinasc",
    "pa": "sia-pa",
    "bi": "sia-bi",
    "dc": "cnes-dc",
    "st": "cnes-st",
    "lt": "cnes-lt",
    "sr": "cnes-sr",
    "cnes": "cnes",
    "deng": "sinan-dengue",
    "chik": "sinan-chikungunya",
    "zika": "sinan-zika",
}


def parse_filename_metadata(filepath_or_name: str | Path) -> dict[str, Any]:
    """Extract partition and dataset metadata from a DATASUS filename.

    Handles standard DATASUS names (e.g. 'RDSP2401.dbc', 'DOSP2022.dbc')
    as well as stamped filenames (e.g. 'RDSP2401@20240215.dbc').

    Args:
        filepath_or_name: File path or filename string.

    Returns:
        Dictionary containing metadata keys (uf, year/ano, month/mes, dataset, etc.).
    """
    path = Path(filepath_or_name)
    raw_name = path.stem.lower()

    # Remover timestamp '@YYYYMMDD' se presente
    if "@" in raw_name:
        name_clean = raw_name.split("@", 1)[0]
    else:
        name_clean = raw_name

    meta: dict[str, Any] = {}

    # 1. Detectar prefixo de dataset
    for pfx, ds in _DATASET_PREFIXES.items():
        if name_clean.startswith(pfx):
            meta["dataset"] = ds
            name_rest = name_clean[len(pfx) :]
            break
    else:
        name_rest = name_clean

    # 2. Heurística UF (2 letras) + ano de 4 dígitos (19xx, 20xx)
    # Ex: 'ac1996' -> uf=ac, ano=1996
    m_uf_y4 = re.match(r"^([a-z]{2})((?:19|20)\d{2})$", name_rest)
    if m_uf_y4:
        uf, y_str = m_uf_y4.groups()
        meta.update({"uf": uf, "ano": int(y_str)})
        return meta

    # 3. Heurística UF (2 letras) + ano de 2 dígitos + mês (01-12)
    # Ex: 'sp2401' -> uf=sp, ano=2024, mes=1
    m_uf_ym = re.match(r"^([a-z]{2})(\d{2})(0[1-9]|1[0-2])$", name_rest)
    if m_uf_ym:
        uf, y_str, m_str = m_uf_ym.groups()
        ano = 1900 + int(y_str) if y_str[0] in "789" else 2000 + int(y_str)
        meta.update({"uf": uf, "ano": ano, "mes": int(m_str)})
        return meta

    # Ex: 'sp24' -> uf=sp, ano=2024
    m_uf_y2 = re.match(r"^([a-z]{2})(\d{2})$", name_rest)
    if m_uf_y2:
        uf, y_str = m_uf_y2.groups()
        ano = 1900 + int(y_str) if y_str[0] in "789" else 2000 + int(y_str)
        meta.update({"uf": uf, "ano": ano})
        return meta

    # Ex: '1996' ou '2024'
    m_y4 = re.search(r"((?:19|20)\d{2})$", name_rest)
    if m_y4:
        meta.update({"ano": int(m_y4.group(1))})
        return meta

    m_y2m2 = re.match(r"^(\d{2})(0[1-9]|1[0-2])$", name_rest)
    if m_y2m2:
        y_str, m_str = m_y2m2.groups()
        ano = 1900 + int(y_str) if y_str[0] in "789" else 2000 + int(y_str)
        meta.update({"ano": ano, "mes": int(m_str)})
        return meta

    return meta


def convert_file(
    input_file: Path | str,
    output_file: Path | str | None = None,
    target_format: str = "parquet",
    compression: str = "zstd",
    clean: bool = True,
    lowercase: bool = True,
    keep_dbf: bool = False,
    dataset: str | None = None,
) -> Path:
    """Convert a single DATASUS file (.dbc or .dbf) to Parquet or DBF.

    Args:
        input_file: Source file path.
        output_file: Target file path. If None, derives filename in same directory.
        target_format: Target format ('parquet' or 'dbf'). Defaults to 'parquet'.
        compression: Parquet compression ('zstd', 'snappy', etc.).
        clean: If True, applies canonical wrangling rules.
        lowercase: If True, lowercases column names.
        keep_dbf: If True and converting .dbc -> .parquet, retains intermediate .dbf.
        dataset: Dataset identifier.

    Returns:
        Path of the generated file.
    """
    src = Path(input_file)
    if not src.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {src}")

    target_fmt = target_format.lower()
    meta = parse_filename_metadata(src)
    effective_dataset = dataset or meta.get("dataset")

    # Extra columns to inject if partition is known
    extra_cols: dict[str, Any] = {}
    if "uf" in meta:
        extra_cols["uf"] = meta["uf"]
    if "ano" in meta:
        extra_cols["ano"] = meta["ano"]
    if "mes" in meta:
        extra_cols["mes"] = meta["mes"]

    if target_fmt == "dbf":
        if src.suffix.lower() == ".dbc":
            dest = Path(output_file) if output_file else src.with_suffix(".dbf")
            return reader.decompress_dbc(src, dest)
        else:
            # Já é .dbf
            return src

    if target_fmt != "parquet":
        raise ValueError(
            f"Formato de destino desconhecido: '{target_format}'. "
            "Use 'parquet' ou 'dbf'."
        )

    dest = Path(output_file) if output_file else src.with_suffix(".parquet")
    dest.parent.mkdir(parents=True, exist_ok=True)

    if src.suffix.lower() == ".dbc":
        df = reader.read_dbc(
            src,
            keep_dbf=keep_dbf,
            clean=clean,
            dataset=effective_dataset,
            lowercase=lowercase,
            extra_columns=extra_cols,
        )
    elif src.suffix.lower() == ".dbf":
        df = reader.read_dbf(src)
        if clean:
            df = reader.wrangle_datasus(
                df,
                dataset=effective_dataset,
                lowercase=lowercase,
                extra_columns=extra_cols,
            )
    else:
        raise ValueError(
            f"Extensão não suportada para conversão: '{src.suffix}'. "
            "Suportadas: .dbc, .dbf"
        )

    return reader.write_parquet(df, dest, compression=compression)


def convert_directory(
    input_dir: Path | str,
    output_dir: Path | str,
    target_format: str = "parquet",
    compression: str = "zstd",
    clean: bool = True,
    lowercase: bool = True,
    keep_dbf: bool = False,
    workers: int = 4,
    recursive: bool = True,
) -> list[Path]:
    """Recursively convert all .dbc and .dbf files in a directory in parallel.

    Args:
        input_dir: Directory containing raw .dbc/.dbf files.
        output_dir: Destination base directory.
        target_format: Target format ('parquet' or 'dbf').
        compression: Parquet compression ('zstd', 'snappy', etc.).
        clean: Whether to apply canonical data wrangling.
        lowercase: Whether to lowercase column names.
        keep_dbf: Whether to keep intermediate .dbf files.
        workers: Number of parallel conversion workers.
        recursive: Whether to scan subdirectories recursively.

    Returns:
        List of generated file paths.
    """
    in_path = Path(input_dir)
    out_path = Path(output_dir)

    if not in_path.exists():
        raise FileNotFoundError(f"Diretório de entrada não encontrado: {in_path}")

    # Coletar arquivos candidatos
    patterns = ["*.dbc", "*.DBC", "*.dbf", "*.DBF"]
    files: list[Path] = []
    for pat in patterns:
        if recursive:
            files.extend(in_path.rglob(pat))
        else:
            files.extend(in_path.glob(pat))

    # Deduplicar mantendo ordem
    unique_files = list(dict.fromkeys(files))

    if not unique_files:
        logger.warning("Nenhum arquivo .dbc ou .dbf encontrado em %s", in_path)
        return []

    logger.info(
        "Convertendo %d arquivos de %s para %s (formato: %s, workers: %d)",
        len(unique_files),
        in_path,
        out_path,
        target_format,
        workers,
    )

    out_suffix = ".dbf" if target_format.lower() == "dbf" else ".parquet"
    converted: list[Path] = []

    def _task(file_path: Path) -> Path:
        rel = file_path.relative_to(in_path)
        dest_file = (out_path / rel).with_suffix(out_suffix)
        return convert_file(
            file_path,
            dest_file,
            target_format=target_format,
            compression=compression,
            clean=clean,
            lowercase=lowercase,
            keep_dbf=keep_dbf,
        )

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        futures = {pool.submit(_task, f): f for f in unique_files}
        for future in concurrent.futures.as_completed(futures):
            f_orig = futures[future]
            try:
                out_file = future.result()
                converted.append(out_file)
            except Exception as exc:
                logger.error("Falha ao converter %s: %s", f_orig, exc)
                raise

    return converted
