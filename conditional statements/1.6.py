ch = input("Enter a character: ")

if ch.isalpha():
    if ch.lower() in "aeiou":
        print("It is a vowel")
    else:
        print("It is a consonant")
elif ch.isdigit():
    print("It is a digit")
else:
    print("It is a special symbol")
    output:
Enter a character: v
It is a consonant
Enter a character: 6
It is a digit
Enter a character: @
It is a special symbol
