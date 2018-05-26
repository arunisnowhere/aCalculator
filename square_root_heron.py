# -*- coding: utf-8 -*-
"""
Arun Narayanan
Started: May 26, 2018
Ended: May 26, 2018 
Modified:
"""

# Heron's method for finding the approximate square root of a non-negative real number
# also called the Babylonian method

# Idea: if y is an under-estimate of sqrt(x), then x/y will be an over-estimate, and vice versa
# Therefore, the average of the over-estimation andunder-estimation will be a closer approximation.
# A quadratically convergent algorithm: the number of correct digits of the approximation roughly doubles with each iteration.

import math

def square_root_heron(x):  
    '''
    Return square root for any nonnegative number    
    (x) -> (nIterations, sqrt(x))
    (float) -> (int, float)
    Uses Heron's method
    '''
    y = 2**(math.frexp(10)[1]/2) # guess the value of y, suggested in https://math.stackexchange.com/questions/521981/picking-an-appropriate-guess-for-herons-method-and-the-fast-reciprocal-method    
    epsilon = 1e-10 # set error
    iter = 0
    while (abs(x-y**2)>=epsilon):        
        iter += 1
        y = (y+x/y)/2    
    return iter, y

print(square_root_heron(1023.45))