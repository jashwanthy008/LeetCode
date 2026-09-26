class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        see=""
        for ch in s:
            if ch in see:
                return ch
            see+=ch
            
        