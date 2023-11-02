import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

word = input("Enter the word: ").upper()

output_list = [phonetic_dict[character] for character in word]

print(output_list)
