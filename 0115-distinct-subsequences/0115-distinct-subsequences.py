class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        L1 = len(s)
        L2 = len(t)
        
        dp = [[0 for _ in range(L1+1)] for _ in range(L2+1)]
        
        for x in range(0, L1+1):
            dp[0][x] = 1
        
        for j in range(1,L2+1):
            
            target = t[j-1]
            
            for i in range(1, L1+1):
                
                if target == s[i-1]:
                    dp[j][i] = dp[j][i-1] + dp[j-1][i-1]
                else :
                    dp[j][i] = dp[j][i-1]
               
        #for item in dp :
        #    print(item)
            
        return dp[-1][-1]
        
        
        
        
        
        