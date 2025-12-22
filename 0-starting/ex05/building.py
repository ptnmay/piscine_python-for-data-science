"""
building.py

A program that counts character types in a given text.
"""

import sys

# manual punctuation list (cannot use string module)
PUNCT = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def count_chars(text: str) -> None:
    """
    Count and display character types in the given text.
    """
    upper = 0
    lower = 0
    digits = 0
    punct = 0
    space = 0

    for c in text:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
        elif c.isdigit():
            digits += 1
        elif c.isspace():
            space += 1
        elif c in PUNCT:
            punct += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")


def main() -> None:
    """
    Main entry point of the program.
    Handles arguments, input, and error catching.
    """
    try:
        args = sys.argv[1:]

        if len(args) > 1:
            raise AssertionError("More than one argument is provided")

        if len(args) == 1:
            text = args[0]
        else:
            text = input("What is the text to count?\n")

        count_chars(text)

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
