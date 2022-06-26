plr = ('Jack', 'John')
pencils = int(input('How many pencils would you like to use:\n'))
i = bool(plr.index(input(f'Who will be the first ({plr[0]}, {plr[1]}):\n')))

while pencils > 0:
    print('|' * pencils)
    print(f"{plr[i]}'s turn:")

    pencils -= int(input())
    i = not i
