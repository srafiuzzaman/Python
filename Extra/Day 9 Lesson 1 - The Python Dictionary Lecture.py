# Sahad Rafiuzzaman
# 01/01/2024
# The Python Dictionary: Deep Dive

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# Retrieving items from dictionary.
print(programming_dictionary["Function"])
print("\n")

# Misspelling the key will produce a KeyError.
# Data types should be the same as the dictionary

# Adding new items to the dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)
print("\n")

# Creating an empty dictionary
empty_dictionary = {}

# Wiping an existing dictionary
# programming_dictionary = {}       # Commented out to make Looping through a dictionary work
# print(programming_dictionary)     # Commented out to make Looping through a dictionary work
# print("\n")

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary
for thing in  programming_dictionary:
    print(thing)
print("\n")
# will print out:    Bug
#                    Function
#                    Loop
# It will only print out the key only

for key in programming_dictionary:
    print(key)                              # Prints out the key only
    print(programming_dictionary[key])      # Prints out the key and key value
