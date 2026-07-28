a = 10
b = 20

print("Before swapping:")
print("a =", a, "b =", b)

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a, "b =", b)
a = 10
b = 20

print("Before swapping:")
print("a =", a, "b =", b)

a, b = b, a

print("After swapping:")
print("a =", a, "b =", b)
 output:
Before swapping:
a = 10 b = 20
After swapping:
a = 20 b = 10
Before swapping:
a = 10 b = 20
After swapping:
a = 20 b = 10

