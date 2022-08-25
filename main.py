import pandas

phonetic_data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data.iterrows()}


def generate_phonetic():
    names = input("Enter the word: ").upper()
    try:
        list1 = [phonetic_dict[letters] for letters in names]
    except KeyError:
        print("Sorry only letters are allowed!!!")
        generate_phonetic()
    else:
        print(list1)


generate_phonetic()
