numbers = [10, -5, 20, -8, 15, -3, 7]

result = [0 if number < 0 else number for number in numbers]

print("Original list:", numbers)
print("Updated list:", result)
output:
Original list: [10, -5, 20, -8, 15, -3, 7]
Updated list: [10, 0, 20, 0, 15, 0, 7]
