import pandas as pd

#import data
data = pd.read_csv('NATO_phonetic_alphabet.csv')
#create dictionary comprehension
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#store user input word
word =  input('Enter a word: ').upper()
#create list comprehension
word_list = [phonetic_dict[letter] for  letter in word]
print(word_list)