class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a list of tuples with indices as first item in tuple
        # Then, we sort them on the basis of 2nd item in tuple which is actual nums.
        sorted_nums = sorted(list(enumerate(nums)), key = lambda x: x[-1])
        
        """
        Now, we take the following approach for the new list, focusing only on the
        2nd item of the each tuple in list. (This is because, this is where our actual
        values from given list are present. 1st item of each tuple is the index of each
        item in original list.)
        """
        # Let's greedily look for largest and smallest item -> if they add upto required
        # sum. If not, 
        # if less than required sum -> 
        #   proceed further (increment list index) from the smaller item side.
        # if more than the required sum ->
        #   proceed back (decrement list index) from the larger item side.

        """
        the caveat: there is no assumption that list should be sorted.
        But the technique can be applied only to sorted list.
        Once we sort, the items move within the array, but we need to return the index
        from the original array.
        This is the caveat we handle by putting the converting the list into an enumerated
        list, and then sorting it only on the basis of values and not the index.
        """

        i = 0
        j = len(nums) - 1
        while i <= j:
            sum = sorted_nums[i][-1] + sorted_nums[j][-1]
            if sum == target:
                if sorted_nums[i][0] > sorted_nums[j][0]:
                    result = [sorted_nums[j][0], sorted_nums[i][0]]
                else:
                    result = [sorted_nums[i][0], sorted_nums[j][0]]
                return result
            elif sum < target:
                i += 1
            elif sum > target:
                j -= 1
        
        return []
        


        