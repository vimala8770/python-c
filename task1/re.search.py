import re
sentence = "1024 requests were served in 3 seconds"
result = re.search(r"served", sentence)
if result:
    print("Found:", result.group())
    print("Position:", result.span())
else:
    print("Word not found.")
    output:
Found: served
Position: (19, 25)

