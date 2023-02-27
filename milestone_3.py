import random
word_list = ['strawberries', 'raspberries', 'apples', 'bananas', 'cherries']
word = random.choice(word_list)

def check_guess(guess):
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry! {guess} is not in the word.")


def ask_for_input():
    while True:
        guess = input('Guess a letter ').lower()
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()