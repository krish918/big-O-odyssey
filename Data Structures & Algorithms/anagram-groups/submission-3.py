"""
Naive Solution
O(m * nlogn)
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Sort each string, make them keys of a hashmap.
        # All anagrams map to same key after sorting.
        result: dict[str,list[str]] = {}
        for str in strs:
            sorted_str: str = ''.join(sorted(str))
            group = result.get(sorted_str, [])
            group.append(str)
            result[sorted_str] = group
        
        return list(result.values())

        