# Copyright (c) 2026 Komesu, D.K.
# Licensed under the MIT License.

"""Typer plugin for quantilica-cli integration."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Annotated

import typer
from quantilica.cli.sdk import FetcherApp
from quantilica.cli.ui import get_console, setup_rich_logging
from quantilica.core.ftp import FtpClient
from rich.rule import Rule
from rich.table import Table

from datasus_fetcher import fetcher, meta
from datasus_fetcher.fetcher import FTP_HOST
from datasus_fetcher.slicer import Slicer
from datasus_fetcher.storage import get_files_metadata

_DEFAULT_OUTPUT = Path("/data/datasus")
console = get_console()

_FTP_CONN = None


def _systems_to_datasets(systems: list[str] | None) -> list[str] | None:
    """Expands ``--system`` values (case-insensitive, comma-separated) to datasets.

    Args:
        systems (list[str] | None): Raw ``--system`` option values.

    Returns:
        list[str] | None: Unique dataset IDs, or None when nothing requested.

    Raises:
        typer.BadParameter: On an unrecognized system/dataset name.
    """
    if not systems:
        return None
    items: list[str] = []
    for chunk in systems:
        items.extend(piece.strip() for piece in chunk.split(",") if piece.strip())
    if not items:
        return None
    try:
        return meta.expand_systems(items)
    except KeyError as exc:
        raise typer.BadParameter(str(exc.args[0])) from exc


def resolve_dataset_targets(
    datasets: list[str] | None, systems: list[str] | None
) -> list[str] | None:
    """Merges positional datasets with ``--system`` resolution.

    Args:
        datasets (list[str] | None): Positional dataset IDs.
        systems (list[str] | None): Dataset IDs expanded from ``--system``.

    Returns:
        list[str] | None: Effective target datasets; None means 'all'.
    """
    if systems:
        merged = list(systems)
        if datasets:
            known = set(systems)
            for dataset in datasets:
                if dataset.lower() not in known:
                    merged.append(dataset)
        return merged
    return datasets


def _get_ftp():
    global _FTP_CONN
    if _FTP_CONN is None:
        _FTP_CONN = fetcher.connect()
    return _FTP_CONN


def datasus_list_datasets(group: str) -> list[dict]:
    """Lists dataset entries for a specific group (dataset ID).

    Args:
        group (str): The dataset ID (e.g., 'sih-rd').

    Returns:
        list[dict]: A list of dataset entries.
    """
    ftp = _get_ftp()
    entries = []

    if group in meta.datasets:
        for f in fetcher.list_dataset_files(ftp, group):
            entries.append(
                {
                    "id": f.filename,
                    "url": f.full_path,
                    "group": group,
                    "dataset": group,
                    "partition": str(f.partition) if f.partition else "—",
                    "remote_file": f,
                    "type": "data",
                    "size": f.size,
                }
            )

    if group in meta.docs:
        for doc in fetcher.list_documentation_files(ftp, group):
            entries.append(
                {
                    "id": doc["filename"],
                    "url": doc["full_path"],
                    "group": group,
                    "dataset": group,
                    "type": "doc",
                    "datetime": doc["datetime"],
                    "size": doc["size"],
                    "extension": doc.get("extension"),
                }
            )

    if group in meta.auxiliary_tables:
        for aux in fetcher.list_auxiliary_tables_files(ftp, group):
            entries.append(
                {
                    "id": aux["filename"],
                    "url": aux["full_path"],
                    "group": group,
                    "dataset": group,
                    "type": "aux",
                    "datetime": aux["datetime"],
                    "size": aux["size"],
                    "extension": aux.get("extension"),
                }
            )

    return entries


def datasus_path_builder(output_dir: Path, entry: dict, last_modified) -> Path:
    """Builds the local file path for a dataset entry.

    Args:
        output_dir (Path): The base output directory.
        entry (dict): The dataset entry metadata.
        last_modified: The last modified timestamp.

    Returns:
        Path: The constructed local file path.
    """
    if entry["type"] == "data":
        from datasus_fetcher.storage import get_data_filepath

        return get_data_filepath(output_dir, entry["remote_file"])
    elif entry["type"] == "doc":
        filename, extension = entry["id"].rsplit(".", 1)
        filename = f"{filename}@{entry['datetime']:%Y%m%d}.{extension}"
        return output_dir / "_documentacao" / entry["dataset"] / filename
    elif entry["type"] == "aux":
        filename, extension = entry["id"].rsplit(".", 1)
        filename = f"{filename}@{entry['datetime']:%Y%m%d}.{extension}"
        return output_dir / "_auxiliar" / entry["dataset"] / filename
    return output_dir / (entry.get("id") or "unknown")


fetcher_app = FetcherApp(
    name="datasus-fetcher",
    help="Dados brutos do DATASUS (SIH, SIM, CNES, etc.).",
    groups_dict=meta.datasets,
    aliases_dict={},
    list_datasets=datasus_list_datasets,
    path_builder=datasus_path_builder,
    default_output=_DEFAULT_OUTPUT,
    client=FtpClient(FTP_HOST),
)

app = fetcher_app.app


@app.command("list")
def cmd_list(
    datasets: Annotated[
        list[str] | None,
        typer.Argument(help="Datasets a listar (omitir para todos)"),
    ] = None,
    systems: Annotated[
        list[str] | None,
        typer.Option(
            "-s",
            "--system",
            help=(
                "Sistema(is) a listar (ex: sim, sinasc). Aceita valores "
                "separados por vírgula e múltiplas ocorrências; "
                "case-insensitive"
            ),
        ),
    ] = None,
    verbose: Annotated[bool, typer.Option("--verbose", help="Logs detalhados")] = False,
) -> None:
    """Listar datasets disponíveis no DATASUS."""
    setup_rich_logging(verbose, console=console)
    systems = _systems_to_datasets(systems)
    targets = resolve_dataset_targets(datasets, systems) or list(meta.datasets.keys())
    with console.status("[cyan]Conectando ao FTP do DATASUS...[/cyan]"):
        _get_ftp()

    total_size = total_files = 0
    t = Table(show_header=True, header_style="bold")
    t.add_column("Dataset", style="cyan")
    t.add_column("Arquivos (Data)", justify="right")
    t.add_column("Tamanho (Data)", justify="right")

    for dataset in sorted(targets):
        if dataset not in meta.datasets:
            console.print(f"[red]Dataset '{dataset}' não reconhecido.[/red]")
            continue
        files = [e for e in fetcher_app.list_datasets(dataset) if e["type"] == "data"]
        if not files:
            continue
        size = sum(f["size"] or 0 for f in files)
        n = len(files)
        total_size += size
        total_files += n
        t.add_row(dataset, str(n), f"{size / 2**20:.1f} MB")

    _FTP_CONN.close()
    console.print(t)
    console.print(
        f"[bold]Total:[/bold] {total_files} arquivos, {total_size / 2**30:.1f} GB"
    )


@app.command("sync")
def cmd_sync(
    datasets: Annotated[
        list[str] | None,
        typer.Argument(help="Datasets (ex: sih-rd, cnes-dc). Omitir para todos."),
    ] = None,
    systems: Annotated[
        list[str] | None,
        typer.Option(
            "-s",
            "--system",
            help=(
                "Sistema(is) a sincronizar (ex: sim, sih). Aceita valores "
                "separados por vírgula e múltiplas ocorrências; "
                "case-insensitive"
            ),
        ),
    ] = None,
    output: Annotated[
        Path, typer.Option("-o", "--output", help="Diretório de saída")
    ] = _DEFAULT_OUTPUT,
    start: Annotated[
        str,
        typer.Option("--start", help="Período inicial (ex: 2001 ou 2001-01)"),
    ] = "",
    end: Annotated[
        str,
        typer.Option("--end", help="Período final (ex: 2020 ou 2020-12)"),
    ] = "",
    regions: Annotated[
        list[str] | None,
        typer.Option("--regions", help="Regiões (ex: br, ac, am)"),
    ] = None,
    threads: Annotated[
        int, typer.Option("-t", "--threads", help="Downloads simultâneos")
    ] = 2,
    docs: Annotated[
        bool,
        typer.Option("--docs", help="Também baixar a documentação"),
    ] = False,
    aux: Annotated[
        bool,
        typer.Option("--aux", help="Também baixar as tabelas auxiliares"),
    ] = False,
    dry_run: Annotated[
        bool, typer.Option("--dry-run", help="Listar sem baixar")
    ] = False,
    convert: Annotated[
        bool,
        typer.Option("--convert", help="Converter para Parquet após download"),
    ] = False,
    parquet_dir: Annotated[
        Path | None,
        typer.Option("--parquet-dir", help="Diretório para salvar arquivos Parquet"),
    ] = None,
    verbose: Annotated[bool, typer.Option("--verbose", help="Logs detalhados")] = False,
) -> None:
    """Sincronizar dados brutos do DATASUS."""
    setup_rich_logging(verbose, console=console)
    systems = _systems_to_datasets(systems)
    targets = resolve_dataset_targets(datasets, systems) or list(meta.datasets.keys())
    slicer = Slicer(start_time=start, end_time=end, regions=regions)

    try:
        with console.status(
            "[cyan]Conectando ao FTP do DATASUS para listar arquivos...[/cyan]"
        ):
            _get_ftp()

        entries = []
        for dataset in sorted(targets):
            if dataset not in meta.datasets:
                console.print(f"[red]Dataset '{dataset}' não reconhecido.[/red]")
                continue

            for e in fetcher_app.list_datasets(dataset):
                if e["type"] == "data":
                    if slicer is not None and not slicer(e["remote_file"]):
                        continue
                    entries.append(e)
                elif e["type"] == "doc" and docs:
                    entries.append(e)
                elif e["type"] == "aux" and aux:
                    entries.append(e)

        _FTP_CONN.close()

        if dry_run:
            total_size = sum(e["size"] or 0 for e in entries)
            t = Table(show_header=True, header_style="bold")
            t.add_column("Dataset", style="cyan")
            t.add_column("Tipo")
            t.add_column("Partição")
            t.add_column("Tamanho", justify="right")
            t.add_column("Path")

            for e in entries:
                t.add_row(
                    e["dataset"],
                    e["type"],
                    e.get("partition", "—"),
                    f"{e['size'] / 2**20:.1f} MB",
                    e["url"],
                )
            console.print(t)
            console.print(
                f"\n[bold]Total:[/bold] {len(entries)} arquivos, "
                f"{total_size / 2**30:.2f} GB"
            )
            return

        fetcher_app.download_datasets(entries, output, workers=threads)

        if convert:
            try:
                from datasus_fetcher import _HAS_ANALYTICS, convert_directory

                if not _HAS_ANALYTICS:
                    raise ImportError
            except ImportError:
                console.print(
                    "[red]Erro:[/red] --convert requer extras de análise: "
                    "pip install datasus-fetcher[analytics]"
                )
                raise typer.Exit(1) from None

            parquet_out = parquet_dir or output
            console.print(Rule("[bold]Conversão para Parquet[/bold]"))
            convert_directory(
                output,
                parquet_out,
                target_format="parquet",
                workers=threads,
            )
            console.print(
                f"[green]✓[/green] Parquet salvo em [bold]{parquet_out}[/bold]"
            )

    except KeyboardInterrupt:
        console.print("[yellow]Download cancelado pelo usuário.[/yellow]")
        raise typer.Exit(code=130) from None


@app.command("decompress")
def cmd_decompress(
    input: Annotated[
        Path,
        typer.Option(
            "-i", "--input", help="Arquivo .dbc ou diretório com arquivos .dbc"
        ),
    ],
    output: Annotated[
        Path | None,
        typer.Option("-o", "--output", help="Destino do arquivo ou diretório .dbf"),
    ] = None,
    workers: Annotated[
        int, typer.Option("--workers", help="Workers para conversão de pastas")
    ] = 4,
    verbose: Annotated[bool, typer.Option("--verbose", help="Logs detalhados")] = False,
) -> None:
    """Descompactar arquivo ou pasta .dbc para .dbf nativamente."""
    setup_rich_logging(verbose, console=console)
    if input.is_dir():
        from datasus_fetcher.wrangling import convert_directory

        out_dir = output or input
        convert_directory(input, out_dir, target_format="dbf", workers=workers)
        console.print(
            f"[green]✓[/green] Descompressão concluída em [bold]{out_dir}[/bold]"
        )
    else:
        from datasus_fetcher import decompress_dbc

        dest = decompress_dbc(input, output)
        console.print(f"[green]✓[/green] Descompactado para [bold]{dest}[/bold]")


@app.command("convert")
def cmd_convert(
    input: Annotated[
        Path,
        typer.Option(
            "-i",
            "--input",
            help="Arquivo ou diretório de origem (.dbc ou .dbf)",
        ),
    ],
    output: Annotated[
        Path | None,
        typer.Option(
            "-o", "--output", help="Destino do arquivo ou diretório convertido"
        ),
    ] = None,
    format: Annotated[
        str,
        typer.Option("--format", help="Formato de saída (parquet ou dbf)"),
    ] = "parquet",
    compression: Annotated[
        str,
        typer.Option("--compression", help="Compressão do Parquet (zstd, snappy)"),
    ] = "zstd",
    clean: Annotated[
        bool,
        typer.Option("--clean/--no-clean", help="Aplicar limpeza e tipagem canônica"),
    ] = True,
    lowercase: Annotated[
        bool,
        typer.Option(
            "--lowercase/--no-lowercase",
            help="Converter nomes de colunas para minúsculas",
        ),
    ] = True,
    keep_dbf: Annotated[
        bool,
        typer.Option("--keep-dbf", help="Manter arquivos intermediários .dbf gerados"),
    ] = False,
    workers: Annotated[
        int, typer.Option("--workers", help="Workers paralelos para diretórios")
    ] = 4,
    verbose: Annotated[bool, typer.Option("--verbose", help="Logs detalhados")] = False,
) -> None:
    """Converter arquivos .dbc ou .dbf para Parquet ou DBF."""
    setup_rich_logging(verbose, console=console)
    if format == "parquet":
        try:
            from datasus_fetcher import _HAS_ANALYTICS

            if not _HAS_ANALYTICS:
                raise ImportError
        except ImportError:
            console.print(
                "[red]Erro:[/red] conversão para Parquet requer extras de análise: "
                "pip install datasus-fetcher[analytics]"
            )
            raise typer.Exit(1) from None

    from datasus_fetcher.wrangling import convert_directory, convert_file

    if input.is_dir():
        out_dir = output or input
        convert_directory(
            input,
            out_dir,
            target_format=format,
            compression=compression,
            clean=clean,
            lowercase=lowercase,
            keep_dbf=keep_dbf,
            workers=workers,
        )
        console.print(f"[green]✓[/green] Conversão concluída em [bold]{out_dir}[/bold]")
    else:
        dest = convert_file(
            input,
            output,
            target_format=format,
            compression=compression,
            clean=clean,
            lowercase=lowercase,
            keep_dbf=keep_dbf,
        )
        console.print(f"[green]✓[/green] Arquivo convertido: [bold]{dest}[/bold]")


@app.command("pipeline")
def cmd_pipeline(
    datasets: Annotated[
        list[str] | None,
        typer.Argument(help="Datasets a baixar (omitir para todos)"),
    ] = None,
    systems: Annotated[
        list[str] | None,
        typer.Option(
            "-s",
            "--system",
            help=(
                "Sistema(is) a processar (ex: sim, sinasc). Aceita valores "
                "separados por vírgula e múltiplas ocorrências; "
                "case-insensitive"
            ),
        ),
    ] = None,
    output: Annotated[
        Path,
        typer.Option("-o", "--output", help="Diretório de dados brutos"),
    ] = _DEFAULT_OUTPUT,
    parquet_dir: Annotated[
        Path | None,
        typer.Option("--parquet-dir", help="Diretório para os Parquets"),
    ] = None,
    start: Annotated[
        str, typer.Option("--start", help="Período inicial (ex: 2024-01)")
    ] = "",
    end: Annotated[str, typer.Option("--end", help="Período final (ex: 2024-12)")] = "",
    regions: Annotated[
        list[str] | None, typer.Option("--regions", help="Regiões (ex: sp, rj)")
    ] = None,
    threads: Annotated[
        int, typer.Option("-t", "--threads", help="Downloads paralelos")
    ] = 2,
    workers: Annotated[
        int, typer.Option("--workers", help="Workers de conversão Parquet")
    ] = 4,
    compression: Annotated[
        str, typer.Option("--compression", help="Compressão do Parquet")
    ] = "zstd",
    clean: Annotated[
        bool, typer.Option("--clean/--no-clean", help="Aplicar limpeza e tipagem")
    ] = True,
    lowercase: Annotated[
        bool, typer.Option("--lowercase/--no-lowercase", help="Colunas minúsculas")
    ] = True,
    docs: Annotated[bool, typer.Option("--docs", help="Baixar documentação")] = False,
    aux: Annotated[
        bool, typer.Option("--aux", help="Baixar tabelas auxiliares")
    ] = False,
    verbose: Annotated[bool, typer.Option("--verbose", help="Logs detalhados")] = False,
) -> None:
    """Pipeline completo do DATASUS (download FTP -> conversão Parquet)."""
    setup_rich_logging(verbose, console=console)
    try:
        from datasus_fetcher import _HAS_ANALYTICS, convert_directory

        if not _HAS_ANALYTICS:
            raise ImportError
    except ImportError:
        console.print(
            "[red]Erro:[/red] pipeline requer extras de análise: "
            "pip install datasus-fetcher[analytics]"
        )
        raise typer.Exit(1) from None

    console.print(Rule("[bold]Passo 1/2: Download FTP[/bold]"))
    cmd_sync(
        datasets=datasets,
        systems=systems,
        output=output,
        start=start,
        end=end,
        regions=regions,
        threads=threads,
        docs=docs,
        aux=aux,
        dry_run=False,
        convert=False,
        verbose=verbose,
    )

    console.print(Rule("[bold]Passo 2/2: Conversão para Parquet[/bold]"))
    parquet_out = parquet_dir or output
    convert_directory(
        output,
        parquet_out,
        target_format="parquet",
        compression=compression,
        clean=clean,
        lowercase=lowercase,
        workers=workers,
    )
    console.print(
        "[green]✓[/green] Pipeline concluído. Parquet salvo em "
        f"[bold]{parquet_out}[/bold]"
    )


@app.command("archive")
def cmd_archive(
    archive_data_dir: Annotated[
        Path,
        typer.Option(
            "--archive-data-dir",
            help="Diretório para onde mover arquivos antigos",
        ),
    ],
    output: Annotated[
        Path, typer.Option("-o", "--output", help="Diretório de dados fonte")
    ] = _DEFAULT_OUTPUT,
    verbose: Annotated[bool, typer.Option("--verbose", help="Logs detalhados")] = False,
) -> None:
    """Mover arquivos desatualizados para diretório de arquivo."""
    setup_rich_logging(verbose, console=console)
    for datasetdir in output.iterdir():
        for datepartitiondir in datasetdir.iterdir():
            for file in get_files_metadata(datepartitiondir):
                if not file.is_most_recent:
                    rel = file.filepath.relative_to(output)
                    dest = archive_data_dir / rel
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(file.filepath, dest)
