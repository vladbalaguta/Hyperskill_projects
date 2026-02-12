# Write your code here
import random

class Hangman:
    def __init__(self):
        self.assume_letter = None
        self.hidden_word = None
        self.attempts = None
        self.win_counter = 0
        self.lose_counter = 0
        self.words_catalog = {'python', 'java', 'swift', 'javascript'}
        self.random_word = None
        self.guessed_letters = None

    def assign_letter(self):
        counter = 0
        self.hidden_word = list(self.hidden_word)
        if self.assume_letter in list(self.random_word):
            for letter in list(self.random_word):
                if letter == self.assume_letter:
                    if self.hidden_word[counter] == self.assume_letter:
                        print("You've already guessed this letter.")
                        break
                    else:
                        self.hidden_word[counter] = self.assume_letter
                        counter += 1
                else:
                    counter += 1
        else:
            print("That letter doesn't appear in the word.")
            self.attempts -= 1
        self.visualize_game()

    def input_conditions(self):
        if len(self.assume_letter) != 1:
            print('Please, input a single letter.')
            self.visualize_game()

        elif self.assume_letter.isupper() or not self.assume_letter.isalpha():
            print('Please, enter a lowercase letter from the English alphabet.')
            self.visualize_game()

        elif self.assume_letter in self.guessed_letters:
            print("You've already guessed this letter.")
            self.visualize_game()

        else:
            self.guessed_letters.append(self.assume_letter)
            self.assign_letter()

    def visualize_game(self):
        self.hidden_word = ''.join(self.hidden_word)
        print(f'\n{self.hidden_word}')
        if '-' not in self.hidden_word:
            print(f'You guessed the word {self.hidden_word}!\nYou survived!')
            self.win_counter += 1
            return
        if self.attempts == 0:
            print('\nYou lost!')
            self.lose_counter += 1
            return
        self.assume_letter = input(f'Input a letter:')
        self.input_conditions()

    def start_menu(self):
        while True:
            self.guessed_letters = []
            self.attempts = 8
            start = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:').lower()
            if start == 'play':
                self.random_word = random.choice(list(self.words_catalog))
                self.hidden_word = ['-' for i in self.random_word]
                self.visualize_game()
            elif start == 'results':
                print(f'You won: {self.win_counter} times.')
                print(f'You lost: {self.lose_counter} times.')
            elif start == 'exit':
                break
            else:
                pass





print('H A N G M A N')
initialization = Hangman()
initialization.start_menu()