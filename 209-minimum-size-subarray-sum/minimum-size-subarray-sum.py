class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        low=0
        summ=0
        min_len=float('inf')

        for right in range(len(nums)):
            summ+=nums[right]


            while summ>=target:
                min_len=min(min_len,right-low+1)
                summ-=nums[low]
                low+=1
        return 0 if min_len==float('inf') else min_len