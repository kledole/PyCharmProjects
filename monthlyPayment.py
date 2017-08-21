# File: monthlyPayment.py
# Description: Simple program that will:
# prompt the user for the cost of the loan,
#    - interest rate
#    - number of years for the loan

# End of session 3:14:11 - Lunch break...

# Result of calculation (below) will provide the
# number of payments:
#
#  monthly_payments = L * [i(1+i)n] / [(1+i)n-1]

# Vars:
#   monthly_payment (M)
#   loan_amt (L)
#   interest_rate (i)
#   number_of_payments

loan_amt = input('What is the loan amount? ')
interest_rate = input('What is the interest rate? ')
years = input('How many years is the loan? ')
number_of_payments = float(years) * 12

# ...being lazy...
# M = monthly_payment
L = float(loan_amt)
i = float(interest_rate)
n = number_of_payments

M = float(L * (i * (1+i) * n) / ((1+i) * n-1))
print(M)

#

print('The monthly payments for the ({0:.2f}) loan ' \
      'with the interest rate of {1:.2f} ' \
      'will be {2:.2f}.  There will be {3:d} payments ' \
      'over {4:0f} years.'.format(float(L),float(i),float(M),int(n),int(years)))
