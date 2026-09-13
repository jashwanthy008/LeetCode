class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nu=[]
        num_se=set(nums)

        for i in range(1,len(nums)+1):
            if i not in num_se:
                nu.append(i)
    


        return nu