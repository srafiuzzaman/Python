# Sahad Rafiuzzaman
# Date: 12/23/2023
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35,
# then the output should be 3 + 5 = 8. Warning. Do not change the code on line 1.
# Your program should work for different inputs. e.g. any two-digit number.
# The last line of your program should print the result.

# given input: 39

two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

# Check for data type
# print(type(two_digit_number))
# <class 'str'>

first_digit_number = int(two_digit_number[0])
second_digit_number = int(two_digit_number[1])

# Add the two integers together
two_digit_number = first_digit_number + second_digit_number
print(two_digit_number)
