# Sahad Rafiuzzaman
# 12/25/2024

# Flooring a Number
# You can floor a number or remove all decimal places using the int() function which converts a floating point number
# (with decimal places) into an integer (whole number).

# int(3.738492)         # Becomes 3

bmi = 84 / 1.65 ** 2

print(bmi)              # 30.85399449035813
print(int(bmi))         # 30

# Rounding a Number
# However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way,
# where anything over .5 rounds up and anything below rounds down. Then you can use the python round () function.

print(round(bmi))       # 31
print(round(bmi, 2))    # 30.85

# Assignment Operators
# Assignment operators such as the addition assignment operators += will add the number on the right to the original
# value of the variable on the left and assign the new value to the variable. += -= *= /=

score = 0

score += 1
print(score)            # 1
score -= 2
print(score)            # -1
score *= 3
print(score)            # -3
score /= 4
print(score)            # -0.75

# f-Strings
# In Python, we can use f-strings to insert a variable or an expression into a string.

print("Your score is " + str(score))

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. Your are winning is {is_winning}.")