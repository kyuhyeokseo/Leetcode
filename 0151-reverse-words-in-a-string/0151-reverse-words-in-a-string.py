class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        tmp = s.split()
        tmp.reverse()
        result = (' ').join(tmp)
        
        return result
        
        
        
        
        
        
        
        
        