data = (10, 20, [30, 40, 50])

print("Before modification:", data)

data[2].append(60)

print("After modification:", data)
output:
Before modification: (10, 20, [30, 40, 50])
After modification: (10, 20, [30, 40, 50, 60])
