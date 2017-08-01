def gcdRec(a, b):
    if b == 0:
        return a
    return gcdRec(b, a % b)


gcdRec(3768, 1701)
