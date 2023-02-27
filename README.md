# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

- GitHub was set-up in this project to track changes to the code and save the changes in the GitHub repo. A GitHub repo was first created, which was then cloned locally using the following terminal command:

```python
git clone https://github.com/Herdataspace/hangman.git
```

## Milestone 2

- Basic Python commands are used to create the variables for the game in a Python file. Each addition to the Python script is commited and pushed to the GitHub repo to save and track the changes. 

- A list of strings of five fruits are asigned to the variable 'word_list'

```python
word_list = ['strawberries', 'raspberries', 'apples', 'bananas', 'cherries']
```

- The random.choice method is used to randomly select a word from this list, which is assigned to the variable 'word'.

```python
import random
word = random.choice(word_list)
print(word)
```

- The input() function is used to ask the user to enter a single letter, which is assigned to the variable 'guess'.

```python
guess = input("Enter a single letter")
```

- The input is validated using if-else statements, to check the user imput is a only single letter and is alphabetical. 

```python
   if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')
```

## Milestone 3

- Following on from the previous milestone, a **while loop** is created to iteratively check if the input is a valid guess. The code will run until a valid guess (single letter) is inputted.

```python
while True:
        guess = input('Guess a letter ').lower()
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
```

- Another check is then created to check if the letter guessed is in the secret word, using **if-else statements**.  

```python
if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry! {guess} is not in the word.")
```

- Functions help to organise the code to better understand which blocks of code do what. The code written is added into two functions:

```python
def check_guess(guess):
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry! {guess} is not in the word.")
```

``` python
def ask_for_input():
    while True:
        guess = input('Guess a letter ').lower()
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()
```

- The **check_guess** function is called in the **ask_for_input** function, with the **guess** variable as the argument. The **ask_for_input** function is then called outside both functions, which in turn, will run both functions. This checks the guess as a valid input, and checks whether the guess is in the word. 




