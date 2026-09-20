"""CLI standalone para datasus-fetcher."""

from __future__ import annotations

import argparse
import logging
import shutil
import sys
from pathlib import Path

from quantilica.core.logging import configure_cli_logging

from . import (
    _HAS_ANALYTICS,
    __version__,
    decompress_dbc,
    fetcher,
    logger,
    meta,
)
from .slicer import Slicer
from .storage import File, get_files_metadata


def list_datasets(args: argparse.Namespace) -> None:
    """Lists datasets available on the DATASUS FTP server.

    Args:
        args (argparse.Namespace): The parsed command line arguments.
    """
    if not args.datasets:
        datasets = meta.datasets
    else:
        datasets = args.datasets

    ftp = fetcher.connect()

    total_size = 0
    total_n_files = 0

    print(
        "|".join(
            (
                "-----------Dataset----------",
                "---Nº files---",
                "--Total size--",
                "------Period range------",
            )
        )
    )

    for dataset in sorted(datasets):
        if dataset not in meta.datasets:
            print("Dataset", dataset, "not recognized.")
            continue
        dataset_files_list = fetcher.list_dataset_files(ftp, dataset)
        if len(dataset_files_list) == 0:
            continue
        dataset_size = sum(f.size or 0 for f in dataset_files_list)
        dataset_n_files = len(dataset_files_list)
        total_size += dataset_size
        total_n_files += dataset_n_files
        first = last = "----"
        if dataset_files_list:
            if "year" in meta.datasets[dataset]["partition"]:
                first = min(
                    dataset_files_list,
                    key=lambda x: x.partition.year or 0,
                )
                first = f"{first.partition.year}"
                last = max(
                    dataset_files_list,
                    key=lambda x: x.partition.year or 0,
                )
                last = f"{last.partition.year}"
            elif "yearmonth" in meta.datasets[dataset]["partition"]:
                first = min(
                    dataset_files_list,
                    key=lambda x: f"{x.partition.year}{x.partition.month:02}",
                )
                first = f"{first.partition.year}-{first.partition.month:02}"
                last = max(
                    dataset_files_list,
                    key=lambda x: f"{x.partition.year}{x.partition.month:02}",
                )
                last = f"{last.partition.year}-{last.partition.month:02}"
        date_range = f"{first: <7} to {last: <7}"
        msg = " | ".join(
            [
                f"{dataset: <27}",
                f"{dataset_n_files: >6} files",
                f"{dataset_size / 2**20: >9.1f} MB",
                f"from {date_range: ^18}",
            ]
        )
        print(msg)

    print(f"Total size: {total_size / 2**30:.1f} GB")
    print(f"Total files: {total_n_files} files")

    ftp.close()


def sync_data(args: argparse.Namespace) -> None:
    """Synchronizes raw data from DATASUS to local storage.

    Args:
        args (argparse.Namespace): The parsed command line arguments.
    """
    data_dir = args.output
    if not args.datasets:
        datasets = list(meta.datasets.keys())
    else:
        datasets = args.datasets

    slicer = Slicer(
        start_time=args.start,
        end_time=args.end,
        regions=args.regions,
    )

    if args.dry_run:
        ftp = fetcher.connect()
        total_size = 0
        total_files = 0
        for dataset in sorted(datasets):
            if dataset not in meta.datasets:
                print(f"Dataset {dataset!r} not recognized.")
                continue
            for remote_file in fetcher.list_dataset_files(ftp, dataset):
                if slicer is not None and not slicer(remote_file):
                    continue
                print(
                    f"{remote_file.dataset: <27} "
                    f"{str(remote_file.partition): <20} "
                    f"{remote_file.size / 2**20: >9.1f} MB  "
                    f"{remote_file.full_path}"
                )
                total_size += remote_file.size
                total_files += 1
        ftp.close()
        print(f"\nTotal: {total_files} files, {total_size / 2**30:.2f} GB")
        return

    fetcher.download_data(
        datasets=sorted(datasets),
        destdir=data_dir,
        threads=args.threads,
        slicer=slicer,
        show_progress=not args.verbose,
    )

    if args.docs:
        ftp = fetcher.connect()
        doc_targets = set(datasets) & set(meta.docs.keys())
        for dataset in sorted(doc_targets):
            for _ in fetcher.download_documentation(ftp, dataset, data_dir):
                pass
        ftp.close()

    if args.aux:
        ftp = fetcher.connect()
        aux_targets = set(datasets) & set(meta.auxiliary_tables.keys())
        for dataset in sorted(aux_targets):
            for _ in fetcher.download_auxiliary_tables(ftp, dataset, data_dir):
                pass
        ftp.close()

    if getattr(args, "convert", False):
        if not _HAS_ANALYTICS:
            raise SystemExit(
                "Erro: --convert requer extras de análise: "
                "pip install datasus-fetcher[analytics]"
            )
        from .wrangling import convert_directory

        parquet_out = args.parquet_dir or data_dir
        convert_directory(
            data_dir,
            parquet_out,
            target_format="parquet",
            workers=args.threads,
        )


