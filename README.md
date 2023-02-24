# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

- GitHub was set-up in this project to track changes to the code and save the changes in the GitHub repo. A GitHub repo was first created, which was then cloned locally using the following terminal command:

```python
""" git clone https://github.com/Herdataspace/hangman.git """
```

## Milestone 2

- Basic Python commands are used to create the variables for the game in a Python file. Each addition to the Python script is commited and pushed to the GitHub repo to save and track the changes. 

- A list of strings of five fruits are asigned to the variable 'word_list'

```python
"""word_list = ['strawberries', 'raspberries', 'apples', 'bananas', 'cherries']
```

- The random.choice method is used to randomly select a word from this list, which is assigned to the variable 'word'.

```python
"""import random
word = random.choice(word_list)
print(word)"""
```

- The input() function is used to ask the user to enter a single letter, which is assigned to the variable 'guess'.

```python
"""guess = input("Enter a single letter")"""
```

- The input is validated using if-else statements, to check the user imput is a only single letter and is alphabetical. 

```python
"""if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')"""
```

