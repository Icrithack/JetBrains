import math

print('Enter the loan principal:')
current_sum = int(input())
print('What do you want to calculate?')
print('type "m" for number of monthly payments,')
print('type "p" for the monthly payment:')
calc_type = input()

if calc_type == 'm':
    print('Enter the monthly payment:')
    monthly_payment = int(input())
    months_to_repay = math.ceil(current_sum / monthly_payment)
    if months_to_repay <= 1:
        print('It will take', months_to_repay, 'month to repay the loan')
    else:
        print('It will take', months_to_repay, 'months to repay the loan')
elif calc_type == 'p':
    print('Enter the number of months:')
    number_of_months = int(input())
    if current_sum % number_of_months == 0:
        monthly_payment = current_sum // number_of_months
        print('Your monthly payment =', monthly_payment)
    else:
        monthly_payment = math.ceil(current_sum / number_of_months)
        last_payment = current_sum - (number_of_months - 1) * monthly_payment
        print('Your monthly payment =', monthly_payment, 'and the last payment =', last_payment, '.')
else:
    print('Wrong type to calculate')
