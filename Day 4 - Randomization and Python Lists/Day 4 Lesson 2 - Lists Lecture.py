# Sahad Rafiuzzaman
# 12/25/2023
# Understanding the Offset and Appending Items to Lists

states_of_america = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland',
                     'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island',
                     'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois',
                     'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin',
                     'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado',
                     'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma',
                     'New Mexico', 'Arizona', 'Alaska', 'Hawaii']

# First Index
print(states_of_america[0])

# Negative Index
print(states_of_america[-1])

# Altering items in the List
states_of_america[1] = 'Pencilvania'

# Appending Items to the List (Adds items to the end of the list)
states_of_america.append("Angelaland")
print(states_of_america)