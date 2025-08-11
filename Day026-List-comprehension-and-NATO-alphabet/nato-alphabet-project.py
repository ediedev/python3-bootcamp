import pandas as pd

#import data
data = pd.read_csv('NATO_phonetic_alphabet.csv')
#create dictionary comprehension
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#store user input word

def generate_phonetic():
    word =  input('Enter a word: ').upper()
    #create list comprehension
    try:
        word_list = [phonetic_dict[letter] for  letter in word]
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()
    else:
        print(word_list)

generate_phonetic()