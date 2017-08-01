animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}


def biggest(aDict):
    biggest = ''
    len_count = 0
    for key in aDict.keys():
        if len(aDict[key]) > len_count:
            biggest = key
        len_count = len(aDict[key])
    return biggest
