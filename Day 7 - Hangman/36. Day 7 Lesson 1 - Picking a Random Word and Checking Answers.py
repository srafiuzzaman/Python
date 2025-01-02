# Sahad Rafiuzzaman
# Date: 01/02/2025

# Step 1: How to Check the User's Answer
# Your Goal is to build a Hangman game using everything you have learned about Python programming.
# The project is split into 5 major steps. In each step, there will be multiple TODOs. Your goal is to go through each
# Your goal is to go through each to do in order and complete them.


word_list = ["aardvark", "baboon", "camel"]

# TODO-1: Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
import random
chosen_word = random.choice(word_list)

# TODO-2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
print(guess)

# TODO-3: Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#   Print "Right" if it is, "Wrong" if it's not.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
