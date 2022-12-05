#Define the __init__method of the hangman class
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list=word_list
        self.word=random.choice(word_list)
        self.num_lives=num_lives
        self.word_guessed=list('_' * len(self.word)) 
        self.unguessed_letters=len(set(list(self.word)))
        self.list_letters=[]
        
        print (f"The mystery word has {len(self.word)} characters")
        print (f'{self.word_guessed}')
    
    def ask_letter(self):
        letter=input('Please enter a character:')
        if letter.isalpha()!=True and len(letter)!=1:
                print("Invalid letter. Please, enter a single alphabetical character.")
        elif letter in self.list_letters:
                print(f"You already tried the letter {letter}!")
        else:
                self.check_letter(letter)
    
    def check_letter(self, letter) -> None:
        letter=letter.lower()
        if letter in self.word:
            print(f"Good guess! {letter} is in the word.")
            for index, char in enumerate(self.word):
                if char == letter:
                    self.word_guessed[index] = letter
            print(self.word_guessed)
            self.unguessed_letters-=1
        else:
            self.num_lives-=1
            print(f'Sorry {letter} is not in the word.')
            print(f"You have {self.num_lives} lives left.")
            
        self.list_letters.append(letter)
      
    
def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives==0:
            print(f'You lost! The correct word is {game.word}')
            break
        elif game.unguessed_letters>0:
            game.ask_letter()
        else:
            print('Congratulations, you have won the game')
            break

if __name__== '__main__':
    word_list=['apple', 'banana', 'orange', 'mango', 'grapes']
    play_game(word_list)

    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"

    
 
    
 

  
