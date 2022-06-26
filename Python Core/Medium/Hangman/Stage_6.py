#  https://hyperskill.org/projects/69/stages/377/implement

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

    if letter in word and letter not in hide_word:
        for i in range(len(word)):
            if word[i] == letter:
                hide_word[i] = letter
    elif letter in hide_word:
        print('No improvements.')
        attempts -= 1
    else:
        print('That letter doesn\'t appear in the word.')
        attempts -= 1

    if ''.join(hide_word) == word:
        print('', word, 'You guessed the word!', 'You survived!', sep='\n')
        exit()

print('You lost!')
