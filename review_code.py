balance = 1200
annualInterestRate = 0.2
lower = balance / 12
upper = ((balance * annualInterestRate) + balance) / 12
epsilon = 0.01
guessPymt = (lower + upper) / 2


def balancePaidOff(balance, annualInterestRate, guessPymt):
    monthlyInterestRate = annualInterestRate / 12
    for month in range(1, 13):
        balance -= guessPymt
        balance += monthlyInterestRate * balance
    return balance


def enoughPymt(balance, guessPymt):
    balanceRemaining = balancePaidOff(balance, annualInterestRate, guessPymt)
    while balanceRemaining > epsilon:
        if balanceRemaining > 0:
            upper = guessPymt
        else:
            lower = guessPymt
        guessPymt = (lower + upper) / 2
    return guessPymt


enoughPymt(balance, guessPymt)
