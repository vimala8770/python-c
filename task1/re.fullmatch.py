import re
text = "12345"
result = re.fullmatch(r"\d+", text)
if result:
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
    output:
The string contains only digits.

