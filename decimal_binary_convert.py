# -*- coding: utf-8 -*-
"""
Arun Narayanan
Started: June 19 2014
Ended: JJuly 16 2014
(Subsequently) Last Modified: July 7 2018
"""

# To convert decimal to binary

def base10_to_base2(decimal_number):
        '''
        (number) -> (number)
        
        Converts a number in base 10, i.e., decimal number, to number in base 2, i.e., binary number.

        Example:
        >>>

        '''
        # Integers
        # Algorithm
        # input = number N
        # initialize counter i = 1
        # while N != 0
            # 1. Divide N by 2 so that N = 2Q + R
            # 2. Store R as i-th binary digit of binary number b (counting from right).
            # 3. N = Q
            # 4. i = i + 1
        # output = b
          
        # initialize
        number = decimal_number # to work with negative numbers
        if decimal_number < 0: number = abs(number)
        count = 0
        binary_number = 0
        
        if type(decimal_number) == int:
                while number != 0:
                        binary_number = (number % 2) * (10 ** count) + binary_number
                        number = number // 2
                        count +=1        
        if decimal_number < 0: binary_number = -binary_number
        return binary_number
