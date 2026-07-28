import keyword

word = input("Enter a word: ")

if keyword.iskeyword(word):
    print(word, "is a Python keyword.")
else:
    print(word, "is NOT a Python keyword.")
    output:
Enter a word: akki
akki is NOT a Python keyword.
