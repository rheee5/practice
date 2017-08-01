lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
secretWord = 'apple'


def getGuessedWord(secretWord, lettersGuessed):  # function which returns an output which shows letters guessed correctly with remaining ones as underscore
    emptyguess = ''  # start wtih empty string to record correct guesses
    for char in secretWord:  # loops through each character in the secret word
        if char in lettersGuessed:  # if character exists in the letters guessed list, then add that character to guess
            emptyguess += char
        else:  # if it doesn't exist, add underscore in place of that missing character
            emptyguess += '_'
    return emptyguess
