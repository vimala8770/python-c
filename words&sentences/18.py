sentence = input("Enter a sentence: ")
words = sentence.split()
result = []
for word in words:
    result.append(word[0].upper() + word[1:])
print("Title Case:", " ".join(result))
output:
Enter a sentence: vimala is good girl
Title Case: Vimala Is Good Girl

