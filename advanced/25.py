def my_find(s, sub):
    if sub == "":
        return 0

    for i in range(len(s) - len(sub) + 1):
        match = True

        for j in range(len(sub)):
            if s[i + j] != sub[j]:
                match = False
                break

        if match:
            return i

    return -1


def my_count(s, sub):
    if sub == "":
        return len(s) + 1

    count = 0
    i = 0

    while i <= len(s) - len(sub):
        match = True

        for j in range(len(sub)):
            if s[i + j] != sub[j]:
                match = False
                break

        if match:
            count += 1
            i += len(sub)
        else:
            i += 1

    return count


s = input("Enter the main string: ")
sub = input("Enter the substring: ")

print("Find position:", my_find(s, sub))
print("Count:", my_count(s, sub))
output:
Enter the main string: hello world
Enter the substring: world
Find position: 6
Count: 1

