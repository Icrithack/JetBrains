from random import randint, choice

rand_sep = choice(['+', '-', '*'])
first_int = randint(2, 9)
second_int = randint(2, 9)

print(string_expression := f'{first_int} {rand_sep} {second_int}')
print('Right!' if eval(string_expression) == int(input()) else 'Wrong!')
