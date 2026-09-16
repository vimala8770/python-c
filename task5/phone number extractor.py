import re
text = """
Call me at 555-123-4567.
Office: (555) 987-6543.
You can also call 555.111.2222.
"""
pattern = r"(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]\d{4}"
numbers = re.findall(pattern, text)
for number in numbers:
    normalized = re.sub(r"\D", "", number)
    normalized = re.sub(r"(\d{3})(\d{3})(\d{4})", r"\1-\2-\3", normalized)
    print(normalized)
    output:
555-123-4567
555-987-6543
555-111-2222
