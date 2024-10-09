class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        L = len(s)
        
        if L == 1 or L == 0 :
            return s
        
        if s == s[::-1] :
            return s
        
        for i in range(L-1, 0, -1):
            if s[:i] == s[:i][::-1] :
                out = s[i:][::-1] + s
                return out