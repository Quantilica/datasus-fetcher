import argparse
import subprocess
from pathlib import Path

from datasus_fetcher import meta


def compress_files_by_period(dataset_dirpath: Path, destdirpath: Path):
    dataset = dataset_dirpath.name
    periods = set(
        [
            partition.split("-")[0]
            for _, partition, _ in (
                f.stem.split("_") for f in dataset_dirpath.iterdir()
            )
        ]
    )
    for period in sorted(periods):
        dest_filepath = destdirpath / f"{dataset}_{period}.7z"
        if dest_filepath.exists():
            continue
        if not dest_filepath.parent.exists():
            dest_filepath.parent.mkdir(parents=True)
        cmd = [
            "7z",
            "a",
            "-t7z",
            "-m0=lzma2",
            str(dest_filepath),
            f"{dataset_dirpath}/{dataset}_{period}*.dbc",
        ]
        print(cmd)
        subprocess.run(cmd)


def compress_files_by_dataset(datadirpath: Path, destdirpath: Path):

    for datasetdir in sorted(datadirpath.iterdir()):
        dest_filepath = destdirpath / f"{datasetdir.name}.7z"
        if dest_filepath.exists():
            continue
        if not dest_filepath.parent.exists():
            dest_filepath.parent.mkdir(parents=True)
        cmd = [
            "7z",
            "a",
            "-t7z",
            "-m0=lzma2",
            str(dest_filepath),
            f"{datasetdir / '*.*'}",
        ]
        print(cmd)
        subprocess.run(cmd)


def get_parser():
    parser = argparse.ArgumentParser(
        description="Compress all raw files in the given directory"
    )
    parser.add_argument(
        "datadirpath",
        type=Path,
        help="Directory to compress",
    )
    parser.add_argument(
        "destdirpath",
        type=Path,
        help="Directory to store compressed files",
    )
    parser.add_argument("-by", choices=["dataset", "period"], default="period")
    return parser


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    datadirpath = args.datadirpath
    destdirpath = args.destdirpath
    if args.by == "dataset":
        compress_files_by_dataset(datadirpath, destdirpath)
    elif args.by == "period":
        for dataset in meta.datasets:
            if not (datadirpath / dataset).exists():
                continue
            compress_files_by_period(datadirpath / dataset, destdirpath / dataset)
    else:
        raise ValueError(f"Unknown value for -by: {args.by}")
