numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Cubes using map()
cubes = list(map(lambda x: x ** 3, numbers))
print("Cubes:", cubes)
# Numbers divisible by 3 using filter()
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print("Numbers divisible by 3:", divisible_by_3)
output:
Cubes: [1, 8, 27, 64, 125, 216, 343, 512, 729]
Numbers divisible by 3: [3, 6, 9]
