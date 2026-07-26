class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_store: dict = {}   # A dict to keep count of a seen chars in first string
        
        # Traverse the first string and keep storing its char occurrances
        for char in s:
            if char in char_store: 
                char_store[char] += 1
            else:
                char_store[char] = 1
        
        # Traverse the second string and check if each character in t
        # is present in s with correct frequency.
        for char in t:
            if char not in char_store:
                return False
            else:
                char_store[char] -= 1
                if char_store[char] == 0:
                    del char_store[char]
        
        if char_store:
            return False
        else:
            return True