list1 = [10, 30, 20, 50]
list2 = [40, 60, 15, 5]

combined = list1 + list2
combined.sort(reverse=True)

print("Combined list in descending order:", combined)
output:
Combined list in descending order: [60, 50, 40, 30, 20, 15, 10, 5]
