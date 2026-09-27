def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    final_price = price + tax - discount
    return final_price
print("Final price:", calculate_price(1000))
print("Final price:", calculate_price(1000, 10))
print("Final price:", calculate_price(1000, 10, 100))
output:
Final price: 1180.0
Final price: 1100.0
Final price: 1000.0
