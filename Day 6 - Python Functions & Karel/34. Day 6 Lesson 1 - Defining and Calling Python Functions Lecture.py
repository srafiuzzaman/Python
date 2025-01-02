# Sahad Rafiuzzaman
# Date: 01/01/2025

# Functions
# A function in its simplest form is just a wrapper name for a block of code. You give it a name and then when you call
# the function by that name, all the code within the function block will be executed.
# It can help us save time and reduce repeated code.

# Defining a new Function
'''
def <function name>():
    print("Hello")
    <do something else>
    <do something else ...>
'''

# Calling a Function
# Calling a function just means triggering the function. WE can call a function at any point in our code in Python.
# <function name>()

# Putting everything together e.g.

name = ""
def get_user_name():
    name = input("What is your name? ")
    # Inside the function

# Outside the function
print("Hello")
get_user_name()     # Calling the function
print("Hello")
print(name)


# print function
print("Hello")

# len function
num_char = len("Hello")
print(num_char)

# defining a custom function
def my_function():
    print("Hello")
    print("Bye")

# Calling the function
my_function()
