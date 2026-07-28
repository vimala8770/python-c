# Program to take multiple values in one line

numbers = input("Enter numbers separated by spaces: ").split()

numbers = list(map(int, numbers))

print("Sum =", sum(numbers))
output:
Enter numbers separated by spaces: 2 5 3 6 
Sum = 16
