#  https://hyperskill.org/projects/208/stages/1043/implement

memory = 0


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
    while True:
        print_msg(4)
        answer = input()

        if answer == 'y':

            if is_one_digit(result):
                msg_index = 10
                msg = ["Are you sure? It is only one digit! (y / n)",
                       "Don't be silly! It's just one number! Add to the memory? (y / n)",
                       "Last chance! Do you really want to embarrass yourself? (y / n)"]

                while True:
                    print(msg[msg_index - 10])
                    ans = input()

                    if ans == 'y':

                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break

                    elif ans == 'n':
                        break
                    else:
                        continue

            else:
                memory = result

            cont_calc()
            break

        elif answer == 'n':
            cont_calc()
            break

        else:
            continue


def cont_calc():
    print_msg(5)
    while True:
        answer = input()
        if answer == 'y':
            main()
            break
        if answer == 'n':
            break


def is_one_digit(number):
    if 10 > number > -10 and number == int(number):
        return True
    else:
        return False


def chek(x, oper, y):
    msg = ''
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"

    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if (x == 1 or y == 1) and oper == '*':
        msg = msg + msg_7
    if (x == 0 or y == 0) and (oper in '*+-'):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg

    print(msg)


def main():
    while True:
        print_msg(0)
        calc = input()

        try:
            check_input(calc)
            chek(x, oper, y)
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
