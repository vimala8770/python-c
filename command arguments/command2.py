import sys

if len(sys.argv) != 3:
    print("Usage: python sum.py <num1> <num2>")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    print("Sum =", num1 + num2)
