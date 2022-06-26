def pen():
    print('How many pencils would you like to use:')

    while True:
        pencils = input()
        if pencils.isdigit():
            pencils = int(pencils)
            if pencils <= 0:
                print('The number of pencils should be positive')
            else:
                return pencils
        else:
            print('The number of pencils should be numeric')
            continue


def who_first(plr):
    print(f'Who will be the first ({plr[0]}, {plr[1]}):')

    while True:
        first = input()

        if first not in plr:
            print(f"Choose between '{plr[0]}' and '{plr[1]}'")
            continue
        break

    return first


def get_num():
    global pencils

    while True:
        num = input()
        if num not in ('1', '2', '3'):
            print("Possible values: '1', '2' or '3'")
            continue
        elif int(num) > pencils:
            print('Too many pencils were taken')
            continue
        else:
            pencils -= int(num)
            break


def bot_logic():
    global pencils
    num = 1

    if pencils % 4 == 0:
        num = 3
    elif pencils % 4 == 3:
        num = 2

    print(num)
    pencils -= num


plr = ('John', 'Jack')
pencils = pen()
i = bool(plr.index(who_first(plr)))

while pencils > 0:
    print('|' * pencils)
    print(f"{plr[i]}'s turn:")

    if plr[i] == 'John':
        get_num()
    else:
        bot_logic()
    i = not i

print(f'{plr[i]} won!')
