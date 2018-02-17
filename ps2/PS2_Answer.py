# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 14:24:13 2018

@author: Oliver
"""

    
#def is_word_guessed(secret_word, letters_guessed):
#    '''
#    secret_word: string, the word the user is guessing; assumes all letters are
#      lowercase
#    letters_guessed: list (of letters), which letters have been guessed so far;
#      assumes that all letters are lowercase
#    returns: boolean, True if all the letters of secret_word are in letters_guessed;
#      False otherwise
#    '''
#    for char in secret_word:
#        if char in letters_guessed:
#            print("yes " + char)
#        else:
#            print("no " + char)
#            return False
#    return True 
#    
#    for char in secret_word:
#        if char not in letters_guessed:
#            print ("No")
#            return False
#        #else:
#            #print ("Yes")
#    return True        
#    
#
#secret_word = "apple"
#letters_guessed = ['a', 'b', 'p', 'e', 'z', 'l']
#print(is_word_guessed(secret_word, letters_guessed))

#==============================================================================

#def get_guessed_word(secret_word, letters_guessed):
#    '''
#    '''
#    elements = []
#    for char in secret_word:
#        if char in letters_guessed:
#            elements.append(char)
#            
#        else:
#            elements.append("_")
#    s = " ".join(elements)
#    return s
#
#
#secret_word = "apple"
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_guessed_word(secret_word, letters_guessed))

#==============================================================================
#import string
#
#def get_available_letters(letters_guessed):
#    '''
#    letters_guessed: list (of letters), which letters have been guessed so far
#    returns: string (of letters), comprised of letters that represents which letters have not
#      yet been guessed.
#    '''
#    alphabet = string.ascii_lowercase
#    remaining_letters = []
#    for char in alphabet:
#        if char not in letters_guessed:
#            remaining_letters.append(char)
#    s = "".join(remaining_letters)
#    return s
#    
#    
#secret_word = "apple"
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_available_letters(letters_guessed))

#==============================================================================

#number_of_guesses = 6
#
#
#while number_of_guesses > 0:
#    print ("you have ", number_of_guesses, " guesses remaining")
#    number_of_guesses -= 1    

#==============================================================================

def valid_letter(letter_input, secret_word):
    for char in secret_word:
        if letter_input in char:
            return(True)
        
    return(False)
        
            


secret_word = "apple" 
letter_input = input("Please enter a letter: ")

print(valid_letter(letter_input, secret_word))   

if (valid_letter(letter_input, secret_word)) == True:
    print("it works")
else:
    print("nope")    
#==============================================================================









    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    