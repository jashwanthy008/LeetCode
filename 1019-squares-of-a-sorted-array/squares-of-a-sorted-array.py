class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nu=[]
        for i in range(len(nums)):
            soo=nums[i]*nums[i]
            nu.append(soo)
        ni=sorted(nu)
        return ni