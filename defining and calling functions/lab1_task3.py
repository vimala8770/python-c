def is_even(n):
    return n%2==0
for i in range(5):
    num = int(input("enter a number:"))
    if is_even(num):
        print(num, "is even")
    else:
        print(num, "is odd")
        output:
enter a number:38
38 is even
