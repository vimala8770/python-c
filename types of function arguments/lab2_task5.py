def order_summary(customer, *items, discount=0, **extra):
    print("Customer:", customer)
    print("Ordered Items:")
    for item in items:
        print("-", item)
    print("Discount:", discount, "%")
    print("Extra Information:")
    for key, value in extra.items():
        print(key.replace("_", " ").capitalize() + ":", value)
order_summary(
    "vimala",
    "Laptop",
    "Mouse",
    discount=10,
    delivery_address="tuni",
    gift_wrap=True
)
output:
Customer: vimala
Ordered Items:
- Laptop
- Mouse
Discount: 10 %
Extra Information:
Delivery address: tuni
Gift wrap: True
