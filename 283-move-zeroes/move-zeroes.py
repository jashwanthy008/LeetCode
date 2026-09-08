class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zeros=[num for num in nums if num!=0]
        zero=len(nums)-len(non_zeros)
        result=non_zeros+[0]*zero

        for i in range(len(nums)):
            nums[i]=result[i]
            