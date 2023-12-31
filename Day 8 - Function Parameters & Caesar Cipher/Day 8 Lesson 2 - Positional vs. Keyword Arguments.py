# Sahad Rafiuzzaman
# 12/31/2023
# Positional vs. Keyword Arguments

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Saleem", "Philadelphia")
print("\n")

# Observe the difference in the positional argument
greet_with("Philadelphia", "Saleem")
print("\n")

# Positional Arguments
# def my_function (a, b, c):
#     Do this with a
#     Then do this with b
#     Finally do this with c
#
# my_function(1, 2, 3)
#   a = 1
#   b = 2
#   c = 3
#
# my_function(3, 2, 1)
#   a = 3
#   b = 2
#   c = 1

# Keyword Arguments
# def my_function (a, b, c):
#     Do this with a
#     Then do this with b
#     Finally do this with c
#
# my_function(a = 1, b = 2, c = 3)
#
# The order does not matter because the arguments will abide to the bindings
# my_function(c = 3, b = 2, a = 1)

# Functions with Keyword Arguments
greet_with(name = "Saleem", location = "London")
print("\n")

greet_with( location = "London", name = "Saleem")