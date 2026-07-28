# Demonstrating different output formatting methods

name = input("Enter name: ")
marks = int(input("Enter marks: "))

# Method 1: Comma-separated print
print("Name:", name, "Marks:", marks)

# Method 2: str.format()
print("Name: {} Marks: {}".format(name, marks))

# Method 3: f-string
print(f"Name: {name} Marks: {marks}")
output:
Enter name: vimala
Enter marks: 96
Name: vimala Marks: 96
Name: vimala Marks: 96
Name: vimala Marks: 96
