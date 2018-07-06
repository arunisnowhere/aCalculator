# -*- coding: utf-8 -*-
"""
Arun Narayanan
Started: June 17, 2018
Ended: June 17, 2018
(Subsequently) Last Modified: June 17, 2018
"""

# Fibonacci numbers (https://en.wikipedia.org/wiki/Fibonacci_number) implemented using recursion and iteration

# recursion
def fib_recur(n):
    '''
    Returns the nth Fibonacci number, where F0 = 0; F1 = 1
    Uses recursion
    (n) -> (F_n)
    (int) -> (int)
    Examples
    >>> print(fib_recur(3))
    2
    >>> print(fib_recur(10))
    55
    >>> print(fib_recur(3.5))
    Error: n must be an integer    
    '''
    # Error check for type
    if not (type(n) == int):
        return ("Error: n must be an integer")
    # Initializing seed values
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recur(n - 1) + fib_recur(n - 2)

# My original solution is given in archives below. The following was taken from stackoverflow:
# https://stackoverflow.com/questions/15047116/an-iterative-algorithm-for-fibonacci-numbers
    
# using iteration with tuple assignment
def fib_iter(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, b + a
    return a

# why does a,b = b,a+b inside the for loop work and not when you write it like this a=b and b = a+b? 
# i mean a,b = b,a+b is just a = b and b = a+b right? 

# Tuple assignment is not the same as sequentially assigning each right side expressions to its respective "variable"
# with tuple assignment, the last evaluation is done before the first assignment: 
# consider swapping: a, b = b, a

''' 
Archives: My original solution
# iteration
def fib_iter(n):
    Returns the nth Fibonacci number, where F0 = 0; F1 = 1
    Uses recursion
    (n) -> (F_n)
    (int) -> (int)
    Examples
    >>> print(fib_iter(3))
    2
    >>> print(fib_iter(10))
    55
    >>> print(fib_iter(3.5))
    Error: n must be an integer
    # Error check for type
    if not (type(n) == int):
        return ("Error: n must be an integer")
    # Initializing seed values
    Fn_2 = 0; # F_(n-2)
    Fn_1 = 1; # F_(n-1)
    if n == 0:
        return 0     
    # otherwise, iterate
    for i in range(1,n):
        Fn = Fn_1 + Fn_2
        Fn_2 = Fn_1
        Fn_1 = Fn
    return Fn_1
'''

