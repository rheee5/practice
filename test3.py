balance = 1000
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

months = 1
while months <= 12:
    monthlyInt = annualInterestRate / 12.0
    minPymt = balance * monthlyPaymentRate
    balance -= minPymt
    balance += monthlyInt * balance
    print('monthly payment is', minPymt)
    months += 1

print('total balance at the end of the year is', round(balance, 2))
