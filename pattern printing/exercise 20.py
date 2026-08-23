N = 5

for i in range(1, N + 1):
    # Print spaces
    for j in range(N - i):
        print(" ", end="")

    # Print stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()
    output:
    *
   ***
  *****
 *******
*********
