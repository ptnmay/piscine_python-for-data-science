import sys


def count_chars(text: str) -> None:
    """
    Count and display character types in the given text.
    """
    upper = 0
    lower = 0
    punct = 0
    space = 0
    digits = 0
    PUNCT = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

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
    """
    if len(sys.argv) > 2:
        raise AssertionError("More than one argument is provided")

    if len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        text = input("What is the text to count?\n")

    count_chars(text)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"AssertionError: {error}")

#PUNCT is constant variable
