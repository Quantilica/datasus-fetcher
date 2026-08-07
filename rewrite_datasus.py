import re
from pathlib import Path

content = Path("src/datasus_fetcher/fetcher.py").read_text()

# We need to remove `class Fetcher(threading.Thread):` and all its methods.
# And rewrite `download_data`.

new_code = """
def download_data(
    datasets: Iterable[str],
    destdir: Path,
    threads: int = 2,
    callback: Callable | None = None,
    slicer: Slicer | None = None,
    show_progress: bool = False,
):
    \"\"\"Multithreaded download data files, dataset by dataset.\"\"\"
    logger.info("Starting download with %s threads", threads)
    datasets_ = (
        set(datasets) & set(meta.datasets.keys())
        if datasets
        else set(meta.datasets.keys())
    )

    ftp0 = connect()
    failed_files: list[str] = []

    live = None
    batch_progress = None
    file_progress = None
    pool = None

    if show_progress and _RICH_AVAILABLE:
        console = get_console()
        batch_progress = make_batch_progress(console)
        file_progress = make_download_progress(console)
        pool = ProgressPool(workers=threads, file_prog=file_progress)
        live = Live(
            Group(batch_progress, file_progress),
            console=console,
            refresh_per_second=10,
        )
        live.start()

    import threading
    thread_local = threading.local()

    def get_ftp() -> ftplib.FTP:
        if not hasattr(thread_local, "ftp"):
            thread_local.ftp = connect()
        return thread_local.ftp

    def _worker(file: RemoteFile) -> dict | None:
        filepath: Path = get_data_filepath(destdir, file)
        if is_complete_file(filepath, file.size):
            return None

        ftp = get_ftp()
        ctx = pool.acquire(description=f"[cyan]{filepath.name}[/cyan]") if pool else contextlib.nullcontext()
        try:
            with ctx as cb:
                downloaded_bytes = 0
                def chunk_cb(n: int) -> None:
                    nonlocal downloaded_bytes
                    downloaded_bytes += n
                    if cb is not None:
                        cb(downloaded_bytes, file.size)

                def reset_cb() -> None:
                    nonlocal downloaded_bytes
                    downloaded_bytes = 0
                    if cb is not None:
                        cb(0, file.size)

                t0 = time.time()
                for attempt in range(1, 4):
                    try:
                        sha256, size_bytes = fetch_file(
                            ftp,
                            file.full_path,
                            filepath,
                            retries=3,
                            chunk_callback=chunk_cb,
                            reset_callback=reset_cb,
                        )
                        break
                    except ftplib.error_perm:
                        logger.exception("Permanent FTP error for %s — skipping.", file.full_path)
                        return None
                    except _RETRYABLE_DOWNLOAD_ERRORS as exc:
                        if attempt == 3:
                            logger.error("Download failed after 3 attempts: %s", file.full_path)
                            failed_files.append(file.full_path)
                            return None
                        logger.warning("Transient error for %s: %s. Reconnecting...", file.full_path, exc)
                        with contextlib.suppress(Exception):
                            ftp.close()
                        try:
                            thread_local.ftp = ftp = connect()
                        except Exception:
                            logger.exception("Reconnect failed")
                            failed_files.append(file.full_path)
                            return None
                    except Exception:
                        logger.exception("Unexpected error for %s — skipping.", file.full_path)
                        failed_files.append(file.full_path)
                        return None

                tt = time.time() - t0
                log_download(tt, file.size, filepath.name)

                url = f"ftp://{FTP_HOST}/{file.full_path}"
                manifest = _write_manifest(
                    filepath,
                    url,
                    file.dataset,
                    metadata={
                        "partition": str(file.partition),
                        "preliminary": file.preliminary,
                        "remote_datetime": file.datetime.isoformat(),
                    },
                    sha256=sha256,
                    size_bytes=size_bytes,
                )

                res = {
                    "url": url,
                    "size": file.size,
                    "filepath": filepath,
                    "suffix": file.extension,
                    "dataset": file.dataset,
                    "created_at": file.datetime,
                    "manifest": manifest,
                }
                if callback:
                    callback(res)
                return res
        except Exception as exc:
            logger.error("Worker failed for %s: %s", file.full_path, exc)
            return None

    try:
        import concurrent.futures
        
        exec_ctx = graceful_executor(max_workers=threads) if _RICH_AVAILABLE else concurrent.futures.ThreadPoolExecutor(max_workers=threads)
        
        with exec_ctx as executor:
            for dataset in sorted(datasets_):
                logger.info("Listing files of %s", dataset)
                
                def _needs_download(f: RemoteFile) -> bool:
                    fp = get_data_filepath(destdir, f)
                    return not is_complete_file(fp, f.size)

                attempts = 3
                while attempts > 0:
                    try:
                        dataset_files = [
                            f
                            for f in list_dataset_files(ftp0, dataset)
                            if (slicer is None or slicer(f)) and _needs_download(f)
                        ]
                        break
                    except FTP_TRANSIENT_ERRORS:
                        attempts -= 1
                        if attempts <= 0:
                            raise
                        logger.warning("Transient error listing %s. Reconnecting...", dataset)
                        with contextlib.suppress(Exception):
                            ftp0.close()
                        ftp0 = connect()

                if not dataset_files:
                    continue

                batch_task = None
                pbar = None
                if show_progress:
                    if batch_progress is not None:
                        batch_task = batch_progress.add_task(
                            f"[cyan]{dataset}[/cyan]", total=len(dataset_files)
                        )
                    else:
                        total_bytes = sum(f.size for f in dataset_files)
                        pbar = _tqdm(
                            total=total_bytes,
                            desc=dataset,
                            unit="B",
                            unit_scale=True,
                            unit_divisor=1024,
                            leave=True,
                        )

                futures = [executor.submit(_worker, f) for f in dataset_files]
                for future in concurrent.futures.as_completed(futures):
                    res = future.result()
                    if batch_task is not None:
                        batch_progress.update(batch_task, advance=1)
                    if pbar is not None and res is not None:
                        pbar.update(res["size"])

                if pbar is not None:
                    pbar.close()

    except KeyboardInterrupt:
        print("\nDownload interrompido pelo usuário.")
        raise
    finally:
        if live is not None:
            with contextlib.suppress(Exception):
                live.stop()
        with contextlib.suppress(Exception):
            ftp0.close()
        if failed_files:
            logger.warning(
                "%d arquivo(s) falharam permanentemente após todas as tentativas:\\n%s",
                len(failed_files),
                "\\n".join(f"  {p}" for p in sorted(failed_files)),
            )
"""

# Now replace the Fetcher class and download_data

content = re.sub(r'class Fetcher\(threading\.Thread\):.*?(?=\ndef log_download)', '', content, flags=re.DOTALL)
content = re.sub(r'def download_data\(.*?(?=\ndef _list_support_files)', new_code + "\n", content, flags=re.DOTALL)

# Let's add ProgressPool and graceful_executor to the rich import if not there
if 'ProgressPool' not in content:
    content = content.replace(
        'from quantilica.cli.ui import (',
        'from quantilica.cli.ui import (\n        ProgressPool,\n        graceful_executor,'
    )

Path("src/datasus_fetcher/fetcher.py").write_text(content)
