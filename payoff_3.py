balance = 1200
annualInterestRate = 0.2


def balancePaidOff(balance, annualInterestRate, guessPymt):
    monthlyInterestRate = annualInterestRate / 12
    for month in range(1, 13):
        balance -= guessPymt
        balance += monthlyInterestRate * balance
    return balance


def enoughPymt(balance):
    epsilon = 0.01
    lower = balance / 12
    upper = ((balance * annualInterestRate) + balance) / 12
    guessPymt = (lower + upper) / 2
    balanceRemaining = balancePaidOff(balance, annualInterestRate, guessPymt)
    while abs(balanceRemaining) > epsilon:
        if balanceRemaining > 0:
            lower = guessPymt
        else:
            upper = guessPymt
        guessPymt = (lower + upper) / 2
        balanceRemaining = balancePaidOff(balance, annualInterestRate, guessPymt)
    print("Lowest payment to finish paying off principal in 1 yr:", round(guessPymt, 2))
    return guessPymt


enoughPymt(balance)
