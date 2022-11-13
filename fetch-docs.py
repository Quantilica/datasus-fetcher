import argparse
from pathlib import Path

from datasus_fetcher import fetcher, meta


def download(datasets, destdir):
    ftp = fetcher.connect()
    if datasets:
        datasets_ = set(datasets) & set(meta.docs.keys())
    else:
        datasets_ = meta.docs.keys()
    for dataset in datasets_:
        fetcher.download_documentation(ftp, dataset, destdir)
    ftp.close()


def get_parser():
    parser = argparse.ArgumentParser(
        description="Download all documentation files from datasus",
    )
    parser.add_argument(
        "datasets",
        nargs="*",
        help="Datasets documentation to download",
    )
    parser.add_argument(
        "-o",
        "--output",
        "--destdir",
        dest="destdir",
        type=Path,
        help="Directory to download to",
    )
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    datasets = args.datasets
    destdir = args.destdir
    download(datasets, destdir)


if __name__ == "__main__":
    main()
