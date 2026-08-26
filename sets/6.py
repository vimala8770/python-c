my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print("After remove(3):", my_set)
my_set.discard(4)
print("After discard(4):", my_set)
my_set.discard(10)   
print("After discard(10):", my_set)
output:
After remove(3): {1, 2, 4, 5}
After discard(4): {1, 2, 5}
After discard(10): {1, 2, 5}
