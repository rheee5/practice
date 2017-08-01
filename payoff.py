balance = 1000
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

months = 1

while months <= 12:
    monthlyInterestRate = annualInterestRate / 12.0
    minimumMonthlyPayment = monthlyPaymentRate * balance
    unpaidBalance = balance - minimumMonthlyPayment
    balance -= minimumMonthlyPayment
    balance += unpaidBalance * monthlyInterestRate
    print('month', months, 'minimum payment amount is', round(minimumMonthlyPayment, 2))
    months += 1

print('balance is', round(balance, 2))
