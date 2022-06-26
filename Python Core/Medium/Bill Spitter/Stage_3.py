#  https://hyperskill.org/projects/175/stages/904/implement

from random import choice

friends_joining = int(input('Enter the number of friends joining (including you):\n'))

if friends_joining > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    party_list = {input(): 0 for _ in range(friends_joining)}

    total_bill = int(input('Enter the total bill value:\n'))

    lucky_man = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky_man == 'Yes':
        print(f'{choice(list(party_list.keys()))} is the lucky one!')
    elif lucky_man == 'No':
        print('No one is going to be lucky')

    if total_bill % friends_joining == 0:
        pay_value = total_bill // friends_joining
    else:
        pay_value = round(total_bill / friends_joining, 2)

    for i in party_list:
        party_list[i] = pay_value


else:
    print('No one is joining for the party')
