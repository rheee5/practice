# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:14:47 2017

@author: Edwin
"""

def isOdd(n):
    if n%2 == 1:
        return True
    else:
        return False
        
def largest_odd_times(L):
    NL = []
    largest = 0
    for n in L:
        if isOdd(L.count(n)) == True:
            NL.append(n)
    for num in NL:
        if num > largest:
            largest = num
    if largest == 0:
        return None
    else:
        return largest