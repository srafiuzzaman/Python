# Sahad Rafiuzzaman
# Date: 01/04/2025

# Positional vs. Keyword Arguments

# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?\n")

greet_with_name("Sahad")

# Multiple Inputs
# You can have multiple inputs in functions. All you need to do is separate them with a comma ,.

# Create a function with multiple inputs
"""
# Hint
def greet(name, greeting):
____print(f"{greeting} {name}")
greet("Angela", "Yo!")
"""

# Modify the function so that it prints the expected values.
"""
def greet_with(name, location)
    Hello name
    What is it like in location
"""

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}\n")

greet_with("Sahad", "Nowhere")
greet_with("Nowhere", "Sahad")          # Positional argument

# Positional Arguments
# By default, when you create a function in Python, it will keep the order of arguments in the function definition.
# e.g. In the function below, the first argument that goes in will always be printed before the second one. a = 2, b = 1
"""
def my_function(a, b)
    print(a)
    print(b)

    my_function(2, 1)
    # It will print:
    # 2
    # 1
"""


# Keyword Arguments
# You can use keywords when you provide the arguments when you call a function so that there is less confusion
# which value is assigned to which input parameter.
"""
# Hint
# Call the greet_with() function using keyword arguments.
greet_with(location="London", name="Angela")
"""
greet_with(name= "Sahad", location="Pennsylvania")
