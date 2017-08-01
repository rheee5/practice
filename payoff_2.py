balance = 5000
annualInterestRate = 0.2
fixedPymt = 0
finding = True


def payment(balance, annualInterestRate, fixedPymt):
    monthlyIterest = annualInterestRate / 12
    for month in range(12):
        balance -= fixedPymt
        balance += monthlyIterest * balance
    if balance <= 0:
        return fixedPymt
    else:
        return False

while finding == True:
    if payment(balance, annualInterestRate, fixedPymt):
        finding = False
        print('fixedPymt:', round(payment(balance, annualInterestRate, fixedPymt), 2))
    else:
        fixedPymt += 0.01
        payment(balance, annualInterestRate, fixedPymt)
