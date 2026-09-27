from functools import reduce
numbers = [10, 25, 7, 45, 18, 32]
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum value:", maximum)
output:
Maximum value: 45
