#  https://hyperskill.org/projects/69/stages/375/implement

import random

print('H A N G M A N')

words_list = ['python', 'java', 'swift', 'javascript']
word = random.choice(words_list)
hints = word[:3] + '-' * (len(word) - 3)
user_word = input(f'Guess the word {hints} ')

print('You survived!' if user_word == word else 'You lost!')
