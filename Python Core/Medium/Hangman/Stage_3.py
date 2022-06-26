#  https://hyperskill.org/projects/69/stages/374/implement

import random

print('H A N G M A N')
print('The game will be available soon.')

words_list = ['python', 'java', 'swift', 'javascript']
word = random.choice(words_list)
user_word = input()

print('You survived!' if user_word == word else 'You lost!')
