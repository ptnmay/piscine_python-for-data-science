import sys
from ft_filter import ft_filter


def main() -> None:
    """
    Main entry point for the program.
    """
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    text = sys.argv[1]

    try:
        n = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    words = text.split()
    result = list(ft_filter(lambda w: len(w) > n, words))
    print(result)

if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")
