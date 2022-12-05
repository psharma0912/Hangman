#iteratively check if the input from user is a valid guess
import random

# word_list=['apple', 'banana', 'orange', 'mango', 'grapes']
# word=random.choice(word_list)
# print(word)
word='banana'

def check_guess(guess):
    guess=guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word {word}.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")   

def ask_for_input():
    while True:
        #guess=input('Enter a character from the user:')
        guess='n'
        if guess.isalpha()==True and len(guess)==1:
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    
    check_guess(guess)
    
ask_for_input()
#%%Classes: Lets say I work for a comapny and we are trying to keep ttrack of all the information about employees in my
#company. So we can use class concept here
class Employee:
    num_of_employees=0
    pay_rise=1.04

    def __init__(self, first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+ '.'+ last+'@gmail.com'

        Employee.num_of_employees+=1

    def fullname(self):
        return (f'{self.first} {self.last}')
    
    def apply_raise(self):
        self.pay= int(self.pay* self.pay_rise)
 
print(Employee.num_of_employees)
#emp1 and emp2 are the instances of the class
emp1=Employee('Poonam','Sharma',10000)
emp2=Employee('Nitin','Vyas', 20000)

print(Employee.num_of_employees)

    
print(emp1.first, emp1.last, emp1.pay, emp1.email)
print(emp2.first, emp2.last, emp2.pay, emp2.email)

print(emp1.fullname())
print(Employee.fullname(emp2))

print(emp2.pay)
emp2.apply_raise()
print(emp2.pay)

# # print(Employee.__dict__)
# print(emp1.__dict__)
# %%
word='apple'
word_guessed=list('_' * len(word))
print(word_guessed)
letter='p'

num_letters=len(set(list(word)))
print(f'Number of letters: {num_letters}')

enumerate(word)
if letter in word:
        print(f"Good guess! {letter} is in the word {word}.")
        for index, char in enumerate(word):
            if char == letter:
                print(index)
                word_guessed[index]=letter
                print(word_guessed)
                
        #         word_guessed[index] = letter
        num_letters=num_letters-1
        print(num_letters)
    

# %%This piece of code creates a class, where we define the init method for the class.
#The random.choice mmthod chooses a random word from the list and initialise the attributes
#of the class.
import random
word_list=['apple', 'banana', 'orange', 'mango', 'grapes']
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list=word_list
        self.word=random.choice(word_list)
        self.num_lives=num_lives
        self.word_guessed=list('_' * len(self.word)) 
        self.unguessed_letters=len(set(list(self.word)))
        self.list_letters=[]

        print (f"The mystery word is {self.word} and has {len(self.word)} characters")
        print (f'{self.word_guessed}')
        print()
        print (f'The unguessed letters are :{self.unguessed_letters}')
    
    def ask_letter(self):
        #while True:
            letter=input('Please enter a character:')
            if letter.isalpha()!=True and len(letter)!=1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif letter in self.list_letters:
                    print(f"You already tried the letter {letter}!")
            else:
                    self.check_letter(letter)
    
    # def check_letter(self, letter) -> None:
    #     letter=letter.lower()

    #     if letter in self.word:
    #         print(f"Good guess! {letter} is in the word {self.word}.")
    #     else:
    #         print(f"Sorry, {letter} is not in the word. Try again.")   
    def check_letter(self, letter) -> None:
        letter=letter.lower()

        if letter in self.word:
            print(f"Good guess! {letter} is in the word {self.word}.")
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
    game=Hangman(word_list, num_lives=5)
    while True:
        if game.num_lives==0:
            print('You lost!')
            break
        elif game.num_lives>0:
            game.ask_letter()
        else:
            print('You have won!')

play_game(word_list)



# %%
word='apple'
letter='l'
letter=letter.lower()
list_letters=[]
num_lives=5
unguessed_letters=len(set(list(word)))
word_guessed=list('_' * len(word)) 

if letter in word:
    print(f"Good guess! {letter} is in the word {word}.")
    for index, char in enumerate(word):
        print(index,char)
        if char == letter:
            word_guessed[index] = letter
            print(word_guessed)
    unguessed_letters-=1
else:
    num_lives-=1
    print(f'Sorry {letter} is not in the word.')
    print(f"You have {num_lives} lives left.")
    list_letters.append(letter)
    print(list_letters)


# %%

# %%
