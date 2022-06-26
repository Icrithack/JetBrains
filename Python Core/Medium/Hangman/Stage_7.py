#  https://hyperskill.org/projects/69/stages/378/implement

import random
import string

word_list = ['python', 'java', 'swift', 'javascript']
word = random.choice(word_list)
attempts = 8
hide_word = list(len(word) * '-')
user_input_letters = []

print('H A N G M A N')

while attempts > 0:
    print()
    print(''.join(hide_word))
    letter = input('Input a letter: ')

    if len(letter) > 1 or len(letter) == 0:
        print('Please, input a single letter.')
    elif letter in list(string.ascii_uppercase) or letter not in list(string.ascii_lowercase):
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

        if ''.join(hide_word) == word:
            print(f'You guessed the word {word}!', 'You survived!', sep='\n')
            exit()

    user_input_letters.append(letter)

print('You lost!')
