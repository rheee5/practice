# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 18:57:39 2017

@author: Edwin
"""

def isPermutation(L1,L2): #checks for permutation 
    if len(L1) != len(L2): #checks length of list 1 to List 2
        return False;  
    for i in range(0, len(L1)):
        if L1.count(L1[i]) != L2.count(L1[i]):
            return False

def is_list_permutation(L1,L2):
    if isPermutation(L1,L2) == False: #check if not permutation
        return False #if not return false
    elif not L1:
        return (None, None, None)
    else:
        mostOccurItem = max(set(L1), key=L1.count)  
        numberOfTimes = L1.count(mostOccurItem)
        theType = type(mostOccurItem)
        return (mostOccurItem, numberOfTimes, theType)