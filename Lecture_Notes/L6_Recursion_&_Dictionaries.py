# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:12:37 2018

@author: Oliver
"""

def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1 
    return result
    
print(mult_iter(3,4))

#==============================================================================

#Iteration
def factorial_iter(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

#Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
n = 3
print(factorial_iter(n))
print(factorial(n))
 