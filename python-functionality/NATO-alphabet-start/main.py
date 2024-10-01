

import pandas
data = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.word for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def userinput():
    user_word = input("whats your word \ned@")
    try:
        phonetic = [ phonetic_dict[letter.upper()] for letter in user_word ]
        print (phonetic)
    except KeyError:
        print("You've not entered a valid word please try again")
        userinput()

userinput()