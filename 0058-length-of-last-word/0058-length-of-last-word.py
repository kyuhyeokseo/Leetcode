class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = s.split()
        return len(tmp[-1])
        
        
        
        
        
        
        
        