import re
pattern = r"\b(cat|dog|bird)\b"
sentence = "I have a cat, a dog, and a bird."
result = re.findall(pattern, sentence)
print(result)
output:
['cat', 'dog', 'bird']
