class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        summ=0
        min_len=float('inf')

        for right in range(len(nums)):
            summ+=nums[right]


            while summ>=target:
                min_len=min(min_len,right-left+1)
                summ-=nums[left]
                left+=1
        return 0 if min_len==float('inf') else min_len

