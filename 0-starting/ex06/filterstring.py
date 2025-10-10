"""
filterstring.py

A program that filters words from a given string S,
keeping only those longer than an integer N.

Usage:
    python filterstring.py "Hello the World" 4
"""

import sys
from ft_filter import ft_filter


def main() -> None:
    """
    Main entry point for the program.
    Validates arguments and prints filtered words.
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text, num = sys.argv[1], sys.argv[2]

        if not num.isdigit():
            raise AssertionError("the arguments are bad")

        n = int(num)
        words = text.split()
        result = list(ft_filter(lambda w: len(w) > n, words))
        print(result)

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
