#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processCouponStackOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def processCouponStackOperations(operations) -> list[int]:
    # Write your code here
    main_stack: list[int] = []
    min_stack: list[int] = []
    output: list[int] = []
    operations_pattern: str = r"^(push (\d+)|pop|top|getMin)$"
    
    for operation in operations:
        
        # Match evey operation with the expected input format
        match = re.search(operations_pattern, operation)
        
        if not match:
            return output
        
        # Take the grouped match - corresponds to the integer alongside the `push` input    
        item = match.group(2)
        
        if item:
            # If integer to be pushed is provided, push to main_stack. 
            # Also, check for min item and push to min_stack
            item = int(item)
            main_stack.append(item)
            if len(min_stack) == 0 or item <= min_stack[-1]:
                min_stack.append(item)
                
        # for any operation other than push
        else:
            # If the main_stack is empty, then top, pop and getMin cannot work.
            if len(main_stack) == 0:
                continue
                
            if operation == "pop":
                popped_item = main_stack.pop()
                if min_stack[-1] == popped_item:
                    min_stack.pop()
                    
            elif operation == "top":
                output.append(main_stack[-1])
                
            elif operation == "getMin":
                output.append(min_stack[-1])
            
    return output
    
"""
- handle all inputs using a match-case construct
- pop, top and getMin should follow the constraint of having non-empty array
- match the operations with expected input using re and proceed only if match is there
- push the value in results array whenever top operation is encountered


"""

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    result = processCouponStackOperations(operations)

    print('\n'.join(map(str, result)))
