# Paste your function here
    

def is_triangular(k):
 # k, a positive integer
 # returns True if k is triangular and False if not

    mySum = 0
    for i in range(k+1):
        mySum += i
        if mySum == k:
            return "True"
    return "False"