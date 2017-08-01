balance = 130
annualInterestRate = 0.2
Finding = True
fixedPymt = 0


def findpymt(balance, annualInterestRate, fixedPymt):
    months = 1
    while months <= 12:
        monthlyInt = annualInterestRate / 12.0
        balance -= fixedPymt
        balance += balance * monthlyInt
        months += 1
    if balance <= 0:
        return fixedPymt
    else:
        return False

while Finding == True:
    if findpymt(balance, annualInterestRate, fixedPymt):
        Finding = False
        print('fixed payment amount should be', fixedPymt)
    else:
        fixedPymt += 10
        findpymt(balance, annualInterestRate, fixedPymt)
