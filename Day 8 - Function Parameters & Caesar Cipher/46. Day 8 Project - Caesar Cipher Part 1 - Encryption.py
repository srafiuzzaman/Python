# Sahad Rafiuzzaman
# Date: 01/04/2025

# Caesar Cipher Part 1 - Encryption

# You are going to build an encryption and decryption program using the Caesar cipher.

# Demo
# https://appbrewery.github.io/python-day8-demo/


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the original_text forwards in the alphabet by the
#  shift_amount and print the encrypted text.

# You can use the built-in Python index() function to find out the position of an item in a list. e.g.
""" 
fruits = ["Apple", "Pear", "Orange"]
fruits.index("Pear") # 1

# e.g.
plain_text = "hello"
shift_amount = 1
"""

# The final encrypted output should be:
"""
Here is the encoded result: ifmmp
"""

# Where each of the letters of 'hello' is shifted up by 1.
# Hint: Lets breakdown the problem:
# 1. You need a for loop to loop through each of the letters in the plain_text.
# 2. Find the position of each letter in the alphabet List
# 3. Add the user desired shift_amount to the position to get the position of the encoded letter.
# 4. Find the corresponding letter for that position.
# 5. Add each encoded letter to a new string and print it out after the loop ends.

# # hello 2
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount    # 7 + 9
#         cipher_text += alphabet[shifted_position]                   # j
#     print(f"Here is the encoded result: {cipher_text}")


# TODO-3: Call the encrypt() function and pass in the user inputs.
#  You should be able to test the code and encrypt a message.
# encrypt(original_text=text, shift_amount=shift)

# TODO-4: What happens if you try to shift the letter 'z' forwards by 9? Can you fix the code?
# Hint: There are many approaches to do this.
# 1. You can add more than 1 set of the alphabet into the List of alphabet letters.
# 2. You can shift the shift_amount so that it is always within 0 - 25 and fits in the List.
# 3. You can use the modulo to get the remainder.

# hello 2
def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount    # 7 + 9
        shifted_position %= len(alphabet)                           # 0-25
        cipher_text += alphabet[shifted_position]                   # j
    print(f"Here is the encoded result: {cipher_text}")


encrypt(original_text=text, shift_amount=shift)