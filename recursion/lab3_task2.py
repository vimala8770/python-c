count = 0


def fibonacci(n):
    global count

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        count += 1
        return fibonacci(n - 1) + fibonacci(n - 2)


# Print first 15 terms
print("First 15 Fibonacci terms:")

for i in range(15):
    print(fibonacci(i), end=" ")

print()


# Count how many times fibonacci(5) is called
count_fib5 = 0


def fibonacci_count(n):
    global count_fib5

    if n == 5:
        count_fib5 += 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_count(n - 1) + fibonacci_count(n - 2)


fibonacci_count(10)

print("\nfibonacci(5) is computed:", count_fib5, "times")
output:
First 15 Fibonacci terms:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 

fibonacci(5) is computed: 8 times





