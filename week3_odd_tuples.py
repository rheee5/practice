def oddTuples(aTup):
    eTup = ()
    index = 0
    while index < len(aTup):
        eTup += (aTup[index],)
        print('index =', index, 'aTup =', aTup[index])
        index += 2
    return eTup
