#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'binarySearch' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def binarySearch(nums, target):
    first = 0
    last = len(nums) - 1
    while not first > last:
        mid = (first + last)//2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            last = mid - 1
        elif target > nums[mid]:
            first = mid + 1
            
    return -1
    
"""
As input is sorted: we will take the middle element and see if the item is less than or greater
If it is less than mid --> then mid is our new last element.
                           else mid is our new first element.
                           
The Caveat: We choose mid as our new last element --> why? we already know item at mid is not the target.
            Also, we might get caught in never ending search if item is not present in array.
            Also, what will be the loop elimination condition once we,  are not able to find the item.
            We might not be even able to find the item which is present, if we choose the last element as mid or first element as mid.
            
            |   |   |
            | 4 | 8 |
            |   |   |
            
            If we try to find 4 in above array:  first mid = 0+1//2 = 1
            as nums[1] is 8 > 4;  we do last = mid, i.e. last = 1.
            But earlier as well last was 1 only, hence we get caught in never ending loop.
            
            Hence, always update last as mid - 1 (as we already know target is not at mid)
                   always update first as mid + 1
                   
Another Issue: Elimination condition

If we put the condition to end loop as first < last, there
are cases where first and last are equal, and it is pretty valid case.
Hence, actual condition should be - while first is not greater than last.

"""

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = binarySearch(nums, target)

    print(result)
