cells = [i for i in input('Enter cells: ')]
win = 0
x_input = 0
o_input = 0
symb = ''

for i in cells:
    if i == 'X':
        x_input += 1
    elif i == 'O':
        o_input += 1

print('---------')
for i in range(0, len(cells), 3):
    print(f'| {cells[i]} {cells[i+1]} {cells[i+2]} |')
print('---------')

for i in range(0, 9, 3):
    if cells[i] != '_' and cells[i] == cells[i+1] and cells[i+1] == cells[i+2]:
        symb = cells[i]
        win += 1

for i in range(0, 3):
    if cells[i] != '_' and cells[i] == cells[i+3] and cells[i+3] == cells[i+6]:
        symb = cells[i]
        win += 1

if cells[0] != '_' and cells[0] == cells[4] and cells[4] == cells[8]:
    symb = cells[0]
    win += 1
elif cells[2] != '_' and cells[2] == cells[4] and cells[4] == cells[6]:
    symb = cells[2]
    win += 1


if '_' not in cells and win == 0:
    print('Draw')
elif win > 1:
    print('Impossible')
elif x_input - o_input > 1 or o_input - x_input > 1:
    print('Impossible')
elif '_' in cells and win == 0:
    print('Game not finished')
else:
    print(f'{symb} wins')
