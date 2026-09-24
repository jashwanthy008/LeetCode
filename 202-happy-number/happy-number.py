class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sett=set()
        while n!=1:
            if n in sett:
                return False
            sett.add(n)
            summ=0
            for i in str(n):
                summ+=int(i)*int(i)
            n=summ
        return True