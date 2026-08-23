year = int(input("Enter a year: "))

if year % 400 == 0:
    print("It is a leap year")
elif year % 100 == 0:
    print("It is not a leap year")
elif year % 4 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")
output:
Enter a year: 2023
It is not a leap year
