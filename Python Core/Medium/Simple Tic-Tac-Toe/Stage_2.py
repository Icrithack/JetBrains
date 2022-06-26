cells = input('Enter cells: ')

print('---------')
for i in range(0, len(cells), 3):
    print(f'| {cells[i]} {cells[i + 1]} {cells[i + 2]} |')
print('---------')
