# Sahad Rafiuzzaman
# 12/25/2023

# Create a coin flip program using what you have learned about randomization in Python. It should randomly print "Heads"
# or "Tails" everytime it is run.

import random
random_side = random.randint(0, 1)
# print(random_side)

if random_side == 1:
    print("Heads")
else:
    print("Tails")
    