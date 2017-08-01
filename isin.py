"""isIn.py
author: edwinrhee
"""


def isIn(char, aStr):
    start = 0
    end = len(aStr)
    if len(aStr) > 0:
        midChar = aStr[(end - start) // 2]
    if len(aStr) == 0:
        return False

    elif len(aStr) == 1:
        return char == aStr
    elif char == midChar:
        return True
    elif char < midChar:
        return isIn(char, aStr[:(end - start) // 2])
    elif char > midChar:
        return isIn(char, aStr[(end - start) // 2:])

isIn('a', '')
