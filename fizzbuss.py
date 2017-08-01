# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 12:42:30 2017

@author: Edwin
"""

def fizzbuzz(num):
    for i in range(1,num + 1):
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 == 0:
            print('fizz')
        else:
            print(i)