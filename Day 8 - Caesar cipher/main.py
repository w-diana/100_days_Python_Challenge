from art import logo

# Print the logo at the start
print(logo)
restart = "yes"

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(text, shift, direction):
    message = ""
    for letter in text:
        # In case the user enters numbers/symbols/spaces
        if letter not in alphabet:
            message += letter

        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                if direction == "encode":
                    # Shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
                    new_location = i + shift
                    # Take care of end case e.g. civilization
                    while new_location > 25:
                        new_location = new_location - 26
                elif direction == "decode":
                    # Shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
                    new_location = i - shift
                    # Take care of end case e.g. civilization
                    if new_location < 0:
                        new_location = new_location + 26
                message = message + alphabet[new_location]

    print(f"The {direction} text is {message}")


while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Call the caesar() function and pass in the use inputs
    caesar(text, shift, direction)
    restart = input(
        "Do you want to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no'. \n"
    ).lower()
    if restart == "no":
        print("Goodbye")
