lyrics = "baby i just don’t know what to say. you were my dream you were my dream and now it all feels so real. you are real. yea heavy drugs and light hearted jokes. quit my day job just to stay up all night with you we are going to hollywood and never coming back, coming back maybe we’ll turn to gold don’t stop. action, friction live in a fiction baby hollywood."

lyrics_list = lyrics.replace('. ', ' ').split(' ')


def lyrics_to_freq(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


freq = lyrics_to_freq(lyrics_list)


def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result
