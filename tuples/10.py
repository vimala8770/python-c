numbers = (10, 20, 30)

try:
    numbers[0] = 100
except TypeError as error:
    print("Error:", error)
    print("Tuples are immutable and cannot be modified.")
Error: 'tuple' object does not support item assignment
Tuples are immutable and cannot be modified.
