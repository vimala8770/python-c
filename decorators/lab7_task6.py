import time
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Execution time:", end_time - start_time, "seconds")
        return result
    return wrapper
@log_call
@timer
def calculate(a, b):
    time.sleep(1)
    return a + b
result = calculate(10, 20)
print("Final result:", result)
output:
Calling wrapper
Execution time: 1.0007741451263428 seconds
wrapper returned 30
Final result: 30
