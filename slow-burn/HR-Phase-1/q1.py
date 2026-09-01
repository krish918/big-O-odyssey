#!/bin/python3

# DOAs
# 1: 

import math
import os
import random
import re
import sys

#
# Complete the 'countResponseTimeRegressions' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.
#

def countResponseTimeRegressions(responseTimes):
    prev_sum = 0
    answer = 0
    if len(responseTimes) < 2:
        return answer
         
    for i in range(1, len(responseTimes)):
        avg_ptr = i-1
        curr_ptr = i  # gives the number with which avg of all previous elements would be compared 
        
        prev_sum = prev_sum + responseTimes[avg_ptr] 
        # the average of all previous elements
        average = prev_sum/curr_ptr
        
        if responseTimes[curr_ptr] > average:
            answer = answer + 1
            
    return answer
            
        
    
"""
100 200 300 400 
    ^   ^^
i = 0
avg_ptr = i
curr_ptr = i+1

prev_sum = 0
answer = 0
num_elem = avg_ptr + 1
avg --> 100
avg = (prev_sum + arr[avg_ptr])/num_elem

if arr[curr_ptr] > avg; then answer++ 

"""
        

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
