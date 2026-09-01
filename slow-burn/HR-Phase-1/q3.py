#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#

def isAlphabeticPalindrome(code):
    only_alphbets = ''
    # extract only alphabets from the string
    for i in range(len(code)):
        ascii_val = ord(code[i])
        if ascii_val in range(65,91) or ascii_val in range(97,123):
            only_alphbets = only_alphbets + code[i].lower()
    
    # check if the extracted string is palindrome
    len_alpha = len(only_alphbets)
    # Run a loop till half of the string and match both halves.
    for i in range(math.floor(len_alpha/2)):
        if only_alphbets[i] != only_alphbets[len_alpha-1-i]:
            return 0       # if any time a mismatch ocurrs return not palindrome
    return 1
        
                
    
"""
ASCII   A-Z : 65-90
        a-z : 97-122
        
-  get all alphabet characters out of the given string
- find palindome of strings
- return answer

"""

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
