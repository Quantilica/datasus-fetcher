"""Tests for the native Rust _datasus_dbc extension."""

from pathlib import Path

import pytest

from datasus_fetcher import _datasus_dbc

FIXTURE_DBC = (
    Path(__file__).parent.parent.parent
    / "quantilica-portal"
    / "tests"
    / "wasm"
    / "fixtures"
    / "DOAC1996.dbc"
)


def test_native_decompress(tmp_path: Path):
    """Test decompressing a real .dbc file with Rust into a .dbf file."""
    if not FIXTURE_DBC.exists():
        pytest.skip(f"Fixture não encontrada: {FIXTURE_DBC}")

    out_dbf = tmp_path / "output.dbf"
    bytes_written = _datasus_dbc.decompress(str(FIXTURE_DBC), str(out_dbf))

    assert out_dbf.exists()
    assert bytes_written > 0
    assert out_dbf.stat().st_size == bytes_written
    # O arquivo descompactado deve ter cabeçalho dBase III+ (0x03 ou 0x83)
    with open(out_dbf, "rb") as f:
        header_byte = f.read(1)
        assert header_byte in (b"\x03", b"\x83")


def test_native_decompress_bytes():
    """Test decompressing .dbc in-memory bytes."""
    if not FIXTURE_DBC.exists():
        pytest.skip(f"Fixture não encontrada: {FIXTURE_DBC}")

    raw_bytes = FIXTURE_DBC.read_bytes()
    dbf_bytes = _datasus_dbc.decompress_bytes(raw_bytes)

    assert isinstance(dbf_bytes, bytes)
    assert len(dbf_bytes) > len(raw_bytes)
    assert dbf_bytes[:1] in (b"\x03", b"\x83")


def test_native_decompress_nonexistent(tmp_path: Path):
    """Test error handling when input file does not exist."""
    fake_path = tmp_path / "nao_existe.dbc"
    out_path = tmp_path / "out.dbf"

    with pytest.raises(OSError) as excinfo:
        _datasus_dbc.decompress(str(fake_path), str(out_path))

    assert "Erro ao abrir arquivo" in str(excinfo.value)
