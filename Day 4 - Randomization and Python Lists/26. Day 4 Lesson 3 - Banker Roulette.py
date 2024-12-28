# Sahad Rafiuzzaman
# Date: 12/27/2024

# Banker Roulette
# Figure out how to pick a random name from the list of friends.
# Hint: use random.choice(seq)
# Returns a random element form the non-empty sequence seq. If seq is empty, raises IndexError.

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
print(random.choice(friends))

# Option 2
random_index = random.randint(0, 4)
print(friends[random_index])
