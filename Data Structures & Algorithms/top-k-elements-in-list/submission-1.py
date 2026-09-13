"""
Naive Solution
O(n + n logn) = O (n logn)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count: dict[int, int] = {}

        # Put each num's frequencies in corresponding num as the key in the hashtable 
        for num in nums:
            freq_count[num] = freq_count.get(num, 0) + 1
        
        # Sorting on the basis of key in dict which is freq of different items in array
        sorted_freq = sorted(freq_count.items(), key=lambda n : n[-1], reverse=True)

        # Getting a new list of the top k nums only from the list of num, freq pairs.
        result = [num for num, freq in sorted_freq][:k]
        return result


        