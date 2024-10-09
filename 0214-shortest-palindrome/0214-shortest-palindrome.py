class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        L = len(s)
        
        if L == 1 or L == 0 :
            return s
        
        if s == s[::-1] :
            return s
        
        S = s[:-1]
        T = s[-1]
        for i in range(L-1, 0, -1):
            if S == S[::-1] :
                out = T[::-1] + s
                return out
            S = S[:-1]
            T = s[i-1]+T