# Copyright (c) 2026 Komesu, D.K.
# Licensed under the MIT License.

"""Typer plugin for quantilica-cli integration."""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Annotated

import typer
from quantilica_core.cli import get_console, setup_rich_logging
from rich.table import Table

from datasus_fetcher import fetcher, meta
from datasus_fetcher.slicer import Slicer
from datasus_fetcher.storage import get_files_metadata

app = typer.Typer(help="Dados brutos do DATASUS (SIH, SIM, CNES, etc.).")

_DEFAULT_OUTPUT = Path("/data/datasus")
console = get_console()


@app.command("list")
def cmd_list(
    datasets: Annotated[
        list[str] | None,
        typer.Argument(help="Datasets a listar (omitir para todos)"),
    ] = None,
    verbose: Annotated[bool, typer.Option("--verbose", help="Logs detalhados")] = False,
) -> None:
    """Listar datasets disponíveis no DATASUS."""
    setup_rich_logging(verbose, console=console)
    targets = datasets if datasets else list(meta.datasets.keys())
    with console.status("[cyan]Conectando ao FTP do DATASUS...[/cyan]"):
        ftp = fetcher.connect()
    total_size = total_files = 0

    t = Table(show_header=True, header_style="bold")
    t.add_column("Dataset", style="cyan")
    t.add_column("Arquivos", justify="right")
    t.add_column("Tamanho", justify="right")

    for dataset in sorted(targets):
        if dataset not in meta.datasets:
            console.print(f"[red]Dataset '{dataset}' não reconhecido.[/red]")
            continue
        files = fetcher.list_dataset_files(ftp, dataset)
        if not files:
            continue
        size = sum(f.size or 0 for f in files)
        n = len(files)
        total_size += size
        total_files += n
        t.add_row(dataset, str(n), f"{size / 2**20:.1f} MB")

    ftp.close()
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
    verbose: Annotated[bool, typer.Option("--verbose", help="Logs detalhados")] = False,
) -> None:
    """Sincronizar dados brutos do DATASUS."""
    setup_rich_logging(verbose, console=console)
    targets = datasets if datasets else list(meta.datasets.keys())
    slicer = Slicer(start_time=start, end_time=end, regions=regions)

    try:
        if dry_run:
            with console.status("[cyan]Conectando ao FTP do DATASUS...[/cyan]"):
                ftp = fetcher.connect()
            total_size = total_n = 0

            t = Table(show_header=True, header_style="bold")
            t.add_column("Dataset", style="cyan")
            t.add_column("Partição")
            t.add_column("Tamanho", justify="right")
            t.add_column("Path")

            for dataset in sorted(targets):
                if dataset not in meta.datasets:
                    console.print(f"[red]Dataset '{dataset}' não reconhecido.[/red]")
                    continue
                for f in fetcher.list_dataset_files(ftp, dataset):
                    if slicer is not None and not slicer(f):
                        continue
                    t.add_row(
                        f.dataset,
                        str(f.partition),
                        f"{f.size / 2**20:.1f} MB",
                        f.full_path,
                    )
                    total_size += f.size
                    total_n += 1
            ftp.close()
            console.print(t)
            console.print(
                f"\n[bold]Total:[/bold] {total_n} arquivos, {total_size / 2**30:.2f} GB"
            )
            return

        fetcher.download_data(
            datasets=sorted(targets),
            destdir=output,
            threads=threads,
            slicer=slicer,
            show_progress=not verbose,
        )

        if docs:
            doc_targets = set(targets) & set(meta.docs.keys())
            with console.status("[cyan]Baixando documentação...[/cyan]"):
                ftp = fetcher.connect()
                for dataset in sorted(doc_targets):
                    for _ in fetcher.download_documentation(ftp, dataset, output):
                        pass
                ftp.close()
            console.print("[green]✓[/green] Documentação sincronizada.")

        if aux:
            aux_targets = set(targets) & set(meta.auxiliary_tables.keys())
            with console.status("[cyan]Baixando tabelas auxiliares...[/cyan]"):
                ftp = fetcher.connect()
                for dataset in sorted(aux_targets):
                    for _ in fetcher.download_auxiliary_tables(ftp, dataset, output):
                        pass
                ftp.close()
            console.print("[green]✓[/green] Tabelas auxiliares sincronizadas.")
    except KeyboardInterrupt:
        console.print("[yellow]Download cancelado pelo usuário.[/yellow]")
        raise typer.Exit(code=130)


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
