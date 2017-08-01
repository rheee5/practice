# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"
secretWord = 'zzz'
lettersGuessed = []


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    word = ''  # set blank intermediary variable where we store correctly guessed letters
    for char in secretWord:  # loop through the word see if it exists in list
        if char in lettersGuessed:
            word += char  # if existing, add to the intermediary variable
    if word == secretWord:  # at the end of the loop, check if it matches
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    emptyguess = ''  # start wtih empty string to record correct guesses
    for char in secretWord:  # loops through each character in the secret word
        if char in lettersGuessed:  # if character exists in the letters guessed list, then add that character to guess
            emptyguess += char
        else:  # if it doesn't exist, add underscore in place of that missing character
            emptyguess += '_'
    return emptyguess

import string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    lettersAvlb = string.ascii_lowercase  # variable where full alphabet from A to Z is stored
    for char in lettersGuessed:  # loop through each letter in the list of characters guessed if in the list, remove it
        if char in lettersAvlb:
            lettersAvlb = lettersAvlb.replace(char, '')
    print('Here are the remaining letters left to guess: ' + lettersAvlb)
    return lettersAvlb


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    guessesleft = 8
    word_length = len(secretWord)
    print('Welcome to the game Hangman!')
    print("I am thinking of a word that is " + str(word_length)+ " letters long")
    print('-----------')
    while guessesleft > 0:
        print('You have ' + str(guessesleft) + " guesses left")
        print('Available Letters: '+ getAvailableLetters(lettersGuessed))
        guess = input('Pleasedw guess a letter: ')
        lowerGuess = guess.lower()
        if len(lowerGuess) > 1:
            print("You can only guess 1 letter at a time. Please enter a single letter.")
            hangman(secretWord)
        if lowerGuess not in lettersGuessed:
            lettersGuessed.append(lowerGuess)
            if lowerGuess in secretWord:
                print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
                print('-----------')
                if isWordGuessed(secretWord, lettersGuessed):
                    print('Congratulations, You won!')
                    break
            else:
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                print('-----------')
                guessesleft -= 1
        else:
           print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
           print('-----------')
    if guessesleft == 0:
        print("Sorry, you've run out of guesses. The secret word was " + str(secretWord))


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
