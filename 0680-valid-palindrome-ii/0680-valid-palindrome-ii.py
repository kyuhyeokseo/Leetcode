class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        cnt = 0
        i, j = 0, len(s)-1

        while i<j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                cnt += 1
                break
        
        if cnt == 0:
            return True
        else:
            A, B = s[:i]+s[i+1:], s[:j]+s[j+1:]
            return (A == A[::-1]) or (B == B[::-1])