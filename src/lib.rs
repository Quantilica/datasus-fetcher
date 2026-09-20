//! Extensão nativa PyO3 em Rust para descompressão de arquivos .dbc do DATASUS.

use pyo3::exceptions::PyIOError;
use pyo3::prelude::*;
use std::fs::File;
use std::io::{BufReader, BufWriter, Read, Write};
use std::path::Path;

/// Descomprime um arquivo `.dbc` (PKWARE DCL implode) diretamente para um arquivo `.dbf` em disco.
///
/// A operação roda com streaming e buffers de 64 KB, liberando o GIL do Python
/// durante a descompressão para permitir paralelismo real em multi-threading.
///
/// Args:
///     input_path (str): Caminho do arquivo .dbc de entrada.
///     output_path (str): Caminho de destino para gravação do .dbf.
///
/// Returns:
///     int: Quantidade de bytes gravados no arquivo .dbf.
#[pyfunction]
fn decompress(py: Python<'_>, input_path: &str, output_path: &str) -> PyResult<u64> {
    py.allow_threads(|| {
        let in_file = File::open(Path::new(input_path)).map_err(|e| {
            PyIOError::new_err(format!(
                "Erro ao abrir arquivo .dbc de entrada '{}': {}",
                input_path, e
            ))
        })?;
        let buf_in = BufReader::with_capacity(64 * 1024, in_file);

        let mut dbf_reader = datasus_dbc::into_dbf_reader(buf_in).map_err(|e| {
            PyIOError::new_err(format!(
                "Erro ao decodificar cabeçalho .dbc de '{}': {}",
                input_path, e
            ))
        })?;

        let out_file = File::create(Path::new(output_path)).map_err(|e| {
            PyIOError::new_err(format!(
                "Erro ao criar arquivo .dbf de destino '{}': {}",
                output_path, e
            ))
        })?;
        let mut buf_out = BufWriter::with_capacity(64 * 1024, out_file);

        let bytes_copied = std::io::copy(&mut dbf_reader, &mut buf_out).map_err(|e| {
            PyIOError::new_err(format!(
                "Erro ao descompactar dados para '{}': {}",
                output_path, e
            ))
        })?;

        buf_out.flush().map_err(|e| {
            PyIOError::new_err(format!(
                "Erro ao finalizar gravação em '{}': {}",
                output_path, e
            ))
        })?;

        Ok(bytes_copied)
    })
}

/// Descomprime bytes de um arquivo `.dbc` em memória e retorna os bytes do `.dbf`.
///
/// Args:
///     input_bytes (bytes): Buffer de bytes .dbc.
///
/// Returns:
///     bytes: Buffer descompactado .dbf.
#[pyfunction]
fn decompress_bytes(py: Python<'_>, input_bytes: &[u8]) -> PyResult<Vec<u8>> {
    py.allow_threads(|| {
        let mut reader = datasus_dbc::into_dbf_reader(input_bytes).map_err(|e| {
            PyIOError::new_err(format!("Erro ao decodificar cabeçalho .dbc: {}", e))
        })?;
        let mut output = Vec::new();
        reader.read_to_end(&mut output).map_err(|e| {
            PyIOError::new_err(format!("Erro ao descompactar dados .dbc: {}", e))
        })?;
        Ok(output)
    })
}

#[pymodule]
fn _datasus_dbc(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(decompress, m)?)?;
    m.add_function(wrap_pyfunction!(decompress_bytes, m)?)?;
    Ok(())
}
