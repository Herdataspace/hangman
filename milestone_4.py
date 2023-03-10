import random
word_list = ['strawberries', 'raspberries', 'apples', 'bananas', 'cherries']
# word = random.choice(word_list)

# def check_guess(guess):
#     if guess in word:
#         print(f"Good guess! {guess} is in the word.")
#     else:
#         print(f"Sorry! {guess} is not in the word.")


# def ask_for_input():
#     while True:
#         guess = input('Guess a letter ').lower()
#         if guess.isalpha() and len(guess) == 1:
#             break
#         else:
#             print("Invalid letter. Please, enter a single alphabetical character.")
#     check_guess(guess)

# ask_for_input()

class Hangman():

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = list(len(self.word)*'_')
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess.lower() in self.word:
            print(f"Good guess! {guess.lower()} is in the word.")
            for index, item in enumerate(self.word):
                if guess.lower() == item:
                    self.word_guessed[index] = guess.lower()
            self.num_letters -= 1    
                
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess.lower()} is not in the word.')
            print(f' You have {self.num_lives} lives left.')
        

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

test = Hangman(word_list)
test.ask_for_input()
