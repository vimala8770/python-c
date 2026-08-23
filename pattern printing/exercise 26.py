N = 5

for i in range(N):
    letter = chr(ord('A') + i)

    for j in range(i + 1):
        print(letter, end=" ")

    print()
    output:
A 
B B 
C C C 
D D D D 
E E E E E 
