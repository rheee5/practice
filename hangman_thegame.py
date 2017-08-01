# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 13:43:04 2017

@author: Edwin
"""

secretWord = 'python'
lettersGuessed = []


def getGuessedWord(secretWord, lettersGuessed):  # function which returns an output which shows letters guessed correctly with remaining ones as underscore
    emptyguess = ''  # start wtih empty string to record correct guesses
    for char in secretWord:  # loops through each character in the secret word
        if char in lettersGuessed:  # if character exists in the letters guessed list, then add that character to guess
            emptyguess += char
        else:  # if it doesn't exist, add underscore in place of that missing character
            emptyguess += '_'
    print(emptyguess)
    return emptyguess

mistakesMade = 0

def hangman(secretWord):
    word_length = len(secretWord)
    print('Welcome to Hangman! Try to guess the word. The word you are trying to guess is ' + str(word_length) + 'characters long.')
    print('You can only guess one letter a time, and the guess must be a letter!')
    guess = input('Please enter a letter to guess for this round: ')
    lowerGuess = guess.lower()
    lettersGuessed.append(lowerGuess)
    if len(guess) > 1:
        print('\nInvalid guess. Your guess must be a single letter. \n')
        hangman(secretWord)
    for char in lettersGuessed:
        if char in secretWord:
            print('Yes! This letter is in the word.')
            getGuessedWord(secretWord, lettersGuessed)
            hangman(secretWord)
        else:
            print('Letter you guessed is not in secret word')
            mistakesMade += 1
            print('you have ' + str(8 - mistakesMade) + ' gusses remaining')
            if mistakesMade == 8:
                print('You have run out of guesses. Sorry, you lose.')
                break
            hangman(secretWord)


hangman(secretWord)
