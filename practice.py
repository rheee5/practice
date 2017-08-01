# Paste your function here
    
d = {4:True, 2:True, 0:True}

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    #YOUR CODE HERE
    inv_d = {}
    for k,v in d:
        inv_d[v] = inv_d.get(v,[])
        inv_d[v].append(k)
        inv_d[v].sort()
    return inv_d