# Sahad Rafiuzzaman
# Date: 12/27/2024

# Lists
# https://docs.python.org/3/tutorial/datastructures.html

# You can create a simple collection  of ordered items using Python list. e.g.
# fruits = [item1, item2]
# fruits = ["Cherry", "Apple, "Pear"]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])       # Delaware
print(states_of_america[-1])      # Hawaii
print(states_of_america)          # prints out the whole list

# Altering items in a list
states_of_america[1] = "Pencilvania"
print(states_of_america)

# Appending Items to Lists
# list.append(x)
# Add an item to the end of the list.

states_of_america.append("Sahadland")
print(states_of_america)

# list.extend(iterable)
# Extend the list by appending all the items from the iterable.
new_states = ["Rafiland","Zamanland"]
states_of_america.extend(new_states)
print(states_of_america)




