class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        chk = 0
        
        for i in range(len(s)):
            chk ^= (ord(s[i]) - ord('a') + 1)
        
        for i in range(len(t)):
            chk ^= (ord(t[i]) - ord('a') + 1)
        
        ans = chr(chk + ord('a') - 1)
        return ans
        
        
        
        
        