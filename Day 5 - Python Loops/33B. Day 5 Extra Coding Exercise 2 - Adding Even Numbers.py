# Sahad Rafiuzzaman
# 12/26/2023
# Adding Even Numbers

# You are going to write a program that calculates the sum of all the even numbers from 1 to X.
# If X is 100 then the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 + 10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output.
# It should just print the final total and not every step of the calculation.

# Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

# Example Input 1
# 10

# Example Output 1
# 30
print("Welcome! This program calculates the sum of all the even numbers from 1 to X.")
target = int(input("Enter a number between 0 and 1000\n"))  # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
even_sum = 0
for number in range(2, target + 1, 2):
    even_sum += number
print(even_sum)

# Another method
alternative_sum = 0
for number in range(1, target + 1):
    if number % 2 == 0:
        alternative_sum += number
print(alternative_sum)
