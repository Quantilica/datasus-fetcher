import argparse
import pathlib
import queue
import threading

from datasus_fetcher import fetcher, meta


def download(datasets, destdir, threads=2, callback=None):
    print(f"Starting download with {threads} threads")
    if datasets:
        datasets_ = set(datasets) & set(meta.datasets.keys())
    else:
        datasets_ = meta.datasets.keys()
    if callback is None:
        callback = print
    ftp0 = fetcher.connect()
    q = queue.Queue()
    for _ in range(threads):
        _w = fetcher.Fetcher(q, destdir, callback=callback)
        _w.start()
    for dataset in datasets_:
        print(f"Getting files of {dataset}")
        for remote_file in fetcher.list_dataset_files(ftp0, dataset):
            q.put(remote_file)
    ftp0.close()
    print("Joining queue")
    q.join()
    for th in threading.enumerate():
        if th.daemon:
            th.ftp.close()


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
    download(datasets, destdir, threads)


if __name__ == "__main__":
    main()
