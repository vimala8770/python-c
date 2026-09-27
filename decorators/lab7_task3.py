import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Execution time:", end_time - start_time, "seconds")
        return result
    return wrapper
@timer
def calculate_sum():
    total = 0
    for i in range(1, 1000001):
        total += i
    return total
result = calculate_sum()
print("Sum:", result)
output:
Execution time: 0.02672886848449707 seconds
Sum: 500000500000
