# Sahad Rafiuzzaman
# 04/13/2024
# Secret Auction Program

# Create a clear() function that clears the console
import os
def clear():
    if os.name =='nt':
        os.system('cls')
    else:
        os.system('clear')
        

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela":123, "James":321}
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.") 
    
from importlib import import_module
logo = import_module("Day 9 Project - Art Logo").logo

# import_module("Day 9 Project - Art Logo"): This dynamically imports the module named "Day 9 Project - Art Logo".
# The argument passed to import_module is the name of the module you want to import. Since Python modules can't have spaces in their names, 
# this name should match the module name defined in the file.

# .logo: This accesses the logo attribute from the imported module. Assuming that "Day 9 Project - Art Logo.py" defines a variable or object named logo,
# this line retrieves that object.

print(logo)
print("\nWelcome to the secret auction program.")

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    price = input("what's your bid?: ")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()
