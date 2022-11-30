#Define the __init__method of the hangman class
import random

word_list=['apple', 'banana', 'orange', 'mango', 'grapes']
word=random.choice(word_list)
print(word) 

word_guessed=['_']
num_letters=0
list_of_guesses=[]


class Hangman:
    def __init__(self, word, num_lives=5):
        self.word=word
        self.num_lives=num_lives
        self.word_guessed=word_guessed
        self.num_letters=num_letters
        self.list_of_guesses=list_of_guesses
