class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        L1 = len(s)
        L2 = len(t)
        i = 0
        
        for j in range(L2) :
            if i == L1 :
                return True
            if s[i] == t[j] :
                i+=1
            
        if i == L1 :
            return True
        else :
            return False
        
        
        
        
        
        