while True:
    guess = input('Guess a letter ')
    if guess.isalpha() and len(guess) == 1:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

import random
word_list = ['strawberries', 'raspberries', 'apples', 'bananas', 'cherries']
word = random.choice(word_list)

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry! {guess} is not in the word.")


