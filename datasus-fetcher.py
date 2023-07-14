import argparse
import shutil
from pathlib import Path

from datasus_fetcher import fetcher, meta
from datasus_fetcher.storage import File, get_filename, get_files_metadata


def list_files(args: argparse.Namespace):
    if not args.datasets:
        datasets = meta.datasets
    else:
        datasets = args.datasets

    ftp = fetcher.connect()

    total_size = 0
    total_n_files = 0

    for dataset in datasets:
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
        msg = " ".join(
            [
                f"{dataset: <27}",
                f"{dataset_n_files: >6} files ",
                f"{dataset_size / 2**20: >9.1f} MB",
                f"from {first} to {last}",
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

    fetcher.download_data(datasets, data_dir, threads)


def fetch_docs(args: argparse.Namespace):
    data_dir = args.data_dir
    if args.datasets is None:
        datasets = meta.datasets
    else:
        datasets = args.datasets

    ftp = fetcher.connect()
    if datasets:
        datasets_ = set(datasets) & set(meta.docs.keys())
    else:
        datasets_ = meta.docs.keys()
    for dataset in datasets_:
        fetcher.download_documentation(ftp, dataset, data_dir)
    ftp.close()


def archive(args: argparse.Namespace):
    data_dir = args.data_dir
    archivedatadir = args.archive_data_dir
    extension = args.extension
    dry_run = args.dry_run

    for datasetdir in data_dir.iterdir():
        print(datasetdir)
        datasetname = datasetdir.name
        for datepartitiondir in datasetdir.iterdir():
            files = get_files_metadata(datepartitiondir, extension=extension)
            for file in files:
                file: File
                if not file.is_most_recent:
                    print(file)
                    if dry_run:
                        continue
                    archivedatasetdir: Path = archivedatadir / datasetname
                    archivedatasetdir.mkdir(parents=True, exist_ok=True)
                    archivefilepath = archivedatasetdir / file.filepath.name
                    shutil.move(file.filepath, archivefilepath)


def get_args():
    parser = argparse.ArgumentParser(
        description="Download raw data files from DATASUS",
    )
    subparsers = parser.add_subparsers(required=True)

    # * list-files ------------------------------------------------------------
    subparser_list_files = subparsers.add_parser("list-files")
    subparser_list_files.add_argument(
        "datasets",
        nargs="*",
        help="Datasets to list",
    )
    subparser_list_files.set_defaults(func=list_files)

    # * fetch data ------------------------------------------------------------
    subparser_fetch = subparsers.add_parser("fetch")
    subparser_fetch.add_argument(
        "datasets",
        nargs="*",
        help="Datasets to download",
    )
    subparser_fetch.add_argument(
        "-o",
        "--output",
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
        "-o",
        "--output",
        "--data-dir",
        dest="data_dir",
        type=Path,
        help="Directory to download to",
    )
    subparser_docs.set_defaults(func=fetch_docs)

    # * archive ---------------------------------------------------------------
    subparser_archive = subparsers.add_parser("archive")
    subparser_archive.add_argument("--data-dir", type=Path, required=True)
    subparser_archive.add_argument(
        "--archive-data-dir",
        type=Path,
        required=True,
    )
    subparser_archive.add_argument("--extension", required=True)
    subparser_archive.add_argument("--dry-run", action="store_true")
    subparser_archive.set_defaults(func=archive)

    args = parser.parse_args()
    return args


def main():
    args = get_args()
    args.func(args)


if __name__ == "__main__":
    main()
