import string  # import string module

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


def getAvailableLetters(lettersGuessed):  # function which takes parameter of letters guessed, and returns letters still left available to guess
    lettersAvlb = string.ascii_lowercase  # variable where full alphabet from A to Z is stored
    for char in lettersGuessed:  # loop through each letter in the list of characters guessed if in the list, remove it
        if char in lettersAvlb:
            lettersAvlb = lettersAvlb.replace(char, '')
    print('Here are the remaining letters left to guess: ' + lettersAvlb)
    return lettersAvlb
