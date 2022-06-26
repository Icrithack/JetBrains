#  https://hyperskill.org/projects/175/stages/902/implement

friends_joining = int(input('Enter the number of friends joining (including you):\n'))

if friends_joining > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    party_list = {input(): 0 for _ in range(friends_joining)}

    total_bill = int(input('Enter the total bill value:\n'))
    if total_bill % friends_joining == 0:
        pay_value = total_bill // friends_joining
    else:
        pay_value = round(total_bill / friends_joining, 2)

    for i in party_list:
        party_list[i] = pay_value

    print(party_list)
else:
    print('No one is joining for the party')
