#  https://hyperskill.org/projects/69/stages/376/implement

import random
word_list = ['python', 'java', 'swift', 'javascript']
word = random.choice(word_list)
attempts = 8
hide_word = list(len(word) * '-')
print('H A N G M A N')

while attempts > 0:
    print()
    print(''.join(hide_word))
    letter = input('Input a letter: ')
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                hide_word[i] = letter
    else:
        print('That letter doesn\'t appear in the word.')
    attempts -= 1

print('Thanks for playing!')
