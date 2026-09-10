s = input("Enter a string: ")
counts = {}
for ch in s:
    counts[ch] = counts.get(ch, 0) + 1
print("Duplicate characters:")
for ch, count in counts.items():
    if count > 1:
        print(ch, ":", count)
        output:
Enter a string: vimala
Duplicate characters:
a : 2
