class Solution:
    def insert_unique_num(self, hashtable: List[int], table_idx: int, num: int, table_len: int) -> bool:
        # Try to push the num into hashtable only if it is not present or the hashtable entry is None
        # for the index where the num should land.
        while hashtable[table_idx] is not None:
            if hashtable[table_idx] == num:
                return False
            else:
                table_idx = (table_idx + 1) % table_len

        hashtable[table_idx] = num
        return True


    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_length: int = len(nums)
        nums_table : List[int | None] = [None] * nums_length
        for idx in range(nums_length):
            # Get the target index in the hashtable for current integer in original list
            table_idx = nums[idx] % nums_length
            
            # If not able to put distinct items in hashtable that means duplicate insert was attempted
            if not self.insert_unique_num(nums_table, table_idx, nums[idx], nums_length):
                return True
        
        return False