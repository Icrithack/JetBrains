from random import randint, choice

count = 0

for _ in range(5):
    print(string_expression := f'{randint(2, 9)} {choice("+-*")} {randint(2, 9)}')

    while True:
        try:
            if eval(string_expression) == int(input()):
                print('Right!')
                count += 1
            else:
                print('Wrong!')
            break
        except ValueError:
            print('Incorrect format.')

print(f'Your mark is {count}/5.')
