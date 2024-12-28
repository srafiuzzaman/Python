# Sahad Rafiuzzaman
# Date : 12/27/2024


# Treasure Map
# You are going to write a program that will mark a spot on a map with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what it looks like, notice the nesting:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# to format the 3 lists to be printed as a 3 by 3 grid, each on a new line.
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

# Define the map
line1 = ["⬜️", "⬜️", "⬜️"]
line2 = ["⬜️", "⬜️", "⬜️"]
line3 = ["⬜️", "⬜️", "⬜️"]
map = [line1, line2, line3]

# Display the initial map with labels
print("Treasure Map Layout:")
print("   1     2     3")
print(f"A {line1}")
print(f"B {line2}")
print(f"C {line3}\n")

# Instructions for the user
print("Hiding your treasure! X marks the spot.")
print("Enter the position as a letter (A-C) for the row and a number (1-3) for the column.")
print("For example, 'B3' will place the treasure in row B and column 3.\n")

# User input
position = input("Where do you want to put the treasure? ").strip()

# Process user input
letter = position[0].lower()  # Get the letter (row) and convert to lowercase
abc = ["a", "b", "c"]  # Reference list for row letters
letter_index = abc.index(letter)  # Find the row index
number_index = int(position[1]) - 1  # Convert column number to zero-based index

# Place the treasure
map[letter_index][number_index] = "X"

# Display the updated map with labels
print("\nUpdated Treasure Map Layout:")
print("   1     2     3")
print(f"A {line1}")
print(f"B {line2}")
print(f"C {line3}")
