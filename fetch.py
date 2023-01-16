import argparse
import logging
from pathlib import Path

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
        type=Path,
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
    logger = logging.getLogger("datasus_fetcher")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(
        logging.Formatter(
            fmt="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    logger.addHandler(handler)
    args = get_args()
    datasets = args.datasets
    destdir = args.destdir
    threads = args.threads
    fetcher.download_data(datasets, destdir, threads)


if __name__ == "__main__":
    main()
