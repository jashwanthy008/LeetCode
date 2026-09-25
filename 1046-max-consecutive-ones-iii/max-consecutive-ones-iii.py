class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        zerocout=0
        max_size=0

        for right in range(len(nums)):
            if nums[right]==0:
                zerocout+=1
            while zerocout>k:
                if nums[left]==0:
                    zerocout-=1
                left+=1
            max_size=max(max_size,right - left +1)
        return max_size
