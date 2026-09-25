class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left=0
        zerocount=0

        for right in range(len(nums)):
            if nums[right]==0:
                zerocount+=1
            if zerocount>k:
                if nums[left]==0:
                    zerocount-=1
                left+=1
        return len(nums)-left

