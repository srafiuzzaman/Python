# Sahad Rafiuzzaman
# Date: 12/26/2024

# Modulo %
# What do you think this will output: 10 % 3 ?
print(10 % 3)  # 1

# Check Odd or Even
# Write some code using what you have learned about the modulo operator and conditional checks in Python to check if
# the number in the input area is odd or even. If it's odd print out the word "Odd" otherwise print out "Even".

number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
