num = int(input("Enter a number: "))

if num < 2:
    print("The number is not prime")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("The number is prime")
    else:
        print("The number is not prime")
        output:
Enter a number: 19
The number is prime