def archive(args: argparse.Namespace) -> None:
    """Moves outdated files to an archive directory.

    Args:
        args (argparse.Namespace): The parsed command line arguments.
    """
    data_dir: Path = args.output
    archivedatadir: Path = args.archive_data_dir
    for datasetdir in data_dir.iterdir():
        for datepartitiondir in datasetdir.iterdir():
            files = get_files_metadata(datepartitiondir)
            for file in files:
                file: File
                if not file.is_most_recent:
                    rel_filepath = file.filepath.relative_to(data_dir)
                    archivefilepath = archivedatadir / rel_filepath
                    logger.info(f"Moving {file.filepath} to {archivefilepath}")
                    archivefilepath.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(file.filepath, archivefilepath)


def handle_decompress(args: argparse.Namespace) -> None:
    """Handles the 'decompress' CLI command."""
    input_path: Path = args.input
    output_path: Path | None = args.output

    if input_path.is_dir():
        out_dir = output_path or input_path
        from .wrangling import convert_directory

        convert_directory(
            input_path,
            out_dir,
            target_format="dbf",
            workers=args.workers,
        )
        print(f"Descompressão de diretório concluída em {out_dir}")
    else:
        dest = decompress_dbc(input_path, output_path)
        print(f"Descompressão concluída: {dest}")


def handle_convert(args: argparse.Namespace) -> None:
    """Handles the 'convert' CLI command."""
    if args.format == "parquet" and not _HAS_ANALYTICS:
        raise SystemExit(
            "Erro: conversão e tratamento requerem extras de análise: "
            "pip install datasus-fetcher[analytics]"
        )

    from .wrangling import convert_directory, convert_file

    input_path: Path = args.input
    output_path: Path | None = args.output

    if input_path.is_dir():
        out_dir = output_path or input_path
        convert_directory(
            input_path,
            out_dir,
            target_format=args.format,
            compression=args.compression,
            clean=not args.no_clean,
            lowercase=not args.no_lowercase,
            keep_dbf=args.keep_dbf,
            workers=args.workers,
        )
    else:
        convert_file(
            input_path,
            output_path,
            target_format=args.format,
            compression=args.compression,
            clean=not args.no_clean,
            lowercase=not args.no_lowercase,
            keep_dbf=args.keep_dbf,
        )
    print("Conversão concluída com sucesso.")


def handle_pipeline(args: argparse.Namespace) -> None:
    """Handles the 'pipeline' CLI command (sync -> convert)."""
    if not _HAS_ANALYTICS:
        raise SystemExit(
            "Erro: pipeline (conversão) requer extras de análise: "
            "pip install datasus-fetcher[analytics]"
        )

    from .wrangling import convert_directory

    print("Passo 1/2: Sincronizando dados brutos via FTP...")
    sync_data(args)

    parquet_out = args.parquet_dir or args.output
    print("Passo 2/2: Convertendo e tratando para Parquet...")
    convert_directory(
        args.output,
        parquet_out,
        target_format="parquet",
        compression=args.compression,
        clean=not args.no_clean,
        lowercase=not args.no_lowercase,
        workers=args.threads,
    )
    print(f"Pipeline concluído. Parquet salvo em {parquet_out}")


