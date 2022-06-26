#  https://hyperskill.org/projects/208/stages/1040/implement

def print_msg(type):
    if type == 0:
        print('Enter an equation')
    elif type == 1:
        print('Do you even know what numbers are? Stay focused!')
    elif type == 2:
        print('Yes ... an interesting math operation. You\'ve slept through all classes, haven\'t you?')
    else:
        print('Yeah... division by zero. Smart move...')


def split_calc(calc):
    global x, oper, y
    x, oper, y = map(str, calc.split())
    try:
        x = int(x)
    except ValueError:
        x = float(x)
    try:
        y = int(y)
    except ValueError:
        y = float(y)


def chek_oper(oper):
    if oper == '+' or oper == '-' or oper == '*' or oper == '/':
        return True
    else:
        return False


def show_result(x, oper, y):
    if oper == '+':
        print(float(x + y))
    elif oper == '-':
        print(float(x - y))
    elif oper == '*':
        print(float(x * y))
    elif oper == '/':
        print(float(x / y))



def main():
    while True:
        print_msg(0)
        calc = input()

        try:
            split_calc(calc)
        except ValueError:
            print_msg(1)
            continue
        else:
            if chek_oper(oper):
                if y == 0:
                    print_msg(3)
                    continue
                else:
                    show_result(x, oper, y)
                    break
            else:
                print_msg(2)
                continue


main()
