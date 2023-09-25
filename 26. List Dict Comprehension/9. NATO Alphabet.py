import pandas
csv_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in csv_data.iterrows()}

user_word = input("Enter a word: ").upper()

nato_code = [nato_alphabet[letter] for letter in user_word]

print(nato_code)
