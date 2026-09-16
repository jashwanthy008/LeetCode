class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        di={}
        for i in range(len(nums)):
            di[nums[i]]=di.get(nums[i],0)+1
        for j in di:
            if di[j]==1:
                return j