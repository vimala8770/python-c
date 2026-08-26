matrix = [[(row * 3) + column + 1 for column in range(3)] 
          for row in range(3)]

print("3x3 Matrix:")
for row in matrix:
    print(row)
    output:
3x3 Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
