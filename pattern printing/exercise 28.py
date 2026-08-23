N = 4

# Upper half
for i in range(1, N + 1):
    # Spaces before stars
    for j in range(N - i):
        print(" ", end="")

    # Stars and spaces inside
    if i == 1:
        print("*")
    else:
        print("*", end="")
        for j in range(2 * i - 3):
            print(" ", end="")
        print("*")

# Lower half
for i in range(N - 1, 0, -1):
    # Spaces before stars
    for j in range(N - i):
        print(" ", end="")

    # Stars and spaces inside
    if i == 1:
        print("*")
    else:
        print("*", end="")
        for j in range(2 * i - 3):
            print(" ", end="")
        print("*")
        output:
   *
  * *
 *   *
*     *
 *   *
  * *
   *
