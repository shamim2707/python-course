# Python program demonstrating first-class functions

# Functions as objects
def greet(name):
    return f"Hello, {name}!"

# Assigning a function to a variable
greeting = greet
print(greeting("Alice"))

# Passing a function as an argument
def call_function(func, value):
    return func(value)

print(call_function(greet, "Bob"))

# Returning a function from another function
def outer_function():
    def inner_function():
        return "This is the inner function!"
    return inner_function

inner = outer_function()
print(inner())