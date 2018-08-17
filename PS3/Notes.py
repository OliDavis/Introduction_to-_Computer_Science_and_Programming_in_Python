# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 20:09:47 2018

@author: Oliver
"""
#Word = "@"
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    Letter_Sum = 0
    s = word.lower()
    wordlen = len(word)
#    print (wordlen)
#    print (n)
    
    for letter in s:
        if (letter in SCRABBLE_LETTER_VALUES) == False:
            return 0
        Letter_Sum += SCRABBLE_LETTER_VALUES[letter]
#    print(Letter_Sum)
    
    second_component = (7*wordlen)-(3*(n-wordlen)) 
    if second_component < 1:
        second_component = 1
    return (Letter_Sum*second_component)
    
print(get_word_score('',HAND_SIZE))