class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev_num=0
        num=x

        while num>0:
            las=num%10
            rev_num=rev_num*10+las
            num=num//10
        
        if x == rev_num:
            return True
        else:
            return False

        