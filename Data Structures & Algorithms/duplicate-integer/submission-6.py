class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list.sort(nums)
        prev_num : int | None = None
        for num in nums:
            if num == prev_num:
                return True
            prev_num = num
        return False
