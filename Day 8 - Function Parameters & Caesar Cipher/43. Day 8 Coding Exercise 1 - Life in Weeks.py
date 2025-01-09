# Sahad Rafiuzzaman
# Date: 01/02/2025

# Life in Weeks
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left,
# if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.

# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

# **Warning** The function must be called life_in_weeks for the tests to pass.
# Also, the output must have the same punctuation and spelling as the example. Including the full stop!

# Example Input
# 56

# Example Output
# You have 1768 weeks left.

def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")

# Call your function with hard coded values.
age = int(input("Please enter your age: "))
life_in_weeks(age)
