# Sahad Rafiuzzaman
# Date: 12/26/2024

# Nested if / else
"""
if condition:
  if another condition:
    do this
  else:
    do this
else:
  do this
"""

# if/elif/else
"""
if condition1:
  do A
elif condition2:
  do B
else:
  do this
"""

# Nesting and Elif
# You cna put if/else statements inside other if/else statements. This is known as nesting. e.g.
"""
if math_score >= 90:
  if english_score >= 90:
    print("You're good at everything")
  else:
    print("You're good at math")
  if english_score >= 90:
    print("You're good at english")
"""
# In this case only when a student has over 90 in math and english, do they get "You're good at everything".
# Note: you can also have if statements that don't have a paired else statement.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in inches? "))

if height >= 48:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

