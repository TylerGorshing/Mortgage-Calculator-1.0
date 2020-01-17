# A program to calculate mortgage stuff.

print('What is the loan amount?')
loan_ammount = float(input())

print('What is the interest rate?')
interest_rate = float(input()) / 100

print('What is the loan term in years?')
loan_term = int(input())

print('How many payments will you make each month?')
yearly_payments = int(input()) * 12

print('How much extra money will you pay each month?')
extra_payment = float(input())

monthly_interest_rate = interest_rate / yearly_payments
total_payment_number = loan_term * yearly_payments

monthly_payment = loan_ammount * ((interest_rate / yearly_payments) / (
    1 - (1 + interest_rate / yearly_payments)**(-1 * yearly_payments * loan_term)))
total_payment_ammount = monthly_payment * total_payment_number
expected_total_interest = total_payment_ammount - loan_ammount
monthly_payment += extra_payment

remaining_principle = loan_ammount
to_principle = 0.0
to_interest = 0.0
month_interest = 0.0
total_interest = 0.0

with open('payment.txt', 'w') as file:
    file.write(f'Your monthly payment is {monthly_payment}. \n')
    file.write(
        f'Over {total_payment_number} months, you will pay ${total_payment_ammount}. \n \n \n')

    if extra_payment == 0:
        for payment in range(1, total_payment_number + 1):
            month_interest = remaining_principle * monthly_interest_rate
            total_interest += month_interest
            to_principle = monthly_payment - month_interest
            remaining_principle += -1 * to_principle

            file.write(
                f'For payment {payment}, ${month_interest} goes to interest and ${to_principle} goes to principle. \n')
            file.write(
                f'  The remaining principle is ${remaining_principle} \n')
            file.write(
                f'  A total of ${total_interest} has gone to interest over the life of the loan.\n \n')

    else:
        payment = 0

        while remaining_principle > monthly_payment:
            month_interest = remaining_principle * monthly_interest_rate
            total_interest += month_interest
            to_principle = monthly_payment - month_interest
            remaining_principle += -1 * to_principle
            payment += 1

            file.write(
                f'For payment {payment}, ${month_interest} goes to interest and ${to_principle} goes to principle. \n')
            file.write(
                f'  The remaining principle is ${remaining_principle} \n')
            file.write(
                f'  A total of ${total_interest} has gone to interest over the life of the loan.\n \n')

        month_interest = remaining_principle * monthly_interest_rate
        last_payment = remaining_principle + month_interest
        total_interest += month_interest
        interest_saved = expected_total_interest - total_interest

        file.write(
            f'Your last payment will be ${last_payment} after {payment} payments. \n')
        file.write(
            f'  A total of ${total_interest} has gone to interest over the life of the loan.\n')
        file.write(
            f'  You have saved ${interest_saved} by paying an additional ${extra_payment} per payment.')
