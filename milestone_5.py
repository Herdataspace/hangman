import random

class Hangman():

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = list(len(self.word)*'_')
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        self.list_visuals = [
            '''
            __________
              |     |
              |     O
              |   \ | /
              |     |
              |    / \ 
            __|________
            ''', '''
            __________
              |     |
              |     O
              |   \ | /
              |     |
              |    
            __|________
            ''', '''
            __________
              |     |
              |     O
              |   \ | /
              |     
              |    
            __|________
            ''', '''
            __________
              |     |
              |     O
              |     | 
              |     
              |    
            __|________
            ''', '''
            __________
              |     |
              |     O
              |   
              |     
              |    
            __|________
            ''']

        print(f'The mistery word has {self.num_letters} characters.', '\n', f'{self.word_guessed}')

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, item in enumerate(self.word):
                if guess == item:
                    self.word_guessed[index] = guess
            print(self.word_guessed)
            self.num_letters -= 1
                
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess.lower()} is not in the word.')
            print(f'You have {self.num_lives} lives left.')
            print(self.list_visuals[self.num_lives])
        
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

word_list = ['strawberries', 'raspberries', 'apples', 'bananas', 'cherries']

def play_game(word_list):
    num_lives = 5

    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}.")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

play_game(word_list)