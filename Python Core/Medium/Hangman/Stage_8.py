#  https://hyperskill.org/projects/69/stages/379/implement

import random
import string

win_games = 0
lose_games = 0

print('H A N G M A N')

while True:
    menu = input('''Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ''')

    if menu == 'play':

        word_list = ['python', 'java', 'swift', 'javascript']
        word = random.choice(word_list)
        attempts = 8
        hide_word = list(len(word) * '-')
        user_input_letters = []

        while attempts > 0:
            print()
            print(''.join(hide_word))
            letter = input('Input a letter: ')

            if len(letter) > 1 or len(letter) == 0:
                print('Please, input a single letter.')
            elif letter in list(string.ascii_uppercase):
                print('Please, enter a lowercase letter from the English alphabet.')
            elif letter not in list(string.ascii_lowercase):
                print('Please, enter a lowercase letter from the English alphabet.')
            elif letter in user_input_letters:
                print('You\'ve already guessed this letter.')
            else:

                if letter in word and letter not in hide_word:
                    for i in range(len(word)):
                        if word[i] == letter:
                            hide_word[i] = letter
                else:
                    print('That letter doesn\'t appear in the word.')
                    attempts -= 1

            user_input_letters.append(letter)

            if ''.join(hide_word) == word:
                print(f'You guessed the word {word}!', 'You survived!', sep='\n')
                win_games += 1
                break
            elif attempts <= 0:
                print('You lost!')
                lose_games += 1
                break

    elif menu == 'results':
        print(f'You won: {win_games} times')
        print(f'You lost: {lose_games} times')
    elif menu == 'exit':
        exit()
    else:
        menu = input('''Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ''')
