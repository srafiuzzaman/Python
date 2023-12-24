# Sahad Rafiuzzaman
# Date: 12/23/2023
# Create a tip calculator

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?\n$ "))
tip_percent = int(input("What percentage tip would you like to give?\n"))
num_people = int(input("How many people to split the bill?\n"))
costperperson = (total_bill/num_people)*(1+(tip_percent/100))
costperperson = "{:.2f}".format(costperperson)
print(f"Each person should pay ${costperperson}")