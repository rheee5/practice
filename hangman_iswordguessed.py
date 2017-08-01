lettersGuessed = ['e', 'y', 'k', 'p', 'r', 's', 't', 'h', 'o', 'n']
secretWord = 'python'


def isWordGuessed(secretWord, lettersGuessed): #function which returns a Boolean based on if the secret word is correctly guessed
    word = ''  # set blank intermediary variable where we store correctly guessed letters
    for char in secretWord:  # loop through the word see if it exists in list
        if char in lettersGuessed:
            word += char  # if existing, add to the intermediary variable
    if word == secretWord:  # at the end of the loop, check if it matches
        return True
    else:
        return False
