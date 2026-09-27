class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ze=0
        on=0
        tw=0


        for i in nums:
            if i == 0:
                ze+=1
            elif i == 1:
                on+=1
            else:
                tw+=1
        
        nums[:] = [0]*ze + [1]*on + [2]*tw
        return nums