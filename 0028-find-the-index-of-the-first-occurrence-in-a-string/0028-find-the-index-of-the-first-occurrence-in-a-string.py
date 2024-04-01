class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        for idx in range(len(haystack) - len(needle) + 1) :
            tmp = haystack[idx:idx+len(needle)]
            if tmp == needle :
                return idx
        
        return -1
        
        
        
        
        
        
        