class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        len_nums=len(nums)
        rotation=k%len_nums
        if rotation == 0 :
            return 
        nums[:]=nums[-rotation:]+nums[:-rotation]
        
        