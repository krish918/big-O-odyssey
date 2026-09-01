#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maximizeNonOverlappingMeetings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY meetings as parameter.
#

def maximizeNonOverlappingMeetings(meetings) -> int:
    # sort meetings based on ending time
    non_overlapping_count: int = 0
    if len(meetings) == 0 or len(meetings[0]) == 0:
        return non_overlapping_count
         
    sorted_meetings: list[list] = sorted(meetings, key = lambda x: x[-1])
    
    # as we have no attended meeting, and we want start a new meeting at a time or after a time
    # when last meeting ended - we initialize last_meeting_endtime as first meeting's start time.
    last_meeting_endtime: int = sorted_meetings[0][0] 
    
    for curr_meeting in sorted_meetings:
        if curr_meeting[0] >= last_meeting_endtime:
            non_overlapping_count = non_overlapping_count + 1
            last_meeting_endtime = curr_meeting[-1]
            
    return non_overlapping_count


"""
approach : we will get greedy

- start by sorting all the items in meeting based on end time (Ascending).
    this will bring the earliest ending meeting at the top.
- we will select the first meeting and look for next meeting which starts when the
    first meeeting (i.e. earliest ending meeting) ends.
- we keep repeating this - so this way, we end up choosing all the shortest possible meeting
    which are not overlapping in a greedy fashion.
- this should give our final count of meetings  which are not overlapping and choosing always the meeting
    with shortest intervals or earliest endings in ascending order ensures that we end up choosing maximum of them.
    
# Common Mistakes

- Look for the condition you put for matching the current_meeting start time with last meetings end time. Even if the cuurent meeting start time is not exactly equal last meeting end time, this current_meeting could be a valid meeting and should be counted. think about it.

- Hint: only when the current meeting start time is behind the last meeting end time - would a unfavorable case here.
"""    
    
    
if __name__ == '__main__':
    meetings_rows = int(input().strip())
    meetings_columns = int(input().strip())

    meetings = []

    for _ in range(meetings_rows):
        meetings.append(list(map(int, input().rstrip().split())))

    result = maximizeNonOverlappingMeetings(meetings)

    print(result)
