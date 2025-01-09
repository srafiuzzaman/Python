# Sahad Rafiuzzaman
# Date: 01/04/2025

# Love Calculator
# 💪 This is a difficult challenge! 💪
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.
# To work out the love score between two people:

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number and print it out.

# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3

# Love Score = 53

# Example Input
# calculate_love_score("Kanye West", "Kim Kardashian")

# Example Output
# 42

# How to test your code and see your output?
# Udemy coding exercises do not have a console, so you cannot use the input() function.
# You will need to call your function with hard-coded values like so:
"""
def calculate_love_score(name1, name2):
    # your code here

# Call your function with hard coded values
# calculate_love_score("Kanye West", "Kim Kardashian")
"""

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    uppercase_names = combined_names.upper()

    T = uppercase_names.count("T")
    R = uppercase_names.count("R")
    U = uppercase_names.count("U")
    E = uppercase_names.count("E")
    first_digit = T + R + U + E

    L = uppercase_names.count("L")
    O = uppercase_names.count("O")
    V = uppercase_names.count("V")
    E = uppercase_names.count("E")
    second_digit = L + O + V + E

    score = int(str(first_digit) + str(second_digit))
    print(f"{score}\n")

# Call your function with hard coded values
calculate_love_score("Kanye West", "Kim Kardashian")

# Without hard coded values: User inputs names
def love_calculator(name1, name2):
    combined_names = name1 + name2
    uppercase_names = combined_names.upper()

    T = uppercase_names.count("T")
    R = uppercase_names.count("R")
    U = uppercase_names.count("U")
    E = uppercase_names.count("E")
    first_digit = T + R + U + E

    L = uppercase_names.count("L")
    O = uppercase_names.count("O")
    V = uppercase_names.count("V")
    E = uppercase_names.count("E")
    second_digit = L + O + V + E

    score = int(str(first_digit) + str(second_digit))

    if int(score) < 10 or int(score) > 90:
        print(f"Your score is {score}, you go together like coke and mentos.\n")
    elif 40 <= score <= 50:
        print(f"Your score is {score}, you are alright together.\n")
    else:
        print(f"Your score is {score}.\n")

name1 = input("What is your name? ")
name2 = input("What is their name? ")
love_calculator(name1, name2)


