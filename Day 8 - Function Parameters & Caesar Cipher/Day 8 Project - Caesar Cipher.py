# Sahad Rafiuzzaman
# 12/31/2023
# Caesar Cipher Part 4 - User Experience Improvements & Final Touches

from caesar_cipher_art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Original functions encrypt() and decrypt() was combined to make caesar()
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position > 25:
                new_position -= 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"\nThe {cipher_direction}d result: {end_text}")

# Using a while loop to ask the user if they want to continue encoding/ decoding

should_continue = True
while should_continue:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("\nType your message:\n").lower()
    shift = int(input("\nType the shift number:\n"))

    # If the user entered a shift amount larger than the range, it will size down using modulus
    if shift > 26:
        shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    continue_cipher = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n")
    if continue_cipher == "no":
        should_continue = False
        print("\nGoodbye!")

