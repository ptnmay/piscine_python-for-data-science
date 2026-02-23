import sys

try:
    ac = len(sys.argv)
    if ac == 1:
        sys.exit()

    assert ac <= 2, "more than one argument is provided"
    av = sys.argv[1]
    assert av.lstrip("-").isdigit(), "argument is not an intiger"
    num = int(av)

    if num % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")

except AssertionError as error:
    print(f"AssertionError: {error}")
