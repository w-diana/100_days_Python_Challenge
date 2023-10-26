import pandas
nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_alphabets_dict = {row.letter: row.code for (index,row) in nato_alphabets.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Type a word: ").upper()
result = [nato_alphabets_dict[char] for char in user_input]
print(result)