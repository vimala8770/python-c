N = 4

# Upper half
for i in range(1, N + 1):
    # Left stars
    for j in range(i):
        print("*", end=" ")

    # Spaces
    for j in range(2 * (N - i)):
        print(" ", end=" ")

    # Right stars
    for j in range(i):
        print("*", end=" ")

    print()

# Lower half
for i in range(N, 0, -1):
    # Left stars
    for j in range(i):
        print("*", end=" ")

    # Spaces
    for j in range(2 * (N - i)):
        print(" ", end=" ")

    # Right stars
    for j in range(i):
        print("*", end=" ")

    print()
    output:
*             * 
* *         * * 
* * *     * * * 
* * * * * * * * 
* * * * * * * * 
* * *     * * * 
* *         * * 
*             * 
