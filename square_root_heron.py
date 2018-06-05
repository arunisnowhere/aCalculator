# -*- coding: utf-8 -*-
"""
Arun Narayanan
Started: May 26, 2018
Ended: May 26, 2018 
Last Modified: June 5, 2018 
"""

# Heron's method for finding the approximate square root of a non-negative real number
# also called the Babylonian method

# Idea: if y is an under-estimate of sqrt(x), then x/y will be an over-estimate, and vice versa
# Therefore, the average of the over-estimation andunder-estimation will be a closer approximation.
# A quadratically convergent algorithm: the number of correct digits of the approximation roughly doubles with each iteration.

import math

def square_root_heron(x, iterations = False):
    '''
    Return square root for any nonnegative number
    Uses Heron's method
    Optionally returns the number of iterations to determine the square root
    (x, boolean) -> (sqrt(x), nIterations)
    (float, bool) -> (float, int)
    Examples
    >>> print(square_root_heron(1225))
    35.0
    >>> print(square_root_heron(1225,True))
    (35.0, 8)
    >>> print(square_root_heron(1225,1)
    Error: optional parameter must be True or False
    >>> print(square_root_heron(1225,'True')
    Error: optional parameter must be True or False
    '''    
    if not (type(iterations) == type(True)):
        return ("Error: optional parameter must be True or False")
    y = 2**(math.frexp(10)[1]/2) # guess the value of y, suggested in https://math.stackexchange.com/questions/521981/picking-an-appropriate-guess-for-herons-method-and-the-fast-reciprocal-method    
    epsilon = 1e-10 # set error
    iter = 0
    while (abs(x-y**2)>=epsilon):        
        iter += 1
        y = (y+x/y)/2
    if iterations:
        return y, iter
    else:
        return y