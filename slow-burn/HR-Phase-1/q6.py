#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findFirstOccurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def findFirstOccurrence(nums, target):
    # Write your code here
    first = 0
    last = len(nums) -1 
    
    while first <= last:
        mid = (first + last) // 2
        if nums[mid] == target:
            # We found the traget but not necessarily the first ocurrance.
            # If this is the first element of array or any element before it is not the target, we found 1st ocurrance.
            # Otherwise, we keep searching in the part of array left to this ocurrance. 
            if mid == 0 or nums[mid-1] != target:
                return mid
            else:
                last = mid - 1
        elif nums[mid] > target:
            last = mid - 1 
        else:
            first = mid + 1
    
    return -1
    
"""
## Non-Optimal Way:

We can simply apply binary search and once an element is found, we start going left, until we stop finding duplicates.
The index of last such element would be the answer. 

But with an array containing lots of duplicates, in worst case this could easily go O(n). (While binary search should be O(log n)).

"""

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = findFirstOccurrence(nums, target)

    print(result)
