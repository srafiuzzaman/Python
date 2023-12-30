# Sahad Rafiuzzaman
# 12/28/2023
# Hangman Game

import random
import os
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

# create clear screen function
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Using word_list from hangman_words.py
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Printing the hangman logo
print(logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # clearing the screen
    clear_console()

    # The user has entered a letter they've already guessed.
    if guess in display:
        print(f"You've already guessed {guess}.")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'\nPssst, the solution was {chosen_word}.')

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # print the life stages
    print(stages[lives])
