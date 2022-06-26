#  https://hyperskill.org/projects/175/stages/901/implement

friends_joining = int(input('Enter the number of friends joining (including you):\n'))

if friends_joining < 1:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    party_list = {input(): 0 for _ in range(friends_joining)}

    print(party_list)
