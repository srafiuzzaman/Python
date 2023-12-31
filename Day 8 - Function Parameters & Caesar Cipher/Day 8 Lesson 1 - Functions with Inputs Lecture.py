# Sahad Rafiuzzaman
# 12/31/2023
# Functions with Inputs

# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def my_function(something)
#     Do this with something
#     Then do this
#     Finally do this
# my_function(123)

# Simple Function
def greet():
    print("Hello")
    print("How are you?")
    print("Isn't the weather nice today?")

greet()

print("\n")

# Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")

greet_with_name("Saleem")
print("\n")
greet_with_name("Asad")
print("\n")
greet_with_name("Mimi")