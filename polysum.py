import math


def polysum(n, s):  # function polysum taking two inputs, n = number of sides s = length of side
    area = (0.25 * n * s**2) / math.tan(math.pi / n)  # calculates the area using some functions from math module
    perimeter = s * n  # calculates perimeter with
    return round(area + perimeter**2, 4)  # returns sum of area and perimeter squared
