s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("String after removing duplicates:", result)
output:
Enter a string: programming
String after removing duplicates: progamin

