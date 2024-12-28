# Sahad Rafiuzzaman
# Date: 12/26/2024

# Write a Pizza Delivery Program
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill. Use the input() function to get the user's preferences and
# then add up the total for their order and tell them how much they have to pay.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1


print("Thank you for choosing Python Pizza Deliveries!")

# Get a valid pizza size
while True:
    size = input("What size pizza do you want? S, M, or L\n").upper()   # What size pizza do you want? S, M, or L
    if size in ["S", "M", "L"]:
        break   # Exit the loop if the size is valid
    print("Invalid size. Please enter S, M, or L.\n")

# Get whether the user wants pepperoni
while True:
    add_pepperoni = input("Do you want pepperoni? Y or N\n").upper()    # Do you want pepperoni? Y or N
    if add_pepperoni in ["Y", "N"]:
        break # Exit the loop if the entry is valid
    print("Invalid entry. Please enter Y or N\n")

# Get whether the user want extra cheese
while True:
    extra_cheese = input("Do you want extra cheese? Y or N\n").upper()  # Do you want extra cheese? Y or N
    if extra_cheese in ["Y", "N"]:
        break # Exit the loop if the entry is valid
    print("Invalid entry. Please enter Y or N\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Initialize the bill
bill = 0

# Calculate the base price based on pizza size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

# Add cost for pepperoni
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size in ["M", "L"]:  # Applies to medium and large pizzas
        bill += 3

# Add cost for extra cheese
if extra_cheese == "Y":
    bill += 1

# Print the final bill with details
# Determine pizza size status
if size == "S":
    size_name = "small"
elif size == "M":
    size_name = "medium"
elif size == "L":
    size_name = "large"

# Determine pepperoni status
if add_pepperoni == "Y":
    pepperoni_status = "with pepperoni"
else:
    pepperoni_status = "without pepperoni"

# Determine cheese status
if extra_cheese == "Y":
    cheese_status = "and extra cheese"
else:
    cheese_status = "without extra cheese"

print(f"You ordered a {size_name} pizza {pepperoni_status} {cheese_status}.")
print(f"Your final bill is: ${bill}.")
