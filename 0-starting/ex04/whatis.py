import sys

if len(sys.argv) != 2:
    print("AssertionError: more than one argument is provided")
    sys.exit()

arg = sys.argv[1]

try:
    num = int(arg)
except ValueError:
    print("AssertionError: argument is not an integer")
    sys.exit()

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
