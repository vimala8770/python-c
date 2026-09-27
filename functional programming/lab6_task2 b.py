def is_palindrome(word):
    return word == word[::-1]
words = ["madam", "python", "level", "hello", "radar", "world"]
palindromes = list(filter(is_palindrome, words))
print("Palindrome words:", palindromes)
output:
Palindrome words: ['madam', 'level', 'radar']

