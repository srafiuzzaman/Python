# Sahad Rafiuzzaman
# 01/01/2024
# Secret Auction

# imports
import os
from Secret_Auction_Logo import logo

# Define clear() function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Show Logo
print(logo)

# Ask for Name input
name = input()
# Ask for Bid Price
# Add Name and Bid into a dictionary as the key and value
# Ask if there are other users who want to bid
# if yes, clear the screen
# if no, Find the highest bid in the dictionary and declare them as the winner
