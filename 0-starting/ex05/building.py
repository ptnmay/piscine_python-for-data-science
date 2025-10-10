"""
building.py

A simple program that counts different character types in a given text.

The program:
- Asks the user to input a line of text.
- Counts the total characters, uppercase letters, lowercase letters,
  punctuation marks, spaces, and digits.
- Prints the result in a formatted way.

Rules followed:
- No code in the global scope.
- Has a main() entry point.
- All exceptions are handled.
- Code follows PEP 8 (flake8) standards.
"""

import string


def count_characters(text: str) -> None:
    """
    Count and display different character types in the given text.

    Args:
        text (str): The input string to analyze.

    Returns:
        None
    """
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punctuation = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main() -> None:
    """
    Main entry point of the program.

    Prompts the user for text input and calls the count_characters function.
    Handles unexpected errors gracefully.
    """
    try:
        text = input("What is the text to count?\n")
        count_characters(text)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
