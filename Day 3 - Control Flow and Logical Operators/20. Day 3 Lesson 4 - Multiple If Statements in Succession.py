# Sahad Rafiuzzaman
# Date: 12/26/2024

# Multiple Ifs
# You can write as many if statements as you need to check for different conditions that are unrelated to each other.
# Compare the code blocks below:

"""
if/elif/else
if <condition 1 is true>
    <do A>
elif <condition 2 is true>
    <do B>
else
    <do C>

Nested if statements
if <condition 1 is true>
    <do A>
    if <condition 2 is true>
        <do B>
        if <condition 3 is true>
            <do C>
"""

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
