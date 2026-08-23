num = int(input("Enter a number: "))

temp = num
sum_digits = 0
count = 0

while temp > 0:
    digit = temp % 10
    sum_digits = sum_digits + digit
    count = count + 1
    temp = temp // 10

average = sum_digits / count

print("Sum of digits:", sum_digits)
print("Average of digits:", average)
output:
Enter a number: 24609
Sum of digits: 21
Average of digits: 4.2
