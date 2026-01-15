from base64 import encode

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     encryption_output = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         encryption_output += alphabet[shifted_position]
#     print(f"Here is the encoded result: {encryption_output}")
#
# def decrypt(original_text, shift_amount):
#     decryption_output = ""
#
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         decryption_output += alphabet[shifted_position]
#     print(f"Here is the encoded result: {decryption_output}")
#
# def caesar(choice):
#     if choice == "encode":
#         encrypt(original_text=text, shift_amount=shift)
#     elif choice == "decode":
#         decrypt(original_text=text, shift_amount=shift)
#     else:
#         print("Invalid input")
#
# caesar(choice=direction)

# ******************** ALTERNATE **********************

def caesar(original_text, shift_amount, choice):
    output = ""
    for letter in original_text:
        if choice == "encode":
            shifted_position = alphabet.index(letter) + shift_amount
            output += alphabet[shifted_position]
        elif choice == "decode":
            shifted_position = alphabet.index(letter) - shift_amount
            output += alphabet[shifted_position]
    print(f"Here is the {choice}d result: {output}")

caesar(original_text=text, shift_amount=shift, choice=direction)