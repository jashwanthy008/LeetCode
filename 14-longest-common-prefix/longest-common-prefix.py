class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        first=strs[0]
        last=strs[-1]
        minlen=min(len(first),len(last))
        i=0

        while i < minlen and first[i]==last[i]:
            i+=1
        return first[:i]