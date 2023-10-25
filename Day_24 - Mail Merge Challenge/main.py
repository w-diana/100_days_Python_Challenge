# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

with open("./Input/Names/invited_names.txt") as invited_names:
    invited_names = invited_names.readlines()

for name in invited_names:
    new_letter = letter.replace(PLACEHOLDER, name.strip())
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter_to_save:
        letter_to_save.write(new_letter)


