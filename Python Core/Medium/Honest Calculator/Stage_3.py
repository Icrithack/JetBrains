#  https://hyperskill.org/projects/208/stages/1041/implement

def print_msg(num):
    if num == 0:
        print('Enter an equation')
    elif num == 1:
        print('Do you even know what numbers are? Stay focused!')
    elif num == 2:
        print('Yes ... an interesting math operation. You\'ve slept through all classes, haven\'t you?')
    elif num == 3:
        print('Yeah... division by zero. Smart move...')
    elif num == 4:
        print('Do you want to store the result? (y / n):')
    elif num == 5:
        print('Do you want to continue calculations? (y / n):')


def check_input(calc):
    global x, oper, y
    x, oper, y = map(str, calc.split())
    if x == 'M':
        x = memory
    else:
        x = float(x)

    if y == 'M':
        y = memory
    else:
        y = float(y)


def chek_oper(oper):
    if oper == '+' or oper == '-' or oper == '*' or oper == '/':
        return True
    else:
        return False


def calc_result(x, oper, y):
    global result
    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/':
        result = x / y
    print(result)
    store_result()


def store_result():
    global memory
    print_msg(4)
    while True:
        answer = input()
        if answer == 'y':
            memory = result
            cont_calc()
            break
        if answer == 'n':
            memory = 0
            cont_calc()
            break


def cont_calc():
    print_msg(5)
    while True:
        answer = input()
        if answer == 'y':
            main()
            break
        if answer == 'n':
            break


def main():
    while True:
        print_msg(0)
        calc = input()

        try:
            check_input(calc)
        except ValueError:
            print_msg(1)
            continue
        else:
            if chek_oper(oper):

                try:
                    calc_result(x, oper, y)
                    break
                except ZeroDivisionError:
                    print_msg(3)
                    continue

            else:
                print_msg(2)
                continue


main()
