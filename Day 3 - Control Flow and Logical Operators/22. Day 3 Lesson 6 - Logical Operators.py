# Sahad Rafiuzzaman
# Date: 12/26/2024

# Logical Operators
# You can combine different conditions using logical operators.
"""
A and B     # Both conditions need to be true
C or D      # Only one condition needs to be true
not E       # The condition must be false

"""

# Age 45 to 55 Modifier
# Update the code so that people age 45 to 55 (inclusive of both ages) ride for free.
# Use logical operators to check that the age is greater than 45, and it's also less than 55.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in inches? "))
bill = 0

if height >= 48:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif 45 <= age <= 55:       # elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us.")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
        # Adds $3 to their bill
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")


