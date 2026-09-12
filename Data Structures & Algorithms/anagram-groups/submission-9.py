"""
O(m * n) Solution
"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Create a list of all non-capital letters
        alphabets: list[str] = [chr(i) for i in range(97,123)]
        result: dict[str,List[str]] = {}

        for st in strs:
            alpha_map: dict[str, int] = dict.fromkeys(alphabets, 0)
            for char in st:
                alpha_map[char] = alpha_map.get(char, 0) + 1 

            # Get the alphabet (key) and the corresponding freq (value) from the map
            # and prepare a unique string for freq for each alphabet
            freq_key = "".join([str(k) + str(v) for k, v in alpha_map.items()])

            # Add the current string to the array contained as a value by the freq_key
            # in the results hashtable; it will be common key for all anagrams
            result[freq_key] = result.get(freq_key, []) + [st]

        return list(result.values())