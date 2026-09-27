# (a) Square of a number
square = lambda x: x * x
print("Square:", square(5))
# (b) Check if a number is even
is_even = lambda x: x % 2 == 0
print("Is 10 even?", is_even(10))
print("Is 7 even?", is_even(7))
# (c) Find larger of two numbers
larger = lambda a, b: a if a > b else b
print("Larger number:", larger(15, 25))
output:
Square: 25
Is 10 even? True
Is 7 even? False
Larger number: 25
