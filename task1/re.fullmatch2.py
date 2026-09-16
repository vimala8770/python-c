import re
text = "123a5"
result = re.fullmatch(r"\d+", text)
if result:
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
    output:
The string does not contain only digits.

