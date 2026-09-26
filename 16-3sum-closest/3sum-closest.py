class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums=sorted(nums)
        closest_sum=nums[0]+nums[1]+nums[2]

        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1

            while j<k:
                current_sum=nums[i]+nums[j]+nums[k]
                if current_sum==target:
                    return current_sum
                
                if abs(current_sum-target)<abs(closest_sum-target):
                    closest_sum=current_sum
                
                if current_sum<target:
                    j+=1
                else:
                    k-=1
        return closest_sum
                    