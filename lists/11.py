numbers = [50, 42, 58, 27, 10]

# append()
numbers.append(15)
print("After append():", numbers)

# insert()
numbers.insert(1, 20)
print("After insert():", numbers)

# extend()
numbers.extend([25, 30])
print("After extend():", numbers)

# remove()
numbers.remove(27)
print("After remove():", numbers)

# pop()
numbers.pop()
print("After pop():", numbers)

# sort()
numbers.sort()
print("After sort():", numbers)

# reverse()
numbers.reverse()
print("After reverse():", numbers)

# count()
print("Count of 2:", numbers.count(2))

# index()
print("Index of 20:", numbers.index(20))
output:
After append(): [50, 42, 58, 27, 10, 15]
After insert(): [50, 20, 42, 58, 27, 10, 15]
After extend(): [50, 20, 42, 58, 27, 10, 15, 25, 30]
After remove(): [50, 20, 42, 58, 10, 15, 25, 30]
After pop(): [50, 20, 42, 58, 10, 15, 25]
After sort(): [10, 15, 20, 25, 42, 50, 58]
After reverse(): [58, 50, 42, 25, 20, 15, 10]
Count of 2: 0
Index of 20: 4
