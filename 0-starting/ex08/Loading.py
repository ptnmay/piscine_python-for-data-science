import os

def ft_tqdm(lst: range) -> None:
    """
    Display a progress bar while iterating over a range.
    """
    total = len(lst)
    count = 0
    for item in lst:
        percent = int((count / total) * 100)
        width = os.get_terminal_size().columns - 20
        filled = int(width * count / total)
        bar = "=" * filled + ">" + " " * (width - filled - 1)

        print(
            f"\r{percent:3d}%|{bar}|",
            end="",
            flush=True
        )

        yield item
        count += 1

    width = os.get_terminal_size().columns - 20
    bar = "=" * width
    print(f"\r100%|{bar}|")