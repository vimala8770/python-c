start = int(input("Enter the lower limit: "))
end = int(input("Enter the upper limit: "))

print("Prime numbers are:")

for num in range(start, end + 1):
    if num >= 2:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num, end=" ")
            output:
Enter the lower limit: 11
Enter the upper limit: 47
Prime numbers are:
11 13 17 19 23 29 31 37 41 43 47 

