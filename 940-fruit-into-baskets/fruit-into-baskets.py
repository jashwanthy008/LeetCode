class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left=0
        di={}
        max_len=-1

        for right in range(len(fruits)):
            di[fruits[right]]=di.get(fruits[right],0)+1

            while len(di)>2:
                di[fruits[left]]-=1

                if di[fruits[left]]==0:
                    del di[fruits[left]]
                left+=1
            

            max_len=max(max_len,right - left +1)
        return max_len