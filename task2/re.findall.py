import re
paragraph = "NASA and USA are working with ISRO on a new space mission."
result = re.findall(r"\b[A-Z]{2,}\b", paragraph)
print(result)
output:
['NASA', 'USA', 'ISRO']
