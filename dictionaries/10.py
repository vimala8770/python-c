items = {
    "Laptop": 60000,
    "Phone": 30000,
    "Tablet": 20000,
    "Headphones": 5000
}

highest_item = max(items, key=items.get)
lowest_item = min(items, key=items.get)

print("Highest priced item:", highest_item)
print("Price:", items[highest_item])

print("Lowest priced item:", lowest_item)
print("Price:", items[lowest_item])
output:
Highest priced item: Laptop
Price: 60000
Lowest priced item: Headphones
Price: 5000
