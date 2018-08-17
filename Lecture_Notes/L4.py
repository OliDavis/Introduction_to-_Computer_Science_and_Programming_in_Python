# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:32:19 2018

@author: Oliver
L4 Functions
"""

def quotient_and_remainder(x,y):
    q = x // y 
    r = x % y
    return (q, r)
(quot, rem) = quotient_and_remainder(4,5) 

#def is_even_with_return(i):
#    """
#    input: i, a positive int
#    returns True if i is even, otherwise False
#    """
#    print("with return")
#    remainder = i % 2
#    return remainder == 0
#
#is_even_with_return(3)
#print(is_even_with_return(3))
#
# 
#
#
#
#def f(x):
#    x = x+1
#    print('in f(x): x = ', x)
#    return x
#
#x = 3
#z = f(x)
#
#
#
#def is_even(i):
#    """
#    input: 1, a positive int
#    returns True if i is even, otherwise False
#    """
#    remainder = i%2
#    return remainder == 0
#
#print("All numbers between 0 and 20: evn or not")
#for i in range(20):
#    if is_even(i):
#        print(i, "even")
#    else:
#        print(i, "odd")