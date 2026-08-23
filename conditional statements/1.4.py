a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c

print("The largest number is:", largest)
output:
    Enter first number: 47
Enter second number: 36
Enter third number: 85
The largest number is: 85
