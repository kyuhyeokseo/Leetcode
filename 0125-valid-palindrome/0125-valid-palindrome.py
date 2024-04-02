class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        target = ""
        for idx in range(len(s)) :
            if 'A' <= s[idx] <= 'Z':
                target += s[idx].lower()
            elif 'a' <= s[idx] <= 'z' :
                target += s[idx]
            elif '0' <= s[idx] <= '9' :
                target += s[idx]
        
        L = len(target)
        
        if L == 0:
            return True
        
        for idx in range(L) :
            if target[idx] != target[L-1-idx] :
                return False
        
        return True
        
        
        
        
        
        
        
        