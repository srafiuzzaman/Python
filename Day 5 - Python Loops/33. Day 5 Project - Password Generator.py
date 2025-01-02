# Sahad Rafiuzzaman
# Date: 12/31/2024

# Password Generator Project
# The program will ask:
# How many letters would you like in your password?
# How many symbols would you like?
# How many numbers would you like?

# The objective is to take the inputs from the user to these questions and then generate a random password.
# Use your knowledge about Python lists and loops to complete the challenge.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_of_letters = int(input(f"How many letters would you like in your password?\n"))
num_of_symbols = int(input(f"How many symbols would you like?\n"))
num_of_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Version
# Generate the password in sequence. Letters, then symbols, then numbers. If the user wants 4 letters 2 symbols and 3
# numbers then the password might look like this: fgdx$*924
# You can see that all the letters are together.
# All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.

password = ""

for char in range(1, num_of_letters + 1):
    random_char = random.choice(letters)
    password += random_char
for char in range(1, num_of_symbols + 1):
    random_char = random.choice(symbols)
    password += random_char
for char in range(1, num_of_numbers + 1):
    random_char = random.choice(numbers)
    password += random_char
print(f"Your password is: {password}")

# random.choice(seq)
# This is a widely used function in practice, wherein you would want to randomly pick up an item from a List/sequence.


# Hard Version
# When you've completed the easy version, you're ready to tackle the hard version.
# In the advanced version of this project the final password does not follow a pattern.
# So the example above might look like this: x$d24g*f9
# And every time you generate a password, the positions of the symbols, numbers, and letters are different.
# This will make the password more difficult.

password_list = []

for char in range(1, num_of_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, num_of_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, num_of_numbers + 1):
    password_list.append(random.choice(numbers))
print(password_list)

# How can I reorder a list: random.shuffle(x)
# This is used to shuffle the sequence in place. A sequence can be any list/tuple containing elements.
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")

