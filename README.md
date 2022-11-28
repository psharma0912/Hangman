# Hangman

> Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Create the variables for the game

The random module is one of Python's built-in modules. It has a choice method which returns a random item from a given sequence. A word_list is defined and is passed to the random.choice method. This is assigned to 'word' which prints out the different words each time the code is run.
  
The next part of code takes a user input as a single character and does some validity checks to ensure that the character entered is an alphabet and the length of character is 1. This is doen using the if else statement.
```python
"""import random

word_list=['apple', 'banana', 'orange', 'mango', 'grapes']
print(word_list)

word=random.choice(word_list)
print(word)

guess=input('Enter a single letter:')
if guess.isalpha()==True and len(guess)==1:
    print('Good guess!')
else: 
    print("Oops! That is not a valid input.")"""
```

## Check if the guessed character is in the word

- Does what you have built in this milestone connect to the previous one? If so explain how. What technologies are used? Why have you used them? Have you run any commands in the terminal? If so insert them using backticks (To get syntax highlighting for code snippets add the language after the first backticks).

- Example below:

```bash
/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
```

- The above command is used to check whether the topic has been created successfully, once confirmed the API script is edited to send data to the created kafka topic. The docker container has an attached volume which allows editing of files to persist on the container. The result of this is below:

```python
"""Insert your code here"""
```

> Insert screenshot of what you have built working.

## Milestone n

- Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

- Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?