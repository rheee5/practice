animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}


def biggest(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = ''  # this stores the key of the biggest length in value from the dictionary
    max = 0  # this is where we store the biggest length of the value of the dictionary
    for k in aDict.keys():  # iterate over the key
        if len(aDict[k]) > max:  # if the length of the value for each key, if it's greater than the stored max,
            result = k  # reassign result to hold that key
            max = len(aDict[k])  # then reassign max to hold that length
    return result  # return final result


biggest(animals)
