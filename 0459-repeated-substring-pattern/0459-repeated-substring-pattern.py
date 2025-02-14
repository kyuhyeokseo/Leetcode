class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        L = len(s)
        target = s[0]

        for i in range(1, L):
            if s[i] == target and (i * (L//i) == L) and (s[:i] * (L//i) == s):
                return True
        return False