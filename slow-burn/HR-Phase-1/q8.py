#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'areBracketsProperlyMatched' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code_snippet as parameter.
#

def areBracketsProperlyMatched(code_snippet) -> int:
    stack: list[str] = []
    brackets_list: dict[str,str] = {
        ")": "(",           # closing brackets being matched to their opening brackets
        "}": "{",
        "]": "[",
    }
    for idx, char in enumerate(code_snippet):
        if char in list(brackets_list.values()):
            stack.append(char)
        elif char in list(brackets_list.keys()):
            if len(stack) and stack[-1] == brackets_list[char]:
                stack.pop()
            else:
                return 0
                
    return len(stack) == 0
    
"""
- use stack to push the brackets, (only the opening brackets not the closing ones).
- pop the opening brackets as soon as a matchig closing bracket appears
- At the end of iteration if stack is not empty then brackets are not balanced.
"""

if __name__ == '__main__':
    code_snippet = input()

    result = areBracketsProperlyMatched(code_snippet)

    print(int(result))
