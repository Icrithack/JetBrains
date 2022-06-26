#  https://hyperskill.org/projects/208/stages/1039/implement

def print_msg(a):
    if a == 0:
        print('Enter an equation')
    elif a == 1:
        print('Do you even know what numbers are? Stay focused!')
    else:
        print('Yes ... an interesting math operation. You\'ve slept through all classes, haven\'t you?')


def split_calc(calc):
    global oper
    x, oper, y = map(str, calc.split())
    try:
        x = int(x)
    except Exception:
        x = float(x)
    try:
        y = int(y)
    except Exception:
        y = float(y)


def chek_oper(oper):
    if oper == '+' or oper == '-' or oper == '*' or oper == '/':
        return True
    else:
        return False


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
                break
            else:
                print_msg(2)
                continue


main()
