class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1=[]
        num2=[]
        num3=[]

        for i in range(len(nums)):
            if nums[i]<0:
                num1.append(nums[i])
            else:
                num2.append(nums[i])
        for i in range(len(num1)):
            num1[i]=num1[i]*num1[i]
        for j in range(len(num2)):
            num2[j]=num2[j]*num2[j]
        num1=num1[::-1]
        left=0
        right=0

        while left<len(num1) and right<len(num2):
            i=num1[left]
            j=num2[right]
            if i<j:
                num3.append(i)
                left+=1
            else:
                num3.append(j)
                right+=1

        while left<len(num1):
            num3.append(num1[left])
            left+=1

        while right<len(num2):
            num3.append(num2[right])
            right+=1
        
        return num3