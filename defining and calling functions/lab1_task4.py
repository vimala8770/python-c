def stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
minimum, maximum, average = stats(numbers)
print("Minimum =", minimum)
print("Maximum =", maximum)
print("Average =", average)
output:
Enter numbers separated by spaces: 5 6 7 8
Minimum = 5.0
Maximum = 8.0
Average = 6.5
