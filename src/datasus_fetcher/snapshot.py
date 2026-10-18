# Copyright (c) 2026 Komesu, D.K.
# Licensed under the MIT License.

"""Metadata-first listing: reads the ``datasus-metadata`` snapshot.

The ``datasus-metadata`` collector lists the DATASUS FTP once a day and writes
one JSON per dataset. When that snapshot is fresh (younger than
``DATASUS_METADATA_MAX_AGE_HOURS``, default 36 h) the fetcher can skip the
slow FTP ``LIST`` and use it instead. Any problem (unset directory, missing or
stale file, malformed JSON) returns ``None`` so callers fall back to the FTP.

This module only reads files: it has no dependency on ``datasus-metadata``,
``quantilica-cli`` or ``quantilica-catalog``.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import time
from pathlib import Path

from . import logger
from .storage import DataPartition, RemoteFile

ENV_DIR = "DATASUS_METADATA_DIR"
ENV_MAX_AGE = "DATASUS_METADATA_MAX_AGE_HOURS"
DEFAULT_MAX_AGE_HOURS = 36.0

_KINDS = {"data": "data", "doc": "documentation", "aux": "auxiliary"}


def metadata_dir() -> Path | None:
    """Returns the snapshot directory from the environment, if configured."""
    value = os.environ.get(ENV_DIR, "").strip()
    return Path(value) if value else None


def max_age_hours() -> float:
    """Returns the maximum accepted snapshot age, in hours."""
    try:
        return float(os.environ[ENV_MAX_AGE])
    except (KeyError, ValueError):
        return DEFAULT_MAX_AGE_HOURS


def load_snapshot(
    kind: str,
    dataset: str,
    base_dir: Path | None = None,
    max_age: float | None = None,
    now: float | None = None,
) -> list[dict] | None:
    """Loads the raw snapshot records of a dataset when the file is fresh.

    Args:
        kind (str): ``"data"``, ``"doc"`` or ``"aux"``.
        dataset (str): Dataset (or documentation/auxiliary group) ID.
        base_dir (Path | None): Snapshot root; defaults to ``DATASUS_METADATA_DIR``.
        max_age (float | None): Maximum age in hours; defaults to the env value.
        now (float | None): Current epoch seconds (testing hook).

    Returns:
        list[dict] | None: The records, or None to signal an FTP fallback.
    """
    base_dir = base_dir if base_dir is not None else metadata_dir()
    if base_dir is None:
        return None
    path = base_dir / _KINDS[kind] / f"{dataset}.json"
    max_age = max_age if max_age is not None else max_age_hours()
    now = now if now is not None else time.time()
    try:
        age_h = (now - path.stat().st_mtime) / 3600
        if age_h > max_age:
            logger.info(
                "snapshot %s stale (%.1f h > %.1f h); using FTP", path, age_h, max_age
            )
            return None
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        logger.info("snapshot %s unavailable (%s); using FTP", path, exc)
        return None
    if not isinstance(data, list):
        return None
    return data


def _partition(raw: dict) -> DataPartition:
    # datasus-metadata names the file suffix ``subpartition``; here it is ``version``.
    return DataPartition(
        uf=raw.get("uf"),
        year=raw.get("year"),
        month=raw.get("month"),
        version=raw.get("version") or raw.get("subpartition"),
    )


def snapshot_data_files(dataset: str, **kwargs) -> list[RemoteFile] | None:
    """Returns the dataset's data files from the snapshot, or None."""
    records = load_snapshot("data", dataset, **kwargs)
    if records is None:
        return None
    try:
        return [
            RemoteFile(
                filename=r["filename"],
                full_path=r["full_path"],
                datetime=dt.datetime.fromisoformat(r["datetime"]),
                extension=r["extension"],
                size=r["size"],
                dataset=dataset,
                preliminary=r.get("preliminary", False),
                partition=_partition(r["partition"]),
            )
            for r in records
        ]
    except (KeyError, TypeError, ValueError) as exc:
        logger.warning("snapshot of %s malformed (%s); using FTP", dataset, exc)
        return None


def snapshot_support_files(kind: str, dataset: str, **kwargs) -> list[dict] | None:
    """Returns documentation/auxiliary files from the snapshot, or None.

    Records use the same shape as ``fetcher.list_documentation_files``
    (``datetime`` parsed to ``datetime.datetime``).
    """
    records = load_snapshot(kind, dataset, **kwargs)
    if records is None:
        return None
    try:
        return [
            {
                "filename": r["filename"],
                "full_path": r["full_path"],
                "datetime": dt.datetime.fromisoformat(r["datetime"]),
                "extension": r["extension"],
                "size": r["size"],
            }
            for r in records
        ]
    except (KeyError, TypeError, ValueError) as exc:
        logger.warning(
            "snapshot of %s/%s malformed (%s); using FTP", kind, dataset, exc
        )
        return None
