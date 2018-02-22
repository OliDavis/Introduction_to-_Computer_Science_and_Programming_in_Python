## -*- coding: utf-8 -*-
#"""
#Created on Thu Feb 15 18:12:37 2018
#
#@author: Oliver
#"""
#
#def mult_iter(a,b):
#    result = 0
#    while b > 0:
#        result += a
#        b -= 1 
#    return result
#    
#print(mult_iter(3,4))
#
##==============================================================================
#
##Iteration
#def factorial_iter(n):
#    prod = 1
#    for i in range(1,n+1):
#        prod *= i
#    return prod
#
##Recursion
#def factorial(n):
#    if n == 1:
#        return 1
#    else:
#        return n*factorial(n-1)
#    
#n = 3
#print(factorial_iter(n))
#print(factorial(n))
# 
#==============================================================================

#def lyrics_to_frequencies(lyrics):
#    myDict = {}
#    for word in lyrics:
#        if word in myDict:
#            myDict[word] +=1
#        else:
#            myDict[word] = 1
#    return myDict
#
#she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
#'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#
#'you', 'think', "you've", 'lost', 'your', 'love',
#'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
#"it's", 'you', "she's", 'thinking', 'of',
#'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',
#
#'she', 'says', 'she', 'loves', 'you',
#'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#'yes', 'she', 'loves', 'you',
#'and', 'you', 'know', 'you', 'should', 'be', 'glad',
#
#'she', 'said', 'you', 'hurt', 'her', 'so',
#'she', 'almost', 'lost', 'her', 'mind',
#'and', 'now', 'she', 'says', 'she', 'knows',
#"you're", 'not', 'the', 'hurting', 'kind',
#
#'she', 'says', 'she', 'loves', 'you',
#'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#'yes', 'she', 'loves', 'you',
#'and', 'you', 'know', 'you', 'should', 'be', 'glad',
#
#'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#'with', 'a', 'love', 'like', 'that',
#'you', 'know', 'you', 'should', 'be', 'glad',
#
#'you', 'know', "it's", 'up', 'to', 'you',
#'i', 'think', "it's", 'only', 'fair',
#'pride', 'can', 'hurt', 'you', 'too',
#'pologize', 'to', 'her',
#
#'Because', 'she', 'loves', 'you',
#'and', 'you', 'know', 'that', "can't", 'be', 'bad',
#'Yes', 'she', 'loves', 'you',
#'and', 'you', 'know', 'you', 'should', 'be', 'glad',
#
#'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
#'with', 'a', 'love', 'like', 'that',
#'you', 'know', 'you', 'should', 'be', 'glad',
#'with', 'a', 'love', 'like', 'that',
#'you', 'know', 'you', 'should', 'be', 'glad',
#'with', 'a', 'love', 'like', 'that',
#'you', 'know', 'you', 'should', 'be', 'glad',
#'yeah', 'yeah', 'yeah',
#'yeah', 'yeah', 'yeah', 'yeah'
#]
#
#
#beatles = lyrics_to_frequencies(she_loves_you)
#
#def most_common_words(freqs):
#    values = freqs.values()
#    best = max(freqs.values())
#    words = []
#    for k in freqs:
#        if freqs[k] == best:
#            words.append(k)
#    return(words, best)
#
#def words_often(freqs, minTimes):
#    result = []
#    done = False
#    while not done:
#        temp = most_common_words(freqs)
#        if temp[1] >= minTimes:
#            result.append(temp)
#            for w in temp[0]:
#                del(freqs[w]) # remove word from dict
#        else:
#            done = True
#    return result
#    
#print(words_often(beatles, 5))


#==============================================================================
    ##DICTIONARIES##

def get_grade(student, name_list, grade_list, course_list):
    i = name_list.index(student)
    grade = grade_list[i]
    course = course_list[i]
    return(course, grade)
    
my_dict = {}
grades = {'Ana':'B','John':'A+','Denise':'A','Katy':'A'}

print(grades['John'])   #Look Up
grades['Sylvan'] = 'A'  #Add Entry
'John' in grades        #Return True
'Daniel' in grades      #Returns False
del(grades['Ana'])      #Delete Entry
   

grades.keys()           #get an iterable that acts like a tuple of all keys
grades.values()         #get an iterable that acts like a tuple of all values

d = {4:{1:0}, (1,3):"twelve", 'const':[3.14,2.7,8.44]}

























