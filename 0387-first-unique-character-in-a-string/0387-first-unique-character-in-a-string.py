class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        MAX = 100001
        D = {}
        L = len(s)
        
        for i in range(L) :
            if s[i] in D :
                D[s[i]] = MAX
            else :
                D[s[i]] = i
        
        ans = MAX
        for k in D.keys():
            ans = min(D[k], ans)
            
        if ans == MAX:
            return -1
        return ans
        
        
        
        
        
        