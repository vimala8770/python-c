def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
# Recursive version
n = 5
print("Factorial using recursion:", factorial(n))
# Iterative version
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
print("Factorial using iteration:", factorial_iterative(n))
output:
Factorial using recursion: 120
Factorial using iteration: 120
