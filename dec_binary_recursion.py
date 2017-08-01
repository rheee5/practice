def decBin(n):
    if n == 0:
        return '0'
    else:
        return decBin(n // 2) + str(n % 2)
