string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if sorted(string1.lower()) == sorted(string2.lower()):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
    output:
Enter first string: listen
Enter second string: silent
The strings are anagrams.

