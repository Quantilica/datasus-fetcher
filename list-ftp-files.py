from datasus_fetcher import fetcher, meta


def main():
    ftp = fetcher.connect()

    total_size = 0
    total_files = 0
    for dataset in meta.datasets:
        dataset_size = 0
        dataset_files = 0
        for file in fetcher.list_dataset_files(ftp, dataset):
            total_size += file.size
            total_files += 1
            dataset_size += file.size
            dataset_files += 1
        msg = " ".join(
            [
                f"{dataset: <27}",
                f"{dataset_files: >6} files",
                f"totaling {dataset_size / 2**20: >9.1f} MB",
            ]
        )
        print(msg)

    print(f"Total size: {total_size / 2**30:.1f} GB")
    print(f"Total files: {total_files} files")

    ftp.close()


if __name__ == "__main__":
    main()
