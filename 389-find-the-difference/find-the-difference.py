class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        di={}

        for i in range(len(s)):
            di[s[i]]=di.get(s[i],0)+1
        for j in t:
            if j not in di or di[j]==0:
                return j
            di[j]-=1 
            
