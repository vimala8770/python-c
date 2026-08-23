n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    i = i + 1
    output:
Enter number of terms: 6
0 1 1 2 3 5 
