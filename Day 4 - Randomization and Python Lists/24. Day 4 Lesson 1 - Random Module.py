# Sahad Rafiuzzaman
# Date: 12/27/2024

# Random Module
# https://docs.python.org/3/library/random.html
# To use it you need to first import it:  import random

import random

# random.randint(a, b)
# Returns a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

random_integer = random.randint(1, 10)
print(random_integer)

# Creating your own module
import my_module

print(my_module.my_favorite_number)

# random.random()
# Returns a random floating point number in the range 0.0 <= X < 1.0.

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

# random.uniform(a, b)
# Returns a random floating point number N such that a <= N <= b for a <= b and b<= N <= a for b < a.
# The end-point value b may or may not be included in the range depending on the floating-point rounding
# in the expression a + (b-a) * random().

random_float = random.uniform(1, 10)
print(random_float)