#  https://hyperskill.org/projects/175/stages/904/implement

from random import choice


def calc_value(total_bill, friends_joining):
    if total_bill % friends_joining == 0:
        return total_bill // friends_joining
    else:
        return round(total_bill / friends_joining, 2)


def add_value(dic, pay_value):
    for i in dic:
        dic[i] = pay_value
    return dic


friends_joining = int(input('Enter the number of friends joining (including you):\n'))

if friends_joining > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    party_list = {input(): 0 for _ in range(friends_joining)}
    total_bill = int(input('Enter the total bill value:\n'))
    lucky_man = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if lucky_man == 'Yes':
        lucky = choice(list(party_list.keys()))
        print(f'{lucky} is the lucky one!')
        pay_value = calc_value(total_bill, friends_joining-1)
        add_value(party_list, pay_value)
        party_list[lucky] = 0
        print(party_list)
    elif lucky_man == 'No':
        print('No one is going to be lucky')
        pay_value = calc_value(total_bill, friends_joining)
        add_value(party_list, pay_value)
        print(party_list)

else:
    print('No one is joining for the party')
