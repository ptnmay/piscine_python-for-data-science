import os


def ft_tqdm(lst: range) -> None:
    """
    Iterate over a range while showing a progress bar.
    """

    total = len(lst)

    if total == 0:
        print("0it [00:00, ?it/s]")
        return

    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80
    bar_length = width - 40
    if bar_length < 10:
        bar_length = 10
    for i, item in enumerate(lst):
        percent = (i + 1) / total * 100
        filled = int(bar_length * (i + 1) / total)
        bar = "=" * filled
        bar += " " * (bar_length - len(bar))
        print(f"{percent:3.0f}%|{bar}| {i + 1}/{total}", end="\r", flush=True)
        yield item
    print()

"""
OsErro is error from os (Operating system)
-> cannot find file, permission error.
if python call OS and OS said cannot throw to OsError

enumerate give index and value
"""