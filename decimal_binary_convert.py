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
        # Algorithm for integers
        # input = number N
        # initialize counter i = 0
        # while N != 0
            # 1. Divide N by 2 so that N = 2Q + R
            # 2. Store R as (10^i)-th binary digit of binary number b (counting from right).
            # 3. N = Q
            # 4. i = i + 1
        # output = b
        
        # Algorithm for fractions
        # 1. First repeatedly multiply number by 2 till it becomes an integer.
        # 2. Count how many 2's were used in (1)
        # 3. Take answer of (1) and decimal places to left by answer of (2)
          
        # initialize
        number = abs(decimal_number) # to work with negative numbers        
        count = 0
        binary_number = 0
        
        # Integers
        if type(number) == int:
                while number != 0:
                        binary_number = (number % 2) * (10 ** count) + binary_number
                        number = number // 2
                        count +=1       
                
        # Fractions (floats)
        elif type(number) == float:
                while((number % 1) > 0.001):
                      number = number * 2 ** count
                      count +=1
                binary_number = base10_to_base2(int(number))

                for i in range(0, count):
                        binary_number = binary_number/10
        
        if decimal_number < 0: binary_number = -binary_number
        return binary_number