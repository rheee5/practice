# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 13:12:36 2017

@author: Edwin
"""

hand = {'c': 1, 'o': 1, 'f': 2, 'e': 2}
wordList = ['coffee', 'cat', 'rhee', 'rapture', 'rap', 'chayote']

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    word_dictionary = {} #convert the word into a dictionary
    updated_hand = {} #this is where we store the new updated hand 
    for char in word: #go thorugh each character in the word
        word_dictionary[char] = word_dictionary.get(char, 0) + 1 #add it to the word dictionary; if it exists, keep counting
    for k, v in hand.items(): #go thorugh each key and value within the hand
        updated_hand[k] = v - word_dictionary.get(k, 0) #subtract the word dicctionary values from the hand values 
    return updated_hand

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    hand_copy = hand.copy() #create a copy of the dictionary
    word_storage = "" #empty storage to pass off characters in dictionary
    for char in word: #loop through each letter 
        if hand_copy.get(char,0) > 0: #if that character value exists, and is greater than 0
            word_storage += char #add it to the word storage, 
            hand_copy[char] -= 1 # subtract 1 off as it's been added to the word storage
    if word in wordList and word_storage == word: #check if word is in the list AND if word is equal to the storage word we created
        return True
    else:
        return False


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    score = 0 #storage for score 
    word_length = len(word) # get word length
    for char in word: #loop through each character in the word,
        score += SCRABBLE_LETTER_VALUES.get(char, 0) # get the point value for each word from the dictionary, then add it to the score
    score = score * word_length #multiply the score with the length 
    if n == word_length: #if the length of the word, is equal to n, ie: every letter is used, give additional 50 points
        score += 50
    else:
        score
    return score
    # TO DO ... <-- Remove this comment when you code this function

def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    for char in hand:
        # Display the hand
        print('current hand is: ', end = '')
        displayHand(hand)
        # Ask user for input
        user_input = input("Enter a word or a \".\" to indicate you are finished: ")
        # If the input is a single period:
        if user_input == '.':
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:

            # If the word is not valid:
            if not isValidWord(user_input, hand, wordList):            
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word. Please try again.')
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                wordScore = getWordScore(user_input, n)
                total_score += wordScore
                print("'"+str(user_input)+"'" + ' earned',wordScore,'points. ' 'Total score is', total_score)
                print()
                # Update the hand 
                hand = updateHand(hand, user_input)
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('game is over, Your total score is: ', total_score)

#