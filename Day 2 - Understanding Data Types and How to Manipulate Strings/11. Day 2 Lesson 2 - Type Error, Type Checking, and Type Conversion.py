# Sahad Rafiuzzaman
# 12/25/2024

# TypeError
# These errors occur when you are using the wrong data type. e.g. len(12345)
# Because you can only give the len() function Strings,
# it will refuse to work and give you a TypeError if you give it a number (Integer).

"""
len(12345)          # TypeError: object of type 'int' has no len()
"""

# Fix the len() function so it has no more warnings or errors.

len("12345")        # 12345

# Type Checking
# You can check the data type of any value of variable in python using the type() function.

"""
print(type("abc"))  # <class 'str'>
"""

print(type("Hello"))                # <class 'str'>

# Write out the four types of checks to print all four data types.
# Using the type() and print() functions to print out four lines into the output area, so we get the full collection
# of data types that we learned about. <class 'str'> <class 'int'> <class 'float'> <class 'bool'>

print(type("Sahad"))                # <class 'str'>
print(type(12345))                  # <class 'int'>
print(type(3.14159))                # <class 'float'>
print(type(True))                   # <class 'bool'>

# Type Conversion
# You can convert data into different data types using special functions. e.g. float(), int(), str(), bool()

print("123" + "456")                # 123456
print(int("123") + int("456"))      # 579

"""
print(int("abc") + int("456"))      # ValueError
"""

# Make this line of code run without errors.

"""
print("Number of letters in your name: " + len(input("Enter your name ")))
"""

print("Number of letters in your name: " + str(len(input("Enter your name "))))


