# Sahad Rafiuzzaman
# 01/05/2025

# The Python Dictionary: Deep Dive

def newline():
    print('\n')

# A dictionary in Python functions similarly to a dictionary in real life.
# It's a data structure that allows us to associate a key to a value and pair the two pieces of data together.

# This is how you create a dictionary in Python:
# An example dictionary
colors = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow"
}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}


# This is how you retrieve items from a dictionary:
print(colors["pear"])  # Will print "green"
newline()

print(programming_dictionary["Bug"])
newline()
# print(programming_dictionary["Bog"])      # KeyError: Bog does not exist in the dictionary
# print(programming_dictionary[Function])   # NameError: Function is not defined. Incorrect data type.

# This is how you can add new items to an existing dictionary:
colors["peach"] = "pink"

programming_dictionary["Loop"] = "The action of doing something over and over again."


# This is how to create an empty dictionary:
my_empty_dictionary = {}


# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)
newline()

# redefining the dictionary
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again."
}


# This is also how you can edit an existing value in a dictionary:
colors["apple"] = "green"

programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)
newline()

# This is how to loop through a dictionary and print all the keys:
for key in colors:
    print(key)
newline()

for thing in programming_dictionary:
    print(thing)      # Bug, Function, Loop
newline()


# This is how to loop through a dictionary and print all the values:
for key in colors:
    print(colors[key])
newline()

for thing in programming_dictionary:
    print(programming_dictionary[thing])
newline()

