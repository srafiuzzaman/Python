# Sahad Rafiuzzaman
# 01/09/2025

# Secret Auction Program
# The goal is to build a blind auction program.

# Demo
# https://appbrewery.github.io/python-day9-demo/

# Clearing the Output
# There are several ways of clearing the output.
# The easiest is to simply print "\n" many times so that the output scrolls down many lines. e.g.
"""
# This will add 20 new lines to the output
print("\n" * 20)
"""

# Functionality
# 1. Each person writes their name and bid.
# 2. The program asks if there are others who need to bid. If so, then the computer clears the output
# (prints several blank lines) then loops back to asking name and bid.
# 3. Each person's name and bid are saved to a dictionary.
# 4. Once all participants have placed their bid, the program works out who has the highest bid and prints it.

# Hint 1: Try writing out a flowchart to plan your program.
# Hint 2: The values that come from the input() function are Strings,
# you'll need to use the int() function to convert it to a number.


# Print Logo from 53A. Day 9 Project - Secret Auction Logo.py
import importlib.util

# Define the path to the file
file_path = "53A. Day 9 Project - Secret Auction Logo.py"

# Load the module from the file
spec = importlib.util.spec_from_file_location("secret_auction_logo", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Access the logo attribute
logo = module.logo

# Explanation:
'''import importlib.util'''
# importlib.util: This module provides utilities for working with the import system,
# allowing more control over how modules are imported dynamically.

'''file_path = "53A. Day 9 Project - Secret Auction Logo.py"'''
# file_path: This is the file path to the Python script you want to load dynamically. The file name includes spaces
# and special characters, which would make it unusable with standard Python import statements.

'''spec = importlib.util.spec_from_file_location("secret_auction_logo", file_path)'''
# spec_from_file_location: This function creates a ModuleSpec object, which describes how to load a module.
# "secret_auction_logo": This is the arbitrary name given to the module during runtime.
# file_path: The path to the Python file you want to load.
# Purpose: It tells Python where to find the module and how to load it.

'''module = importlib.util.module_from_spec(spec)'''
# module_from_spec: This function creates a new module object based on the specification (spec) created earlier.
# The module is not yet loaded. It's just an empty container at this point.

'''spec.loader.exec_module(module)'''
# exec_module: This method executes the module's code within the created module object (module). After this line,
# the module is fully loaded, and you can access its attributes (e.g., functions, classes, variables).

'''logo = module.logo'''
# module.logo: Accesses the logo attribute or variable defined in the dynamically loaded module (module).

# Print the logo
print(logo)
print("\nWelcome to the secret auction program.")

# Create a clear() function that clears the console
import os

def clear():
    # prints several blank line. A redundancy if the console cannot use system functions
    print("\n" * 50)
    # System functions
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary)  # max() function: highest value

    for bidder in bidding_dictionary:
        bid_amount = int(bidding_dictionary[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


# TODO-1: Ask the user for input
# name = input("What is your name?: ")
# price = int(input("what's your bid?: "))

# TODO-2: Save data into dictionary {name: price}
bids = {}
# bids[name] = price

# TODO-3: Whether if new bids need to be added
# should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")

continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()



