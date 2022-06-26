import math

print('What do you want to calculate?',
      'type "n" for number of monthly payments,',
      'type "a" for annuity monthly payment amount,',
      'type "p" for loan principal:',
      sep='\n')
calc_type = input()

if calc_type == 'n':
    print('Enter the loan principal:')
    loan_principal = int(input())
    print('Enter the monthly payment:')
    monthly_payment = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())

    i = loan_interest / (12 * 100)
    number_of_months = math.ceil(math.log((monthly_payment / (monthly_payment - i * loan_principal)), 1 + i))
    years_pay = number_of_months // 12
    month_pay = number_of_months % 12

    if years_pay == 0:
        if month_pay == 1:
            print(f'It will take {month_pay} month to repay this loan!')
        else:
            print(f'It will take {month_pay} months to repay this loan!')
    elif month_pay == 0:
        if years_pay == 1:
            print(f'It will take {years_pay} year to repay this loan!')
        else:
            print(f'It will take {years_pay} years to repay this loan!')
    elif years_pay == 0 and month_pay == 0:
        print('You already repay this loan')
    else:
        print(f'It will take {years_pay} years and {month_pay} months to repay this loan!')
elif calc_type == 'a':
    print('Enter the loan principal:')
    loan_principal = int(input())
    print('Enter the number of periods:')
    number_of_periods = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())

    i = loan_interest / (12 * 100)
    monthly_payment = loan_principal * (i * ((1 + i) ** number_of_periods)) / (((1 + i) ** number_of_periods) - 1)

    print(f'Your monthly payment = {math.ceil(monthly_payment)}!')
elif calc_type == 'p':
    print('Enter the annuity payment:')
    annuity_payment = float(input())
    print('Enter the number of periods:')
    number_of_periods = int(input())
    print('Enter the loan interest:')
    loan_interest = float(input())

    i = loan_interest / (12 * 100)
    P = annuity_payment / ((i * (1 + i) ** number_of_periods) / ((1 + i) ** number_of_periods - 1))

    print(math.floor(P))
else:
    print('Wrong type.')
