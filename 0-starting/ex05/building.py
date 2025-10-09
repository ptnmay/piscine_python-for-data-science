
import string


def count_characters(text: str) -> None:

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

    try:
        text = input("What is the text to count?\n")
        count_characters(text)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
