import sys

"""
sos.py

A program that converts text to Morse code.
"""


def get_morse() -> dict:
    """
    Returns the Morse code dictionary.
    """
    return {
        "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
        "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
        "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
        "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
        "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
        "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
        "Y": "-.--",  "Z": "--..",

        "0": "-----", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.",
    }


def main() -> None:
    """
    Main entry point of program.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        text = sys.argv[1]
        text = text.upper()

        for char in text:
            if not (char.isalnum() or char == " "):
                raise AssertionError("the arguments are bad")
        morse_dict = get_morse()
        result = []

        for char in text:
            if char == " ":
                result.append("/")
            else:
                result.append(morse_dict[char])
        print(" ".join(result))

    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
