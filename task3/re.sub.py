import re
text = "Contact john@gmail.com or support@yahoo.com for help."
result = re.sub(r"\b[\w.-]+@[\w.-]+\.\w+\b", "[EMAIL HIDDEN]", text)
print(result)
output:
Contact [EMAIL HIDDEN] or [EMAIL HIDDEN] for help.

