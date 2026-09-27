def greet(name):
    return "Hello " + name
# (a) Assigning function to another variable
new_function = greet
print(new_function("Vimala"))
# (b) Passing function as an argument
def execute_function(func, name):
    print(func(name))
execute_function(greet, "Python")
# (c) Returning a function from another function
def create_greeting():
    def message():
        return "Welcome to Python!"
    return message
my_function = create_greeting()
print(my_function())
output:
Hello Vimala
Hello Python
Welcome to Python!
