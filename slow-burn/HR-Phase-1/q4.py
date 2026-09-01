#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isNonTrivialRotation' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def isNonTrivialRotation(s1, s2):
    # Write your code here
    str_len = len(s1)
    if str_len != len(s2):
        return 0
    
    i = j = 0
    while j < str_len and i < (2 * str_len):
        if s1[i % str_len] == s2[j]:
            j = j + 1
            i = i + 1
        elif j > 0:
            # reset j to start if a mismatch happens
            j = j - 1
        else:
            i = i + 1

    # # if both indices are at same place, the strings are equal. trivial rotation case.
    # # if i is still 0, it means it has been reset due to a mismach and and never again matched any char in s2.
    # if i == j or i == 0:
    #     return 0
        
    # # restart looking for possible matches for rest of s1 from beginning of s2 (unrotated part of string)
    # j = 0
    # while i < str_len and j < str_len:
    #     if s1[i] != s2[j]:
    #         return 0
    #     i = i + 1
    #     j = j + 1
    
    if j < str_len or i == j:
        return 0
            
    return 1

"""
Brute-force solution:
    left shift s1 till n-1 times and see if it matches the s2 string
        how to left shift 1 time:
            a b c d e
            0 1 2 3 4
            swap 0 and 1 ->  bacde
            swap 1 and 2 ->  bcade
            swap 2 and 3 ->  bcdae
            swap 3 and 4 ->  bcdea
            ----- itself an O(n) operation
    left shift n times -----> O(n^2)
    
    given a string:  a b c e c | a e f
    rotation: a e f | a b c e c

    2 parts of string : unrotated part U part
                        rotated part R part
                        
Run a loop on s1 from i=0  to len and s2 from j=0  to len:
    check if char at index matches 
        - yes : increment both i and j as this is probably R part
        - if not : reset i (s1) to beginning of string but increment j (s2) as usual 
                                            (we found a bad match - not a R part --> this match will 
                                            eventually fail when we are trying to match with U part which will be
                                            probably the beginning of s2 string.)

Once j exhausts we have checked all possible R part - most likely i has not exhausted yet. If i is also exhausetd means both strings are equal.
Eventually if i has been reset to 0, means we never found a single char from R part.
In both cases roatation check fails.

If that is not the case, proceed to keep checking rest of s1 with beginning of s2 for possible U part.
If any mismatch occurs no rotation possible.
If everything is fine, we are assured we found a  non-trivial rotation.


### FAILED CASE
aaaaaba
aaaabaa

repeating chars with one new char and then same chars repeat.
                         
##### NEXT ATTEMPT

--> Solution becomes apparent when we try to augment another array of same size to input array.
1. Start matching the s2 (rotated) with s1 chars one by one. The moment mismatch occurs we step back on s2.
2. Once we reach end of s1 --> we proceed to augmented array which has exactly same element as s1.
3. If rotation is done the rest of the elements of s2 will match some of the elements of augmented array.        

a b c e c a e f | a b c e c a e f
a e f a b c e c

i=0 and j=0 matches -> Increment both idx.
i=1 and j=1 does not matches -> decrement j keep i same.
keep doing till s2 ends.

-> This will require O(n) space. How to save? Instead of using an aumented array, we allow the idx of i to rotate using mod operator.   
    
"""

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = isNonTrivialRotation(s1, s2)

    print(int(result))
