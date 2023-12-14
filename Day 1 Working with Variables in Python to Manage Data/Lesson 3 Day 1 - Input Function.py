# Sahad Rafiuzzaman
# Date: 12/14/2023
# Task 1

print("Enter the names of your three friends:")
name1 = input("What is your first friend's name? ")
print(name1 +"\n")        #This line will print the text and line 1 of the input into the output.
name2 = input("What is your second friend's name? ")
print(name2 +"\n")        #This line will only print the name on line 2 of the input pane.
name3 = input("What is your third friend's name? ")
print(name3 +"\n")

# Task 2
# Try this exercise to understand how tests work with inputs in Auditorium. Write some code that multiples together
# the two numbers in the input area. When you run the tests, different inputs will replace the ones in the input area
# and pass the new inputs through your code.
print("This will multiply two integers:")
num1 = int(input("What is the first number: "))
num2 = int(input("What is the second number: "))
print(num1 * num2)

# Task 3
# Write a program that calculates and outputs the number of characters in any name.
# The automated tests will try out lots of different names as the input. Your code should work for any name.

print("\nThis will output the number of characters in any name")
name = input("What is your name? ")
print(len(name))
