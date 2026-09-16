import re

sentence = "1024 requests were served in 3 seconds"
m1 = re.match(r"\d", sentence)
if m1:
    print("The sentence starts with a digit.")
    print("Match:", m1.group())
else:
    print("The sentence does not start with a digit.")
output:
The sentence starts with a digit.
Match: 1

