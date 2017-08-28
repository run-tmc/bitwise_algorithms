# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 17:46:44 2017

@author: trevo
"""

"""This algorithm counts the number of bits in binary number
   from an input variable that is a normal integer or binary (0b),
   octal (0o), hexadecimal (0X) literals"""

def count_bits(n):
    # initialize bit counter number to zero (0)
    num_bits = 0
    # loop until binary number equals zero (0) - False
    while n:
        # mask and the LSB position and add to bit counter 
        num_bits += n & 1
        # right shift binary number one position inplace
        n >>= 1
    return num_bits

# set value to count bits
n=0O10
print 'The number of bits in ', n, 'is ', count_bits(n)
