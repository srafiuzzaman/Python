# Sahad Rafiuzzaman
# 01/09/2025

# Nesting Lists and Dictionary
# You can mix and match various data types to achieve your desired structure.
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

# Nesting a List inside a Dictionary
# Instead of a String value assigned to a key, we can replace it with a List.
# You can nest a List in a Dictionary like this:
"""
my_dictionary = {
    key1: [List],
    key2: Value,
}
"""
# See if you can figure out how to print out "Lille" from the nested List called travel_log.
'''
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
'''
# Hint: To get this part: ["Paris", "Lille", "Dijon"] You would need: travel_log["France"]
# Therefore to get Lille, you need: travel_log["France"][1]

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Print Lille
print(travel_log)                 # prints out the entire travel log
print(travel_log["France"])       # prints out the France travel log
print(travel_log["France"][1])    # prints out Lille


# Nesting Lists inside other Lists
# We've previously seen Nested Lists:
''' nested_list = ["A", "B", ["C", "D"]] '''
# Do you remember how to get items that are nested deeply in a list? Try to print "D" from the list nested_list.
# Hint: To get this list: ["C", "D"] we need the code:
''' nested_list[2] '''
# Therefore, to get "D" we need:
''' nested_list[2][1] '''

nested_list = ["A", "B", ["C", "D"]]

# Print D
print(nested_list)              # prints: ['A', 'B', ['C', 'D']]
print(nested_list[2])           # prints: ['C', 'D']
print(nested_list[2][1])        # prints: D


# Nesting a Dictionary inside a Dictionary
# You can also nest a dictionary in a dictionary:
'''
my_dictionary = {
    key1: Value,
    key2: {Key: Value, Key: Value},
}
'''
# Figure out how to print out "Stuttgart" from the following list:
'''
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
'''

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

# Print Stuttgart
print(travel_log)                                        # prints out the entire travel log
print(travel_log["Germany"])                             # prints out the Germany travel log
print(travel_log["Germany"]["cities_visited"])           # prints: ['Berlin', 'Hamburg', 'Stuttgart']
print(travel_log["Germany"]["cities_visited"][2])        # prints: ['Berlin', 'Hamburg', 'Stuttgart']
