animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

ani_value = animals.values()
ani_key = animals.keys()


def how_many(aDict):
    counter = 0
    for v in aDict.values():         # Since all the values of aDict are lists, aDict.values() will be a list of lists
        counter = counter + len(v)
    return counter
