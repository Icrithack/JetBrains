from random import randint, choice


def easy_mod():
    right_answer = 0

    for _ in range(5):
        print(string_expression := f'{randint(2, 9)} {choice("+-*")} {randint(2, 9)}')

        while True:
            try:
                if eval(string_expression) == int(input()):
                    print('Right!')
                    right_answer += 1
                else:
                    print('Wrong!')
                break
            except ValueError:
                print('Incorrect format.')

    return right_answer


def medium_mode():
    right_answer = 0

    for _ in range(5):
        print(string_expression := randint(11, 29))

        while True:
            try:
                if string_expression ** 2 == int(input()):
                    print('Right!')
                    right_answer += 1
                else:
                    print('Wrong!')
                break
            except ValueError:
                print('Incorrect format.')

    return right_answer


def save_result(mark, complexity):
    name = input('What is your name?\n')
    if complexity == '1':
        lvl = '1 (simple operations with numbers 2-9)'
    else:
        lvl = '2 (integral squares of 11-29)'

    with open('results.txt', 'a', encoding='utf-8') as test_results:
        test_results.write(f'{name}: {mark}/5 in level {lvl}.\n')

    print('The results are saved in "results.txt".')


def main():
    print('Which level do you want? Enter a number:',
          '1 - simple operations with numbers 2-9',
          '2 - integral squares of 11-29', sep='\n')
    complexity = input()

    if complexity == '1':
        mark = easy_mod()
    elif complexity == '2':
        mark = medium_mode()

    print(f'Your mark is {mark}/5. Would you like to save the result? Enter yes or no.')

    if input() in ('yes', 'YES', 'y', 'Yes'):
        save_result(mark, complexity)


if __name__ == '__main__':
    main()
