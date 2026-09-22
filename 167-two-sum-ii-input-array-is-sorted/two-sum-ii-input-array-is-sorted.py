class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(numbers)-1
        fou=False
        nums=[]

        while left<right:
            i=numbers[left]
            j=numbers[right]
            summ=i+j
            if summ==target:
                fuu=True
                nums.append(left+1)
                nums.append(right+1)
                return nums
            elif summ<target:
                left+=1
            else:
                right-=1
        return []
            
