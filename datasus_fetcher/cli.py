"""Command Line Interface for datasus-fetcher package."""


import argparse
import logging
import shutil
import threading
from pathlib import Path
from typing import Any

from . import fetcher, meta
from .slicer import Slicer
from .storage import File, get_files_metadata

logger = logging.getLogger(__name__)

if Path("logging.ini").exists():
    import logging.config

    logging.config.fileConfig("logging.ini")


def list_datasets(args: argparse.Namespace):
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
        dataset_size = sum(f.size for f in dataset_files_list)
        dataset_n_files = len(dataset_files_list)
        total_size += dataset_size
        total_n_files += dataset_n_files
        if dataset_files_list:
            if "year" in meta.datasets[dataset]["partition"]:
                first = min(dataset_files_list, key=lambda x: x.partition.year)
                first = f"{first.partition.year}"
                last = max(dataset_files_list, key=lambda x: x.partition.year)
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
        else:
            first = last = "----"
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


def fetch_data(args: argparse.Namespace):
    data_dir = args.data_dir
    threads = args.threads
    if not args.datasets:
        datasets = meta.datasets
    else:
        datasets = args.datasets

    slicer = Slicer(
        start_time=args.start,
        end_time=args.end,
        regions=args.regions,
    )

    def log_fetch_data(file_metadata: dict[str, Any]):
        message = (
            "Downloaded "
            f"{file_metadata['dataset']: <27} "
            f"{str(file_metadata['filepath']): <20} "
            f"{file_metadata['size'] / 2**20: >9.1f} MB"
        )
        logger.info(message)

    try:
        fetcher.download_data(
            datasets=sorted(datasets),
            destdir=data_dir,
            threads=threads,
            callback=log_fetch_data,
            slicer=slicer,
        )
    except KeyboardInterrupt:
        for th in threading.enumerate():
            if th.daemon:
                th.ftp.close()
                th.kill()
        logger.warning("KeyboardInterrupt: closing FTP connections")


def fetch_docs(args: argparse.Namespace):
    data_dir = args.data_dir
    if args.datasets is None:
        datasets = meta.docs
    else:
        datasets = args.datasets

    ftp = fetcher.connect()
    if datasets:
        datasets_ = set(datasets) & set(meta.docs.keys())
    else:
        datasets_ = meta.docs.keys()
    for dataset in sorted(datasets_):
        for _ in fetcher.download_documentation(ftp, dataset, data_dir):
            pass
    ftp.close()


def fetch_aux(args: argparse.Namespace):
    data_dir = args.data_dir
    if args.datasets is None:
        datasets = meta.auxiliary_tables
    else:
        datasets = args.datasets

    ftp = fetcher.connect()
    if datasets:
        datasets_ = set(datasets) & set(meta.auxiliary_tables.keys())
    else:
        datasets_ = meta.auxiliary_tables.keys()
    for dataset in sorted(datasets_):
        for _ in fetcher.download_auxiliary_tables(ftp, dataset, data_dir):
            pass
    ftp.close()


def archive(args: argparse.Namespace):
    data_dir = args.data_dir
    archivedatadir = args.archive_data_dir
    for datasetdir in data_dir.iterdir():
        datasetname = datasetdir.name
        for datepartitiondir in datasetdir.iterdir():
            files = get_files_metadata(datepartitiondir)
            for file in files:
                file: File
                if not file.is_most_recent:
                    archivedatasetdir: Path = archivedatadir / datasetname
                    archivedatasetdir.mkdir(parents=True, exist_ok=True)
                    archivefilepath = archivedatasetdir / file.filepath.name
                    shutil.move(file.filepath, archivefilepath)


def get_args():
    parser = argparse.ArgumentParser(
        description="Download raw data files from DATASUS",
    )
    subparsers = parser.add_subparsers(required=True)

    # * list-datasets ---------------------------------------------------------
    subparser_list_datasets = subparsers.add_parser("list-datasets")
    subparser_list_datasets.add_argument(
        "datasets",
        nargs="*",
        help="Datasets to list",
    )
    subparser_list_datasets.set_defaults(func=list_datasets)

    # * fetch data ------------------------------------------------------------
    subparser_fetch = subparsers.add_parser("data")
    subparser_fetch_group = subparser_fetch.add_argument_group("dataset")
    subparser_fetch_group.add_argument(
        "datasets",
        nargs="*",
        help="Datasets to download (eg.: sih-rd, cnes-dc, ...)",
    )
    subparser_fetch_group.add_argument(
        "--start",
        help="Start period to download (eg.: 2001 OR 2001-01)",
    )
    subparser_fetch_group.add_argument(
        "--end",
        help="End period to download (eg.: 2020 OR 2020-12)",
    )
    subparser_fetch_group.add_argument(
        "--regions",
        nargs="+",
        help="Regions to download (eg.: br, ac, am, ce, ...)",
    )
    subparser_fetch.add_argument(
        "--data-dir",
        dest="data_dir",
        type=Path,
        required=True,
        help="Directory to download to",
    )
    subparser_fetch.add_argument(
        "-t",
        "--threads",
        dest="threads",
        type=int,
        default=2,
        help="Number of concurrent fetchers",
    )
    subparser_fetch.set_defaults(func=fetch_data)

    # * fetch docs ------------------------------------------------------------
    subparser_docs = subparsers.add_parser("docs")
    subparser_docs.add_argument(
        "datasets",
        nargs="*",
        help="Datasets documentation to download",
    )
    subparser_docs.add_argument(
        "--data-dir",
        dest="data_dir",
        type=Path,
        help="Directory to download to",
    )
    subparser_docs.set_defaults(func=fetch_docs)

    # * fetch aux -------------------------------------------------------------
    subparser_aux = subparsers.add_parser("aux")
    subparser_aux.add_argument(
        "datasets",
        nargs="*",
        help="Datasets auxiliary tables to download",
    )
    subparser_aux.add_argument(
        "--data-dir",
        dest="data_dir",
        type=Path,
        help="Directory to download to",
    )
    subparser_aux.set_defaults(func=fetch_aux)

    # * archive ---------------------------------------------------------------
    subparser_archive = subparsers.add_parser("archive")
    subparser_archive.add_argument("--data-dir", type=Path, required=True)
    subparser_archive.add_argument(
        "--archive-data-dir",
        type=Path,
        required=True,
    )
    subparser_archive.set_defaults(func=archive)

    args = parser.parse_args()
    return args


def main():
    args = get_args()
    args.func(args)


if __name__ == "__main__":
    main()
