# Sahad Rafiuzzaman
# Date: 12/25/2024

# Tip Calculator Project
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay: (150.00/ 5) * 1.2 = 33.6
# After formatting the results to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n$ "))
tip_percent = float(input("What percentage tip would you like to give?\n"))
num_people = int(input("How many people to split the bill?\n"))
billperperson = "{:.2f}".format((total_bill / num_people) * (1 + (tip_percent / 100)))
print(f"Each person should pay ${billperperson}")

