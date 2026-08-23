N = 4

# Upper half
for i in range(1, N + 1):
    # Spaces
    for j in range(N - i):
        print(" ", end="")

    # Stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()

# Lower half
for i in range(N, 0, -1):
    # Spaces
    for j in range(N - i):
        print(" ", end="")

    # Stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()
    output:
   *
  ***
 *****
*******
*******
 *****
  ***
   *
