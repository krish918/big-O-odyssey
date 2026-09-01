#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def swap_nums_at_index(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] =  temp

def findSmallestMissingPositive(orderNumbers):
    ans = 1
    i = 0
    total_orders = len(orderNumbers)
    while i < total_orders:
        order_num = orderNumbers[i]
        if order_num > 0 and order_num < total_orders and i+1 != order_num and orderNumbers[i] != orderNumbers[order_num-1]:
            # last condition is needed - to not try to swap if both nums are same - duplicate items
            swap_nums_at_index(orderNumbers, i, order_num-1)
        else:
            i = i + 1
    
    for i in range(len(orderNumbers)):
        if i+1 == orderNumbers[i]:
            ans = ans + 1
        else:
            break
    return ans
         
                
    
"""

Smallest +ve integers : 1,2,3,4,5,6,7 .. 1000, 1001 .... +inf

Sample input 1 (worst case): 1 2 3 4 5 6 7 .... 789 ... 900 .. 999 999 
ans: 1000
Sample input 2:  8976 63788 1900092 2 4 -1 6 10 2000 1001 10 -89 30 1 3
processed array: 
    1st pass:
        replacing/swapping the 2000 elements of the array : if number at index i is not i+1 and 0 < i < 1000
        1: 1 2 3 4 63788 6 -1 1001 2000 10 10 -89 0 8976 1900092 11 .... 30
    2nd pass:
        look for the first index which does not have the integer equal to its index (i+1)
ans: 5
sample inpt 3: 823203 734839 4583829292 263268193 503503532 923492
ans: 1

"""

if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
