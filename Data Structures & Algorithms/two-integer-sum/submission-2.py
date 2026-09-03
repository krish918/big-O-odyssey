class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_map = dict(sorted(enumerate(nums), key = lambda x: x[-1]))
        values = list(sorted_map.values())
        
        i = 0
        j = len(nums) - 1
        while i <= j:
            sum = values[i] + values[j]
            if sum == target:
                index = list(sorted_map.keys())
                if index[i] < index[j]:
                    return [index[i], index[j]]
                else:
                    return [index[j], index[i]]
            elif sum < target:
                i += 1
            elif sum > target:
                j -= 1
        
        return []
        


        