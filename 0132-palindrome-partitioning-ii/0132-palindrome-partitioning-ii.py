class Solution:
    def minCut(self, s: str) -> int:
        
        out = len(s)-1
        
        dp = [i-1 for i in range(len(s)+1)]
        
        for i in range(1, len(s)+1):
            for j in range(0, i):
                
                if s[j:i] == s[j:i][::-1] :
                    dp[i] = min(dp[i], dp[j]+1)
                    
                    #print(i,j, dp)
        
        return dp[-1]
        
                
        
        
        
        
        
        