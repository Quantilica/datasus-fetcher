import re

from . import meta


def _get_year2(year_: str) -> int:
    if year_[0] in "789":
        year = 1900 + int(year_)
    else:
        year = 2000 + int(year_)
    return year


def _parse_uf_year2_month_filename(m: re.Match) -> dict:
    uf = m.group(1)
    year_ = m.group(2)
    year = _get_year2(year_)
    month = int(m.group(3))
    return {
        "uf": uf,
        "year": year,
        "month": month,
    }


def _parse_year_filename(m: re.Match) -> dict:
    year = int(m.group(1))
    return {
        "year": year,
    }


def _parse_year2_filename(m: re.Match) -> dict:
    year_ = m.group(1)
    year = _get_year2(year_)
    return {
        "year": year,
    }


def _parse_uf_year_filename(m: re.Match) -> dict:
    uf = m.group(1)
    year = int(m.group(2))
    return {
        "uf": uf,
        "year": year,
    }


def _parse_uf_year2_filename(m: re.Match) -> dict:
    uf = m.group(1)
    year_ = m.group(2)
    year = _get_year2(year_)
    return {
        "uf": uf,
        "year": year,
    }


def _parse_uf_filename(m: re.Match) -> dict:
    uf = m.group(1)
    return {
        "uf": uf,
    }


def _parse_uf_year2_month_filename_sia_pa(m: re.Match) -> dict:
    uf = m.group(1)
    year_ = m.group(2)
    year = _get_year2(year_)
    month = int(m.group(3))
    version = m.group(4)
    return {
        "uf": uf,
        "year": year,
        "month": month,
        "version": version,
    }


def get_pattern(period: dict) -> re.Pattern:
    fn_prefix = period["filename_prefix"]
    fn_pattern = period["filename_pattern"]
    fn_ext = period["extension"]
    pattern = re.compile(f"^{fn_prefix}{fn_pattern}\\.{fn_ext}$".lower())
    return pattern


def parse_filename(m: re.Match, pattern: str) -> dict:
    """Parse remote file name and returns a dictionary with metadata for data
    partitioning.

    :param m: a re.Match object
    :param pattern: a string pattern from .meta.datasets

    """
    match pattern:
        case meta.uf_year_pattern:
            return _parse_uf_year_filename(m)
        case meta.uf_year2_pattern:
            return _parse_uf_year2_filename(m)
        case meta.uf_year2_month_pattern:
            return _parse_uf_year2_month_filename(m)
        case meta.uf_year2_month_pattern_sia_pa:
            return _parse_uf_year2_month_filename_sia_pa(m)
        case meta.year_pattern:
            return _parse_year_filename(m)
        case meta.year2_pattern:
            return _parse_year2_filename(m)
        case meta.uf_mapas_year_pattern:
            return _parse_uf_year_filename(m)
        case meta.uf_cnv_pattern:
            return _parse_uf_filename(m)
        case "base_territorial":
            return {}
        case _:
            raise ValueError(f"Pattern not found: {pattern}")
