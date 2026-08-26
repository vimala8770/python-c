numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print("Original list:", numbers)
print("List without duplicates:", unique)
output:
Original list: [10, 20, 10, 30, 20, 40, 30, 50]
List without duplicates: [10, 20, 30, 40, 50]
