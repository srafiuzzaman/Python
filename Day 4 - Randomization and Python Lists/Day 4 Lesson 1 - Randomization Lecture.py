# Sahad Rafiuzzaman
# 12/25/2023
# Randomization
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

import random

# Generating Random Integers
# randint(a,b)
# Returns a random integer between a and b (both inclusive). This also raises a ValueError if a > b.

random_integer = random.randint(1, 10)
print(random_integer)

# Generating Random floating point numbers
# random.random()
# Returns the next random floating point number between [0.0 to 1.0)
random_float = random.random() * 5
print(random_float)


love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")