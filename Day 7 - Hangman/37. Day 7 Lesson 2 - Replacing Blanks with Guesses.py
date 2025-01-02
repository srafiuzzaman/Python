# Sahad Rafiuzzaman
# Date: 01/02/2025

# Step 2: Replacing Blanks with Guesses

import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# TODO-1: Create a "Placeholder" with the same number of blanks as the chosen_word.
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += " _ "
print(placeholder)

guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display that puts the guess letter in the right position and _ in the rest of the string.
display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += " _ "
print(display)