def get_parser() -> argparse.ArgumentParser:
    """Creates and configures the argument parser for the CLI.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    parser = argparse.ArgumentParser(
        prog="datasus-fetcher",
        description="Baixar e processar dados brutos do DATASUS.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Exibir logs detalhados em vez de barra de progresso",
    )
    parser.set_defaults(func=lambda _: parser.print_help())
    subparsers = parser.add_subparsers(dest="command")

    # list
    subparser_list = subparsers.add_parser("list", help="Listar datasets disponíveis")
    subparser_list.add_argument(
        "datasets",
        nargs="*",
        help="Datasets a listar (ex: sih-rd, cnes-dc)",
    )
    subparser_list.set_defaults(func=list_datasets)

    # sync
    subparser_sync = subparsers.add_parser(
        "sync", help="Sincronizar dados brutos do DATASUS"
    )
    subparser_sync.add_argument(
        "datasets",
        nargs="*",
        help="Datasets a baixar (ex: sih-rd, cnes-dc). Omitir para todos.",
    )
    subparser_sync.add_argument(
        "--start",
        default="",
        help="Período inicial (ex: 2001 ou 2001-01)",
    )
    subparser_sync.add_argument(
        "--end",
        default="",
        help="Período final (ex: 2020 ou 2020-12)",
    )
    subparser_sync.add_argument(
        "--regions",
        nargs="+",
        help="Regiões a baixar (ex: br, ac, am, ce)",
    )
    subparser_sync.add_argument(
        "-o",
        "--output",
        dest="output",
        type=Path,
        default=Path("/data/datasus"),
        help="Diretório de saída (padrão: /data/datasus)",
    )
    subparser_sync.add_argument(
        "-t",
        "--threads",
        dest="threads",
        type=int,
        default=2,
        help="Downloads simultâneos (padrão: 2)",
    )
    subparser_sync.add_argument(
        "--docs",
        action="store_true",
        default=False,
        help="Também baixar a documentação",
    )
    subparser_sync.add_argument(
        "--aux",
        action="store_true",
        default=False,
        help="Também baixar as tabelas auxiliares",
    )
    subparser_sync.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        default=False,
        help="Listar arquivos sem baixar",
    )
    subparser_sync.add_argument(
        "--convert",
        action="store_true",
        default=False,
        help="Converter automaticamente para Parquet após download",
    )
    subparser_sync.add_argument(
        "--parquet-dir",
        type=Path,
        default=None,
        help="Diretório de destino para Parquet (padrão: igual a --output)",
    )
    subparser_sync.set_defaults(func=sync_data)

    # decompress
    subparser_decomp = subparsers.add_parser(
        "decompress", help="Descompactar arquivo ou pasta .dbc para .dbf nativamente"
    )
    subparser_decomp.add_argument(
        "-i",
        "--input",
        type=Path,
        required=True,
        help="Arquivo ou diretório de entrada .dbc",
    )
    subparser_decomp.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Destino do arquivo ou pasta .dbf",
    )
    subparser_decomp.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Workers para conversão de pastas",
    )
    subparser_decomp.set_defaults(func=handle_decompress)

    # convert
    subparser_convert = subparsers.add_parser(
        "convert", help="Converter arquivos .dbc ou .dbf para Parquet ou DBF"
    )
    subparser_convert.add_argument(
        "-i",
        "--input",
        type=Path,
        required=True,
        help="Arquivo ou diretório de origem (.dbc ou .dbf)",
    )
    subparser_convert.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Destino do arquivo ou diretório convertido",
    )
    subparser_convert.add_argument(
        "--format",
        choices=["parquet", "dbf"],
        default="parquet",
        help="Formato de saída (padrão: parquet)",
    )
    subparser_convert.add_argument(
        "--compression",
        default="zstd",
        help="Algoritmo de compressão Parquet (padrão: zstd)",
    )
    subparser_convert.add_argument(
        "--no-clean",
        action="store_true",
        default=False,
        help="Desativar sanitização e tipagem canônica",
    )
    subparser_convert.add_argument(
        "--no-lowercase",
        action="store_true",
        default=False,
        help="Manter nomes originais de colunas (não converter para minúsculas)",
    )
    subparser_convert.add_argument(
        "--keep-dbf",
        action="store_true",
        default=False,
        help="Manter arquivos intermediários .dbf gerados",
    )
    subparser_convert.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Número de workers paralelos para diretórios",
    )
    subparser_convert.set_defaults(func=handle_convert)

    # pipeline
    subparser_pipe = subparsers.add_parser(
        "pipeline", help="Pipeline completo (sync -> convert)"
    )
    subparser_pipe.add_argument(
        "datasets",
        nargs="*",
        help="Datasets a processar. Omitir para todos.",
    )
    subparser_pipe.add_argument(
        "--start",
        default="",
        help="Período inicial",
    )
    subparser_pipe.add_argument(
        "--end",
        default="",
        help="Período final",
    )
    subparser_pipe.add_argument(
        "--regions",
        nargs="+",
        help="Regiões a baixar",
    )
    subparser_pipe.add_argument(
        "-o",
        "--output",
        dest="output",
        type=Path,
        default=Path("/data/datasus"),
        help="Diretório de dados brutos (padrão: /data/datasus)",
    )
    subparser_pipe.add_argument(
        "--parquet-dir",
        type=Path,
        default=None,
        help="Diretório de destino dos arquivos Parquet",
    )
    subparser_pipe.add_argument(
        "-t",
        "--threads",
        dest="threads",
        type=int,
        default=2,
        help="Downloads e conversões simultâneos",
    )
    subparser_pipe.add_argument(
        "--compression",
        default="zstd",
        help="Compressão do Parquet (padrão: zstd)",
    )
    subparser_pipe.add_argument(
        "--no-clean",
        action="store_true",
        default=False,
        help="Desativar regras de limpeza de dados",
    )
    subparser_pipe.add_argument(
        "--no-lowercase",
        action="store_true",
        default=False,
        help="Manter maiúsculas nos nomes de colunas",
    )
    subparser_pipe.add_argument(
        "--docs",
        action="store_true",
        default=False,
        help="Também baixar documentação",
    )
    subparser_pipe.add_argument(
        "--aux",
        action="store_true",
        default=False,
        help="Também baixar tabelas auxiliares",
    )
    subparser_pipe.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Listar sem baixar",
    )
    subparser_pipe.set_defaults(func=handle_pipeline)

    # archive
    subparser_archive = subparsers.add_parser(
        "archive", help="Mover arquivos desatualizados para diretório de histórico"
    )
    subparser_archive.add_argument(
        "-o",
        "--output",
        dest="output",
        type=Path,
        default=Path("/data/datasus"),
        help="Diretório de origem (padrão: /data/datasus)",
    )
    subparser_archive.add_argument(
        "--archive-data-dir",
        type=Path,
        required=True,
        help="Diretório de destino para arquivos arquivados",
    )
    subparser_archive.set_defaults(func=archive)

    return parser


def main(argv: list[str] | None = None) -> None:
    """Main entry point for the CLI.

    Args:
        argv (list[str] | None, optional): The command line arguments. Defaults to None.
    """
    parser = get_parser()
    args = parser.parse_args(argv)
    configure_cli_logging(verbose=args.verbose)
    if not args.verbose:
        logging.getLogger("quantilica.core").setLevel(logging.WARNING)
        logging.getLogger("datasus_fetcher").setLevel(logging.WARNING)
    try:
        args.func(args)
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.", file=sys.stderr)
        sys.exit(130)


if __name__ == "__main__":
    main()
