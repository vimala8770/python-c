def to_uppercase(word):
    return word.upper()
words = ["python", "java", "c", "javascript"]
uppercase_words = list(map(to_uppercase, words))
print("Original:", words)
print("Uppercase:", uppercase_words)
output:
Original: ['python', 'java', 'c', 'javascript']
Uppercase: ['PYTHON', 'JAVA', 'C', 'JAVASCRIPT']

