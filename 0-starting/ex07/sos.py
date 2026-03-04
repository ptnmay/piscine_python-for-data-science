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
    if len(sys.argv) != 2:
        raise AssertionError("Invalid arguments")
    text = sys.argv[1].upper()
    morse_dict = get_morse()
    result = []
    for char in text:
        if char == " ":
            result.append("/")
        elif char in morse_dict:
            result.append(morse_dict[char])
        else:
            raise AssertionError(
                "Only letters (A-Z) and digits (0-9) are allowed."
            )
    print(" ".join(result))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
