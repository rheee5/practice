balance = 5000
annualInterestRate = 0.2
mir = annualInterestRate / 12.0

upper_bound = (balance * (1 + mir)**12) / 12.0
lower_bound = balance / 12

x = (upper_bound + lower_bound) / 2


def totalInterests(x):
    "calculate total interests in 12 months"
    total_interests = 0
    new_balance = balance

    for month in range(12):
        interests = (new_balance - x) * mir
        new_balance = (new_balance - x) * (1 + mir)
        total_interests += interests
    return total_interests

# Use bisection method
while abs(12 * x - totalInterests(x) - balance) > 0.01:
    if 12 * x - totalInterests(x) - balance > 0:
        upper_bound = x
        x = (upper_bound + lower_bound) / 2
    else:
        lower_bound = x
        x = (upper_bound + lower_bound) / 2

print("Lowest Payment: %s" % round(x, 2))
