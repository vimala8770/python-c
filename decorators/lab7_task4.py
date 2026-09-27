def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
@repeat(3)
def greeting():
    print("Hello! Welcome to Python.")
greeting()
output:
Hello! Welcome to Python.
Hello! Welcome to Python.
Hello! Welcome to Python.
