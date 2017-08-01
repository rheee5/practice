def iterPower(base, exp):
    total = 1
    while exp > 0:
        total = total * base
        exp -= 1
    return total
    print(total)
