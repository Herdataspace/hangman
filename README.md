# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

<br>

## Milestone 1

- GitHub was set-up in this project to track changes to the code and save the changes in the GitHub repo. A GitHub repo was first created, which was then cloned locally using the following terminal command:

```python
git clone https://github.com/Herdataspace/hangman.git
```

<br>

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

<br>

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

<br>

## Milestone 4

- Classes are a standard feature of 'object oriented programming', which bundle data and functionality together. Using the functions created in milestone 3, a Hangman class is defined which is first initialised with attributes of the class. 

```python
class Hangman():

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = list(len(self.word)*'_')
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
```

- Atrributes include variables defined in previous milestones, as well as:

    - **num_lives** = The number of lives the player has at the start of the game, default 5.
    - **word_guessed** = A list of the letters in the word, with ' _ ' in place of each letter not yet guessed. When a correct letter is guessed, the ' _ ' in the corresponding position is replaced with the correct letter. 
    - **num_letters** = The number of unique letters in the word that have not been guessed yet.
    - **list_of_guesses** = A list of the guesses that have already been tried. Initially set to an empty list.


<br>

- 2 methods are defined: **ask_for_input** asks the user to guess a letter, and **check_guess** checks if this guess is in the randomly selected word. 

- Passing 'self' into these methods as a parameter, passes an instance of the Hangman class into the methods.


- Additional **If-else statements** are added to the **ask_for_input** method, to check if the guessed letter is in the word, using the **list_of_guesses** attribute, initialised in the Hangman class. If it is not, this guess is appended to the list. 


```python
    def ask_for_input(self):
        while True:
            guess = input('Guess a letter ')
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
```

<br>

- A **for-loop** is added to the **check_guess** method, to add the correctly guessed letter to the **word_guessed** attribute, replacing the underscore at the appropriate index.  

```python
for index, item in enumerate(self.word):
                if guess.lower() == item:
                    self.word_guessed[index] = guess.lower()
```

- The num_letters variable is then reduced by 1. 

```python
self.num_letters -= 1 
```

- An **else-block** is added for if there is an incorrect guess, which reduces the num_lives variable by one and prints corresponding messages. 

```python
else:
            self.num_lives -= 1
            print(f'Sorry, {guess.lower()} is not in the word.')
            print(f' You have {self.num_lives} lives left.')
```

<br>