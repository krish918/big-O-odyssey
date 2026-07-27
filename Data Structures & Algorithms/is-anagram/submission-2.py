class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_store: dict = {}
        # Traverse the first string and keep storing its char occurrances
        for char in s:
            char_store[char] = char_store.get(char, False) + 1
            
        # Traverse the second string and m check if each character in t
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