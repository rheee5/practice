# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 17:44:48 2017

@author: Edwin
"""

def genPrimes():
    primeList = []
    start = 1 
    while True:
        start +=1
        for p in primeList:
            if start % p == 0:
                break
        else:
            primeList.append(start)
            yield start