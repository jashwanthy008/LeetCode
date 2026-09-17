class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        di = {}
        # Step 1: Build the dictionary, but map the number to its index instead of counting it
        for i in range(len(nums)):
            di[nums[i]] = i 
        
        # Step 2: Loop through and look for the complement
        for i in range(len(nums)):
            summ = target - nums[i]
            
            # Check if the complement exists AND ensure it's not the exact same element reused
            if summ in di and di[summ] != i:
                return [i, di[summ]]
        
            