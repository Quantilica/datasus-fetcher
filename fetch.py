import argparse
import pathlib

from datasus_fetcher import fetcher


def get_args():
    parser = argparse.ArgumentParser(
        description="Download all raw files from datasus",
    )
    parser.add_argument(
        "datasets",
        nargs="*",
        help="Datasets to download",
    )
    parser.add_argument(
        "-o",
        "--output",
        "--destdir",
        dest="destdir",
        type=pathlib.Path,
        required=True,
        help="Directory to download to",
    )
    parser.add_argument(
        "-t",
        "--threads",
        dest="threads",
        type=int,
        default=2,
        help="Number of concurrent fetchers",
    )
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    datasets = args.datasets
    destdir = args.destdir
    threads = args.threads
    fetcher.download_data(datasets, destdir, threads)


if __name__ == "__main__":
    main()
