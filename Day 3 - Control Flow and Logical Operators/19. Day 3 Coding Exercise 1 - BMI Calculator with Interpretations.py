# Sahad Rafiuzzaman
# Date: 12/26/2024

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"

# Enter your height in meters e.g., 1.85
height = float(input("Enter your height in meters? "))
# Enter your weight in kilograms e.g., 85
weight = int(input("Enter your weight in kilograms? "))
bmi = (weight / (height ** 2))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(bmi, 1)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25:
  print(f"Your BMI is {bmi}, you are overweight.")
