# -*- coding: utf-8 -*-
"""
Arun Narayanan
Started: May 26, 2018
Ended: May 26, 2018 
Last Modified: June 8, 2018 
"""

# Heron's method for finding the approximate square root of a non-negative real number
# also called the Babylonian method

# Idea: if y is an under-estimate of sqrt(x), then x/y will be an over-estimate, and vice versa
# Therefore, the average of the over-estimation andunder-estimation will be a closer approximation.
# A quadratically convergent algorithm: the number of correct digits of the approximation roughly doubles with each iteration.

import math

def square_root_heron(x, precision = 2, iterations = False):
    '''
    Return square root for any nonnegative number
    Uses Heron's method
    Required precision can be input; default setting = 2    
    Optionally returns the number of iterations used to determine the square root
    (x, precision, iterations) -> (sqrt(x), -sqrt(x), nIterations)
    (float, int, bool) -> (float, float, int)
    Examples
    >>> print(square_root_heron(1225))
    (35.0, -35.0)
    >>> print(square_root_heron(1000))
    (31.62, -31.62)
    >>> print(square_root_heron(1000,5))
    (31.62278, -31.62278)
    >>> print(square_root_heron(1000,'5'))
    Error: precision must be an integer
    >>> print(square_root_heron(1000,5.0))
    Error: precision must be an integer
    >>> print(square_root_heron(1000,True))
    Error: precision must be an integer
    >>> print(square_root_heron(1000,2,'True'))
    Error: request for number of iterations must be boolean True or False
    '''
    # Error check for precision
    if not (type(precision) == int):
        return ("Error: precision must be an integer")
    # Error check for iterations
    if not (type(iterations) == type(True)):
        return ("Error: request for number of iterations must be boolean True or False")
    # Error check for x (must be >= 0)
    if x < 0:
        return ("Error: please enter nonnegative number only")
    if x == 0:
        return 0
    y = 2**(math.frexp(10)[1]/2) # guess the value of y, suggested in https://math.stackexchange.com/questions/521981/picking-an-appropriate-guess-for-herons-method-and-the-fast-reciprocal-method    
    epsilon = 1/(10**precision) # set error    
    iter = 0
    while (abs(x-y**2)>epsilon):        
        iter += 1
        y = (y+x/y)/2
    # the while test tests precision of y**2 not y itself, so this rounding step is required
    # then, why check against precision in the while test?
    # to decrease the number of iterations required. lower reqd. precision => fewer iterations
    y = round(y,precision)
    if iterations:
        return y, -y, iter
    else:
        return y, -y