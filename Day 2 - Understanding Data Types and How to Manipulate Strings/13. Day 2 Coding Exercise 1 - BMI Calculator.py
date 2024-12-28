# Sahad Rafiuzzaman
# Date: 12/25/2024

# BMI Calculator

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person
# both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# Create a calculator to test someone's BMI using mathematical operators in Python.

# Given input: 1.65, 84

# 1st input: enter height in meters e.g: 1.65
height = input("Enter height in meters: ")

# 2nd input: enter weight in kilograms e.g: 84
weight = input("Enter weight in kilograms: ")

# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# Calculate the bmi using weight and height.

int_weight = int(weight)
float_height = float(height)
bmi = int_weight / float_height ** 2
print("BMI: " + str(int(bmi)))         # 30.85399449035813

