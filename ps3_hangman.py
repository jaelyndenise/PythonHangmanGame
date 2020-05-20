# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

#WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open('C:/Users/superpawn/Desktop/Hangman Game/words.txt', 'r')
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

#isWordGuessed('apple', ['e', 'i', 'k', 'p', 'r', 's'])
def isWordGuessed(secretWord, lettersGuessed):
  '''
  secretWord: string, the word the user is guessing
  lettersGuessed: list, what letters have been guessed so far
  returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
  '''
  # FILL IN YOUR CODE HERE...
  for letter in secretWord:
      if letter.lower() not in lettersGuessed:
          return False
  return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessed = ""
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            guessed += "_ "
        else:
            guessed += (letter + " ")
            
    return guessed


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alpha = "abcdefghijklmnopqrstuvwxyz"
    remaining = ""
    for letter in alpha:
        if letter in lettersGuessed:
            pass
        else:
            remaining += letter
            
    return remaining

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
    # FILL IN YOUR CODE HERE...
    #secretWord = chooseWord(wordlist)
    guesses = 8
    lettersGuessed = []
    print ("Welcome to the game, Hangman!")
    if len(secretWord) > 1:
        print ("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    elif len(secretWord) == 1:
        print ("I am thinking of a word that is " + str(len(secretWord)) + " letter long.")
    print ("- - - - - - - - - - ")
    print ("You have " + str(guesses) + " guesses left.")
    print ("Available letters: " + getAvailableLetters([lettersGuessed]))
    
    while isWordGuessed(secretWord, lettersGuessed) == False:
        guess = input("Please guess a letter: ")
        if guess.lower() == secretWord:
            lettersGuessed += guess
            print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print ("- - - - - - - - - - ")
            break
        elif guess.lower() in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print ("- - - - - - - - - - ")
            print ("You have " + str(guesses) + " guesses left.")
            print ("Available letters: " + getAvailableLetters(lettersGuessed))
        elif guess.lower() in secretWord:
            lettersGuessed += guess
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                print ("- - - - - - - - - - ")
                break
            else:
                print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                print ("- - - - - - - - - - ")
                print ("You have " + str(guesses) + " guesses left.")
                print ("Available letters: " + getAvailableLetters(lettersGuessed))
        elif guess.lower() not in secretWord:
            lettersGuessed += guess
            guesses -= 1
            print ("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            print ("- - - - - - - - - - ")
            if guesses == 0:
                break
            else:
                print ("You have " + str(guesses) + " guesses left.")
                print ("Available letters: " + getAvailableLetters(lettersGuessed))
            
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print ("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + str(secretWord))
        
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
