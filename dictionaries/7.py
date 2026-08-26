student = {
    "name": "vimala",
    "age": 18,
    "course": "Python"
}

removed_value = student.pop("age")
print("Removed value:", removed_value)
print("After pop():", student)

# Safely access a key that may not exist
result = student.get("phone", "Key does not exist")

print("Result:", result)
output:
Removed value: 18
After pop(): {'name': 'vimala', 'course': 'Python'}
Result: Key does not exist
