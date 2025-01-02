# Sahad Rafiuzzaman
# 12/28/2023
# Hangman Game

import random
import os
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

# create clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Using word_list from hangman_words.py
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

# Printing the hangman logo
print(logo)

chosen_word = random.choice(word_list)  # chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

# Create blanks
placeholder = ""
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    # clearing the screen
    clear()

    # Tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # The user has entered a letter they've already guessed.
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # The letter is not in the chosen_word.

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            # Give the user the correct word they were trying to guess.
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Use the stages List from the file hangman_art.py
    print(stages[lives])

-------
game_over = False
lives = 6



# Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
#
# while not game_over:
#     guess = input("Guess a letter: ").lower()
#
#     # clearing the screen
#     clear()
#
#     # The user has entered a letter they've already guessed.
#     if guess in display:
# #         print(f"You've already guessed {guess}.")
#
#     # # Check guessed letter
#     # for position in range(word_length):
#     #     letter = chosen_word[position]
#     #     if letter == guess:
#     #         display[position] = letter
#
#     # Check if user is wrong.
#     if guess not in chosen_word:
#         print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")
#         lives -= 1
#         if lives == 0:
#             game_over = True
#             print("You lose.")
#             print(f'\nPssst, the solution was {chosen_word}.')
#
#     # Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")
#
#     # Check if user has got all letters.
#     if "_" not in display:
#         game_over = True
#         print("You win.")
#
#     # print the life stages
#     print(stages[lives])
