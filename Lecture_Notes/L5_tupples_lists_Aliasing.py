# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 18:25:18 2018

@author: Oliver
"""
#Tuples
def quotient_and_remainder(x,y):
    q = x // y
    r = x % y
    return(q, r)

(quot, rem) = quotient_and_remainder(4,5)
print(quot, rem)

#=====================================================================

#Manipulating Tuples
def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)


# apply to any data you want!
tswift = ((2014,"Katy"),
          (2014, "Harry"),
          (2012,"Jake"), 
          (2010,"Taylor"), 
          (2008,"Joe"))    
(min_year, max_year, num_people) = get_data(tswift)
print("From", min_year, "to", max_year, \
        "Taylor Swift wrote songs about", num_people, "people!")

#=====================================================================


def sum_elem_method1(L):
    total = 0
    for i in L:
        total += i
    return total
    
def sum_elem_method2(L):
    total = 0
    for i in range(len(L)):
        total += L[i] 
    return total
    
print(sum_elem_method1([1,2,3,4,]))
print(sum_elem_method2([1,2,3,4,]))