# Sahad Rafiuzzaman
# Date: 12/28/2023
# While Loops

number_of_hurdles = 6
while number_of_hurdles > 0:
    print("Jump")
    number_of_hurdles -= 1
    print(number_of_hurdles)

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
import random


at_goal = random.randint(1,10)
while not at_goal == 0:
    at_goal -= 1
    print("Jump")

