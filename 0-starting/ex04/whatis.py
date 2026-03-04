import sys

try:
    if len(sys.argv) == 1:
        sys.exit()
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")
    try:
        n = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print(f"AssertionError: {e}")

"""
AssertionError is for debug logic.

ValueError is for wrong input, like int("abc").

raise throw error
except catch error
"""
 